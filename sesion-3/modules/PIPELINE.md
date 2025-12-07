# Pipeline - Reto B: Feature Health

## Reto elegido
Identificar features con poco uso que podrían necesitar mejora o deprecarse.

## Módulos implementados
1. `filter.py` - Filtrar datos por campo y valor
2. `topn.py` - Extraer los N elementos con mayor conteo
3. `report.py` - Generar reporte en Markdown

## Pipeline completo
```bash
# Paso 1: Obtener datos de eventos
python3 fetch.py events > events.json

# Paso 2: Contar features
cat events.json | python3 counter.py feature > feature_counts.json

# Paso 3: Generar reporte
cat feature_counts.json | python3 report.py "Análisis de Features" > reporte_features.md
```

## Resultado
Ver `reporte_features.md` para el análisis completo.
