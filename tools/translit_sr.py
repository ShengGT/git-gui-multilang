#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build sr_latn.json from sr.json with the official Serbian Cyrillic->Latin map."""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from po_tools import read

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANS = os.path.join(ROOT, 'gitk', 'translations')

DIGRAPHS = {'љ': 'lj', 'њ': 'nj', 'џ': 'dž'}
SINGLE = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'ђ': 'đ', 'е': 'e',
    'ж': 'ž', 'з': 'z', 'и': 'i', 'ј': 'j', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'ћ': 'ć',
    'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č', 'ш': 'š',
}


def convert(text):
    out = []
    for i, ch in enumerate(text):
        low = ch.lower()
        # A digraph is capitalised when it starts a word or the whole word is caps.
        upper = ch.isupper()
        if low in DIGRAPHS:
            lat = DIGRAPHS[low]
            prev = text[i - 1] if i else ''
            nxt = text[i + 1] if i + 1 < len(text) else ''
            if upper:
                lat = lat[0].upper() + lat[1:]
            out.append(lat)
        elif low in SINGLE:
            lat = SINGLE[low]
            out.append(lat.upper() if upper else lat)
        else:
            out.append(ch)
    return ''.join(out)


def main():
    src = json.loads(read(os.path.join(TRANS, 'sr.json')))
    out = {k: convert(v) for k, v in src.items()}
    io.open(os.path.join(TRANS, 'sr_latn.json'), 'w', encoding='utf-8', newline='\n').write(
        json.dumps(out, ensure_ascii=False, indent=0).replace('\n', '\n') + '\n')
    print('sr_latn: %d entries' % len(out))


if __name__ == '__main__':
    main()
