# Cheatsheet: Módulos disponibles

## Arrancar la API

```bash
cd tramontana-edicion-6
python3 api/server.py
```

Deja esta terminal abierta. Abre otra para trabajar.

---

## Módulos que os doy

| Módulo | Qué hace | Input | Output |
|--------|----------|-------|--------|
| `fetch.py` | Obtiene datos de la API | recurso | JSON array |
| `counter.py` | Cuenta por campo | JSON array | JSON conteos |

---

## Usando fetch.py

```bash
# Ver eventos en pantalla
python3 fetch.py events

# Ver usuarios
python3 fetch.py users

# Ver features del producto
python3 fetch.py features

# Guardar en archivo
python3 fetch.py events > events.json
```

---

## Usando counter.py

```bash
# Contar eventos por feature
python3 fetch.py events | python3 counter.py feature

# Contar eventos por usuario
python3 fetch.py events | python3 counter.py user_id

# Contar eventos por tipo
python3 fetch.py events | python3 counter.py event_type

# Contar usuarios por plan
python3 fetch.py users | python3 counter.py plan

# Contar usuarios por empresa
python3 fetch.py users | python3 counter.py company
```

---

## Guardar resultados intermedios

```bash
# Guardar conteos en archivo
python3 fetch.py events | python3 counter.py feature > counts.json

# Ver el archivo
cat counts.json
```

---

## Estructura de los datos

### /api/events
```json
{
  "id": "evt_0001",
  "user_id": "usr_001",
  "event_type": "click",
  "feature": "dashboard",
  "timestamp": "2025-11-26T10:30:00Z"
}
```

### /api/users
```json
{
  "id": "usr_001",
  "name": "Ana García",
  "email": "ana@startup.io",
  "plan": "pro",
  "signup_date": "2024-01-15",
  "company": "StartupCo"
}
```

### /api/features
```json
{
  "id": "feat_dashboard",
  "name": "dashboard",
  "status": "stable",
  "release_date": "2023-06-01",
  "team": "frontend"
}
```

---

## Comandos útiles de terminal

```bash
# Ver solo las primeras líneas
python3 fetch.py events | head -20

# Contar líneas
python3 fetch.py events | wc -l

# Buscar texto en el output
python3 fetch.py events | grep "dashboard"
```

---

## Tip de debugging

Si un pipe no funciona, ejecuta cada parte por separado:

```bash
# Paso 1: ¿fetch funciona?
python3 fetch.py events

# Paso 2: ¿counter recibe bien los datos?
python3 fetch.py events | python3 counter.py feature
```
