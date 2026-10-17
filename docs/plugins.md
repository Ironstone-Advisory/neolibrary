# Plugin contract

Plugins extend NeoLibrary without changing the core. The contract lives in [`src/neolibrary/plugins/base.py`](../src/neolibrary/plugins/base.py).

## Kinds

| Kind | Base class | Job |
|---|---|---|
| Connector | `Connector` | Pull `SourceItem`s from a source |
| Synthesizer | `Synthesizer` | Turn items into `KnowledgeObject`s |
| Publisher | `Publisher` | Render objects somewhere |

## Registering a plugin

Plugins are found through Python entry points in the `neolibrary.plugins` group:

```toml
# your plugin's pyproject.toml
[project.entry-points."neolibrary.plugins"]
my_connector = "my_package.connector:MyConnector"
```

## Open and commercial plugins

Anyone can write and license their own plugins. Ironstone Advisory's commercial plugins (SSO, audit trail, regulatory reporting, enterprise connectors) are distributed separately and are not part of this repo.

## Minimal example

```python
from neolibrary.plugins.base import Connector
from neolibrary.core import SourceItem

class FolderConnector(Connector):
    name = "folder"

    def __init__(self, path: str):
        self.path = path

    def fetch(self):
        from pathlib import Path
        for p in Path(self.path).rglob("*.md"):
            yield SourceItem.from_text(p.read_text(), origin=p.as_uri())
```
