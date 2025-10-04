from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/quickscan")
def quickscan():
    chain = request.args.get("chain", "ethereum")
    address = request.args.get("address", "0x0000000000000000000000000000000000000000")
    demo = {
        "chain": chain,
        "address": address,
        "pair": "TOKEN/WETH on uniswap (ethereum)" if chain == "ethereum" else "TOKEN/WBNB on pancakeswap (bsc)",
        "price_usd": 0.00001,
        "fdv_usd": 4090000000,
        "mcap_usd": 4090000000,
        "liquidity_usd": 59190000,
        "volume24h_usd": 4770000,
        "delta_24h_pct": -0.74,
        "source": "Demo",
        "site": "https://example.org/",
        "domain_checks": {
            "rdap": "OK (demo)",
            "created": "—",
            "registrar": "—",
            "ssl": {"status": "OK", "expires": "2025-12-16", "issuer": "Let's Encrypt"},
            "wayback_first": "2021-12-18"
        },
        "risk": {"overall": "LOW RISK", "score": 20},
        "actions": {
            "open_in_dex": f"https://app.uniswap.org/#/swap?outputCurrency={address}",
            "open_in_scan": f"https://etherscan.io/address/{address}",
            "copy_ca": address
        },
        "notes": [
            "Static mock response for demo purposes only.",
            "Production logic is private."
        ]
    }
    return jsonify(demo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
