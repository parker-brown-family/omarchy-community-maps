# Oma Maps — Reuse-First Roadmap and Agent Handoff

**Prepared:** 28 October 2026  
**Repository:** `parker-brown-family/omarchy-community-maps`  
**Purpose:** Turn the sovereign, Google Maps-depth ambition into an explicit component map, dependency graph and bounded implementation queue.  
**Status:** Research and design proposal. No repository changes, engine execution, feed decoding, field tests or platform certification were performed. All stack choices below are candidates until tested.

## 1. Mission: preserve the ambition, make the work composable

Build a community-controlled maps utility for Omarchy with a long-term destination of comprehensive everyday usefulness: finding places, understanding businesses, planning trips, navigating, using transit, seeing disruptions and imagery, contributing corrections, and carrying useful information between devices. The first desktop trip is an early proof, not the definition of the finished product.

**Your immediate assignment as the receiving agent is a roadmap revision, not a wholesale implementation or a replacement architecture invented in one session.** Read the current repository and branch diff, reconcile this handoff against it, propose precise reuse decisions, and create reviewable task packets. Retain the existing evidence and human-authorization rules. This handoff does not authorize paid services, deployments, upstream messages, public map edits or changes to branch protections.

The repository already separates trip state, location, rendering, search/routing, packs and platform shells; APP-01 intentionally leaves engine selection open. Preserve those seams. The work map currently emphasizes qualification across devices, while transit is represented by one later assessment. Add **product/data/service lanes alongside the platform lanes**, rather than discarding the platform work or treating “installable on a phone” as the product roadmap. [S03](https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/docs/architecture.md) [S02](https://github.com/parker-brown-family/omarchy-community-maps/blob/master/docs/work-map.md) [S04](https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/tasks/app-01.md) [S05](https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/tasks/transit-01.md)

### Working definition of sovereignty — proposed acceptance requirements

A user can use core planning without a proprietary account; select or replace service operators; retain/export private places and trips; install a permitted regional offline pack; and understand what leaves their device. A community operator can rebuild the required data products from permitted sources. A missing remote service produces a truthful degraded mode, not a silent switch to another provider.

Evaluate four dimensions separately: **software freedom, data reuse rights, operational control, and user privacy**. An open-source client calling an irreplaceable remote endpoint is not full operational sovereignty. Conversely, a transit feed from an agency can be a legitimate external input without pretending the community controls that agency. “Publicly downloadable” is not a license category.

Offer explicit modes: `offline-local`, `self-hosted`, and `community-hosted`. Optional third-party endpoints require disclosure and consent. In offline-local mode, missing coverage must fail locally; it must never trigger a remote search, tile request or location lookup.

## 2. The architecture decision: compare coherent systems, not a bag of libraries

### Track A — useful application integration now

Run the existing APP-01 comparison with **CoMaps and GNOME Maps**. CoMaps supplies an integrated offline-map/navigation candidate; its Linux listing explicitly warns of differences from its mobile versions. GNOME Maps supplies a desktop-planning baseline, and its maintainers have previously integrated Transitous. Treat that as reuse evidence, not proof that today’s build covers the pilot or accepts arbitrary replacement services. Organic Maps is an additional comparator only for a specific unresolved need. [S13](https://github.com/comaps/comaps) [S14](https://flathub.org/en/apps/app.comaps.comaps) [S17](https://apps.gnome.org/Maps/) [S18](https://discourse.gnome.org/t/163-public-transit/23035) [S19](https://github.com/organicmaps/organicmaps)

Prefer installation, packaging, tested deep links, supported imports/exports, or a small companion surface. Do not assume CoMaps is a plugin host into which Photon, Valhalla or OTP can simply be dropped. Establish the actual extension boundary from the pinned code. A fork requires a demonstrated unmet workflow, a maintenance owner, and an upstream-update strategy.

### Track B — sovereign service expansion, investigated in parallel

**First service candidate: a regional MOTIS instance**, because it already combines multimodal planning, address/stop geocoding and tiles behind REST/OpenAPI. Compare OpenTripPlanner when timetable behavior, supported features or integration needs justify it; OTP2 exposes GraphQL and runs on a JVM. Add a dedicated Valhalla road-routing or Photon search service only when a measured requirement beats the integrated option. Pelias is a later search alternative where multi-source ingestion justifies its additional components. [S23](https://github.com/motis-project/motis) [S24](https://github.com/motis-project/motis/blob/master/docs/setup.md) [S25](https://github.com/opentripplanner/OpenTripPlanner) [S26](https://github.com/valhalla/valhalla) [S27](https://github.com/komoot/photon) [S28](https://github.com/pelias/documentation/blob/master/data-sources.md) [S29](https://github.com/pelias/documentation/blob/master/requirements.md)

A small **MapLibre GL JS test surface** is suitable for comparing these services without committing the product to a browser shell. If a bespoke native UI is justified, MapLibre Native/Qt is a separate rendering candidate. A renderer is not a navigation engine. The eventual client decision must include keyboard/touch accessibility, lifecycle, offline I/O, memory, GPU behavior and maintainability—not just an attractive screenshot. [S20](https://github.com/maplibre/maplibre-gl-js) [S21](https://github.com/maplibre/maplibre-native) [S22](https://github.com/maplibre/maplibre-native-qt)

```text
                     Oma Maps user workflows
         existing-app integration OR justified shared surface
                               |
                  Versioned, bounded adapters
                 /       |         |         \
              search    routes    transit    overlays/imagery
                 \       |         |         /
             selected engines and approved source providers
                               |
             provenance + coverage + freshness + attribution

  Independent platform adapters: location / permissions / audio / handoff
  Independent data pipeline: source snapshots -> compiled regional artifacts
```

**Do not deploy both stacks by default.** Track B can be a laboratory/companion while Track A proves a usable workflow. At the decision gate, choose one default delivery path and document which pieces remain experiments. Preserve a route to a cohesive experience; permanently launching unrelated apps is not the long-term product goal.

## 3. What plugs into which build lane

These are integration proposals, not claims that the components are mutually interchangeable. `reuse-matrix.json` contains machine-readable candidate records and first tests.

| Build lane | Existing task anchors | First reusable pieces | Integration point and Oma Maps-owned work |
|---|---|---|---|
| Client and desktop experience | APP-01, UX-01, PKG-01 | CoMaps; GNOME Maps | Package/test existing apps first. Own consistent launch, failure explanations and safe handoff; prove available APIs before promising customization. |
| Basemap and rendering | DATA-01, WEB-01, PACK-01/02 | OSM/Geofabrik → Protomaps/Planetiler → PMTiles → MapLibre; or the chosen app’s own pipeline | Pin tile schema with style, fonts and sprites. Own source selection, offline assembly, attribution and update policy. |
| Search and discovery | DATA-01, APP-01 | Existing app/MOTIS first; Photon or Pelias if needed | Normalize bounded results, ranking tests, language behavior, cancellation, provenance and missing coverage. |
| Walking, cycling and driving | ROUTE-01, ROAD-01, NAV-01 | Existing app; MOTIS for planning; Valhalla for a dedicated engine | Own route-mode semantics, restrictions, instructions, reroute state and independent tests. |
| Transit and shared mobility | TRANSIT-01, DATA-01 | MOTIS or OTP; GTFS/GTFS-RT; MobilityData validator; GBFS | Own feed registry, static/realtime joins, freshness, transfers, accessibility and fare uncertainty. |
| Location and guidance | LOC-01/02, NAV-01/02 | GeoClue; Android LocationManager; selected upstream app | Own timing/uncertainty semantics, permission UX, screen-off behavior and physical qualification. |
| Offline region lifecycle | PACK-01/02, REL-01 | Chosen app’s map format OR separate display/search/route artifacts | Own signed manifests, compatibility, storage limits, atomic installation, expiry and rollback. |
| Places and business detail | DATA-01; proposed PLACE-01 | OSM plus audited Overture; optional AllThePlaces | Own deduplication, source attribution, field-level freshness, conflicting hours and source-specific rights. |
| Incidents and traffic | INT-01, ROAD-01; proposed INCIDENT-01/TRAFFIC-01 | DriveBC/Open511 for pilot incidents; lawful speed source still to establish | Keep visual events, route penalties, measured speeds and predicted ETAs distinct. |
| Mesh and weather overlays | INT-01, PRIV-01 | Omamesh and Omastorm | Reuse bounded integration patterns; independently choose providers, preserve time/coverage and avoid leaking peer locations. |
| Street imagery | INT-01; proposed IMAGERY-01 | Panoramax API/viewer/federation | Own coverage/date UI, rights, resource limits, privacy and contribution moderation. |
| Community corrections and reviews | PRIV-01; proposed COMMUNITY-01 | Existing OSM editing workflows such as StreetComplete | Route factual corrections upstream; keep reviews as separate content with authorship, moderation and removal policies. |
| Saved places and cross-device use | HAND-01, AND-01; proposed SYNC-01 | Existing app export/import and platform handoff | Own a portable private data format, consent, device pairing and revocation; no mandatory identity service. |
| Device integration | ARM-01/02, TAB-01/02, AND-01/02, MOB-01/02, BRIDGE-01 | Existing supported OS/app stacks and platform APIs | Qualify exact hardware/OS/app combinations; do not turn this initiative into a kernel-porting project. |
| Operations, security and qualification | GOV-01, SEC-01, PRIV-01, OPS-01, QA-01, REL-01 | Existing repository procedures; upstream test tools | Own provider budgets, controlled builds, independent evidence, incident response and maintainership. |

Sources for the candidate capabilities: [S13](https://github.com/comaps/comaps) [S17](https://apps.gnome.org/Maps/) [S20](https://github.com/maplibre/maplibre-gl-js) [S30](https://github.com/protomaps/basemaps) [S31](https://github.com/onthegomap/planetiler) [S32](https://docs.protomaps.com/pmtiles/) [S23](https://github.com/motis-project/motis) [S25](https://github.com/opentripplanner/OpenTripPlanner) [S26](https://github.com/valhalla/valhalla) [S27](https://github.com/komoot/photon) [S46](https://docs.overturemaps.org/guides/places/) [S52](https://api.open511.gov.bc.ca/help) [S49](https://docs.panoramax.fr/how-to-contribute/use-panoramax/) [S53](https://www.freedesktop.org/software/geoclue/docs/gdbus-org.freedesktop.GeoClue2.Location.html) [S55](https://developer.android.com/reference/android/location/LocationManager) [S56](https://github.com/streetcomplete/StreetComplete)

### Three compatibility traps to eliminate early

**Display data is not navigation data.** PMTiles stores tiled imagery/vector data; it does not supply an address index or routing graph. A usable offline region needs every required asset. CoMaps/Organic Maps artifacts, Valhalla graph tiles, MOTIS imports and PMTiles are distinct data products; no interchange is implied. [S32](https://docs.protomaps.com/pmtiles/) [S13](https://github.com/comaps/comaps) [S26](https://github.com/valhalla/valhalla) [S23](https://github.com/motis-project/motis)

**Styles depend on tile schemas.** Select a matching Protomaps generator/style pair, or an independently verified alternative. Do not render one schema with another project’s style and call missing labels a renderer bug. The documented PMTiles GL JS protocol is not proof that Native/Qt accepts the same source URL. [S30](https://github.com/protomaps/basemaps) [S33](https://docs.protomaps.com/pmtiles/maplibre) [S22](https://github.com/maplibre/maplibre-native-qt)

**Service engines are not necessarily handset runtimes.** A self-hosted server can be sovereign without fitting on a phone. Measure regional memory, storage, start-up, import and battery implications before choosing on-device deployment. Keep build machines, optional regional servers and end-user devices separate in the architecture.

### Specific Omarchy reuse boundaries

Omamesh already connects MeshCore transport/contact state to an Omarchy map. Its current README describes Esri/OSM online basemaps and an offline coordinate grid. Reuse its bounded state/transport patterns, not an assumption that its complete map backend meets this project’s sovereignty or offline-navigation goals. Advertised peer coordinates should remain peer observations, not become the user’s current location. [S58](https://github.com/clartek/omamesh)

Omastorm is a useful weather-layer and Rust/Quickshell integration reference, including explicit observation times and stale states. Its documented radar products have specific geographic coverage; do not assume the Kelowna pilot automatically has a suitable radar source. An IP-derived city is not GNSS, and radar observations are not a forecast or warning. Use a separate, consent-aware overlay adapter. Neither project is an assumed partner or supplier. [S59](https://github.com/wesleygrimes/omastorm)

## 4. Contracts: own the seams, reuse the engines

Extend the existing `contracts/` rather than adding an unconstrained plugin framework. The following records are proposed; they are not existing repository APIs. Validate them with network-free fixtures before binding them to an engine.

| Contract | Required information | Critical failure behavior |
|---|---|---|
| `ProviderCapabilities` | Provider/adapter version; supported modes; region/language bounds; offline support; available features; request limits | Unsupported capability is an explicit response, never silently substituted. |
| `SearchRequest/Result` | Query, locale, optional bounds/bias, source-namespaced ID, label, coordinates, match type, provenance, dataset version | Distinguish no result, outside coverage, network failure and cancelled request. Never turn a low-quality search match into a measured location. |
| `PlaceRecord` | Source IDs, names/categories, entrances, address, hours, accessibility, field-level source/time and conflicts | Unknown is not false. An old business record is not evidence that the business is open now. |
| `RouteRequest/Itinerary` | Start/end/vias, mode, departure or arrival constraint, accessibility preferences, legs/maneuvers, units, geometry encoding, provider/data version | Return unsupported restrictions and route gaps; do not substitute a car route for a walk. Preserve transit metadata rather than flattening everything into a polyline. |
| `TransitSnapshot` | Agency/feed namespace, feed hash/version, service date/time zone, trip/stop IDs, schedule, realtime timestamps and status | Expire stale realtime; preserve useful schedule fallback with explicit labeling. No matching trip is not zero delay. |
| `LocationObservation` | Coordinates, observation source, source timestamp/provenance, local receipt time, uncertainty semantics, permission/provider state | Unknown time/accuracy remains null. Ignore stale/out-of-order observations under a documented policy; never invent a new fix at reconnect. |
| `RegionManifest` | Region polygon/bounds, coverage per capability, source snapshots, artifact hashes, signature/trust identity, engine/schema compatibility, bytes, terms, expiry | Reject incompatible/corrupt artifacts. Keep last complete region active through failed download/update. |
| `Overlay/ImageryItem` | Geometry, source, observed/capture/expiry time, attribution, license, confidence/quality notes, display bounds | Outage is not “no incidents.” Missing imagery is not current imagery. Route impact requires a separate validated adapter. |
| `TripHandoff` | Explicit destination or itinerary, share scope, coordinate order, optional expiry and approved transport | Strip private labels/history unless explicitly included. No arbitrary executable URI or shell interpolation. |

Use WGS84 coordinates with an explicit order, explicit distance/time units, namespaced identifiers and UTC instants plus agency time-zone context where required. Keep source data versions separate from application versions. Review map-boundary crossings, antimeridian behavior and Unicode early enough to avoid embedding pilot-only assumptions.

GeoClue documents that its timestamp can reflect receipt rather than measurement, can be old, and need not be monotonic. Preserve that uncertainty instead of assigning stronger semantics to the provider. Android’s native location API is a candidate, not a guarantee of permission, background execution or a particular underlying positioning source. [S53](https://www.freedesktop.org/software/geoclue/docs/gdbus-org.freedesktop.GeoClue2.Location.html) [S54](https://www.freedesktop.org/software/geoclue/docs/gdbus-org.freedesktop.GeoClue2.Client.html) [S55](https://developer.android.com/reference/android/location/LocationManager)

**Security boundary:** local services bind to loopback with a narrow interface; do not expose an unauthenticated routing/pack/file API to the LAN. Review web-origin controls, untrusted provider URLs, redirects, oversized input, decompression, file traversal and arbitrary local-file access. Logs must omit raw private searches, home coordinates and route histories by default. Custom endpoints require an explicit trust decision.

## 5. Roadmap: delivery stages, with parallel discovery

These stage labels are planning vocabulary, **not new values to insert into the repository’s P0–P3 schema**. Product research may start before a feature is ready for release. In particular, transit data discovery does not depend on a working Linux phone.

| Stage | User-visible result | Release gate | Work that can proceed in parallel |
|---|---|---|---|
| D0 — Choose the seams | Clear capability map and architecture decision process | Source-backed candidates; missing rights/owners visible; bounded test plan | Feed inventory, imagery coverage, business-data sampling and accessibility requirements |
| D1 — Complete one desktop workflow | Install → find destination → choose start → pedestrian route → clear absent-location/outage states | Independent repetition of the existing desktop acceptance path | MOTIS regional lab; transit static-feed validation; private handoff design |
| D2 — Own a usable region | Offline display + search + route; controlled update and rollback | Network denied; all assets present; corrupt/mismatched pack cannot activate | ARM/touch qualification, native location adapters, search-quality corpus |
| D3 — Useful public transport | Scheduled journey first, then clearly labeled realtime changes | Timetable validity, transfers, cancellation and stale-feed tests | Screen-off guidance tests on supported devices; next-region discovery |
| D4 — Rich everyday utility | Better places, closures, imagery and accessible trip information | Per-layer provenance, coverage, terms and failure behavior; field checks where needed | Community contribution flow; selected imagery hosting feasibility |
| D5 — Expand depth and geography | More regions, richer transit, traffic quality, community data and optional sync | Reusable onboarding, sustained operation and independently measured improvement | Satellite/terrain, indoor complexity, shared mobility and additional devices |

Do not force every user/device through every stage before another region can contribute. Conversely, do not let parallel experiments silently become production dependencies.

### Dependency changes worth proposing, not silently making

1. Split TRANSIT-01 into an **early discovery/validation investigation** and later implementation/qualification packets. The current task’s stated dependency is DATA-01; no phone driver is needed to inspect a feed. Keep its existing identity/history and propose additional packets rather than replacing it. [S05](https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/tasks/transit-01.md)
2. Let basemap/pack format investigation overlap APP-01, but do not finalize pack compatibility before the client/engine decision.
3. Treat platform and product capability as two axes. A desktop can prove a transit itinerary; a phone can prove a location fix; neither automatically proves the other.
4. Keep security, provider permission and human review as release gates. Do not represent all gates as serial blockers to harmless research.

## 6. Bounded implementation queue

`roadmap-proposals.json` contains 16 proposed packets, deliberately separate from `data/tasks.json`. Owner/reviewer/phase assignments remain unset. The following ordering is a recommendation for accepted work, not permission to execute it all.

**First planning PR — ROADMAP-01.** Reconcile repository HEAD, record reuse decisions and the capability/dependency map, and add narrowly scoped investigation packets. Do not select an engine based on project popularity or README claims. Preserve existing task IDs, append source records and regenerate the views.

**First parallel technical investigations, after their scope is accepted:** finish the existing APP-01 comparison; implement SERVICE-01 with a bounded regional dataset; inventory and validate the proposed transit feed under DATA-01/TRANSIT-01; and finish LOC-01 fixtures. These produce independently reviewable findings, not one giant PR.

| Proposed packet | Output | Acceptance focus |
|---|---|---|
| SERVICE-01 | MOTIS regional spike and justified OTP/Valhalla comparisons | Same inputs/scenarios; import and runtime resources; missing features visible |
| TILE-01 | Self-controlled regional display bundle | Matching schema/style/fonts; attribution; no hidden remote fetch; safe replacement |
| SEARCH-01 | Held-out search corpus and candidate report | Typos, ambiguity, languages, out-of-area, no-result and provenance |
| TRANSIT-02 | Static scheduled itinerary | Walk–bus–walk, transfer, service-day rollover and no service |
| TRANSIT-03 | Freshness-aware realtime | Cancellations, unmatched IDs, skipped stops, reconnect and stale fallback |
| PLACE-01 | Regional place enrichment experiment | Duplicates, contradictory hours, source licensing and field-level traceability |
| INCIDENT-01 | Expiring Open511 overlay | Partial closures, geometry mismatch and source outage before route penalties |
| TRAFFIC-01 | Lawful speed-data/ETA feasibility | Measured speeds distinguished from assumptions; no covert trace collection |
| IMAGERY-01 | Panoramax panel | Capture date, coverage gaps, license and privacy handling |
| COMMUNITY-01 | Correction flow plus separate reviews proposal | Human confirmation; moderation and removal; no proprietary review imports |
| SYNC-01 | Local-first saved-place/trip portability | No mandatory account; deliberate share scope and revocation |
| ACCESS-01 | Real-world accessibility corpus | Unknown facilities; lift failures; human validation of route claims |
| TERRAIN-01 | Satellite demonstration and elevation research | Date/resolution/no-data; rights and storage; no aerial-parity claim |
| OPS-02 | Measured regional cost and recovery model | Build/storage/egress numbers, hard caps and rollback |
| COVERAGE-01 | A second independently sourced region | Reusable recipe; no hardcoded pilot feeds; per-capability coverage |

## 7. Concrete transit pilot: Kelowna as a proposed first region

Kelowna is a **proposed pilot**, not an existing repository decision. BC Transit’s catalog links a static GTFS feed and three distinct realtime feeds for Kelowna. This gives the transit lane a specific public-resource starting point. The catalog links were inspected; the ZIP and protobuf contents were not decoded or freshness-tested here. [S38](https://www.bctransit.com/open-data/)

```text
Static GTFS:
https://bct.tmix.se/Tmix.Cap.TdExport.WebApi/gtfs/?operatorIds=47
Service alerts:
https://bct.tmix.se/gtfs-realtime/alerts.pb?operatorIds=47
Trip updates:
https://bct.tmix.se/gtfs-realtime/tripupdates.pb?operatorIds=47
Vehicle positions:
https://bct.tmix.se/gtfs-realtime/vehicleupdates.pb?operatorIds=47
```

Re-resolve these links from the agency catalog before use. BC Transit’s terms grant a limited, revocable right to use/reproduce/redistribute data under conditions, including attribution. Record the actual terms, refresh policy and operator approval; do not label this CC0 or claim an unconditional redistribution right. [S39](https://www.bctransit.com/open-data/terms-of-use/)

### Pilot procedure

1. Acquire an approved, bounded snapshot. Record final URL, retrieval time, service interval, agency time zone, digest, terms and redirect behavior. Do not put large datasets or credentials into git. Use synthetic/public-location fixtures, not personal travel history.
2. Run the MobilityData static validator. Save the report, including warnings; distinguish feed validity from routing correctness. Resolve expired/empty service calendars before importing. [S42](https://github.com/MobilityData/gtfs-validator)
3. Build a regional graph from permitted OSM input with enough surrounding network to avoid cutting valid approaches and transfers at the boundary. Geofabrik provides the British Columbia PBF input; a complete province need not be the deployed handset pack. [S37](https://download.geofabrik.de/north-america/canada/british-columbia.html)
4. Test MOTIS first; compare OTP on the same accepted itinerary cases when needed. Adapter contracts, not whichever UI looks better, decide whether the engine fits.
5. Join realtime to the static feed using the appropriate agency/feed/trip/service context. Treat vehicle positions, arrival predictions and service alerts as different information. A moving bus icon is not a working journey planner. [S40](https://gtfs.org/documentation/schedule/reference/) [S41](https://gtfs.org/documentation/realtime/reference/)
6. Use a recorded fixture clock. Test a direct ride; a transfer; the last feasible trip; after-midnight service; a weekend/exception day; a cancellation; a skipped stop; stale/missing realtime; mismatched trip identifiers; and unknown wheelchair/fare information. For cross-zone/time transitions, follow the agency’s authoritative zone rules rather than inventing a universal offset.
7. Compare selected public-stop trips with published agency information and independent human observations. Never treat agreement with Google as the sole correctness oracle.
8. Build the UI: next departures, itinerary alternatives, walk segments, scheduled versus realtime badges, alert relevance and a legible no-service explanation. Then measure refresh load and failed-fetch behavior.

Broader feed discovery can use Mobility Database. Transitous is an optional operated MOTIS endpoint, not a free unlimited substitute for an operator: its current policy includes eligibility, identification, attribution and resource constraints. Keep development/CI on local fixtures; no automated public-endpoint load testing. [S43](https://mobilitydatabase.org/) [S44](https://transitous.org/api/)

Later transit depth deserves separate acceptance cases: fares and fare uncertainty, transfers and station entrances, lift outages, inter-agency journeys, missed connections, bike carriage, service alerts, flexible services and shared mobility. GBFS can describe available shared vehicles/stations; it does not itself implement booking or payment. [S45](https://gbfs.org/)

## 8. Google Maps-depth areas that need more than a library

### Places, businesses and search quality

Start with sources already serving the chosen client, then test a regional Overture/OSM enrichment layer. Overture’s source/theme licensing varies; follow its current attribution records rather than giving the whole dataset one license. AllThePlaces can inform an additional published-data route. Neither source should be presented as a licensed corpus of Google reviews or proof of current business hours. [S46](https://docs.overturemaps.org/guides/places/) [S47](https://docs.overturemaps.org/attribution/) [S48](https://github.com/alltheplaces/alltheplaces)

The real work is a stable place model, duplicate resolution, entrances versus centroids, language/aliases, freshness, contradictions and relevance evaluation. Maintain source-namespaced IDs and an explicit merge history; a name/address match is not enough to overwrite records. Store factual corrections separately from subjective reviews. The latter requires anti-spam, moderation, abuse reporting, removal, authorship and a funding/operations decision.

### Road incidents, traffic and reliable ETAs

DriveBC/Open511 is a specific pilot source for road events. Use it first as an attributed, time-bounded overlay. Later routing penalties require correctly matching an event’s geometry, direction, timing and closure semantics to graph edges. [S52](https://api.open511.gov.bc.ca/help)

Do not call that a live-traffic system. Measured road speeds, historical patterns and prediction quality need lawful inputs and coverage audits. A routing engine can consume costs without supplying the observations that make those costs good. No background collection of users’ movements by default; any proposed trace contribution needs explicit opt-in, minimization and a separate privacy review. ETA quality should be evaluated by mode, region and condition, not one global average.

### Street-level imagery and aerial/terrain layers

Panoramax offers reusable API/viewer and federated-hosting infrastructure. Start with coverage lookup and a viewer; show capture date and license, and handle areas with no imagery. Hosting contributions adds storage, moderation, face/plate privacy and takedown work. Follow the actual image/instance terms, not just the software license. [S49](https://docs.panoramax.fr/how-to-contribute/use-panoramax/) [S50](https://docs.panoramax.fr/how-to-contribute/hosting-instance/) [S51](https://docs.panoramax.fr/federated-catalog/)

Satellite, aerial, terrain and street imagery are separate products. Copernicus Sentinel-2 is a later satellite-source candidate, not a drop-in substitute for high-resolution city aerial imagery. Evaluate each imagery/elevation source on rights, resolution, freshness, storage and reproducible transformation. [S57](https://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/sentinel-2)

### Accessibility, guidance and indoor complexity

Keep UI accessibility distinct from the accessibility of the physical route. Keyboard navigation and screen-reader behavior do not prove a kerb, lift, pathway or station entrance is usable. Missing data must remain unknown. Separate testing is needed for instructions, off-route detection, audio timing, GNSS uncertainty, intermittent connectivity and screen-off power behavior.

A desktop planner should remain useful without live position. A mobile guidance claim requires physical tests on the exact supported device/OS/application/data revision. Keep kernel/GPU/GNSS bring-up upstream where possible. An Android guest environment does not inherit working host location merely because it runs a Linux UI.

### Community participation and private continuity

Make factual map improvements benefit the upstream commons. Learn from existing OSM contribution tools; use deliberate human handoff before building another editor. Do not automate uploads, fabricate reviews or treat model confidence as geographic evidence. [S56](https://github.com/streetcomplete/StreetComplete)

Saved places, collections, recent destinations and cross-device handoff are valuable product depth without needing a mandatory account or behavioral-advertising infrastructure. Start with local export/import. Add optional sync only after a threat model, pairing/revocation design and maintainable data-conflict policy.

## 9. Data rights, public endpoints and sustainability

Separate **code license, source-data license, generated-database obligations, style/font/media license, and service terms**. The repository’s MIT license cannot override upstream terms. Maintain a per-artifact attribution/rights manifest and obtain qualified review for unresolved redistribution or derivative-database questions. [S06](https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/docs/providers.md) [S34](https://www.openstreetmap.org/copyright)

The standard OSM raster-tile endpoint does not permit the bulk downloads needed for offline packs. Public Nominatim is not an autocomplete backend and its rate limit applies to aggregate application traffic. These public-service restrictions do not prohibit operating appropriately licensed software on your own infrastructure. [S35](https://operations.osmfoundation.org/policies/tiles/) [S36](https://operations.osmfoundation.org/policies/nominatim/)

For every selected provider record: operator; exact URLs and revision; region/languages; permitted caching/prefetch/distribution; authentication; renewal/expiry; freshness; quota/rate policy; contact route; failure/migration plan; data sent; attribution; and monthly operational assumptions. Use `null` for unknown prices, capacities and credentials—not zero.

Measure one region before forecasting the world:

```text
Monthly operating requirement =
  serving compute + data-build compute + storage + transfer/egress
  + backups/monitoring + moderation/support/maintenance work

Pack egress =
  cold installations × complete-download bytes
  + refreshes × actual-update bytes

Build storage peak =
  source inputs + temporary build data + new artifacts + rollback copy
```

Keep money estimates separate from human labor. Publishing a binary is not the same cost as keeping its data fresh. Use quotas, download sizes, last-good artifacts and operator-visible degradation before inviting unbounded use.

## 10. Repository changes the receiving agent should make

**Do not copy these JSON files directly over the canonical registries.** They use a handoff/proposal schema and contain no approved owners, claims, evidence or issue numbers.

Recommended first accepted roadmap change:

- Extend `docs/architecture.md` with the two-track comparison and explicit decision gates.
- Add `docs/roadmap.md` and `docs/reuse-map.md` explaining product/service lanes alongside platform qualification.
- Append vetted sources to `data/sources.json`, preserving its current schema and existing entries.
- Reconcile proposed tasks into `data/tasks.json` and individual `tasks/` packets only after maintainers agree scope. Preserve old IDs/dependencies/history; assign repository phases deliberately.
- Extend `docs/providers.md` with source/coverage/rights/cost decisions. Keep live credentials and private coordinates out.
- Regenerate `docs/work-map.md`, the contribution map and task/support indexes via `tools/render.py`; do not maintain conflicting hand-edited copies. The current renderer enumerates P0–P3, so adding another phase requires a reviewed schema/renderer/test change. [S11](https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/tools/render.py) [S12](https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/tools/validate.py)

Inspect current code before running the repository’s documented checks. These commands are for the receiving agent; they were not run against a checkout in this research session:

```bash
# In an inspected, isolated checkout of the agreed branch:
python3 tools/render.py
python3 tools/validate.py
python3 -m unittest discover -s tests -v
python3 tools/render.py --check
```

Do not weaken validation merely to make the proposal fit. Do not mark a candidate as supported or a source-reviewed feature as physically verified. New source records and new task packets are not implementation evidence.

### Upstream relationships and AI-assisted work

Respect each upstream’s current contribution rules and licenses. CoMaps links a separate AI-usage policy, whose body could not be retrieved here; that is an explicit revalidation item, not permission. MOTIS explicitly requires human-written communication intended for humans. Agents may research, test and prepare local findings within Oma Maps’ contract; a human must decide and author upstream contact as required. Do not misrepresent generated material as human-written. [S15](https://raw.githubusercontent.com/comaps/comaps/main/docs/CONTRIBUTING.md) [S16](https://codeberg.org/comaps/Governance/src/branch/main/AI_USAGE.md) [S23](https://github.com/motis-project/motis) [S08](https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/docs/agent-contract.md)

## 11. Acceptance: what makes the roadmap clearer

The revised roadmap passes only when a contributor can select one lane and answer: what is reused; through what interface; what remains ours; which region/platform/mode is covered; what upstream/data rights apply; which prerequisite is real; what to test; what evidence is sufficient; and what would cause us to reject the candidate.

Record the following dimensions separately:

| Dimension | Example evidence, not a target already achieved |
|---|---|
| Search | Held-out top-k relevance, no-result behavior, language and source freshness |
| Routes | Mode/restriction correctness, disconnected graphs, access boundaries and instruction quality |
| Transit | Valid service days, plausible transfers, realtime matching and stale-data behavior |
| Offline | Display/search/route under denied network; matching artifact versions; update/rollback |
| Performance | Dataset and hardware recorded; cold/warm latency, RAM, disk, import time and power |
| Privacy | Audited request destinations, consent, data minimization and no silent fallback |
| Operations | Build reproducibility, source rights, size/cost assumptions, backups and failure recovery |
| Device support | Exact hardware/OS/app/data revision and an independent physical test where required |

Every result must say whether it came from source inspection, replay, emulator or physical observation. Synthetic fixtures belong in tests; they are not proof of a real-world trip. Keep an explicit list of failed attempts, unrun tests and unknowns. [S07](https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/AGENTS.md) [S12](https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/tools/validate.py)

### Required agent return package

Return a concise decision memo; a proposed repository diff; regenerated views; candidate and provider records; scoped task packets; a dependency graph; the test plan; and a source/pin ledger. Include an architecture decision record showing the selected option, rejected alternatives, evidence and what would change the choice. Report remaining blockers as specific unknowns, not a claim that the long-term ambition is impossible.

**The outcome is not “a smaller dream.” It is a large dream divided into reusable engines, lawful data inputs, explicit integration work and observable milestones.**

## 12. Research limitations and source ledger

This package is based on public primary pages and repository text inspected on 28 October 2026. No Git SHA is asserted: a container clone failed because external hostname resolution was unavailable, so the receiving agent must pin current HEAD and each selected upstream revision. No current releases were installed or benchmarked. BC Transit binary links returned ZIP/protobuf content types that were not decoded. CoMaps’ linked AI-policy body was inaccessible. None of those unknowns is silently treated as a pass.

`SOURCES.md` and `sources.json` provide the primary-source ledger, including retrieval limitations. `reuse-matrix.json` maps candidates to existing task IDs. `roadmap-proposals.json` supplies bounded next-work proposals. The website/repository claims cited here are discovery evidence only; implementation and physical support require new results.
