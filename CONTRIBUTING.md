# Contributing to NeoLibrary

Thanks for helping. A few rules keep the open core clean.

## Before you start

1. Open an issue describing the change, unless it is a small fix.
2. Fork, branch from `main`, keep pull requests focused.
3. Run `python -m pytest` before you push.

## Contributor License Agreement (CLA)

NeoLibrary is open core: the engine is Apache 2.0 and Ironstone Advisory also offers commercial plugins. To keep that model workable, every outside contribution is accepted under the CLA in [CLA.md](CLA.md).

By opening a pull request you confirm that:

- you wrote the contribution, or have the right to submit it;
- you agree to the terms in CLA.md;
- your contribution may be distributed under Apache 2.0 and under other terms Ironstone Advisory chooses.

Add this line to each commit (`git commit -s` does it for you):

```
Signed-off-by: Your Name <you@example.com>
```

Pull requests without a sign-off cannot be merged.

## What goes where

| Change | Repo |
|---|---|
| Engine, plugin contract, docs | `neolibrary` (here) |
| Test data | `neolibrary-commons`, with attribution |
| Commercial features | Not accepted here; talk to Ironstone Advisory |

## AI-assisted contributions

Welcome, but say so in the PR description and make sure you have reviewed and understand every line. Provenance matters in this project.

## Style

- Python 3.10+, type hints, `ruff` for lint.
- Docs in plain English, short sentences, no marketing copy.
