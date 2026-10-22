#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dry-run test of install-all-languages.bat against a fake Git layout."""
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BAT = os.path.join(ROOT, 'install-all-languages.bat')

tmp = tempfile.mkdtemp(prefix='gitloc_')
gitroot = os.path.join(tmp, 'Git')
os.makedirs(os.path.join(gitroot, 'ucrt64', 'bin'))
os.makedirs(os.path.join(gitroot, 'ucrt64', 'share', 'git-gui', 'lib'))
io.open(os.path.join(gitroot, 'ucrt64', 'bin', 'gitk'), 'w').write('# fake gitk\n')
io.open(os.path.join(gitroot, 'ucrt64', 'share', 'git-gui', 'lib', 'about.tcl'), 'w').write('# fake\n')

shutil.copytree(os.path.join(ROOT, 'msgs'), os.path.join(tmp, 'msgs'))
shutil.copytree(os.path.join(ROOT, 'gitk', 'msgs'), os.path.join(tmp, 'gitk', 'msgs'))

src = io.open(BAT, encoding='utf-8').read()
src = re.sub(r'fltmc >nul 2>&1.*?exit /b 0\r?\n\)\r?\n', '', src, flags=re.S)
src = src.replace('pause', 'rem pause')
fake = os.path.join(tmp, 'test.bat')
io.open(fake, 'w', encoding='utf-8', newline='\r\n').write(src)

proc = subprocess.run(['cmd', '/c', fake, gitroot], capture_output=True, text=True,
                      encoding='mbcs', errors='replace')
print(proc.stdout)
print('--- stderr ---')
print(proc.stderr)
print('--- tree ---')
for base, dirs, files in os.walk(gitroot):
    rel = os.path.relpath(base, gitroot)
    print('%-60s %d files' % (rel, len(files)))
shutil.rmtree(tmp, ignore_errors=True)
