#!/usr/bin/env python3
"""List tweets from a daily X timeline dump (data/x/YYYY-MM-DD.json).

Reads the JSON produced by collect_sources.py (a list of Tweet objects),
filters to the last N hours and prints a compact summary.

Usage:
    python3 list_tweets.py data/x/2026-09-16.json
    python3 list_tweets.py data/x/2026-09-16.json --hours 12
"""

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone


def parse_tweet_date(tweet: dict):
    """Return an aware datetime from a tweet's created_at, or None."""
    raw = tweet.get("created_at")
    if not raw:
        return None
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None


def list_tweets(path: str, hours: int | None = None) -> list[dict]:
    """Return deduplicated tweets from the dump, newest first.

    Accepts the dump as a list (current collect_sources.py format) or as a
    legacy dict of account -> list, for backward compatibility.
    """
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        items = []
        for acct, lst in data.items():
            for t in lst:
                t = dict(t)
                t.setdefault("_acct", acct)
                items.append(t)
    else:
        items = data

    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours) if hours else None
    seen: set[str] = set()
    rows: list[dict] = []

    for t in items:
        if not isinstance(t, dict):
            continue
        if t.get("__typename") not in (None, "Tweet"):
            continue
        text = (t.get("text") or t.get("full_text") or "").strip()
        if not text:
            continue
        dt = parse_tweet_date(t)
        if cutoff and dt and dt < cutoff:
            continue
        key = t.get("id_str") or text
        if key in seen:
            continue
        seen.add(key)
        user = t.get("user") or {}
        rows.append({
            "created": t.get("created_at"),
            "user": user.get("screen_name") or t.get("_acct", "?"),
            "id": t.get("id_str") or t.get("id"),
            "text": text,
            "_dt": dt,
        })

    rows.sort(key=lambda r: (r["_dt"] is None, r["_dt"] or datetime.min.replace(tzinfo=timezone.utc)), reverse=True)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="List tweets from a daily X dump.")
    parser.add_argument("path", help="Path to a data/x/YYYY-MM-DD.json file")
    parser.add_argument("--hours", type=int, default=None,
                        help="Only show tweets within the last N hours (default: all)")
    args = parser.parse_args()

    try:
        rows = list_tweets(args.path, args.hours)
    except (OSError, ValueError) as err:
        print(f"Error: {err}", file=sys.stderr)
        return 1

    for r in rows:
        print(f"[{r['created']}] @{r['user']} id={r['id']}")
        print(f"  {r['text'].replace(chr(10), ' ')}")
        print()

    print(f"{len(rows)} tweet(s)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
