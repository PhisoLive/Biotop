"""Veröffentlicht den Abschlussordner der Behebungsrunde 3 vor T4 und prüft jede Datei über HTTPS bytegleich.

Ein vorhandener Zielordner wird nie gelöscht oder überschrieben — Abbruch. Rechte root:caddy, Ordner 750, Dateien 640.
Nachspiel-Belege werden zu einer Datei gebündelt (je Originaldatei sha256, Größe, Inhalt). Skripte mit Endungen, die
der Server womöglich nicht als Text ausliefert (.sh, .mjs, .xml, .patch), bekommen „.txt“ angehängt.
(Übernommen aus laeufe/biotop-vor-t4-02/skript_veroeffentlichen.py; geändert: Quellenliste, Nachspielbündel 10 statt 7,
Gutachterproben der Runde 3 per Verzeichnis.)
"""
import hashlib
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

AKTE = Path('/etc/pruefkanal/schluessel').read_text().strip()
BASIS = 'laeufe/biotop-vor-t4-03'
ZIEL = Path(f'/var/pruefkanal/oeffentlich/_akte/{AKTE}/{BASIS}')
URL = f'https://milieulux-reinigung-muenchen.de/_akte/{AKTE}/{BASIS}'
A = Path('/root/biotop-vor-t4-03')
R = Path('/root/biotop')
KOMMIT = subprocess.run(['git', '-C', str(R), 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()

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
    'NACHSPIEL-D1.txt': A / 'nachspiel/NACHSPIEL-D1.txt',
    'NACHSPIEL-D2.txt': A / 'nachspiel/NACHSPIEL-D2.txt',
    'NACHSPIEL-D3.txt': A / 'nachspiel/NACHSPIEL-D3.txt',
    'skript_nachspiel_vor_t4_03.py': A / 'nachspiel/nachspiel_vor_t4_03.py',
    'RISSPROBE-ECHT.txt': A / 'proben/RISSPROBE-ECHT.txt',
    'RISSPROBE-ECHT.json': A / 'proben/RISSPROBE-ECHT.json',
    'skript_rissprobe_echt.py': A / 'proben/rissprobe_echt.py',
    'GEGENZEUGEN-DOPPELT-am-commit.txt': A / 's1/GEGENZEUGEN-DOPPELT-am-commit.txt',
    'GEGENZEUGEN-DOPPELT.json': A / 's1/GEGENZEUGEN-DOPPELT.json',
    'GEGENZEUGEN-DOPPELT-arbeitsbaum.txt': A / 's1/GEGENZEUGEN-DOPPELT.txt',
    'skript_gegenzeugen_doppelt.py': A / 's1/gegenzeugen_doppelt.py',
    'skript_s1_harness.mjs.txt': Path('/root/biotop-vor-t4/s1/s1_harness.mjs'),
    'SPEZ-GEWINNSCHWELLE-am-arbeitsbaum.txt': A / 'spez/SPEZ-GEWINNSCHWELLE-am-arbeitsbaum.txt',
    'spez_test_gewinnschwelle_nachmessung.py': A / 'spez/test_spez_gewinnschwelle_nachmessung.py',
    'TEILLAUF-1-arbeitsbaum.txt': A / 'bau/TEILLAUF-1.txt',
    'TEILLAUF-2-arbeitsbaum.txt': A / 'bau/TEILLAUF-2.txt',
    'TEILLAUF-3-arbeitsbaum.txt': A / 'bau/TEILLAUF-3.txt',
    'TEILLAUF-4-arbeitsbaum.txt': A / 'bau/TEILLAUF-4.txt',
    'TEILLAUF-5-arbeitsbaum.txt': A / 'bau/TEILLAUF-5.txt',
    'DIAGNOSE-PROBEWERK-arbeitsbaum.txt': A / 'bau/DIAGNOSE-PROBEWERK.txt',
    'skript_diagnose_probewerk.py': A / 'bau/diagnose_probewerk.py',
    'verhalten_py.py': R / 'biotop/kern/py/verhalten.py',
    'verhaltensvergleich.py': R / 'biotop/organe/verhaltensvergleich.py',
    'gegenzeugen.py': R / 'biotop/kern/gegenzeugen.py',
    'einwickeln.mjs.txt': R / 'biotop/kern/ts/einwickeln.mjs',
    'test_vor_t4_03.py': R / 'tests/test_vor_t4_03.py',
    'skript_veroeffentlichen.py': A / 'veroeffentlichen.py',
    'SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md': A / 'SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md',
    'SPERRE-KOPIE-GUTACHTERPROBEN.txt': A / 'sperre/SPERRE-KOPIE-GUTACHTERPROBEN.txt',
    'SPERRE-2-BERICHT-ABSCHLUSS.txt': A / 'sperre/SPERRE-2-BERICHT-ABSCHLUSS.txt',
    'skript_bericht_abschluss_gesperrt.py': A / 'bau/bericht_abschluss_gesperrt.py',
    'skript_abschluss_1_bericht.py': A / 'bau/abschluss_1_bericht.py',
    'VORHER-6243377.txt': A / 'proben/VORHER-6243377.txt',
    'NACHHER-HEAD.txt': A / 'proben/NACHHER-HEAD.txt',
    'NACHHER-HEAD.json': A / 'proben/NACHHER-HEAD.json',
    'skript_nachher_head.py': A / 'proben/nachher_head.py',
    'COMMIT-NACHRICHT-2.txt': A / 'COMMIT-NACHRICHT-2.txt',
    'COMMIT-2-STAT.txt': A / 'COMMIT-2-STAT.txt',
    'KERN-COMMIT-2.patch.txt': A / 'KERN-COMMIT-2.patch.txt',
    'JOB-NACHTRAG.txt': A / 'JOB-NACHTRAG.txt',
    'skript_job_commit_regression_nachtrag.sh.txt': A / 'job_commit_regression_nachtrag.sh',
    'REGRESSION-2.txt': A / 'REGRESSION-2.txt',
    'REGRESSION-2.junit.xml.txt': A / 'REGRESSION-2.junit.xml',
    'VERDRAHTUNG-BELEG-REGRESSION-2.json': A / 'VERDRAHTUNG-BELEG-REGRESSION-2.json',
    'VORHER-6243377.json': A / 'proben/VORHER-6243377.json',
    'skript_vorher_6243377.py': A / 'proben/vorher_6243377.py',
    'KETTE.txt': A / 'bau/KETTE.txt',
    'skript_kette.sh.txt': A / 'bau/kette.sh',
    'skript_rauchprobe_sonde.py': A / 'bau/rauchprobe_sonde.py',
    'skript_rauchprobe_ts.py': A / 'bau/rauchprobe_ts.py',
}
for p in sorted(A.glob('bau/TEILLAUF-[6-9].txt')):
    QUELLEN[f'{p.stem}-arbeitsbaum.txt'] = p
# Proben des Gutachtens Runde 3 (vom Prüfer unter /tmp/review-vor-t4-03/ geschrieben, unverändert hierher kopiert)
for p in sorted((A / 'review-proben').glob('*')) if (A / 'review-proben').is_dir() else []:
    if p.is_file() and p.suffix in ('.py', '.txt', '.json', '.md', '.sh', '.mjs'):
        QUELLEN['review_' + p.name + ('.txt' if p.suffix in ('.sh', '.mjs') else '')] = p
fehlend = [f'{n} ({q})' for n, q in QUELLEN.items() if not Path(q).is_file()]
if '‹' in (A / 'BERICHT.md').read_text():
    raise SystemExit('BERICHT.md enthält noch Platzhalter ‹…› — Abbruch')
if fehlend:
    raise SystemExit(f'Quellen fehlen: {fehlend}')

buendel = {}
for ordner in ('d1', 'd2', 'd3'):
    for p in sorted((A / 'nachspiel' / ordner).glob('*.json')):
        daten = p.read_bytes()
        buendel[f'nachspiel/{ordner}/{p.name}'] = {'sha256': hashlib.sha256(daten).hexdigest(), 'bytes': len(daten),
                                                   'inhalt': json.loads(daten)}
if len(buendel) != 10:
    raise SystemExit(f'Nachspielbelege: {len(buendel)} statt 10 (d1: 6, d2: 2, d3: 2) — Abbruch vor dem Veröffentlichen')

neu_angelegt = not ZIEL.exists()
ZIEL.mkdir(parents=True, exist_ok=True)
gelegt = {}
for name, quelle in QUELLEN.items():
    daten = Path(quelle).read_bytes()
    (ZIEL / name).write_bytes(daten)
    gelegt[name] = hashlib.sha256(daten).hexdigest()
text = json.dumps(buendel, ensure_ascii=False, indent=1)
(ZIEL / 'NACHSPIEL-BELEGE.json').write_text(text)
gelegt['NACHSPIEL-BELEGE.json'] = hashlib.sha256(text.encode()).hexdigest()

zeilen = [f'# Behebungsrunde 3 vor T4 — Abschlussordner (Kern-Commits d54bf2f und Nachtrag {KOMMIT} auf 6243377)', '', 'Bericht:', f'{URL}/BERICHT.md', '',
          'Umbenennungen: *.sh.txt, *.mjs.txt, *.junit.xml.txt, KERN-COMMIT.patch.txt = Originaldateien mit angehängtem .txt; '
          'skript_* = Skripte aus dem Arbeitsordner; *-arbeitsbaum = Läufe vor dem Commit; review_* = Proben des Gutachtens.',
          f'NACHSPIEL-BELEGE.json bündelt {len(buendel)} Nachspiel-Belege am Commit d54bf2f (Durchgänge d1–d3; je Datei sha256, Größe, Inhalt).', '',
          'Jede Datei einzeln (volle Abholadresse, dahinter sha256):', '']
zeilen += [f'{URL}/{n}  {gelegt[n]}' for n in sorted(gelegt)]
# Zwischenberichte des Wächters in diesem Ordner: eigene Lieferungen mit eigener Prüfsumme, nicht im Manifest.
zwb = sorted(p.name for p in ZIEL.iterdir() if p.is_dir() and p.name.startswith('zwischenbericht-'))
if zwb:
    zeilen += ['', 'Zwischenberichte des Wächters in diesem Ordner (eigene Lieferungen mit eigener Prüfsumme, nicht im '
               'Manifest dieses Ordners; je Zeile ihre Dateiliste):', '']
    zeilen += [f'{URL}/{d}/DATEIEN.txt' for d in zwb]
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
print(json.dumps({'ordner': str(ZIEL).replace(AKTE, '[AKTE]'), 'kommit': KOMMIT, 'dateien': len(alle),
                  'https_bytegleich': f'{bytegleich} von {len(alle)}', 'fehler': [f.replace(AKTE, '[AKTE]') for f in fehler[:10]],
                  'ordnerpruefsumme': ordner, 'webseite_http': webseite, 'neu_angelegt': neu_angelegt},
                 ensure_ascii=False, indent=2))
sys.exit(0 if bytegleich == len(alle) else 1)
