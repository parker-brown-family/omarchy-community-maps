# Primary-source ledger

Checked on 28 October 2026. These are sources for discovery and proposed reuse, not runtime qualification. Follow selected sources again and pin revisions before implementation.

## S01 — Repository overview

https://github.com/parker-brown-family/omarchy-community-maps

Public master snapshot reviewed; no local checkout or implementation test. Resolve HEAD again before work.

Status: `reviewed`.

## S02 — Existing work map

https://github.com/parker-brown-family/omarchy-community-maps/blob/master/docs/work-map.md

Existing P0–P3 task identifiers and dependencies.

Status: `reviewed`.

## S03 — Existing architecture

https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/docs/architecture.md

APP-01 selects the engine; reuse and bounded contracts are existing decisions.

Status: `reviewed`.

## S04 — APP-01 packet

https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/tasks/app-01.md

Existing-app comparison before a new client.

Status: `reviewed`.

## S05 — TRANSIT-01 packet

https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/tasks/transit-01.md

Existing transit assessment is P3 and depends on DATA-01.

Status: `reviewed`.

## S06 — Existing provider policy

https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/docs/providers.md

Licenses, offline rights, provenance, costs and safe pack lifecycle.

Status: `reviewed`.

## S07 — Agent entry point

https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/AGENTS.md

Scope, human authorization, evidence kinds and canonical JSON.

Status: `reviewed`.

## S08 — Agent run contract

https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/docs/agent-contract.md

One accepted task per PR; reviewer, cap and stop conditions.

Status: `reviewed`.

## S09 — Canonical task registry

https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/data/tasks.json

Current task metadata; rebase proposed additions rather than replacing this file.

Status: `reviewed`.

## S10 — Existing source registry

https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/data/sources.json

Existing inspirations and provider-policy findings; retain these records.

Status: `reviewed`.

## S11 — Board renderer

https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/tools/render.py

Generates contribution views from canonical data; current phase loop is P0–P3.

Status: `reviewed`.

## S12 — Repository validator

https://raw.githubusercontent.com/parker-brown-family/omarchy-community-maps/master/tools/validate.py

Inspect constraints before extending data schemas or evidence.

Status: `reviewed`.

## S13 — CoMaps official source mirror

https://github.com/comaps/comaps

Whole-app/offline baseline; primary development is on Codeberg. Apache-2.0 at project level, with NOTICE/data/component terms to inspect.

Status: `reviewed`.

## S14 — CoMaps Linux distribution listing

https://flathub.org/en/apps/app.comaps.comaps

Listing explicitly warns that Linux does not yet match mobile feature parity; not an Omarchy qualification result.

Status: `reviewed`.

## S15 — CoMaps contribution guide

https://raw.githubusercontent.com/comaps/comaps/main/docs/CONTRIBUTING.md

Links upstream AI-usage policy; obtain and respect the current policy before contributions.

Status: `reviewed`.

## S16 — CoMaps AI-usage policy target

https://codeberg.org/comaps/Governance/src/branch/main/AI_USAGE.md

Linked by upstream contribution guide, but policy body was inaccessible in this research session. Do not infer permission.

Status: `linked_but_not_retrieved`.

## S17 — GNOME Maps

https://apps.gnome.org/Maps/

Desktop planning baseline based on OpenStreetMap.

Status: `reviewed`.

## S18 — GNOME developer announcement of Transitous integration

https://discourse.gnome.org/t/163-public-transit/23035

Historical primary announcement from 2024; demonstrates prior integration, not current region coverage. Verify installed version.

Status: `reviewed`.

## S19 — Organic Maps

https://github.com/organicmaps/organicmaps

Alternative whole-app/offline navigation reference; do not build a second fork by default.

Status: `reviewed`.

## S20 — MapLibre GL JS

https://github.com/maplibre/maplibre-gl-js

Browser vector-map renderer; not search, routing or navigation.

Status: `reviewed`.

## S21 — MapLibre Native

https://github.com/maplibre/maplibre-native

Native rendering family; platform integration must be qualified.

Status: `reviewed`.

## S22 — MapLibre Native Qt

https://github.com/maplibre/maplibre-native-qt

Qt bindings and Qt Location plugin; candidate for a justified native surface.

Status: `reviewed`.

## S23 — MOTIS

https://github.com/motis-project/motis

Multimodal routing, geocoding and tiles; REST/OpenAPI. Human-facing upstream communication must be human-written.

Status: `reviewed`.

## S24 — MOTIS configuration and realtime inputs

https://github.com/motis-project/motis/blob/master/docs/setup.md

OSM plus timetable inputs, realtime and GBFS configuration; pin the release before implementing.

Status: `reviewed`.

## S25 — OpenTripPlanner

https://github.com/opentripplanner/OpenTripPlanner

OTP2 server uses GTFS/OSM and realtime updates, exposes GraphQL; JVM deployment and LGPL-3.0 license need release-specific review.

Status: `reviewed`.

## S26 — Valhalla

https://github.com/valhalla/valhalla

MIT routing engine with tiled graph architecture; test route profiles, instructions and device resource requirements.

Status: `reviewed`.

## S27 — Photon

https://github.com/komoot/photon

Apache-2.0 geocoder with typeahead, multilingual search and reverse geocoding; data and import dependencies remain separate.

Status: `reviewed`.

## S28 — Pelias data-source architecture

https://github.com/pelias/documentation/blob/master/data-sources.md

Alternative multi-source geocoder; do not assume every new dataset has a maintained importer.

Status: `reviewed`.

## S29 — Pelias runtime requirements

https://github.com/pelias/documentation/blob/master/requirements.md

Search backend/version requirements matter; review bundled dependency licenses and operational costs.

Status: `reviewed`.

## S30 — Protomaps basemaps

https://github.com/protomaps/basemaps

Basemap generation plus matching cartographic styles; preserve tile-schema/style compatibility.

Status: `reviewed`.

## S31 — Planetiler

https://github.com/onthegomap/planetiler

Build tool for vector tiles, including PMTiles output; build infrastructure is not a phone runtime.

Status: `reviewed`.

## S32 — PMTiles concepts

https://docs.protomaps.com/pmtiles/

Tile archive accessed with byte ranges; read-only format, not a search index or route graph.

Status: `reviewed`.

## S33 — PMTiles MapLibre GL integration

https://docs.protomaps.com/pmtiles/maplibre

Documented GL JS protocol integration; do not assume identical Native/Qt support.

Status: `reviewed`.

## S34 — OpenStreetMap copyright and license

https://www.openstreetmap.org/copyright

OSM data is ODbL, independent of application code licensing.

Status: `reviewed`.

## S35 — OSMF tile-server policy

https://operations.osmfoundation.org/policies/tiles/

Standard public tile service is not a bulk/offline-download backend.

Status: `reviewed`.

## S36 — Public Nominatim policy

https://operations.osmfoundation.org/policies/nominatim/

Public endpoint: application-wide maximum 1 request/second and no client autocomplete; self-hosted software is a different case.

Status: `reviewed`.

## S37 — Geofabrik British Columbia extract

https://download.geofabrik.de/north-america/canada/british-columbia.html

OSM PBF input and update files. Source version and acquired digest must be pinned.

Status: `reviewed`.

## S38 — BC Transit open-data catalog

https://www.bctransit.com/open-data/

Kelowna links static GTFS plus alerts, trip updates and vehicle positions. Binary bodies were not decoded in this session.

Status: `reviewed`.

## S39 — BC Transit data terms

https://www.bctransit.com/open-data/terms-of-use/

Limited, revocable license with attribution and other conditions; not equivalent to unrestricted public-domain data.

Status: `reviewed`.

## S40 — GTFS Schedule specification

https://gtfs.org/documentation/schedule/reference/

Canonical timetable specification; service dates, times and supported optional features must be respected.

Status: `reviewed`.

## S41 — GTFS Realtime specification

https://gtfs.org/documentation/realtime/reference/

Trip updates, vehicle positions and service alerts have distinct semantics.

Status: `reviewed`.

## S42 — MobilityData GTFS validator

https://github.com/MobilityData/gtfs-validator

Apache-2.0 static-feed validator; validation alone is not a successful itinerary or realtime test.

Status: `reviewed`.

## S43 — Mobility Database

https://mobilitydatabase.org/

Discovery catalog for GTFS, GTFS-RT and GBFS; individual feed terms still apply.

Status: `reviewed`.

## S44 — Transitous API policy

https://transitous.org/api/

Optional community-operated MOTIS service with eligibility, identification, attribution and usage limits; not a mandatory default.

Status: `reviewed`.

## S45 — General Bikeshare Feed Specification

https://gbfs.org/

Shared-mobility availability standard; discovery is distinct from booking/payment.

Status: `reviewed`.

## S46 — Overture Places guide

https://docs.overturemaps.org/guides/places/

Business/place data with source-dependent provenance and licensing; not a review corpus.

Status: `reviewed`.

## S47 — Overture attribution and licensing

https://docs.overturemaps.org/attribution/

Theme and source-specific licenses; do not label all Overture data CC0 or one blanket license.

Status: `reviewed`.

## S48 — AllThePlaces

https://github.com/alltheplaces/alltheplaces

Existing location-data extraction project; assess published data and provenance before launching new crawlers.

Status: `reviewed`.

## S49 — Panoramax integration

https://docs.panoramax.fr/how-to-contribute/use-panoramax/

Open street imagery API using OGC/STAC; viewer and images have separate terms.

Status: `reviewed`.

## S50 — Panoramax self-hosting

https://docs.panoramax.fr/how-to-contribute/hosting-instance/

Federated/self-hostable imagery infrastructure; does not provide uniform worldwide photographic coverage.

Status: `reviewed`.

## S51 — Panoramax federation requirements

https://docs.panoramax.fr/federated-catalog/

Imagery/metadata licensing and anonymization requirements; check the actual instance and image.

Status: `reviewed`.

## S52 — DriveBC Open511 API

https://api.open511.gov.bc.ca/help

Documented road events under OGL-BC and API terms. Event overlays are not live network-wide speed data.

Status: `reviewed`.

## S53 — GeoClue Location interface

https://www.freedesktop.org/software/geoclue/docs/gdbus-org.freedesktop.GeoClue2.Location.html

Timestamp can be receipt time, cached or non-monotonic; do not invent measurement provenance.

Status: `reviewed`.

## S54 — GeoClue Client interface

https://www.freedesktop.org/software/geoclue/docs/gdbus-org.freedesktop.GeoClue2.Client.html

Application identity, permissions, provider state and updates need integration.

Status: `reviewed`.

## S55 — Android LocationManager

https://developer.android.com/reference/android/location/LocationManager

Platform location API candidate; separately review target SDK, permissions and background lifecycle.

Status: `reviewed`.

## S56 — StreetComplete

https://github.com/streetcomplete/StreetComplete

Existing OSM contribution workflow to learn from or hand off to; no automated edits authorized.

Status: `reviewed`.

## S57 — Copernicus Sentinel-2

https://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/sentinel-2

Satellite imagery candidate for later layers; not equivalent to street-level or high-resolution aerial coverage.

Status: `reviewed`.

## S58 — Omamesh

https://github.com/clartek/omamesh

MeshCore messaging/advertised-contact map integration. Current README names Esri/OSM online basemaps and an offline coordinate grid; reuse transport/normalization separately from map-provider choices.

Status: `reviewed`.

## S59 — Omastorm

https://github.com/wesleygrimes/omastorm

Rust/Quickshell weather-radar integration; observation timestamps, stale states and provider coverage. Do not infer Canada-wide radar, forecasts, warnings or GNSS from the app.

Status: `reviewed`.

