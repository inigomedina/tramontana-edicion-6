#!/usr/bin/env python3
"""
=============================================================================
MÓDULO: report.py
Propósito: Generar reporte Markdown legible de power users
=============================================================================

Uso:

Interfaz:

Campos comunes:
=============================================================================
"""

import json
import sys

data = json.load(sys.stdin)

with open('users.json', 'r') as f:
    users = json.load(f)

users_lookup = {user['id']: user for user in users}

position = 1
for user_id, count in data.items():
    user = users_lookup[user_id]
    name = user['name']
    plan = user['plan']
    print(f"{position}. {name} ({plan}) con {count}")
    position += 1
