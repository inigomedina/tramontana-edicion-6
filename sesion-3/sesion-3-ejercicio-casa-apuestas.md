# Ejercicio para casa: Diseño de entidades

## Contexto

Vais a diseñar el modelo de datos para una casa de apuestas deportivas simplificada.
**Antes de escribir código**, necesitáis pensar bien qué entidades existen y cómo
se relacionan.

Un buen diseño hará que el código sea fácil de escribir. Un mal diseño os hará
sufrir.

---

## El problema

Una casa de apuestas necesita gestionar:

- **Usuarios** que se registran y tienen un saldo
- **Eventos deportivos** (partidos) sobre los que se puede apostar
- **Apuestas** que hacen los usuarios sobre los eventos
- Los **resultados** de los eventos cuando terminan

### Ejemplos de uso

> Ana apuesta 10€ a que el Rayo Vallecano gana contra el Real Madrid. La cuota es 2.5.
> Si acierta, gana 25€ (10 × 2.5). Si falla, pierde los 10€.

> Carlos apuesta 5€ al empate en el mismo partido. La cuota es 3.0.

> El partido termina 2-1. Ana gana, Carlos pierde.

---

## Parte 1: Diseño del modelo

Antes de escribir nada, responded estas preguntas en un documento o papel:

### 1.1 Identificar las "cosas"

Leed el problema otra vez. ¿Qué **sustantivos** aparecen?

Haced una lista de todo lo que podría ser una entidad:
```
- User
- Event
- Bet
- ...¿qué más?
```

### 1.2 Separar entidades de propiedades

No todo lo que parece importante es una entidad. Algunas cosas son **propiedades**
de otras.

Para cada elemento de vuestra lista, preguntaos:
- ¿Tiene identidad propia? (¿necesita un ID?)
- ¿Puede existir sin otra cosa?
- ¿Vamos a querer listarlo, buscarlo, o referenciarlo desde otro sitio?

**Pregunta clave:** "Fútbol", "Baloncesto"... ¿son entidades o propiedades?

Argumentad vuestra decisión:
```
"Fútbol" es una _________ porque _________________________________
```

### 1.3 Definir las propiedades de cada entidad

Para cada entidad que hayáis identificado, listad sus propiedades:

```
User:
  - id
  - name
  - ...¿qué más necesitáis?

Event:
  - id
  - ...
```

### 1.4 Identificar las relaciones

¿Cómo se conectan las entidades entre sí?

- Un usuario puede hacer muchas apuestas → User 1:N Bet
- Una apuesta es sobre un evento → Bet N:1 Event
- ...¿qué más?

Dibujad un diagrama simple (cajas y flechas) o escribidlo:
```
User ──1:N──> Bet ──N:1──> Event
```

### 1.5 Decisiones de diseño

Responded estas preguntas (no hay respuesta única correcta, pero debéis argumentar):

**Pregunta A:** ¿Dónde guardáis la cuota de una apuesta?
- Opción 1: En el Event (home_odds, draw_odds, away_odds)
- Opción 2: En la Bet (la cuota que tenía cuando se hizo)
- Opción 3: En una entidad separada Market u Odds

¿Qué pasa si la cuota cambia después de que alguien apueste? ¿Afecta a vuestra decisión?

**Pregunta B:** ¿El resultado del partido es una entidad o propiedades del Event?
- Opción 1: Añadimos campos al Event (home_score, away_score, status)
- Opción 2: Creamos una entidad Result separada

¿Qué pasa si queréis guardar histórico de resultados? ¿Y si un partido se suspende?

**Pregunta C:** ¿Cómo representáis el tipo de apuesta (victoria local, empate, victoria visitante)?
- Opción 1: Un campo de texto libre ("Real Madrid wins")
- Opción 2: Un código fijo ("1", "X", "2")
- Opción 3: Una entidad BetType o Market

---

## Parte 2: Implementar el modelo

Una vez tengáis claro vuestro diseño, implementadlo:

### 2.1 Crear los archivos JSON

Cread archivos con datos de ejemplo para cada entidad:

```
my-model/
├── users.json
├── events.json
├── bets.json
└── ...otros si los necesitáis
```

Incluid al menos:
- 3-5 usuarios
- 4-6 eventos (algunos pendientes, algunos terminados)
- 8-10 apuestas de diferentes usuarios sobre diferentes eventos

### 2.2 Verificar las relaciones

Comprobad que vuestros datos son coherentes:
- Toda apuesta referencia un usuario que existe
- Toda apuesta referencia un evento que existe
- Los IDs son únicos dentro de cada entidad

---

## Parte 3: Crear la API

Ahora escribid un servidor (como el `api/server.py` que usamos en clase) que sirva
vuestros datos.

### Endpoints mínimos

```
GET /api/users          → Lista de usuarios
GET /api/events         → Lista de eventos
GET /api/bets           → Lista de apuestas
```

### Endpoints que demuestran vuestro diseño

Estos endpoints requieren que vuestro modelo esté bien pensado:

```
GET /api/users/:id/bets     → Apuestas de un usuario específico
GET /api/events/:id/bets    → Apuestas sobre un evento específico
GET /api/events/open        → Eventos sobre los que aún se puede apostar
```

**Pista:** Si estos endpoints son difíciles de implementar, quizás vuestro modelo
necesita ajustes.

### Punto de partida

Podéis copiar `api/server.py` y adaptarlo, o empezar desde cero.
El servidor debe:
- Leer vuestros archivos JSON al arrancar
- Servir los endpoints con los datos
- Devolver JSON válido

---

## Entregable

1. **Documento de diseño** con vuestras respuestas a la Parte 1
2. **Archivos JSON** con vuestro modelo de datos
3. **Servidor API** funcionando
4. **Prueba** de que los endpoints funcionan (capturas de curl o similar)

---

## Criterios de un buen diseño

Vuestro diseño es bueno si:

✅ **Añadir un deporte nuevo** (tenis, F1...) no requiere cambiar código, solo datos

✅ **Saber cuánto ha ganado/perdido un usuario** se puede calcular con los datos que tenéis

✅ **No hay datos duplicados** — si cambio el nombre de un usuario, solo lo cambio en un sitio

✅ **Las relaciones son claras** — puedo navegar de User a sus Bets a sus Events

---

## Reflexión final

Cuando terminéis, responded:

1. ¿Qué decisión de diseño os costó más tomar? ¿Por qué?

2. Si tuvierais que añadir "apuestas combinadas" (apostar a varios resultados a la vez),
   ¿vuestro modelo lo soporta o tendríais que cambiarlo?

3. ¿Qué haríais diferente si empezarais de nuevo?
