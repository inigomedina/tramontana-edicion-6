# El navegador también es un sistema

## Antes de empezar

1. Asegúrate de tener abierto el archivo `index-dom.html` en tu navegador
2. Abre la consola del navegador (F12 o Cmd+Option+J)
3. Verifica que ves el Dashboard de Producto
4. Cada ejercicio debe ejecutarse en la consola

## Índice de ejercicios 

1. [Exploración inicial](#1-exploración-inicial)
2. [Selección de elementos](#2-selección-de-elementos)
3. [Extracción de información](#3-extracción-de-información)
4. [Análisis de datos](#4-análisis-de-datos)
5. [Modificación del DOM](#5-modificación-del-dom)
6. [Trabajo con localStorage](#6-trabajo-con-localstorage)
7. [Ejercicios integradores](#7-ejercicios-integradores)

---

## 1. Exploración inicial

### 1.1 Tu primer comando

**Objetivo:** Familiarizarte con la ejecución de comandos en la consola.

**Contexto:** La consola te permite ejecutar código JavaScript directamente.
Es como tener acceso de "admin" para inspeccionar cualquier aplicación web.

**Ejercicio:**
Escribe este comando en la consola y presiona Enter:

```javascript
console.log('Hello from the console!');
```

**¿Qué debería pasar?**
Deberías ver tu mensaje impreso en la consola.

---

### 1.2 Explorar el documento

**Objetivo:** Entender que toda la página es un objeto JavaScript llamado 
`document`.

**Contexto:** El DOM (Document Object Model) es la representación en JavaScript 
de todo lo que ves en la página. Entender esto te ayuda a comunicarte mejor con 
tu equipo técnico. Y te ayuda a entender el sistema de programaición que es el
propio navegador.

**Ejercicio:**
```javascript
console.log(document);
```

**Observa:**
- Se imprime un objeto HTML completo
- Puedes expandirlo para ver su estructura
- Todo lo que ves en la página está dentro de este objeto

**Ejercicio adicional:**
```javascript
console.log(document.title);
```
¿Qué devuelve? Compáralo con el título de la pestaña del navegador.

---

### 1.3 Información de la página

**Objetivo:** Extraer información básica de la página.

**Ejercicio:** Ejecuta cada comando y observa qué devuelve:

```javascript
// What is the URL of this page?
console.log(document.URL);

// When was it last modified?
console.log(document.lastModified);

// What encoding does it use?
console.log(document.characterSet);
```

**Reflexión:** Piensa en contextos de QA, debugging o análisis de competencia.

---

## 2. Selección de elementos

### 2.1 Seleccionar por ID

**Objetivo:** Encontrar un elemento específico usando su ID único.

**Contexto:** Es como buscar un usuario por su ID único en tu base de datos.

**Ejercicio:**
```javascript
const list = document.getElementById('featuresList');
console.log(list);
```

**Observa:**
- Devuelve UN elemento específico
- Los IDs son únicos en una página
- Puedes expandir el elemento para ver su contenido

**Ejercicio adicional:**
```javascript
// Try to select the metrics table
const table = document.getElementById('metricsTable');
console.log(table);
```

---

### 2.2 Seleccionar por clase CSS

**Objetivo:** Seleccionar elementos usando selectores CSS.

**Contexto:** Así puedes encontrar múltiples elementos del mismo tipo (como 
todas las features, todos los usuarios, etc.).

**Ejercicio:**
```javascript
// Select ONE element with that class (the first one found)
const firstFeature = document.querySelector('.feature-item');
console.log(firstFeature);

// Select ALL elements with that class
const allFeatures = document.querySelectorAll('.feature-item');
console.log(allFeatures);
```

**Pregunta:** ¿Cuál es la diferencia entre `querySelector` y `querySelectorAll`?

**Ejercicio práctico:**
```javascript
// How many features are there in total?
const features = document.querySelectorAll('.feature-item');
console.log('Total features:', features.length);
```

---

### 2.3 Selectores CSS avanzados

**Objetivo:** Usar selectores más específicos.

**Contexto:** Cuando quieres ser muy específico en lo que buscas (por ejemplo, 
solo features en desarrollo).

**Ejercicio:**
```javascript
// Select all status badges
const statusBadges = document.querySelectorAll('.feature-status');
console.log('Status badges found:', statusBadges.length);

// Select all user cards
const users = document.querySelectorAll('.user-card');
console.log('Team users:', users.length);

// Select all table rows (excluding header)
const metricRows = document.querySelectorAll('.metrics-table tbody tr');
console.log('Metrics recorded:', metricRows.length);
```

---

### 2.4 Seleccionar por atributos data

**Objetivo:** Usar atributos data-* para encontrar elementos con características 
específicas.

**Contexto:** Los atributos data-* almacenan metadata sobre elementos. Son muy 
útiles para análisis.

**Ejercicio:**
```javascript
// Select all high priority features
const highFeatures = document.querySelectorAll('[data-priority="high"]');
console.log('High priority features:', highFeatures.length);

// Select all frontend team features
const frontendFeatures = document.querySelectorAll('[data-team="frontend"]');
console.log('Frontend features:', frontendFeatures.length);
```

**Reto:** ¿Puedes seleccionar todos los miembros del equipo con seniority 
"senior"?

---

## 3. Extracción de información

### 3.1 Leer contenido de texto

**Objetivo:** Extraer el texto visible de elementos.

**Contexto:** Útil para hacer scraping de información, auditorías de contenido, 
o análisis.

**Ejercicio:**
```javascript
// Get the main title
const title = document.querySelector('h1');
console.log(title.textContent);

// Get the name of the first feature
const firstFeature = document.querySelector('.feature-name');
console.log(firstFeature.textContent);
```

---

### 3.2 Extraer múltiples valores

**Objetivo:** Obtener información de múltiples elementos a la vez.

**Contexto:** Cuando necesitas analizar listas completas de datos.

**Ejercicio:**
```javascript
// Get the names of all features
const featureNames = document.querySelectorAll('.feature-name');
featureNames.forEach(feature => {
    console.log(feature.textContent);
});
```

**Observa:**
- Usamos `forEach` para iterar sobre cada elemento
- Es similar a hacer un loop en Excel o en SQL

**Reto:** ¿Puedes obtener los nombres de todos los miembros del equipo?

<details>
<summary>💡 Ver pista</summary>

```javascript
const names = document.querySelectorAll('.user-name');
names.forEach(name => {
    console.log(name.textContent);
});
```
</details>

---

### 3.3 Leer atributos data

**Objetivo:** Acceder a metadata almacenada en atributos.

**Contexto:** Los atributos data-* frecuentemente contienen información 
estructurada (IDs, valores numéricos, categorías).

**Ejercicio:**
```javascript
// Get information from a specific feature
const feature = document.querySelector('[data-feature-id="F001"]');
console.log('ID:', feature.dataset.featureId);
console.log('Priority:', feature.dataset.priority);
console.log('Team:', feature.dataset.team);
```

**Nota:** Observa que `data-feature-id` se convierte en `dataset.featureId` 
(camelCase).

**Ejercicio adicional:**
```javascript
// View all data attributes of an element
const feature = document.querySelector('.feature-item');
console.log('All data attributes:', feature.dataset);
```

---

## 4. Análisis de datos

### 4.1 Crear un array de datos

**Objetivo:** Extraer datos y convertirlos en una estructura manipulable.

**Contexto:** Convertir lo visual en datos que puedes analizar, exportar, o usar 
en reports.

**Ejercicio:**
```javascript
// Create an array with information from all features
const featuresData = [];
const features = document.querySelectorAll('.feature-item');

features.forEach(feature => {
    const data = {
        id: feature.dataset.featureId,
        name: feature.querySelector('.feature-name').textContent,
        priority: feature.dataset.priority,
        team: feature.dataset.team,
        progress: feature.dataset.progress
    };
    featuresData.push(data);
});

console.table(featuresData);
```

**Observa:**
- Usamos `console.table()` para ver los datos en formato tabla
- Es mucho más fácil de leer que un array normal

---

### 4.2 Filtrar datos

**Objetivo:** Aplicar filtros para analizar subconjuntos de datos.

**Contexto:** Como aplicar filtros en Excel o en tu herramienta de analytics.

**Ejercicio:**
```javascript
// From the previous exercise, filter only high priority features
const highPriorityFeatures = featuresData.filter(f => f.priority === 'high');
console.table(highPriorityFeatures);

// Count how many there are
console.log('High priority features:', highPriorityFeatures.length);
```

**Reto:** Filtra solo las features del equipo de frontend.

---

### 4.3 Calcular estadísticas

**Objetivo:** Realizar cálculos sobre los datos extraídos.

**Contexto:** Calcular promedios, totales, porcentajes - habilidades core de product analytics.

**Ejercicio:**
```javascript
// Calculate the average progress of all features
const totalProgress = featuresData.reduce((sum, f) => sum + parseInt(f.progress), 0);
const averageProgress = totalProgress / featuresData.length;
console.log('Average progress:', averageProgress.toFixed(2) + '%');
```

**Ejercicio adicional:**
```javascript
// Group features by team
const featuresByTeam = {};
featuresData.forEach(f => {
    if (!featuresByTeam[f.team]) {
        featuresByTeam[f.team] = 0;
    }
    featuresByTeam[f.team]++;
});
console.table(featuresByTeam);
```

---

### 4.4 Extraer métricas

**Objetivo:** Convertir la tabla de métricas en datos estructurados.

**Contexto:** Saber extraer métricas programáticamente es muy valioso.

**Ejercicio:**
```javascript
// Extract all metrics in a clean object
const metrics = {};
const metricRows = document.querySelectorAll('.metrics-table tbody tr');

metricRows.forEach(row => {
    const metricKey = row.dataset.metric;
    const metricValue = parseFloat(row.dataset.value);
    metrics[metricKey] = metricValue;
});

console.log('Product metrics:', metrics);
console.log('Current MAU:', metrics.mau);
console.log('Conversion rate:', metrics.conversion + '%');
```

---

## 5. Modificación del DOM

### 5.1 Cambiar texto

**Objetivo:** Modificar el contenido visible de elementos.

**Contexto:** Útil para prototipar cambios, hacer mockups rápidos, o testing 
A/B manual.

**Ejercicio:**
```javascript
// Change the main title
const title = document.querySelector('h1');
title.textContent = 'My Custom Dashboard';
```

**Observa:** El cambio es inmediato y visible. Recarga la página (F5) para volver 
al original.

**Ejercicio adicional:**
```javascript
// Change the name of a feature
const firstFeature = document.querySelector('.feature-name');
firstFeature.textContent = 'New Important Feature';
```

---

### 5.2 Modificar estilos

**Objetivo:** Cambiar la apariencia visual de elementos.

**Contexto:** Probar variaciones visuales sin necesidad de modificar el código 
fuente.

**Ejercicio:**
```javascript
// Change the title color
const title = document.querySelector('h1');
title.style.color = 'red';
title.style.fontSize = '48px';
```

**Ejercicio creativo:**
```javascript
// Highlight high priority features
const highFeatures = document.querySelectorAll('[data-priority="high"]');
highFeatures.forEach(feature => {
    feature.style.backgroundColor = '#fff3cd';
    feature.style.borderLeft = '4px solid #ffc107';
});
```

---

### 5.3 Agregar y eliminar CSS

**Objetivo:** Usar clases CSS existentes para modificar estilos.

**Contexto:** Más limpio que modificar estilos inline. Las clases CSS ya tienen 
estilos definidos.

**Ejercicio:**
```javascript
// View the current classes of an element
const feature = document.querySelector('.feature-item');
console.log('Current classes:', feature.classList);

// Add a class
feature.classList.add('highlighted');

// Remove a class
feature.classList.remove('feature-item');

// Toggle (add if doesn't exist, remove if exists)
feature.classList.toggle('active');

// Check if it has a class
console.log('Has highlighted class?', feature.classList.contains('highlighted'));
```

---

### 5.4 Modificar atributos

**Objetivo:** Cambiar atributos de elementos (incluyendo data-*).

**Contexto:** Útil para cambiar estados, actualizar metadata, o simular interacciones.

**Ejercicio:**
```javascript
// Change the priority of a feature
const feature = document.querySelector('[data-feature-id="F002"]');
console.log('Current priority:', feature.dataset.priority);
feature.dataset.priority = 'high';
console.log('New priority:', feature.dataset.priority);
```

---

### 5.5 Crear y agregar elementos

**Objetivo:** Crear nuevos elementos HTML y agregarlos al DOM.

**Contexto:** Prototipar nuevas features, agregar elementos a listas, simular estados.

**Ejercicio:**
```javascript
// Create a new feature
const newFeature = document.createElement('li');
newFeature.className = 'feature-item';
newFeature.dataset.featureId = 'F006';
newFeature.dataset.priority = 'medium';
newFeature.dataset.team = 'backend';
newFeature.innerHTML = `
    <div class="feature-info">
        <div class="feature-name">Email Notification System</div>
        <span class="feature-status status-planning">Planning</span>
    </div>
    <div data-progress="10">10%</div>
`;

// Add it to the list
const list = document.getElementById('featuresList');
list.appendChild(newFeature);
```

**Observa:** Ahora hay una nueva feature en la lista. ¡La creaste con código!

---

### 5.6 Eliminar elementos

**Objetivo:** Remover elementos del DOM.

**Contexto:** Útil para prototipar layouts sin ciertas secciones, o simular eliminación de features.

**Ejercicio:**
```javascript
// Delete the last feature
const features = document.querySelectorAll('.feature-item');
const lastFeature = features[features.length - 1];
lastFeature.remove();
```

**Recuerda:** Recarga la página (F5) para recuperar los elementos eliminados.

---

## 6. Trabajo con localStorage

### 6.1 Entender localStorage

**Objetivo:** Comprender qué es localStorage y para qué sirve.

**Contexto:** localStorage es como una mini base de datos en el navegador. 
Las apps lo usan para guardar preferencias, sesiones, cache, etc. 
Entenderlo te ayuda a:

- Diseñar mejor las features de tu producto
- Hacer debugging de problemas de usuarios
- Entender limitaciones técnicas (espacio, privacidad, etc.)

**Teoría:**
- Almacena datos como pares clave-valor (como un diccionario)
- Los datos persisten incluso después de cerrar el navegador
- Solo almacena strings (pero podemos guardar JSON)
- Tiene un límite de ~5-10MB por dominio

---

### 6.2 Leer del localStorage

**Objetivo:** Ver qué datos ya están guardados.

**Ejercicio:**
```javascript
// View all saved data
console.log('Complete LocalStorage:', localStorage);

// Read a specific value
const savedData = localStorage.getItem('productDashboard');
console.log('Dashboard data:', savedData);
```

**Observa:** Los datos están en formato string JSON.

**Ejercicio adicional:**
```javascript
// Convert the JSON string to JavaScript object
const data = JSON.parse(localStorage.getItem('productDashboard'));
console.log('Data as object:', data);
console.log('Last visit:', data.lastVisit);
console.log('Preferences:', data.userPreferences);
```

---

### 6.3 Guardar en localStorage

**Objetivo:** Almacenar nuevos datos o actualizar existentes.

**Contexto:** Simular preferencias del usuario, guardar estado de la aplicación, etc.

**Ejercicio:**
```javascript
// Save a simple value
localStorage.setItem('myName', 'YourName');

// Read it
console.log(localStorage.getItem('myName'));
```

**Ejercicio con objetos:**
```javascript
// Save a complete object (like user preferences)
const preferences = {
    theme: 'dark',
    language: 'en',
    notifications: true,
    defaultView: 'dashboard'
};

// Convert to JSON string before saving
localStorage.setItem('myPreferences', JSON.stringify(preferences));

// Read and convert back
const savedPrefs = JSON.parse(localStorage.getItem('myPreferences'));
console.log('Saved preferences:', savedPrefs);
console.log('Preferred theme:', savedPrefs.theme);
```

---

### 6.4 Actualizar datos existentes

**Objetivo:** Modificar datos ya guardados en localStorage.

**Ejercicio:**
```javascript
// Read current dashboard data
const dashboardData = JSON.parse(localStorage.getItem('productDashboard'));

// Modify something
dashboardData.userPreferences.theme = 'dark';
dashboardData.lastVisit = new Date().toISOString();

// Save back
localStorage.setItem('productDashboard', JSON.stringify(dashboardData));

// Verify
console.log('Updated data:', JSON.parse(localStorage.getItem('productDashboard')));
```

---

### 6.5 Eliminar del localStorage

**Objetivo:** Borrar datos específicos o limpiar todo el storage.

**Ejercicio:**
```javascript
// Remove a specific item
localStorage.removeItem('myName');

// Verify it was removed
console.log('Does myName exist?', localStorage.getItem('myName')); // null

// Clear ALL localStorage (careful!)
// localStorage.clear();
```

**Nota:** Comenta `localStorage.clear()` para no borrar accidentalmente todo.

---

### 6.6 SessionStorage

**Objetivo:** Conocer la alternativa temporal a localStorage.

**Contexto:** sessionStorage funciona igual que localStorage, pero los datos se 
borran cuando cierras la pestaña/ventana. Útil para datos temporales de sesión.

**Ejercicio:**
```javascript
// Save in sessionStorage
sessionStorage.setItem('currentSession', 'session-123');

// Read
console.log('Session:', sessionStorage.getItem('currentSession'));

// Save the session start timestamp
sessionStorage.setItem('sessionStart', new Date().toISOString());
console.log('You started the session at:', sessionStorage.getItem('sessionStart'));
```

**Experimento:** Cierra esta pestaña y vuelve a abrir `index-dom.html`. 
¿Qué pasó con los datos de sessionStorage vs localStorage?


## 7. Ejercicios integradores

Estos ejercicios combinan múltiples conceptos que has aprendido.

---

### 7.1 Crear un sistema de favoritos

**Objetivo:** Permitir "marcar" features favoritas y guardarlas.

**Ejercicio:**
```javascript
// Complete favorites system

// 1. Function to add to favorites
function addFavorite(featureId) {
    let favorites = JSON.parse(localStorage.getItem('favoriteFeatures') || '[]');
    if (!favorites.includes(featureId)) {
        favorites.push(featureId);
        localStorage.setItem('favoriteFeatures', JSON.stringify(favorites));
        console.log(`✓ Feature ${featureId} added to favorites`);
    } else {
        console.log(`Feature ${featureId} is already in favorites`);
    }
}

// 2. Function to remove from favorites
function removeFavorite(featureId) {
    let favorites = JSON.parse(localStorage.getItem('favoriteFeatures') || '[]');
    favorites = favorites.filter(id => id !== featureId);
    localStorage.setItem('favoriteFeatures', JSON.stringify(favorites));
    console.log(`✗ Feature ${featureId} removed from favorites`);
}

// 3. Function to view favorites
function viewFavorites() {
    const favorites = JSON.parse(localStorage.getItem('favoriteFeatures') || '[]');
    console.log('Favorite features:', favorites);

    favorites.forEach(id => {
        const feature = document.querySelector(`[data-feature-id="${id}"]`);
        if (feature) {
            const name = feature.querySelector('.feature-name').textContent;
            console.log(`- ${id}: ${name}`);
        }
    });
}

// 4. Function to visually highlight favorites
function highlightFavorites() {
    const favorites = JSON.parse(localStorage.getItem('favoriteFeatures') || '[]');
    favorites.forEach(id => {
        const feature = document.querySelector(`[data-feature-id="${id}"]`);
        if (feature) {
            feature.style.borderLeft = '5px solid gold';
            feature.style.backgroundColor = '#fff9e6';
        }
    });
}

// Try it:
addFavorite('F001');
addFavorite('F003');
viewFavorites();
highlightFavorites();
```

---

### 7.2 Exportar datos a CSV

**Objetivo:** Extraer los datos del dashboard en un formato que puedas usar en 
Excel/Sheets.

**Contexto:** Muy útil para crear reportes, compartir datos con stakeholders o 
análisis profundo.

**Ejercicio:**
```javascript
// Function to export features to CSV format
function exportFeaturesCSV() {
    const features = document.querySelectorAll('.feature-item');

    // CSV header
    let csv = 'ID,Name,Priority,Team,Progress\n';

    // Data
    features.forEach(feature => {
        const id = feature.dataset.featureId;
        const name = feature.querySelector('.feature-name').textContent;
        const priority = feature.dataset.priority;
        const team = feature.dataset.team;
        const progress = feature.querySelector('[data-progress]').dataset.progress;

        csv += `${id},"${name}",${priority},${team},${progress}\n`;
    });

    // Show in console
    console.log('=== FEATURES CSV ===');
    console.log(csv);
    console.log('\nCopy this text and paste it in a .csv file or directly in Excel/Sheets');

    return csv;
}

// Execute
exportFeaturesCSV();

// BONUS: Download as file
function downloadCSV() {
    const csv = exportFeaturesCSV();
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'features-dashboard.csv';
    a.click();
}

// Uncomment to download:
// downloadCSV();
```

---

### 7.3 Simulador de actualización en tiempo real

**Objetivo:** Simular cómo se actualizaría un dashboard real con datos en tiempo real.

**Ejercicio:**
```javascript
// Function that simulates progress updates
function simulateUpdates() {
    const features = document.querySelectorAll('.feature-item');

    console.log('Starting update simulation...');

    setInterval(() => {
        // Choose a random feature
        const randomIndex = Math.floor(Math.random() * features.length);
        const feature = features[randomIndex];

        // Get current progress
        const progressElement = feature.querySelector('[data-progress]');
        let currentProgress = parseInt(progressElement.dataset.progress);

        // Increment progress (max 100)
        if (currentProgress < 100) {
            currentProgress = Math.min(100, currentProgress + Math.floor(Math.random() * 5) + 1);

            // Update
            progressElement.dataset.progress = currentProgress;
            progressElement.textContent = currentProgress + '%';

            const name = feature.querySelector('.feature-name').textContent;
            console.log(`📊 ${name}: ${currentProgress}%`);

            // If it reaches 100, change status
            if (currentProgress === 100) {
                const status = feature.querySelector('.feature-status');
                status.textContent = 'Completed';
                status.className = 'feature-status status-deployed';
                console.log(`✅ ${name} completed!`);
            }
        }
    }, 2000); // Every 2 seconds

    console.log('Simulation active. Watch how progress updates...');
}

// To start: simulateUpdates()
// To stop: reload the page (F5)
```

---

## Próximos pasos

Si te animas, puedes seguir experimentando con **`ejercicios-notion.md`** para 
aplicar esto en un sistema real.

---

## Tips finales

**Mejores Prácticas:**
- Usa nombres de variables descriptivos
- Comenta tu código para recordar qué hace
- Guarda tus funciones útiles en un archivo personal
- Practica regularmente - la consola es una herramienta diaria

**Debugging:**
- Si algo no funciona, lee el error en rojo en la consola
- Usa `console.log()` liberalmente para ver qué está pasando
- Prueba partes pequeñas de código antes de ejecutar todo junto

**Recursos:**
- [MDN JavaScript Guide](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide)
- [JavaScript.info](https://javascript.info/)
- [Chrome DevTools Documentation](https://developer.chrome.com/docs/devtools/)
