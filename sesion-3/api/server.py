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

# =============================================================================
# DATOS DEL PRODUCTO FICTICIO: "Metrix" - Herramienta de analytics para PMs
# =============================================================================

USERS = [
    {"id": "usr_001", "name": "Ana García", "email": "ana@startup.io", "plan": "pro", "signup_date": "2024-01-15", "company": "StartupCo"},
    {"id": "usr_002", "name": "Carlos Ruiz", "email": "carlos@bigcorp.com", "plan": "enterprise", "signup_date": "2024-02-20", "company": "BigCorp"},
    {"id": "usr_003", "name": "María López", "email": "maria@agency.es", "plan": "free", "signup_date": "2024-03-10", "company": "Digital Agency"},
    {"id": "usr_004", "name": "Pedro Sánchez", "email": "pedro@techie.dev", "plan": "pro", "signup_date": "2024-04-05", "company": "Techie Labs"},
    {"id": "usr_005", "name": "Laura Martín", "email": "laura@ecom.shop", "plan": "pro", "signup_date": "2024-05-12", "company": "EcomShop"},
    {"id": "usr_006", "name": "Diego Torres", "email": "diego@fintech.io", "plan": "enterprise", "signup_date": "2024-01-08", "company": "FinTech Plus"},
    {"id": "usr_007", "name": "Elena Vega", "email": "elena@saas.tools", "plan": "free", "signup_date": "2024-06-22", "company": "SaaS Tools"},
    {"id": "usr_008", "name": "Javier Mora", "email": "javier@design.co", "plan": "pro", "signup_date": "2024-07-01", "company": "Design Co"},
    {"id": "usr_009", "name": "Sara Blanco", "email": "sara@data.team", "plan": "enterprise", "signup_date": "2024-02-14", "company": "Data Team"},
    {"id": "usr_010", "name": "Miguel Ángel", "email": "miguel@retail.mx", "plan": "free", "signup_date": "2024-08-30", "company": "Retail MX"},
]

FEATURES = [
    {"id": "feat_dashboard", "name": "dashboard", "status": "stable", "release_date": "2023-06-01", "team": "frontend"},
    {"id": "feat_reports", "name": "reports", "status": "stable", "release_date": "2023-09-15", "team": "analytics"},
    {"id": "feat_export_csv", "name": "export_csv", "status": "stable", "release_date": "2023-11-01", "team": "backend"},
    {"id": "feat_export_pdf", "name": "export_pdf", "status": "beta", "release_date": "2024-08-01", "team": "backend"},
    {"id": "feat_integrations", "name": "integrations", "status": "stable", "release_date": "2024-01-10", "team": "platform"},
    {"id": "feat_alerts", "name": "alerts", "status": "stable", "release_date": "2024-03-20", "team": "backend"},
    {"id": "feat_collaboration", "name": "collaboration", "status": "beta", "release_date": "2024-09-01", "team": "frontend"},
    {"id": "feat_ai_insights", "name": "ai_insights", "status": "alpha", "release_date": "2024-10-15", "team": "ml"},
    {"id": "feat_custom_dashboards", "name": "custom_dashboards", "status": "stable", "release_date": "2024-04-01", "team": "frontend"},
    {"id": "feat_api_access", "name": "api_access", "status": "stable", "release_date": "2023-12-01", "team": "platform"},
]

# Generar eventos realistas
def generate_events():
    """Genera eventos de uso simulados para las últimas 4 semanas."""
    events = []
    event_types = ["pageview", "click", "feature_use", "export", "share"]

    # Pesos para simular uso realista (dashboard se usa mucho más)
    feature_weights = {
        "dashboard": 35,
        "reports": 20,
        "export_csv": 12,
        "export_pdf": 3,
        "integrations": 8,
        "alerts": 10,
        "collaboration": 5,
        "ai_insights": 2,
        "custom_dashboards": 15,
        "api_access": 5,
    }

    # Usuarios más activos (power users)
    user_weights = {
        "usr_001": 25,  # Ana - muy activa
        "usr_002": 30,  # Carlos - enterprise, muy activo
        "usr_003": 8,   # María - free, poco activa
        "usr_004": 18,  # Pedro - pro, activo
        "usr_005": 15,  # Laura - pro, activa
        "usr_006": 28,  # Diego - enterprise, muy activo
        "usr_007": 5,   # Elena - free, poco activa
        "usr_008": 12,  # Javier - pro, moderado
        "usr_009": 22,  # Sara - enterprise, activa
        "usr_010": 4,   # Miguel - free, muy poco activo
    }

    features_list = list(feature_weights.keys())
    features_weights_list = list(feature_weights.values())
    users_list = list(user_weights.keys())
    users_weights_list = list(user_weights.values())

    # Generar ~500 eventos en las últimas 4 semanas
    base_date = datetime.now()
    event_id = 1

    for days_ago in range(28, -1, -1):
        # Más eventos en días laborables
        day_of_week = (base_date - timedelta(days=days_ago)).weekday()
        events_today = random.randint(12, 25) if day_of_week < 5 else random.randint(3, 8)

        for _ in range(events_today):
            user_id = random.choices(users_list, weights=users_weights_list)[0]
            feature = random.choices(features_list, weights=features_weights_list)[0]
            event_type = random.choice(event_types)

            # Timestamp aleatorio durante el día (horario laboral más probable)
            hour = random.choices(
                range(24),
                weights=[1,1,1,1,1,2,3,5,8,10,10,9,8,9,10,10,8,6,4,3,2,2,1,1]
            )[0]
            minute = random.randint(0, 59)

            event_date = base_date - timedelta(days=days_ago)
            timestamp = event_date.replace(hour=hour, minute=minute, second=0, microsecond=0)

            events.append({
                "id": f"evt_{event_id:04d}",
                "user_id": user_id,
                "event_type": event_type,
                "feature": feature,
                "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
            })
            event_id += 1

    # Ordenar por timestamp
    events.sort(key=lambda x: x["timestamp"], reverse=True)
    return events

# Generar eventos al iniciar
EVENTS = generate_events()


# =============================================================================
# SERVIDOR HTTP
# =============================================================================

def generate_live_event():
    """Genera un evento nuevo en tiempo real (para el stream)."""
    event_types = ["pageview", "click", "feature_use", "export", "share"]
    features = ["dashboard", "reports", "export_csv", "alerts", "custom_dashboards"]
    users = ["usr_001", "usr_002", "usr_004", "usr_006", "usr_009"]

    return {
        "id": f"evt_live_{random.randint(1000, 9999)}",
        "user_id": random.choice(users),
        "event_type": random.choice(event_types),
        "feature": random.choice(features),
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "live": True
    }


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

    def _send_stream(self):
        """
        Server-Sent Events (SSE) - Producer-Consumer en tiempo real.
        El servidor PRODUCE eventos, el cliente los CONSUME conforme llegan.
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Connection", "keep-alive")
        self.end_headers()

        print("[STREAM] Cliente conectado - produciendo eventos...")

        try:
            # Enviar 10 eventos, uno cada 1-2 segundos
            for i in range(10):
                event = generate_live_event()
                event["sequence"] = i + 1

                # Formato SSE: "data: {json}\n\n"
                message = f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
                self.wfile.write(message.encode("utf-8"))
                self.wfile.flush()

                print(f"[STREAM] Evento {i+1}/10: {event['feature']} ({event['event_type']})")

                # Esperar entre 1 y 2 segundos (simula eventos en tiempo real)
                time.sleep(random.uniform(1.0, 2.0))

            # Mensaje final
            final = {"type": "complete", "message": "Stream finalizado", "total_events": 10}
            self.wfile.write(f"data: {json.dumps(final)}\n\n".encode("utf-8"))
            self.wfile.flush()
            print("[STREAM] Stream completado")

        except (BrokenPipeError, ConnectionResetError):
            print("[STREAM] Cliente desconectado")

    def _send_slow(self):
        """
        Endpoint lento - simula una operación que tarda.
        Útil para entender async y por qué no bloquear.
        """
        print("[SLOW] Procesando petición lenta (3 segundos)...")

        # Simular proceso pesado
        time.sleep(3)

        result = {
            "status": "completed",
            "message": "Operación completada después de 3 segundos",
            "processing_time": "3s",
            "tip": "En un sistema real, esto podría ser: generar PDF, procesar datos, llamar a otra API..."
        }

        print("[SLOW] Completado")
        self._send_json(result)

    def do_GET(self):
        """Maneja peticiones GET."""

        if self.path == "/" or self.path == "/api":
            self._send_json({
                "name": "Metrix API",
                "version": "1.0",
                "description": "API de métricas de producto para Tramontana",
                "endpoints": [
                    {"path": "/api/events", "description": "Todos los eventos de uso"},
                    {"path": "/api/users", "description": "Información de usuarios"},
                    {"path": "/api/features", "description": "Features del producto"},
                    {"path": "/api/events/stream", "description": "Stream de eventos en tiempo real (SSE)"},
                    {"path": "/api/events/slow", "description": "Endpoint lento (3s) para ver async"},
                ]
            })

        elif self.path == "/api/events":
            self._send_json(EVENTS)

        elif self.path == "/api/events/stream":
            self._send_stream()

        elif self.path == "/api/events/slow":
            self._send_slow()

        elif self.path == "/api/users":
            self._send_json(USERS)

        elif self.path == "/api/features":
            self._send_json(FEATURES)

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
║     GET /api/events        → {len(EVENTS):>4} eventos             
║     GET /api/users         → {len(USERS):>4} usuarios              
║     GET /api/features      → {len(FEATURES):>4} features          
║     GET /api/events/stream → eventos en tiempo real (SSE)         
║     GET /api/events/slow   → respuesta lenta (3s)                 
║                                                                   
║   Prueba:                                                         
║     curl http://localhost:{port}/api/events                       
║     curl http://localhost:{port}/api/events/stream                
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
