#!/usr/bin/env python3
"""
=============================================================================
MÓDULO: report.py
Propósito: Generar un reporte en Markdown a partir de datos JSON
=============================================================================

Uso:
    cat counts.json | python report.py "Top Features"
    cat counts.json | python report.py "Power Users" > report.md

Interfaz:
    Input:  JSON objeto con conteos {clave: número}
    Output: Texto Markdown formateado

Ejemplo de pipeline completo:
    ./fetch.sh /api/events | python counter.py feature | python topn.py 5 | python report.py "Features más usadas"
=============================================================================
"""

import json
import sys
from datetime import datetime

# Leer datos de stdin
data = json.load(sys.stdin)

# Título del reporte
title = sys.argv[1] if len(sys.argv) > 1 else "Reporte"

# Generar Markdown
print(f"# {title}")
print(f"\n_Generado: {datetime.now().strftime('%Y-%m-%d %H:%M')}_")
print()

# Calcular total para porcentajes
total = sum(data.values())

print("| Item | Cantidad | % del total |")
print("|------|----------|-------------|")

for item, count in data.items():
    percentage = (count / total * 100) if total > 0 else 0
    print(f"| {item} | {count} | {percentage:.1f}% |")

print()
print(f"**Total:** {total}")
