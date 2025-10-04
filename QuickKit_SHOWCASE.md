# QuickKit_SHOWCASE (Smoke tests)

Use these tests after deploying the demo server:

## Health & Version
- `GET /healthz` → `{"ok": true, "version": "..."}`
- `GET /version`  → returns a short version string

## Telegram Webhook
Use your bot token to check webhook status (replace `TOKEN`):
```
curl -s "https://api.telegram.org/bot$TOKEN/getWebhookInfo"
```
You should see `ok:true` and a `url` pointing to `/webhook/<secret>`.

## Crypto IPN (Optional for demo)
A minimal POST to your `/crypto_webhook/<secret>` endpoint should return `200 OK`.
Live callbacks are configured privately in production.
