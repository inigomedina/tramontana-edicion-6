## Parte 2: API y construcción modular

### Objetivo
Construir un sistema modular que consuma una API, transforme datos y produzca 
un resultado útil. Cada pareja creará su propia solución.

---

### 2.1 La API: Sistema de métricas de producto

He preparado una API simple en el repositorio que simula un sistema tonto de 
métricas de producto.

**Endpoints disponibles:**

```
GET /api/events
→ Devuelve eventos de usuario (clicks, pageviews, etc.)

GET /api/users
→ Devuelve información de usuarios

GET /api/features
→ Devuelve lista de features del producto y su estado
```

**Formato de datos:**

```json
// GET /api/events
[
  {
    "id": "evt_001",
    "user_id": "usr_123",
    "event_type": "click",
    "feature": "checkout",
    "timestamp": "2024-11-25T10:30:00Z"
  },
  ...
]

// GET /api/users
[
  {
    "id": "usr_123",
    "name": "Ana García",
    "plan": "pro",
    "signup_date": "2024-01-15"
  },
  ...
]

// GET /api/features
[
  {
    "name": "checkout",
    "status": "stable",
    "release_date": "2024-01-01"
  },
  ...
]
```

---

### 2.2 Arrancar la API localmente

**En una terminal:**

```bash
# Navega al directorio del repo
cd tramontana-edicion-6

# Arranca el servidor (Python 3)
python3 api/server.py
```

**Deberías ver:**
```
API de métricas corriendo en http://localhost:3000
Endpoints disponibles:
  - GET /api/events
  - GET /api/users
  - GET /api/features
```

**Prueba que funciona:**

En otra terminal o en tu navegador:
```bash
curl http://localhost:3000/api/events
```

---

### 2.3 Ejercicio principal: Construye un sistema modular

**Contexto:**
Necesitas analizar el uso de las features. Tienes acceso a la API pero 
necesitas construir herramientas para:
- Analizar qué features se usan más
- Identificar usuarios power users
- Detectar features poco utilizadas
- Generar reportes para el equipo

**Restricción importante:**
No puedes crear una aplicación monolítica. Debes construir **módulos 
independientes** que se puedan componer.

---

### 2.4 Módulos: lo que os doy vs lo que construís

Trabajáis por parejas. Os doy **dos módulos funcionando**:
- `fetch.py` — obtiene datos de la API
- `counter.py` — cuenta ocurrencias por campo

Vuestro trabajo es **implementar al menos 2-3 módulos más** de los que se describen
abajo para poder resolver vuestro reto. Los ejemplos son orientativos, no código
que podáis copiar directamente.

#### Módulo 1: Fetcher ✅ OS LO DAMOS
**Propósito:** Obtener datos de la API

**Interfaz:**
- Input: nombre del recurso (`events`, `users`, `features`)
- Output: JSON a stdout

**Uso:**
```bash
python3 fetch.py events                  # ver en pantalla
python3 fetch.py events > events.json    # guardar en archivo
python3 fetch.py users | python3 counter.py plan   # encadenar
```

---

#### Módulo 2: Filter 🔨 LO CONSTRUÍS
**Propósito:** Filtrar datos por un campo y valor

**Interfaz:**
- Input: JSON array desde stdin
- Output: JSON array filtrado a stdout

**Pistas:**
- `json.load(sys.stdin)` para leer JSON de stdin
- `sys.argv[1]` y `sys.argv[2]` para los argumentos
- List comprehension para filtrar: `[x for x in data if ...]`
- `json.dumps(resultado, indent=2)` para imprimir

**Uso esperado:**
```bash
python3 fetch.py events | python3 filter.py feature dashboard
python3 fetch.py users | python3 filter.py plan pro
```

---

#### Módulo 3: Counter ✅ OS LO DAMOS
**Propósito:** Contar ocurrencias por un campo

**Interfaz:**
- Input: JSON array desde stdin
- Output: JSON objeto con conteos `{valor: cantidad}`

**Uso:**
```bash
python3 fetch.py events | python3 counter.py feature
python3 fetch.py events | python3 counter.py user_id
python3 fetch.py users | python3 counter.py plan
```

---

#### Módulo 4: Top N 🔨 LO CONSTRUÍS
**Propósito:** Extraer los N elementos con mayor conteo

**Interfaz:**
- Input: JSON objeto con conteos desde stdin
- Output: JSON objeto con solo los top N

**Pistas:**
- `dict.items()` devuelve pares (clave, valor)
- `sorted(..., key=lambda x: x[1], reverse=True)` ordena por valor descendente
- Slicing `[:n]` para tomar los primeros N
- Devuelve JSON, no texto, para poder encadenar

**Uso esperado:**
```bash
python3 fetch.py events | python3 counter.py feature | python3 topn.py 5
```

---

#### Módulo 5: Joiner 🔨 LO CONSTRUÍS
**Propósito:** Unir datos de eventos con datos de usuarios (como un JOIN en SQL)

**Interfaz:**
- Input: dos archivos JSON como argumentos
- Output: eventos enriquecidos con info del usuario a stdout

**Pistas:**
- Lee archivos con `open()` y `json.load()`
- Crea un diccionario de lookup: `{user_id: user_data}`
- Recorre eventos y añade campos del usuario
- El campo `user_id` en eventos conecta con `id` en users

**Uso esperado:**
```bash
# Primero guardas los datos
python3 fetch.py events > events.json
python3 fetch.py users > users.json

# Luego haces el join
python3 join.py events.json users.json
```

---

#### Módulo 6: Reporter 🔨 LO CONSTRUÍS
**Propósito:** Generar un reporte legible en markdown

**Interfaz:**
- Input: JSON objeto con conteos desde stdin
- Output: texto Markdown a stdout

**Pistas:**
- `datetime.now().strftime('%Y-%m-%d %H:%M')` para la fecha
- `dict.items()` para iterar sobre los datos
- Usa `print()` para generar el markdown línea a línea
- Puedes calcular porcentajes con `count / total * 100`

**Uso esperado:**
```bash
python3 fetch.py events | python3 counter.py feature | python3 report.py "Top Features"
```

---

### 2.5 Cómo probar mientras desarrolláis

Con los módulos que os doy, ya podéis hacer cosas:

```bash
# Ver eventos
python3 fetch.py events

# Contar por feature
python3 fetch.py events | python3 counter.py feature

# Contar usuarios por plan
python3 fetch.py users | python3 counter.py plan
```

Cuando implementéis vuestros módulos, podréis encadenarlos:

```bash
# Ejemplo: top 5 features (cuando tengáis por ejemplo topn.py)
python3 fetch.py events | python3 counter.py feature | python3 topn.py 5

# Ejemplo: generar reporte (cuando tengáis por ejemplo report.py)
python3 fetch.py events | python3 counter.py feature | python3 report.py "Features"
```

**Tip para debuggear:** Ejecutad cada parte del pipe por separado para ver qué produce.

---

### 2.6 Retos para cada pareja

Elegid **uno de estos retos**. Cada uno requiere implementar módulos diferentes.

#### Reto A: Power Users
Identifica los 5 usuarios que más interactúan con el producto.

**Ya tenéis:** fetch.py, counter.py
**Tendréis que construir:** topn.py, join.py, report.py (o adaptación)

**Output esperado:** Un reporte que muestre los top 5 usuarios con su nombre, plan y número de eventos.

---

#### Reto B: Feature Health
Identifica features con poco uso que podrían necesitar mejora o deprecarse.

**Ya tenéis:** fetch.py, counter.py
**Tendréis que construir:** filter.py (para separar por umbral), report.py

**Output esperado:** Un reporte que separe features "sanas" (muchos eventos) de features "en riesgo" (pocos eventos).

---

#### Reto C: User Segmentation
Analiza el comportamiento por tipo de plan (free vs pro vs enterprise).

**Ya tenéis:** fetch.py, counter.py
**Tendréis que construir:** join.py, filter.py, report.py (o un módulo de agregación)

**Output esperado:** Un reporte que compare el uso entre usuarios de cada plan.

---

### 2.7 Entregable

Cada pareja debe entregar:

1. **Los módulos que habéis implementado** (archivos .py)
2. **El pipeline completo** — los comandos que resuelven vuestro reto
3. **El output generado** — el reporte o resultado final

---

### 2.8 Tips de implementación

1. **Empieza simple:** Haz un módulo, pruébalo, luego haz el siguiente
2. **Usa archivos intermedios:** Guarda outputs con `> archivo.json` para inspeccionar
3. **Prueba cada módulo aisladamente:** `cat test.json | python3 tumodulo.py`
4. **El orden importa:** fetch → filter/counter → topn → report
5. **Si algo falla:** Ejecuta cada parte del pipe por separado

---

## Parte 3: Puesta en común

### Formato

Cada pareja presenta:

1. **Qué reto eligieron**
2. **Qué módulos construyeron**
   - Mostrar uno en detalle
   - Explicar su interfaz (input/output)
3. **Cómo los compusieron**
   - Mostrar el pipeline final
4. **Qué aprendieron**
   - ¿Qué fue difícil?
   - ¿Qué ventajas vieron en el enfoque modular?
   - ¿Qué harían diferente?

### Preguntas para la reflexión grupal

1. **Modularidad:**
   - ¿Qué hace que un módulo sea "bueno"?
   - ¿Cuándo es demasiado pequeño? ¿Demasiado grande?

2. **Interfaces:**
   - ¿Qué tipos de interfaces vimos? (JSON, texto, archivos)
   - ¿Cuál es más flexible? ¿Más fácil de debuggear?

3. **Composición:**
   - ¿Cuál es la ventaja de poder reutilizar módulos?
   - ¿Cómo cambia esto la forma de trabajar?

4. **Producto:**
   - ¿Cómo se relaciona esto con features de producto?
   - ¿Cómo podríamos aplicar estos principios al diseñar APIs?
   - ¿Qué implica para equipos y arquitectura?
