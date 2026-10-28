#!/usr/bin/env python3
"""Validate repository data without executing submission files. Standard library only."""
import argparse
import datetime as dt
import json
import math
from pathlib import Path, PurePosixPath
import re
import sys

MAX_FILE = 1_000_000
MAX_TOTAL = 15_000_000
MAX_FILES = 1500
ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]{0,79}$")
REV = re.compile(r"^[0-9a-f]{40}(?:[0-9a-f]{24})?$")
SECRET = re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)")
REQUIRED = ["README.md", "AGENTS.md", "CONTRIBUTING.md", "GOVERNANCE.md", "SECURITY.md", "LICENSE", ".github/CODEOWNERS",
            ".github/workflows/policy.yml", ".github/workflows/checks.yml",
            "tools/validate.py", "tools/trusted_policy.py", "tools/render.py",
            "data/roles.json", "data/platforms.json", "data/capabilities.json", "data/tasks.json", "data/sources.json", "data/devices.json"]

class Invalid(ValueError):
    pass

def need(ok, message):
    if not ok:
        raise Invalid(message)

def safe_path(name):
    need(isinstance(name, str) and name and len(name) <= 240, "invalid path length/type")
    p = PurePosixPath(name)
    need(not p.is_absolute() and all(x not in ("", ".", "..") for x in name.split("/")),
         "unsafe relative path")
    need("\\" not in name and "\x00" not in name and not any(ord(c) < 32 for c in name),
         "unsafe path character")
    need(name.split("/")[0] != ".git", "git metadata forbidden")
    return p

def text(value, label):
    need(isinstance(value, str) and bool(value.strip()) and len(value) <= 20000, label + " must be nonempty text")

def fields(obj, keys, label):
    need(isinstance(obj, dict), label + " must be an object")
    need(set(keys) <= obj.keys(), label + " missing fields: " + ", ".join(sorted(set(keys)-obj.keys())))

def person(v, label, nullable=True):
    if nullable and v is None:
        return
    need(isinstance(v, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}", v), label + " must be a GitHub login or null")

def sequence(v, label):
    need(isinstance(v, list), label + " must be an array")
    return v

def timestamp(v, label):
    text(v, label)
    try:
        value = dt.datetime.fromisoformat(v.replace("Z", "+00:00"))
    except ValueError as exc:
        raise Invalid(label + " is not ISO time") from exc
    need(value.tzinfo is not None, label + " must have timezone")
    return value

def read_json(p):
    try:
        def pairs(entries):
            out = {}
            for k, v in entries:
                need(k not in out, "duplicate JSON key")
                out[k] = v
            return out
        return json.loads(p.read_text(encoding="utf-8"), object_pairs_hook=pairs,
                          parse_constant=lambda x: (_ for _ in ()).throw(Invalid("nonfinite JSON number")))
    except (ValueError, UnicodeError, RecursionError) as exc:
        raise Invalid("invalid JSON: " + p.name + ": " + str(exc)) from exc

def index(rows, label):
    sequence(rows, label)
    need(0 < len(rows) <= 500, label + " empty or excessive")
    out = {}
    for row in rows:
        fields(row, ["id"], label)
        need(isinstance(row["id"], str) and ID.fullmatch(row["id"]), label + " invalid id")
        need(row["id"] not in out, label + " duplicate id")
        out[row["id"]] = row
    return out

def validate_evidence(e, profiles, capabilities, now=None):
    fields(e, ["id","profile","capability","kind","status","scenario","revision","hardware","os_build",
               "provider_version","operator","reviewer","tested_at","expires_at","procedure","expected",
               "observed","artifacts","limitations"], "evidence")
    need(isinstance(e["id"], str) and ID.fullmatch(e["id"]), "invalid evidence id")
    need(e["profile"] in profiles and e["capability"] in capabilities, "unknown evidence target")
    need(e["kind"] in ("source","replay","emulator","physical"), "invalid evidence kind")
    need(e["status"] in ("not-tested","observed","failed","verified"), "invalid evidence status")
    text(e["scenario"], "scenario")
    for key in ("procedure","artifacts","limitations"):
        sequence(e[key], key)
    for key in ("operator","reviewer"):
        person(e[key], key)
    if e["status"] == "not-tested":
        need(e["observed"] is None and e["tested_at"] is None, "unrun evidence cannot claim observation/time")
        return
    need(isinstance(e["revision"], str) and REV.fullmatch(e["revision"]), "evidence revision must be full commit/digest")
    person(e["operator"], "operator", False)
    measured = timestamp(e["tested_at"], "tested_at")
    now = now or dt.datetime.now(dt.timezone.utc)
    need(measured <= now + dt.timedelta(minutes=5), "future test timestamp")
    need(e["procedure"] and e["artifacts"], "observed evidence requires procedure and artifacts")
    for p in e["procedure"]:
        text(p, "procedure step")
    text(e["expected"], "expected")
    text(e["observed"], "observed")
    for a in e["artifacts"]:
        fields(a, ["url","sha256","description"], "artifact")
        need(isinstance(a["url"], str) and a["url"].startswith("https://") and len(a["url"]) < 2048,
             "artifact needs HTTPS URL")
        need(isinstance(a["sha256"], str) and re.fullmatch("[0-9a-f]{64}", a["sha256"]), "artifact needs SHA-256")
        text(a["description"], "artifact description")
    if e["kind"] == "physical":
        text(e["hardware"], "hardware")
        text(e["os_build"], "os_build")
        profile = profiles[e["profile"]]
        need(profile.get("device_id") is not None, "physical evidence needs an exact device link")
        need(profile.get("hardware") == e["hardware"] and profile.get("os_build") == e["os_build"],
             "physical evidence must match its hardware/OS configuration")
    if e["status"] == "verified":
        need(e["kind"] == "physical", "only physical observation certifies device support")
        profile = profiles[e["profile"]]
        need(profile.get("hardware") == e["hardware"] and profile.get("os_build") == e["os_build"],
             "verified evidence needs an exact matching hardware/OS profile, not a candidate group")
        text((profile.get("configuration") or {}).get("model_identifier"), "verified model identifier")
        person(e["reviewer"], "reviewer", False)
        need(e["operator"].lower() != e["reviewer"].lower(), "reviewer must be independent")
        expiry = timestamp(e["expires_at"], "expires_at")
        need(expiry > measured, "expiry must follow observation")
    elif e["expires_at"] is not None:
        timestamp(e["expires_at"], "expires_at")

def validate_receipt(r, tasks):
    keys = ["task","base_revision","operator","agent_tool","model","cap_minutes","cap_cost","currency",
            "elapsed_minutes","input_tokens","cached_tokens","output_tokens","cost","cost_kind","cost_method",
            "commands","tests_not_run","failures","artifacts","limitations"]
    fields(r, keys, "receipt")
    need(r["task"] in tasks, "unknown receipt task")
    for k in ("cap_minutes","cap_cost","elapsed_minutes","input_tokens","cached_tokens","output_tokens","cost"):
        v = r[k]
        need(v is None or (isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) and v >= 0),
             k + " must be nonnegative measurement or null")
    need(r["cost_kind"] in ("unknown","measured","estimated"), "invalid cost kind")
    if r["cost_kind"] == "unknown":
        need(r["cost"] is None, "unknown cost must be null")
    else:
        need(r["cost"] is not None, "known cost missing")
        text(r["currency"], "currency")
        if r["cost_kind"] == "estimated":
            text(r["cost_method"], "cost_method")
    if r["base_revision"] is not None:
        need(isinstance(r["base_revision"],str) and REV.fullmatch(r["base_revision"]), "invalid base revision")
    person(r["operator"], "operator")
    for k in ("commands","tests_not_run","failures","artifacts","limitations"):
        sequence(r[k], k)

CONFIGURATION_FIELDS = ("model_identifier", "soc", "gpu", "ram_gib", "storage_gib", "kernel",
                        "firmware", "browser", "location_provider", "power_settings")

def validate_devices(devices, profiles):
    known_identifiers = set()
    for d in devices.values():
        fields(d, ["family", "manufacturer", "model", "identity", "aliases", "model_identifiers",
                   "soc", "sources", "notes"], "device")
        need(d["family"] in ("desktop", "laptop", "tablet", "phone"), "invalid device family")
        need(d["identity"] in ("model", "placeholder"), "invalid device identity")
        for key in ("model", "notes"): text(d[key], key)
        for key in ("manufacturer", "soc"):
            if d[key] is not None: text(d[key], key)
        for key in ("aliases", "model_identifiers", "sources"):
            for item in sequence(d[key], key): text(item, key)
        need(all(u.startswith("https://") for u in d["sources"]), "device sources require HTTPS")
        if d["identity"] == "placeholder":
            need(not d["model_identifiers"], "placeholder cannot assert a model identifier")
        for ident in d["model_identifiers"]:
            key = (d["manufacturer"], ident.casefold())
            need(key not in known_identifiers, "model identifier belongs to multiple devices")
            known_identifiers.add(key)
    for p in profiles.values():
        fields(p, ["device_id", "configuration"], "platform")
        if p["device_id"] is None:
            need(p["configuration"] is None, "broad candidate cannot carry an exact configuration")
            continue
        need(p["device_id"] in devices, "unknown device reference")
        d = devices[p["device_id"]]
        need(d["identity"] == "model", "placeholder cannot be a tested configuration")
        need(p["family"] == d["family"], "configuration family differs from device")
        fields(p["configuration"], CONFIGURATION_FIELDS, "configuration")
        for key in CONFIGURATION_FIELDS:
            value = p["configuration"][key]
            if value is None: continue
            if key in ("ram_gib", "storage_gib"):
                need(isinstance(value, (int, float)) and not isinstance(value, bool) and
                     math.isfinite(value) and value > 0, key + " must be positive or null")
            else: text(value, key)
        ident = p["configuration"]["model_identifier"]
        if ident is not None and d["model_identifiers"]:
            need(ident in d["model_identifiers"], "configuration model identifier differs from device")

def validate(root):
    root = Path(root)
    total = 0
    paths = []
    # Do not traverse .git or interpreter caches; reject all other symlinks before reads.
    def walk(d):
        for p in d.iterdir():
            if p.name in (".git","__pycache__", ".venv"):
                continue
            rel = p.relative_to(root).as_posix()
            safe_path(rel)
            need(not p.is_symlink(), "symlink forbidden: " + rel)
            if p.is_dir():
                yield from walk(p)
            else:
                need(p.is_file(), "nonregular file: " + rel)
                yield p
    for p in walk(root):
        n = p.stat().st_size
        need(n <= MAX_FILE, "file too large: " + p.relative_to(root).as_posix())
        total += n; paths.append(p)
        need(len(paths) <= MAX_FILES and total <= MAX_TOTAL, "repository data exceeds budget")
        if p.suffix not in (".png",".jpg",".jpeg",".woff",".woff2",".webp"):
            try:
                body = p.read_text(encoding="utf-8")
            except UnicodeError as exc:
                raise Invalid("unexpected binary file: " + str(p.relative_to(root))) from exc
            need(not SECRET.search(body), "credential-shaped secret in " + p.relative_to(root).as_posix())
    for name in REQUIRED:
        need((root/name).is_file(), "required file missing: " + name)
    reg = {name: index(read_json(root/"data"/(name+".json")), name)
           for name in ("roles","platforms","capabilities","tasks","sources","devices")}
    validate_devices(reg["devices"], reg["platforms"])
    for r in reg["roles"].values():
        fields(r,["name","responsibility","authority","who","maintainers","status"],"role")
        for k in ("name","responsibility","authority","who"):text(r[k],k)
        for p in sequence(r["maintainers"],"maintainers"): person(p,"maintainer",False)
        need(r["status"] in ("vacant","staffed"), "invalid role status")
        need(bool(r["maintainers"]) == (r["status"]=="staffed"), "role staffing mismatch")
    for p in reg["platforms"].values():
        fields(p,["family","os_lane","arch","hardware_candidate","hardware","os_build","owner","status","blocker"],"platform")
        need(p["family"] in ("desktop","laptop","tablet","phone","all"),"invalid family")
        need(p["os_lane"] in ("linux-native","android-native","linux-guest","browser"),"invalid OS lane")
        need(p["status"]=="candidate","support comes from evidence, not a profile flag")
        person(p["owner"],"owner")
    for c in reg["capabilities"].values():
        fields(c,["name","acceptance","phase"],"capability")
        text(c["name"],"name");text(c["acceptance"],"acceptance")
        need(c["phase"] in ("P0","P1","P2","P3"),"invalid phase")
    for t in reg["tasks"].values():
        fields(t,["title","track","phase","depends_on","roles","scope","agent_suitability",
                  "owner","reviewer","state","packet","issue_url"],"task")
        text(t["title"],"task title")
        need(t["phase"] in ("P0","P1","P2","P3"),"invalid phase")
        need(t["state"] in ("unclaimed","claimed","in-progress","review","done","blocked"),"invalid work state")
        need(t["agent_suitability"] in ("suitable","assist","human-only"),"invalid agent suitability")
        for k in ("depends_on","roles","scope"): sequence(t[k],k)
        need(t["roles"] and t["scope"],"task needs roles and scope")
        need(all(x in reg["roles"] for x in t["roles"]),"unknown role")
        need(all(x in reg["tasks"] for x in t["depends_on"]),"unknown dependency")
        for s in t["scope"]: safe_path(s.rstrip("/"))
        safe_path(t["packet"])
        need((root/t["packet"]).is_file(),"missing task packet")
        for k in ("owner","reviewer"):person(t[k],k)
        if t["state"] in ("claimed","in-progress","review","done"):
            need(t["owner"] and t["reviewer"],"active task needs owner and reviewer")
            need(t["owner"].lower()!=t["reviewer"].lower(),"task self-review")
        if t["issue_url"] is not None:
            need(re.fullmatch(r"https://github.com/parker-brown-family/omarchy-community-maps/issues/[1-9][0-9]*",t["issue_url"]),
                 "invalid task issue URL")
    active, done = set(), set()
    def visit(i):
        need(i not in active,"task dependency cycle")
        if i in done:return
        active.add(i)
        for dep in reg["tasks"][i]["depends_on"]:visit(dep)
        active.remove(i);done.add(i)
    for i in reg["tasks"]:visit(i)
    for s in reg["sources"].values():
        fields(s,["url","license","decision","scope","checked_on"],"source")
        need(isinstance(s["url"],str) and s["url"].startswith("https://"),"source URL requires HTTPS")
    seen=set()
    for p in sorted((root/"evidence/records").glob("*.json")):
        e=read_json(p);validate_evidence(e,reg["platforms"],reg["capabilities"])
        need(e["id"] not in seen,"duplicate evidence id");seen.add(e["id"])
    for p in (root/"receipts").glob("*.json"):
        validate_receipt(read_json(p),reg["tasks"])
    return dict(files=len(paths),tasks=len(reg["tasks"]),profiles=len(reg["platforms"]),devices=len(reg["devices"]),
                capabilities=len(reg["capabilities"]),evidence=len(seen))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("root",nargs="?",default=str(Path(__file__).resolve().parents[1]))
    a=ap.parse_args()
    try: print(json.dumps(validate(Path(a.root)),sort_keys=True))
    except (Invalid,OSError,TypeError,KeyError,RecursionError) as exc:
        print("Validation failed: "+str(exc),file=sys.stderr);return 1
    return 0
if __name__=="__main__":sys.exit(main())
