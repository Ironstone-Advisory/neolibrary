# RFC-0002: Knowledge objects and the provenance spine

| | |
|---|---|
| Author | Rob Tyrie, Ironstone Advisory |
| Version | 1.0 |
| Status | Accepted |
| Date | October 17, 2026 |
| Depends on | RFC-0001 |
| License | [CC BY 4.0](../LICENSE-docs) |

## Summary

Every piece of knowledge in a NeoLibrary is a knowledge object that names its sources and keeps its history. This RFC sets the rules those objects follow and the events the provenance spine records.

## The problem it solves

Most AI systems can tell you an answer but not where it came from. Once a summary is separated from its sources, nobody can check it, credit it, correct it or bill for it. NeoLibrary makes the link between a claim and its source a property of the data, not a courtesy.

## The four types

**Source item.** Raw material as it arrived. Fields: a stable id, the origin (URI or system reference), the content, a SHA-256 hash of the content, the time it was retrieved, and its license and attribution.

**Knowledge object.** Synthesized knowledge. Fields: a stable id, a title, the body, the ids of its sources, its author (human or agent), its license and attribution, and its history.

**Document.** An ordered collection of knowledge objects with structure: contents, sections, summaries, notes, references and index (RFC-0001: book and document mean the same thing).

**Provenance event.** One entry on the spine: which object, what happened, who or what did it, when, and a note.

## Rules

1. **No object without a source.** Creating a knowledge object with no source ids fails.
2. **Hash at the door.** Every source item is hashed when it enters. Later copies are checked against the hash, not trusted.
3. **Append only.** Provenance events are added, never edited or deleted. A correction is a new event that points at the one it corrects.
4. **License travels with content.** A knowledge object inherits the license and attribution of its sources. If any source is CC BY, the object carries that credit into every output built from it.
5. **Machine output is marked.** A field produced by a model records the model, the source objects used, and a confidence. When a human or an authoritative source disagrees, the human or authoritative value wins and the override is itself an event.
6. **Derivation is provenance.** Editions, translations, excerpts and syntheses are relationships on the spine, not loose copies.

## Event types

| Event | Meaning |
|---|---|
| `ingested` | A source item entered the library |
| `created` | A knowledge object was made from sources |
| `edited` | Content changed; the note says what and why |
| `derived-from` | This object was built from another object |
| `edition-of` | A later version of the same work |
| `translation-of` | The same work in another language |
| `part-of` | This object belongs to a document or collection |
| `overridden` | A human or authoritative value replaced a machine value |
| `published` | The object went out in a given format and place |

## Mapping to Dublin Core

So NeoLibrary can trade metadata with libraries and repositories, the core fields map onto Dublin Core:

| Dublin Core | NeoLibrary |
|---|---|
| `identifier` | id |
| `title` | title |
| `creator` | author |
| `date` | created time, or retrieved time for a source item |
| `source` | source ids (for a knowledge object), origin (for a source item) |
| `rights` | license and attribution |
| `relation` | `derived-from`, `edition-of`, `translation-of`, `part-of` events |
| `format` | the format recorded on a `published` event |

## Reference implementation

`src/neolibrary/core.py` implements rules 1 to 3 today. Rules 4 to 6 and the event vocabulary are the next pieces of work, tracked against this RFC.

## Change log

- 1.0 (October 17, 2026): first accepted version.
