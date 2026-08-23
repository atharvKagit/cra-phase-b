# cra-phase-b

Fresh demo repo for **Code Review Assistant** Phase B+ testing (clean PR path).

## Purpose

1. PR review pipeline (webhook → Kafka → worker)
2. `review-events`: `REVIEW_STARTED` → `REVIEW_COMPLETED`
3. Later: inline comments, metrics, feedback

## Layout

| File | Purpose |
|------|---------|
| `app.py` | Intentional SQL injection (scanner + LLM target) |
| `api.py` | Calls `get_user` — impact / caller signal |
| `helpers.py` | Weak sanitizer |
| `db.py` | Fake query helper |
| `config.py` | Clean config on `main` |
| `requirements.txt` | Minimal deps |

## Branches

- `main` — baseline (slightly safer `get_user`)
- `feature/phase-b-review` — worsens SQL in `app.py` for the PR
