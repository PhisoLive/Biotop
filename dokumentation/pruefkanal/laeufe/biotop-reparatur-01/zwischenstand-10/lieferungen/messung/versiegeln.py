"""Prüft und versiegelt die eigene Lieferung; niemals Parent/Produktion."""
import ast
import hashlib
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

D = Path(__file__).resolve().parent
R = D.parent / 'repo'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

stats = json.loads((D / 'KENNZAHLEN.json').read_text())
for f in stats['dateien']:
    assert sha(D / 'dateien' / f['pfad']) == sha(R / f['pfad']) == f['sha256']
final = list(ET.parse(D / 'roh/31-final/junit.xml').getroot().iter('testcase'))
assert len(final) == stats['final_tests_mit_bestandsregeln']
assert not any(x.find(t) is not None for x in final for t in ['failure', 'error', 'skipped'])
names = [x.get('name') for x in final]
befunde = json.loads((D / 'BEFUNDE.json').read_text())
for b in befunde['lesestellen']:
    assert b['kernpfadbezug'] and b['grenzen']
    for n in b['negativtests'] + b['gegenroute']:
        assert any(x == n or x.startswith(n + '[') for x in names), (b['id'], n)
    for label in b['tdd']:
        assert (D / 'roh' / label / 'junit.xml').exists(), label

# Keine Mess-/Rausch-/Grenzkonstante verändert.
def constants(p):
    return {t.id: ast.dump(n.value, include_attributes=False)
            for n in ast.parse(p.read_text()).body if isinstance(n, ast.Assign)
            for t in n.targets if isinstance(t, ast.Name) and t.id.isupper() and t.id != 'MESSSKRIPT'}
assert constants(D / 'roh/messgeraet.original.py') == constants(R / 'biotop/kern/messgeraet.py')
image = subprocess.run(['docker', 'image', 'inspect', 'biotop-kammer:1', '--format', '{{.Id}}'], text=True, capture_output=True, check=True)
(D / 'VERIFIKATION.json').write_text(json.dumps({'liefermengen_und_testverweise_geprueft': True,
    'liefersourcen_identisch_zum_getesteten_stand': True, 'konstanten_unveraendert': True,
    'image_inspect': image.stdout.strip(), 'netz_und_modelle': 'nicht verwendet; Eigen-Tests sperren Socket-connect, Kammer network none',
    'final_tests': len(final), 'eigene_testfaelle': stats['eigene_testfaelle'],
    'gesamtpruefung_gruen': False, 'grund': 'offene Anpassung alter Setup-Gültigkeitsassertion, zwei nicht ausgeführte Privat-Replays; Parent macht vollständige Suite/CLI'}, indent=2) + '\n')
exclude = {'MANIFEST.json', 'DATEIEN.txt', 'SHA256SUMS', 'SHA256SUMS.sha256'}
paths = sorted(p for p in D.rglob('*') if p.is_file() and p.relative_to(D).as_posix() not in exclude and '__pycache__' not in p.parts)
manifest = [{'pfad': p.relative_to(D).as_posix(), 'bytes': p.stat().st_size, 'sha256': sha(p)} for p in paths]
(D / 'MANIFEST.json').write_text(json.dumps({'dateien': len(manifest), 'summe_bytes': sum(x['bytes'] for x in manifest),
    'nicht_selbst_enthalten': sorted(exclude), 'eintraege': manifest}, ensure_ascii=False, indent=2) + '\n')
(D / 'DATEIEN.txt').write_text('\n'.join(x['pfad'] for x in manifest) + '\nMANIFEST.json\nDATEIEN.txt\nSHA256SUMS\nSHA256SUMS.sha256\n')
checkpaths = paths + [D / 'MANIFEST.json', D / 'DATEIEN.txt']
(D / 'SHA256SUMS').write_text(''.join(sha(p) + '  ' + p.relative_to(D).as_posix() + '\n' for p in sorted(checkpaths)))
(D / 'SHA256SUMS.sha256').write_text(sha(D / 'SHA256SUMS') + '  SHA256SUMS\n')
# Lesevergleich aller transportierten Bytes gegen den erzeugten Hashsatz.
for line in (D / 'SHA256SUMS').read_text().splitlines():
    h, rel = line.split('  ', 1)
    assert sha(D / rel) == h, rel
print(json.dumps({'manifest_dateien': len(manifest), 'sha256sum_eintraege': len(checkpaths),
    'alle_hashes_geprueft': True, 'sha256sum_datei_sha256': sha(D / 'SHA256SUMS'),
    'bericht': str(D / 'LIEFERUNG.md'), 'gesamtpruefung_gruen': False}, indent=2))
