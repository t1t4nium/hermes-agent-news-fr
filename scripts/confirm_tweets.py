#!/usr/bin/env python3
"""Confirm tweets via the Twitter syndication API (no key needed)."""
import json, sys, urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"

for tid in sys.argv[1:]:
    url = f"https://cdn.syndication.twimg.com/tweet-result?id={tid}&lang=en&token=123"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            d = json.loads(r.read().decode("utf-8", "ignore"))
        print(f"=== {tid} ===")
        print("user:", d.get("user", {}).get("screen_name"))
        print("created:", d.get("created_at"))
        print("text:", (d.get("text") or "").replace("\n", " "))
        print()
    except Exception as e:
        print(f"=== {tid} === FAILED: {e}\n")
