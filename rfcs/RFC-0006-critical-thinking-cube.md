# RFC-0006: The Ironstone Critical Thinking Cube

| | |
|---|---|
| Author | Rob Tyrie, Ironstone Advisory |
| Version | 0.9 |
| Status | Draft (awaiting Rob's confirmation of the v2 faces) |
| Date | October 17, 2026 |
| Also called | The Ironstone Cube, the Critical Cube |
| License | [CC BY 4.0](../LICENSE-docs) |

## Summary

A difficult question has more than one face. The Cube is a structured way to turn a question around before you get attached to an answer: reframe it, shift the point of view, and examine the answer from several sides. I use it for critical thinking, decisions and problem-solving, especially when the first answer is probably too easy.

It was built for speed. Before generative AI, analysing an enterprise-scale problem this thoroughly needed expensive outside strategy consultants. With a structured analysis prompt, a team can look at the problem space, the solution space and the change it implies in an afternoon.

## The faces (v1, September 2024)

Each face asks a different kind of question. Run them in order the first time; after that, go to the face the problem needs.

| Face | Questions | What it's for |
|---|---|---|
| **1. The 5 Ws** | Who, what, when, where, why | Context. Gather enough of it before solving anything |
| **2. The 5 Whys** | Ask why five times | Root cause. Get under the first explanation |
| **3. The 5 Hows** | How will it be done, how does it meet the need, how does it scale, how are internal problems handled, how is the advantage kept | Action. Turn analysis into steps someone can take |
| **4. SWOT** | Strengths, weaknesses, opportunities, threats | Perspective. Switch between what's inside and what's outside |
| **5. The 5 Wise** | Why now? Why here? Why this way? Why you? Why this impact? | Judgment. Timing, position, method, fit and long-term consequences, including ethics |
| **6. Mental models** | First principles, systems thinking, second-order thinking (plus inversion, Pareto and Occam's razor as options) | Depth. Break the problem down and follow the consequences |

The analysis closes with a summary: insights, recommendations and risks.

### The 5 Wise

The 5 Wise are the Cube's reflective face, and the part that is most mine. They keep a strategy from being driven only by data.

- **Why now?** Is this the right moment, given readiness inside and conditions outside? Would waiting, or acting early, undermine it?
- **Why here?** Why this market, region, niche or intellectual position?
- **Why this way?** Are the methods effective, sustainable and principled, not just fast?
- **Why you?** Are you the right team, with the right skills and resources, or is this someone else's opportunity?
- **Why this impact?** What does this do to customers, the industry, society and the environment over the long run?

### Why each face is there

The September 2024 write-up ties each face to an idea from cognitive psychology: the 5 Ws to schema activation (organizing what you already know), the 5 Whys to deep processing, the 5 Hows to planning and goal-setting, SWOT to cognitive flexibility, and the Cube as a whole to metacognition (checking your own thinking) and distributed cognition (spreading a big problem across a team). These are the design rationale, not tested claims about the brain.

## The skeptic's cube (v2, October 2026)

In October 2026 the Cube became one of the skeptic's instruments in [RFC-0004](RFC-0004-how-we-build.md), described as six faces, each split into SWOT quadrants, with swappable lenses on each quadrant. In that form SWOT stops being one face and becomes the grid on every face, and a lens (a named critic, a stakeholder, a time horizon) can be swapped in to read each quadrant.

The v2 face list hasn't been written down yet. Until it is, use the v1 faces.

## Using it with an AI model

The 2024 Cube was run as a custom GPT with a structured TOML prompt. The prompt, as written in September 2024:

```toml
[Ironstone_Cube_Analysis]
company = "Your Company Name"

[Ironstone_Cube_Analysis.5Ws]
who = "Identify the target audience, stakeholders, customers, partners, and investors."
what = "Analyze the products/services the company offers and what problems they aim to solve."
when = "Assess the timing of their offerings (market trends, regulatory shifts, or industry changes)."
where = "Evaluate the company's geographical focus and market positioning."
why = "Explore the company's mission and purpose behind their strategies and offerings."

[Ironstone_Cube_Analysis.5Whys]
1st_why = "Why is the company pursuing its current strategy?"
2nd_why = "Why are these methods necessary for their objectives?"
3rd_why = "Why are the resources being allocated in this way?"
4th_why = "Why is this a priority for the company?"
5th_why = "Why will this approach achieve their desired outcomes?"

[Ironstone_Cube_Analysis.5Hows]
1st_how = "How does the company plan to execute its strategy?"
2nd_how = "How are they addressing customer needs and market demands?"
3rd_how = "How are they scaling their operations?"
4th_how = "How are they handling internal challenges?"
5th_how = "How do they maintain a competitive advantage?"

[Ironstone_Cube_Analysis.SWOT]
strengths = "Identify the company's competitive strengths."
weaknesses = "Analyze potential weaknesses or gaps in their strategy."
opportunities = "Explore market opportunities for growth or innovation."
threats = "Identify external threats (competitors, regulations, market conditions)."

[Ironstone_Cube_Analysis.5Wise]
why_now = "Why is now the right time for the company's initiatives?"
why_here = "Why is the company positioned in this specific market or region?"
why_this_way = "Why are they using these particular methods? Are they optimal?"
why_you = "Why is this company uniquely suited to solve these problems?"
why_this_impact = "What long-term impact will their actions have on the industry, society, and environment?"

[Ironstone_Cube_Analysis.Mental_Models]
first_principles = "Break down the company's strategy to its basic components."
systems_thinking = "Analyze how the company's actions interact with the broader market and ecosystem."
second_order_thinking = "Evaluate long-term consequences of their current strategy."

[Ironstone_Cube_Analysis.Summary]
insights = "Summarize the findings from the analysis."
recommendations = "Provide critical feedback and highlight opportunities for improvement."
risks = "Identify potential risks in the company's approach and strategy."
```

A model's Cube output is a first draft. Grade its claims with the [Evidence Ladder](RFC-0007-evidence-ladder.md) before acting on them: a model reading a company's website produces E0 and E1 evidence at best.

## What it was invented for

1. **Rapid business planning** in fast industries such as InsurTech.
2. **Business positioning**: finding a niche by holding internal strengths and external forces in view at once.
3. **Teaching software design alternatives**: getting software teams to see how design choices affect the business.

## History

| Date | What | Source |
|---|---|---|
| Sep 15, 2024 | "The Ironstone Cube" write-up with the TOML prompt and a worked example on a real InsurTech company. AI-assisted (custom GPT) | Drive doc, private archive |
| Oct 17, 2026 | Named as a skeptic instrument: six faces, SWOT quadrants, swappable lenses | [RFC-0004](RFC-0004-how-we-build.md) |
| Oct 2026 | Published as the "Ironstone Critical Thinking Cube" | [Ironstone Methods](https://www.ironstoneadvisory.com/what-we-do/ironstone-methods) |

## Change log

- 0.9 (October 17, 2026): first draft from the September 2024 write-up and the October 2026 statements. Drafted with Claude (AI-assisted); the faces, questions and prompt are Rob's, quoted or closely restated.
