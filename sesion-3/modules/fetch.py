#!/usr/bin/env python3
"""
=============================================================================
MÓDULO: fetch.py
Propósito: Obtener datos de la API (funciona en Mac, Linux y Windows)
=============================================================================

Uso:
    python3 fetch.py events              → Muestra eventos
    python3 fetch.py users               → Muestra usuarios
    python3 fetch.py features            → Muestra features

    python3 fetch.py events > data.json  → Guarda en archivo

Interfaz:
    Input:  nombre del recurso (events, users, features)
    Output: JSON con los datos
=============================================================================
"""

import sys
import urllib.request
import json

# Configuración
BASE_URL = "http://localhost:3000/api"

# ¿Qué recurso pedimos?
resource = sys.argv[1] if len(sys.argv) > 1 else "events"

# Construir URL
url = f"{BASE_URL}/{resource}"

try:
    # Hacer la petición
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    # Imprimir JSON formateado
    print(json.dumps(data, indent=2, ensure_ascii=False))

except urllib.error.URLError as e:
    print(f"Error: No se pudo conectar a {url}", file=sys.stderr)
    print(f"¿Está corriendo el servidor? (python3 api/server.py)", file=sys.stderr)
    sys.exit(1)
