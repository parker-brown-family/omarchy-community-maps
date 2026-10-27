# Architecture

This bootstrap implements coordination and evidence. APP-01 selects the eventual product engine.

Preserve these boundaries:
- Trip model: chosen start/destination, travel mode and route provenance.
- Location adapter: source time, receipt time, optional uncertainty, permission/provider state.
- Renderer: map/route/uncertainty without inventing a fix.
- Search/routing: named bounded providers, cancellation and explicit failures.
- Packs: region/version, integrity, storage, update and rollback.
- Platform shell: keyboard/touch, permissions, lifecycle, audio and handoff.

Test contracts without network/GPS. Reuse upstream clients under their licenses. No new shared runtime, server or model client is needed to coordinate contributors.

| Approach | Useful first result | Cost |
|---|---|---|
| Existing-app integration | Small launcher/search/plan/handoff | Upstream UI/extension limits; device qualification |
| Shared core/native shells | Reused route/data/state | Multiple lifecycle/permission/audio adapters |
| Web planner | Broad foreground access | Browser background/storage limits |
| Full fork | Full control | Upstream sync, releases and vulnerabilities |

CoMaps is a candidate, not an approved fork. Respect licenses and human-authored contribution requirements upstream.

Canonical JSON plus Markdown procedures generate the board. Evidence is append-only by convention: corrections supersede with explanation. A new code/kernel/provider revision never silently inherits support. No production endpoint, telemetry, subscription or user-account service is provisioned.
