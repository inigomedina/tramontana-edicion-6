#!/usr/bin/env python3
"""
=============================================================================
MÓDULO: report.py
Propósito: Generar reporte de power users
=============================================================================

Uso:

Interfaz:

Campos comunes:
=============================================================================
"""

import json
import sys

data = json.load(sys.stdin)

position = 1
for user_info, count in data.items():
    print(f"{position}. {user_info} con {count} eventos")
    position += 1
