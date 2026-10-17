# RFC-0005: The Ironstone Creation Model

| | |
|---|---|
| Author | Rob Tyrie, Ironstone Advisory |
| Version | 0.9 |
| Status | Draft (awaiting Rob's confirmation of the energy order) |
| Date | October 17, 2026 |
| Also called | The creator model, the creation model, Seven Energies, Eight Energies |
| License | [CC BY 4.0](../LICENSE-docs) |

## Site summaries

For ironstoneadvisory.com and other short uses. Copy these as written; they change in the same commit as the RFC.

**One line**

Creation needs eight kinds of work, and most teams are strong in only two or three of them.

**50 words**

The Ironstone Creation Model names the eight energies creation needs: ideate, think, make, do, judge, decide, execute and archive. They're energies, not stages. Work moves between them in any direction, and the whole model runs again inside each one. Use it to see which energies a team has and which are missing.

**200 words**

The Ironstone Creation Model describes how something goes from an idea to a thing that exists, is used and is kept. It names eight energies: ideate, think, make, do, judge, decide, execute and archive. Most people and most teams are strong in two or three of them, and the missing ones are where projects stall.

The energies form a graph, not a staircase. New evidence can send the work backward, sideways or around again, and the whole model runs again inside any single energy. The most valuable move is from archive back to ideate: mining your own finished work for the next idea. The test for any backward move is simple. If you can name what you learned, it's a return. If you're just uncomfortable, it's a retreat.

Outside forces act on the work: fans, skeptics, and regulation and law. Judging honestly inside the team is what makes the outside critics survivable.

The model began as six roles in a conversation in July 2023 and grew to eight energies by October 2026. AI now takes part in every energy, which makes ideas and fluent prose cheap and makes judgment and a well-kept archive the scarce parts.

## Summary

The Ironstone Creation Model describes how something goes from an idea to a thing that exists, is used and is kept. It names the kinds of work creation needs, which I call **energies**: ideate, think, make, do, judge, decide, execute and archive. Most people and most teams are strong in two or three of them. The model exists so you can see which energies are present, which are missing, and what has to happen next.

Creation starts before analysis. It starts when an idea, a question, a pressure or a possibility enters the system.

## The energies

| Energy | What it does | Done when |
|---|---|---|
| **Ideate** | Generates options without killing them. Ideators observe, mix observation with memory, and frame ideas in words or pictures that others can use | There are more options than feel comfortable, and some are strange |
| **Think** | Refines, analyzes and filters. Writes down every "this only works if" and ranks the assumptions by what kills you when they're wrong | You can take a real step. That bar is lower than certainty |
| **Make** | Builds the idea into something tangible: a prototype, a draft, a model | A small thing exists that could prove you wrong |
| **Do** | Puts it to work on real material and tests it | It has been used for real, not demonstrated |
| **Judge** | Assesses quality and fit against the intent. Can judge any part of the work, including the believers and the critics | A judgment exists that someone other than the maker would sign |
| **Decide** | Chooses a direction from the judgment: go left, go right, adopt, abandon or run the loop again | The choice is written down with its reason |
| **Execute** | Ships it and runs it | Strangers can see it, which makes it production |
| **Archive** | Keeps the work, the decision and the lesson so they can be found and reused | A later reader could pick it up without asking you |

## These are energies, not stages

The order above is the common path, not a staircase. The model is a graph: energies are nodes, and moves between them are edges that run in both directions. New evidence can send the work backward, sideways or around again.

- **Useful backward edges.** Archive to Ideate, mining your own finished loops, is the most valuable and the least used. Judge to Think means the review found a strategy error, so re-plan instead of working harder. Do to Make means operations exposed a design flaw, so prototype the fix instead of patching it live.
- **Pathological edges.** Ideate straight to Execute (enthusiasm with a deadline). Think to Think (planning as procrastination). Make to Make (prototype addiction). Execute to Ideate (abandoning at 90% for a shinier idea).
- **The test for a backward move.** Can you name the specific thing you learned that invalidates the later energy? If yes, it's a return. If you're just uncomfortable, it's a retreat.

## Recursion

The whole model runs again inside any single energy, governed by that energy. Inside Archive you can ideate (what could preservation look like here), think (which approach, for whose future use), make (one archive entry), do (run it across several projects), and so on. The parent energy sets the subject and the success test for the loop inside it. Two levels of recursion is plenty.

## Roles and outside forces

An energy is often carried by a person, and it's rare for one person to carry all of them. The judge in particular needs distance from the work: it's hard to judge objectively what you created. In small companies the judge is often an outside advisor, trusted for exactly that distance. The judging must not kill the energy of the creative work.

Forces outside the team act on the work: **fans** (believers), **skeptics** (critics), and **regulation and law**. Judging internally before you meet the outside world is what makes the outside critics survivable.

In the NeoLibrary repos the skeptic is treated as an aspect that wraps every energy rather than an outside force alone; see [RFC-0004](RFC-0004-how-we-build.md).

## Where AI fits

AI can take part in every energy, and the model was framed from the start as a framework for human and machine collaboration. What changes:

- Generating ideas and fluent strategy prose now costs nothing, so fluency is no longer evidence of clear thinking. Grade the assumptions, not the prose (see [RFC-0007](RFC-0007-evidence-ladder.md)).
- Rough versions now look finished, which makes Make and Judge harder, not easier.
- An archive is now queryable working context. Archives used to be write-only because retrieval cost more than rewriting from memory. That has flipped, which makes Archive the energy that compounds.

The person leads; the tools amplify.

## Scope

The model was designed for groups: in particular the first 20 people in an organization taking digital ideas to their first few million dollars of revenue. It also works for one person moving between energies. Physical goods follow a different model.

## History

| Date | Version | What changed | Source |
|---|---|---|---|
| Jul 2, 2023 | Creator model | Six internal roles: ideator, thinker, maker, doer, judge (judger), decider. Two outside roles: fans or believers, and skeptics or critics. Described as non-linear, not reductionist, "along ideas of physics", with energies causing change at different levels; drawn as connected nodes like neurons | Rob's voice conversation with Pi, Drive doc "Creator model full July 2 2023" (private archive) |
| May 22, 2024 | Creator model x 9 | Eclipse Labs (now XLabs) deck slide "Labs Use the Ironstone Creator Model x 9": Archive, Judge, Make, Believe, Decide, Critique, Do, Think, Ideate, crossed with the uses Summarize, Q&A, Transform, Optimize, Simulate, Automate | Drive deck, May 22, 2024 (private archive) |
| Sep 20-21, 2026 | Seven Energies | Ideate, think, make, do, execute, judge, archive. Renamed from stages to energies; graph and recursion added; book planned | Claude conversation "Creative process framework" |
| Oct 13, 2026 | Eight Energies | Decide added after Judge and before Archive, from Deming's plan-do-check-act. A ninth energy may yet emerge | Claude conversation "Creator model conversations" |
| Oct 17, 2026 | Published | ironstoneadvisory.com lists ideate, think, make, do, judge, decide, execute, archive, with fans, skeptics and regulation as outside forces | [Ironstone Methods](https://www.ironstoneadvisory.com/what-we-do/ironstone-methods) |

## Open question

On October 17, 2026 I also stated the flow as "ideate, think, make, do, decide, judge, execute" ([RFC-0004](RFC-0004-how-we-build.md)). That wording puts Decide before Judge and leaves out Archive. This draft follows the published order. RFC-0004 will be brought into line once the order is confirmed, and this RFC moves to Accepted.

## Change log

- 0.9 (October 17, 2026): first draft, compiled from the sources above. Drafted with Claude (AI-assisted) from Rob's own words; no content invented beyond restating them.
