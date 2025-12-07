#!/usr/bin/env python3
"""
=============================================================================
MÓDULO: filter.py
Propósito: Filtrar datos JSON por un campo y valor específico
=============================================================================

Uso:
    cat events.json | python filter.py feature dashboard
    cat events.json | python filter.py user_id usr_001
    cat users.json | python filter.py plan pro

Interfaz:
    Input:  JSON array desde stdin
    Output: JSON array filtrado

Ejemplos:
    # Solo eventos del dashboard
    ./fetch.sh /api/events | python filter.py feature dashboard

    # Solo usuarios enterprise
    ./fetch.sh /api/users | python filter.py plan enterprise
=============================================================================
"""

import json
import sys

# Leer datos de stdin
data = json.load(sys.stdin)

# ¿Por qué campo y valor filtramos?
field = sys.argv[1] if len(sys.argv) > 1 else "feature"
value = sys.argv[2] if len(sys.argv) > 2 else ""

# Filtrar
if value:
    filtered = [item for item in data if item.get(field) == value]
else:
    # Si no hay valor, mostrar valores únicos disponibles
    unique_values = set(item.get(field) for item in data if field in item)
    print(f"Valores disponibles para '{field}':", file=sys.stderr)
    for v in sorted(unique_values):
        print(f"  - {v}", file=sys.stderr)
    filtered = data

# Imprimir resultado
print(json.dumps(filtered, indent=2, ensure_ascii=False))
