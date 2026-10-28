# Exact Device Registry

Difficulty: 5/10. Extend the existing evidence store with model identity and a searchable view; no application or device certification ships.

Parker's autonomous bootstrap delegation remains in force. His October 27 clarification explicitly requests an open-ended model manifest and evidence tracking. The combined plan is selected under that delegation, without claiming independent review. Protected-branch review remains required.

## Plan

Keep three distinct records: device model, tested configuration, capability observation. `data/devices.json` identifies models and explicit placeholders. Existing platform profiles link to a model when an operator supplies an exact configuration. Existing evidence records continue to name a profile, capability, app revision, procedure, result and artifacts.

Generate a searchable HTML device page and a JSON CLI lookup from the same records. Every observation stays visible with its kind, dates, revision and review state. No device-wide support badge is inferred. A report about a different OS, revision or model is not evidence for the user's configuration.

The initial entries demonstrate iPhone generations, individual Pixels, Apple Silicon laptop variants and other form factors. Unconfirmed future hardware stays a placeholder and cannot receive physical certification. New models require data additions, not code changes. Repository byte/file limits still bound untrusted submissions.

Least confident decision: retaining the existing profile registry for configurations avoids migrating evidence, but its older broad candidate rows remain a separate recruitment view. Agents must use the exact device page for model-specific answers.

## Slices

- [x] Model registry, configuration template and validation.
- [x] Shared query, generated tracker and contributor instructions.
- [x] Negative tests and browser checks; PR prepared for protected-branch review.

Turned out to be: 5/10. Reusing the evidence store kept the change bounded; preserving configuration identity and old results required the most care.

Validation: 35 Python tests pass, generated views match, and sandboxed Chromium runs the installed TD extractor against the device page. Browser search finds Pixel 7 Pro and Mac17,3 independently, shows an honest empty state for mismatched filters, and keeps the M6 watchlist marked unconfirmed. Narrow layout was observed at 500 CSS pixels; the browser clamped the requested 390-pixel override, so 390 pixels is not claimed. The override was reset.

This extends DOC-01, contributor onboarding, under Parker's explicit model-tracking request. Authorized scope includes data/devices.json, data/platforms.json, tools/devices.py, tools/validate.py, tools/render.py, tests/, schemas/device-profile.example.json, docs/device-registry.md, docs/devices.html, generated contribution links, AGENTS.md, README.md and the device intake form. Independent reviewers remain unassigned; neither the task nor any hardware is certified by this change.
