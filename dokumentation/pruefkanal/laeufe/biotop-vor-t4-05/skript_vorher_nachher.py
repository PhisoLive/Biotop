"""Vorher/Nachher (Behebungsrunde 5): dieselben neuen Testfälle (tests/test_vor_t4_05.py aus dem neuen Commit) am Code von
43b8fad und am Code von HEAD — beide aus `git archive`, die Tests jeweils aus HEAD (dazu die Hilfsdateien, die die neuen
Tests importieren). Ein Fall, der an 43b8fad fehlt (Schnittstelle), ist als solcher gekennzeichnet — kein
Verhaltensnachweis. Aufruf: python vorher_nachher.py <ausgabeordner>"""
import json
import os
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

AUS = Path(sys.argv[1])
R = Path('/root/biotop')
PY = '/root/biotop-t3/venv/bin/python'
HEAD = subprocess.run(['git', '-C', str(R), 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
TESTS = ['tests/test_vor_t4_05.py', 'tests/test_vor_t4_03.py', 'tests/test_vorspann.py', 'tests/conftest.py']


def stand(commit, name):
    d = Path(tempfile.mkdtemp(prefix=f'biotop-{name}-', dir='/tmp'))
    subprocess.run(f'git -C {R} archive {commit} | tar -x -C {d}', shell=True, check=True)
    for t in TESTS:
        (d / t).write_text(subprocess.run(['git', '-C', str(R), 'show', f'HEAD:{t}'], capture_output=True, text=True,
                                          check=True).stdout)
    xml = AUS / f'{name}.junit.xml'
    env = {**os.environ, 'BIOTOP_KAMMER_IMAGE': 'biotop-kammer:ts1', 'BIOTOP_AUFTRAG_LAUF_AB': '26',
           'BIOTOP_AUFTRAG_BUDGET_EUR': '10', 'TMPDIR': '/tmp'}
    p = subprocess.run([PY, '-m', 'pytest', 'tests/test_vor_t4_05.py', '-q', '-p', 'no:cacheprovider', '--tb=line',
                        f'--junitxml={xml}'], cwd=d, capture_output=True, text=True, env=env)
    faelle = {}
    for tc in ET.parse(xml).getroot().iter('testcase'):
        f = tc.find('failure') if tc.find('failure') is not None else tc.find('error')
        faelle[tc.get('name')] = 'grün' if f is None and tc.find('skipped') is None else \
            ('übersprungen' if tc.find('skipped') is not None else 'rot: ' + (f.get('message') or '')[:220].replace('\n', ' '))
    gruen = sum(1 for v in faelle.values() if v == 'grün')
    zeilen = [f'{commit} ({name}): {gruen} von {len(faelle)} grün (rc {p.returncode})']
    zeilen += [f'  {k:95} {v}' for k, v in sorted(faelle.items())]
    (AUS / f'{name}.txt').write_text('\n'.join(zeilen) + '\n')
    (AUS / f'{name}.json').write_text(json.dumps({'commit': commit, 'faelle': faelle, 'gruen': gruen, 'n': len(faelle),
                                                  'rc': p.returncode}, ensure_ascii=False, indent=1))
    print(zeilen[0], flush=True)


AUS.mkdir(parents=True, exist_ok=True)
stand('43b8fad', 'VORHER-43b8fad')
stand(HEAD, 'NACHHER-HEAD')
