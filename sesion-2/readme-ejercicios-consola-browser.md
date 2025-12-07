# Ejercicios de consola en el browser

La idea es coger familiaridad con el browser como sistema. En el camino, también
habituarnos a control de versiones sobre el código (Git), por lo tanto a
colaboración, y a las estructuras más habituales de datos junto con sus
operaciones.

## Objetivos

- Trabajar con repositorios Git (clonar, navegar)
- Usar la consola del navegador
- Manipular el DOM para entender cómo funcionan las aplicaciones web
- Analizar y transformar datos con JavaScript
- Trabajar con localStorage y sessionStorage
- Aplicar estos conocimientos en herramientas reales como Notion

## Configuración inicial

### 1. Clonar el repositorio

Abre tu terminal y ejecuta:

```bash
git clone [URL_DEL_REPOSITORIO]
cd ejercicios-consola-browser
```

Si no quieres trabajar con terminal, considera editores como Cursor, que ya
traen incorporadas las capacidades de IA y te pueden asistir muy bien.

En mi caso particular, uso Claude Code directamente en terminal.

### 2. Abrir el archivo HTML

Desde tu navegador abre el fichero index-dom.html.

### 3. Abrir la consola del navegador

Una vez abierto el archivo HTML en el navegador, abre la consola: inspect, F12,
etc.

## Ruta de aprendizaje

### Entender el DOM
📄 Archivo: `index-dom.md`

Ejercicios para practicar con el dashboard local (`index-dom.html`). 

Aquí aprenderás:

- Navegación y selección de elementos del DOM
- Manipulación de contenido y estilos
- Extracción y transformación de datos
- Trabajo con localStorage/sessionStorage

### Programar sobre Notion
📄 Archivo: `programming-notion.md`

Una vez domines los ejercicios básicos, mira si te animas a seguir
experimentando con un producto real.

- Explorar la estructura de Notion
- Extraer información de tu workspace
- Analizar el uso de la aplicación
- Experimentos avanzados

## Consejos para aprovechar al máximo los ejercicios

### 1. La consola es tu amiga
La consola del navegador es una de las herramientas más poderosas para entender
cómo funcionan los productos digitales.

- Te ayuda a entender limitaciones técnicas
- Puedes hacer prototipos rápidos
- Puedes investigar cómo funcionan otras aplicaciones
- Es útil para QA y reporting de bugs

### 2. No tengas miedo de experimentar
Todos los cambios que hagas en la consola son temporales. Si algo sale mal:
- Refresca la página
- Todo volverá a su estado inicial | homeostasis técnica ;)

### 3. Usa la función de autocompletado
Cuando escribas en la consola:
- Presiona `Tab` para autocompletar
- Escribe algo como `document.` y presiona `Tab` para ver opciones
- Usa las flechas arriba/abajo para ver el historial de comandos

### 4. Copia y prueba
Puedes copiar código JavaScript de cualquier lugar y ejecutarlo en la consola
para ver qué hace.

### 5. Documenta lo que descubres
Cada persona tiene un directorio con su nombre. Guarda allí todo lo que
consideres interesante. Te ayudará a aprender a cómo contribuir con Git.

## Recursos útiles

### Documentación oficial
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
- [Firefox Developer Tools](https://developer.mozilla.org/es/docs/Tools)
- [MDN Web Docs - Consola](https://developer.mozilla.org/es/docs/Web/API/Console)

### Conceptos clave
- **DOM (Document Object Model)**: Representación en árbol de la estructura HTML
- **Selector CSS**: Patrón para seleccionar elementos (ej: `.clase`, `#id`, `div`)
- **localStorage**: Almacenamiento persistente en el navegador
- **sessionStorage**: Almacenamiento temporal durante la sesión
