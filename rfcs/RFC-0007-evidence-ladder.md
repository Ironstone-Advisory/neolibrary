# RFC-0007: The Evidence Ladder

| | |
|---|---|
| Author | Rob Tyrie, Ironstone Advisory |
| Version | 0.9 |
| Status | Draft |
| Date | October 17, 2026 |
| Part of | The Startup Pitch Canvas (v4) |
| License | [CC BY 4.0](../LICENSE-docs) |

## Site summaries

For ironstoneadvisory.com and other short uses. Copy these as written; they change in the same commit as the RFC.

**One line**

Confidence can't be higher than the evidence under it.

**50 words**

The Evidence Ladder grades evidence from E0, an assertion, to E4, a result you've watched repeat. Your confidence in a claim is capped at the best grade behind it. Five rules keep the grades honest: the cap, a network discount, evidence against, staleness, and dependency between claims.

**200 words**

The Evidence Ladder is a simple discipline: you can't be more confident in a claim than the evidence under it allows. It was built for the Ironstone Startup Pitch Canvas but works on any claim, from a strategy to a forecast to a vendor's pitch.

Evidence is graded on five rungs. E0 is an assertion: something believed because someone said it. E1 is reported: interviews, surveys, analyst reports. E2 is observed: real behavior you watched, like a prototype in use. E3 is committed: someone paid or risked something, like a paid pilot or a signed letter of intent. E4 is repeated: several independent commitments with visible margins, and the only grade you may call validated.

Five rules keep the grades honest. Confidence is capped at the best grade. Evidence from friends and advisors counts one grade lower. Every claim needs evidence against it, or it stays at low confidence. Evidence older than about a year drops a grade. A claim can't be stronger than the claims it rests on.

For each claim, pick the cheapest test that would earn the next grade. That turns a pitch or plan into a list of experiments. Anything at E0 or E1 is presented as a hypothesis, never as a fact.

## Summary

Confidence can't be higher than the evidence under it. The Evidence Ladder grades every piece of evidence from E0 to E4, then caps how confident you're allowed to be in a claim at the best grade behind it. It turns "never upgrade a hypothesis into a fact" from a principle into a mechanism.

It was built for the Startup Pitch Canvas, where every block is a claim about the business, but it works on any claim: a strategy, a forecast, a Cube analysis or a knowledge object.

## The grades

| Grade | Name | What counts | Confidence allowed |
|---|---|---|---|
| **E0** | Assertion | Your belief, desk logic, a hunch. Something we believe because we said it | Low |
| **E1** | Reported | Interviews, surveys, analyst reports. Talk is cheap | Low |
| **E2** | Observed | You watched real behavior: a workflow, a prototype in use, an unpaid pilot | Medium at most |
| **E3** | Committed | The other party paid or risked something: a paid pilot, a deposit, a signed letter of intent | High |
| **E4** | Repeated | Several independent E3s with visible unit margins | The only grade you may call validated |

## The five rules

1. **Cap.** Confidence can't exceed the best evidence grade behind the claim.
2. **Network discount.** Evidence from friends, advisors and your own network counts one grade lower. A friend watching your demo is E1, not E2.
3. **Evidence against.** Log at least one piece of evidence against each claim, or write "none sought". None sought caps confidence at Low.
4. **Staleness.** Evidence older than about 12 months drops one grade. A paid pilot from 14 months ago is E2, not E3.
5. **Dependency.** A claim's effective grade is the lower of its own grade and the grades of the claims it rests on. A financial model built on an E1 market figure is an E1 model, however clean the spreadsheet.

Each rule closes a loophole. The cap stops a confident founder rating a hunch High. The network discount stops friendly feedback counting as demand. Evidence against forces a search for disconfirming proof. Staleness stops old wins propping up today's claims. Dependency stops a strong late claim hiding a weak early one.

## How to use it

For each claim, in order:

1. **Grade the evidence.** Apply the network discount and staleness first.
2. **Cap the confidence.** Never above the grade.
3. **Pick the next test.** The cheapest step that would earn the next grade. Every claim below E3 carries one, which is what makes a canvas a plan rather than a report.

Then roll up: apply the dependency rule across claims. The weakest early claims are where the next test goes.

When presenting, label any claim graded E0 or E1 as a hypothesis. Never present it as a fact.

### The kill list

In thinking work, write down every sentence that begins "this only works if," then rank them by what kills you when they're wrong. Grade each one. An assumption near the top of the kill list with E0 beside it is your first experiment. The cheapest test is often careful reading: plenty of assumptions dissolve once you check exactly how the underlying question was worded.

## Why it matters now

Fluent prose costs nothing now. Describe any plan to a language model, including a bad one, and five confident pages come back. Clear writing used to be weak evidence of clear thinking; that evidence is gone. So grade the evidence under the claims, not the quality of the writing.

## In NeoLibrary

A knowledge object can carry an evidence grade on each claim it makes, with the sources that justify the grade on its provenance spine ([RFC-0002](RFC-0002-knowledge-objects-and-provenance.md)). That's a proposed use, not yet part of the object schema.

## History

| Date | What | Source |
|---|---|---|
| The five years to Oct 2026 | The Startup Pitch Canvas develops: claim, evidence, risk and confidence on every block | Rob's Ironstone method; v3 workbook, CC BY 4.0 |
| Oct 11, 2026 | The ladder, the cap and the dependency rule are added in Canvas v4. Proposed by Claude in a critique Rob asked for, then adopted and revised by Rob (AI-assisted) | Claude conversation "Startup pitch methodology critique" |
| Oct 13, 2026 | Used in the Think chapter of the Eight Energies manuscript (the kill list) | Claude conversation "Creator model conversations" |
| Oct 2026 | Published: "Confidence cannot be higher than the evidence" | [Ironstone Methods](https://www.ironstoneadvisory.com/what-we-do/ironstone-methods) |

## Change log

- 0.9 (October 17, 2026): first written definition, compiled from Canvas v4 (October 11, 2026). Drafted with Claude (AI-assisted).
