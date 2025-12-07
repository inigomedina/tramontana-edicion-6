#!/usr/bin/env python3
import json
import sys

def filter_data(data, field, value):
    """Filtra un array JSON por campo y valor"""
    return [item for item in data if item.get(field) == value]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 filter.py <campo> <valor>", file=sys.stderr)
        sys.exit(1)
    
    field = sys.argv[1]
    value = sys.argv[2]
    
    data = json.load(sys.stdin)
    filtered = filter_data(data, field, value)
    
    print(json.dumps(filtered, indent=2))