# Copyright 2024-2026 Ironstone Advisory
# SPDX-License-Identifier: Apache-2.0
"""The plugin contract. Connectors, synthesizers and publishers subclass these."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable
from importlib.metadata import entry_points

from neolibrary.core import KnowledgeObject, SourceItem

ENTRY_POINT_GROUP = "neolibrary.plugins"


class Plugin(ABC):
    name: str = "unnamed"


class Connector(Plugin):
    @abstractmethod
    def fetch(self) -> Iterable[SourceItem]:
        """Yield source items from wherever this connector points."""


class Synthesizer(Plugin):
    @abstractmethod
    def synthesize(self, items: list[SourceItem]) -> Iterable[KnowledgeObject]:
        """Turn source items into knowledge objects that cite them."""


class Publisher(Plugin):
    @abstractmethod
    def publish(self, objects: Iterable[KnowledgeObject]) -> None:
        """Render knowledge objects somewhere."""


def discover() -> dict[str, type[Plugin]]:
    """Return installed plugins registered under the entry point group."""
    return {ep.name: ep.load() for ep in entry_points(group=ENTRY_POINT_GROUP)}
