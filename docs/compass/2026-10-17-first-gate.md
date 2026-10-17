# Compass gate record: October 17, 2026

*By Rob Tyrie, Ironstone Advisory. Licensed [CC BY 4.0](../../LICENSE-docs). Rule: [RFC-0004](../../rfcs/RFC-0004-how-we-build.md).*

The first gate run, covering everything public in `neolibrary`, `neolibrary-commons` and `adaptivegaming` on October 17, 2026.

## 1. Instrument check: failed

The Bullshit Compass v1 reference code (`Ironstone-Advisory/BullshitCompass`, file `code`) was run unmodified, with NLTK stopwords supplied from spaCy because the NLTK download is blocked in this environment.

| Calibration sample | Expected | Score |
|---|---|---|
| "We are leveraging synergistic paradigms to actualize next-generation value-added solutions." | high | 0.04 ("clear and substantive") |
| "The project deadline is May 15th. We need to deliver the database migration and API endpoints by then." | low | 0.00 |

The fluffy sample barely registers, and on longer documents two components saturate: tautology hits 1.0 because spaCy vector similarity is high between almost any pair of sentences in a long text, and semantic emptiness sits around 0.95 for every file. The scores (0.20 to 0.43 across the public files) therefore can't tell good prose from bad. **Finding for Compass v2: fix calibration first** (sentence-pair similarity needs a far higher threshold or a contextual model, and emptiness needs normalizing for document length).

## 2. Manual reading against the RFC FS02 indicators

Because the code failed calibration, each public document was read against the nine indicators.

| Document | Indicators that fired | Decision |
|---|---|---|
| RFCs 0001 to 0004, README, GOVERNANCE, PROVENANCE, framework, architecture | None material. Claims are specific and dated; terms are defined before use | Pass |
| `docs/history/2024-06-metarag-and-neolibrary.md` | None material | Pass |
| `docs/history/2024-09-10-memory-objects-op-ed.md` | Buzzword load and emotional persuasion ("revolutionize", "bastions") | Accepted: a verbatim 2024 record, labelled AI-assisted; not to be quoted as current method |
| Sep 19, 2024 essays | Buzzword load, emotional persuasion, pseudo-profound framing; obviously generated | Removed from public earlier the same day; kept in the private archive |
| `neolibrary-commons` workbook | AI-invented editors and contributors (false attribution) | Fixed before publishing |
| `adaptivegaming` README and docs | Assertion ambiguity on two details: the session recording and the job titles of participants, both from Rob's own account | Accepted; sourced to Rob's Oct 5, 2024 email |

## 3. AI-generated content

All public documents were drafted with AI assistance under Rob Tyrie's direction and read in full before publishing.

## Addendum: RFCs 0005 to 0007 (October 17, 2026, afternoon)

The v1 code still fails calibration, so these were read against the nine RFC FS02 indicators.

| Document | Indicators that fired | Decision |
|---|---|---|
| RFC-0005 Creation Model | Assertion ambiguity on the energy order (two versions stated the same day) | Accepted as Draft; the conflict is stated in the RFC as an open question |
| RFC-0006 Critical Thinking Cube | Pseudoscience rhetoric in the 2024 source (the 5 Hows tied to "the prefrontal cortex") | Fixed: the brain claims were dropped and the cognitive links labelled as design rationale, not tested claims. The worked example on a named company was left in the private archive |
| RFC-0007 Evidence Ladder | None material. Grades and rules are specific and checkable | Pass |

All three are labelled AI-assisted, with the share of the work that was AI stated in each history table.

## Addendum: RFC-0006 version 1.0 (October 17, 2026)

Read against the RFC FS02 indicators. The cognitive-psychology rationale from the September 2024 version was not carried into 1.0, so the pseudoscience flag no longer applies. The 5 Wise section requires simulated points of view to be labelled as simulations, which covers assertion ambiguity. Cynefin is credited to Dave Snowden. Pass.

## Addendum: site summaries in RFCs 0005 to 0007 (October 17, 2026)

Read against the RFC FS02 indicators. Each summary restates its RFC and adds no claims of its own; no buzzword load or emotional persuasion. Pass.

## Addendum: RFC-0005 1.0 and RFC-0004 1.1 (October 17, 2026)

Read against the RFC FS02 indicators. The 2022 origin rests on Rob's own statement and the RFC says no 2022 document has been found, which keeps assertion ambiguity in check. Pass.

## Addendum: RFC-0005 1.1 and RFC-0004 1.2 (October 17, 2026)

Read against the RFC FS02 indicators. "Quantum" is borrowed from physics and could read as pseudoscience rhetoric, so the RFC defines it in plain words (a whole, usable unit of an energy's output) and gives examples. Pass.

## Addendum: RFC-0005 1.2 (October 17, 2026)

Read against the RFC FS02 indicators. The message table uses concrete examples, and "level of energy" and "level of done" are defined in plain words. Pass.

## Addendum: RFC-0005 1.3 and RFC-0004 1.3 (October 17, 2026)

Read against the RFC FS02 indicators. Each energy's output is stated concretely (ideas, systems, inputs and outputs, repeated runs, opportunities). Pass.

## Addendum: RFC-0005 1.4 (October 17, 2026)

Read against the RFC FS02 indicators. "Retrievable memory" is given a test (retrieval, not storage) and concrete examples per energy. Pass.

## Addendum: RFC-0005 1.5 and PROVENANCE (October 17, 2026)

Read against the RFC FS02 indicators. The July 2023 remark is paraphrased from the private transcript with its source named; the claim that NeoLibrary was built with the model is attributed to Rob's October 17, 2026 statement. Pass.

## Addendum: RFC-0005 1.6 (October 17, 2026)

Read against the RFC FS02 indicators. Intrinsic and extrinsic are defined by one test (does the company control it), with examples of each feedback loop. Pass.
