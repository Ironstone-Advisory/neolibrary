# NeoLibrary

*By Rob Tyrie, Ironstone Advisory · [ironstoneadvisory.com](https://ironstoneadvisory.com) · [@robtyrie](https://github.com/robtyrie)*

**NeoLibrary is an open engine that turns raw material into knowledge objects you can trace.**

It is a series of interconnected layers that let data be accessed, researched, combined, synthesized, published and tracked, so that it becomes new **knowledge objects** and **wisdom objects**. Every object carries its provenance: where it came from, who touched it, and what it was built from.

The base engine is free and open source under Apache 2.0. Commercial plugins and services are offered separately by Ironstone Advisory.

> Status: early. This repo holds the canonical definitions ([RFCs](rfcs/)), the architecture, the framework, the plugin contract and the provenance record. Working code lands here next.

## Start here

| If you want to know | Read |
|---|---|
| What NeoLibrary, MetaRAG and a knowledge object are | [RFC-0001: definitions and scope](rfcs/RFC-0001-definitions.md) |
| The rules every knowledge object follows | [RFC-0002: knowledge objects and the provenance spine](rfcs/RFC-0002-knowledge-objects-and-provenance.md) |
| How to extend it, and what's open vs. commercial | [RFC-0003: plugin contract](rfcs/RFC-0003-plugin-contract.md) |
| How the work is governed, and the gate before anything goes public | [RFC-0004: how NeoLibrary is built](rfcs/RFC-0004-how-we-build.md) |
| The Ironstone methods it's built with: the Creation Model, the Critical Thinking Cube, the Evidence Ladder | [RFC-0005](rfcs/RFC-0005-creation-model.md), [RFC-0006](rfcs/RFC-0006-critical-thinking-cube.md), [RFC-0007](rfcs/RFC-0007-evidence-ladder.md) |
| The client-facing overview | [NeoLibrary on ironstoneadvisory.com](https://www.ironstoneadvisory.com/insights/neolibrary) and [Ironstone Methods](https://www.ironstoneadvisory.com/what-we-do/ironstone-methods) |
| Where the idea came from | [MetaRAG and the NeoLibrary (June 2024)](docs/history/2024-06-metarag-and-neolibrary.md) and [PROVENANCE.md](PROVENANCE.md) |

---

## Why this exists

This is how information dies in the modern world. A group does real thinking together for years. The thinking lives in a Slack that hits its limit and shuts down, a Discord nobody remembers how to log into, WhatsApp threads, email attachments, and chat sessions with AI tools that are never exported. The people are still there. The knowledge is gone.

NeoLibrary is built so that does not happen: material goes in, it is turned into objects that keep their sources, and those objects stay findable, citable and reusable.

## The framework: DAC-EK and the NeoLibrary Helix

**v1, DAC-EK (March 14, 2025).** Five resources every knowledge system runs on: **D**ata, **A**lgorithms, **C**ompute, **E**nergy, **K**nowledge.

**v2, the NeoLibrary Helix (working draft, October 17, 2026).** Two strands wound around a provenance spine:

| Strand | Steps | What it is |
|---|---|---|
| Machine strand | Data, Algorithms, Compute, Energy | What the system runs on |
| Meaning strand | Information, Knowledge, Wisdom, Action | What people get out of it |
| Rungs | Knowledge objects | Each rung joins a machine step to a meaning step |
| Crossings | Action becomes new Data | The helix climbs instead of looping |
| Spine | Provenance | Runs up the centre; every object keeps its lineage |

![NeoLibrary Helix v2 working draft](docs/images/NeoLibrary-Helix-v2-draft.png)

The meaning strand builds on the DIKW hierarchy (Russell Ackoff, 1989). See [docs/framework.md](docs/framework.md) for versions and open questions.

## Architecture in one picture

```
 sources ──► ingest ──► objects ──► synthesize ──► publish
   │           │           │            │             │
   └───────────┴─── provenance spine (every step logged) ───┘
                           │
                       plugins (connectors, SSO, audit, reporting)
```

| Layer | Job |
|---|---|
| Access | Connect to sources: files, mail, chat exports, drives, archives |
| Research | Search, retrieve, cluster |
| Combine | Link material across sources into a graph |
| Synthesize | Produce knowledge objects and wisdom objects |
| Publish | Render objects for people and machines |
| Track | Record provenance for every object and every change |

Details: [docs/architecture.md](docs/architecture.md). Plugin contract: [docs/plugins.md](docs/plugins.md).

## Repos in this family

| Repo | What it holds | License |
|---|---|---|
| [neolibrary](https://github.com/Ironstone-Advisory/neolibrary) | The open engine (this repo) | Apache 2.0 |
| [neolibrary-commons](https://github.com/Ironstone-Advisory/neolibrary-commons) | Test dataset: the Grey Swan Guild sessions corpus | CC BY 4.0 |
| neolibrary-plugins | Commercial plugins (private) | Proprietary |

## Getting started

```bash
git clone https://github.com/Ironstone-Advisory/neolibrary
cd neolibrary
python -m pip install -e .
python -m pytest
```

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first: outside contributions are accepted under a Contributor License Agreement so the project can keep a clean open core.

## Ownership and credit

NeoLibrary was conceived, named and developed by Rob Tyrie. It is owned by **Ironstone Advisory**. The dated record is in [PROVENANCE.md](PROVENANCE.md); the people who helped shape it are in [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md).

"NeoLibrary" is a trademark of Ironstone Advisory. The Apache 2.0 license does not grant rights to the name; see [NOTICE](NOTICE).

## License

- **Code** (`src/`, `tests/`): [Apache License 2.0](LICENSE).
- **Documents** (`rfcs/`, `docs/`, and the Markdown files in this repo): [CC BY 4.0](LICENSE-docs). Share and adapt them freely; credit "Rob Tyrie, Ironstone Advisory".
- **Name:** "NeoLibrary" is a trademark of Ironstone Advisory; see [NOTICE](NOTICE).

To cite NeoLibrary, use [CITATION.cff](CITATION.cff). A machine-readable index of the canonical documents is in [llms.txt](llms.txt).

Copyright 2024-2026 Ironstone Advisory.
