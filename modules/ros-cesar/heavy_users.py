#!/usr/bin/env python3
"""
heavy_users.py — Calcula heavy users a partir de eventos recibidos por stdin.

Uso:
    python3 fetch.py events | python3 heavy_users.py
    python3 fetch.py events | python3 heavy_users.py 10   → top 10
"""

import sys
import json
import subprocess


def load_users_from_api():
    # Llama al módulo fetch.py como proceso independiente
    result = subprocess.run(
        ["python3", "fetch.py", "users"],
        capture_output=True,
        text=True
    )
    return json.loads(result.stdout)


def load_events_from_stdin():
    raw = sys.stdin.read()
    return json.loads(raw)


def heavy_users(events, users, limit=None):
    counts = {}

    for ev in events:
        uid = ev.get("user_id")
        if uid:
            counts[uid] = counts.get(uid, 0) + 1

    ranking = []
    for user in users:
        uid = user.get("id")
        ranking.append({
            "id": uid,
            "name": user.get("name", "(sin nombre)"),
            "event_count": counts.get(uid, 0)
        })

    ranking.sort(key=lambda u: u["event_count"], reverse=True)

    if limit:
        ranking = ranking[:limit]

    return ranking


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None

    events = load_events_from_stdin()
    users = load_users_from_api()

    ranking = heavy_users(events, users, limit)

    print(json.dumps(ranking, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
