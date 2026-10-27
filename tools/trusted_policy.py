#!/usr/bin/env python3
"""Protected-base checker: reads PR metadata and blobs; never executes proposed code."""
import base64
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import urllib.request

# Resolve only the validator beside this trusted script, never the submitted tree.
spec=importlib.util.spec_from_file_location("trusted_validator",Path(__file__).with_name("validate.py"))
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
SECTIONS=("Purpose","Proof","Tests","Security and privacy","Agent assistance","Provenance","Not tested")

def check_body(body,tasks):
    v.need(isinstance(body,str) and len(body)<=40000,"PR body absent or oversized")
    body=re.sub(r"<!--.*?-->","",body,flags=re.S)
    match=re.search(r"(?m)^Task: ([A-Z]+-[0-9]+)\s*$",body)
    v.need(match and match.group(1) in tasks,"PR must link one known Task: ID")
    for heading in SECTIONS:
        m=re.search(r"(?ms)^## "+re.escape(heading)+r"\s*\n(.*?)(?=^## |\Z)",body)
        content=m.group(1).strip() if m else ""
        v.need(len(content)>=20 and not re.search(r"(?i)\b(TODO|TBD|replace me|fill this)\b",content),
               "complete PR section: "+heading)
    return match.group(1)

def get_api(repo,endpoint,token):
    v.need(re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+",repo),"invalid repository")
    request=urllib.request.Request("https://api.github.com/repos/"+repo+"/"+endpoint,
        headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json",
                 "X-GitHub-Api-Version":"2022-11-28","User-Agent":"omarchy-community-maps-policy"})
    with urllib.request.urlopen(request,timeout=30) as response:
        raw=response.read(22_000_001)
        v.need(len(raw)<=22_000_000,"API response too large")
        return json.loads(raw)

def tree_entries(tree):
    v.need(tree.get("truncated") is False,"truncated tree cannot be validated")
    entries=tree.get("tree")
    v.need(isinstance(entries,list) and len(entries)<=v.MAX_FILES,"tree exceeds file budget")
    total=0;out=[];seen=set()
    for item in entries:
        v.safe_path(item["path"])
        v.need(item["path"] not in seen,"duplicate tree path");seen.add(item["path"])
        if item["type"]=="tree":
            v.need(item["mode"]=="040000","invalid tree mode");continue
        v.need(item["type"]=="blob" and item["mode"] in ("100644","100755"),
               "symlink/submodule/nonregular tree entry forbidden")
        size=item.get("size")
        v.need(isinstance(size,int) and 0<=size<=v.MAX_FILE,"blob too large or unknown")
        total+=size;v.need(total<=v.MAX_TOTAL,"snapshot exceeds byte budget")
        v.need(re.fullmatch("[0-9a-f]{40}",item["sha"]),"invalid blob SHA")
        out.append(item)
    return out

def main():
    event=json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    pr=event["pull_request"];repo=pr["head"]["repo"]["full_name"];sha=pr["head"]["sha"]
    v.need(re.fullmatch("[0-9a-f]{40}",sha),"invalid head SHA")
    token=os.environ["GH_TOKEN"]
    tree=get_api(repo,"git/trees/"+sha+"?recursive=1",token)
    entries=tree_entries(tree)
    with tempfile.TemporaryDirectory(prefix="ocm-policy-") as folder:
        root=Path(folder)
        for item in entries:
            blob=get_api(repo,"git/blobs/"+item["sha"],token)
            v.need(blob.get("encoding")=="base64","unexpected blob encoding")
            raw=base64.b64decode(blob["content"].replace("\n",""),validate=True)
            v.need(len(raw)==item["size"] and len(raw)<=v.MAX_FILE,"blob size mismatch")
            digest=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
            v.need(digest==item["sha"],"blob digest mismatch")
            path=root/item["path"];path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)
        summary=v.validate(root)
        tasks=v.index(v.read_json(Path(__file__).resolve().parent.parent/"data/tasks.json"),"trusted tasks")
        task=check_body(pr.get("body"),tasks)
        print(json.dumps({"head":sha,"task":task,"validation":summary,
                          "method":"protected-base policy, submission read only as data"},sort_keys=True))
    return 0

if __name__=="__main__":
    try: sys.exit(main())
    except Exception as exc:
        # Do not dump headers, environment or input blobs.
        print("Trusted policy failed: "+type(exc).__name__+": "+str(exc),file=sys.stderr)
        sys.exit(1)
