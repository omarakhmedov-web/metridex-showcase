# DEPLOY_RENDER_SHOWCASE (Sanitized)

High-level notes for running the Metridex demo service on Render.

## Runtime
- Python 3.11, `Flask` + `Gunicorn` (1 worker is enough for demo)
- Health check: `GET /healthz` → returns JSON

## Start command
```
gunicorn server:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
```

## Environment Variables (no secrets in repo)
Set these via Render **Environment** (values are provided privately):
- `TELEGRAM_TOKEN`
- `WEBHOOK_SECRET` (path component for `/webhook/<secret>`)
- `WEBHOOK_HEADER_SECRET` (HMAC / secret header for Telegram)
- Optional: `BOT_USERNAME`, `CACHE_TTL_SECONDS`, `HTTP_TIMEOUT`

On‑chain/RPC (demo-friendly):
- `RPC_URLS` = JSON with per‑chain endpoints (ETH/BSC/Polygon)
- You can also set legacy per‑chain variables if needed.

**Note:** The production list of RPCs and thresholds is private. This demo uses generic public RPCs.
