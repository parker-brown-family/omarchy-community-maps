# Releases

No map binary is released by this bootstrap. Green PRs do not authorize publication.

Before first release: appoint custodian/security reviewer; build a protected commit with pinned inputs; produce SBOM/license inventory, provenance, hashes and verifiable signature. Keep signing authority out of PR jobs. Configure protected release environment, independent human approval and no self-review where supported.

Test exact artifact against explicit device/OS/capability scope, update/downgrade/rollback, pack compatibility and known failures. Do not expand a tested Pixel to all phones or one ARM board to all aarch64. Publish support owner and data terms.

REL-01 owns this gate, including tag mutation/deletion protection. No auto-release workflow or signing secret exists now.
