# Work map

Snapshot: 2026-10-27. Assignment and evidence are separate. All operational roles begin vacant.

[Interactive map](contribution-map.html) · [Support](support-matrix.md) · [Agent contract](agent-contract.md)

## P0

| Task | Roles | Prerequisites | Agent work |
|---|---|---|---|
| [GOV-01 — Recruit independent stewards and reviewers](../tasks/gov-01.md) | steward, reviewer, security | none | assist |
| [SEC-01 — Audit protection and hostile pull requests](../tasks/sec-01.md) | security, reviewer | none | assist |
| [DATA-01 — Choose sustainable providers for the pilot](../tasks/data-01.md) | data, maps | GOV-01 | suitable |
| [APP-01 — Compare existing apps on one desktop trip](../tasks/app-01.md) | desktop, maps, hardware | DATA-01 | assist |
| [LOC-01 — Specify location state and uncertainty](../tasks/loc-01.md) | location, reviewer | none | suitable |
| [LOC-02 — Reproduce Linux time and accuracy behavior](../tasks/loc-02.md) | location, linux | LOC-01 | suitable |
| [UX-01 — Define desktop trip and failure screens](../tasks/ux-01.md) | desktop, touch | APP-01, LOC-01 | assist |
| [PKG-01 — Package an x86_64 desktop integration](../tasks/pkg-01.md) | desktop, linux | APP-01, UX-01, SEC-01 | suitable |
| [ROUTE-01 — Prove walking routes respect pedestrian access](../tasks/route-01.md) | maps, hardware | DATA-01 | suitable |
| [QA-01 — Repeat the desktop trip independently](../tasks/qa-01.md) | hardware, reviewer | PKG-01, ROUTE-01, LOC-02 | human-only |
| [OPS-01 — Run the bounded community pilot](../tasks/ops-01.md) | steward, automation | GOV-01, DATA-01 | assist |
| [PRIV-01 — Audit map and location privacy](../tasks/priv-01.md) | security, data | LOC-01, DATA-01 | assist |
| [DOC-01 — Verify contributor onboarding](../tasks/doc-01.md) | docs, automation | none | suitable |

## P1

| Task | Roles | Prerequisites | Agent work |
|---|---|---|---|
| [ARM-01 — Qualify Apple Silicon Linux](../tasks/arm-01.md) | linux, hardware | QA-01 | assist |
| [ARM-02 — Qualify other ARM Linux computers](../tasks/arm-02.md) | linux, hardware | QA-01 | assist |
| [TAB-01 — Qualify x86 tablets and convertibles](../tasks/tab-01.md) | linux, touch, hardware | QA-01, UX-02 | assist |
| [TAB-02 — Qualify ARM Linux tablets](../tasks/tab-02.md) | linux, hardware | ARM-02, UX-02 | assist |
| [UX-02 — Adapt touch and accessibility](../tasks/ux-02.md) | touch, hardware | UX-01 | assist |
| [AND-01 — Choose Android integration and handoff](../tasks/and-01.md) | android, location | APP-01, LOC-01 | assist |
| [AND-02 — Qualify Android on Pixel and another vendor](../tasks/and-02.md) | android, hardware | AND-01, UX-02 | human-only |
| [MOB-01 — Integrate native Linux Pixel location](../tasks/mob-01.md) | linux, location, hardware | LOC-02, UX-02 | assist |
| [MOB-02 — Audit Phonechy and other phone ports](../tasks/mob-02.md) | linux, hardware | LOC-01 | assist |
| [BRIDGE-01 — Evaluate Android Linux-guest location](../tasks/bridge-01.md) | android, location, security | AND-01, LOC-01 | assist |
| [PACK-01 — Specify offline pack lifecycle](../tasks/pack-01.md) | data, maps, security | DATA-01, APP-01 | suitable |
| [PACK-02 — Prove offline display search and routing](../tasks/pack-02.md) | maps, hardware | PACK-01 | assist |
| [HAND-01 — Share a destination safely](../tasks/hand-01.md) | desktop, android, security | AND-01, LOC-01 | suitable |
| [REL-01 — Design signed releases and rollback](../tasks/rel-01.md) | release, security | SEC-01, PKG-01 | assist |
| [INT-01 — Define mesh and weather overlay contracts](../tasks/int-01.md) | desktop, maps | HAND-01, DATA-01 | suitable |
| [WEB-01 — Evaluate browser planning fallback](../tasks/web-01.md) | desktop, touch, security | DATA-01, UX-02 | assist |

## P2

| Task | Roles | Prerequisites | Agent work |
|---|---|---|---|
| [NAV-01 — Qualify outdoor walking guidance](../tasks/nav-01.md) | location, hardware, reviewer | QA-01, MOB-01, PACK-02 | human-only |
| [NAV-02 — Qualify screen-off audio and power](../tasks/nav-02.md) | android, linux, hardware | NAV-01, AND-02 | human-only |
| [DOC-02 — Translate and test user workflows](../tasks/doc-02.md) | docs, hardware | QA-01 | assist |

## P3

| Task | Roles | Prerequisites | Agent work |
|---|---|---|---|
| [ROAD-01 — Qualify cycling and driving](../tasks/road-01.md) | maps, hardware | ROUTE-01, NAV-01 | assist |
| [TRANSIT-01 — Assess transit and live data](../tasks/transit-01.md) | maps, data | DATA-01 | suitable |

