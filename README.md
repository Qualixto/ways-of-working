# Qualixto Ways of Working

How Qualixto builds data platforms: six principles, six pillars of engineering excellence, a maturity model to assess against, and the practical standards that make them real.

**Read it at [qualixto.github.io/ways-of-working](https://qualixto.github.io/ways-of-working/).**

---

## What's inside

| Section | What it covers |
|---|---|
| Principles | The *why*: customer value, simplicity, automation, built-in quality, ownership, continuous improvement |
| Pillars | The *what*: technical, delivery, quality, operational, security and data excellence, each with strong and weak signals |
| Maturity model | Five levels, from Emerging to Optimised, for scoring a team or platform |
| Delivery | Git workflow, pull requests, commit messages, CI/CD and the Definition of Done |
| Testing | The testing pyramid: unit, integration and end-to-end |
| Standards | Python, SQL and documentation |
| Operations | Architecture decision records, incident management, monitoring |
| Metrics | Engineering and data metrics worth tracking |

The standards are put into practice in [python-template](https://github.com/Qualixto/python-template) and [data-platform-starter](https://github.com/Qualixto/data-platform-starter).

## How it's maintained

The handbook is written as linked notes, then synced into `docs/` by [`scripts/sync.py`](scripts/sync.py), which turns wikilinks into site links. So pages under `docs/` are generated: change the source notes and re-sync, rather than editing them here. `docs/in-practice.md` and the assets are hand-written.

```sh
uv sync
uv run invoke sync --vault ~/path/to/vault   # regenerate docs/
uv run invoke serve                          # preview on :8000
uv run invoke build                          # strict build; broken links fail
```

CI lints and tests the sync script, builds the site in strict mode, and deploys to GitHub Pages from `main`.

## Licence

Content is licensed [CC BY 4.0](LICENSE): reuse and adapt it for your own team, with attribution to Qualixto.
