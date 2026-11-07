"""Erzeugt die lokale Lieferung ausschließlich aus eigener Kopie/Rohbelegen."""
import ast
import base64
from collections import Counter
import difflib
import hashlib
import json
from pathlib import Path
import shutil
import xml.etree.ElementTree as ET
import zlib

D = Path(__file__).resolve().parent
R = D.parent / "repo"
Q = Path('/root/reparatur-01/nachweis-leserpruefung-02')

def jwrite(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def junit(path):
    return [{"klasse": x.get('classname'), "name": x.get('name'),
             "status": 'failure' if x.find('failure') is not None else 'error' if x.find('error') is not None else 'skipped' if x.find('skipped') is not None else 'passed'}
            for x in ET.parse(path).getroot().iter('testcase')]

# Es wird nicht gegen irgendeine Eltern-/Produktionsdatei verglichen.
original = D / 'roh/messgeraet.original.py'
q = json.loads((Q / 'QUELLEN.json').read_text())
assert sha(original) == next(x['sha256'] for x in q if x['pfad'] == 'biotop/kern/messgeraet.py')
rows = [{"pfad": x['pfad'], "soll_sha256": x['sha256'], "ist_sha256": sha(R / x['pfad'])} for x in q]
changed = [x['pfad'] for x in rows if x['soll_sha256'] != x['ist_sha256']]
assert changed == ['biotop/kern/messgeraet.py'], changed
jwrite(D / 'roh/quellen-nachher.json', rows)
for name in ['AUFTRAGGEBER-WORTLAUT.txt', 'FASSUNG-7-SATZ.json', 'QUELLEN.json']:
    (D / 'auftrag').mkdir(exist_ok=True)
    shutil.copy2(Q / name, D / 'auftrag' / name)
hits = [x for x in json.loads((Q / 'SUCHTREFFER.json').read_text()) if x['pfad'] == 'biotop/kern/messgeraet.py']
jwrite(D / 'roh/SUCHTREFFER-messgeraet.json', hits)

files = ['biotop/kern/messgeraet.py', 'tests/test_messnachweise.py']
diffs = []
for name in files:
    target = D / 'dateien' / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(R / name, target)
    before = original.read_text().splitlines(keepends=True) if name.startswith('biotop/') else []
    diffs.extend(difflib.unified_diff(before, target.read_text().splitlines(keepends=True), fromfile='a/' + name if before else '/dev/null', tofile='b/' + name))
(D / 'AENDERUNGEN.diff').write_text(''.join(diffs))
mod = ast.parse((R / files[0]).read_text())
script = next(ast.literal_eval(n.value) for n in mod.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'MESSSKRIPT' for t in n.targets))
compile(script, '<MESSSKRIPT>', 'exec')
compile((R / files[1]).read_text(), files[1], 'exec')

versuche = []
for f in sorted((D / 'roh').glob('*/lauf.json')):
    lauf = json.loads(f.read_text())
    actual_original = 'original_plugin' in lauf['befehl']
    lauf['ausgefuehrtes_messmodul'] = 'roh/messgeraet.original.py' if actual_original else str(f.parent.relative_to(D) / files[0])
    lauf['ausgefuehrtes_modul_sha256'] = sha(original) if actual_original else lauf['sha256'][files[0]]
    lauf['hinweis_repository_hash'] = 'sha256 im ursprünglichen lauf.json ist der Repository-Zustand, nicht bei original_plugin das ausgeführte Ausgangsmodul'
    counters = f.parent / 'kammer-gesamt'
    if not counters.exists():
        counters = f.parent / 'kammer'
    records = [json.loads(p.read_text()) for p in counters.glob('*.json')]
    n = sum(len(r['kammer']) for r in records)
    assert n == lauf['kammerlaeufe'], (f, n, lauf['kammerlaeufe'])
    lauf['rohzaehler_dateien'] = len(records)
    lauf['zaehlungsquelle'] = str(counters.relative_to(D))
    lauf['junit'] = str((f.parent / 'junit.xml').relative_to(D))
    lauf['junit_auszaehlung'] = dict(Counter(x['status'] for x in junit(f.parent / 'junit.xml')))
    if lauf['label'] == '05-junit-red':
        lauf['belegluecke'] = 'Zu langer parametrisierter Dateiname im eigenen Teardown-Archivierer: 8 Testaufrufe liefen bis zum Ergebnis, nur 7 vollständige Kammer-Rohdatensätze archiviert. Der 8. Lauf ist aus JUnit/Traceback ableitbar, sein vollständiger Kammerzähler nicht mehr vorhanden. Nicht als gemessenen Rohzähler addiert. Vor Produktänderung als 06-junit-red-korrigiert wiederholt.'
    if lauf['label'] == '02-skip-green':
        lauf['harnessfehler'] = 'Eigene Assertion verwechselte äußeres rc mit innerem pytest_rc. Produktfix zurückgenommen, Assertion auf inneres rc korrigiert, erneutes echtes Rot in 03 und Grün in 04.'
    versuche.append(lauf)
jwrite(D / 'VERSUCHE.json', versuche)

# Letzter Stand pro eigener Node-ID; Original-Replay mit ergänzenden Gutpaaren.
final = [x for x in junit(D / 'roh/31-final/junit.xml') if x['klasse'].endswith('test_messnachweise')]
original_cases = junit(D / 'roh/28-original-replay/junit.xml') + junit(D / 'roh/30-original-gutpaare/junit.xml')
o = {x['name']: x for x in original_cases}
assert len(o) == len(final) == 60
assert set(o) == {x['name'] for x in final}
assert all(x['status'] == 'passed' for x in final)

def evidence(label):
    return {json.loads(f.read_text())['nodeid'].split('::', 1)[1]: str(f.relative_to(D)) for f in (D / 'roh' / label / 'kammer').glob('*.json')}
orig_ev = {**evidence('28-original-replay'), **evidence('30-original-gutpaare')}
final_ev = evidence('31-final')
cases = []
for x in final:
    cases.append({**x, 'original_status': o[x['name']]['status'], 'original_roh': orig_ev.get(x['name']), 'final_roh': final_ev.get(x['name']),
                  'ausfuehrung': 'echte Kammer' if x['name'] in final_ev else 'Unit-Übergabe an Originalfunktionen; kein Kammerlauf'})
jwrite(D / 'EIGENTESTS.json', cases)

# Komprimierter Belegtransport wird für die großen JUnit-Dateien lesbar beigelegt.
unpacked = []
for label in ['25-liste-red', '26-liste-green', '28-original-replay', '31-final']:
    for f in (D / 'roh' / label / 'kammer').glob('*.json'):
        for i, k in enumerate(json.loads(f.read_text())['kammer']):
            for line in k['stdout'].splitlines():
                if line.startswith('@@ROHDATEI@@') and ':<zlib-base64>' in line:
                    name, encoded = line[len('@@ROHDATEI@@'):].split(':<zlib-base64>', 1)
                    content = zlib.decompress(base64.b64decode(encoded))
                    dest = D / 'roh/ausgepackt' / label / f.stem / (str(i) + '-' + Path(name).name)
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(content)
                    unpacked.append({'quelle': str(f.relative_to(D)), 'ziel': str(dest.relative_to(D)), 'sha256': sha(dest)})
jwrite(D / 'roh/AUSGEPACKT.json', unpacked)

stats = {
    'eigene_testfaelle': len(final), 'eigene_bestanden': sum(x['status'] == 'passed' for x in final),
    'original_bestanden': sum(x['status'] == 'passed' for x in o.values()),
    'original_fehlgeschlagen': sum(x['status'] == 'failure' for x in o.values()),
    'eigene_echte_kammerfaelle': len(final_ev), 'final_tests_mit_bestandsregeln': len(junit(D / 'roh/31-final/junit.xml')),
    'versuche': len(versuche), 'archivierte_echte_kammeraufrufe': sum(x['kammerlaeufe'] for x in versuche),
    'abgeleiteter_weiterer_lauf_ohne_vollstaendigen_rohzaehler': 1,
    'modellaufrufe': 0, 'modellkosten_eur': 0,
    'quellen_vorher_abgeglichen': len(rows), 'unveraenderte_inventarisierte_dateien': len(rows) - len(changed),
    'geaenderte_vorhandene_dateien': changed, 'neue_repodateien': ['tests/test_messnachweise.py'],
    'suchtreffer_zieldatei': len(hits), 'befundzeilen': len(json.loads((D / 'BEFUNDE.json').read_text())['lesestellen']),
    'dateien': [{'pfad': f, 'sha256': sha(R / f), 'bytes': (R / f).stat().st_size} for f in files]
}
jwrite(D / 'KENNZAHLEN.json', stats)
(D / 'KOSTEN.md').write_text('# Ausführungskosten und Grenzen\n\n' +
    f"- {stats['versuche']} erhaltene lokale pytest-Versuche.\n- {stats['archivierte_echte_kammeraufrufe']} echte, vollständig archivierte Kammer-Aufrufdatensätze (keine Hochrechnung, keine Doppelzählung der verschachtelten Zähler).\n" +
    '- Zusätzlich ein aus Testausgabe ableitbarer Lauf ohne vollständigen archivierten Rohzähler in Versuch 05; nicht stillschweigend zu den Rohzählungen addiert.\n' +
    '- 0 Modellaufrufe / 0 EUR Modellkosten: kein Anbieterpfad benutzt, Python-Netz in Eigen-Tests gesperrt, Container --network none. Keine Installation/kein Image-Neubau. Keine Gesamtrechnung für Host-/Docker-Ressourcen erhoben.\n')
print(json.dumps(stats, indent=2, ensure_ascii=False))
