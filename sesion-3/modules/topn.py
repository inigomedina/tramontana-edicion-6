#!/usr/bin/env python3
"""
=============================================================================
MÓDULO: topn.py
Propósito: Extraer los N elementos con mayor valor de un JSON de conteos
=============================================================================

Uso:
    cat counts.json | python topn.py 5
    cat counts.json | python topn.py 10

Interfaz:
    Input:  JSON objeto con conteos {clave: número}
    Output: JSON objeto con solo los top N

Ejemplo de pipeline:
    ./fetch.sh /api/events | python counter.py feature | python topn.py 5
=============================================================================
"""

import json
import sys

# Leer datos de stdin (esperamos un diccionario de conteos)
data = json.load(sys.stdin)

# ¿Cuántos queremos?
n = int(sys.argv[1]) if len(sys.argv) > 1 else 5

# Ordenar y tomar top N
sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
top_n = dict(sorted_items[:n])

# Imprimir resultado
print(json.dumps(top_n, indent=2, ensure_ascii=False))
