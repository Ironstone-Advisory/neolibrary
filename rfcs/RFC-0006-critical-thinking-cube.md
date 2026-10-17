# RFC-0006: The Ironstone Critical Thinking Cube

| | |
|---|---|
| Author | Rob Tyrie, Ironstone Advisory |
| Version | 1.0 |
| Status | Accepted |
| Date | October 17, 2026 |
| Also called | The Critical Cube, the Ironstone Cube |
| License | [CC BY 4.0](../LICENSE-docs) |

## Summary

A difficult question has more than one face. The Cube is a way to turn a question around before you get attached to an answer. It has six faces, and each one is a set of five: **the 5 Ws, the 5 Whys, the 5 Hows, the 5 Whens, the 5 Wise and the 5 Weirds**. Each face's answers are then split across a SWOT grid, so you see what's strong, what's weak, what's open and what's dangerous from every side.

I use it for critical thinking, decisions and problem-solving, especially when the first answer is probably too easy. It was built for speed. Before generative AI, analysing an enterprise-scale problem this thoroughly needed expensive outside strategy consultants. With a structured prompt, a team can cover the problem space and the solution space in an afternoon.

## Before the cube: the foundation

Write three lines before turning the cube at all:

- **Base assumption.** What are we taking as true?
- **Context.** What's happening around this?
- **Key question.** The one question the analysis has to answer.

If you can't write the key question in one sentence, you're not ready for the cube.

## The six faces

| Face | Five of what | What it's for |
|---|---|---|
| **5 Ws** | Who, what, where, when, why | Context. Gather enough of it before solving anything |
| **5 Whys** | Ask why five times, each answer feeding the next question | Root cause. Get under the first explanation |
| **5 Hows** | Five how-questions, each more specific than the last | Action. The fifth how should be something a person can do this week |
| **5 Whens** | Five timing questions: when to start, first release, the next milestones, when the market is mature | Sequence. What has to happen before what, and how long it really takes |
| **5 Wise** | Five wise points of view, chosen for this problem | Judgment. See the question through other eyes before deciding |
| **5 Weirds** | Five "what if" questions that break an assumption | Disruption. Find the move nobody else in the room would suggest |

### The 5 Wise

The 5 Wise are five points of view, and they change with the problem. For an AI product they might be an ethicist, a linguist, a business strategist, a cognitive scientist and an end user. For an insurance workflow they might be an underwriter, a broker, a regulator, a claims adjuster and the policyholder. Pick people whose disagreement would teach you something. At least one of them should be the person who has to live with the result.

A wise point of view used in a write-up is a simulation of how that kind of person would see it. If you name a real person, label it as a simulation and never quote it as their words.

### The 5 Weirds

The 5 Weirds are deliberately strange. "What if the product could switch levels at will?" "What if the customer were the supplier?" Most get thrown away. One usually survives and changes the plan. Run this face after the others, when you know enough to break the right assumption.

## The SWOT grid on every face

Each face's answers get sorted into four quadrants: **strengths, weaknesses, opportunities and threats**. The 5 Ws in a SWOT grid show whose interests help or hurt you. The 5 Whens in a SWOT grid show which timing works for you and which works against you. Sorting every face this way is what turns six lists into a decision.

## After the cube: the Cynefin check

Close by placing each part of the problem in a Cynefin domain (Dave Snowden's framework):

- **Clear:** known answers. Apply best practice.
- **Complicated:** answerable by experts. Analyse, then act.
- **Complex:** unknowns that only experiments reveal. Probe, then act.
- **Chaotic:** no stable pattern yet. Act to stabilize first.

Then state how uncertain the whole picture is. The Cynefin check tells you which parts of the plan to execute and which to run as experiments.

## Using it with an AI model

The Cube works as a structured prompt. A model fills the faces quickly. Treat that output as a first draft: a model reading a company's website produces E0 and E1 evidence at best, so grade the claims with the [Evidence Ladder](RFC-0007-evidence-ladder.md) before acting on them. The 5 Wise and the 5 Weirds are where a model helps most and where it most needs a human to throw half of it away.

```toml
[critical_cube]
subject = "The question or company being analysed"

[critical_cube.foundation]
base_assumption = "What are we taking as true?"
context = "What is happening around this?"
key_question = "The one question this analysis must answer"

[critical_cube.five_ws]
who = ""
what = ""
where = ""
when = ""
why = ""

[critical_cube.five_whys]
why_1 = ""
why_2 = "Why is the answer to why_1 true?"
why_3 = ""
why_4 = ""
why_5 = "The root cause"

[critical_cube.five_hows]
how_1 = ""
how_2 = ""
how_3 = ""
how_4 = ""
how_5 = "An action someone can take this week"

[critical_cube.five_whens]
when_1 = "When to start"
when_2 = "When the first version ships"
when_3 = ""
when_4 = ""
when_5 = "When the market is mature"

[critical_cube.five_wise]
# Five points of view chosen for this problem. Label simulations as simulations.
points_of_view = ["", "", "", "", ""]

[critical_cube.five_weirds]
what_if = ["", "", "", "", ""]

[critical_cube.swot]
# Apply to every face above
strengths = ""
weaknesses = ""
opportunities = ""
threats = ""

[critical_cube.cynefin]
clear = ""
complicated = ""
complex = ""
chaotic = ""
uncertainty = "Low, medium or high, and why"
```

## In NeoLibrary

The Cube is one of the skeptic's instruments in [RFC-0004](RFC-0004-how-we-build.md). It can be called into any energy of the [Creation Model](RFC-0005-creation-model.md), and most often into Think and Judge.

## History

| Date | Version | What changed | Source |
|---|---|---|---|
| Sep 15, 2024 | "Ironstone Cube" | Six sections: 5 Ws, 5 Whys, 5 Hows, SWOT, 5 Wise, mental models (first principles, systems thinking, second-order thinking). The 5 Wise were five reflective questions: why now, why here, why this way, why you, why this impact. Written up with a custom GPT and a TOML prompt; each face tied to an idea from cognitive psychology. AI-assisted | Drive doc, private archive |
| Oct 8, 2024 | "Ironstone Critical Cube" | Six fives: 5 Ws, 5 Whys, 5 Hows, 5 Whens, 5 Wise, 5 Weirds, with a Critical Thinking Foundation before and a Cynefin assessment after. The 5 Wise became five expert points of view. AI-assisted worked example | Drive doc, private archive |
| Apr 16, 2025 | Named tool | Listed beside the Bullshit Compass and the Uncertainty Meter as an Ironstone tool | Drive doc |
| Oct 2026 | Published | "Ironstone Critical Thinking Cube" on ironstoneadvisory.com, faces not named | [Ironstone Methods](https://www.ironstoneadvisory.com/what-we-do/ironstone-methods) |
| Oct 17, 2026 | 1.0 | The October 2024 six fives made canonical. SWOT moves from a face to the grid on every face. The 5 Wise are points of view that vary with the problem. Mental models are no longer a face | Rob Tyrie, October 17, 2026 |

The September 2024 why-questions (why now, why here, why this way, why you, why this impact) are still good questions. They now belong to whichever wise point of view would ask them.

## Change log

- 1.0 (October 17, 2026): accepted. The six fives, the SWOT grid on every face, the foundation and the Cynefin check, as confirmed by Rob Tyrie. Drafted with Claude (AI-assisted).
- 0.9 (October 17, 2026): first draft, based on the September 2024 version.
