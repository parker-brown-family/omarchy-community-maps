# Run the bounded community pilot

Task: OPS-01. Phase: P0. Track: governance. State: unclaimed.
Owner and independent reviewer: unassigned.

## Purpose and acceptance
Declare the accepted pilot scope, contributor limits and operational owners; measure review backlog, reproducibility, compute and service costs separately. Open intake has no fixed global task-count, date or founder-attention cap. Stop unsafe or over-cap runs individually and publish prioritization decisions.

## Dependencies and roles
Prerequisites: GOV-01, DATA-01.
Roles: steward, automation. Agent suitability: assist.
Read AGENTS.md, CONTRIBUTING.md, docs/agent-contract.md and docs/feasibility.md.

## Allowed paths
- docs/pilot.md
- receipts/

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
