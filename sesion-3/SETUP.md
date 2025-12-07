# Setup para la Sesión 3

## Verificar si ya tienes Python

Abre la terminal y ejecuta:

```bash
python3 --version
```

**Si ves algo como `Python 3.x.x`** → Ya estás listo. Salta a "Verificar que todo funciona".

**Si ves un error** → Sigue las instrucciones de instalación.

---

## Instalar Python (solo si no lo tienes)

### macOS

Python 3 viene incluido en macOS moderno. Si no lo tienes:

```bash
# Opción 1: Instalar Xcode Command Line Tools (incluye Python)
xcode-select --install

# Opción 2: Desde python.org
# Descarga de https://www.python.org/downloads/
```

### Windows

**Opción más fácil (2 minutos):**

1. Abre Microsoft Store
2. Busca "Python 3.11"
3. Click en "Obtener"
4. Listo

**Alternativa:**
- Descarga desde https://www.python.org/downloads/
- IMPORTANTE: Marca la casilla "Add Python to PATH" durante la instalación

---

## Verificar que todo funciona

Una vez tengas Python, ejecuta este comando en la terminal:

```bash
python3 -c "print('Python funcionando')"
```

Deberías ver: `Python funcionando`

---

## Abrir la terminal

### macOS
- Cmd + Espacio → escribe "Terminal" → Enter
- O: Aplicaciones → Utilidades → Terminal

### Windows
- Win + R → escribe "cmd" → Enter
- O: Buscar "Command Prompt" o "PowerShell"

---

## Clonar el repositorio

```bash
git clone [URL_DEL_REPO]
cd tramontana-edicion-6
```

---

## Probar la API

En una terminal:
```bash
python3 api/server.py
```

En otra terminal:
```bash
curl http://localhost:3000/api/users
```

Si ves JSON con usuarios, todo funciona.

---

## Problemas comunes

### "python3 no encontrado" en Windows

Prueba con `python` (sin el 3):
```bash
python --version
```

Si funciona, usa `python` en lugar de `python3` en todos los comandos.

### "curl no encontrado" en Windows

Usa PowerShell en lugar de CMD, o instala curl, o simplemente abre en el navegador:
```
http://localhost:3000/api/users
```

### El puerto 3000 está ocupado

Otro programa usa ese puerto. Cierra otras aplicaciones o reinicia.

---

## Checklist final

- [ ] `python3 --version` funciona
- [ ] Tengo el repositorio clonado
- [ ] `python3 api/server.py` arranca sin errores
