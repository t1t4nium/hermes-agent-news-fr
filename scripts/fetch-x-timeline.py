#!/usr/bin/env python3
"""Fetch recent statuses from an X/Twitter profile timeline with browser disguise."""

import argparse
import datetime
import json
import random
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from typing import Any, Dict, List, Optional

HTML_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
    "Sec-Ch-Ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
}

SYNDICATION_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
    "Origin": "https://x.com",
    "Referer": "https://x.com/",
    "Sec-Ch-Ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
}


def fetch_status_detail(status_id: str, timeout: int = 15) -> Optional[Dict[str, Any]]:
    """Fetch status detail via syndication API with browser headers."""
    url = f"https://cdn.syndication.twimg.com/tweet-result?id={status_id}&lang=en&token=123"
    req = urllib.request.Request(url, headers=SYNDICATION_HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status == 200:
                return json.loads(resp.read().decode("utf-8", "ignore"))
    except Exception as err:
        sys.stderr.write(f"Warning: could not fetch details for status {status_id}: {err}\n")
    return None


def fetch_user_timeline_ids(username: str, timeout: int = 30) -> List[str]:
    """Scrape timeline page with browser navigation headers."""
    clean_username = username.lstrip("@")
    url = f"https://x.com/{clean_username}"
    req = urllib.request.Request(url, headers=HTML_HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            html = resp.read().decode("utf-8", "ignore")
    except Exception as err:
        sys.stderr.write(f"Error fetching profile page for @{clean_username}: {err}\n")
        return []

    user_status_ids = re.findall(rf'/{re.escape(clean_username)}/status/(\d+)', html, re.IGNORECASE)
    all_status_ids = re.findall(r'/status/(\d+)', html)

    counts = Counter(all_status_ids)
    ordered_ids: List[str] = []
    seen = set()

    for sid in user_status_ids:
        if sid not in seen:
            seen.add(sid)
            ordered_ids.append(sid)

    for sid, count in counts.most_common():
        if sid not in seen and count >= 2:
            seen.add(sid)
            ordered_ids.append(sid)

    return ordered_ids


def fetch_timeline(
    username: str,
    limit: int = 20,
    hours: Optional[int] = None,
    delay_min: float = 0.3,
    delay_max: float = 0.8,
) -> List[Dict[str, Any]]:
    """Fetch timeline statuses with jitter delay between requests."""
    clean_username = username.lstrip("@")
    status_ids = fetch_user_timeline_ids(clean_username)
    statuses: List[Dict[str, Any]] = []

    cutoff_date: Optional[datetime.datetime] = None
    if hours is not None:
        cutoff_date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=hours)

    for sid in status_ids[:limit]:
        # Human/browser jitter delay between status queries
        if delay_max > 0:
            time.sleep(random.uniform(delay_min, delay_max))

        detail = fetch_status_detail(sid)
        if not detail:
            continue

        created_at_str = detail.get("created_at")
        if cutoff_date and created_at_str:
            try:
                created_dt = datetime.datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))
                if created_dt < cutoff_date:
                    continue
            except Exception:
                pass

        statuses.append(detail)

    return statuses


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch X/Twitter timeline statuses with browser disguise.")
    parser.add_argument("username", help="X username (e.g. NousResearch or @Teknium)")
    parser.add_argument("-o", "--output", help="Optional output JSON file path", default=None)
    parser.add_argument("-n", "--limit", type=int, default=20, help="Maximum number of statuses to inspect (default: 20)")
    parser.add_argument("--hours", type=int, default=None, help="Only include statuses created within the last N hours")
    args = parser.parse_args()

    clean_username = args.username.lstrip("@")
    statuses = fetch_timeline(clean_username, limit=args.limit, hours=args.hours)

    payload = {
        "username": clean_username,
        "fetched_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "count": len(statuses),
        "statuses": statuses,
    }

    formatted_json = json.dumps(payload, indent=2, ensure_ascii=False)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(formatted_json + "\n")
        print(f"Collected {len(statuses)} status(es) for @{clean_username} -> {args.output}")
    else:
        print(formatted_json)

    return 0


if __name__ == "__main__":
    sys.exit(main())
