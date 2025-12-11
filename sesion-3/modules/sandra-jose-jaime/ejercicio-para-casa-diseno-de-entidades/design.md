# 📚 Diseño de la API de Métricas de Producto (Metrix API)

Este documento describe las entidades (recursos) y las relaciones fundamentales de la API, basadas en los archivos de datos JSON.

## 1. Entidades (Recursos)

La API expone **seis** recursos principales, que se corresponden con los archivos JSON cargados.

| Recurso | Archivo Fuente | Descripción | Número de Registros |
| :--- | :--- | :--- | :--- |
| **USERS** | `users.json` | Usuarios registrados en el sistema. | 3 |
| **EVENTS** | `events.json` | Eventos deportivos o de otro tipo disponibles para apostar. | 4 |
| **SELECTIONS** | `selections.json` | Opciones específicas dentro de un evento (ej. "Equipo A Gana"). | 4 |
| **ODDS** | `odds.json` | Valores de cuota (multiplicadores de ganancia) para una selección. | 4 |
| **BETS** | `bets.json` | Apuestas realizadas por los usuarios. | 10 |
| **TRANSFERS** | `transfers.json` | Movimientos de saldo de los usuarios (depósitos, apuestas, pagos). | 10 |

---

## 2. Diagrama de Relación de Entidades

La estructura de la API sigue un modelo relacional, donde los recursos se enlazan mediante claves externas (`_id`).


---

## 3. Detalle de las Relaciones

Las relaciones son de tipo **Uno a Muchos (1:N)**, lo que significa que un registro en la entidad "Uno" puede estar vinculado a múltiples registros en la entidad "Muchos".

| Entidad "Uno" | Entidad "Muchos" | Clave Externa (FK) | Relación |
| :--- | :--- | :--- | :--- |
| **USERS** | **BETS** | `user_id` en `bets.json` | Un usuario puede realizar **muchas** apuestas. |
| **USERS** | **TRANSFERS** | `user_id` en `transfers.json` | Un usuario puede tener **muchas** transferencias. |
| **EVENTS** | **SELECTIONS** | `event_id` en `selections.json` | Un evento tiene **muchas** opciones de selección. |
| **SELECTIONS** | **ODDS** | `selection_id` en `odds.json` | Una selección puede tener **muchas** cuotas (históricas o actualizadas). |
| **ODDS** | **BETS** | `odd_id` en `bets.json` | Una cuota específica se usa para realizar **muchas** apuestas. |

### Ejemplo de Flujo de Datos

1.  El **`EVENT`** (id 501: "Atlético vs. Sevilla") tiene una **`SELECTION`** (id 601: "Atlético Gana").
2.  Esa **`SELECTION`** (601) tiene una **`ODD`** (id 701: valor 1.8500).
3.  El **`USER`** (id 100) usa esa **`ODD`** (701) para crear una **`BET`** (id 801).
4.  La **`BET`** (801) genera una **`TRANSFER`** (id 901) con el monto negativo (`-50.00`).

---

## 4. Estructura y Ejemplos de Endpoints

Basado en una convención RESTful, estos serían los *endpoints* principales:

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `GET` | `/api/users` | Obtener la lista completa de usuarios. |
| `GET` | `/api/users/{id}` | Obtener los detalles de un usuario específico. |
| `GET` | `/api/events` | Obtener la lista de eventos. |
| `GET` | `/api/events/{id}/selections` | Obtener las selecciones disponibles para un evento. |
| `GET` | `/api/bets` | Obtener todas las apuestas realizadas. |
| `GET` | `/api/users/{user_id}/transfers` | Obtener el historial de transferencias de un usuario. |
