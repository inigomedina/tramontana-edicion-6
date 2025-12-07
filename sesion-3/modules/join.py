#!/usr/bin/env python3
"""
=============================================================================
MÓDULO: join.py
Propósito: Unir (JOIN) eventos con información de usuarios
=============================================================================

Uso:
    python join.py events.json users.json
    python join.py events.json users.json > enriched.json

Interfaz:
    Input:  Dos archivos JSON (eventos y usuarios)
    Output: Eventos enriquecidos con datos del usuario

Ejemplo:
    # Primero guardamos los datos
    ./fetch.sh /api/events > events.json
    ./fetch.sh /api/users > users.json

    # Luego hacemos el join
    python join.py events.json users.json

El resultado incluye para cada evento:
    - Todos los campos originales del evento
    - user_name: nombre del usuario
    - user_plan: plan del usuario (free/pro/enterprise)
    - user_company: empresa del usuario
=============================================================================
"""

import json
import sys

# Necesitamos dos archivos
if len(sys.argv) < 3:
    print("Uso: python join.py events.json users.json", file=sys.stderr)
    print("", file=sys.stderr)
    print("Primero obtén los datos:", file=sys.stderr)
    print("  ./fetch.sh /api/events > events.json", file=sys.stderr)
    print("  ./fetch.sh /api/users > users.json", file=sys.stderr)
    sys.exit(1)

events_file = sys.argv[1]
users_file = sys.argv[2]

# Leer archivos
with open(events_file) as f:
    events = json.load(f)

with open(users_file) as f:
    users = json.load(f)

# Crear diccionario de usuarios para búsqueda rápida
users_dict = {u["id"]: u for u in users}

# Enriquecer eventos con datos de usuario
enriched = []
for event in events:
    user_id = event.get("user_id")
    user = users_dict.get(user_id, {})

    enriched_event = {
        **event,
        "user_name": user.get("name", "Unknown"),
        "user_plan": user.get("plan", "unknown"),
        "user_company": user.get("company", "Unknown")
    }
    enriched.append(enriched_event)

# Imprimir resultado
print(json.dumps(enriched, indent=2, ensure_ascii=False))
