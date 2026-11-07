"""Veröffentlicht den Abschlussordner der Behebungsrunde vor T4 und prüft jede Datei über HTTPS bytegleich.

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
BASIS = 'laeufe/biotop-vor-t4'
ZIEL = Path(f'/var/pruefkanal/oeffentlich/_akte/{AKTE}/{BASIS}')
URL = f'https://milieulux-reinigung-muenchen.de/_akte/{AKTE}/{BASIS}'
A = Path('/root/biotop-vor-t4')
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
    'REVIEW-AUFTRAG-VOR-T4.md': A / 'REVIEW-AUFTRAG-VOR-T4.md',
    'KASSE.md': A / 'KASSE.md',
    'KERN-COMMIT.patch.txt': A / 'KERN-COMMIT.patch.txt',
    'COMMIT-STAT.txt': A / 'COMMIT-STAT.txt',
    'JOB-COMMIT-REGRESSION.txt': A / 'JOB-COMMIT-REGRESSION.txt',
    'REGRESSION-VOR-T4.txt': A / 'REGRESSION-VOR-T4.txt',
    'REGRESSION-VOR-T4.junit.xml.txt': A / 'REGRESSION-VOR-T4.junit.xml',
    'VERDRAHTUNG-BELEG-REGRESSION.json': A / 'VERDRAHTUNG-BELEG-REGRESSION.json',
    'JOB-VERDRAHTUNG.txt': A / 'JOB-VERDRAHTUNG.txt',
    'JOB-SCHWARM.txt': A / 'JOB-SCHWARM.txt',
    'VERDRAHTUNG-GEGENPROBE-mass_roh-gruen.txt': A / 'VERDRAHTUNG-ROT-mass_roh.txt',
    'VERDRAHTUNG-GEGENPROBE-beide-rot.txt': A / 'VERDRAHTUNG-ROT-beide.txt',
    'skript_job_schwarm.sh.txt': A / 'job_schwarm.sh',
    'VERDRAHTUNG-ERSTER-VERSUCH-ABGEBROCHEN.txt': A / 'VERDRAHTUNG-GRUEN.txt',
    'VERDRAHTUNG-GEGENPROBE-phase-rot.txt': A / 'VERDRAHTUNG-ROT-phase.txt',
    'VERDRAHTUNG-GEGENPROBE-vv-rot.txt': A / 'VERDRAHTUNG-ROT-vv.txt',
    'VERDRAHTUNG-GEGENPROBE-schwarm-gruen.txt': A / 'VERDRAHTUNG-ROT-schwarm.txt',
    'skript_verdrahtung_gegenprobe.py': A / 'verdrahtung_gegenprobe.py',
    'skript_job_verdrahtung.sh.txt': A / 'job_verdrahtung.sh',
    'NACHSPIEL-VOR-T4.txt': A / 'NACHSPIEL-VOR-T4.txt',
    'NACHSPIEL-K2868-DURCHGANG2.txt': A / 'NACHSPIEL-K2868-DURCHGANG2.txt',
    'NACHSPIEL-PROBE.txt': A / 'NACHSPIEL-PROBE.txt',
    'skript_nachspiel_vor_t4.py': A / 'nachspiel_vor_t4.py',
    'VV-KAMMERPROBE.txt': A / 'VV-KAMMERPROBE.txt',
    'VV-KAMMERPROBE.json': A / 'VV-KAMMERPROBE.json',
    'skript_vv_kammerprobe.py': A / 'vv_kammerprobe.py',
    'T4-SPEZIFIKATION-ROT-an-f821707.txt': Path('/root/biotop-t3/abschluss3/T4-SPEZIFIKATION-ROT.txt'),
    'test_vor_t4.py': R / 'tests/test_vor_t4.py',
    'test_verdrahtung.py': R / 'tests/test_verdrahtung.py',
    'drahtwerk.py': R / 'tests/drahtwerk.py',
    'verhaltensvergleich.py': R / 'biotop/organe/verhaltensvergleich.py',
    'verhalten.mjs.txt': R / 'biotop/kern/ts/verhalten.mjs',
    'verhalten-runner.mjs.txt': R / 'biotop/kern/ts/verhalten-runner.mjs',
    'UEBERGABE.md': A / 'UEBERGABE.md',
    'skript_veroeffentlichen.py': A / 'veroeffentlichen.py',
    # ---- zweite Sitzung (Review-Befunde, Träger, S1, Sperre, Wächter)
    'KERN-COMMIT2.patch.txt': A / 'KERN-COMMIT2.patch.txt',
    'COMMIT2-STAT.txt': A / 'COMMIT2-STAT.txt',
    'COMMIT2-NACHRICHT.txt': A / 'COMMIT2-NACHRICHT.txt',
    'JOB-COMMIT2-REGRESSION.txt': A / 'JOB-COMMIT2-REGRESSION.txt',
    'skript_job_commit2_regression.sh.txt': A / 'job_commit2_regression.sh',
    'REGRESSION2-VOR-T4.txt': A / 'REGRESSION2-VOR-T4.txt',
    'REGRESSION2-VOR-T4.junit.xml.txt': A / 'REGRESSION2-VOR-T4.junit.xml',
    'VERDRAHTUNG-BELEG-REGRESSION2.json': A / 'VERDRAHTUNG-BELEG-REGRESSION2.json',
    'NACHSPIEL2-AM-COMMIT.txt': A / 'NACHSPIEL2-AM-COMMIT.txt',
    'PYTHON-LAUFZEIT-PROBE.json': A / 'PYTHON-LAUFZEIT-PROBE.json',
    'PYTHON-LAUFZEIT-PROBE.txt': A / 'PYTHON-LAUFZEIT-PROBE.txt',
    'skript_python_laufzeit_probe.py': A / 'python_laufzeit_probe.py',
    'TRAEGER-BELEG.json': A / 'traeger/TRAEGER-BELEG.json',
    'TRAEGER-BELEG.txt': A / 'traeger/TRAEGER-BELEG.txt',
    'TRAEGER-CONFIG-SETZEN.txt': A / 'traeger/CONFIG-SETZEN.txt',
    'TRAEGER-SICHERUNG.txt': A / 'traeger/SICHERUNG.txt',
    'skript_traeger_beleg.py': A / 'traeger/traeger_beleg.py',
    'skript_traeger_config_setzen.py': A / 'traeger/config_setzen.py',
    'S1-KLAERUNG.json': A / 's1/S1-KLAERUNG.json',
    'S1-KLAERUNG.txt': A / 's1/S1-KLAERUNG.txt',
    'S1-KLAERUNG-lauf1.txt': A / 's1/S1-KLAERUNG-lauf1.txt',
    'S1-DECKUNG.json': A / 's1/S1-DECKUNG.json',
    'S1-DECKUNG.txt': A / 's1/S1-DECKUNG.txt',
    'skript_s1_klaerung.py': A / 's1/s1_klaerung.py',
    'skript_s1_harness.mjs.txt': A / 's1/s1_harness.mjs',
    'skript_s1_deckung.py': A / 's1/s1_deckung.py',
    'SPERRE-GEGENPROBE.json': A / 'sperre/SPERRE-GEGENPROBE.json',
    'SPERRE-GEGENPROBE.txt': A / 'sperre/SPERRE-GEGENPROBE.txt',
    'skript_sperre_gegenprobe.py': A / 'sperre/sperre_gegenprobe.py',
    'WAECHTER-TESTS.txt': A / 'waechter/TESTS-NEU.txt',
    'WAECHTER-GEGENPROBEN.json': A / 'waechter/GEGENPROBEN.json',
    'WAECHTER-GEGENPROBEN.txt': A / 'waechter/GEGENPROBEN.txt',
    'WAECHTER-NACHSPIEL-ECHTE-SITZUNG.json': A / 'waechter/NACHSPIEL-ECHTE-SITZUNG.json',
    'WAECHTER-NACHSPIEL-ECHTE-SITZUNG.txt': A / 'waechter/NACHSPIEL-ECHTE-SITZUNG.txt',
    'skript_waechter_gegenproben.py': A / 'waechter/gegenproben.py',
    'skript_waechter_nachspiel.py': A / 'waechter/nachspiel_echte_sitzung.py',
    'skript_waechter_erweitern.py': A / 'waechter/erweitern.py',
    'zwischenbericht_waechter.py': Path('/root/.hermes/scripts/zwischenbericht_waechter.py'),
    'test_waechter.py': Path('/root/.hermes/zwischenbericht/test_waechter.py'),
    'gedaechtnis.py': R / 'biotop/organe/gedaechtnis.py',
    'NACHLESE.json': A / 'NACHLESE.json',
    'NACHLESE.txt': A / 'NACHLESE.txt',
    'skript_nachlese.py': A / 'nachlese.py',
    'spez_test_laufzeit_gepaart_teilausfall.py': A / 'spez/test_spez_laufzeit_gepaart_teilausfall.py',
    'NACHSPIEL3-S2.txt': A / 'NACHSPIEL3-S2.txt',
    'NACHSPIEL3-s2_k2904.json': A / 'nachspiel3/s2_k2904.json',
    'NACHSPIEL3-s2_k3091.json': A / 'nachspiel3/s2_k3091.json',
    'PYTHON-LAUFZEIT-PROBE-lauf1.json': A / 'PYTHON-LAUFZEIT-PROBE-lauf1.json',
    'PYTHON-LAUFZEIT-PROBE-lauf1.txt': A / 'PYTHON-LAUFZEIT-PROBE-lauf1.txt',
    'skript_platzhalter_fuellen.py': A / 'platzhalter_fuellen.py',
    'KERN-COMMIT2-NACHRICHT.txt': A / 'COMMIT2-NACHRICHT.txt',
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
for p in sorted((A / 'nachspiel').glob('*.json')):
    daten = p.read_bytes()
    buendel[p.name] = {'sha256': hashlib.sha256(daten).hexdigest(), 'bytes': len(daten), 'inhalt': json.loads(daten)}
text = json.dumps(buendel, ensure_ascii=False, indent=1)
(ZIEL / 'NACHSPIEL-BELEGE.json').write_text(text)
gelegt['NACHSPIEL-BELEGE.json'] = hashlib.sha256(text.encode()).hexdigest()
buendel2 = {}
for p in sorted((A / 'nachspiel2').glob('*.json')):
    daten = p.read_bytes()
    buendel2[p.name] = {'sha256': hashlib.sha256(daten).hexdigest(), 'bytes': len(daten), 'inhalt': json.loads(daten)}
if len(buendel2) != 7:
    raise SystemExit(f'nachspiel2: {len(buendel2)} statt 7 Belege — Abbruch vor dem Veröffentlichen')
text2 = json.dumps(buendel2, ensure_ascii=False, indent=1)
(ZIEL / 'NACHSPIEL2-BELEGE.json').write_text(text2)
gelegt['NACHSPIEL2-BELEGE.json'] = hashlib.sha256(text2.encode()).hexdigest()

zeilen = ['# Behebungsrunde vor T4 — Abschlussordner, Stand 2026-09-23 (zweite Sitzung, Commit 330b4ec)', '', 'Bericht:', f'{URL}/BERICHT.md', '',
          'Umbenennungen: *.sh.txt, *.mjs.txt, *.junit.xml.txt, KERN-COMMIT.patch.txt = Originaldateien mit angehängtem .txt; '
          'VERDRAHTUNG-GEGENPROBE-<art>-<rot|gruen>.txt = Arbeitsdatei VERDRAHTUNG-ROT-<art>.txt (Name nach dem Ergebnis); '
          'VERDRAHTUNG-ERSTER-VERSUCH-ABGEBROCHEN.txt = VERDRAHTUNG-GRUEN.txt (Satz-2-Abbruch, siehe BERICHT §5).',
          f'NACHSPIEL-BELEGE.json bündelt {len(buendel)} Nachspiel-Belege an 58bd9f9 (Arbeitsbaum), NACHSPIEL2-BELEGE.json {len(buendel2)} am Commit 330b4ec (je Datei sha256, Größe, Inhalt).',
          'Kern-Commits: 58bd9f9 (KERN-COMMIT.patch.txt), 330b4ec (KERN-COMMIT2.patch.txt). Wächter und Träger: außerhalb des Biotop-Repositorys, Dateien im Ordner.', '',
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
