# Find Tests for Your Device

The registry answers a narrow question: what did someone observe on this model, in this configuration, at this app revision? A device entry can exist before anyone tests it. The initial entries are examples, and contributors can add any model within the project scope.

Open [the searchable tracker](devices.html), or ask your agent to run:

```sh
python3 tools/devices.py --query "Pixel 7 Pro" --json
python3 tools/devices.py --query "iPhone 13" --json
python3 tools/devices.py --query "Mac17,3" --json
```

The command reads the checked-out repository. Fetch current changes before treating an old checkout as the community's latest record. Search results include exact matches separately from broader matches. Multiple matches require identification, not a guess. No matching record means evidence is absent here; it says nothing about unrecorded tests elsewhere.

## Follow the Three Records

| Record | Contains | Canonical location |
|---|---|---|
| Model | Manufacturer, model, aliases, identifiers and identity sources | `data/devices.json` |
| Configuration | Device ID, OS lane/build, actual hardware variant, kernel, GPU, memory, browser and location provider | `data/platforms.json` |
| Observation | Configuration ID, capability, app revision, expected/observed result, procedure, artifacts, operator and reviewer | `evidence/records/*.json` |

An iPhone 13 observation does not apply to an iPhone 14. A Pixel running Android and the same Pixel running native Linux need separate configurations. A MacBook Air M4 result does not certify an M5 model, a different screen-size variant, or another OS image. Browser testing on an iPhone does not demonstrate native Omarchy installation.

The Apple model names and identifiers in the seed manifest come from Apple's [MacBook Air identification page](https://support.apple.com/en-us/102869) and [iPhone identification page](https://support.apple.com/en-us/108044), checked October 27, 2026. The M6 watchlist remains unconfirmed here. Product identification establishes neither Linux support nor application support.

## Add a Model or Configuration

1. Search by marketing name and model identifier. Reuse an existing model ID only when it is the same hardware model. Add another row for Pro/Plus/mini variants, board revisions or materially different hardware. For a custom desktop, identify the motherboard/revision, CPU and GPU together.
2. Add a row to `data/devices.json` with a stable slug, family, manufacturer, model, aliases, model identifiers, SoC, sources and notes. Unknown fields remain null or empty lists. An unconfirmed future model uses `identity: "placeholder"`; no configuration can point to it yet.
3. Copy `schemas/device-profile.example.json` into a new entry in `data/platforms.json`. Give it a unique ID and the correct `device_id`. Record the actual hardware, OS build and configuration. Do not change an old profile to describe a new OS or hardware configuration; create another profile so earlier records retain their meaning.
4. Use the existing OS lanes: `linux-native`, `android-native`, `linux-guest` or `browser`. A lane describes the test environment; it grants no compatibility. Keep unmeasured configuration values null.

The list is not a product whitelist. Adding a model never requires changing the query code or rendering code. Repository file and byte budgets still limit each submitted snapshot; expanding those safety limits needs review.

## Record an Actual Run

Copy `schemas/evidence.example.json` only after running a test. Set `profile` to the exact configuration and `capability` to one registered capability. Follow [device qualification](device-testing.md). Each app revision, test date, capability and result gets its own evidence record; a partial result describes its limits rather than claiming the whole device works.

An observation needs an operator, procedure, expected/observed behavior and sanitized, hash-pinned artifacts. Physical observations must match the linked profile's hardware and OS. Verification also needs a model identifier, an independent reviewer and an expiry. Tests, validators and an agent's confidence cannot substitute for that review.

The tracker retains all observations, including failures and older app revisions. Source, replay and emulator records remain distinguishable from physical tests. Expired verification becomes stale. Conflicting results stay visible for review; the page does not choose a winning claim or compute a device-wide support badge.

Report a run through the **Device evidence** issue form or an accepted task's PR. Issues are intake; reviewed records in the protected repository are the storehouse. Until a report is merged, it is not in the generated tracker. Run the three checks in README and regenerate the views with `python3 tools/render.py` before submission. Never publish a serial, IMEI, account identifier, home address or private route.
