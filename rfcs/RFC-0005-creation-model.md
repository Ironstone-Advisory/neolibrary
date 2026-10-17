# RFC-0005: The Ironstone Creation Model

| | |
|---|---|
| Author | Rob Tyrie, Ironstone Advisory |
| Version | 1.2 |
| Status | Accepted |
| Date | October 17, 2026 |
| Also called | The creator model, the creation model, Seven Energies, Eight Energies |
| License | [CC BY 4.0](../LICENSE-docs) |

## Site summaries

For ironstoneadvisory.com and other short uses. Copy these as written; they change in the same commit as the RFC.

**One line**

Creation needs eight kinds of work, and most teams are strong in only two or three of them.

**50 words**

The Ironstone Creation Model names eight energies a venture needs to take an idea to market: ideate, think, make, do, judge, decide, execute and archive. They run in parallel, not in order. Each works toward a quantum of usable output, demanding inputs from the others and handing its outputs on.

**200 words**

The Ironstone Creation Model describes how an idea becomes something that exists, is used and is kept. For a for-profit enterprise, the goal is plain: get the idea to market. It names eight energies: ideate, think, make, do, judge, decide, execute and archive. Most people and most teams are strong in two or three, and the missing ones are where ventures stall.

There is no order of execution. All eight run in parallel, each at its own level of energy and its own level of done. Each works toward a quantum, a whole and usable unit of its own output, and trades messages with the others: it demands the inputs it needs and hands on the outputs it has. Make demands a sharp assumption from Think. Judge hands Decide a signed verdict. Archive hands Ideate the lessons of the last loop, which is how the model reproduces itself.

Outside forces act on the work: fans, skeptics, and regulation and law.

The model began in 2022 with fewer energies. Execute and archive came later. AI now takes part in every energy, which makes ideas and fluent prose cheap and makes judgment and a well-kept archive scarce.

## Summary

The Ironstone Creation Model describes how something goes from an idea to a thing that exists, is used and is kept. It names the kinds of work creation needs, which I call **energies**: ideate, think, make, do, judge, decide, execute and archive. Most people and most teams are strong in two or three of them. The model exists so you can see which energies are present, which are missing, and what has to happen next.

The list is a naming order, not an execution order. There is no fixed sequence in a model like this.

Creation starts before analysis. It starts when an idea, a question, a pressure or a possibility enters the system. For a for-profit enterprise, the goal is to get that idea to market.

## The energies

| Energy | What it does | Its quantum: enough to tap another energy |
|---|---|---|
| **Ideate** | Generates options without killing them. Ideators observe, mix observation with memory, and frame ideas in words or pictures that others can use | There are more options than feel comfortable, and some are strange |
| **Think** | Refines, analyzes and filters. Writes down every "this only works if" and ranks the assumptions by what kills you when they're wrong | You can take a real step. That bar is lower than certainty |
| **Make** | Builds the idea into something tangible: a prototype, a draft, a model | A small thing exists that could prove you wrong |
| **Do** | Puts it to work on real material and tests it | It has been used for real, not demonstrated |
| **Judge** | Assesses quality and fit against the intent. Can judge any part of the work, including the believers and the critics | A judgment exists that someone other than the maker would sign |
| **Decide** | Chooses a direction from the judgment: go left, go right, adopt, abandon or run the loop again | The choice is written down with its reason |
| **Execute** | Ships it and runs it | Strangers can see it, which makes it production |
| **Archive** | Keeps the work, the decision and the lesson so they can be found and reused | A later reader could pick it up without asking you |

## Energies and quanta, not stages

There is no order of execution. Each energy works until it reaches a **quantum**: a whole, usable unit of its own output, like a set of options worth thinking about, a prototype that could prove you wrong, or a decision written down with its reason. Below that threshold the energy has nothing to hand on. Once it reaches one, it can tap any other energy, in any direction.

So the model is a graph: energies are nodes, and taps between them are edges. Several energies can be live at once, at different altitudes. You can be in Do on the project while one deliverable is still in Make.

- **High-value taps.** Archive to Ideate, mining your own finished loops, is the most valuable and the least used. Judge to Think means the review found a strategy error, so re-plan instead of working harder. Do to Make means real use exposed a design flaw, so prototype the fix instead of patching it live.
- **Taps without a quantum.** Ideate straight to Execute is enthusiasm with a deadline: nothing was thought through or made. Execute to Ideate at 90% abandons a nearly finished quantum for a shinier idea.
- **Loops that never reach a quantum.** Think to Think is planning as procrastination. Make to Make is prototype addiction, usually fear of exposure.
- **The test for any tap.** Can you name the quantum you're carrying, or the specific thing you learned? If yes, it's a real move. If you're just uncomfortable, it's a retreat.

## Parallel energies and the messages between them

All eight energies run at the same time. At any moment each one has two readings:

- **Level of energy:** how much attention and effort it's getting right now, from none to full.
- **Level of done:** how close it is to its next quantum.

A healthy venture has every energy live at some level. A stalled one usually has one or two at zero, and that's where to look first.

The energies coordinate by passing messages. Each one **demands inputs** it needs from the others and **gives outputs**, its quanta, to whichever energy needs them. Some typical messages:

| From | To | Message |
|---|---|---|
| Make | Think | Demand: which assumption must this prototype test? |
| Think | Make | Output: the top of the kill list, graded |
| Do | Judge | Output: what happened when real people used it |
| Judge | Decide | Output: a verdict someone other than the maker would sign |
| Decide | Execute | Output: go, with this scope, by this date |
| Execute | Make | Demand: a fix for the defect customers hit |
| Execute | Archive | Output: the release and its decision record |
| Archive | Ideate | Output: the lessons of the last loop |

Reading a team this way, energy by energy and message by message, shows what's blocking the idea from reaching market: an energy with no effort on it, a demand nobody is answering, or an output nobody picked up.

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

## Why eight: a model that reproduces itself

The model started in 2022 with fewer energies. I added Execute and Archive later, for two reasons. Without Execute, nothing reaches the people it was made for. Without Archive, every loop starts from nothing. Archive is what makes the model reproduce itself: a finished loop, written down, becomes the raw material for the next Ideate, so each cycle seeds the one after it.

## Scope

The model was designed for groups: in particular the first 20 people in an organization taking digital ideas to their first few million dollars of revenue. It also works for one person moving between energies. Physical goods follow a different model.

## History

| Date | Version | What changed | Source |
|---|---|---|---|
| 2022 | Creator model | Invented with fewer energies than today, by Rob's account. No 2022 document has been found yet | Rob Tyrie, October 17, 2026 |
| Jul 2, 2023 | Creator model | Six internal roles: ideator, thinker, maker, doer, judge (judger), decider. Two outside roles: fans or believers, and skeptics or critics. Described as non-linear, not reductionist, "along ideas of physics", with energies causing change at different levels; drawn as connected nodes like neurons | Rob's voice conversation with Pi, Drive doc "Creator model full July 2 2023" (private archive) |
| May 22, 2024 | Creator model x 9 | Eclipse Labs (now XLabs) deck slide "Labs Use the Ironstone Creator Model x 9": Archive, Judge, Make, Believe, Decide, Critique, Do, Think, Ideate, crossed with the uses Summarize, Q&A, Transform, Optimize, Simulate, Automate | Drive deck, May 22, 2024 (private archive) |
| Sep 20-21, 2026 | Seven Energies | Ideate, think, make, do, execute, judge, archive. Renamed from stages to energies; graph and recursion added; book planned | Claude conversation "Creative process framework" |
| Oct 13, 2026 | Eight Energies | Decide added after Judge and before Archive, from Deming's plan-do-check-act. A ninth energy may yet emerge | Claude conversation "Creator model conversations" |
| Oct 17, 2026 | Published | ironstoneadvisory.com lists ideate, think, make, do, judge, decide, execute, archive, with fans, skeptics and regulation as outside forces | [Ironstone Methods](https://www.ironstoneadvisory.com/what-we-do/ironstone-methods) |

## Change log

- 1.2 (October 17, 2026): the goal for a for-profit enterprise is getting the idea to market; all energies run in parallel, each with a level of energy and a level of done, and coordinate by demanding inputs and giving outputs, as stated by Rob Tyrie.
- 1.1 (October 17, 2026): no order of execution. Each energy reaches a quantum before it taps the others, as stated by Rob Tyrie. The "Done when" column becomes each energy's quantum, and "backward edges" become taps.
- 1.0 (October 17, 2026): accepted. Rob confirmed the order (ideate, think, make, do, judge, decide, execute, archive) and the 2022 origin, with Execute and Archive added later so the model is complete and reproduces itself.
- 0.9 (October 17, 2026): first draft, compiled from the sources above. Drafted with Claude (AI-assisted) from Rob's own words; no content invented beyond restating them.
