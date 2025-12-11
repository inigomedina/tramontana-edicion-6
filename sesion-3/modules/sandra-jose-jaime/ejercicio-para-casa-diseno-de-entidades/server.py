#!/usr/bin/env python3
"""
API de métricas de producto para Tramontana - Sesión 3
Un servidor simple sin dependencias externas.

Uso:
    python3 server.py

Endpoints:
    GET /api/events        - Eventos de uso del producto
    GET /api/users         - Información de usuarios
    GET /api/features      - Features del producto
    GET /api/events/stream - Stream de eventos en tiempo real (SSE)
    GET /api/events/slow   - Endpoint lento (simula proceso pesado)
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime, timedelta
import random
import time
import os

# =============================================================================
# DATOS DEL PRODUCTO FICTICIO: "Metrix" - Herramienta de analytics para PMs
# =============================================================================

# --------------------------------------------------------------------------
# 1. Definir la lista de mapeo (Variable de Python, Nombre del Archivo JSON)
# --------------------------------------------------------------------------
# Cada elemento es una tupla: (nombre_de_la_variable, nombre_del_archivo)
archivos_a_cargar = [
    ("USERS", "users.json"),
    ("EVENTS", "events.json"),
    ("SELECTIONS", "selections.json"),
    ("ODDS", "odds.json"),
    ("BETS", "bets.json"),
    ("TRANSFERS", "transfers.json")
]

# Un diccionario para almacenar todas las variables de forma dinámica.
# Es la mejor forma de gestionar variables creadas dentro de un bucle.
datos_cargados = {}


# --------------------------------------------------------------------------
# 2. Iterar sobre la lista y cargar cada archivo
# --------------------------------------------------------------------------
print("--- Iniciando proceso de carga de archivos JSON ---")

for nombre_variable, nombre_archivo in archivos_a_cargar:
    print(f"\nProcesando: {nombre_archivo} -> Variable: {nombre_variable}")
    
    try:
        # Abrir el archivo
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            
            # Cargar el JSON en el diccionario 'datos_cargados' usando 
            # el 'nombre_variable' como clave
            datos_cargados[nombre_variable] = json.load(f)
            
            print(f"   ✅ Éxito. Contenido cargado (Tipo: {type(datos_cargados[nombre_variable]).__name__})")
            print(f"La variable {nombre_variable} tiene {len(datos_cargados[nombre_variable])} registros.")
            
    except FileNotFoundError:
        print(f"   ❌ ERROR: Archivo no encontrado ('{nombre_archivo}'). Saltando.")
        # Asignamos un valor nulo para saber que falló la carga
        datos_cargados[nombre_variable] = None 
        
    except json.JSONDecodeError:
        print(f"   ❌ ERROR: Formato JSON inválido en '{nombre_archivo}'. Saltando.")
        datos_cargados[nombre_variable] = None


# --------------------------------------------------------------------------
# 3. Acceder a las variables creadas
# --------------------------------------------------------------------------
print("\n--- Resultados Finales ---")

# Puedes acceder a tus variables finales así:
USERS = datos_cargados.get("USERS")
EVENTS = datos_cargados.get("EVENTS")
SELECTIONS = datos_cargados.get("SELECTIONS")
ODDS = datos_cargados.get("ODSS")
BETS = datos_cargados.get("BETS")
TRANSFERS = datos_cargados.get("TRANSFERS")

# Comprobación:
if USERS is not None:
    print(f"La variable USERS tiene {len(USERS)} registros.")
else:
    print("La variable USERS no se pudo cargar.")

# Ejemplo de acceso:
# print("\nPrimer producto cargado:")
# print(PRODUCTS_DATA[0] if PRODUCTS_DATA and len(PRODUCTS_DATA) > 0 else "N/A")

# =============================================================================
# SERVIDOR HTTP
# =============================================================================


class APIHandler(BaseHTTPRequestHandler):
    """Handler para la API REST."""

    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def _send_json(self, data, status=200):
        self._set_headers(status)
        self.wfile.write(json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8"))

    def do_GET(self):
        """Maneja peticiones GET."""

        if self.path == "/" or self.path == "/api":
            self._send_json({
                "name": "Metrix API",
                "version": "1.0",
                "description": "API de métricas de producto para Tramontana",
                "endpoints": [
                    {"path": "/api/users", "description": "Información de los que se \"divierten\""},
                    {"path": "/api/events", "description": "Información de los eventos deportivos"},
                    {"path": "/api/selections", "description": "Apuestas de evetos disponibles"},
                    {"path": "/api/odds", "description": "Cuotas deportivas activas e historico de cuotas de cada apuesta"},
                    {"path": "/api/bets", "description": "Información sobre las apuestas realizadas por los usuarios"},
                    {"path": "/api/transfers", "description": "Información sobre las transferencias monetarias"},
                ]
            })

        elif self.path == "/api/users":
            self._send_json(USERS)

        elif self.path == "/api/events":
            self._send_json(EVENTS)

        elif self.path == "/api/selections":
            self._send_json(SELECTIONS)
            
        elif self.path == "/api/odds":
            self._send_json(ODDS)

        elif self.path == "/api/bets":
            self._send_json(BETS)

        elif self.path == "/api/transfers":
            self._send_json(TRANSFERS)

        else:
            self._send_json({"error": "Endpoint not found", "path": self.path}, 404)

    def log_message(self, format, *args):
        """Log más limpio."""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {args[0]}")


def run_server(port=3000):
    """Arranca el servidor."""
    server = HTTPServer(("localhost", port), APIHandler)

    print(f"""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   
║   Metrix API - Servidor de métricas de producto                  
║                                                                   
║   Corriendo en: http://localhost:{port}                           
║                                                                   
║   Endpoints:                                                      
║     GET /api/users         → usuarios                 
║     GET /api/events        → eventos          
║     GET /api/selections      → apuestas disponibles         
║     GET /api/odds         → cuotas                 
║     GET /api/bets        → apuestas          
║     GET /api/transfers      → transferencias              
║                                                                   
║   Prueba:                                                         
║     curl http://localhost:{port}/api/users                       
║     curl http://localhost:{port}/api/events                
║                                                                   
║   Ctrl+C para detener                                             
║                                                                   
╚═══════════════════════════════════════════════════════════════════╝
""")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
        server.shutdown()


if __name__ == "__main__":
    run_server()
