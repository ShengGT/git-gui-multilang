#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate the generated gitk .msg catalogs.

Checks that every catalog
  * parses as a list of ::msgcat::mcset lines,
  * covers every current gitk source string exactly once,
  * keeps printf placeholders and newline counts,
  * round-trips through the Tcl escaping used at build time.
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from po_tools import escape_tcl, read, unescape_tcl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'gitk', 'source_strings.json')
MSGS = os.path.join(ROOT, 'gitk', 'msgs')

LINE = re.compile(r'^(##)?::msgcat::mcset (\w+) "((?:[^"\\]|\\.)*)" "((?:[^"\\]|\\.)*)"$')
PLACEHOLDER = re.compile(r'%(?:\d+\$)?[sdif]')


def main():
    keys = json.loads(read(SRC))
    keep = set(keys)
    errors = []
    files = sorted(f for f in os.listdir(MSGS) if f.endswith('.msg'))
    for name in files:
        locale = name[:-4]
        seen = {}
        active = 0
        for lineno, line in enumerate(read(os.path.join(MSGS, name)).splitlines(), 1):
            if not line.strip() or line.startswith('#'):
                continue
            m = LINE.match(line)
            if not m:
                errors.append('%s:%d unparsable line: %r' % (name, lineno, line[:80]))
                continue
            commented, loc, src, tr = m.groups()
            if loc != locale:
                errors.append('%s:%d wrong locale %s' % (name, lineno, loc))
            src_v = unescape_tcl(src)
            tr_v = unescape_tcl(tr)
            if src_v not in keep:
                errors.append('%s:%d unknown source string %r' % (name, lineno, src_v[:60]))
            if src_v in seen:
                errors.append('%s:%d duplicate %r' % (name, lineno, src_v[:60]))
            seen[src_v] = tr_v
            if not commented:
                active += 1
                if PLACEHOLDER.findall(src_v) != PLACEHOLDER.findall(tr_v):
                    errors.append('%s:%d placeholder mismatch %r -> %r' % (name, lineno, src_v, tr_v))
                if src_v.count('\n') != tr_v.count('\n'):
                    errors.append('%s:%d newline mismatch %r -> %r' % (name, lineno, src_v, tr_v))
                if escape_tcl(tr_v) != tr or escape_tcl(src_v) != src:
                    errors.append('%s:%d escaping not canonical %r' % (name, lineno, src_v[:60]))
        missing = [k for k in keys if k not in seen]
        if missing and active > 0:
            errors.append('%s missing %d source strings, e.g. %r' % (name, len(missing), missing[0]))
        print('%-8s lines=%3d active=%3d' % (locale, len(seen), active))
    print('\n%d catalogs checked, %d problem(s)' % (len(files), len(errors)))
    for e in errors[:40]:
        print('  ' + e)
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
