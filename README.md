# Omarchy Community Maps

An independent community effort to build a sovereign maps utility for Omarchy desktops, laptops, tablets and phones. Working product name: **Oma Maps**. Our long-term destination is the breadth and depth of Google Maps: places, directions, transit, offline use, imagery and useful local information.

## Sovereignty

A core planning trip should require no Google service or account, use inspectable software and permitted data, and have a documented way to replace its data source. Transparency means being able to inspect, understand and improve the pieces, see what leaves the device, and repair weak links in the data or security chain. Offline operation is a separate capability that we test explicitly.

We build from existing open-source pieces and contribute improvements where they fit. Software freedom, data rights, operational control and privacy each need evidence. These are acceptance requirements; the project has not met them yet.

## Start here

**This repository is the project foundation. No mapping application or device support is released yet.** The first milestone is one independently reproduced desktop trip. All device families have a place in the roadmap from the beginning.

- [Product roadmap](docs/roadmap.md) · [Reuse map](docs/reuse-map.md) · [Research handoff](docs/research/reuse-handoff-2026-10-28/AGENT_HANDOFF.md).
- [Contribution map](docs/contribution-map.html): download and open the interactive local page, or use the [Markdown work map](docs/work-map.md).
- [Contribute](CONTRIBUTING.md) · [Agent entry point](AGENTS.md) · [Task packets](tasks/README.md).
- [Can this work across all devices?](docs/feasibility.md) · [Support matrix](docs/support-matrix.md).
- [PR proof and security](docs/review.md) · [Governance](GOVERNANCE.md).

## Join the work
We need maintainers, independent reviewers, developers, device testers, map/data specialists, accessibility testers and writers. You can contribute one bounded run of your preferred agent on your own account. Keep your credentials; agree the task and cap first. There is no central token pool. Intake is open without a fixed task-count or founder-attention cap. Agents help assess what to include, dismantle for useful parts, rebuild or reject; protected branches, required checks and independent review control integration.

A verified support cell needs repeatable evidence for exact hardware, OS and software revision. A build, upstream README, simulator or screenshot cannot certify physical navigation.

## Local checks
Python 3.11 or later; standard library only. From the repository root:

    python3 tools/validate.py
    python3 -m unittest discover -s tests -v
    python3 tools/render.py --check

Read unknown code before running it and use an isolated runner without credentials.

## Inspiration
[Omamesh](https://github.com/clartek/omamesh), [Omastorm](https://github.com/wesleygrimes/omastorm), [Phonechy](https://phonechy.org/) and [Omarchy Mobile](https://github.com/derekross/omarchy-mobile) inspired this initiative. [Derek Ross's device board](https://x.com/derekmross/status/2115174266979455346) inspired the capability matrix. These are independent projects; no endorsement or membership is implied. See [reuse decisions](docs/inspirations.md).

Original code and documentation use the [MIT license](LICENSE). Upstream code, databases, tiles and media retain their own terms. No map data is bundled.
