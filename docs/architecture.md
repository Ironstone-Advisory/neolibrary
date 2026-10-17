# Architecture

NeoLibrary is a pipeline of six layers sharing one provenance record.

| Layer | Input | Output | Notes |
|---|---|---|---|
| Access | A source (folder, mailbox export, chat export, drive, URL list) | `SourceItem`s | Done by connector plugins |
| Research | `SourceItem`s | Indexed, searchable items | Full text plus embeddings |
| Combine | Indexed items | A graph of links between items | Entities, topics, citations |
| Synthesize | Graph neighbourhoods | `KnowledgeObject`s | Human or model authored; always cites sources |
| Publish | `KnowledgeObject`s | Pages, feeds, exports | Markdown first |
| Track | Every step above | Provenance events | Append-only |

## Core types

Defined in [`src/neolibrary/core.py`](../src/neolibrary/core.py).

- `SourceItem`: one piece of raw material, with a stable id, origin URI, retrieval time and content hash.
- `KnowledgeObject`: synthesized content plus the ids of the items it was built from.
- `ProvenanceEvent`: who or what did what to which object, and when.

## Design rules

1. **Nothing without a source.** A knowledge object with no source ids is invalid.
2. **Hashes, not trust.** Every source item is hashed at ingest so later copies can be checked.
3. **Append-only provenance.** Events are never edited, only added.
4. **Plugins at the edges.** The core never talks to a vendor API directly; connectors do.
5. **Open core boundary.** Anything a single user or small team needs is open. Enterprise controls (SSO, audit export, regulatory reporting) are plugins.
