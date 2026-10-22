#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compare an existing gitk .msg against the current gitk source strings."""
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from po_tools import read, parse_msg

keys = json.loads(read(sys.argv[1]))
old = dict(parse_msg(sys.argv[2]))
missing = [k for k in keys if k not in old]
stale = [k for k in old if k not in keys]
print('source: %d  msg: %d  missing: %d  stale: %d' % (len(keys), len(old), len(missing), len(stale)))
print('--- MISSING ---')
for k in missing:
    print(repr(k))
print('--- STALE ---')
for k in stale:
    print(repr(k))
