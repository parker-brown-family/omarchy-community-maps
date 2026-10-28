# Device qualification

First [look up the exact model](device-registry.md) and create a configuration profile linked to its device record. Broad family candidates cannot receive physical observations. The [device tracker](devices.html) retains all configurations and test records.

Record exact model, SoC/GPU, RAM/storage, OS image/kernel, display/input/scale, location provider, app revision/package hash, map/provider/pack version, network/permissions/power settings. Omit serials, SIM/account IDs and private addresses.

1. Clean install/launch and visible attribution.
2. Search fixed public queries, ambiguity and no result.
3. Manual origin/destination and pedestrian-discriminating route.
4. Denied/coarse/precise/revoked location with usable manual fallback.
5. Separate stale/absent replay from real outdoor observation.
6. Disable network and test offline display/search/routing independently.
7. On ready hardware, supervised public walk, lost fix and deviation/recovery.
8. Screen-off/lock/audio/suspend/battery-saver separately; power measurement with baseline/duration.
9. Upgrade/remove and interrupted/corrupt/disk-full pack update.
10. Independent reproduction/review stating precisely what was checked.

No active-driving interaction by driver. Use passenger/parked tests later. Firmware bring-up needs a separate upstream procedure and explicit operator authority.

Copy the evidence template only for an actual run. Source/replay/emulator evidence cannot become physical support. Failures are useful, unrun remains not-tested. Declare review expiry; app/kernel/provider changes require applicability review or rerun.
