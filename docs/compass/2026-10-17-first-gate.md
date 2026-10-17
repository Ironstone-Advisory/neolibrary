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
