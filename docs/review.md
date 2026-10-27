# PR proof and security

Every PR comes from an untrusted branch. Explanations, tests and receipts remain claims until checked.

## Server rules
Protect master, main and release branches: PRs, two approvals, code-owner review, stale-review dismissal, approval after last push, resolved conversations, strict required checks, no force pushes/deletion, no bypass actors. Actual readback lives in admin-verification.json; missing means unverified.

## Two checks
trusted-policy runs protected-base code. It fetches a bounded GitHub tree/blob snapshot as data, never checks out/executes contributor code, imports proposed modules, installs dependencies or consumes workflow artifacts. It rejects symlinks/submodules, traversal, excessive files/bytes, malformed evidence/registries and incomplete PR disclosures. It uses read-only permissions, no secrets, no caches and no publishing authority.

repository-checks runs proposed tests on a disposable GitHub-hosted runner with read-only access and no secrets. A PR can change these tests, so its green badge is not independent proof. The base-policy gate and mandatory human code review remain separate. External actions are pinned to verified full SHAs.

## Human review
Inspect exact diff, dependencies, licenses, inputs and permissions. Reproduce acceptance in isolation. Read workflow/test changes. Require failure cases, failed attempts and explicitly unrun tests. AI reviews are advisory; two actual independent people approve.

Physical support needs exact hardware/OS/revision, procedure, expected/observed result, artifact hashes and independent reviewer. A model cannot verify a walk. Schema validation cannot prove a report truthful or an account human.

CI, validator, ownership, governance, location/privacy, parsers/downloads and releases require domain/security review. Protected-base changes take effect only after that reviewed merge.

## Limits
The seed is one direct bootstrap push before rules, without collaborators; subsequent changes use PRs. A personal owner can edit settings, so account compromise remains. Merges wait for reviewers rather than weaker rules. No self-hosted runner or signing secret is attached. Public binaries wait for release controls.

Required GitHub Actions check contexts identify an app and check name, not a cryptographically fixed workflow. Review workflow-name collisions and changes to event triggers; green checks alone never authorize a merge. A personal repository has no independent organization-wide policy administrator. SEC-01 includes auditing these limits before adding collaborators or privileged automation.
