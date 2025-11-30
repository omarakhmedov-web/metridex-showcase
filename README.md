[README_METRIDEX_SHOWCASE_UPDATED.md](https://github.com/user-attachments/files/23839097/README_METRIDEX_SHOWCASE_UPDATED.md)
# Metridex — Showcase

**On-chain Risk Intelligence for Web3.**  
Metridex delivers fast, reliable risk assessments for tokens, LPs, and dApps — helping traders, protocols, and ecosystems stay safe.

This repository is a **public showcase for grants, partner evaluation, and ecosystem due diligence**.  
It contains **no proprietary logic**, only safe mock/demo components.

- **Website:** https://metridex.com  
- **Telegram Bot:** https://t.me/MetridexBot  
- **Arbitrum-focused QuickScan (primary demo domain):** https://metridex.com/quickscan  
- **Showcase API (mock):** https://metridex-showcase.onrender.com  
- **GitHub:** https://github.com/omarakhmedov-web/metridex-showcase  
- **Contact:** contact@metridex.com

---

## 🔍 Arbitrum & Orbit Chain Focus

Metridex is being actively adapted for:

- **Arbitrum One** — full QuickScan support, low-latency API, DEX/pair coverage  
- **Arbitrum Nova / Stylus-ready chains** — lightweight endpoints  
- **Orbit custom L3s** — config-based chain onboarding (Orbit Chain Adapter Kit)

This repo provides a **safe, static demonstration** for reviewers.

---

## 🧪 Public Demo (Mock API)

This endpoint simulates how the real QuickScan API responds.

- **Health:**  
  https://metridex-showcase.onrender.com/healthz
- **QuickScan (sample JSON):**  
  https://metridex-showcase.onrender.com/quickscan?chain=ethereum&address=0x6982508145454Ce325dDbE47a25d4ec3d2311933

> **Disclaimer:**  
> Mock only. Production API, risk algorithms, on-chain intel, domain scanners, and LP analyzers are private.

---

## ⚙️ Local Run (Demo Only)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
gunicorn server_stub:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
# or:
python server_stub.py
```

---

## 🛡️ Security & Licensing

This repository contains **no secrets, API keys, ML models, or internal datasets**.  
It is licensed strictly for **Evaluation Only / Non‑Commercial Use**.
