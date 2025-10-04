[README_FINAL_REAL_2025-10-04_22-48.md](https://github.com/user-attachments/files/22704591/README_FINAL_REAL_2025-10-04_22-48.md)
# Metridex — Showcase

**On-chain Risk Intelligence for Web3.**  
Metridex helps investors and DeFi users identify potential scam projects before they invest.  
This repository is a **public showcase** for hackathon evaluation — safe, self-contained, and without proprietary logic.

- **Website:** https://metridex.com  
- **Telegram Bot:** https://t.me/MetridexBot  
- **Public Demo (mock):** https://metridex-showcase.onrender.com  
- **GitHub:** [https://github.com/omarakhmedov-web/metridex-showcase](https://github.com/omarakhmedov-web/metridex-showcase)  
- **Contact:** contact@metridex.com

---

## 🔍 Public Demo (mock API)

This demo API illustrates how Metridex QuickScan works.  
It provides a static, safe JSON response for judges and partners to test.

- **Health:**  
  https://metridex-showcase.onrender.com/healthz
- **QuickScan (sample JSON):**  
  https://metridex-showcase.onrender.com/quickscan?chain=ethereum&address=0x6982508145454Ce325dDbE47a25d4ec3d2311933

> **Disclaimer:** This is a static mock response.  
> The production API, algorithms, and datasets are private and used only in the live Metridex system.

---

## ⚙️ Quick Start (local)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
gunicorn server_stub:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
# or simply:
python server_stub.py
```

---

## 🛡️ Security & Licensing

No secrets, API keys, or internal datasets are stored here.  
See `LICENSE`: **Evaluation Only / No Commercial Use.**
