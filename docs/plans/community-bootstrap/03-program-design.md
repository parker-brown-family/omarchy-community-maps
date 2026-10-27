# Program design

- AGENTS.md: portable entry point and trust boundaries; no dependence on this workstation's tools.
- README.md, CONTRIBUTING.md, GOVERNANCE.md, SECURITY.md: contributor routing, human responsibility and operational limits.
- data/{roles,platforms,capabilities,tasks,sources}.json: canonical registries.
- evidence/records/*.json: measured results; initially empty.
- schemas/: record shapes and required-field documentation.
- tasks/*.md: one bounded task per packet, dependencies and independent verification.
- docs/feasibility.md, architecture.md, location.md, providers.md, review.md, agent-contract.md, device-testing.md, milestones.md: the full engineering map.
- tools/validate.py: validation over a directory of plain data; no execution of submission files.
- tools/trusted_policy.py: bounded GitHub API snapshot retrieval, event/body checks, trusted validator invocation.
- tools/render.py: escaped static HTML and Markdown indexes.
- tests/test_policy.py: adversarial data and boundary tests.
- .github/workflows/: trusted-policy and repository-checks, checkout pinned to a verified full SHA.
- .github/ISSUE_TEMPLATE/: task, evidence, bug and role offers; PR template and CODEOWNERS.

## Contracts
Profile = id + device family + OS lane + architecture + candidate hardware + blockers + owner (nullable).
Evidence = id + profile + capability + status + scenario + tested revision + hardware/OS versions + expected/observed + procedure + artifacts + operator + independent reviewer + tested_at + expires_at + limitations.
Task = id + title + track + phase + scope paths + dependencies + required roles + agent suitability + owner/reviewer (nullable) + state + packet.

Verified evidence requires a named independent reviewer, immutable revision, exact hardware/OS and nonempty proof. Source inspection and synthetic replays never promote physical-device support. Regressions and expiration remain visible.

## Before implementation tests
Reject missing-vs-zero collapse, verified-without-proof, author-as-reviewer, duplicate identifiers, dangling task dependencies, dependency cycles, traversal/symlink paths, oversized blobs, secret-shaped tokens and malformed PR metadata. Validate a complete synthetic fixture as test data only. Confirm generated HTML escapes contributor text. Live GitHub: a negative PR fails and a valid PR passes checks but still waits for independent reviews; direct update/force push must be refused.

Least confident: the eventual app engine, actual volunteer capacity, provider operating budget, hardware coverage and whether this personal-account ruleset can express all desired restrictions. Record measured GitHub settings and gaps instead of claiming the plan enforced them.
