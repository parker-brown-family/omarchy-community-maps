# Architecture

Use one repository for coordination, typed evidence and small integration experiments. Reuse existing navigation applications before selecting a new rendering stack. Keep map display, place search, routing, location, offline packs and platform shells separate in the design; select an engine only after a comparative desktop trial.

JSON registries hold roles, platform profiles, capabilities, tasks and evidence. Markdown packets carry reproducible scope and acceptance checks. A Python standard-library validator checks references and evidence requirements. A deterministic renderer produces a self-contained contribution map and Markdown indexes. Unknown values stay null or not-tested.

GitHub hosts public issues and forks. Protected master (plus main and release branches) requires two approvals, code-owner review, stale-review dismissal, approval after the last push, resolved conversations and passing named checks. No bypass actors are configured. Founder custody is temporary; ordinary merges wait for enough independent human maintainers.

A trusted pull_request_target workflow checks out only the protected base and runs its validator. It obtains the proposed tree and blobs through the GitHub API as bounded data, never executes or checks out proposed code, and uses a read-only token. An ordinary pull_request workflow runs proposed tests on ephemeral GitHub-hosted runners with read-only permissions and no secrets. Neither publishes packages or deploys. No agent receives repository credentials from a token donor.

No production endpoints, database, paid maps account or deployment exists. Future services need a named operator, budget and terms review. Location stays local unless a person explicitly opts into a feature that sends it.
