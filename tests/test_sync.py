from pathlib import Path, PurePosixPath

import pytest
import sync
from sync import convert, destination, slugify

PAGES = {
    "Engineering Excellence": PurePosixPath("index.md"),
    "Ownership": PurePosixPath("principles/ownership.md"),
    "Git Workflow": PurePosixPath("delivery/git-workflow.md"),
}
PAGE = PurePosixPath("principles/ownership.md")


def body(text: str, page: PurePosixPath = PAGE) -> str:
    return convert(text, page, PAGES).removeprefix(sync.HEADER).strip()


def test_slugify() -> None:
    assert slugify("CI-CD Pipeline") == "ci-cd-pipeline"
    assert slugify("End-to-End Tests") == "end-to-end-tests"


@pytest.mark.parametrize(
    ("note", "page"),
    [
        ("Engineering Excellence.md", "index.md"),
        ("Security and compliance.md", "security/security-and-compliance.md"),
        ("delivery/CI-CD Pipeline.md", "delivery/ci-cd-pipeline.md"),
    ],
)
def test_destination(note: str, page: str) -> None:
    assert destination(PurePosixPath(note)) == PurePosixPath(page)


def test_wikilinks_become_relative_links() -> None:
    assert body("See [[Git Workflow]].") == (
        "See [Git Workflow](../delivery/git-workflow.md)."
    )


def test_links_from_the_root_page_have_no_parent_hops() -> None:
    text = body("- [[Ownership]]", PurePosixPath("index.md"))

    assert text == "- [Ownership](principles/ownership.md)"


def test_aliases_and_vault_paths_resolve_by_note_name() -> None:
    assert body("[[delivery/Git Workflow|branching]]") == (
        "[branching](../delivery/git-workflow.md)"
    )


def test_unresolved_links_become_plain_text() -> None:
    assert body("Ask [[Someone Private]] first.") == "Ask Someone Private first."


def test_breadcrumbs_out_of_the_handbook_are_dropped() -> None:
    text = body(
        "← [[knowledge-base/Knowledge Base]]\n\n# Title\n\n← [[Engineering Excellence]]"
    )

    assert text == "# Title\n\n← [Engineering Excellence](../index.md)"


def test_trailing_whitespace_is_stripped() -> None:
    assert body("**Date:** YYYY-MM-DD  \nNext") == "**Date:** YYYY-MM-DD\nNext"


def test_tags_sections_and_repeated_rules_are_removed() -> None:
    text = body("# Title\n\n---\n\n## Tags\n\n`#git`\n\n---\n\nEnd")

    assert text == "# Title\n\n---\n\nEnd"


def test_sync_regenerates_docs_and_keeps_hand_written_pages(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    notes = tmp_path / "vault" / sync.SOURCE
    (notes / "principles").mkdir(parents=True)
    (notes / "Engineering Excellence.md").write_text("# Home\n\n- [[Ownership]]")
    (notes / "principles" / "Ownership.md").write_text("# Ownership")
    docs = tmp_path / "docs"
    (docs / "stale").mkdir(parents=True)
    (docs / "in-practice.md").write_text("kept")
    monkeypatch.setattr(sync, "DOCS", docs)

    written = sync.sync(tmp_path / "vault")

    assert written == [
        PurePosixPath("index.md"),
        PurePosixPath("principles/ownership.md"),
    ]
    assert not (docs / "stale").exists()
    assert (docs / "in-practice.md").read_text() == "kept"
    assert "(principles/ownership.md)" in (docs / "index.md").read_text()


def test_sync_fails_without_notes(tmp_path: Path) -> None:
    with pytest.raises(SystemExit, match="No notes found"):
        sync.sync(tmp_path)
