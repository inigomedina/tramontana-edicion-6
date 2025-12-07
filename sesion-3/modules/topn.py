#!/usr/bin/env python3
"""
=============================================================================
MÓDULO: topN.py
Propósito: Extraer los N elementos con mayor conteo
=============================================================================

Uso:
    cat counts.json | python3 topN.py 5
    python3 fetch.py events | python3 counter.py user_id | python3 topN.py 10

Interfaz:
    Input:  JSON objeto con conteos desde stdin
    Output: JSON objeto con solo los top N

Ejemplo:
    Input:  {"usr_001": 45, "usr_002": 30, "usr_003": 20, "usr_004": 15}
    Output (topN.py 2): {"usr_001": 45, "usr_002": 30}
=============================================================================
"""

import json
import sys

# Leer datos de stdin
data = json.load(sys.stdin)

# ¿Cuántos top elementos queremos?
n = int(sys.argv[1]) if len(sys.argv) > 1 else 5

# Ordenar por valor descendente y tomar los primeros N
sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
top_n = dict(sorted_items[:n])

# Imprimir como JSON
print(json.dumps(top_n, indent=2, ensure_ascii=False))


