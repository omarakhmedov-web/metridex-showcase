[Uploading README_METRIDEX_L2_SHOWCASE_CORE.md…]()
[README_METRIDEX_L2_SHOWCASE_CHAINLINK.md](https://github.com/user-attachments/files/23866439/README_METRIDEX_L2_SHOWCASE_CHAINLINK.md)
# Metridex — On-Chain Risk Intelligence (Showcase)

**Fast, reliable on-chain risk analytics for EVM ecosystems.**
Metridex helps traders, protocols, and L2 ecosystems identify risk signals early — LP locks, holder concentration, domain/SSL issues, contract metadata, liquidity anomalies, and more.

This repository is a **safe public showcase** used for:
- grant applications  
- ecosystem due diligence  
- partner integrations  
- technical review by L2 foundations  

It contains **no proprietary engine**, only demo logic and sample outputs.

---

## 🚀 Ecosystem Focus

Metridex is actively adapting its QuickScan engine for major L2s:

### Mantle Network
- QuickScan support for Mantle-native tokens  
- low-latency scan endpoints  
- integration layer for Mantle DEX pairs  
- foundation-ready dashboard mockups  

### Optimism
- OP Stack–ready QuickScan endpoints  
- security-focused user flows  
- Rapid Scan API preview  

### Arbitrum & Orbit Chains
- Arbitrum One full coverage  
- Nova & Stylus-compatible endpoints  
- Orbit Chain Adapter Kit (config-based onboarding)

### Zircuit (zk-Rollup)

- QuickScan support for Zircuit-native tokens and pools  
- low-latency scan endpoints adapted for Zircuit rollup infrastructure  
- integration stubs for Zircuit DEX / LP pairs  
- sample flows for using QuickScan as a safety layer in Zircuit wallets, bots, and dashboards  

This repository demonstrates the **public, non-sensitive** parts of the project.

---

## 🔗 Oracle & Chainlink Integration (Showcase Notes)

Metridex is designed to sit alongside existing market data and oracle layers rather than replace them.
For Chainlink and other oracle networks, we focus on:

- simple interface examples for consuming external price and Proof-of-Reserve style feeds;
- mapping these feeds into additional risk flags and thresholds inside QuickScan;
- basic dashboards or bot flows that show combined “price + risk” views for end-users.

In this showcase, any oracle-related examples stay strictly high-level: no secrets, no production keys, and no proprietary risk logic — only the integration surface that L2 foundations and reviewers need to understand.

---

## 🧪 Public Demo (Mock API)

These endpoints simulate the behavior of the production QuickScan API.

- **Health:**  
  https://metridex-showcase.onrender.com/healthz

- **QuickScan (sample JSON):**  
  https://metridex-showcase.onrender.com/quickscan?chain=ethereum&address=0x6982508145454Ce325dDbE47a25d4ec3d2311933

> **Note:**  
> Production risk scoring, LP/holder engine, domain intelligence, and on-chain inspection modules remain private.

---

## 📦 Contents of This Repository

- server_stub.py — demo-only server  
- mock QuickScan responses  
- static showcases for reviewers  
- no private logic, no API keys, no secrets  

This repo is intentionally minimal: only what ecosystems need to validate feasibility and integration flow.

---

## ⚙️ Run Locally (Demo Mode)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
gunicorn server_stub:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
# or:
python server_stub.py
```

---

---

## 🛡️ Security & Licensing

This repository:
- contains **no sensitive code**,  
- does **not** include the production QuickScan engine,  
- is licensed for **Evaluation Only / Non-Commercial Use**.

For questions, collaboration, or ecosystem integrations:

- Website: https://metridex.com  
- Bot: https://t.me/MetridexBot  
- Email: contact@metridex.com  
