-- con la ayuda de Claude <3 

# 🎲 Diseño de Base de Datos - API de Apuestas

## 📋 Descripción

Sistema de gestión de apuestas deportivas que permite a los usuarios registrarse, apostar sobre eventos deportivos y gestionar sus ganancias.

---

## 🗂️ Entidades

### **Users** (Usuarios)
| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | INT | Identificador único (PK) |
| `name` | VARCHAR | Nombre del usuario |
| `email` | VARCHAR | Email del usuario |
| `balance` | DECIMAL | Saldo disponible en € |
| `created_at` | TIMESTAMP | Fecha de registro |

### **Events** (Eventos deportivos)
| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | INT | Identificador único (PK) |
| `name` | VARCHAR | Nombre del evento (ej: "Rayo vs Real Madrid") |
| `home_team` | VARCHAR | Equipo local |
| `away_team` | VARCHAR | Equipo visitante |
| `sport` | VARCHAR | Deporte (ej: "football", "basketball") |
| `competition` | VARCHAR | Competición (ej: "La Liga") |
| `event_date` | TIMESTAMP | Fecha y hora del evento |
| `status` | VARCHAR | Estado (pending, live, finished, cancelled) |
| `result` | VARCHAR | Resultado (home_win, away_win, draw, null) |
| `created_at` | TIMESTAMP | Fecha de creación |

### **Markets** (Cuotas/Opciones de apuesta)
| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | INT | Identificador único (PK) |
| `event_id` | INT | Referencia al evento (FK) |
| `market_type` | VARCHAR | Tipo de mercado (match_result, over_under) |
| `selection` | VARCHAR | Selección (home_win, draw, away_win) |
| `odds` | DECIMAL | Cuota (ej: 2.5, 3.0) |
| `created_at` | TIMESTAMP | Fecha de creación |

### **Bets** (Apuestas)
| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | INT | Identificador único (PK) |
| `user_id` | INT | Referencia al usuario (FK) |
| `market_id` | INT | Referencia al mercado (FK) |
| `stake_amount` | DECIMAL | Cantidad apostada en € |
| `potential_winnings` | DECIMAL | Ganancias potenciales (stake × odds) |
| `status` | VARCHAR | Estado (pending, won, lost, void) |
| `actual_winnings` | DECIMAL | Ganancias reales (0 si pierde) |
| `placed_at` | TIMESTAMP | Fecha de la apuesta |
| `settled_at` | TIMESTAMP | Fecha de resolución (null si pending) |

---

## 🔗 Relaciones

```
Users (1) ──→ (N) Bets
Events (1) ──→ (N) Markets
Markets (1) ──→ (N) Bets
```

**Descripción**: Users tiene muchas Bets (via `user_id`), Events tiene muchos Markets (via `event_id`), y Markets tiene muchas Bets (via `market_id`).

---

## 📌 Ejemplo de Uso

**Escenario**: Ana apuesta 10€ a que el Rayo Vallecano gana contra el Real Madrid con cuota 2.5

```
User:
  id: 1, name: "Ana", balance: 100€

Event:
  id: 1, name: "Rayo Vallecano vs Real Madrid", status: "pending"

Market:
  id: 1, event_id: 1, selection: "home_win", odds: 2.5

Bet:
  id: 1, user_id: 1, market_id: 1, stake_amount: 10€, 
  potential_winnings: 25€, status: "pending"
```

**Resultado**: El partido termina 2-1 (Rayo gana)
- Event.result = "home_win"
- Bet.status = "won"
- Bet.actual_winnings = 25€
- User.balance = 115€

---

## 🚀 Endpoints Sugeridos

```
POST   /api/users              # Crear usuario
GET    /api/users/:id          # Ver usuario y saldo

POST   /api/events             # Crear evento
GET    /api/events             # Listar eventos
GET    /api/events/:id         # Ver evento específico

POST   /api/markets            # Crear cuota
GET    /api/events/:id/markets # Ver cuotas de un evento

POST   /api/bets               # Hacer apuesta
GET    /api/users/:id/bets     # Ver apuestas de usuario

PUT    /api/events/:id/result  # Marcar resultado
```