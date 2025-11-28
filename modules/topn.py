#!/usr/bin/env python3
"""
=============================================================================
MÓDULO: topn.py
Propósito: Contar n ocurrencias de mayor valor en los datos JSON
=============================================================================

Uso:

Interfaz:

Campos comunes:
=============================================================================
"""

import json
import sys
from collections import Counter

data  = json.load(sys.stdin)

sorted_counts = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
topnumber     = sys.argv[1]
sliced        = dict(list(sorted_counts.items())[:int(topnumber)])
tops          = json.dumps(sliced, indent=2, ensure_ascii=False)

print (tops)
