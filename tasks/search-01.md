# Benchmark regional place and address search

Task: SEARCH-01. Phase: P0. Track: search. State: unclaimed.
Owner and independent reviewer: unassigned. This is a scope proposal, not an accepted assignment.

## Purpose and Acceptance

Held-out search corpus and measured candidate report.

- Typo, ambiguous, multilingual and missing-address cases.
- Top-k relevance, latency and source freshness recorded.
- Out-of-region differs from no match.

## Discovery and Delivery

Source reading, rights/coverage inventory and synthetic fixture design can begin before delivery dependencies. Engine execution, live requests and integration need their own accepted scope and inputs.

Delivery prerequisites: APP-01, SERVICE-01.
Roles: maps, data. Read AGENTS.md, CONTRIBUTING.md, docs/agent-contract.md, docs/roadmap.md and docs/reuse-map.md. Phase is delivery vocabulary, not a ban on early research.

## Allowed Paths

- experiments/search/
- fixtures/search/
- docs/providers.md

## Before a Technical Run

A human accepts the issue claim, base revision, branch, allowed paths, input sources, owner, time/compute cap, stop condition and independent acceptance test. Unknown budgets/reviewers remain unknown; this packet assigns nobody. Do not subscribe, deploy, contact upstream or change another person's device from this packet.

## Independent Acceptance

Return one task-sized PR with pinned inputs/code, exact environment, procedure, expected/observed results, failures, unrun checks and a run receipt. A different reviewer repeats the acceptance cases or states which source/fixture findings they checked. A source review, replay or lab service is not physical navigation evidence. Keep source, coverage, terms and measured resource use separate.

## Invalidate First

Recheck upstream and current project results before implementing. If an existing app or a reviewed result already passes these cases, reproduce it and recommend reuse/narrowing rather than building another copy. Reject the candidate if the accepted case fails, necessary rights are absent, or measured resource needs exceed the run's agreed cap; record the limiting case.

## Stop Condition

Stop the affected run on its cap, missing runtime prerequisite, unclear input rights, unexpected private data or a credential boundary. Keep read-only findings. Never fabricate missing time, accuracy, cost or coverage. Tests run against local fixtures; no load testing of public services. Branch protections and independent reviews still govern integration.
