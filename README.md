[README.md](https://github.com/user-attachments/files/22704523/README.md)
# Metridex — Showcase

**On‑chain risk intelligence** for Web3. This repository is a **public showcase** used for hackathons and partner review.
It includes safe documentation, screenshots, and a mock API. **No proprietary logic** is published here.

- Website: https://metridex.com
- Telegram bot: https://t.me/MetridexBot
- Demo video: *(add link)*
- Contact: contact@metridex.com

## Public demo (mock)

This repository includes a **mock API** for demonstration purposes only.

- Health:  
  https://metridex-showcase-demo.onrender.com/healthz
- QuickScan (sample JSON):  
  https://metridex-showcase-demo.onrender.com/quickscan?chain=ethereum&address=0x6982508145454Ce325dDbE47a25d4ec3d2311933

**Disclaimer:** Static mock response. Production API and internal datasets are private.

## Quick start (local)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
gunicorn server_stub:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
# or simply: python server_stub.py
```

## Security & Licensing
No secrets or keys are stored here.  
See `LICENSE`: Evaluation Only / No Commercial Use.
