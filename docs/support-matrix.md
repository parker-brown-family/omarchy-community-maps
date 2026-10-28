# Support matrix

Snapshot: 2026-10-28. Families are candidates. Verification belongs to exact hardware/OS/revision; see evidence records.

| Candidate | Family / lane / architecture | Evidence | Blocker |
|---|---|---|---|
| Intel desktop/iGPU | desktop / linux-native / x86_64 | No observations recorded | GeoClue provider may be absent; test without GNSS. |
| AMD desktop/AMD GPU | desktop / linux-native / x86_64 | No observations recorded | Qualify rendering and packaging. |
| Desktop/NVIDIA GPU | desktop / linux-native / x86_64 | No observations recorded | Driver/Wayland path needs separate test. |
| Intel laptop | laptop / linux-native / x86_64 | No observations recorded | Wi-Fi positioning, suspend and scaling vary. |
| AMD laptop | laptop / linux-native / x86_64 | No observations recorded | Measure power and resume. |
| Apple M1/M2 on supported Linux/Omarchy | laptop / linux-native / aarch64 | No observations recorded | Upstream OS support is not app certification. |
| Apple Silicon Linux desktop | desktop / linux-native / aarch64 | No observations recorded | Exact model/GPU/OS; no automatic GNSS. |
| Qualcomm Linux laptop | laptop / linux-native / aarch64 | No observations recorded | Kernel/firmware/graphics are model-specific. |
| x86 detachable/convertible | tablet / linux-native / x86_64 | No observations recorded | Touch, keyboard, rotation, sleep. |
| ARM Linux tablet | tablet / linux-native / aarch64 | No observations recorded | Upstream drivers and location prerequisites. |
| Android tablet | tablet / android-native / aarch64 | No observations recorded | OS and vendor power policy. |
| Pixel 7 Pro/cheetah/Omarchy Mobile | phone / linux-native / aarch64 | No observations recorded | GNSS reports exist; app outdoor/sleep qualification open. |
| Pixel 6/6 Pro/7a/Fold/8 Pro/9a candidates | phone / linux-native / aarch64 | No observations recorded | Split each handset before certification. |
| OnePlus native Linux candidate | phone / linux-native / aarch64 | No observations recorded | Audit upstream bring-up/location/suspend. |
| Phonechy target hardware unknown here | phone / linux-native / aarch64 | No observations recorded | Verify model, OS, source license and location API. |
| Other native Linux handset | phone / linux-native / aarch64 | No observations recorded | Kernel/firmware support belongs upstream. |
| Pixel running Android | phone / android-native / aarch64 | No observations recorded | Different OS lane from native Omarchy Mobile. |
| Samsung/Qualcomm/MediaTek candidates | phone / android-native / aarch64 | No observations recorded | Exact models required; no assumed Google services. |
| Omarchy in Termux/proot/QEMU | phone / linux-guest / aarch64 | No observations recorded | Explicit host GPS/lifecycle bridge or native handoff. |
| Modern compatible browser | all / browser / architecture-independent | No observations recorded | Foreground planning; storage/background constraints. |

## Capabilities

- **Install, update and remove**: Clean install/launch/upgrade/removal at pinned version.
- **Display a map**: Attribution, scaling and network errors.
- **Find a place**: Address/POI/ambiguous/no-result fixtures.
- **Choose a start**: Manual planning without measured location.
- **Plan a walking route**: Pedestrian-discriminating geometry and profile.
- **Use current location**: Permission, observation time, uncertainty, stale/denied/absent.
- **Touch and accessibility**: Rotation, keyboard, screen reader, scaling.
- **Offline map packs**: Terms, disk budget, corruption/interruption recovery.
- **Offline place search**: Disconnected search, coverage and pack version.
- **Offline routing**: Disconnected correct mode and missing region.
- **Live guidance**: Physical route, off-route and fix recovery.
- **Screen-off guidance**: Locked-screen audio/GPS and lifecycle.
- **Power and thermal budget**: Measured duration/delta/baseline/conditions.
- **Safe trip handoff**: Bounded URI/data exchange with confirmation.
- **Cycling and driving**: Discriminating fixtures/restrictions/traffic limits.
- **Transit and live information**: Feed coverage, freshness, terms and outage.
