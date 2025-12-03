[README_METRIDEX_L2_SHOWCASE_CORE (2).md](https://github.com/user-attachments/files/23914876/README_METRIDEX_L2_SHOWCASE_CORE.2.md)
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

Metridex is designed as a **chain-agnostic QuickScan layer** for EVM ecosystems.

Current priority L2s and rollups include:
- Mantle Network  
- Optimism (OP Stack)  
- Arbitrum & Orbit chains  
- Zircuit (zk-rollup, in progress)  

This repository demonstrates only the **public, non-sensitive** parts of the project and how the QuickScan surface can be adapted per ecosystem without exposing proprietary risk logic.

---


## ✅ What Metridex can do today

Metridex QuickScan already provides a practical, production-ready feature set for traders, L2 ecosystems, and partners:

### QuickScan risk snapshots
- 5–10 second **QuickScan snapshot** for a token or pool (via Telegram bot or API).  
- Unified view of **price, FDV, MC, liquidity, 24h volume**, basic volatility and activity.  
- Consistent risk label (e.g. *Low / Medium / High risk*) based on multiple signals, not a single metric.

### On‑chain & holder analytics (lite)
- Contract age and basic deployment metadata.  
- Holder distribution (top holders, contract/custodian concentration, basic “whale” view).  
- LP position overview (total LP, basic split between main holders, mixing with contracts).

### Website / domain intelligence
- WHOIS age and registrar checks.  
- SSL certificate status and expiry.  
- Wayback/archival presence to distinguish **fresh throwaway domains** от более устоявшихся сайтов.

### LP‑lock & liquidity safety (lite)
- LP‑lock status (locked / partially locked / unlocked / mixed via contracts).  
- Approximate unlock dates and high‑level assessment of **how much liquidity is at real risk**.  
- Highlighting suspicious patterns (e.g. single contract holding most LP).

### Reports & sharing
- HTML **QuickScan report** with full breakdown of signals.  
- PDF snapshot suitable for sharing in chats, channels, or due diligence threads.  
- Inline buttons in Telegram (“Open in Scan”, “Open in DEX”, “Copy CA”, etc.) for fast action.

### Telegram‑first UX
- Telegram bot **@MetridexBot** as the primary interface for traders and communities.  
- Stateless inline buttons (no зависания при повторных нажатиях) and clear “Processing…” states for heavier checks.  
- Multi‑language groundwork (EN/RU today, extendable to other languages).



### Watchlists & alerts (live, beta)

- `/watch <address>` — добавляет токен/пул в персональный watchlist.  
- Несколько пресетов алертов с разными порогами по `d5 / d1h / d24`, объёму и частоте (например, 1–3% движение, $150k–400k volume, интервал 10–30 минут, cooldown 45–90 минут).  
- Быстрое **mute / unmute** (в т.ч. на 24 часа) для отключения спама по конкретному токену.  
- Удаление из watchlist и подсчёт активных наблюдаемых позиций (*“Total: N”*).  

Алерты приходят в Telegram напрямую, чтобы трейдер видел изменения по отслеживаемым активам без открытия графиков или сканеров.
---

## 🧭 Roadmap — what we are building next

Metridex is not just a single QuickScan endpoint; it is a roadmap toward a full **on‑chain risk & trust layer** for DeFi.

### Near‑term roadmap
- **Owner intel (lite):** analysis of contract and LP owners (EOA vs contracts, multisig, custodians).  
- **Watchlists & alerts:** user‑level watchlists for tokens/pools with Telegram notifications on key risk events.  
- **Deeper LP analytics:** better handling of LP locks, vesting contracts, and multi‑pool setups (incl. Uniswap v3‑style positions).  
- **Extended chain coverage:** more EVM L2s and rollups (beyond ETH/BSC/Polygon/Base/Arbitrum/Optimism) with consistent UX.  
- **Partner integrations:** embeddable QuickScan widgets and APIs for wallets, DEXes, Telegram‑ботов и аналитических панелей.

### Longer‑term vision
- **Metridex as a “trust oracle”:** standardised risk snapshots that can be consumed by bots, front‑ends, and protocols.  
- **Badges & verification:** “Verified by Metridex” badges for communities, launchpads, and Telegram‑каналов.  
- **Licensing & teams:** Pro / Teams plans with API access, seats for research teams, and custom SLAs for ecosystems.  
- **Educational layer:** in‑product explainers and articles that teach users *why* certain signals matter (LP, holders, domains, etc.).

This showcase repository exists to demonstrate **how QuickScan looks and behaves in public form** — without exposing the proprietary risk engine that powers the production Metridex stack.



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
