# Site Change Log: November 3, 2026

| | |
|---|---|
| Author | Rob Tyrie, Ironstone Advisory |
| Date | Tuesday, November 3, 2026 |
| Status | Work order for ironstoneadvisory.com, not canonical |
| Sources | Weekly site and repo check, Nov 2, 2026; PR #2; Rob's request in the same session |
| License | [CC BY 4.0](../../LICENSE-docs) |

> **Reading note.** Logs record what happened; RFCs define. Where this log and an RFC disagree, the RFC wins. This log is the work order for the robot that edits the site. It carries forward the [October 28 work order](2026-10-28-site-changes.md) and adds to it.

## What happened

The weekly check on November 2, 2026 read the live site. None of the four changes in the October 28 work order were on the published pages. Rob thinks some of them may already be in a saved version of the site that was never published. The check also found new differences from the RFCs, listed below.

## Instructions for the robot

### Rules

1. The site is a Google Site. Edit it in the Google Sites editor while signed in as rob@ironstoneadvisory.com.
2. The rules in the October 28 work order still apply: make only the changes listed, copy text exactly, don't add em dashes, stop and report if the text to find isn't there or appears more than once.
3. Click **Publish** once, at the end, after every change is made.

### Step 0: check saved versions first

Before editing anything:

1. Open the site in the editor and compare the draft with the published site. If the draft already has some of the changes below, don't type them again.
2. Open **Version history** and look for versions saved on or after October 28, 2026. If a saved version has the changes, report which version and what it contains. Don't restore it yourself: restoring replaces the whole site, and Rob decides that.
3. Write down which changes were already in the draft and which you made. Report this list at the end.

### Changes carried forward from October 28

Make these exactly as written in the [October 28 work order](2026-10-28-site-changes.md), with one exception:

- Change 1: Critical Cube page (foundation and Cynefin check)
- Change 2a, 2b and 2c: Creation Model guide (energy order, Ideate, version)
- Change 3: Licensing & Attribution page
- Change 4: Glossary (five entries)

**Exception: skip change 2d.** The Ironstone Methods page no longer says "Status: Creation Model v1.7, accepted." It now says "Status: working model; the broader consulting methodology is evolving." Leave it as it is until Rob decides (see "Waiting on Rob").

### Change 5: Outside forces on the Ironstone Methods page

**Page:** https://www.ironstoneadvisory.com/what-we-do/ironstone-methods

Find:

> Fans, skeptics and regulation or law act on the work from outside it.

Replace with:

> Fans, skeptics, competition and the law act on the work from outside it.

**Why:** RFC-0005 has four extrinsic energies: fans, skeptics, competition and the law. The Creation Model guide already lists all four.

**Check:** the Methods page names competition as an outside force.

### Change 6: Cube link text on the Ironstone Methods page

**Page:** https://www.ironstoneadvisory.com/what-we-do/ironstone-methods

Find the link text:

> Read the restored Critical Thinking Cube guide

Replace it with:

> Read the Critical Cube guide (version 1.5)

Keep the link pointing to https://www.ironstoneadvisory.com/what-we-do/ironstone-methods/ironstone-critical-thinking-cube.

**Why:** "restored" is the word used for the archived earlier guide, so the old link text sent readers to the wrong page in their heads.

**Check:** the link reads "Read the Critical Cube guide (version 1.5)" and opens the Critical Cube page.

### Check only: site index (don't change)

On https://www.ironstoneadvisory.com/insights/site-index, report:

- Whether github.com/Ironstone-Advisory/neocrm and github.com/Ironstone-Advisory/ImportantPublicDocumentsTemplates open as public repositories.
- Whether both https://www.ironstoneadvisory.com/about/about-rob and https://www.ironstoneadvisory.com/about/rob-tyrie are listed, and whether the second one opens a page or a "not found" page.

## Waiting on Rob

The robot doesn't touch these until Rob decides and this log is updated:

| # | Question | Options |
|---|---|---|
| 1 | Creation Model status on the Methods page | Say "Status: Creation Model v1.8, accepted." as the RFC does, or keep "working model" and record that in RFC-0005's History |
| 2 | "Aspects" or "faces" for the Cube's six parts | The Critical Cube page says aspects; RFC-0006 says faces |
| 3 | The two repos on the site index | Keep both linked, or remove whichever isn't meant to be public |

## Status

- [ ] Step 0: draft and version history checked, findings reported
- [ ] Changes 1, 2a to 2c, 3 and 4 (from October 28)
- [ ] Change 5: outside forces
- [ ] Change 6: Cube link text
- [ ] Site index checked and reported
- [ ] Published and checked
