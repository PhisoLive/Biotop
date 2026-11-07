"""Zweite enge Nachbesserung: Skip-Zeuge, keine Phase-4-Änderungen."""
from pathlib import Path
import subprocess, shutil, hashlib, json
R = Path('/root/biotop')
P = Path('/root/reparatur-01')
O = P / 'nachbesserung-02'
O.mkdir(exist_ok=False)
files = sorted(set(f for f in subprocess.check_output(['git', '-C', str(R), 'ls-files', '--cached', '--others', '--exclude-standard', '-z']).decode().split('\0') if f))
assert not any(f.startswith('daten/') or Path(f).name.startswith('.env') for f in files)
manifest = {}
for f in files:
    p = R / f
    manifest[f] = {'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'size': p.stat().st_size, 'mtime_ns': p.stat().st_mtime_ns}
    z = O / 'repo' / f
    z.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(p, z)
(O / 'ELTERN-AUSGANG.json').write_text(json.dumps(manifest, indent=2)+'\n')
# Reviewerbelege bleiben versiegelt; Elternrepro bekommt einen eigenen Ordner.
S = P / 'review-02/pruefer-kern'
E = P / 'eltern-skip-repro'
E.mkdir(exist_ok=False)
(E / 'guard').mkdir()
(E / 'tmp').mkdir()
(E / 'elternbelege').mkdir()
code = (S / 'repro_skip_vertragszeuge.py').read_text()
code = code.replace("ROOT / 'arbeitskopie'", "Path('/root/biotop')").replace("str(ROOT/'arbeitskopie')", "'/root/biotop'")
code = code.replace("consumer_replay=dict(boundary=", "try:\n    qualitaet = vorspann._qualitaet(recorded)\nexcept ValueError as e:\n    qualitaet = {'gesperrt': True, 'grund': str(e)}\nconsumer_replay=dict(boundary=")
code = code.replace('quality=vorspann._qualitaet(recorded))', 'quality=qualitaet)')
code += "\nassert unit_row['pruefbar'] is False\nassert consumer_replay['battery_complete'] is False\nassert qualitaet.get('gesperrt') is True\n"
(E / 'repro_skip_vertragszeuge.py').write_text(code)
guard = (S / 'guard/sitecustomize.py').read_text().replace(str(S), str(E))
(E / 'guard/sitecustomize.py').write_text(guard)
shutil.copy2(S / 'elternbelege/48-gesamtsuite-kernabschluss-eichpaare.json', E / 'elternbelege/48-gesamtsuite-kernabschluss-eichpaare.json')
(O / 'GRENZE.json').write_text(json.dumps({'review_fix_zyklus': 2, 'befund': 'KERN-EICH4-SKIP', 'erlaubt': ['biotop/organe/aegis.py', 'biotop/organe/eichproben.py', 'tests/test_review_vertrag.py', 'tests/test_junit_zeugen.py'], 'phase4': 'unveraendert offen, nicht bearbeiten', 'abnahme': 'offen'}, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'fixrepo': str(O/'repo'), 'dateien': len(files), 'elternrepro': str(E)}, ensure_ascii=False))
