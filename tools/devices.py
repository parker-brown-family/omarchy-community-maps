#!/usr/bin/env python3
"""Look up models and preserve every configuration-specific evidence record."""
import argparse
import datetime as dt
from html import escape
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def load_registry(root):
    def read(path):
        return json.loads((root / path).read_text())
    return (read("data/devices.json"), read("data/platforms.json"),
            [dict(read(p.relative_to(root)), record_path=p.relative_to(root).as_posix())
             for p in sorted((root / "evidence/records").glob("*.json"))])

def evidence_state(record, as_of):
    if record["status"] == "verified":
        expiry = dt.datetime.fromisoformat(record["expires_at"].replace("Z", "+00:00"))
        if expiry <= as_of:
            return "stale"
    return record["status"]

def search(models, profiles, records, query, as_of):
    words = query.casefold().split()
    found = []
    exact = []
    for d in models:
        names = [d["id"], d["model"], *d["aliases"], *d["model_identifiers"]]
        haystack = " ".join(str(x) for x in [*names, d["manufacturer"], d["soc"], d["family"]] if x is not None).casefold()
        if not all(word in haystack for word in words):
            continue
        if query and query.casefold() in [name.casefold() for name in names]:
            exact.append(d["id"])
        configurations = []
        for p in profiles:
            if p.get("device_id") != d["id"]:
                continue
            observations = [dict(e, state_at_query=evidence_state(e, as_of))
                            for e in records if e["profile"] == p["id"]]
            configurations.append(dict(profile=p, observations=observations))
        found.append(dict(device=d, configurations=configurations,
                          observation_count=sum(len(p["observations"]) for p in configurations)))
    return dict(query=query, as_of=as_of.isoformat(), exact_matches=exact,
                matches=found, match_count=len(found),
                interpretation="Each record applies only to its model, configuration, capability and revision. No result means no evidence in this repository; support elsewhere is unknown.")

def render_page(root, as_of):
    data = search(*load_registry(root), "", as_of)
    h = lambda value: escape(str(value), quote=True)
    cards = []
    for entry in data["matches"]:
        d = entry["device"]
        configurations = []
        for item in entry["configurations"]:
            p = item["profile"]
            observations = []
            for e in item["observations"]:
                expiry = '' if e["expires_at"] is None else ' data-expires="'+h(e["expires_at"])+'"'
                observations.append('<li><a href="../'+h(e["record_path"])+'">'+h(e["capability"])+
                    '</a> · '+h(e["kind"])+ ' · <b data-status="'+h(e["status"])+ '"'+expiry+'>'+h(e["state_at_query"])+
                    '</b><p>'+h(e["observed"] if e["observed"] is not None else "No observation")+
                    '</p><small>Tested '+h(e["tested_at"])+ ' · app '+h(e["revision"])+
                    ' · operator '+h(e["operator"])+ ' · reviewer '+h(e["reviewer"] if e["reviewer"] else "unassigned")+
                    '</small></li>')
            facts = ''.join('<dt>'+h(k.replace('_', ' '))+'</dt><dd>'+h(v if v is not None else 'unknown')+'</dd>'
                            for k,v in p["configuration"].items())
            configurations.append('<details><summary>'+h(p["os_lane"])+ ' · '+h(p["os_build"] or "OS build unknown")+
                '</summary><p>'+h(p["hardware"] or "Hardware configuration pending")+'</p><dl>'+facts+
                '</dl><ul>'+''.join(observations)+'</ul>'+('' if observations else '<p>No observations recorded.</p>')+'</details>')
        names = ' '.join([d["id"], d["model"], *d["aliases"], *d["model_identifiers"], d["soc"] or '', d["manufacturer"] or ''])
        cards.append('<article class="device" id="'+h(d["id"])+ '" data-family="'+h(d["family"])+ '" data-search="'+h(names.casefold())+'">'+
            '<p class="tag">'+h(d["family"])+ ' · '+h(d["identity"])+ '</p><h2>'+h(d["model"])+ '</h2><p>'+h(d["notes"])+
            '</p><p class="status">'+('No observations recorded' if entry["observation_count"] == 0 else str(entry["observation_count"])+ ' records; inspect each configuration')+
            '</p><p class="small">Model identifiers: '+h(', '.join(d["model_identifiers"]) or 'not recorded')+'</p>'+''.join(configurations)+
            '<details><summary>Identify or test this device</summary><p>Registry key: <code>'+h(d["id"])+
            '</code>. Check the model identifier and OS before reusing any result.</p><p>'+(' · '.join('<a href="'+h(u)+'">Identity source</a>' for u in d["sources"]) or 'Identity source not recorded.')+
            '</p><a href="device-registry.md">Add a model, configuration or observation</a></details></article>')
    css = '''*{box-sizing:border-box}body{background:#091c25;color:#edf5e8;margin:0;font:17px/1.6 system-ui,sans-serif}main{max-width:1150px;padding:40px 24px 90px;margin:auto}h1{font-size:clamp(32px,6vw,58px);line-height:1.12}h2{font-size:23px;line-height:1.2}p{max-width:850px}a{color:#b3df89}input,select{background:#132f3c;color:inherit;padding:12px;border:1px solid #68858d;border-radius:8px;font:inherit;max-width:100%}.controls{display:flex;gap:16px;flex-wrap:wrap}input{flex:1;min-width:180px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,310px),1fr));gap:20px}.device{padding:24px;background:#102b37;border:1px solid #395965;border-radius:16px}.tag,.small,small{color:#abc0c8;font-size:13px}.status{color:#dfc087}.flow{display:flex;flex-wrap:wrap;gap:18px;padding:20px 0}.flow span{background:#193844;padding:14px 20px;border-radius:10px}.notice{border-left:4px solid #dfc087;padding:12px 20px;background:#292b26}details{margin:18px 0}summary{cursor:pointer}dl{font-size:14px;overflow-wrap:anywhere}dt{color:#a9bbc3}dd{margin:0 0 10px}li{margin:18px 0;overflow-wrap:anywhere}[hidden]{display:none!important}code{overflow-wrap:anywhere}'''
    script = '''const q=document.querySelector('#query'),f=document.querySelector('#family');function filter(){const words=q.value.toLowerCase().trim().split(/\\s+/).filter(Boolean);let n=0;document.querySelectorAll('.device').forEach(c=>{const show=(!f.value||f.value===c.dataset.family)&&words.every(w=>c.dataset.search.includes(w));c.hidden=!show;if(show)n++});document.querySelector('#count').textContent=n+' matching entries';document.querySelector('#missing').hidden=n!==0}q.addEventListener('input',filter);f.addEventListener('change',filter);q.value=new URLSearchParams(location.search).get('q')||'';document.querySelectorAll('[data-status="verified"][data-expires]').forEach(e=>{if(new Date(e.dataset.expires)<=new Date())e.textContent='stale'});filter();'''
    return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Device evidence · Omarchy Community Maps</title><style>'+css+'</style><body><main><p class="tag">OMARCHY COMMUNITY MAPS · DEVICE EVIDENCE</p><h1>Has anyone tested my device?</h1><p>Find your model, then compare its OS, hardware configuration and app revision with each recorded test. Anyone can propose another model. This starting list is open-ended.</p><p class="notice">A listed model is a place to collect evidence. It does not establish that Omarchy installs on it, or that Community Maps works. Future-device placeholders need identification before testing.</p><div class="flow" aria-label="Evidence applies to one model, configuration and test"><span>1 · Exact model / variant</span><span>2 · OS + hardware configuration</span><span>3 · Capability + app revision + proof</span></div><p><a href="device-registry.md">How to contribute a result</a> · <a href="contribution-map.html">Project work map</a> · <a href="../data/devices.json">Machine-readable manifest</a></p><p class="small">Data snapshot '+h(as_of.isoformat())+'. Every record is retained, including failures and older revisions. Expired verified records display as stale when this page opens. Run the CLI against the current repository for the latest records.</p><div class="controls"><input id="query" aria-label="Find a device" placeholder="Pixel 7 Pro, iPhone 13, M5, Mac17,3"><select id="family" aria-label="Device family"><option value="">All device families</option>'+''.join('<option>'+x+'</option>' for x in ('phone','tablet','laptop','desktop'))+'</select></div><p id="count" aria-live="polite"></p><p id="missing" hidden>No matching entry yet. <a href="device-registry.md">Add your exact model</a>; absence is not a failed test.</p><div class="grid">'+''.join(cards)+'</div></main><script>'+script+'</script></body></html>\n'

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--query', default='')
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()
    import validate
    try:
        validate.validate(ROOT)
        result = search(*load_registry(ROOT), args.query, dt.datetime.now(dt.timezone.utc))
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print('Registry lookup failed: '+str(exc), file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(result['interpretation'])
        for entry in result['matches']:
            print(entry['device']['id']+' — '+entry['device']['model']+' — '+str(entry['observation_count'])+' evidence records')
        if not result['matches']:
            print('No matching entry; add a model using docs/device-registry.md.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
