# Copyright 2024-2026 Ironstone Advisory
# SPDX-License-Identifier: Apache-2.0
"""Core types for NeoLibrary: source items, knowledge objects, provenance."""

from __future__ import annotations

import hashlib
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone


def _now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(frozen=True)
class SourceItem:
    """One piece of raw material, hashed at ingest."""

    id: str
    origin: str
    content: str
    sha256: str
    retrieved_at: datetime = field(default_factory=_now)

    @classmethod
    def from_text(cls, content: str, origin: str) -> "SourceItem":
        digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
        return cls(id=f"src_{digest[:16]}", origin=origin, content=content, sha256=digest)


@dataclass(frozen=True)
class ProvenanceEvent:
    """An append-only record of something done to an object."""

    object_id: str
    action: str
    actor: str
    at: datetime = field(default_factory=_now)
    note: str = ""


@dataclass
class KnowledgeObject:
    """Synthesized knowledge that always carries its sources."""

    title: str
    body: str
    source_ids: list[str]
    author: str
    id: str = field(default_factory=lambda: f"ko_{uuid.uuid4().hex[:16]}")
    created_at: datetime = field(default_factory=_now)
    history: list[ProvenanceEvent] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.source_ids:
            raise ValueError("A knowledge object must cite at least one source.")
        self.history.append(ProvenanceEvent(self.id, "created", self.author))

    def record(self, action: str, actor: str, note: str = "") -> ProvenanceEvent:
        event = ProvenanceEvent(self.id, action, actor, note=note)
        self.history.append(event)
        return event
