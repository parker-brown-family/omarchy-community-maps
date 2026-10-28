# Omarchy Community Maps

An independent community effort toward maps and directions across Omarchy desktops, laptops, tablets and phones. Working product name: **Oma Maps**.

**This repository is the project foundation. No mapping application or device support is released yet.** The first milestone is one independently reproduced desktop trip. All device families have a place in the roadmap from the beginning.

- [Contribution map](docs/contribution-map.html): download and open the interactive local page, or use the [Markdown work map](docs/work-map.md).
- [Contribute](CONTRIBUTING.md) · [Agent entry point](AGENTS.md) · [Task packets](tasks/README.md).
- [Can this work across all devices?](docs/feasibility.md) · [Support matrix](docs/support-matrix.md).
- [Has anyone tested my exact device?](docs/devices.html) · [Add a model or test result](docs/device-registry.md). The model manifest is open-ended; placeholders and untested models carry no support claim.
- [PR proof and security](docs/review.md) · [Governance](GOVERNANCE.md).

## Join the work
We need maintainers, independent reviewers, developers, device testers, map/data specialists, accessibility testers and writers. You can contribute one bounded run of your preferred agent on your own account. Keep your credentials; agree the task and cap first. There is no central token pool.

A verified support cell needs repeatable evidence for exact hardware, OS and software revision. A build, upstream README, simulator or screenshot cannot certify physical navigation.

## Local checks
Python 3.11 or later; standard library only. From the repository root:

    python3 tools/validate.py
    python3 -m unittest discover -s tests -v
    python3 tools/render.py --check

For an agent-readable lookup, run `python3 tools/devices.py --query "Pixel 7 Pro" --json`. Compare the returned model identifier, OS build and app revision before reusing a result. An empty result means no matching evidence here.

Read unknown code before running it and use an isolated runner without credentials.

## Inspiration
[Omamesh](https://github.com/clartek/omamesh), [Omastorm](https://github.com/wesleygrimes/omastorm), [Phonechy](https://phonechy.org/) and [Omarchy Mobile](https://github.com/derekross/omarchy-mobile) inspired this initiative. [Derek Ross's device board](https://x.com/derekmross/status/2115174266979455346) inspired the capability matrix. These are independent projects; no endorsement or membership is implied. See [reuse decisions](docs/inspirations.md).

Original code and documentation use the [MIT license](LICENSE). Upstream code, databases, tiles and media retain their own terms. No map data is bundled.
