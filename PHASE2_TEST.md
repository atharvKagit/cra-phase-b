# Phase 2 E2E — cra-phase-b + Code Review Assistant

Branch: **`test/review-quality-phase-2`** → open PR into **`main`**.

This PR intentionally triggers:

| Signal | File | What CRA should find |
|--------|------|----------------------|
| HIGH scanner | `app.py` | SQL injection (`OR 1=1`) |
| Impact caller | `api.py` (on **main**) | Imports changed `app.get_user`; LLM may warn on caller |
| LOW-ish noise | `app.py` | Unused demo token constant (filtered when `REVIEW_MIN_SEVERITY=HIGH`) |

---

## 0. CRA prep (once)

From `Code_Review_Assistant` repo root:

```bash
npm run migrate
docker compose up -d
docker compose ps   # postgres + kafka healthy
```

Terminal 1 — API:

```bash
cd ~/Code_Review_Assistant
npm run dev -w @cra/api
```

Terminal 2 — worker (optional severity filter):

```bash
cd ~/Code_Review_Assistant
# Default (no filter):
npm run dev -w @cra/worker

# Or only HIGH+ in GitHub comment:
# REVIEW_MIN_SEVERITY=HIGH npm run dev -w @cra/worker
```

Terminal 3 — dashboard:

```bash
cd ~/Code_Review_Assistant
npm run dev -w @cra/dashboard
```

Sign in at http://localhost:5173 → confirm **cra-phase-b** is linked to your GitHub App.

---

## 1. Push this branch and open PR

```bash
cd ~/Code_Review_Assistant/test_repos/cra-phase-b
git push -u origin test/review-quality-phase-2
```

GitHub → **atharvKagit/cra-phase-b** → **Compare & pull request**

- Base: `main`
- Compare: `test/review-quality-phase-2`
- Title: `Phase 2: impact caller + SQLi + suppression/rerun test`

Wait for worker: `Starting PR review` → `Review completed`.

---

## 2. Test suppression (Track 1)

1. Dashboard → **cra-phase-b** → latest review → open issues.
2. Find the **SQL injection** / `OR 1=1` finding on **`app.py`** → click **Not useful**.
3. Click **Re-run review** (no git push).
4. **Expect:** that SQLi finding **does not** come back in GitHub comment or dashboard.
5. **Expect:** impact finding on **`api.py`** (if any) still appears.

Optional DB check (CRA Postgres):

```sql
SELECT fingerprint FROM suppressed_findings sf
JOIN repositories r ON r.id = sf.repository_id
WHERE r.full_name = 'atharvKagit/cra-phase-b';
```

---

## 3. Test REVIEW_MIN_SEVERITY (Track 2)

1. Stop worker. Restart with:

```bash
REVIEW_MIN_SEVERITY=HIGH npm run dev -w @cra/worker
```

2. Dashboard → **Re-run review** on the same PR.
3. **Expect:** GitHub summary has **HIGH/CRITICAL only** (SQLi yes; LOW maintainability nits no).
4. Remove env var and restart worker to restore default.

---

## 4. Test impact context (Track 3 — Python)

Worker logs on first review should include:

```text
Built impact context ... callers: 1
```

Graph edge like: `api.py imports_changed app.py`

**Expect:** LLM may comment on **`api.py`** (caller still uses `get_user` return value without a `None` check).

---

## 5. Test re-run without empty commit (Track 4)

1. After review status is **completed**, click **Re-run review**.
2. **Expect:** status → **pending** → **completed** again.
3. **Expect:** same GitHub PR summary comment **updated** (not a second bot comment).
4. API log: `Published PR_REVIEW_REQUESTED (manual rerun)`.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Review skipped / not claimable | Use **Re-run review** or push a new commit |
| Suppression errors | Run `npm run migrate` (migration `011`) |
| No webhook | ngrok → App webhook URL → `/webhooks/github` |
| Worker 403 | GitHub App installed on **atharvKagit/cra-phase-b** |
