#!/usr/bin/env python3
import json
import sys
from datetime import datetime

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 report.py <titulo>", file=sys.stderr)
        sys.exit(1)
    
    title = sys.argv[1]
    
    # Leer datos de stdin
    data = json.load(sys.stdin)
    
    # Calcular total
    total = sum(data.values())
    
    # Generar reporte
    print(f"# {title}")
    print(f"\n**Fecha:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"\n**Total de eventos:** {total}")
    print(f"\n## Resumen de Features\n")
    
    for feature, count in data.items():
        percentage = (count / total * 100)
        print(f"- **{feature}**: {count} eventos ({percentage:.1f}%)")
