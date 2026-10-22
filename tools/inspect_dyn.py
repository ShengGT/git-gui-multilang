#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""List mc calls in gitk whose argument is not a plain quoted literal."""
import io
import re
import sys

src = io.open(sys.argv[1], encoding='utf-8').read()
calls = re.findall(r'\bmc[ \t]+(\[[^\n]*|"[^"\n]{0,60})', src)
dyn = [c for c in calls if not c.startswith('"')]
print('total mc calls: %d, non-literal: %d' % (len(calls), len(dyn)))
for c in dyn:
    print(c[:80])
