# Product Roadmap

Oma Maps aims for the breadth and depth of Google Maps through inspectable, replaceable components. The first desktop trip proves a useful application path. Transit, business information, imagery, traffic, offline use and community data remain part of the destination from the beginning.

## Work Starts on Two Tracks

**Application:** compare CoMaps and GNOME Maps on one desktop trip, including a manual start, walking access, missing location, provider failure and separate offline display/search/routing tests. Reuse the smallest complete integration that passes. APP-01 — Compare existing apps preserves that decision.

**Regional services:** investigate MOTIS as an integrated routing/geocoding/tile candidate. Record a pinned revision, input snapshots, import time, cold/warm latency, RAM/disk, unsupported features and network destinations. Bring OTP or Valhalla into the same comparison only for a demonstrated need. SERVICE-01 — Compare a regional service is a local experiment, not a deployment promise.

The two findings meet at an application review: can an existing client deliver the required workflow, can it use a service through a supported boundary, or does a specific gap justify a companion/new surface? One default path is selected from results, not from a list of popular libraries.

## Research and Delivery Are Separate

P0–P3 are the existing task phases, not a requirement to finish every phone before inspecting a bus feed. Read-only discovery and fixtures may begin early. A completed research report does not release its feature. No new phase values or bypass rules are introduced.

| Capability | First useful result | Delivery evidence | Can investigate now |
|---|---|---|---|
| Desktop planning | Install, search and a manual walking route | Independent repetition of the packaged trip | Both client candidates and missing-location fixtures |
| Regional services | Reproducible regional engine comparison | Bounded APIs, resources, rights and operating owner | MOTIS source/import recipe; alternatives when needed |
| Offline region | Display, search and route without network | Compatible full assets, failed-update recovery and rollback | Formats, source rights and realistic storage |
| Transit | Scheduled itinerary, then labeled realtime | Service days, transfers, cancellations, matching IDs and stale fallback | Feed catalog, schedules, terms and source validation |
| Places and imagery | Traceable local detail and dated imagery | Conflict/coverage handling, rights and privacy | Regional samples and absent coverage |
| Traffic and accessibility | Specific supported information | Lawful speed inputs; physical route observations | Source feasibility and unknown-data cases |
| Device guidance | Position, instructions, audio and recovery | Exact hardware/OS/app/data with physical review | Existing platform work and replay contracts |
| Community and portability | Deliberate corrections and private exports | Moderation, source rights, consent and revocation | Local formats and human correction flows |

## A Concrete Transit Investigation

Kelowna is the proposed first region because BC Transit's catalog lists static schedules, trip updates, service alerts and vehicle positions. The feed links have been checked against the catalog; binary contents have not been decoded or tested by this roadmap change. This is a source lead, not a working transit feature. See [the pilot procedure](transit-pilot.md).

Keep TRANSIT-01 — Assess transit and live data and its history; move its discovery assessment to P0. Its DATA-01 dependency still applies to an accepted provider/integration decision. Catalog inspection and synthetic fixtures need no working phone. Later scheduled and realtime packets have their own acceptance tests.

## Contributions Enter Broadly

The original 34 tasks remain, including all exact-device and human field tests. Sixteen handoff proposals are reconciled into unclaimed packets, giving 50 total packets. New packets carry no assignee, reviewer, issue URL, measured budget or support certification. Before implementation, create or agree one task issue, accept scope, and record the owner's cap and independent acceptance procedure. This planning PR does not authorize all 16 implementations.

There is no project-wide concurrency or founder-attention ceiling. Contributors use forks/branches. Agent analysis recommends include, scuttle for fitting parts, rebuild from a bounded specification, or reject. Protected-base checks, isolated proposed tests and independent human review control what lands. Governance, CI and validators receive the same review as app changes.

The [generated work map](work-map.md) is the canonical dependency view. The [34-task crosswalk](research/reuse-handoff-2026-10-28/TASK_CROSSWALK.md) preserves the old work; the [reuse map](reuse-map.md) explains all 29 candidates and where the first test belongs. The source handoff remains a dated proposal, with its limitations preserved.
