# Site Change Log: October 28, 2026

| | |
|---|---|
| Author | Rob Tyrie, Ironstone Advisory |
| Date | Wednesday, October 28, 2026 |
| Status | Work order for ironstoneadvisory.com, not canonical |
| Sources | Weekly site and repo check, Oct 28, 2026; Rob's decisions in the same session; PR #1 |
| License | [CC BY 4.0](../../LICENSE-docs) |

> **Reading note.** Logs record what happened; RFCs define. Where this log and an RFC disagree, the RFC wins. This log is the work order for the robot that edits the site.

## What happened

The weekly check found that the site had published a Creation Model guide and a Critical Cube page on October 25, 2026. Their wording differed from RFC-0005 and RFC-0006 in a few places. Rob decided each difference on October 28:

| # | Question | Rob's decision | Where it lands |
|---|---|---|---|
| 1 | Cube name and version | "Ironstone Critical Thinking Cube" is the formal name, "Critical Cube" the short one. Version 1.5 | RFC-0006 1.5 (done) |
| 2 | Cube foundation and Cynefin check | Still part of the method | Site, change 1 |
| 3 | SWOT wording | A check on every face: strengths and weaknesses inside the organization, opportunities and threats in its environment | RFC-0006 1.5 (done) |
| 4 | Energy order in the guide intro | Execute before Archive, as in the RFC | Site, change 2 |
| 5 | What Ideate produces | "Ideas: options not yet judged" | RFC-0005 1.8 (done) and site, change 2 |
| 6 | Licensing page | Full statement, with a link to GitHub | Site, change 3 |
| 7 | Glossary | Add five entries | Site, change 4 |

**Merged.** PR #1 merged into main on October 28, 2026 (commit 6122a8c), so RFC-0006 1.5, RFC-0005 1.8 and this log are on main. Compass gate: the FS02 manual reading found nothing; Rob saw the decisions and the drafted glossary and licensing text in the session, and chose to merge without a separate full read of the diff.

## Instructions for the robot

### Rules

1. The site is a Google Site. Edit it in the Google Sites editor while signed in as rob@ironstoneadvisory.com.
2. Make only the four changes below. Don't reword anything else, and don't change layout, navigation or images.
3. Copy the replacement text exactly as written here, including capitals and punctuation. Don't add em dashes.
4. If the text to find isn't on the page, or appears more than once, stop and report it. Don't guess.
5. After all four changes, click **Publish** once, then check every page against its "Check" line.
6. If any step fails, stop, change nothing more, and report which step failed and what the page shows.
7. When finished, tick the boxes below in a commit on this file, or report the result to Rob.

### Change 1: Critical Cube page

**Page:** https://www.ironstoneadvisory.com/what-we-do/ironstone-methods/ironstone-critical-thinking-cube

**1a. Add the foundation.** Insert this section just before the section on the first face ("The 5 Ws"):

> **Before the Cube: the foundation**
>
> Write three lines before turning the Cube at all:
>
> - **Base assumption.** What are we taking as true?
> - **Context.** What's happening around this?
> - **Key question.** The one question the analysis has to answer.
>
> If you can't write the key question in one sentence, you're not ready for the Cube.

**1b. Add the Cynefin check.** Insert this section just after the section on the last face ("The 5 Weirds") and after any SWOT text that follows it:

> **After the Cube: the Cynefin check**
>
> Close by placing each part of the problem in a Cynefin domain (Dave Snowden's framework):
>
> - **Clear:** known answers. Apply best practice.
> - **Complicated:** answerable by experts. Analyse, then act.
> - **Complex:** unknowns that only experiments reveal. Probe, then act.
> - **Chaotic:** no stable pattern yet. Act to stabilize first.
>
> Then state how uncertain the whole picture is. The Cynefin check tells you which parts of the plan to execute and which to run as experiments.

**1c. Leave as is:** the title "Ironstone Critical Cube", "Version 1.5" and the sentence "SWOT is now a check applied to every aspect, not a separate face." These already match RFC-0006 1.5.

**Check:** the page shows the foundation before the 5 Ws and the Cynefin check after the 5 Weirds, and still says Version 1.5.

### Change 2: Creation Model guide

**Page:** https://www.ironstoneadvisory.com/what-we-do/ironstone-methods/creation-model

**2a. Energy order in the intro.** In the intro paragraph, find the list that ends "Deciding, Archiving, Execution" (or "Deciding, Archiving and Execution"). Swap the last two words so it ends "Deciding, Execution, Archiving" (or "Deciding, Execution and Archiving"). Keep the rest of the sentence as it is.

**2b. Ideate.** Find:

> Ideate produces options.

Replace with:

> Ideate produces ideas: options not yet judged.

**2c. Version.** Find:

> Creation Model v1.7, accepted October 17, 2026

Replace with:

> Creation Model v1.8, accepted October 28, 2026 (v1.7 accepted October 17, 2026)

Leave "Site guide published October 25, 2026" as it is.

**2d. Ironstone Methods page.** On https://www.ironstoneadvisory.com/what-we-do/ironstone-methods, find "Status: Creation Model v1.7, accepted." and replace it with "Status: Creation Model v1.8, accepted."

**Check:** the guide's intro ends "Execution, Archiving"; the guide says "ideas: options not yet judged" and v1.8; the Methods page says v1.8.

### Change 3: Licensing & Attribution page

**Page:** https://www.ironstoneadvisory.com/licensing-and-attribution

Find the line "Original Ironstone Advisory content is © Ironstone Advisory." Directly after it, insert these five paragraphs. Make each GitHub address a link to itself.

> **Ironstone methods.** The source documents for the Ironstone Creation Model, the Ironstone Critical Thinking Cube (Critical Cube) and the Evidence Ladder are published as RFCs at github.com/Ironstone-Advisory/neolibrary under Creative Commons Attribution 4.0 (CC BY 4.0). You may share and adapt them. Credit: "Rob Tyrie, Ironstone Advisory."
>
> **NeoLibrary.** The NeoLibrary code is open source under the Apache License 2.0, and its documents are under CC BY 4.0. "NeoLibrary" and the NeoLibrary Helix are trademarks of Ironstone Advisory. The Apache license does not grant rights to these names or marks.
>
> **Bullshit Compass.** The Bullshit Compass code and specifications are published at github.com/Ironstone-Advisory/bullshit-compass-v2 (current) and github.com/Ironstone-Advisory/BullshitCompass (v1) under the MIT License.
>
> **NeoLibrary Commons.** The test corpus at github.com/Ironstone-Advisory/neolibrary-commons is CC BY 4.0.
>
> All of Ironstone Advisory's public repositories are at github.com/Ironstone-Advisory.

Link targets:

- github.com/Ironstone-Advisory/neolibrary → https://github.com/Ironstone-Advisory/neolibrary
- github.com/Ironstone-Advisory/bullshit-compass-v2 → https://github.com/Ironstone-Advisory/bullshit-compass-v2
- github.com/Ironstone-Advisory/BullshitCompass → https://github.com/Ironstone-Advisory/BullshitCompass
- github.com/Ironstone-Advisory/neolibrary-commons → https://github.com/Ironstone-Advisory/neolibrary-commons
- github.com/Ironstone-Advisory → https://github.com/Ironstone-Advisory
- CC BY 4.0 → https://creativecommons.org/licenses/by/4.0/

Leave the existing photo credit, NeoLibrary authorship and Grey Swan Guild test-material paragraphs as they are.

**Check:** the page names CC BY 4.0 for the methods, Apache 2.0 and the trademark for NeoLibrary, and MIT for the Compass, and every GitHub link opens the right repository.

### Change 4: Glossary

**Page:** https://www.ironstoneadvisory.com/insights/glossary

Add these five entries in the same format as the existing ones (term in bold, then the definition). Put them after the "NeoLibrary" entry, in this order:

> **Creation Model:** The Ironstone Creation Model: eight intrinsic energies a company controls (ideate, think, make, do, judge, decide, execute, archive), with execute orchestrating the rest, and four extrinsic ones it does not (fans, skeptics, competition, the law). Most teams are strong in only two or three.
>
> **Critical Cube:** The Ironstone Critical Thinking Cube: a way to look at a difficult question from six faces (5 Ws, 5 Whys, 5 Hows, 5 Whens, 5 Wise, 5 Weirds), with a SWOT check on every face, before you answer.
>
> **Evidence Ladder:** Five grades of evidence, from E0 (assertion) to E4 (repeated result). Confidence in a claim can't be higher than the evidence under it.
>
> **Bullshit Compass:** A method and experimental software for spotting vague, plausible, meaningless language in business writing. It reads language patterns, not truth or intent.
>
> **MetaRAG:** Rob Tyrie's June 2024 idea that became NeoLibrary: ground an AI model in a curated, broadly agreed library of documents, using their whole structure, instead of a database.

**Check:** the glossary has fifteen entries, and the five new ones read exactly as above.

## Status

- [ ] Change 1: Critical Cube page
- [ ] Change 2: Creation Model guide and Methods page
- [ ] Change 3: Licensing & Attribution
- [ ] Change 4: Glossary
- [ ] Published and checked

## Still open

- Bullshit Compass method documents: keep them MIT like the code, or move them to CC BY 4.0 like the other methods. If they move, the Compass repos need a docs license file first, and the Compass paragraph in change 3 changes.
- The trademark sentence in change 3 follows this repo's NOTICE file. It hasn't been reviewed by a lawyer.
