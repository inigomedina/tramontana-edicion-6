#!/usr/bin/env python3
"""
=============================================================================
MÓDULO: join.py
Propósito: Unir conteos de usuarios con datos de usuarios
=============================================================================

Uso:

Interfaz:

Campos comunes:
=============================================================================
"""

import json
import sys

user_counts = json.load(sys.stdin)

users_file = sys.argv[1]
with open(users_file, 'r') as f:
    users = json.load(f)

users_lookup = {user['id']: user for user in users}

enriched_counts = {}
for user_id, count in user_counts.items():
    if user_id in users_lookup:
        user = users_lookup[user_id]
        name = user.get('name', 'Unknown')
        plan = user.get('plan', 'unknown')
        enriched_counts[f"{name} ({plan})"] = count
    else:
        enriched_counts[user_id] = count

result = json.dumps(enriched_counts, indent=2, ensure_ascii=False)

print(result)
