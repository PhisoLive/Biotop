"""Veröffentlicht den Abschlussordner der Behebungsrunde 2 vor T4 und prüft jede Datei über HTTPS bytegleich.

Ein vorhandener Zielordner wird nie gelöscht oder überschrieben — Abbruch. Rechte root:caddy, Ordner 750, Dateien 640.
Nachspiel-Belege werden zu einer Datei gebündelt (je Originaldatei sha256, Größe, Inhalt). Skripte mit Endungen, die
der Server womöglich nicht als Text ausliefert (.sh, .mjs, .xml, .patch), bekommen „.txt“ angehängt.
"""
import hashlib
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

AKTE = Path('/etc/pruefkanal/schluessel').read_text().strip()
BASIS = 'laeufe/biotop-vor-t4-02'
ZIEL = Path(f'/var/pruefkanal/oeffentlich/_akte/{AKTE}/{BASIS}')
URL = f'https://milieulux-reinigung-muenchen.de/_akte/{AKTE}/{BASIS}'
A = Path('/root/biotop-vor-t4-02')
R = Path('/root/biotop')
T4 = Path('/root/biotop-t3/abschluss3/t4-vorbedingungen')

if ZIEL.exists():
    # Erlaubt sind nur die Unterordner, die der Zwischenbericht-Wächter dort anlegt; alles andere wären gelieferte Bytes.
    fremd = [p.name for p in ZIEL.iterdir() if not (p.is_dir() and p.name.startswith('zwischenbericht-'))]
    if fremd:
        raise SystemExit(f'{ZIEL} enthält schon gelieferte Dateien {fremd[:5]} — nichts wird überschrieben. Abbruch.')

QUELLEN = {
    'BERICHT.md': A / 'BERICHT.md',
    'REVIEW.md': A / 'REVIEW.md',
    'REVIEW-AUFTRAG.md': A / 'REVIEW-AUFTRAG.md',
    'KASSE.md': A / 'KASSE.md',
    'UEBERGABE.md': A / 'UEBERGABE.md',
    'KERN-COMMIT.patch.txt': A / 'KERN-COMMIT.patch.txt',
    'COMMIT-STAT.txt': A / 'COMMIT-STAT.txt',
    'COMMIT-NACHRICHT.txt': A / 'COMMIT-NACHRICHT.txt',
    'JOB-COMMIT-REGRESSION.txt': A / 'JOB-COMMIT-REGRESSION.txt',
    'skript_job_commit_regression.sh.txt': A / 'job_commit_regression.sh',
    'REGRESSION.txt': A / 'REGRESSION.txt',
    'REGRESSION.junit.xml.txt': A / 'REGRESSION.junit.xml',
    'VERDRAHTUNG-BELEG-REGRESSION.json': A / 'VERDRAHTUNG-BELEG-REGRESSION.json',
    'NACHSPIEL-D1.txt': A / 'NACHSPIEL-D1.txt',
    'NACHSPIEL-D2.txt': A / 'NACHSPIEL-D2.txt',
    'NACHSPIEL-D3.txt': A / 'NACHSPIEL-D3.txt',
    'skript_nachspiel_vor_t4.py': Path('/root/biotop-vor-t4/nachspiel_vor_t4.py'),
    'S1-STAENDE.json': A / 's1/S1-STAENDE.json',
    'S1-STAENDE.txt': A / 's1/S1-STAENDE.txt',
    'skript_s1_staende.py': A / 's1/s1_staende.py',
    'skript_s1_harness.mjs.txt': Path('/root/biotop-vor-t4/s1/s1_harness.mjs'),
    'DIAGNOSE-PY-SONDE.json': A / 'py/DIAGNOSE-PY-SONDE.json',
    'DIAGNOSE-PY-SONDE.txt': A / 'py/DIAGNOSE-PY-SONDE.txt',
    'skript_diagnose_py_sonde.py': A / 'py/diagnose_py_sonde.py',
    'PYTHON-LAUFZEIT-TEILAUSFALL.json': A / 'py/PYTHON-LAUFZEIT-TEILAUSFALL.json',
    'PYTHON-LAUFZEIT-TEILAUSFALL.txt': A / 'py/PYTHON-LAUFZEIT-TEILAUSFALL.txt',
    'skript_python_laufzeit_teilausfall.py': A / 'py/python_laufzeit_teilausfall.py',
    'SPERRE-OHNE-IMAGE.txt': A / 'sperre/OHNE-IMAGE.txt',
    'VORPRUEFUNG.txt': A / 'bau/VORPRUEFUNG.txt',
    'skript_vorpruefung.sh.txt': A / 'bau/vorpruefung.sh',
    'VV-KAMMERPROBE-arbeitsbaum.json': A / 'bau/VV-KAMMERPROBE-arbeitsbaum.json',
    'NACHSPIEL-VORAB-k2868.json': A / 'bau/nachspiel-vorab/k2868.json',
    'ERSTLAUF-ALLE-arbeitsbaum.txt': A / 'bau/ERSTLAUF-ALLE.txt',
    'TEILLAUF-2-arbeitsbaum.txt': A / 'bau/TEILLAUF-2.txt',
    'skript_bau_ts_seite.py': A / 'bau/ts_seite.py',
    'skript_bau_vv_umbau.py': A / 'bau/vv_umbau.py',
    'skript_bau_laufzeit_umbau.py': A / 'bau/laufzeit_umbau.py',
    'skript_bau_deckung_umbau.py': A / 'bau/deckung_umbau.py',
    'skript_bau_deckung_umbau_organ.py': A / 'bau/deckung_umbau_organ.py',
    'skript_bau_aufzeichner_haerten.py': A / 'bau/aufzeichner_haerten.py',
    'skript_diagnose_eichproben.py': A / 'bau/diagnose_eichproben.py',
    'verhalten_py.py': R / 'biotop/kern/py/verhalten.py',
    'verhaltensvergleich.py': R / 'biotop/organe/verhaltensvergleich.py',
    'test_vor_t4_02.py': R / 'tests/test_vor_t4_02.py',
    'speicherwerk.py': R / 'tests/speicherwerk.py',
    'skript_veroeffentlichen.py': A / 'veroeffentlichen.py',
    'spez_test_gewinnschwelle_nachmessung.py': A / 'spez/test_spez_gewinnschwelle_nachmessung.py',
    'SPEZ-GEWINNSCHWELLE-an-6243377.txt': A / 'spez/SPEZ-GEWINNSCHWELLE-an-6243377.txt',
    'SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md': A / 'SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md',
    'review_sondenprobe.py': A / 'review-proben/sondenprobe.py',
    'review_sondenprobe2.py': A / 'review-proben/sondenprobe2.py',
    'REVIEW-SONDENPROBE.txt': A / 'review-proben/SONDENPROBE.txt',
    'REVIEW-SONDENPROBE.json': A / 'review-proben/SONDENPROBE.json',
    'REVIEW-SONDENPROBE-2.txt': A / 'review-proben/SONDENPROBE-2.txt',
    'REVIEW-SONDENPROBE-2.json': A / 'review-proben/SONDENPROBE-2.json',
}
fehlend = [f'{n} ({q})' for n, q in QUELLEN.items() if not Path(q).is_file()]
if '‹' in (A / 'BERICHT.md').read_text():
    raise SystemExit('BERICHT.md enthält noch Platzhalter ‹…› — Abbruch')
if fehlend:
    raise SystemExit(f'Quellen fehlen: {fehlend}')

neu_angelegt = not ZIEL.exists()
ZIEL.mkdir(parents=True, exist_ok=True)
gelegt = {}
for name, quelle in QUELLEN.items():
    daten = Path(quelle).read_bytes()
    (ZIEL / name).write_bytes(daten)
    gelegt[name] = hashlib.sha256(daten).hexdigest()
buendel = {}
for ordner in ('nachspiel-d1', 'nachspiel-d2', 'nachspiel-d3'):
    for p in sorted((A / ordner).glob('*.json')):
        daten = p.read_bytes()
        buendel[f'{ordner}/{p.name}'] = {'sha256': hashlib.sha256(daten).hexdigest(), 'bytes': len(daten), 'inhalt': json.loads(daten)}
if len(buendel) != 7:
    raise SystemExit(f'Nachspielbelege: {len(buendel)} statt 7 (d1: 3, d2: 2, d3: 2) — Abbruch vor dem Veröffentlichen')
text = json.dumps(buendel, ensure_ascii=False, indent=1)
(ZIEL / 'NACHSPIEL-BELEGE.json').write_text(text)
gelegt['NACHSPIEL-BELEGE.json'] = hashlib.sha256(text.encode()).hexdigest()

zeilen = ['# Behebungsrunde 2 vor T4 — Abschlussordner, Stand 2026-09-24 (Kern-Commit 6243377)', '', 'Bericht:', f'{URL}/BERICHT.md', '',
          'Umbenennungen: *.sh.txt, *.mjs.txt, *.junit.xml.txt, KERN-COMMIT.patch.txt = Originaldateien mit angehängtem .txt; '
          'skript_* = Skripte aus dem Arbeitsordner; *-arbeitsbaum = Läufe vor dem Commit.',
          f'NACHSPIEL-BELEGE.json bündelt {len(buendel)} Nachspiel-Belege am Commit 6243377 (Durchgänge d1–d3; je Datei sha256, Größe, Inhalt).', '',
          'Jede Datei einzeln (volle Abholadresse, dahinter sha256):', '']
zeilen += [f'{URL}/{n}  {gelegt[n]}' for n in sorted(gelegt)]
(ZIEL / 'DATEIEN.txt').write_text('\n'.join(zeilen) + '\n')
gelegt['DATEIEN.txt'] = hashlib.sha256((ZIEL / 'DATEIEN.txt').read_bytes()).hexdigest()
manifest = ''.join(f'{h}  {n}\n' for n, h in sorted(gelegt.items()))
(ZIEL / 'MANIFEST.sha256').write_text(manifest)
ordner = hashlib.sha256(manifest.encode()).hexdigest()
(ZIEL / 'PRUEFSUMME-ORDNER.txt').write_text(ordner + '\n')
subprocess.run(['chown', 'root:caddy', str(ZIEL)], check=True)
subprocess.run(['chmod', '750', str(ZIEL)], check=True)
for name in list(gelegt) + ['MANIFEST.sha256', 'PRUEFSUMME-ORDNER.txt']:
    subprocess.run(['chown', 'root:caddy', str(ZIEL / name)], check=True)
    subprocess.run(['chmod', '640', str(ZIEL / name)], check=True)

bytegleich, fehler = 0, []
alle = sorted(gelegt) + ['MANIFEST.sha256', 'PRUEFSUMME-ORDNER.txt']
for name in alle:
    try:
        with urllib.request.urlopen(f'{URL}/{name}', timeout=60) as r:
            h = hashlib.sha256(r.read()).hexdigest()
        bytegleich += h == hashlib.sha256((ZIEL / name).read_bytes()).hexdigest()
        if h != hashlib.sha256((ZIEL / name).read_bytes()).hexdigest():
            fehler.append(f'{name}: HTTPS weicht ab')
    except Exception as e:
        fehler.append(f'{name}: {type(e).__name__} {e}')
try:
    with urllib.request.urlopen('https://milieulux-reinigung-muenchen.de/', timeout=60) as r:
        webseite = r.status
except Exception as e:
    webseite = f'{type(e).__name__} {e}'
print(json.dumps({'ordner': str(ZIEL), 'url': URL, 'dateien': len(alle), 'https_bytegleich': f'{bytegleich} von {len(alle)}',
                  'fehler': fehler[:10], 'ordnerpruefsumme': ordner, 'webseite_http': webseite}, ensure_ascii=False, indent=2))
sys.exit(0 if bytegleich == len(alle) else 1)
