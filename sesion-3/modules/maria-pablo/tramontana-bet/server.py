#!/usr/bin/env python3
"""
API de Casa de Apuestas - Tramontana Bet
Un servidor simple para gestionar apuestas deportivas.

Uso:
    python3 server.py

Endpoints:
    GET /api/users                  - Lista de usuarios
    GET /api/events                 - Lista de eventos deportivos
    GET /api/bets                   - Lista de apuestas
    GET /api/odds                   - Lista de cuotas
    GET /api/users/:id/bets         - Apuestas de un usuario específico
    GET /api/events/:id/bets        - Apuestas sobre un evento específico
    GET /api/events/open            - Eventos aún abiertos para apostar
"""

import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

# =============================================================================
# CARGAR DATOS DESDE ARCHIVOS JSON
# =============================================================================

def load_json_data():
    """Carga todos los datos desde los archivos JSON"""
    data_dir = os.path.dirname(os.path.abspath(__file__))
    
    with open(os.path.join(data_dir, 'users.json'), 'r', encoding='utf-8') as f:
        users = json.load(f)
    
    with open(os.path.join(data_dir, 'events.json'), 'r', encoding='utf-8') as f:
        events = json.load(f)
    
    with open(os.path.join(data_dir, 'bets.json'), 'r', encoding='utf-8') as f:
        bets = json.load(f)
    
    with open(os.path.join(data_dir, 'odds.json'), 'r', encoding='utf-8') as f:
        odds = json.load(f)
    
    return users, events, bets, odds

# Cargar datos al inicio
USERS, EVENTS, BETS, ODDS = load_json_data()

# =============================================================================
# SERVIDOR HTTP
# =============================================================================

class TramontanaBetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        """Maneja todas las peticiones GET"""
        
        # Parse URL
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)
        
        # Headers comunes
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # Router principal
        if path == '/api/users':
            self.handle_users()
        elif path == '/api/events':
            self.handle_events()
        elif path == '/api/bets':
            self.handle_bets()
        elif path == '/api/odds':
            self.handle_odds()
        elif path.startswith('/api/users/') and path.endswith('/bets'):
            user_id = path.split('/')[3]
            self.handle_user_bets(user_id)
        elif path.startswith('/api/events/') and path.endswith('/bets'):
            event_id = path.split('/')[3]
            self.handle_event_bets(event_id)
        elif path == '/api/events/open':
            self.handle_open_events()
        else:
            self.handle_404()
    
    def handle_users(self):
        """GET /api/users - Lista de usuarios"""
        response = json.dumps(USERS, indent=2, ensure_ascii=False)
        self.wfile.write(response.encode('utf-8'))
    
    def handle_events(self):
        """GET /api/events - Lista de eventos"""
        response = json.dumps(EVENTS, indent=2, ensure_ascii=False)
        self.wfile.write(response.encode('utf-8'))
    
    def handle_bets(self):
        """GET /api/bets - Lista de apuestas"""
        response = json.dumps(BETS, indent=2, ensure_ascii=False)
        self.wfile.write(response.encode('utf-8'))
    
    def handle_odds(self):
        """GET /api/odds - Lista de cuotas"""
        response = json.dumps(ODDS, indent=2, ensure_ascii=False)
        self.wfile.write(response.encode('utf-8'))
    
    def handle_user_bets(self, user_id):
        """GET /api/users/:id/bets - Apuestas de un usuario específico"""
        user_bets = [bet for bet in BETS if bet['user_id'] == user_id]
        response = json.dumps(user_bets, indent=2, ensure_ascii=False)
        self.wfile.write(response.encode('utf-8'))
    
    def handle_event_bets(self, event_id):
        """GET /api/events/:id/bets - Apuestas sobre un evento específico"""
        # Necesitamos encontrar las odds del evento y luego las bets de esas odds
        event_odds = [odd for odd in ODDS if odd['event_id'] == event_id]
        event_odds_ids = [odd['id'] for odd in event_odds]
        event_bets = [bet for bet in BETS if bet['odds_id'] in event_odds_ids]
        response = json.dumps(event_bets, indent=2, ensure_ascii=False)
        self.wfile.write(response.encode('utf-8'))
    
    def handle_open_events(self):
        """GET /api/events/open - Eventos aún abiertos para apostar"""
        open_events = [event for event in EVENTS if event['status'] == 'pending']
        response = json.dumps(open_events, indent=2, ensure_ascii=False)
        self.wfile.write(response.encode('utf-8'))
    
    def handle_404(self):
        """Maneja rutas no encontradas"""
        self.send_response(404)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = json.dumps({"error": "Endpoint not found"})
        self.wfile.write(response.encode('utf-8'))
    
    def log_message(self, format, *args):
        """Log personalizado"""
        print(f"[{self.date_time_string()}] {format % args}")

# =============================================================================
# ARRANCAR SERVIDOR
# =============================================================================

def run_server(port=3001):
    server_address = ('', port)
    httpd = HTTPServer(server_address, TramontanaBetHandler)
    
    print(f"🎰 Tramontana Bet API corriendo en http://localhost:{port}")
    print("Endpoints disponibles:")
    print("  - GET /api/users")
    print("  - GET /api/events") 
    print("  - GET /api/bets")
    print("  - GET /api/odds")
    print("  - GET /api/users/:id/bets")
    print("  - GET /api/events/:id/bets")
    print("  - GET /api/events/open")
    print("\nPrueba:")
    print(f"  curl http://localhost:{port}/api/events")
    print()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
