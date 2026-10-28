# Assess transit and live data

Task: TRANSIT-01. Phase: P0. Track: routing. State: unclaimed.
Owner and independent reviewer: unassigned.

## Purpose and acceptance
Start early with a named region, catalog-resolved feeds, terms, refresh assumptions and explicit unknown costs. Source discovery and synthetic fixtures need no mobile navigation. DATA-01 still gates the operating-provider/integration decision. Scheduled and realtime runtime work is separated into TRANSIT-02 and TRANSIT-03; test missed service and stale feeds before any delivered transit claim.

## Dependencies and roles
Prerequisites: DATA-01.
Roles: maps, data. Agent suitability: suitable.
Read AGENTS.md, CONTRIBUTING.md, docs/agent-contract.md and docs/feasibility.md.

## Allowed paths
- experiments/transit/
- docs/providers.md

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
