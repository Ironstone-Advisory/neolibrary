# Site Change Log: November 23, 2026

| | |
|---|---|
| Author | Rob Tyrie, Ironstone Advisory |
| Date | Monday, November 23, 2026 |
| For | Dot (Robot(Dot)), who edits ironstoneadvisory.com |
| Status | Work order for ironstoneadvisory.com, not canonical |
| Sources | Weekly site and repo check, Nov 23, 2026; PR #6; Rob's rulings in the same session |
| License | [CC BY 4.0](../../LICENSE-docs) |

> **Reading note.** Logs record what happened; RFCs define. This repo is the canonical store: where the site and an RFC disagree, the site changes to match the RFC. This log is Dot's work order for the site. It replaces the [October 28 work order](2026-10-28-site-changes.md) and carries forward everything from it that isn't on the site yet. The November 3 work order was never merged, so it doesn't apply.

## What happened

The weekly check on November 23, 2026 read the live site.

**Done since October 28:** the glossary now has entries for the Creation Model, Critical Cube, Evidence Ladder and Bullshit Compass (part of old change 4). The NeoLibrary page, the glossary and the method guides now link to the public GitHub repositories.

**Still open:** every other change from October 28, plus four new ones. Rob ruled on November 23, 2026 that this repo is canonical, which settles the Cube questions the November 3 log left waiting. He also decided that the Bullshit Compass method documents move to CC BY 4.0, with the code staying MIT. He also said Ironstone-Advisory/Ironstone-Creation-Model-Legacy is the canonical repo for the Creation Model; this check couldn't read it, so the Creation Model changes wait.

## Instructions for Dot

### Rules

1. The site is a Google Site. Edit it in the Google Sites editor while signed in as rob@ironstoneadvisory.com.
2. Make only the changes below. Don't reword anything else, and don't change layout, navigation or images.
3. Copy replacement text exactly as written here, including capitals and punctuation. Don't add em dashes.
4. If the text to find isn't on the page, or appears more than once where this log expects one, stop and report it. Don't guess.
5. Before editing, compare the editor draft with the published site. If the draft already has a change, don't type it again; note it in your report. Don't restore an old version yourself.
6. Click **Publish** once, after every change is made, then check each page against its "Check" line.
7. Report the result to Rob: which changes you made, which were already in the draft, and any step that failed and what the page showed.

### Change 1: Critical Cube page, foundation and Cynefin check (from October 28)

**Page:** https://www.ironstoneadvisory.com/what-we-do/ironstone-methods/ironstone-critical-thinking-cube

Make change 1a (the foundation, before the 5 Ws) and change 1b (the Cynefin check, after the 5 Weirds) exactly as written in the [October 28 work order](2026-10-28-site-changes.md). Ignore its change 1c; change 6 below replaces it.

**Check:** the page shows the foundation before the 5 Ws and the Cynefin check after the 5 Weirds.

### Change 2: Creation Model guide (on hold)

Don't make any Creation Model change yet. Rob said on November 23, 2026 that Ironstone-Advisory/Ironstone-Creation-Model-Legacy is the canonical repo for the Creation Model, and this check couldn't read it. The Creation Model items are in "Waiting on Rob" until they are checked against that repo.

### Change 3: Licensing & Attribution page (from October 28)

**Page:** https://www.ironstoneadvisory.com/licensing-and-attribution

Make change 3 as written in the [October 28 work order](2026-10-28-site-changes.md): five paragraphs after "Original Ironstone Advisory content is © Ironstone Advisory.", with every GitHub address linked. One exception: Rob decided on November 23, 2026 that the Bullshit Compass method documents move to CC BY 4.0, so use this paragraph in place of the October 28 "Bullshit Compass" paragraph:

> **Bullshit Compass.** The Bullshit Compass method documents (the RFC FS02 specification, its specs and use cases) are under Creative Commons Attribution 4.0 (CC BY 4.0), and its code is under the MIT License. Both are published at github.com/Ironstone-Advisory/bullshit-compass-v2 (current) and github.com/Ironstone-Advisory/BullshitCompass (v1).

Link targets are the same as in the October 28 order. Make this change only after Rob has merged the two Compass license pull requests (bullshit-compass-v2 #2 and BullshitCompass #1); if either is still open, skip change 3 and report it.

**Check:** the page names CC BY 4.0 for the methods, including the Compass method documents; Apache 2.0 and the trademark for NeoLibrary; MIT for the Compass code; and every GitHub link opens the right repository.

### Change 4: Glossary

**Page:** https://www.ironstoneadvisory.com/insights/glossary

The four method entries are already there. Don't add the October 28 versions of them.

**4a. Add MetaRAG.** Add this entry in the "Agentic systems, archives and evidence" group, directly after the "RAG" entry, in the same format as the others. This text replaces the October 28 MetaRAG entry, which RFC-0001 1.1 superseded:

> **MetaRAG:** Retrieval-augmented generation that uses meta information about documents, such as tags, an ontology and the documents' own structure (contents, headings, summaries, index), to ground what is retrieved and the answers that large language models give. It does not need the full text of the documents. The ontology and meta information can be created in many ways.

**4b. Updated date.** Find "Updated October 25, 2026." and replace it with the date you publish, in the same format.

**Check:** MetaRAG follows RAG and reads exactly as above.

### Change 5: Ironstone Methods page

**Page:** https://www.ironstoneadvisory.com/what-we-do/ironstone-methods

**5a. Cube link text.** Find the link text:

> Read the restored Critical Thinking Cube guide

Replace it with:

> Read the Critical Cube guide (version 1.5)

Keep the link pointing to https://www.ironstoneadvisory.com/what-we-do/ironstone-methods/ironstone-critical-thinking-cube.

**5b. XLabs.** Find:

> the Ironstone xLab

Replace with:

> Ironstone XLabs

**Check:** the Methods page has the new Cube link text and says XLabs.

### Change 6: "Faces", not "aspects", for the Cube

RFC-0006 calls the Cube's six parts faces. Change "aspect" to "face" and "aspects" to "faces" wherever the word refers to the Cube's six parts, on these two pages only:

- https://www.ironstoneadvisory.com/what-we-do/ironstone-methods/ironstone-critical-thinking-cube (for example "six aspects", "every aspect", "six-aspect")
- https://www.ironstoneadvisory.com/insights/glossary, in the "Critical Cube" and "SWOT" entries

The Cube page sentence "SWOT is now a check applied to every aspect, not a separate face." becomes "SWOT is now a check applied to every face, not a separate face of its own."

Don't change the archived earlier guide (https://www.ironstoneadvisory.com/insights/field-notes-essays/critical-cube-earlier-guide); it already says faces. List every sentence you changed in your report.

**Check:** neither page uses "aspect" for the Cube's parts.

## Waiting on Rob

Dot doesn't touch these until Rob decides and this log is updated:

| # | Question | Options |
|---|---|---|
| 1 | Trademark sentence in change 3 (from October 28) | It follows this repo's NOTICE file and hasn't been reviewed by a lawyer |
| 2 | Creation Model wording, to be checked against Ironstone-Advisory/Ironstone-Creation-Model-Legacy | On the site today: the guide intro ends "Deciding, Archiving, Execution"; the guide says "Ideate produces options."; the guide and the glossary cite v1.7; the Methods page says "Status: working model; the broader consulting methodology is evolving." and "Fans, skeptics and regulation or law act on the work from outside it." RFC-0005 1.8 has Execute before Archive, "ideas: options not yet judged", Accepted v1.8, and four outside forces: fans, skeptics, competition and the law. The October 28 changes 2a to 2d hold until the canonical repo is checked |
| 3 | Two repos on the site index (from November 3) | github.com/Ironstone-Advisory/neocrm and github.com/Ironstone-Advisory/ImportantPublicDocumentsTemplates: keep both linked, or remove whichever isn't meant to be public |

## Status

- [ ] Draft compared with the published site
- [ ] Change 1: Critical Cube foundation and Cynefin check
- [ ] Change 2: on hold (Creation Model)
- [ ] Change 3: Licensing & Attribution
- [ ] Change 4: Glossary (4a, 4b)
- [ ] Change 5: Ironstone Methods page (5a, 5b)
- [ ] Change 6: faces, not aspects
- [ ] Published, checked and reported to Rob
