#!/usr/bin/env python3
"""Generate escaped, self-contained contribution views from canonical JSON."""
import argparse
import datetime as dt
from html import escape
import json
from pathlib import Path
import sys
import devices

ROOT=Path(__file__).resolve().parents[1]
def h(x):return escape(str(x),quote=True)
def load(root,name):return json.loads((root/"data"/(name+".json")).read_text())
def cell_status(records,profile,capability,as_of):
    matches=[e for e in records if e["profile"]==profile and e["capability"]==capability and e["tested_at"]]
    if not matches:return "not-tested",None
    e=max(matches,key=lambda x:x["tested_at"])
    status=e["status"]
    if status=="verified" and e["expires_at"][:10] < as_of:status="stale"
    return status,e
def outputs(root):
    roles=load(root,"roles");tasks=load(root,"tasks");ps=load(root,"platforms")
    caps=load(root,"capabilities");sources=load(root,"sources")
    project=json.loads((root/"data/project.json").read_text())
    records=[json.loads(p.read_text()) for p in sorted((root/"evidence/records").glob("*.json"))]
    as_of=project["as_of"]
    md=["# Work map","",f"Snapshot: {as_of}. Assignment and evidence are separate. All operational roles begin vacant.","",
        "[Interactive map](contribution-map.html) · [Support](support-matrix.md) · [Agent contract](agent-contract.md)",""]
    for phase in ("P0","P1","P2","P3"):
        md += ["## "+phase,"","| Task | Roles | Prerequisites | Agent work |","|---|---|---|---|"]
        for t in tasks:
            if t["phase"]==phase:
                md.append("| ["+t["id"]+" — "+t["title"]+"](../"+t["packet"]+") | "+", ".join(t["roles"])+" | "+(", ".join(t["depends_on"]) or "none")+" | "+t["agent_suitability"]+" |")
        md.append("")
    index=["# Task packets","", "Canonical registry: data/tasks.json. One task, one PR; claim requires maintainer acceptance.",""]
    for t in tasks:index.append("- ["+t["id"]+" — "+t["title"]+"]("+t["id"].lower()+".md)"+(" · [issue]("+t["issue_url"]+")" if t["issue_url"] else " · issue unlinked"))
    matrix=["# Support matrix","",f"Snapshot: {as_of}. Families are candidates. Verification belongs to exact hardware/OS/revision; see evidence records.","",
            "| Candidate | Family / lane / architecture | Evidence | Blocker |","|---|---|---|---|"]
    for p in ps:
        statuses=[cell_status(records,p["id"],c["id"],as_of)[0] for c in caps]
        result="No observations recorded" if all(s=="not-tested" for s in statuses) else ", ".join(c["id"]+": "+s for c,s in zip(caps,statuses) if s!="not-tested")
        matrix.append("| "+p["hardware_candidate"]+" | "+p["family"]+" / "+p["os_lane"]+" / "+p["arch"]+" | "+result+" | "+p["blocker"]+" |")
    matrix+=["","## Capabilities",""]
    matrix += ["- **"+c["name"]+"**: "+c["acceptance"] for c in caps]
    rolecards=[]
    for r in roles:
        count=sum(r["id"] in t["roles"] for t in tasks)
        rolecards.append('<article class="role"><h3>'+h(r["name"])+'</h3><p>'+h(r["responsibility"])+'</p><p class="muted">'+h(r["who"])+'</p><p><b>'+h(r["status"])+'</b> · '+str(count)+' tasks</p><button type="button" data-role="'+h(r["id"])+'">Show these tasks</button></article>')
    taskcards=[]
    for t in tasks:
        url="../"+t["packet"]
        taskcards.append('<article class="task" data-phase="'+h(t["phase"])+'" data-roles="'+h(" ".join(t["roles"]))+'"><div class="chips"><span>'+h(t["phase"])+'</span><span>'+h(t["agent_suitability"])+'</span><span>'+h(t["state"])+'</span></div><h3><a href="'+h(url)+'">'+h(t["title"])+'</a></h3><p class="muted">'+h(t["id"])+' · '+h(t["track"])+'</p><p>Roles: '+h(", ".join(t["roles"]))+'</p><p>Depends on: '+h(", ".join(t["depends_on"]) or "no other task")+'</p><p>Owner: '+h(t["owner"] or "unassigned")+' · Reviewer: '+h(t["reviewer"] or "unassigned")+'</p><details><summary>Allowed paths</summary><ul>'+''.join('<li>'+h(x)+'</li>' for x in t["scope"])+'</ul></details>'+(('<a class="button" href="'+h(t["issue_url"])+'">Open task issue</a>') if t["issue_url"] else '<span class="muted">Issue link pending</span>')+'</article>')
    rows=[]
    for p in ps:
        cells=[]
        for c in caps:
            status,e=cell_status(records,p["id"],c["id"],as_of)
            label={"not-tested":"?","verified":"✓","failed":"×","observed":"Obs","stale":"Old"}[status]
            title=c["name"]+": "+status
            if e: title += " · "+str(e["hardware"])+" · "+str(e["os_build"])+" · "+str(e["revision"])+" · "+str(e["tested_at"])
            inner=h(label) if e is None else '<a href="../evidence/records/'+h(e["_file"] if "_file" in e else next(q.name for q in (root/"evidence/records").glob("*.json") if json.loads(q.read_text())["id"]==e["id"]))+'" title="'+h(title)+'">'+h(label)+'</a>'
            cells.append('<td class="'+h(status)+'" title="'+h(title)+'">'+inner+'</td>')
        rows.append('<tr data-family="'+h(p["family"])+'"><th><strong>'+h(p["hardware_candidate"])+'</strong><small>'+h(p["os_lane"]+" · "+p["arch"])+'</small></th>'+''.join(cells)+'</tr>')
    sourceitems=''.join('<li><a href="'+h(s["url"])+'">'+h(s["id"])+'</a> — '+h(s["decision"])+' <small>'+h(s["license"])+'</small></li>' for s in sources)
    css="""*{box-sizing:border-box}body{margin:0;background:#10141d;color:#e3e8ef;font:16px/1.55 system-ui,sans-serif}header,main,footer{max-width:1240px;margin:auto;padding:32px 24px}header{padding-top:70px}h1{font-size:clamp(36px,6vw,68px);line-height:1.05;max-width:850px}h2{font-size:30px;margin-top:0}h3{font-size:19px;line-height:1.3}a{color:#a9d9ff}p{max-width:850px}.eyebrow{letter-spacing:.12em;text-transform:uppercase;color:#89d2bd;font-size:12px}.lede{font-size:22px}.muted,small{color:#a5b2c5}.notice{padding:18px 22px;border-left:4px solid #e7b971;background:#27241e}.stats,.path{display:flex;gap:14px;flex-wrap:wrap}.stat{flex:1;min-width:150px;background:#1a2431;padding:22px;border-radius:12px}.stat b{display:block;font-size:36px;color:#9fe3ce}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:16px}.role,.task{padding:24px;background:#1a2130;border:1px solid #303b50;border-radius:12px}.role p{font-size:14px}.task p{font-size:14px}section{margin:60px 0}.path>div{flex:1;min-width:180px;background:#182a30;padding:20px;border-radius:10px}.path b{display:block}.caption{font-size:13px;color:#a5b2c5}button,select,input,.button{background:#25364a;color:#edf4ff;border:1px solid #4f6684;border-radius:7px;padding:10px 14px;font:inherit}button{cursor:pointer}.controls{display:flex;gap:12px;flex-wrap:wrap;margin:20px 0}input{flex:1;min-width:200px}.chips{display:flex;gap:7px;flex-wrap:wrap;font-size:11px}.chips span{padding:3px 8px;border:1px solid #566277;border-radius:20px}.matrix{overflow:auto;border:1px solid #354257;border-radius:12px}table{border-collapse:collapse;width:100%;font-size:12px}th,td{padding:13px 10px;border-bottom:1px solid #303b50;text-align:center}thead th{background:#202a3b;min-width:80px}tbody th{min-width:280px;position:sticky;left:0;background:#17202e;text-align:left}th small{display:block}td.not-tested{color:#8795aa}td.verified{color:#93dfb2}td.failed{color:#ffa37d}td.observed,td.stale{color:#edc36b}details{margin:14px 0}summary{cursor:pointer}li{margin:10px 0}li small{display:block}.hide{display:none!important}footer{border-top:1px solid #334057}svg{width:100%;height:auto}figure{margin:22px 0}figcaption{font-size:13px;color:#a5b2c5}@media(max-width:600px){header,main,footer{padding:24px 16px}.stat{min-width:130px}h1{margin:22px 0}.grid{grid-template-columns:1fr}}"""
    body=f"""<header><div class="eyebrow">Independent community initiative · snapshot {h(as_of)}</div><h1>Omarchy Community Maps</h1><p class="lede">Maps for desktops, laptops, tablets and phones. Start with one useful desktop trip and prove each device capability as the work grows.</p><p class="notice">The application is not released. Every platform below is a candidate; no device has been certified by this project.</p><p><a href="../README.md">Repository guide</a> · <a href="feasibility.md">Platform feasibility</a> · <a href="../CONTRIBUTING.md">Contribute</a> · <a href="../AGENTS.md">For agents</a></p><div class="stats"><div class="stat"><b>{len(tasks)}</b>bounded task packets</div><div class="stat"><b>{len(roles)}</b>roles to fill</div><div class="stat"><b>{len(ps)}</b>candidate profiles</div><div class="stat"><b>{len(caps)}</b>separate capabilities</div></div></header>
<main><section><h2>What can be shared</h2><p>A shared app or engine can cover map data and trip planning. Permissions, location, touch, audio and sleep still need platform adapters and physical tests. A model that cannot run the host OS remains blocked upstream.</p><figure><div class="path"><div><b>Common trip</b>Start · destination · mode<br>Map · search · route · packs</div><div><b>Platform adapter</b>Linux / Android / guest / browser<br>Permission · location · lifecycle</div><div><b>Exact device</b>Model · OS · GPU · provider<br>Independent capability evidence</div></div><figcaption>Figure 1. Code can be shared while support remains specific to the tested hardware and software. This is the proposed architecture, not a completed implementation.</figcaption></figure></section>
<section><h2>Find your part</h2><p>People own scope, risk and review. Agents can investigate and implement a bounded task. Hardware owners can contribute evidence without writing code. All operational seats are currently vacant.</p><div class="grid">{''.join(rolecards)}</div></section>
<section id="tasks"><h2>Choose a task</h2><p>Agree the task, owner, reviewer and cap before a run. Keep your keys. Submit one PR with a result someone else can reproduce. Filters change this page only; they do not claim a task.</p><div class="controls"><input id="query" aria-label="Search tasks" placeholder="Search a task or skill"><select id="phase" aria-label="Phase"><option value="">All phases</option>{''.join('<option>'+x+'</option>' for x in ('P0','P1','P2','P3'))}</select><select id="role" aria-label="Role"><option value="">All roles</option>{''.join('<option value="'+h(x['id'])+'">'+h(x['name'])+'</option>' for x in roles)}</select><button id="reset">Reset</button></div><p id="count" aria-live="polite"></p><div class="grid" id="task-grid">{''.join(taskcards)}</div></section>
<section><h2>Prove the devices</h2><p>A question mark means no observation, not a failure. Observed source/replay results do not certify physical hardware. Verified records require an independent reviewer, exact revision and evidence; expired verification is marked old.</p><div class="controls"><select id="family" aria-label="Device family"><option value="">All families</option>{''.join('<option>'+x+'</option>' for x in ('desktop','laptop','tablet','phone','all'))}</select></div><figure><div class="matrix"><table><thead><tr><th>Candidate profile</th>{''.join('<th>'+h(c['name'])+'</th>' for c in caps)}</tr></thead><tbody>{''.join(rows)}</tbody></table></div><figcaption>Figure 2. This registry contains {len(records)} evidence records as of {h(as_of)}. Candidate hardware names identify recruitment scope, not proven compatibility. Exact model/OS data must accompany any future verification.</figcaption></figure></section>
<section><h2>How a change lands</h2><figure><div class="path"><div><b>Accepted task</b>Owner + reviewer<br>Paths + budget + stop rule</div><div><b>Contributor fork</b>Agent disclosed<br>Proof + failures + receipt</div><div><b>Trusted policy</b>Base code reads data<br>Isolated proposed tests</div><div><b>Human review</b>Two approvals + code owner<br>Protected integration</div></div><figcaption>Figure 3. Automated checks inspect structure and reproducibility; people remain responsible for the truth and safety of the contribution. See live admin verification before relying on enforcement.</figcaption></figure><p>The initial owner is temporary custodian. Ordinary merges wait until independent reviewers accept responsibility. AI compute and map-service operating budgets remain separate.</p><p><a href="review.md">Security and proof</a> · <a href="../GOVERNANCE.md">Authority and vacant roles</a> · <a href="providers.md">Data and operating costs</a> · <a href="milestones.md">Release sequence</a></p></section>
<section><h2>Where this started</h2><p>Omamesh, Omastorm, Phonechy and Omarchy Mobile are the named inspirations. Their projects have not endorsed or joined this initiative. Existing applications and components get evaluated before a new client or fork.</p><details><summary>Primary sources and reuse decisions</summary><ul>{sourceitems}</ul></details></section></main>
<footer><p>Generated from canonical JSON. No analytics, external scripts, map requests or account connection. <a href="https://github.com/parker-brown-family/omarchy-community-maps">Open the repository</a>.</p></footer>"""
    script="""const q=document.querySelector('#query'),p=document.querySelector('#phase'),r=document.querySelector('#role');function filter(){let n=0;document.querySelectorAll('.task').forEach(t=>{const show=(!p.value||t.dataset.phase===p.value)&&(!r.value||t.dataset.roles.split(' ').includes(r.value))&&t.textContent.toLowerCase().includes(q.value.toLowerCase());t.classList.toggle('hide',!show);if(show)n++});document.querySelector('#count').textContent=n+' tasks shown'}[q,p,r].forEach(x=>x.addEventListener('input',filter));document.querySelector('#reset').onclick=()=>{q.value='';p.value='';r.value='';filter()};document.querySelectorAll('[data-role]').forEach(b=>b.onclick=()=>{r.value=b.dataset.role;filter();document.querySelector('#tasks').scrollIntoView({behavior:'smooth'})});document.querySelector('#family').onchange=e=>document.querySelectorAll('[data-family]').forEach(row=>row.classList.toggle('hide',!!e.target.value&&row.dataset.family!==e.target.value));filter();"""
    page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Omarchy Community Maps</title><style>'+css+'</style></head><body>'+body+'<script>'+script+'</script></body></html>\n'
    page=page.replace('<h2>Prove the devices</h2>', '<h2>Prove the devices</h2><p><a href="devices.html">Search exact models and their complete test history</a>. The matrix below groups recruitment candidates; use the model registry for device-specific evidence.</p>')
    return {"docs/work-map.md":"\n".join(md)+"\n","tasks/README.md":"\n".join(index)+"\n","docs/support-matrix.md":"\n".join(matrix)+"\n","docs/contribution-map.html":page,
            "docs/devices.html":devices.render_page(root,dt.datetime.fromisoformat(as_of+"T23:59:59+00:00"))}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--check",action="store_true");a=ap.parse_args()
    failed=[]
    for name,content in outputs(ROOT).items():
        p=ROOT/name
        if a.check:
            if not p.exists() or p.read_text()!=content:failed.append(name)
        else:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content)
    if failed:print("Stale generated views: "+", ".join(failed));return 1
    print("Generated views verified" if a.check else "Generated contribution map and indexes");return 0
if __name__=="__main__":sys.exit(main())
