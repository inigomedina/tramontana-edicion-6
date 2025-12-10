#!/usr/bin/env python3
"""
=============================================================================
MÓDULO: join.py
Propósito: Unir datos de eventos con datos de usuarios (como un JOIN en SQL)
=============================================================================

Uso:

Interfaz:

Campos comunes:
=============================================================================
"""

import json
import sys

events_file = sys.argv[1]
users_file  = sys.argv[2]

with open(events_file, 'r') as f:
    events = json.load(f)

with open(users_file, 'r') as f:
    users = json.load(f)

users_lookup = {user['id']: user for user in users}

enriched_events = []
for event in events:
    user_id = event.get('user_id')
    if user_id in users_lookup:
        user = users_lookup[user_id]
        enriched_event = {**event, 'user_name': user.get('name'), 'user_plan': user.get('plan')}
        enriched_events.append(enriched_event)
    else:
        enriched_events.append(event)

result = json.dumps(enriched_events, indent=2, ensure_ascii=False)

print(result)
