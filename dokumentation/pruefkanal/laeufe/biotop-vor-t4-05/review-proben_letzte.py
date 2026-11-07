"""Nur lesend: letzte Nachrechnungen (Stufe-2-Dauer aus der jsonl, Nachspiel-Stempel, R6-Spezifikationen, T4-Diagnose)
und Stand für den Schreibort-Nachweis. Kein Kammerlauf."""
import json
import os
import statistics as st
import subprocess
from pathlib import Path

A = Path('/root/biotop-vor-t4-05')
R = A / 'REVIEW.md'
print('REVIEW.md vorhanden:', R.exists(), (os.path.getmtime(R) if R.exists() else ''))
z = [json.loads(l) for l in (A / 'proben/STUFE2-EICHUNG.jsonl').read_text().splitlines() if l.strip()]
print('jsonl zeilen', len(z))
for var in ('W60_ist', 'W240', 'W480'):
    zz = [x for x in z if x['variante'] == var]
    w = [v for x in zz for v in (x['werte']['eingang'] or [])]
    rel = [(max(x['werte']['eingang']) - min(x['werte']['eingang'])) / st.median(x['werte']['eingang']) for x in zz]
    print(f"{var}: messungen={len(zz)} werte={len(w)} median={st.median(w):.1f} spanne={min(w):.1f}..{max(w):.1f} "
          f"rel_spannweite={min(rel):.2f}..{max(rel):.2f} sperren={sum(1 for x in zz if 'eingang' in x['gesperrt'])}")
for b in ('zahlen', 'tarife', 'bericht', 'planung'):
    w = [v for x in z for v in (x['werte'][b] or [])]
    rel = [(max(x['werte'][b]) - min(x['werte'][b])) / st.median(x['werte'][b]) for x in z]
    print(f"{b}: messungen={len(z)} median={st.median(w):.1f} rel={min(rel):.2f}..{max(rel):.2f} "
          f"sperren={sum(1 for x in z if b in x['gesperrt'])}")
for d in ('n1', 'n2', 'n3'):
    for f in sorted((A / 'nachspiel' / d).glob('*.json')):
        j = json.loads(f.read_text())
        print(d, f.name, 'import', j.get('code_stand_beim_import'), 'nach', j.get('code_stand_nach_fall'))
for n in ('spez/SPEZ-R6-4.txt', 'spez/SPEZ-R6-LAUFWEG.txt', 'spez/SPEZ-R6-UNIT.txt', 'proben/VORPROBE-E2b.txt',
          'proben/T4-DIAGNOSE.txt', 'proben/STUFE2-EINGANG-DAUER.txt'):
    t = (A / n).read_text().splitlines()
    print('==', n, len(t), 'Zeilen')
    for zeile in (t[-4:] if n.startswith('spez') else t[:14]):
        print('  ', zeile[:230])
print('== __pycache__:', [str(p) for p in Path('/tmp/review-vor-t4-05').rglob('__pycache__')])
print('== fremde Einträge (nicht von mir):', sorted(p.name for p in Path('/tmp/review-vor-t4-05').iterdir()
                                                  if p.name in ('bericht_neu.sh', 'e2b', 'e2b_probe.py', 'e2b_probe.out.txt',
                                                                'review-vor-t4-05', '__pycache__')))
print('git status leer:', subprocess.run(['git', '-C', '/root/biotop', 'status', '--porcelain'], capture_output=True,
                                          text=True).stdout.strip() == '')
print('container:', subprocess.run(['docker', 'ps', '-q'], capture_output=True, text=True).stdout.split())
