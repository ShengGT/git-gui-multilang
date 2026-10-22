#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Helper utilities for the gitk / git-gui msgs pipeline."""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(path):
    # utf-8-sig tolerates a BOM, which Windows editors like to add.
    return io.open(path, encoding='utf-8-sig').read()


def unescape_tcl(s):
    """Turn a Tcl double-quoted literal body into its real value."""
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c != '\\':
            out.append(c)
            i += 1
            continue
        i += 1
        if i >= len(s):
            out.append('\\')
            break
        e = s[i]
        simple = {'n': '\n', 't': '\t', 'r': '\r', 'a': '\a', 'b': '\b',
                  'f': '\f', 'v': '\v', '\\': '\\', '"': '"', '$': '$', '[': '['}
        if e in simple:
            out.append(simple[e])
            i += 1
        elif e == 'u' and i + 4 < len(s):
            out.append(chr(int(s[i + 1:i + 5], 16)))
            i += 5
        elif e == 'x' and i + 2 < len(s):
            out.append(chr(int(s[i + 1:i + 3], 16)))
            i += 3
        elif e.isdigit():
            j = i
            while j < len(s) and j < i + 3 and s[j].isdigit():
                j += 1
            out.append(chr(int(s[i:j], 8)))
            i = j
        else:
            out.append(e)
            i += 1
    return ''.join(out)


def escape_tcl(s):
    out = []
    for ch in s:
        if ch == '\\':
            out.append('\\\\')
        elif ch == '"':
            out.append('\\"')
        elif ch == '\n':
            out.append('\\n')
        elif ch == '\t':
            out.append('\\t')
        elif ch == '\r':
            out.append('\\r')
        elif ch == '$':
            out.append('\\$')
        elif ch == '[':
            out.append('\\[')
        elif ch == ']':
            out.append('\\]')
        else:
            out.append(ch)
    return ''.join(out)


def extract_gitk(path):
    src = read(path)
    keys = []
    seen = set()
    for m in re.finditer(r'\bmc\s+"((?:[^"\\]|\\.)*)"', src):
        val = unescape_tcl(m.group(1))
        if val not in seen:
            seen.add(val)
            keys.append(val)
    return keys


def parse_msg(path):
    """Return ordered dict english -> translation from a .msg file."""
    pairs = []
    for m in re.finditer(r'^::msgcat::mcset [\w@]+ "((?:[^"\\]|\\.)*)" "((?:[^"\\]|\\.)*)"',
                         read(path), re.M):
        pairs.append((unescape_tcl(m.group(1)), unescape_tcl(m.group(2))))
    return pairs


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'help'
    if cmd == 'extract':
        src = sys.argv[2]
        out = sys.argv[3]
        keys = extract_gitk(src)
        io.open(out, 'w', encoding='utf-8', newline='\n').write(
            json.dumps(keys, ensure_ascii=False, indent=1))
        print('extracted %d unique keys -> %s' % (len(keys), out))
    elif cmd == 'overlap':
        gitk_keys = json.loads(read(sys.argv[2]))
        gui = parse_msg(sys.argv[3])
        gk = [k for k, _ in gui]
        ov = [k for k in gitk_keys if k in gk]
        print('gitk keys: %d, gui keys: %d, exact overlap: %d' % (len(gitk_keys), len(gk), len(ov)))
        gd = dict(gui)
        for k in ov[:200]:
            print('  %-50s | %s' % (k.replace('\n', '\\n')[:50], gd[k].replace('\n', '\\n')[:40]))
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
