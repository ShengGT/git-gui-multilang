#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create an empty (or variant-copied) translation table for every known locale."""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from po_tools import read

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANS = os.path.join(ROOT, 'gitk', 'translations')
META = json.loads(read(os.path.join(ROOT, 'languages.json')))['locales']

for entry in META:
    loc = entry['locale']
    path = os.path.join(TRANS, loc + '.json')
    if os.path.exists(path):
        continue
    variant = entry.get('variantOf')
    if variant:
        src = os.path.join(TRANS, variant + '.json')
        if os.path.exists(src):
            io.open(path, 'w', encoding='utf-8', newline='\n').write(read(src))
            print('%-9s copied from %s' % (loc, variant))
            continue
    io.open(path, 'w', encoding='utf-8', newline='\n').write('{}')
    print('%-9s empty table created' % loc)
