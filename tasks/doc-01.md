# Verify contributor onboarding

Task: DOC-01. Phase: P0. Track: documentation. State: unclaimed.
Owner and independent reviewer: unassigned.

## Purpose and acceptance
Fresh agent without private tools selects task, runs stdlib checks and understands evidence/trust boundaries.

## Dependencies and roles
Prerequisites: none recorded.
Roles: docs, automation. Agent suitability: suitable.
Read AGENTS.md, CONTRIBUTING.md, docs/agent-contract.md and docs/feasibility.md.

## Allowed paths
- CONTRIBUTING.md
- docs/agent-contract.md
- docs/onboarding.md

## Before starting
Maintainer accepts claim, exact base revision, scope, time/spend cap, stop condition and independent acceptance procedure. Missing budget stays unknown and must be agreed before paid work. Do not expand scope or acquire credentials.

## Deliverable and proof
One reviewable PR with procedure, environment, pinned revision, expected/observed behavior, failed attempts and limitations. Use schemas/run-receipt.example.json. Physical results use schemas/evidence.example.json and sanitized artifacts with SHA-256. Templates are not evidence.

## Independent verification
A different person repeats the acceptance procedure or states exactly which source/fixture claims they checked. Replays certify only replay behavior. Physical support requires physical observation.

## Invalidate first
Recheck upstream and the current registry. If already independently evidenced at the target revision, link that result and propose closing/narrowing this task instead of duplicating work.

## Stop condition
Stop on an unmet dependency, cap, license uncertainty, credential boundary or missing hardware. No paid subscription, firmware flash, public upstream message or deployment is authorized by this packet. Return reproducible findings. One task produces one PR; abandoned attempts stay outside the review queue.
