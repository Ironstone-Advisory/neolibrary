# RFC-0003: The plugin contract and the open-core boundary

| | |
|---|---|
| Author | Rob Tyrie, Ironstone Advisory |
| Version | 1.0 |
| Status | Accepted |
| Date | October 17, 2026 |
| Depends on | RFC-0001, RFC-0002 |
| License | [CC BY 4.0](../LICENSE-docs) |

## Summary

NeoLibrary stays small by pushing everything that touches the outside world into plugins. This RFC defines the three kinds of plugin, how they're found, how they're versioned, and which capabilities stay open versus commercial.

## Three kinds of plugin

**Connectors** bring material in. A connector reads a source (a folder, a mailbox export, a chat archive, a drive) and yields source items, already hashed and carrying their license.

**Synthesizers** turn source items into knowledge objects. A synthesizer may use a model, a rule set or a human workflow, but every object it emits cites its sources (RFC-0002, rule 1) and marks machine-produced fields (rule 5).

**Publishers** send knowledge objects out: as Markdown pages, feeds, exports, or answers in a chat. A publisher carries attribution through to the output (rule 4).

## Discovery

Plugins register under the Python entry-point group `neolibrary.plugins`. The engine finds whatever is installed; it never imports a vendor SDK itself.

## Manifest

Each plugin declares:

| Field | Meaning |
|---|---|
| `name` | Unique name |
| `kind` | `connector`, `synthesizer` or `publisher` |
| `version` | The plugin's own version |
| `contract_version` | The version of this RFC it implements, for example `1.0` |
| `license` | SPDX identifier, or `proprietary` |
| `vendor` | Who maintains it |

The engine refuses a plugin whose `contract_version` has a different major number from its own.

## The open-core boundary

The rule is simple: **anything a single person or a small team needs to build and use a library is open; anything an enterprise needs to govern one at scale is commercial.**

| Open (this repo, Apache 2.0) | Commercial (Ironstone Advisory) |
|---|---|
| Core types and the provenance spine | Single sign-on and role mapping |
| Plugin contract and discovery | Tamper-evident audit export and retention rules |
| Folder and Markdown connectors and publishers | Regulatory reporting, starting with OSFI Guideline E-23 model inventories |
| Dublin Core mapping | Enterprise connectors (SharePoint, Google Workspace, Slack, Teams, Confluence) |
| Reference synthesizer | Chat-archive connectors with provenance (ChatGPT, Claude, Discord, WhatsApp exports) |
| | Usage metering, subscriptions and billing |

Anyone can write and license their own plugins. Commercial plugins implement this same public contract; there's no private back door into the core.

## Change log

- 1.0 (October 17, 2026): first accepted version.
