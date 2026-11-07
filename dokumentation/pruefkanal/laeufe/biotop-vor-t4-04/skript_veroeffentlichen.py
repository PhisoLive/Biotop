"""Veröffentlicht den Abschlussordner der Behebungsrunde 4 vor T4 und prüft jede Datei über HTTPS bytegleich.

Ein vorhandener Zielordner wird nie gelöscht oder überschrieben — Abbruch (erlaubt sind nur die Unterordner des
Zwischenbericht-Wächters). Rechte root:caddy, Ordner 750, Dateien 640. Nachspiel-Belege werden zu einer Datei gebündelt
(je Originaldatei sha256, Größe, Inhalt). Endungen, die der Server womöglich nicht als Text ausliefert (.sh, .mjs,
.xml, .patch, .jsonl), bekommen „.txt“ angehängt. (Übernommen aus laeufe/biotop-vor-t4-03/skript_veroeffentlichen.py;
geändert: Quellenliste, Nachspielbündel 15.)
"""
import hashlib
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

AKTE = Path('/etc/pruefkanal/schluessel').read_text().strip()
BASIS = 'laeufe/biotop-vor-t4-04'
ZIEL = Path(f'/var/pruefkanal/oeffentlich/_akte/{AKTE}/{BASIS}')
URL = f'https://milieulux-reinigung-muenchen.de/_akte/{AKTE}/{BASIS}'
A = Path('/root/biotop-vor-t4-04')
R = Path('/root/biotop')
KOMMIT = subprocess.run(['git', '-C', str(R), 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()

if ZIEL.exists():
    fremd = [p.name for p in ZIEL.iterdir() if not (p.is_dir() and p.name.startswith('zwischenbericht-'))]
    if fremd:
        raise SystemExit(f'{ZIEL} enthält schon gelieferte Dateien {fremd[:5]} — nichts wird überschrieben. Abbruch.')

QUELLEN = {
    'BERICHT.md': A / 'BERICHT.md',
    'REVIEW.md': A / 'REVIEW.md',
    'REVIEW-AUFTRAG.md': A / 'REVIEW-AUFTRAG.md',
    'KASSE.md': A / 'KASSE.md',
    'UEBERGABE.md': A / 'UEBERGABE.md',
    'FEHLALARM-SICHERHEITSFILTER.md': A / 'FEHLALARM-SICHERHEITSFILTER.md',
    'KERN-COMMIT.patch.txt': A / 'KERN-COMMIT.patch.txt',
    'COMMIT-STAT.txt': A / 'COMMIT-STAT.txt',
    'COMMIT-NACHRICHT.txt': A / 'COMMIT-NACHRICHT.txt',
    'KERN-COMMIT-2.patch.txt': A / 'KERN-COMMIT-2.patch.txt',
    'COMMIT-2-STAT.txt': A / 'COMMIT-2-STAT.txt',
    'COMMIT-NACHRICHT-2.txt': A / 'COMMIT-NACHRICHT-2.txt',
    'JOB-COMMIT-REGRESSION.txt': A / 'JOB-COMMIT-REGRESSION.txt',
    'skript_job_commit_regression.sh.txt': A / 'job_commit_regression.sh',
    'JOB-NACHTRAG.txt': A / 'JOB-NACHTRAG.txt',
    'skript_job_nachtrag.sh.txt': A / 'job_nachtrag.sh',
    'REGRESSION.txt': A / 'REGRESSION.txt',
    'REGRESSION.junit.xml.txt': A / 'REGRESSION.junit.xml',
    'VERDRAHTUNG-BELEG-REGRESSION.json': A / 'VERDRAHTUNG-BELEG-REGRESSION.json',
    'REGRESSION-2.txt': A / 'REGRESSION-2.txt',
    'REGRESSION-2.junit.xml.txt': A / 'REGRESSION-2.junit.xml',
    'VERDRAHTUNG-BELEG-REGRESSION-2.json': A / 'VERDRAHTUNG-BELEG-REGRESSION-2.json',
    'NACHSPIEL-D1-abgebrochen.txt': A / 'nachspiel/NACHSPIEL-D1.txt',
    'NACHSPIEL-D2-abgebrochen.txt': A / 'nachspiel/NACHSPIEL-D2.txt',
    'NACHSPIEL-D3-abgebrochen.txt': A / 'nachspiel/NACHSPIEL-D3.txt',
    'NACHSPIEL-N1.txt': A / 'nachspiel/NACHSPIEL-N1.txt',
    'NACHSPIEL-N2.txt': A / 'nachspiel/NACHSPIEL-N2.txt',
    'NACHSPIEL-N3.txt': A / 'nachspiel/NACHSPIEL-N3.txt',
    'NACHSPIEL-PROBE-ARBEITSBAUM.txt': A / 'nachspiel/PROBE-ARBEITSBAUM.txt',
    'AUSWERTUNG-NACHTRAG.txt': A / 'nachspiel/AUSWERTUNG-NACHTRAG.txt',
    'EINZELHEITEN-NACHSPIELE.txt': A / 'nachspiel/EINZELHEITEN.txt',
    'skript_nachspiel_vor_t4_04.py': A / 'nachspiel/nachspiel_vor_t4_04.py',
    'skript_probe_arbeitsbaum.py': A / 'nachspiel/probe_arbeitsbaum.py',
    'skript_auswertung_nachtrag.py': A / 'nachspiel/auswertung_nachtrag.py',
    'skript_einzelheiten.py': A / 'nachspiel/einzelheiten.py',
    'STUFE2-ZEITEN.txt': A / 'proben/STUFE2-ZEITEN.txt',
    'STUFE2-ZEITEN.json': A / 'proben/STUFE2-ZEITEN.json',
    'STUFE2-ZEITEN-erste-fassung.txt': A / 'proben/STUFE2-ZEITEN-erste-fassung.txt',
    'STUFE2-ZEITEN-erste-fassung.json': A / 'proben/STUFE2-ZEITEN-erste-fassung.json',
    'skript_stufe2_zeiten.py': A / 'proben/stufe2_zeiten.py',
    'VORHER-0aac612.txt': A / 'proben/VORHER-0aac612.txt',
    'VORHER-0aac612.json': A / 'proben/VORHER-0aac612.json',
    'VORHER-0aac612.junit.xml.txt': A / 'proben/VORHER-0aac612.junit.xml',
    'NACHHER-HEAD.txt': A / 'proben/NACHHER-HEAD.txt',
    'NACHHER-HEAD.json': A / 'proben/NACHHER-HEAD.json',
    'NACHHER-HEAD.junit.xml.txt': A / 'proben/NACHHER-HEAD.junit.xml',
    'skript_vorher_nachher.py': A / 'proben/vorher_nachher.py',
    'SPION-GEWINN.txt': A / 'proben/SPION-GEWINN.txt',
    'SPION-GEWINN.jsonl.txt': A / 'proben/SPION-GEWINN.jsonl',
    'SPION-GEWINN-PYTEST.txt': A / 'proben/SPION-GEWINN-PYTEST.txt',
    'skript_spion_gewinn.py': A / 'proben/spion_gewinn.py',
    'skript_spion_gewinn.sh.txt': A / 'proben/spion_gewinn.sh',
    'TORZEILE-SCHWAECHEN-T3.txt': A / 's1/TORZEILE-SCHWAECHEN-T3.txt',
    'TORZEILE-SCHWAECHEN-T3.json': A / 's1/TORZEILE-SCHWAECHEN-T3.json',
    'TORZEILE-SCHWAECHEN-T3-am-commit.txt': A / 's1/TORZEILE-SCHWAECHEN-T3-am-commit.txt',
    'skript_torzeile_schwaechen_t3.py': A / 's1/torzeile_schwaechen_t3.py',
    'FORMATSPERRE-1.txt': A / 'sperre/FORMATSPERRE-1.txt',
    'formatsperre-1-befehl.sh.txt': A / 'sperre/formatsperre-1-befehl.sh',
    'TEILLAUF-1-arbeitsbaum.txt': A / 'bau/TEILLAUF-1.txt',
    'TEILLAUF-2-arbeitsbaum.txt': A / 'bau/TEILLAUF-2.txt',
    'TEILLAUF-3-arbeitsbaum.txt': A / 'bau/TEILLAUF-3.txt',
    'TEILLAUF-4-arbeitsbaum.txt': A / 'bau/TEILLAUF-4.txt',
    'TEILLAUF-5-arbeitsbaum.txt': A / 'bau/TEILLAUF-5.txt',
    'KETTE.txt': A / 'bau/KETTE.txt',
    'KETTE-NACHTRAG-gestoppt.txt': A / 'bau/KETTE-NACHTRAG.txt',
    'skript_kette.sh.txt': A / 'bau/kette.sh',
    'skript_kette_nachtrag.sh.txt': A / 'bau/kette_nachtrag.sh',
    'skript_bau_r4_stufe2.py': A / 'bau/r4_stufe2.py',
    'skript_bau_r4_sonde_py.py': A / 'bau/r4_sonde_py.py',
    'skript_bau_r4_sonde_ts.py': A / 'bau/r4_sonde_ts.py',
    'skript_bau_r4_deckung.py': A / 'bau/r4_deckung.py',
    'skript_bau_r4_muster.py': A / 'bau/r4_muster.py',
    'skript_bau_r4_fix1.py': A / 'bau/r4_fix1.py',
    'skript_bau_r4_fix2_tests.py': A / 'bau/r4_fix2_tests.py',
    'skript_bau_r4_nachspiel_torzeile.py': A / 'bau/r4_nachspiel_torzeile.py',
    'skript_bau_r4_nachtrag.py': A / 'bau/r4_nachtrag.py',
    'skript_bau_r4_fix_nachspiel.py': A / 'bau/r4_fix_nachspiel.py',
    'skript_bau_r4_waechtertest_nachspiel.py': A / 'bau/r4_waechtertest_nachspiel.py',
    'versandwerk-t3-02.stufe2.mjs.txt': R / 'biotop/kern/referenzlast/versandwerk-t3-02.stufe2.mjs',
    'verhalten_py.py': R / 'biotop/kern/py/verhalten.py',
    'kanon.mjs.txt': R / 'biotop/kern/ts/kanon.mjs',
    'verhaltensvergleich.py': R / 'biotop/organe/verhaltensvergleich.py',
    'gegenzeugen.py': R / 'biotop/kern/gegenzeugen.py',
    'test_vor_t4_04.py': R / 'tests/test_vor_t4_04.py',
    'skript_veroeffentlichen.py': A / 'veroeffentlichen.py',
}
for p in sorted((A / 'review-proben').glob('*')) if (A / 'review-proben').is_dir() else []:
    if p.is_file() and p.suffix in ('.py', '.txt', '.json', '.md', '.sh', '.mjs'):
        QUELLEN['review_' + p.name + ('.txt' if p.suffix in ('.sh', '.mjs') else '')] = p
if (A / 'SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md').is_file():
    QUELLEN['SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md'] = A / 'SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md'
fehlend = [f'{n} ({q})' for n, q in QUELLEN.items() if not Path(q).is_file()]
if '‹' in (A / 'BERICHT.md').read_text() or '‹' in (A / 'KASSE.md').read_text():
    raise SystemExit('BERICHT.md oder KASSE.md enthält noch Platzhalter ‹…› — Abbruch')
if fehlend:
    raise SystemExit(f'Quellen fehlen: {fehlend}')

buendel = {}
for ordner in ('d1', 'd2', 'd3', 'probe-arbeitsbaum', 'n1', 'n2', 'n3'):
    for p in sorted((A / 'nachspiel' / ordner).glob('*.json')):
        daten = p.read_bytes()
        buendel[f'nachspiel/{ordner}/{p.name}'] = {'sha256': hashlib.sha256(daten).hexdigest(), 'bytes': len(daten),
                                                   'inhalt': json.loads(daten)}
if len(buendel) != 15:
    raise SystemExit(f'Nachspielbelege: {len(buendel)} statt 15 (d1 3, d2 2, d3 2, Vorprobe 1, n1 3, n2 2, n3 2) — Abbruch')

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

zeilen = [f'# Behebungsrunde 4 vor T4 — Abschlussordner (Kern-Commits 1d9a5aa und Nachtrag {KOMMIT} auf 0aac612)', '',
          'Bericht:', f'{URL}/BERICHT.md', '',
          'Umbenennungen: *.sh.txt, *.mjs.txt, *.junit.xml.txt, *.jsonl.txt, KERN-COMMIT*.patch.txt = Originaldateien mit '
          'angehängtem .txt; skript_* = Skripte aus dem Arbeitsordner; *-arbeitsbaum = Läufe vor dem Commit; '
          'review_* = Proben des Gutachtens; NACHSPIEL-D*-abgebrochen = die Nachspiele am Commit 1d9a5aa (Befund, BERICHT §13).',
          f'NACHSPIEL-BELEGE.json bündelt {len(buendel)} Nachspiel-Belege (d1–d3 am Commit 1d9a5aa, abgebrochen; eine Vorprobe '
          f'am Arbeitsbaum; n1–n3 am Nachtrag {KOMMIT}; je Datei sha256, Größe, Inhalt).', '',
          'Jede Datei einzeln (volle Abholadresse, dahinter sha256):', '']
zeilen += [f'{URL}/{n}  {gelegt[n]}' for n in sorted(gelegt)]
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
                  'ordnerpruefsumme': ordner, 'webseite_http': webseite, 'neu_angelegt': neu_angelegt,
                  'zwischenberichte': len(zwb)}, ensure_ascii=False, indent=2))
sys.exit(0 if bytegleich == len(alle) else 1)
