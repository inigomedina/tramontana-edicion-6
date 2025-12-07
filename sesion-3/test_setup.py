#!/usr/bin/env python3
"""
Test de setup para la Sesión 3.
Ejecuta: python3 test_setup.py
"""

import sys
import os

def check(name, condition, hint=""):
    status = "OK" if condition else "FALTA"
    symbol = "[OK]" if condition else "[X]"
    print(f"  {symbol} {name}")
    if not condition and hint:
        print(f"      Hint: {hint}")
    return condition

print()
print("=" * 50)
print("  TEST DE SETUP - Sesión 3: Catedrales y Bazares")
print("=" * 50)
print()

all_ok = True

# Python version
print("Python:")
version = sys.version_info
version_ok = version.major == 3 and version.minor >= 6
all_ok &= check(
    f"Versión {version.major}.{version.minor}.{version.micro}",
    version_ok,
    "Necesitas Python 3.6 o superior"
)
print()

# Archivos necesarios
print("Archivos:")
base_dir = os.path.dirname(os.path.abspath(__file__))

files_to_check = [
    ("api/server.py", "API del servidor"),
    ("modules/fetch.py", "Módulo fetch"),
    ("modules/counter.py", "Módulo counter"),
]

for filepath, desc in files_to_check:
    full_path = os.path.join(base_dir, filepath)
    exists = os.path.exists(full_path)
    all_ok &= check(f"{desc} ({filepath})", exists, f"Archivo no encontrado: {filepath}")

print()

# Módulos Python estándar (no deberían fallar, pero por si acaso)
print("Módulos Python:")
modules_ok = True
try:
    import json
    import http.server
    from collections import Counter
    from datetime import datetime
except ImportError as e:
    modules_ok = False
all_ok &= check("Módulos estándar (json, http, collections)", modules_ok)
print()

# Resumen
print("=" * 50)
if all_ok:
    print("  RESULTADO: Todo listo para la sesión")
    print()
    print("  Siguiente paso:")
    print("    python3 api/server.py")
    print()
else:
    print("  RESULTADO: Hay cosas pendientes (ver arriba)")
    print()
print("=" * 50)
print()
