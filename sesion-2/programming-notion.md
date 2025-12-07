# Ejercicios con Notion

## Antes de empezar

### Preparación
1. Completa primero los ejercicios básicos con `index.html`
2. Abre [Notion](https://notion.so) en tu navegador
3. Inicia sesión en tu cuenta (o crea una gratuita)
4. Ten al menos una página con algo de contenido
5. Abre la consola del navegador (F12 o Cmd+Option+J)

---

## Índice

1. [Exploración inicial de Notion](#1-exploración-inicial-de-notion)
2. [Estructura del DOM en Notion](#2-estructura-del-dom-en-notion)
3. [Extracción de contenido](#3-extracción-de-contenido)
4. [Análisis de tu workspace](#4-análisis-de-tu-workspace)
5. [Experimentos visuales](#5-experimentos-visuales)
6. [Análisis de uso personal](#6-análisis-de-uso-personal)
7. [Proyectos avanzados](#7-proyectos-avanzados)

---

## 1. Exploración inicial de Notion

### 1.1 Inspector de elementos

**Objetivo:** Aprender a usar el inspector para entender la estructura HTML.

**Contexto:** El inspector es tu mejor amigo para entender cómo están construidas 
las aplicaciones web.

**Ejercicio:**
1. Haz click derecho en el título de tu página de Notion
2. Selecciona "Inspeccionar"
3. Observa cómo se ilumina el elemento en el código HTML
4. Mira los estilos CSS aplicados en el panel derecho

**¿Qué observas?**
- Notion usa muchos `<div>` con clases CSS específicas
- Cada bloque de contenido es un elemento separado
- Los estilos son dinámicos y complejos

---

### 1.2 Identificar la aplicación

**Objetivo:** Entender la tecnología detrás de Notion.

**Ejercicio:**
```javascript
// View the page title
console.log('Title:', document.title);

// View the current URL
console.log('URL:', window.location.href);

// Look for clues about the framework used
console.log('Uses React?:', !!document.querySelector('[data-reactroot], [data-reactid]'));
```

---

### 1.3 Estructura global

**Objetivo:** Identificar las secciones principales de la interfaz.

**Ejercicio:**
```javascript
// Try to find main elements
// Note: Selectors may vary depending on Notion updates

// Look for the sidebar
const sidebar = document.querySelector('[class*="sidebar"]');
console.log('Sidebar found:', !!sidebar);

// Look for the main content area
const mainContent = document.querySelector('[class*="page"], main, [role="main"]');
console.log('Main content found:', !!mainContent);
```

**Nota:** Si estos selectores no funcionan, usa el inspector para encontrar las 
clases correctas actuales.

---

## 2. Estructura del DOM en Notion

### 2.1 Explorar bloques de contenido

**Objetivo:** Entender cómo Notion estructura el contenido en bloques.

**Contexto:** Notion está construido con una arquitectura de "bloques". 
Cada párrafo, título, imagen, etc. es un bloque independiente.

**Ejercicio:**
```javascript
// Find all blocks (the selector may vary)
// Try different selectors until you find the right one
const blocks = document.querySelectorAll('[data-block-id]');
console.log('Blocks found:', blocks.length);

// If the above doesn't work, try:
const blocks2 = document.querySelectorAll('[class*="block"]');
console.log('Blocks (method 2):', blocks2.length);
```

**Ejercicio de exploración:**
```javascript
// Examine the first block
const firstBlock = document.querySelector('[data-block-id]');
if (firstBlock) {
    console.log('First block:', firstBlock);
    console.log('Block ID:', firstBlock.dataset.blockId);
    console.log('Content:', firstBlock.textContent);
}
```

---

### 2.2 Tipos de bloques

**Objetivo:** Identificar diferentes tipos de contenido.

**Ejercicio:**
```javascript
// Create an inventory of block types on your page
function analyzeBlocks() {
    const blocks = document.querySelectorAll('[data-block-id]');

    console.log(`Total blocks: ${blocks.length}`);

    // Analyze each block
    blocks.forEach((block, index) => {
        console.log(`\n--- Block ${index + 1} ---`);
        console.log('ID:', block.dataset.blockId);
        console.log('Classes:', block.className);
        console.log('Element type:', block.tagName);
        console.log('Text:', block.textContent.substring(0, 50) + '...');
    });
}

// Execute
analyzeBlocks();
```

---

### 2.3 Encontrar selectores útiles

**Objetivo:** Desarrollar la habilidad de encontrar patrones en el DOM.

**Contexto:** Esta es una habilidad crucial para:
- Hacer QA efectivo
- Reportar bugs específicos
- Entender limitaciones técnicas
- Proponer mejoras realistas

**Ejercicio de exploración libre:**
```javascript
// Method to search for elements by visible text
function searchByText(text) {
    const elements = Array.from(document.querySelectorAll('*'));
    const results = elements.filter(el =>
        el.textContent.includes(text) &&
        el.children.length === 0 // Only "leaf" elements without children
    );
    console.log(`Found ${results.length} elements with "${text}"`);
    return results;
}

// Try it with some text from your page
searchByText('your text here');
```

---

## 3. Extracción de contenido

### 3.1 Extraer el título de la página

**Objetivo:** Obtener el título principal de tu página de Notion.

**Ejercicio:**
```javascript
// The title is usually in a specific element
// May require exploration with the inspector

// Method 1: By selector (adjust according to your Notion version)
const title = document.querySelector('h1, [placeholder*="Untitled"], [class*="title"]');
if (title) {
    console.log('Page title:', title.textContent);
}

// Method 2: Look for the largest element at the top
const largeElements = document.querySelectorAll('[style*="font-size"]');
// Explore the results manually
```

---

### 3.2 Extraer todo el texto de la página

**Objetivo:** Obtener un dump completo del contenido textual.

**Contexto:** Útil para:
- Contar palabras
- Hacer análisis de contenido
- Crear backups rápidos
- Buscar menciones de términos específicos

**Ejercicio:**
```javascript
// Function to extract all text
function extractFullContent() {
    // Find the main page container
    const container = document.querySelector('[class*="page-body"], main, [role="main"]');

    if (container) {
        const text = container.textContent;

        // Statistics
        const words = text.trim().split(/\s+/).length;
        const characters = text.length;
        const lines = text.split('\n').length;

        console.log('=== CONTENT ANALYSIS ===');
        console.log('Characters:', characters);
        console.log('Words:', words);
        console.log('Lines:', lines);
        console.log('\n--- Full content ---');
        console.log(text);

        return text;
    } else {
        console.log('Could not find the main container');
    }
}

// Execute
extractFullContent();
```

---

### 3.3 Extraer links

**Objetivo:** Obtener todos los enlaces de la página.

**Contexto:** Útil para:
- Auditorías de contenido
- Verificar enlaces rotos
- Mapear conexiones entre páginas
- Análisis de estructura de información

**Ejercicio:**
```javascript
// Extract all links
function extractLinks() {
    const links = document.querySelectorAll('a[href]');

    console.log(`=== LINKS FOUND: ${links.length} ===\n`);

    const linksData = [];

    links.forEach((link, index) => {
        const data = {
            text: link.textContent.trim(),
            url: link.href,
            isInternal: link.href.includes('notion.so'),
            isExternal: !link.href.includes('notion.so')
        };
        linksData.push(data);
    });

    // Group by type
    const internal = linksData.filter(l => l.isInternal);
    const external = linksData.filter(l => l.isExternal);

    console.log('Internal links (Notion):', internal.length);
    console.log('External links:', external.length);
    console.log('\nExternal links:');
    console.table(external);

    return linksData;
}

// Execute
extractLinks();
```

---

### 3.4 Extraer bases de datos / tablas

**Objetivo:** Si tienes una tabla o database en la página, extraer sus datos.

**Contexto:** Las bases de datos de Notion son muy populares. Poder extraer estos 
datos es muy útil para análisis.

**Ejercicio:**
```javascript
// Find tables
function extractTables() {
    // Notion uses specific structures for databases
    const tables = document.querySelectorAll('table, [class*="collection"], [class*="database"]');

    console.log(`Tables/Databases found: ${tables.length}`);

    if (tables.length > 0) {
        // Analyze the first table found
        const table = tables[0];

        // Try to extract headers
        const headers = table.querySelectorAll('th, [class*="header"]');
        console.log('Headers found:', headers.length);

        headers.forEach((header, i) => {
            console.log(`Column ${i + 1}:`, header.textContent);
        });

        // Try to extract rows
        const rows = table.querySelectorAll('tr, [class*="row"]');
        console.log('Rows found:', rows.length);
    } else {
        console.log('No tables found. Make sure you have a database or table on your page.');
    }
}

// Execute
extractTables();
```

---

## 4. Análisis de tu workspace

### 4.1 Inventario de páginas en sidebar

**Objetivo:** Contar cuántas páginas tienes en tu workspace.

**Ejercicio:**
```javascript
// Find items in the sidebar
function analyzeSidebar() {
    // Selectors may vary
    const items = document.querySelectorAll('[class*="sidebar"] a, [class*="tree"] [role="link"]');

    console.log(`=== WORKSPACE ANALYSIS ===`);
    console.log(`Total items in sidebar: ${items.length}`);

    // Extract names
    const names = [];
    items.forEach(item => {
        const name = item.textContent.trim();
        if (name && name.length > 0) {
            names.push(name);
        }
    });

    console.log('\nPages found:');
    names.forEach((name, i) => {
        console.log(`${i + 1}. ${name}`);
    });

    return names;
}

// Execute
analyzeSidebar();
```

---

### 4.2 Análisis de jerarquía

**Objetivo:** Entender la estructura jerárquica de tu workspace.

**Ejercicio:**
```javascript
// Identify hierarchy levels
function analyzeHierarchy() {
    const items = document.querySelectorAll('[class*="sidebar"] [role="link"], [class*="tree"] a');

    console.log('=== HIERARCHY ANALYSIS ===\n');

    items.forEach((item, index) => {
        // Look for level indicators (indentation, padding, etc.)
        const style = window.getComputedStyle(item);
        const paddingLeft = style.paddingLeft;

        console.log(`${index + 1}. ${item.textContent.trim()} (padding: ${paddingLeft})`);
    });

    console.log('\nObserve the padding values - greater padding = more nested');
}

// Execute
analyzeHierarchy();
```

---

### 4.3 Estadísticas de uso personal

**Objetivo:** Crear métricas sobre tu propio uso de Notion.

**Ejercicio:**
```javascript
// Track visits with timestamps
function trackVisit() {
    const pageId = window.location.pathname;
    const timestamp = new Date().toISOString();

    // Get history
    let history = JSON.parse(localStorage.getItem('notionVisits') || '{}');

    // Add this visit
    if (!history[pageId]) {
        history[pageId] = [];
    }
    history[pageId].push(timestamp);

    // Save
    localStorage.setItem('notionVisits', JSON.stringify(history));

    // Report
    console.log('=== YOUR NOTION USAGE ===');
    console.log('Current page:', pageId);
    console.log('Visits to this page:', history[pageId].length);
    console.log('Total pages visited:', Object.keys(history).length);

    // Most visited pages
    const sortedPages = Object.entries(history)
        .map(([id, visits]) => ({ id, visits: visits.length }))
        .sort((a, b) => b.visits - a.visits);

    console.log('\nYour most visited pages:');
    console.table(sortedPages.slice(0, 5));
}

// Execute every time you visit a page
trackVisit();
```

---

## 5. Experimentos visuales

### 5.1 Modo oscuro personalizado

**Objetivo:** Experimentar con estilos personalizados.

**Contexto:** Entender cómo funcionan los temas te ayuda a diseñar mejores 
funcionalidades de personalización.

**Ejercicio:**
```javascript
// Apply a custom theme
function applyCustomTheme() {
    document.body.style.backgroundColor = '#1a1a1a';
    document.body.style.color = '#e0e0e0';

    // Change the color of all text
    const elements = document.querySelectorAll('*');
    elements.forEach(el => {
        if (window.getComputedStyle(el).color === 'rgb(0, 0, 0)') {
            el.style.color = '#e0e0e0';
        }
    });

    console.log('✓ Dark theme applied. Reload (F5) to revert.');
}

// Execute
applyCustomTheme();
```

---

### 5.2 Resaltar elementos

**Objetivo:** Destacar visualmente ciertos tipos de contenido.

**Ejercicio:**
```javascript
// Highlight all links
function highlightLinks() {
    const links = document.querySelectorAll('a');
    links.forEach(link => {
        link.style.backgroundColor = 'yellow';
        link.style.padding = '2px 4px';
        link.style.borderRadius = '3px';
    });
    console.log(`✓ ${links.length} links highlighted`);
}

// Execute
highlightLinks();
```

**Reto:** Crea una función para resaltar todas las tareas completadas (checkboxes marcados).

---

### 5.3 Modo de enfoque

**Objetivo:** Ocultar distracciones para enfocarte en el contenido.

**Ejercicio:**
```javascript
// Focus mode - hide sidebar
function focusMode() {
    const sidebar = document.querySelector('[class*="sidebar"], [class*="left"], aside');

    if (sidebar) {
        sidebar.style.display = 'none';
        console.log('✓ Focus mode activated - sidebar hidden');

        // Expand main content
        const main = document.querySelector('main, [class*="page"], [class*="content"]');
        if (main) {
            main.style.marginLeft = '0';
            main.style.maxWidth = '100%';
        }
    } else {
        console.log('Could not find the sidebar');
    }

    console.log('Reload (F5) to return to normal');
}

// Execute
focusMode();
```

---

### 5.4 Análisis de colores

**Objetivo:** Extraer la paleta de colores usada en tu página.

**Ejercicio:**
```javascript
// Extract unique colors
function analyzeColors() {
    const elements = document.querySelectorAll('*');
    const colors = new Set();

    elements.forEach(el => {
        const style = window.getComputedStyle(el);
        colors.add(style.color);
        colors.add(style.backgroundColor);
    });

    const colorsArray = Array.from(colors)
        .filter(color => color !== 'rgba(0, 0, 0, 0)' && color !== 'transparent');

    console.log('=== COLOR PALETTE ===');
    console.log(`Unique colors found: ${colorsArray.length}`);
    console.log('\nFirst 20 colors:');
    colorsArray.slice(0, 20).forEach(color => {
        console.log(`%c ${color}`, `color: ${color}; background: ${color}; padding: 5px;`);
    });
}

// Execute
analyzeColors();
```

---

## 6. Análisis de uso personal

### 6.1 Tiempo en la página

**Objetivo:** Trackear cuánto tiempo pasas en cada página.

**Ejercicio:**
```javascript
// Time tracking system
const startTime = Date.now();

function timeReport() {
    const totalTime = Date.now() - startTime;
    const minutes = Math.floor(totalTime / 60000);
    const seconds = Math.floor((totalTime % 60000) / 1000);

    console.log(`⏱️ You have been on this page for ${minutes}m ${seconds}s`);

    // Save to history
    const pageId = window.location.pathname;
    let history = JSON.parse(localStorage.getItem('notionTimes') || '{}');

    if (!history[pageId]) {
        history[pageId] = 0;
    }
    history[pageId] += totalTime;

    localStorage.setItem('notionTimes', JSON.stringify(history));

    // Show accumulated total
    const totalMinutes = Math.floor(history[pageId] / 60000);
    console.log(`📊 Total time on this page: ${totalMinutes} minutes`);
}

// Execute at intervals
setInterval(timeReport, 60000); // Every minute

// Also execute on exit (doesn't always work)
window.addEventListener('beforeunload', timeReport);

console.log('⏱️ Time tracking started');
```

---

### 6.2 Contador de ediciones

**Objetivo:** Detectar cuándo editas contenido.

**Ejercicio:**
```javascript
// Observe DOM changes
let changeCounter = 0;

const observer = new MutationObserver(mutations => {
    changeCounter += mutations.length;
});

// Observe main content
const container = document.querySelector('[class*="page"], main');
if (container) {
    observer.observe(container, {
        childList: true,
        subtree: true,
        characterData: true
    });

    console.log('👀 Observing page changes...');

    // Report every 10 seconds
    setInterval(() => {
        if (changeCounter > 0) {
            console.log(`✏️ Changes detected: ${changeCounter}`);
            changeCounter = 0;
        }
    }, 10000);
}
```

---

### 6.3 Dashboard personal de productividad

**Objetivo:** Crear un dashboard completo de tu uso de Notion.

**Ejercicio:**
```javascript
// Productivity dashboard in Notion
function productivityDashboard() {
    // Collect data
    const visits = JSON.parse(localStorage.getItem('notionVisits') || '{}');
    const times = JSON.parse(localStorage.getItem('notionTimes') || '{}');

    console.log('='.repeat(50));
    console.log('📊 YOUR NOTION PRODUCTIVITY DASHBOARD');
    console.log('='.repeat(50));

    // Total unique pages visited
    const totalPages = Object.keys(visits).length;
    console.log(`\n📄 Unique pages visited: ${totalPages}`);

    // Total visits
    const totalVisits = Object.values(visits).reduce((sum, arr) => sum + arr.length, 0);
    console.log(`👀 Total visits: ${totalVisits}`);

    // Total time
    const totalTime = Object.values(times).reduce((sum, t) => sum + t, 0);
    const totalHours = (totalTime / 3600000).toFixed(1);
    console.log(`⏱️ Total time in Notion: ${totalHours} hours`);

    // Top 5 most visited pages
    console.log('\n🏆 TOP 5 MOST VISITED PAGES:');
    const topPages = Object.entries(visits)
        .map(([id, arr]) => ({ id, visits: arr.length }))
        .sort((a, b) => b.visits - a.visits)
        .slice(0, 5);
    console.table(topPages);

    // Today's statistics
    const today = new Date().toISOString().split('T')[0];
    let visitsToday = 0;
    Object.values(visits).forEach(arr => {
        visitsToday += arr.filter(v => v.startsWith(today)).length;
    });
    console.log(`\n📅 Visits today: ${visitsToday}`);

    // Average visits per day
    const firstVisit = Object.values(visits).flat().sort()[0];
    if (firstVisit) {
        const daysUsing = Math.max(1, Math.ceil((Date.now() - new Date(firstVisit)) / 86400000));
        const dailyAverage = (totalVisits / daysUsing).toFixed(1);
        console.log(`📈 Average visits per day: ${dailyAverage}`);
    }

    console.log('\n' + '='.repeat(50));
}

// Execute
productivityDashboard();
```

---

## 7. Proyectos avanzados

### 7.1 Exportador de contenido

**Objetivo:** Crear una función que exporte el contenido de la página actual 
en formato markdown.

**Contexto:** Útil para backups, migraciones, o compartir contenido fuera de Notion.

**Ejercicio:**
```javascript
function exportMarkdown() {
    const container = document.querySelector('[class*="page"], main');
    if (!container) {
        console.log('Could not find the content');
        return;
    }

    let markdown = '';

    // Helper function to convert elements to markdown
    function processElement(element) {
        const tag = element.tagName.toLowerCase();
        const text = element.textContent.trim();

        switch(tag) {
            case 'h1':
                return `# ${text}\n\n`;
            case 'h2':
                return `## ${text}\n\n`;
            case 'h3':
                return `### ${text}\n\n`;
            case 'p':
                return `${text}\n\n`;
            case 'li':
                return `- ${text}\n`;
            case 'a':
                return `[${text}](${element.href})`;
            default:
                return text ? `${text}\n` : '';
        }
    }

    // Traverse elements (simplified)
    const elements = container.querySelectorAll('h1, h2, h3, p, li, a');
    elements.forEach(el => {
        markdown += processElement(el);
    });

    console.log('=== CONTENT IN MARKDOWN ===\n');
    console.log(markdown);
    console.log('\n=== END OF CONTENT ===');

    return markdown;
}

// Execute
exportMarkdown();
```

---

### 7.2 Buscador personalizado

**Objetivo:** Crear una función de búsqueda que encuentre texto en toda la página.

**Ejercicio:**
```javascript
function searchInPage(term) {
    const container = document.querySelector('[class*="page"], main');
    if (!container) {
        console.log('Could not find the content');
        return;
    }

    const elements = container.querySelectorAll('*');
    const results = [];

    elements.forEach(el => {
        if (el.textContent.toLowerCase().includes(term.toLowerCase()) &&
            el.children.length === 0) { // Only "leaf" elements

            results.push({
                type: el.tagName,
                text: el.textContent.substring(0, 100),
                element: el
            });
        }
    });

    console.log(`=== SEARCH: "${term}" ===`);
    console.log(`Results found: ${results.length}\n`);

    results.forEach((r, i) => {
        console.log(`${i + 1}. [${r.type}] ${r.text}...`);

        // Highlight visually
        r.element.style.backgroundColor = 'yellow';
    });

    return results;
}

// Usage: searchInPage('your search term')
```

---

### 7.3 Analizador de productividad textual

**Objetivo:** Analizar tu estilo de escritura y uso de Notion.

**Ejercicio:**
```javascript
function analyzeWriting() {
    const text = extractFullContent(); // From previous exercises

    if (!text) return;

    // Basic analysis
    const words = text.trim().split(/\s+/);
    const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 0);

    // Calculate statistics
    const totalWords = words.length;
    const totalSentences = sentences.length;
    const wordsPerSentence = (totalWords / totalSentences).toFixed(1);

    // Most used words
    const frequency = {};
    words.forEach(word => {
        const clean = word.toLowerCase().replace(/[^a-záéíóúñ]/g, '');
        if (clean.length > 3) { // Only words longer than 3 letters
            frequency[clean] = (frequency[clean] || 0) + 1;
        }
    });

    const topWords = Object.entries(frequency)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 10);

    // Report
    console.log('='.repeat(50));
    console.log('📝 YOUR WRITING ANALYSIS');
    console.log('='.repeat(50));
    console.log(`\n📊 General statistics:`);
    console.log(`- Total words: ${totalWords}`);
    console.log(`- Sentences: ${totalSentences}`);
    console.log(`- Words per sentence: ${wordsPerSentence}`);

    console.log(`\n🔤 Your 10 most used words:`);
    console.table(topWords.map(([word, freq]) => ({ word, frequency: freq })));

    // Length analysis
    const averageLength = words.reduce((sum, p) => sum + p.length, 0) / totalWords;
    console.log(`\n📏 Average word length: ${averageLength.toFixed(1)} characters`);

    // Estimated reading time (250 words per minute)
    const minutes = Math.ceil(totalWords / 250);
    console.log(`⏱️ Estimated reading time: ${minutes} minutes`);

    console.log('\n' + '='.repeat(50));
}

// Execute
analyzeWriting();
```

---

### 7.4 Monitor de cambios en tiempo real

**Objetivo:** Crear un sistema que te notifique cuando se modifica la página.

**Contexto:** Útil para colaboración - saber cuando alguien más está editando.

**Ejercicio:**
```javascript
// Advanced monitoring system
function startMonitoring() {
    let lastChange = Date.now();
    const changes = [];

    const observer = new MutationObserver(mutations => {
        const now = Date.now();

        mutations.forEach(mutation => {
            const record = {
                type: mutation.type,
                element: mutation.target.tagName || 'TEXT',
                timestamp: new Date().toLocaleTimeString(),
                msSinceLast: now - lastChange
            };

            changes.push(record);

            // Log if more than 1 second has passed since last change
            if (now - lastChange > 1000) {
                console.log(`✏️ [${record.timestamp}] Change detected in ${record.element}`);
            }
        });

        lastChange = now;
    });

    // Observe the entire document
    observer.observe(document.body, {
        childList: true,
        subtree: true,
        characterData: true,
        attributes: true
    });

    console.log('👀 Change monitor activated');

    // Report every minute
    setInterval(() => {
        if (changes.length > 0) {
            console.log(`\n📊 Changes in the last minute: ${changes.length}`);
            changes.length = 0; // Clear
        }
    }, 60000);

    // Function to stop
    window.stopMonitoring = () => {
        observer.disconnect();
        console.log('❌ Monitor stopped');
    };

    console.log('To stop: run stopMonitoring()');
}

// Execute
startMonitoring();
```

### Siguientes pasos
1. Practica regularmente - usa la consola diariamente
2. Explora otras herramientas que uses (Slack, Trello, etc.)
3. Comparte tus descubrimientos con tu equipo
4. Incorpora JavaScript a tus hábitos ;)
