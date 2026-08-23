# End-to-end: cra-phase-b + Code Review Assistant

Replace `YOUR_GITHUB_USER` with your login (e.g. `atharvKagit`).

## 1. Create empty GitHub repo

GitHub → New repository → name **`cra-phase-b`** → create (no README).

## 2. Push local repo

```bash
cd ~/Code_Review_Assistant/test_repos/cra-phase-b
git remote add origin https://github.com/YOUR_GITHUB_USER/cra-phase-b.git
git push -u origin main
git push -u origin feature/phase-b-review
```

## 3. Webhook

Repo → Settings → Webhooks → Add webhook

| Field | Value |
|-------|--------|
| Payload URL | `https://YOUR_NGROK_HOST/webhooks/github` |
| Content type | `application/json` |
| Secret | Same as `GITHUB_WEBHOOK_SECRET` in CRA `.env` |
| Events | Pull requests + Pushes |

## 4. Open PR

GitHub → New pull request

- Base: `main`
- Compare: `feature/phase-b-review`
- Title: `Phase B: unsafe get_user for review-events`

## 5. Watch

- Worker: `Starting PR review` → completed
- Kafka UI → `review-events`: `REVIEW_STARTED` then `REVIEW_COMPLETED`
