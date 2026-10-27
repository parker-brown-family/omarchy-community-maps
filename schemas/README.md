# Contracts

tools/validate.py is the executable schema. Templates are excluded from evidence. Unknown is null, never an invented zero.

IDs are unique and references resolve. Task dependencies are acyclic. Vacant roles have no maintainers. Candidate profiles can have unknown hardware/OS.

Evidence statuses: not-tested, observed, failed, verified. Kinds: source, replay, emulator, physical. Verified requires physical input, exact revision/hardware/OS, source date, declared expiry, procedure, expected/observed, artifact hashes and different operator/reviewer. Expired support is stale. Schema checks do not prove truth or reviewer identity.

Artifacts contain url, sha256, description. Run receipts permit null measurements; cost_kind is unknown, measured or estimated; estimates carry method.
