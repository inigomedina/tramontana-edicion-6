#!/usr/bin/env python3
import json
import sys
from collections import Counter

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 counter.py <campo>", file=sys.stderr)
        sys.exit(1)
    
    field = sys.argv[1]
    
    # Leer datos de stdin
    data = json.load(sys.stdin)
    
    # Contar ocurrencias
    counts = Counter(item.get(field, "unknown") for item in data)
    
    # Convertir a dict y ordenar
    sorted_counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
    
    # Imprimir como JSON
    print(json.dumps(sorted_counts, indent=2, ensure_ascii=False))
