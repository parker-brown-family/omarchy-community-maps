# Security policy

No application release is supported yet. Repository infrastructure and contribution handling are the initial scope.

Use **Security → Report a vulnerability** for private reports. Do not put credentials, exploits or location histories in public issues. If unavailable, request a private channel via the owner's GitHub profile; do not send the secret itself. No response SLA is promised while the security steward is vacant.

Trusted policy runs base-branch code and reads proposed files as bounded data. It never executes contributor programs. PR tests run on disposable GitHub-hosted runners with read-only permissions and no deployment secrets. No self-hosted runners are attached.

Review inputs, downloads/packs, dependencies, location privacy, permission revocation, workflows and signing. Passing checks do not establish absence of vulnerabilities. See docs/review.md and docs/releases.md.
