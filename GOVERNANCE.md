# Governance

Parker (parker-brown-family) is initial repository custodian. This does not commit him to daily maintenance. Operational roles begin vacant. A person must explicitly accept scope and availability before appointment.

The steward prioritizes/caps work; domain maintainers select engineering approaches; reviewers independently verify; security reviews trust boundaries; the data steward owns provider terms/budgets/outages. Device operators report observations and a separate reviewer certifies their exact scope.

Agents may propose, implement and test. They cannot appoint maintainers, accept terms, spend others' funds, grant access, certify their own physical results or release software.

## Merge authority
Every PR requires two independent approving reviews, including a code owner. Neither reviewer may be the author; the last push requires another person's approval. The founder is initially the sole CODEOWNER, so ordinary merges deliberately wait for independent humans. A named JSON role grants no platform access.

Recruit with read/triage access first. Grant write only after identity, relevant review examples, scope, availability and security practices are checked. No admin grant for an agent task; no shared personal token. Initial accepted maintainers can be granted write by the custodian so they can review the ownership PR without relaxing review counts.

A personal repository cannot provide organization team isolation. Before scale or signing secrets, consider community organization ownership and multiple admins. The owner can edit protections; branch rules cannot prevent compromise of that account.

## Disputes and incidents
Record options with evidence. Domain maintainer plus independent reviewer selects the approach. Security/data objections hold the change until resolved. No bot approval or auto-merge. Stop publication and revoke exposed credentials during incidents; record all temporary settings changes with before/after evidence.

## Pilot
Open intake has no fixed two-task, fourteen-day or founder-attention limit. Parker explicitly accepts a potentially large contribution queue. Each contributor still owns their time/compute cap; no intake decision commits project funds.

Agents inspect contributions and recommend including them, dismantling them for useful parts, rebuilding from a bounded specification, or rejecting them with evidence. They cannot bypass branch rules, grant approval, appoint maintainers or self-certify. Integration still requires the independent human reviews above.

Read-only source research and local fixtures can proceed while operational roles are being recruited. A hosted service, release or support claim waits for its actual operator, rights, security and evidence prerequisites. Measure review backlog and time so the custodian can prioritize; a growing queue alone does not close intake.
