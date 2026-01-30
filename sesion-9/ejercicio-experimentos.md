# Ejercicio: Autopsia de un experimento

## El caso

Trabajas como PM en Duolingo. Tu equipo ha estado probando una nueva funcionalidad llamada **"Streak Rescue"** durante las últimas 4 semanas.

### ¿En qué consiste?

Cuando un usuario está a punto de perder su racha (no ha completado ninguna lección y son las 22:00 en su zona horaria), recibe una notificación push especial. Esta notificación le ofrece hacer una "micro-lección" de 30 segundos que cuenta para mantener la racha.

### ¿Por qué se propuso?

El equipo de Growth tenía una hipótesis clara: muchos usuarios abandonan Duolingo después de perder su racha. La racha es un mecanismo de retención muy potente, pero también es frágil: basta un día malo para perderla. Si conseguimos que menos usuarios rompan su racha, deberíamos ver una mejora en la retención.

### ¿Cómo se probó?

Se diseñó un experimento A/B con dos grupos:
- **Grupo de control (A)**: 50,000 usuarios que siguen con la experiencia normal
- **Grupo de tratamiento (B)**: 50,000 usuarios que reciben la nueva funcionalidad Streak Rescue

El experimento duró 4 semanas. Ahora tienes los datos y debes decidir: ¿lanzamos esto a todos los usuarios o no?

---

## Conceptos que necesitas manejar

Antes de mirar los datos, vamos a asegurarnos de que hablamos el mismo idioma.

### Grupo de control y grupo de tratamiento

En un experimento, dividimos a los usuarios en dos grupos:

- **Grupo de control**: No recibe ningún cambio. Es nuestra referencia, nuestro "así estaban las cosas antes".
- **Grupo de tratamiento**: Recibe el cambio que queremos probar.

Comparamos lo que pasa en ambos grupos. Si hay una diferencia significativa, podemos atribuirla al cambio que introdujimos.

La lógica es sencilla: si ambos grupos son iguales en todo excepto en el cambio que estamos probando, cualquier diferencia en los resultados debería venir de ese cambio.

### Aleatorización: por qué es importante

Para que la comparación sea justa, los usuarios deben asignarse a cada grupo **al azar**. Si no lo hacemos así, podríamos estar comparando grupos que ya eran diferentes de partida.

Por ejemplo, si asignamos al grupo de tratamiento solo a usuarios muy activos, y al grupo de control a usuarios menos activos, cualquier mejora que veamos podría deberse a que ya teníamos a los "mejores" usuarios en un grupo, no a que la funcionalidad funcione.

La aleatorización busca que ambos grupos sean estadísticamente equivalentes antes de empezar: misma distribución de edad de cuenta, mismo nivel de actividad previa, misma mezcla de países, etc.

### El p-value: qué significa (sin fórmulas)

Cuando comparas los resultados de dos grupos, siempre habrá alguna diferencia. La pregunta es: ¿esa diferencia es real o es ruido?

Imagina que lanzas una moneda 10 veces y salen 6 caras. ¿Está trucada? Probablemente no, eso puede pasar por azar. Pero si lanzas 1,000 veces y salen 600 caras, algo raro está pasando.

El **p-value** te dice: "Si no hubiera ninguna diferencia real entre los grupos, ¿qué probabilidad hay de que observara una diferencia tan grande (o mayor) solo por azar?"

- **p-value bajo (< 0.05)**: Es poco probable que la diferencia sea solo ruido. Decimos que el resultado es "estadísticamente significativo".
- **p-value alto (> 0.05)**: La diferencia que ves podría ser perfectamente explicable por el azar. No puedes descartar que no haya efecto real.

**Cuidado**: Un p-value de 0.05 no significa que haya un 95% de probabilidad de que la funcionalidad funcione. Significa que, si la funcionalidad NO hiciera nada, solo un 5% de las veces veríamos una diferencia tan grande por casualidad.

### El umbral de 0.05: una convención, no una ley física

El umbral de p < 0.05 es una convención heredada de la estadística del siglo XX. No tiene nada de mágico. Un resultado con p = 0.049 no es fundamentalmente distinto de uno con p = 0.051.

En la práctica, te encontrarás con situaciones ambiguas. Un p-value de 0.08 no te dice "no hay efecto", te dice "no tenemos suficiente evidencia para estar seguros". Son cosas distintas.

### Contaminación entre grupos

Uno de los mayores riesgos en un experimento es que los grupos se "contaminen" entre sí.

Ejemplos de contaminación:
- **Contaminación social**: Un usuario del grupo de control ve la nueva funcionalidad en el móvil de su amigo (que está en el grupo de tratamiento) y cambia su comportamiento.
- **Contaminación técnica**: Por un bug, algunos usuarios del grupo de control reciben ocasionalmente la funcionalidad del grupo de tratamiento.
- **Contaminación por cuentas múltiples**: Un usuario tiene dos cuentas, una en cada grupo.

La contaminación suele **diluir** el efecto: hace que los grupos se parezcan más entre sí, lo que dificulta detectar diferencias reales. Si aun así ves un efecto, probablemente el efecto real sea mayor. Pero si no ves efecto, no sabes si es porque no lo hay o porque la contaminación lo ha ocultado.

**Pregunta que debes hacerte**: ¿Cómo puedo estar seguro de que no ha habido contaminación en este experimento?

### Efecto novelty: el espejismo del principio

Cuando introduces algo nuevo, los usuarios pueden reaccionar simplemente porque es nuevo, no porque sea mejor.

En el caso de Streak Rescue: quizás los usuarios responden bien las primeras semanas porque la notificación es novedosa y les llama la atención. Pero después de un mes, podrían empezar a ignorarla.

Esto significa que un experimento de 4 semanas podría sobreestimar el efecto real a largo plazo.

**Pregunta que debes hacerte**: ¿El efecto que veo se mantiene en el tiempo o decae?

### Métricas primarias y secundarias

En cualquier experimento debes definir de antemano qué métrica es la más importante (primaria) y cuáles son complementarias (secundarias).

- **Métrica primaria**: La que usarás para tomar la decisión. En nuestro caso: retención a 14 días (D14 retention).
- **Métricas secundarias**: Otras que te ayudan a entender el contexto. En nuestro caso: lecciones completadas por semana, tiempo en la app, etc.

¿Por qué importa esta distinción? Porque si miras muchas métricas, por puro azar algunas mostrarán diferencias significativas. Si decides después de ver los datos cuál es "la importante", puedes engañarte a ti mismo.

### Segmentación: el efecto puede no ser igual para todos

Un error común es mirar solo el promedio general. El efecto de una funcionalidad puede ser muy distinto según el segmento:

- Usuarios nuevos vs. veteranos
- Usuarios de pago vs. usuarios gratuitos
- Usuarios de un país vs. otro

Esto es un arma de doble filo:
- Por un lado, te permite descubrir para quién funciona y para quién no.
- Por otro lado, si buscas en suficientes segmentos, encontrarás alguno donde "funciona" solo por azar.

La regla sana es: define de antemano qué segmentos vas a mirar y por qué. No hagas "fishing" de segmentos después de ver los datos.

---

## Ahora sí: los datos

Con estos conceptos claros, estás en posición de analizar los resultados del experimento.

En esta carpeta encontrarás el dataset `streak_rescue_experiment.csv` con los datos de los 100,000 usuarios del experimento.

---

## Preguntas

### Parte A: Comprensión

1. ¿Cuál es la diferencia en retención a 14 días entre el grupo de control y el grupo de tratamiento? ¿Es estadísticamente significativa?

2. ¿Qué pasa con las métricas secundarias (lecciones completadas, tiempo en app)? ¿Cuentan la misma historia que la métrica primaria?

3. ¿El efecto es igual para todos los usuarios o hay diferencias por segmento?

### Parte B: Juicio

4. Con los datos que tienes, ¿lanzarías Streak Rescue a todos los usuarios? Justifica tu respuesta.

5. Si tu respuesta no es un "sí" rotundo ni un "no" rotundo, ¿qué información adicional necesitarías para decidir?

### Parte C: Profundización

6. ¿Qué podría haber salido mal en este experimento? Identifica al menos dos posibles problemas metodológicos.

7. Si decidieras no lanzar la funcionalidad, ¿cómo se lo explicarías al equipo que la desarrolló durante 3 meses?

8. ¿Crees que este experimento se podría haber hecho de otra forma? ¿Qué cambiarías en el diseño?
