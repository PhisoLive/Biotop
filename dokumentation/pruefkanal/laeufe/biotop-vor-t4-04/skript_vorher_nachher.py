"""Vorher/Nachher der Behebungsrunde 4 vor T4: dieselben Testfunktionen der Gruppen H, E3, E4, R4-5/6/13/14 aus
tests/test_vor_t4_04.py am Code des angegebenen Stands (git archive), echte Kammer wo der Test sie nutzt. Zweck: zeigen,
dass diese Fälle an 0aac612 (Runde 3) rot waren und am neuen Commit grün sind. Die Testdatei kommt aus dem NEUEN
Commit, der Code (biotop/) aus dem angegebenen Stand; Hilfsdateien der Tests (tests/*.py) ebenfalls aus dem NEUEN Commit.
Aufruf: python vorher_nachher.py <verzeichnis mit git archive> <kennung> <ausgabe.json>
Kein Modellaufruf."""
import json
import subprocess
import sys
import time
from pathlib import Path

CODE, KENNUNG, AUSGABE = Path(sys.argv[1]).resolve(), sys.argv[2], Path(sys.argv[3])
NEU = Path('/root/biotop')
assert (CODE / 'biotop' / 'organe' / 'aegis.py').is_file(), CODE
AUSWAHL = ('test_h1_ or test_h2_ or test_h3_ or test_h4_ or test_e3_ or test_e4_ or test_r45_ or test_r46_ or '
           'test_r413_ or test_r414_ or test_merkmale_')
# pytest im Code-Verzeichnis des Stands, Tests aus dem neuen Commit (kopiert, ohne pycache)
ziel_tests = CODE / 'tests_neu'
subprocess.run(['rm', '-rf', str(ziel_tests)], check=True)
subprocess.run(['cp', '-r', str(NEU / 'tests'), str(ziel_tests)], check=True)
subprocess.run(['find', str(ziel_tests), '-name', '__pycache__', '-prune', '-exec', 'rm', '-rf', '{}', '+'], check=False)
t0 = time.monotonic()
junit = AUSGABE.with_suffix('.junit.xml')
p = subprocess.run([sys.executable, '-m', 'pytest', str(ziel_tests / 'test_vor_t4_04.py'), '-k', AUSWAHL, '-q',
                    '-p', 'no:cacheprovider', '--tb=line', '--rootdir', str(CODE), f'--junitxml={junit}'],
                   cwd=str(CODE), capture_output=True, text=True,
                   env={**__import__('os').environ, 'PYTHONPATH': str(CODE), 'PYTHONDONTWRITEBYTECODE': '1'})
import xml.etree.ElementTree as ET  # noqa: E402
faelle = {}
for tc in ET.parse(junit).getroot().iter('testcase'):
    name = tc.get('name')
    f = tc.find('failure') if tc.find('failure') is not None else tc.find('error')
    s = tc.find('skipped')
    faelle[name] = ('rot: ' + (f.get('message') or '')[:300]) if f is not None else ('übersprungen' if s is not None else 'grün')
aus = {'stand': KENNUNG, 'code': str(CODE), 'tests_aus': subprocess.run(['git', '-C', str(NEU), 'rev-parse', '--short', 'HEAD'],
       capture_output=True, text=True).stdout.strip(), 'rc': p.returncode, 'dauer_s': round(time.monotonic() - t0, 1),
       'gruen': sum(v == 'grün' for v in faelle.values()), 'gesamt': len(faelle), 'faelle': faelle,
       'ende_stdout': p.stdout[-1500:]}
AUSGABE.write_text(json.dumps(aus, ensure_ascii=False, indent=1))
print(f"{KENNUNG}: {aus['gruen']} von {aus['gesamt']} grün (rc {p.returncode}, {aus['dauer_s']} s)")
for n, v in sorted(faelle.items()):
    print(f"  {n:90} {v[:160]}")
