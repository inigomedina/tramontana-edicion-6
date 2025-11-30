#!/usr/bin/env python3
"""
=============================================================================
MÓDULO: counter.py
Propósito: Contar ocurrencias de un campo en los datos JSON
=============================================================================

Uso:
    cat events.json | python counter.py feature
    cat events.json | python counter.py user_id
    cat users.json | python counter.py plan

Interfaz:
    Input:  JSON array desde stdin
    Output: JSON objeto con conteos {valor: cantidad}

Campos comunes:
    - events: feature, user_id, event_type
    - users: plan, company
=============================================================================
"""

import json
import sys
from collections import Counter

# Leer datos de stdin
data = json.load(sys.stdin)

# ¿Qué campo queremos contar?
field = sys.argv[1] if len(sys.argv) > 1 else "feature"

# Contar ocurrencias
counts = Counter(item.get(field, "unknown") for item in data)

# Ordenar de mayor a menor
sorted_counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

# Imprimir como JSON
print(json.dumps(sorted_counts, indent=2, ensure_ascii=False))
