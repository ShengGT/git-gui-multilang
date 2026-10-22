#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Derive Croatian (hr) from the Serbian Latin table, swapping the terms that differ."""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from po_tools import read

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANS = os.path.join(ROOT, 'gitk', 'translations')

# Ordered: multi-word forms first, then the individual terms.
SWAPS = [
    ('Komandna linija', 'Naredbeni redak'),
    ('komandna linija', 'naredbeni redak'),
    ('komande', 'naredbe'),
    ('komandu', 'naredbu'),
    ('komandi', 'naredbi'),
    ('komanda', 'naredba'),
    ('Komanda', 'Naredba'),
    ('komit', 'commit'),
    ('Komit', 'Commit'),
    ('spisak', 'popis'),
    ('Spisak', 'Popis'),
    ('pregledač', 'preglednik'),
    ('Pregledač', 'Preglednik'),
    ('sistem', 'sustav'),
    ('Sistem', 'Sustav'),
    ('tastaturi', 'tipkovnici'),
    ('tastature', 'tipkovnice'),
    ('tastatura', 'tipkovnica'),
    ('tačno', 'točno'),
    ('Tačno', 'Točno'),
    ('obriši', 'izbriši'),
    ('Obriši', 'Izbriši'),
    (' u toku', ' u tijeku'),
    ('deliti', 'dijeliti'),
    ('izabran', 'odabran'),
    ('Izabran', 'Odabran'),
    ('izaberi', 'odaberi'),
    ('Izaberi', 'Odaberi'),
]


def main():
    src = json.loads(read(os.path.join(TRANS, 'sr_latn.json')))
    out = {}
    for key, text in src.items():
        for old, new in SWAPS:
            text = text.replace(old, new)
        out[key] = text
    path = os.path.join(TRANS, 'hr.json')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(
        json.dumps(out, ensure_ascii=False, indent=0) + '\n')
    print('hr: %d entries' % len(out))


if __name__ == '__main__':
    main()
