#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Derive zh_tw / zh_sg from the authored zh_cn table using OpenCC."""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from po_tools import read

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANS = os.path.join(ROOT, 'gitk', 'translations')


def convert(config, src, dst):
    from opencc import OpenCC
    cc = OpenCC(config) if config != 'none' else None
    table = json.loads(read(os.path.join(TRANS, src + '.json')))
    out = {k: (cc.convert(v) if (cc and v) else v) for k, v in table.items()}
    io.open(os.path.join(TRANS, dst + '.json'), 'w', encoding='utf-8', newline='\n').write(
        json.dumps(out, ensure_ascii=False, indent=0))
    print('%s -> %s (%s): %d entries' % (src, dst, config, len(out)))


if __name__ == '__main__':
    convert('s2twp', 'zh_cn', 'zh_tw')
    convert('s2tw', 'zh_tw', 'zh_hk')
    # Singapore uses Simplified Chinese; reuse the authored zh_cn table.
    convert('none', 'zh_cn', 'zh_sg')
