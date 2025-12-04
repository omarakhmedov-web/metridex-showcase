# Metridex – System Design

This document describes the high-level system design of Metridex: a multi-chain risk & analytics layer for DeFi traders, wallets and bots. It also explains how the architecture extends to new chains such as the XRP Ledger (XRPL) and the XRPL EVM Sidechain.

---

## 1. Overview

Metridex provides:

- A one-screen **QuickScan** for any supported asset / pool (risk score, signals, key metrics).
- **Deeper reports** (HTML/PDF) for due diligence and sharing.
- **Alerts / watchlists** for tracking selected assets over time.
- **Integration options** for wallets, DEX front-ends and bots.

The system is intentionally designed to be **multi-chain**.  
Current production integrations focus on EVM networks (Ethereum, BNB Chain, Polygon, Base).  
Additional chains (e.g. XRPL mainnet and XRPL EVM Sidechain) are integrated via dedicated adapters.

---

## 2. High-level architecture

Core components:

1. **Client layer**
   - Telegram bot and (optionally) web UI.
   - Accepts user input (contract address, pair, token symbol, etc.).
   - Displays QuickScan results, inline actions, alerts and links.

2. **API & Risk Engine (backend service)**
   - Python (Flask / Gunicorn) HTTP service.
   - Exposes a small API surface (health checks, QuickScan endpoints, report generation).
   - Orchestrates calls to chain adapters and external data sources.
   - Aggregates metrics into a unified QuickScan result (score, signals, explanations, links).

3. **Chain adapters**
   - Encapsulate chain-specific logic (RPC calls, explorers, DEX APIs, address formats, concepts).
   - Provide a normalized view of:
     - Assets / tokens
     - Liquidity / pools
     - Holders / concentration
     - Age / history
     - Selected anomaly indicators

4. **Rendering layer**
   - Formats compact Telegram messages (Markdown).
   - Renders detailed HTML views and converts them to PDF when needed.
   - Produces links to explorers, DEXes and dashboards.

5. **Storage & caching**
   - Caches recent scan results and metadata to reduce latency and external calls.
   - Stores lightweight telemetry (anonymous usage, per-chain latencies, error codes).

Logical diagram (not deployment-specific):

`[Clients (Telegram / Web)] → [API & Risk Engine] → [Chain Adapters] → [Nodes / Explorers / DEX APIs]`

---

## 3. Code organization (summary)

The repository is organized into the following main areas (filenames may vary slightly):

- `server.py`
  - Flask / Gunicorn entrypoint.
  - HTTP routing, health checks, webhook handling for the Telegram bot.

- `risk_engine.py`
  - Orchestration of risk checks.
  - Combines data from chain adapters and external APIs into a QuickScan result.

- `chain/evm_adapter.py` (current)
  - EVM-specific integration (Ethereum, BNB Chain, Polygon, Base).
  - JSON-RPC calls to nodes and/or indexers.
  - Normalization of pools, tokens, holders and basic on-chain metrics.

- `renderers.py`
  - Formatting of Telegram messages (Markdown).
  - HTML and PDF report generation.

- `buttons.py`, `state.py`
  - Inline keyboard definitions.
  - Simple state handling for callbacks and multi-step flows.

- `common.py`, `utils.py`
  - Shared utilities (logging, configuration, retries, timeouts, formatting helpers).

- `tests/`
  - Lightweight sanity tests for core flows.

This structure allows new chains to be added as new adapters with minimal impact on the rest of the codebase.

---

## 4. Current chains (EVM)

The current production-ready implementation supports multiple EVM networks:

- **Ethereum**
- **BNB Chain**
- **Polygon**
- **Base**

For these networks the system already supports:

- Fetching and normalizing on-chain data:
  - Token contracts and metadata.
  - Liquidity pools and basic DEX metrics (price, volume, liquidity).
  - Simple holder / concentration metrics and contract age.
- Computing risk signals:
  - Liquidity depth / LP-style security (where applicable).
  - Holder concentration heuristics.
  - Basic anomaly / red-flag signals.
- Presenting results:
  - QuickScan messages in Telegram.
  - Detailed HTML/PDF reports.
- Basic alerting and watchlist primitives.

This EVM implementation is the “proven path” that new chains follow in terms of architecture and UX.

---

## 5. Planned XRPL integration

XRPL integration is designed as a **first-class chain adapter**, not just a simple RPC switch.

### 5.1 XRPL mainnet

The planned XRPL mainnet adapter will:

- Connect to **XRPL full-history APIs** and **WebSocket streams**.
- Index:
  - Native DEX order books and AMM pools.
  - Issued currencies (trust lines) and issuer accounts.
  - Relevant account and trust line flags (e.g. `freeze`, `defaultRipple`).
- Derive QuickScan metrics for XRPL assets and pools:
  - “LP-style” liquidity security for AMM positions.
  - Issuer / holder concentration and age.
  - Basic anomaly signals around key accounts and flows.
- Feed these metrics back into the risk engine so that clients can display:
  - XRPL-specific QuickScan views.
  - Watchlists and alerts for XRPL assets.
  - XRPL risk dashboards and HTML/PDF reports.

As XRPL evolves (e.g. amendments around DEX/AMM behaviour, hooks / smart-transaction features), the adapter and risk engine will be updated so that new protections and risks are reflected in the scoring.

### 5.2 XRPL EVM Sidechain

For the **XRPL EVM Sidechain**:

- The existing **EVM adapter** will be reused:
  - The adapter will be pointed to XRPL EVM RPC endpoints.
  - Contracts, pools and LP positions on the sidechain will be analysed with the same logic already used on Ethereum / BNB / Polygon / Base.
- Where useful, the system will correlate XRPL EVM activity with XRPL mainnet assets to present a unified, chain-aware risk picture.

---

## 6. Libraries and frameworks

The backend primarily uses:

- **Python 3.x**
- **Flask** – HTTP API, webhooks.
- **Gunicorn** – production WSGI server.
- **Requests / httpx** – outbound HTTP clients (RPC / APIs).
- **Telegram Bot API library** – integration with Telegram for the bot interface.
- **Jinja2 / HTML templating** – generation of HTML for detailed reports.
- **HTML→PDF tooling** (e.g. wkhtmltopdf / WeasyPrint or similar) – PDF exports.

Exact versions and dependencies are documented in `requirements.txt`.

---

This design keeps each chain neatly encapsulated in its own adapter, while reusing the same risk engine, rendering logic and client layer. It also provides a clear path to bring XRPL and the XRPL EVM Sidechain into the existing, battle-tested architecture.
