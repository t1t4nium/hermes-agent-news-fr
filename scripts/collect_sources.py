#!/usr/bin/env python3
"""Collect X timelines for hermes-agent-news-fr source accounts into a daily deduplicated JSON file.

Fails loudly: a per-account fetch error, or an account that returns zero tweets,
is reported on stderr and reflected in a non-zero exit code, so the cron job
surfaces it instead of silently producing incomplete data.
"""

import datetime
import json
import os
import subprocess
import sys
import tempfile
from typing import Any, Dict, List

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fetch-x-timeline.py")
SOURCES_FILE = os.path.join(BASE_DIR, "data", "sources.json")


def load_source_accounts() -> List[str]:
    """Read data/sources.json and return the X account usernames (kind=x_account)."""
    if not os.path.exists(SOURCES_FILE):
        sys.stderr.write(f"ERROR: sources file not found: {SOURCES_FILE}\n")
        return []
    try:
        with open(SOURCES_FILE, "r", encoding="utf-8") as f:
            entries = json.load(f)
    except (json.JSONDecodeError, OSError) as err:
        sys.stderr.write(f"ERROR: cannot read {SOURCES_FILE}: {err}\n")
        return []

    accounts: List[str] = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        if entry.get("kind") != "x_account":
            continue
        # Prefer the URL path segment (x.com/<username>); fall back to the name.
        username = ""
        url = entry.get("url", "")
        if url:
            username = url.rstrip("/").rsplit("/", 1)[-1]
        if not username:
            username = (entry.get("name") or "").lstrip("@")
        if username:
            accounts.append(username)
    return accounts


def parse_tweet_date(tweet: Dict[str, Any]) -> float:
    """Extract a sortable timestamp in seconds from a tweet dictionary."""
    # 1. Check created_at (ISO format)
    created_at = tweet.get("created_at")
    if created_at:
        try:
            dt = datetime.datetime.fromisoformat(created_at.replace("Z", "+00:00"))
            return dt.timestamp()
        except Exception:
            pass

    # 2. Check created_at_ms
    created_at_ms = tweet.get("created_at_ms")
    if created_at_ms:
        try:
            return float(created_at_ms) / 1000.0
        except Exception:
            pass

    # 3. Fallback to status id if numeric
    tid = tweet.get("id_str") or tweet.get("id")
    if tid and str(tid).isdigit():
        return float(tid)

    return 0.0


def load_existing_tweets(filepath: str) -> Dict[str, Dict[str, Any]]:
    """Load existing tweets mapped by their unique identifier."""
    if not os.path.exists(filepath):
        return {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return {
                    str(item.get("id_str") or item.get("id")): item
                    for item in data
                    if isinstance(item, dict) and (item.get("id_str") or item.get("id"))
                }
    except Exception as err:
        sys.stderr.write(f"Warning: could not read {filepath}: {err}\n")
    return {}


def fetch_account(username: str, tmp_out: str) -> List[Dict[str, Any]]:
    """Fetch one account via fetch-x-timeline.py. Raises on failure or bad output."""
    cmd = [
        sys.executable,
        SCRIPT_PATH,
        username,
        "--hours",
        "24",
        "-n",
        "20",
        "-o",
        tmp_out,
    ]
    subprocess.run(cmd, capture_output=True, text=True, check=True)
    with open(tmp_out, "r", encoding="utf-8") as f:
        account_payload = json.load(f)
    if isinstance(account_payload, dict) and "statuses" in account_payload:
        return account_payload.get("statuses", [])
    if isinstance(account_payload, list):
        return account_payload
    return []


def main() -> int:
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    hour_str = now.strftime("%Hh%M")

    accounts = load_source_accounts()
    if not accounts:
        print("ERROR: no x_account sources found in data/sources.json", file=sys.stderr)
        return 1

    target_dir = os.path.join(BASE_DIR, "data", "x")
    os.makedirs(target_dir, exist_ok=True)
    target_file = os.path.join(target_dir, f"{date_str}.json")

    print(f"Starting X collection for {date_str} at {hour_str} into {target_file}")

    tweets_by_id = load_existing_tweets(target_file)
    initial_count = len(tweets_by_id)

    errors: List[str] = []
    empty: List[str] = []
    malformed: List[str] = []
    per_account: Dict[str, int] = {}

    with tempfile.TemporaryDirectory() as tmp_dir:
        for username in accounts:
            tmp_out = os.path.join(tmp_dir, f"{username}.json")
            try:
                statuses = fetch_account(username, tmp_out)
            except subprocess.CalledProcessError as err:
                msg = (err.stderr or "").strip() or f"exit code {err.returncode}"
                errors.append(f"@{username}: {msg}")
                per_account[username] = 0
                continue
            except (json.JSONDecodeError, OSError) as err:
                errors.append(f"@{username}: unreadable output ({err})")
                per_account[username] = 0
                continue

            valid = 0
            unusable = 0
            for tweet in statuses:
                if not isinstance(tweet, dict):
                    unusable += 1
                    continue
                tid = str(tweet.get("id_str") or tweet.get("id"))
                text = tweet.get("text") or tweet.get("full_text")
                if tid and tid != "None" and text:
                    tweets_by_id[tid] = tweet
                    valid += 1
                else:
                    unusable += 1
            per_account[username] = valid

            if statuses and valid == 0:
                # The account returned tweet objects but none carried id+text:
                # X likely changed its data shape. Treat as a hard anomaly.
                malformed.append(username)
                print(
                    f"ERROR: @{username} returned {len(statuses)} object(s) "
                    f"but none usable (missing id/text), likely X structure change",
                    file=sys.stderr,
                )
            elif valid == 0:
                empty.append(username)
                print(f"WARN: @{username} returned 0 tweets in the last 24h", file=sys.stderr)
            else:
                print(f"OK: @{username} fetched ({valid} tweets)")

    sorted_tweets = sorted(
        tweets_by_id.values(),
        key=parse_tweet_date,
        reverse=True,
    )

    with open(target_file, "w", encoding="utf-8") as f:
        json.dump(sorted_tweets, f, ensure_ascii=False, indent=2)

    summary = ", ".join(f"@{u}={per_account.get(u, 0)}" for u in accounts)

    # Hard failures: a fetch error, malformed data, or every account empty
    # (global block / structure change). Single quiet accounts are only warned.
    if errors:
        print(
            f"ERROR: collection incomplete: {len(errors)} account(s) failed: "
            + "; ".join(errors),
            file=sys.stderr,
        )
        print(f"Summary: {summary}", file=sys.stderr)
        return 1

    if malformed:
        print(
            f"ERROR: data shape anomaly on {', '.join(malformed)}. "
            "X likely changed its response structure. Inspect fetch-x-timeline.py.",
            file=sys.stderr,
        )
        print(f"Summary: {summary}", file=sys.stderr)
        return 1

    if len(empty) == len(accounts):
        print(
            "ERROR: no tweets returned for ANY account. "
            "Possible global X block or structure change. Inspect fetch-x-timeline.py.",
            file=sys.stderr,
        )
        print(f"Summary: {summary}", file=sys.stderr)
        return 1

    added_count = len(sorted_tweets) - initial_count
    print(
        f"Collection finished: {len(sorted_tweets)} total tweets "
        f"({added_count} new). Summary: {summary}"
    )
    if empty:
        print(
            f"Note: {len(empty)} account(s) quiet in the last 24h: {', '.join(empty)}",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
