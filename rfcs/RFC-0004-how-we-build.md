# RFC-0004: How NeoLibrary is built: the creative flow and the skeptic gate

| | |
|---|---|
| Author | Rob Tyrie, Ironstone Advisory |
| Version | 1.3 |
| Status | Accepted |
| Date | October 17, 2026 |
| License | [CC BY 4.0](../LICENSE-docs) |

## Summary

Everything in the NeoLibrary repos is made with Rob Tyrie's creative flow, the Ironstone creator model ([RFC-0005](RFC-0005-creation-model.md)): **ideate, think, make, do, judge, decide, execute, archive**. A skeptic wraps the whole flow and can be called into any part of it. It's required in exactly one place: nothing goes public until the Bullshit Compass has run on it at least once.

## The creative flow

These are energies, not a production line, and there is no order of execution: each energy works until it reaches a quantum, a usable unit of its own output, and then taps the others ([RFC-0005](RFC-0005-creation-model.md)). They connect as a graph, and the whole flow can run again inside any single energy, governed by that energy. A big "make" contains its own small ideate, think and judge.

| Energy | What happens | What it produces in these repos |
|---|---|---|
| **Ideate** | Generate possibilities without filtering them | Notes, sketches, rough prompts, issues |
| **Think** | Turn the idea into a system: its parts, how they connect, its inputs and outputs | Draft RFCs, definitions, diagrams |
| **Make** | Build the first real thing | Code, documents, designs |
| **Do** | Run the system for real, repeatedly | Runs against the commons corpus, pilots |
| **Judge** | Assess quality and outcome against the intent | Reviews, critiques, test results, a Compass reading |
| **Decide** | Choose a direction from the judgment: go left or go right | Accepted RFCs, merged pull requests, a change log entry |
| **Execute** | Orchestrate all the energies and bring the work to market | Releases, published pages, public commits |
| **Archive** | Keep the work, the decision and the lesson so the next loop starts from them | PROVENANCE, the private evidence archive, change logs, the commons corpus |

### Who leads

Rob leads every energy. AI tools amplify, drafting, generating options, checking and building at speed, and the record shows which is which: commits are authored by Rob, and AI involvement is stated in co-author lines and in "AI-assisted" labels on documents (see [PROVENANCE.md](../PROVENANCE.md)).

## The skeptic: an aspect, not a stage

The skeptic isn't a step you pass through once. It wraps all the energies, and you call it into whichever one needs it. Its instruments:

- **The Critical Cube** (Ironstone Critical Thinking Cube, [RFC-0006](RFC-0006-critical-thinking-cube.md)) for assessing a situation: six faces (the 5 Ws, 5 Whys, 5 Hows, 5 Whens, 5 Wise and 5 Weirds), each sorted into SWOT quadrants, with the 5 Wise as points of view that change with the problem.
- **The Bullshit Compass** for separating signal from noise in any artifact. It reads language patterns, not truth or intent: tautology, ideological smuggling, semantic drift, assertion ambiguity, buzzword load, pseudoscience rhetoric, emotional persuasion, Orwellian obfuscation and data-presentation obfuscation, adjusted for the kind of text it is Version 1 is RFC FS02 v0.88 with its reference code ([Ironstone-Advisory/BullshitCompass](https://github.com/Ironstone-Advisory/BullshitCompass)); version 2, the active version, began in September 2026 and inherits v1's history ([Ironstone-Advisory/bullshit-compass-v2](https://github.com/Ironstone-Advisory/bullshit-compass-v2)).
- **Named critics** to get the good, the bad and the ugly in a recognizable voice. Critiques "in the voice of" Galloway, Mintzberg, Graeber or Jobs are simulations of their published views, labelled as such, and never quoted as their words.
- **The Evidence Ladder** ([RFC-0007](RFC-0007-evidence-ladder.md)) for grading the evidence under a claim and capping confidence at that grade.
- **The Skepticism Maturity Model** for judging the quality of the critique itself.

## The one fixed gate

**Nothing goes public until the Bullshit Compass has run on it at least once.** This is the only place the skeptic is mandatory; everywhere else it's called by choice.

"Public" means: a commit to a public repository, a published page, a release, or text sent outside Ironstone. The gate sits at the point where Execute makes something visible to strangers (Ironstone Axiom: if it can be seen by strangers, it's production).

A pull request to a public repo passes the gate when its description records:

1. That the Compass ran on the changed prose, and the result (a score, or the indicators that fired).
2. What was changed because of it, or why a flag was accepted.
3. Anything AI-generated, and that a person read it in full.

Per the Compass's own rules, a reading is a prompt for judgment, not a verdict. It never decides truth or intent.

A Compass run counts only if the instrument passes its own calibration first: a known-fluffy sample must score worse than a known-plain one. If the code fails calibration, the run is done by reading the text against the RFC FS02 indicators, and the record says so. Gate records live in [docs/compass/](../docs/compass/).

## Invariants

These hold in every energy:

- **Newton before quantum.** Use the simple, established method first; reach for the exotic one only when the simple one fails.
- **The model is the asset.** The durable value is the method and the model of the domain, written down, not any single output.
- **Beauty is a requirement.** Clear, well-made work is part of "done", not decoration.
- **Plan before costly builds.** Anything expensive to undo gets a written plan first.

## Change log

- 1.3 (October 17, 2026): Think builds systems, Do runs them repeatedly, Execute orchestrates everything (RFC-0005 1.3).
- 1.2 (October 17, 2026): no order of execution; energies tap each other once they reach a quantum.
- 1.1 (October 17, 2026): the flow brought into line with [RFC-0005](RFC-0005-creation-model.md): Judge comes before Decide, and Archive is added, as confirmed by Rob Tyrie.
- 1.0 (October 17, 2026): first accepted version. The creative flow as stated by Rob Tyrie on October 17, 2026. An earlier eight-part draft named the public gate "Stake (Compass, ship)"; this version places the same gate at the point where Execute goes public.
