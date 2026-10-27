# Feasibility

A useful maps experience across desktops, laptops, tablets and phones is technically plausible. Guaranteed Google Maps feature parity on every model is not a support promise we can make. Reuse mature engines, define shared contracts and qualify exact hardware/OS combinations as people supply evidence.

## Meaning of all devices
Every family is eligible where its host OS already boots and exposes usable display/input. Manual planning works without a measured location; live guidance does not. Missing drivers are upstream prerequisites. The project is not a universal kernel-porting effort.

Support identifies model, SoC/GPU where relevant, OS/kernel/build, display/input stack, location provider, app revision and data/provider version. Pixel, ARM and tablet are recruitment groupings. Android on a Pixel and native Linux on the same Pixel are separate targets.

| Lane | Shared work | Target-specific work |
|---|---|---|
| Linux x86_64 | Engine/data, trip model, fixtures | GPU/Wayland, packaging, GeoClue/portal authorization |
| Apple Silicon Linux | aarch64 engine/core | Exact upstream-supported model/OS, GPU and location source |
| Other ARM Linux | Contracts/data | ABI, kernel/firmware, thermal/storage limits |
| Linux tablet | Core/Linux adapters | Touch, keyboard, rotation, suspend and GNSS |
| Native Linux phone | Core/GeoClue where available | GNSS daemon, permissions, shell, power and screen-off |
| Android phone/tablet | Contracts, portable engine | Native APIs, foreground service, lifecycle, distribution |
| Linux guest on Android | Guest UI/core | Explicit host bridge or native handoff; no inherited GPS |
| Browser | Foreground planning | Secure context, permissions, rendering/storage/background limits |

Native macOS and iOS are separate additional ports, not implied by Apple Silicon Linux. A model without a usable Linux port may have an Android/browser path if those requirements are met.

## Reuse before a new client
CoMaps is a serious offline navigation candidate. GNOME Maps is a useful Linux planning baseline. Compare the complete desktop trip first; a launcher/handoff or small shell may suffice. A custom MapLibre/Qt surface still needs search, routing, packs, location and lifecycle. A fork brings upstream merges, security and releases; justify it with an unmet workflow.

A renderer does not supply navigation. Offline tiles do not supply offline search/routing. IP city lookup does not supply a navigation fix.

## What earlier evidence establishes
Discovery found existing mapping integrations, not a verified universal product. Pinned-source and isolated service tests exposed why time, uncertainty and mode discrimination belong in acceptance criteria. Current upstream may differ; re-run invalidation before claiming a current defect. Reproduction requirements are summarized in research-notes.md.

Omarchy Mobile reports hardware progress. Its current head is recorded in data/sources.json. Earlier GNSS bring-up established receiver/GeoClue work, while end-to-end outdoor app and lifecycle qualification remained open. A hardware board's green GNSS cell cannot be copied into a navigation cell.

## Remaining product work
Map/search/address/POI quality, profiles, offline lifecycle, accessibility, trusted location, rerouting, restrictions, service operation and updates need owners. Traffic, transit, imagery, business data and reviews each need coverage/terms; none is promised for the first milestone.

Prove the desktop trip independently, then qualify ARM and touch while designing mobile adapters. Live guidance follows physical outdoor testing. Universal availability remains conditional on host support, tests, volunteers and sustainable services. See data/sources.json for primary sources reviewed 2026-10-27.
