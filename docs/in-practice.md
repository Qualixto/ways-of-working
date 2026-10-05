# In practice

These standards aren't aspirational. Qualixto applies them on every engagement, and they're built into open-source starting points you can use today.

---

## Templates that implement the standards

| Repository | What it gives you | Standards it implements |
|---|---|---|
| [python-template](https://github.com/Qualixto/python-template) | A Copier template: uv, ruff, strict mypy, pytest with a coverage gate, pre-commit with secrets scanning, dependency audits, a tested Docker image and CI | [Python Standards](standards/python-standards.md), [CI/CD Pipeline](delivery/ci-cd-pipeline.md), [Commit Message Standards](delivery/commit-message-standards.md), [Definition of Done](delivery/definition-of-done.md), [Security Excellence](pillars/security-excellence.md) |
| [data-platform-starter](https://github.com/Qualixto/data-platform-starter) | A runnable platform: dlt, DuckDB or MotherDuck, dbt and Dagster, with data contracts, severity-based quality gates and branch-isolated builds | [Data Excellence](pillars/data-excellence.md), [SQL Standards](standards/sql-standards.md), [Testing Pyramid](testing/testing-pyramid.md), [Architecture Decision Records](operations/architecture-decision-records.md) |

## Assessing a platform

The [maturity model](index.md#maturity-model) turns these pages into a scorecard. An assessment scores each pillar from 1 (Emerging) to 5 (Optimised), using evidence from the code, the pipelines and the team's own practices. It names the biggest gap and a quick win per pillar, and finishes with a prioritised plan.

Most teams don't need to reach level 5 everywhere. They need to know where they are, which gaps cost them most, and what to do first.

## Working with Qualixto

Qualixto is an independent consultancy for hands-on data platform engineering. We build platforms with your team and leave them with the standards to run them.

[Book a 30-minute call](https://calendar.app.google/X1fQ6cLut7ehLALr6){ .md-button .md-button--primary } [qualixto.com](https://qualixto.com){ .md-button }
