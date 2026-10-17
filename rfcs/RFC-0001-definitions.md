# RFC-0001: NeoLibrary, definitions and scope

| | |
|---|---|
| Author | Rob Tyrie, Ironstone Advisory |
| Version | 1.0 |
| Status | Accepted |
| Date | October 17, 2026 |
| License | [CC BY 4.0](../LICENSE-docs) |

## Summary

NeoLibrary is an engine that turns a collection of documents into connected knowledge objects that keep their sources, so people and AI systems can find, combine, synthesize and publish knowledge without losing track of where it came from. This RFC fixes the vocabulary. Every other RFC uses these words in exactly these senses.

## Why it exists

Organizations and communities lose what they know. The thinking happens in chat tools, recorded calls, email threads and AI sessions that are never exported. When a workspace hits its limit or a login is forgotten, the knowledge goes with it, even though the people are still around.

Large language models make the problem sharper. They can answer anything, but in a narrow domain they hallucinate, because they aren't grounded in the material that domain agrees on. NeoLibrary grounds them in a library: a curated, structured, consensus body of documents whose every part can be traced.

## Where the idea came from

In June 2024 Rob Tyrie called the first version of this idea **MetaRAG**: instead of grounding prompt creation in a database, ground it in a library of books that are closely related to the subject and broadly agreed on. Thinking about what a modern library of books really is led him to generalize MetaRAG into the **NeoLibrary**. The dated record is in [PROVENANCE.md](../PROVENANCE.md).

## Definitions

**NeoLibrary.** A series of interconnected layers that let material be accessed, researched, combined, synthesized, published and tracked, turning it into new knowledge objects and wisdom objects. The layers are Access, Research, Combine, Synthesize, Publish and Track; see [architecture](../docs/architecture.md).

**MetaRAG.** Retrieval-augmented generation that retrieves from a curated, consensus library of documents and uses their whole structure (contents, ordering, sections, summaries, notes, references and index) rather than isolated text fragments. MetaRAG is how a model reads a NeoLibrary.

**Book (document).** The two words mean the same thing. A book is a collection of knowledge objects together with its full structure: table of contents, chapter ordering, the shape of each section, end-of-chapter lessons, summaries and quizzes, concordance, notes, references and index. The structure is part of the knowledge, not packaging around it.

**Library.** A collection of books, plus the links among them.

**Source item.** One piece of raw material as it arrived: a file, a message, a transcript, a page. It's hashed when it enters the library so any later copy can be checked against it.

**Knowledge object.** The smallest unit of synthesized knowledge that can stand on its own and be cited. It carries its content, the source items it was built from, and the history of everything done to it. A knowledge object with no sources is invalid. RFC-0002 specifies it.

**Wisdom object.** Reserved. It will name what results when knowledge objects are applied to a decision and the outcome is recorded. It isn't defined until a later RFC defines it.

**Provenance.** The recorded chain from a source item to every object built from it, including who or what acted at each step and when.

**Provenance spine.** The single, append-only provenance record that runs through every layer of a NeoLibrary. Nothing enters, changes or leaves without an entry on the spine.

**Neolibrarian.** A person who curates a NeoLibrary: deciding what enters, how it's structured, which sources are authoritative, and what gets published.

**Neo Librarian (agent).** An AI agent that does librarian work under a Neolibrarian's direction: reading documents, extracting entities, proposing links, answering questions and recommending material. It always cites the knowledge objects it used.

**DAC-EK.** Five resources every knowledge system consumes: Data, Algorithms, Compute, Energy and Knowledge (Rob Tyrie, March 14, 2025).

**NeoLibrary Helix.** The second version of DAC-EK (working draft, October 17, 2026). A machine strand (Data, Algorithms, Compute, Energy) and a meaning strand (Information, Knowledge, Wisdom, Action) wind around the provenance spine. Rungs are knowledge objects; at each crossing, action produces new data, so the structure climbs instead of looping. The meaning strand builds on Ackoff's DIKW hierarchy (1989). See [framework](../docs/framework.md).

## Scope

In scope: ingesting documents, building knowledge objects with provenance, linking them into a graph, retrieving and synthesizing from them, and publishing results that cite their sources.

Out of scope: running a lending library (holds, loans, fines), and replacing a records-management or integrated library system. NeoLibrary connects to those instead of rebuilding them.

## Open core

The engine and these definitions are open: code under Apache 2.0, documents under CC BY 4.0. Commercial plugins and services from Ironstone Advisory add enterprise controls on top. RFC-0003 draws the line. "NeoLibrary" is a trademark of Ironstone Advisory; the open licenses don't grant use of the name.

## Change log

- 1.0 (October 17, 2026): first accepted version.
