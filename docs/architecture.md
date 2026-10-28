# Architecture

The repository coordinates contributions and evidence; no product engine is selected. We are assembling inspectable components toward a sovereign mapping utility. The [roadmap](roadmap.md) treats product capabilities and exact-device qualification as separate axes.

## Two investigations

The existing desktop comparison tests CoMaps and GNOME Maps on the same trip. Prefer a complete application, packaging, supported imports/exports and tested destination handoff. A companion or fork needs an unmet workflow and a maintenance owner. Neither app is assumed to accept arbitrary replacement engines.

In parallel, SERVICE-01 — Compare a regional service investigates MOTIS using bounded OSM/timetable inputs. Its documented REST/OpenAPI service includes multimodal routing, geocoding and tiles. Compare OTP for transit or Valhalla for dedicated routing only when the same fixture exposes a relevant gap. This experiment does not commit the product to a browser client, hosted service or second permanent runtime.

At the comparison review, select one default application path; record failed cases, unsupported capabilities, resource use and what would reopen the decision. Keep useful service experiments separate until an adapter and operating owner are accepted. A MapLibre comparison surface remains a test harness until product evidence justifies it.

## Boundaries

- Trip: chosen origin/destination, travel mode, itinerary legs and route provenance.
- Location: source and receipt time, optional uncertainty, permission/provider state.
- Renderer: map, route and uncertainty without inventing a fix.
- Search/routes/transit: bounded requests, supported capabilities, cancellation and explicit failures.
- Places/overlays/imagery: source identity, coverage, observation/capture time, terms and attribution.
- Packs: per-capability coverage, compatible engine/schema, publisher trust, integrity, storage, atomic update and rollback.
- Platform shell: keyboard/touch, permissions, lifecycle, audio and deliberate handoff.

Extend existing contracts only after a fixture needs the field; this roadmap introduces no new runtime API. Keep unknown values nullable to the renderer. PMTiles supplies display tiles, not a search index or routing graph. The chosen app's packs, MOTIS imports and Valhalla graphs are distinct formats. A server's ability to handle a region says nothing about handset resource use.

Test seams with network-free fixtures. Local experiments bind to loopback with web-origin controls; no untrusted route, place or provider string becomes shell code. Requests, provider switches and private sharing remain explicit. No new AI service or shared runtime is needed for orchestration.

Source research can run before an operating-provider decision. Production services and physical support retain their separate rights, operator, security, review and device-evidence gates. See [reuse decisions](reuse-map.md), [provider research](providers.md) and [the architecture decision](decisions/0001-reuse-first-maps.md).
