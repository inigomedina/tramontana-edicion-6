# Sesión 3: Catedrales y Bazares

## Introducción

Esta sesión explora cómo se construyen sistemas complejos a través de piezas 
simples y composables. Vamos a experimentar con la **filosofía UNIX** y el 
**diseño modular** para entender cómo estas ideas transforman nuestra forma de 
pensar producto.

---

## Parte 1: Terminal y composición

### Objetivo
Experimentar con la composición de comandos simples en la terminal para entender 
cómo la filosofía UNIX funciona en la práctica.

---

### Ejercicio 1.1: Tu primer pipe

**Concepto:** El pipe `|` conecta la salida de un comando con la entrada del 
siguiente.

```bash
# Listar archivos y contar cuántos hay
ls | wc -l
```

**Explicación:**
- `ls` lista los archivos → produce texto
- `|` pasa ese texto al siguiente comando
- `wc -l` cuenta las líneas → produce un número

**Observa:**
- Dos programas simples
- Cada uno hace una cosa
- Combinados, resuelven un problema nuevo

**Ejercicio adicional:**
```bash
# Listar archivos, buscar los .md, contarlos
ls .. | grep ".md" | wc -l
```

---

### Ejercicio 1.2: Crear y transformar datos

Vamos a crear un archivo de datos y transformarlo.

```bash
# Crear un archivo con nombres de divinidades griegas
cat > gods.txt << EOF
Zeus
Poseidon
Hades
Atenea
Apolo
Artemisa
Afrodita
Ares
Hefesto
Hermes
Artemisa
Dionisio
Demeter
Hera
Zeus
Apolo
Atenea
Poseidon
Afrodita
Artemisa
Hermes
Apolo
Atenea
Artemisa
Artemisa
Hades
Apolo
Zeus
Afrodita
Atenea
Hermes
Poseidon
Artemisa
Apolo
Dionisio
Atenea
Artemisa
Hefesto
Ares
Apolo
Artemisa
Atenea
Afrodita
Hermes
Poseidon
Artemisa
Apolo
Artemisa
Demeter
Hera
EOF
```

**Ahora experimenta:**

```bash
# Ver el contenido
cat gods.txt

# Ordenar alfabéticamente
cat gods.txt | sort

# Ordenar y eliminar duplicados
cat gods.txt | sort | uniq

# Contar cuántas veces aparece cada producto
cat gods.txt | sort | uniq -c

# Ordenar por frecuencia (más populares primero)
cat gods.txt | sort | uniq -c | sort -rn
```

**Reflexión:**
- ¿Cuántos comandos usaste?
- ¿Cuántos "programas" diferentes?
- ¿Cómo se combinaron?
- ¿Podrías hacer esto con una aplicación monolítica?

---

### Ejercicio 1.3: Buscar y filtrar

Vamos a trabajar con el archivo `index-dom.html` que ya tienes en el repo.

```bash
# Ver cuántas líneas tiene
wc -l ../index-dom.html

# Buscar todas las líneas que contienen "class"
grep "class" ../index-dom.html

# Contar cuántas veces aparece "class"
grep "class" ../index-dom.html | wc -l

# Ver solo las primeras 5 ocurrencias
grep "class" ../index-dom.html | head -5

# Buscar "class" y mostrar el nombre de cada clase
grep -o 'class="[^"]*"' ../index-dom.html

# Contar cuántas clases CSS únicas hay
grep -o 'class="[^"]*"' ../index-dom.html | sort | uniq | wc -l
```

**Observa:**
- Cada comando hace una transformación simple
- El resultado de uno alimenta al siguiente
- Puedes "debuggear" quitando comandos del final del pipe

---

### Ejercicio 1.4: JSON y APIs desde terminal

Tu ordenador incluye herramientas para trabajar con JSON. Vamos a hacer una 
petición HTTP y procesarla.

```bash
# Hacer una petición a una API pública
curl -s "https://api.github.com/users/github"

# Extraer solo el nombre (requiere jq, si no lo tienes: brew install jq)
curl -s "https://api.github.com/users/github" | jq '.name'

# Extraer múltiples campos
curl -s "https://api.github.com/users/github" | jq '{name: .name, repos: .public_repos, followers: .followers}'
```

**Si no tienes `jq` instalado:**
```bash
# Alternativa con grep (menos elegante pero funciona)
curl -s "https://api.github.com/users/github" | grep '"name"'
```

---

### Ejercicio 1.5: Construye tu propio pipeline

**Reto:** Crea un pipeline que:
1. Liste todos los archivos `.md` del directorio padre
2. Busque los que contienen la palabra "ejercicio"
3. Cuente cuántos son

**Solución:**
```bash
ls ../*.md | xargs grep -l "ejercicio" | wc -l
```

**Reto avanzado:**
Crea un comando que extraiga todos los títulos (líneas que empiezan con `#`) 
del archivo `index-dom.md` y los enumere.

**Pista:**
```bash
grep "^#" ../index-dom.md | nl
```

---

### Reflexión

**Preguntas para discutir:**

1. ¿Qué tienen en común todos estos comandos?
   - Hacen una cosa
   - Leen input, producen output
   - Se pueden combinar

2. ¿Qué pasaría si cada tarea requiriera una aplicación diferente?
   - No podríamos componerlas
   - Tendríamos que copiar/pegar datos manualmente
   - Perderíamos la capacidad de automatizar

3. ¿Cómo se relaciona esto con diseño de producto?
   - APIs como "comandos"
   - Webhooks como "pipes"
   - Cada feature como un módulo componible

---

## Apéndice: Comandos útiles de terminal

### Navegación
```bash
pwd                 # Dónde estoy
ls                  # Listar archivos
ls -la              # Listar con detalles
cd directorio       # Cambiar de directorio
cd ..               # Subir un nivel
cd ~                # Ir a home
```

### Archivos
```bash
cat archivo.txt     # Ver contenido
head archivo.txt    # Primeras 10 líneas
tail archivo.txt    # Últimas 10 líneas
wc -l archivo.txt   # Contar líneas
```

### Búsqueda
```bash
grep "texto" archivo.txt           # Buscar texto
grep -i "texto" archivo.txt        # Case insensitive
grep -r "texto" directorio/        # Buscar en directorio
```

### Transformación
```bash
sort archivo.txt                   # Ordenar
uniq archivo.txt                   # Eliminar duplicados
uniq -c archivo.txt                # Contar duplicados
```

### Pipes
```bash
comando1 | comando2                # Conectar salida con entrada
comando > archivo.txt              # Guardar salida en archivo
comando >> archivo.txt             # Añadir al archivo
comando < archivo.txt              # Leer entrada de archivo
```

### HTTP
```bash
curl http://example.com            # GET request
curl -X POST http://example.com    # POST request
curl -s http://example.com         # Silent (sin progress)
```

### JSON
```bash
cat data.json | jq .               # Pretty print
cat data.json | jq '.name'         # Extraer campo
cat data.json | jq '.[] | .name'   # Extraer de array
```
