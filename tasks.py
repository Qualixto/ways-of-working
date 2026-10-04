"""Development tasks. Run with `uv run invoke <task>`; CI runs the same tasks."""

from invoke.context import Context
from invoke.tasks import task


@task
def format(c: Context) -> None:
    """Fix lint issues and format the code."""
    c.run("ruff check --fix", echo=True)
    c.run("ruff format", echo=True)


@task
def lint(c: Context) -> None:
    """Lint, format-check and type-check the sync script and tests."""
    c.run("ruff check", echo=True)
    c.run("ruff format --check", echo=True)
    c.run("mypy", echo=True)


@task
def test(c: Context) -> None:
    """Test the note-to-page conversion."""
    c.run("pytest", echo=True)


@task
def build(c: Context) -> None:
    """Build the site; any broken link or missing page fails the build."""
    c.run("mkdocs build --strict", echo=True)


@task
def serve(c: Context) -> None:
    """Preview the site with live reload on :8000."""
    c.run("mkdocs serve", echo=True, pty=True)


@task
def sync(c: Context, vault: str) -> None:
    """Regenerate docs/ from the ways-of-working notes in VAULT."""
    c.run(f"python scripts/sync.py --vault {vault}", echo=True)
