import pytest

from neolibrary.core import KnowledgeObject, SourceItem


def test_source_item_is_hashed():
    item = SourceItem.from_text("hello", origin="file:///hello.md")
    assert item.sha256 == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    assert item.id.startswith("src_")


def test_knowledge_object_requires_sources():
    with pytest.raises(ValueError):
        KnowledgeObject(title="t", body="b", source_ids=[], author="rob")


def test_knowledge_object_records_provenance():
    item = SourceItem.from_text("hello", origin="file:///hello.md")
    ko = KnowledgeObject(title="t", body="b", source_ids=[item.id], author="rob")
    ko.record("edited", "rob", "tightened wording")
    assert [e.action for e in ko.history] == ["created", "edited"]
