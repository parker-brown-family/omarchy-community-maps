# Work map

Snapshot: 2026-10-28. Assignment and evidence are separate. All operational roles begin vacant.

[Interactive map](contribution-map.html) · [Product roadmap](roadmap.md) · [Reuse map](reuse-map.md) · [Support](support-matrix.md) · [Agent contract](agent-contract.md)

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
| [TRANSIT-01 — Assess transit and live data](../tasks/transit-01.md) | maps, data | DATA-01 | suitable |
| [DOC-01 — Verify contributor onboarding](../tasks/doc-01.md) | docs, automation | none | suitable |
| [ROADMAP-01 — Publish reuse-first architecture and lane map](../tasks/roadmap-01.md) | docs, maps, data | none | assist |
| [SERVICE-01 — Compare a regional MOTIS service with justified alternatives](../tasks/service-01.md) | maps, data, linux | none | assist |
| [SEARCH-01 — Benchmark regional place and address search](../tasks/search-01.md) | maps, data | APP-01, SERVICE-01 | assist |
| [PLACE-01 — Add provenance-aware place enrichment](../tasks/place-01.md) | maps, data | none | assist |
| [TRAFFIC-01 — Establish lawful traffic inputs and ETA evaluation](../tasks/traffic-01.md) | maps, data, security | none | assist |
| [IMAGERY-01 — Integrate a licensed street-imagery panel](../tasks/imagery-01.md) | maps, data, security | none | assist |
| [ACCESS-01 — Validate physical-accessibility data and route semantics](../tasks/access-01.md) | maps, touch, hardware | none | assist |

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
| [TILE-01 — Produce a self-controlled regional display pack](../tasks/tile-01.md) | maps, data, security | DATA-01, PACK-01 | assist |
| [TRANSIT-02 — Plan scheduled regional transit](../tasks/transit-02.md) | maps, data | TRANSIT-01, SERVICE-01 | assist |
| [TRANSIT-03 — Apply and expire realtime transit](../tasks/transit-03.md) | maps, data | TRANSIT-02 | assist |
| [INCIDENT-01 — Show expiry-aware road events](../tasks/incident-01.md) | maps, data, security | DATA-01 | assist |
| [COMMUNITY-01 — Separate corrections, shared places and reviews](../tasks/community-01.md) | maps, security, docs | PLACE-01, PRIV-01 | assist |
| [SYNC-01 — Design private saved places and portable trip handoff](../tasks/sync-01.md) | desktop, security | HAND-01, PRIV-01 | assist |
| [TERRAIN-01 — Scope satellite and terrain layers](../tasks/terrain-01.md) | maps, data | DATA-01 | assist |
| [OPS-02 — Measure region build and distribution costs](../tasks/ops-02.md) | data, automation | TILE-01 | assist |

## P2

| Task | Roles | Prerequisites | Agent work |
|---|---|---|---|
| [NAV-01 — Qualify outdoor walking guidance](../tasks/nav-01.md) | location, hardware, reviewer | QA-01, MOB-01, PACK-02 | human-only |
| [NAV-02 — Qualify screen-off audio and power](../tasks/nav-02.md) | android, linux, hardware | NAV-01, AND-02 | human-only |
| [DOC-02 — Translate and test user workflows](../tasks/doc-02.md) | docs, hardware | QA-01 | assist |
| [COVERAGE-01 — Add a second independent region](../tasks/coverage-01.md) | maps, data, reviewer | TRANSIT-03, OPS-02 | assist |

## P3

| Task | Roles | Prerequisites | Agent work |
|---|---|---|---|
| [ROAD-01 — Qualify cycling and driving](../tasks/road-01.md) | maps, hardware | ROUTE-01, NAV-01 | assist |

