"""
Crypto Price Fetcher Skill (Synced)

Metadata:
- Author: AI OS Level 4 Synthesizer
- Tags: crypto, finance, api
"""

import logging
import requests
import json

def run(payload: str) -> str:
    ticker = payload.strip().upper() or "BTC"
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        price = data["price"]
        result = {"status": "success", "ticker": ticker, "price_usd": price, "timestamp": "now"}
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"status": "failed", "error": str(e)})
