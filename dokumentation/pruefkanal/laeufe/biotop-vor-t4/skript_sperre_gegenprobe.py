"""Gegenprobe (Auftrag Philipp, Punkt 2): Kann der nach dem Review geänderte Gedächtnissperre-Test weiterhin rot werden?

Gegenstand: tests/test_vor_t4.py::test_10_sperre_am_laufweg_projekt_merken_und_wiederholung (nach dem Review um die
Vorrichtung `ts_kammer` ergänzt — ohne TS-Kammerimage wird er jetzt ÜBERSPRUNGEN statt rot) und der neue Lesetest
test_review11_altbestand_grenzmass_laufzeit_sperrt_beim_lesen_nicht. Seit dem Review wirkt die Regel an ZWEI Stellen:
beim Schreiben (projekt_merken klassifiziert 'laufzeit_unbestaetigt') und beim Lesen (_sperrt in wiederholung und
gescheiterte_wege). Wie beim Schwarm-2×2 kann eine Einzelgegenprobe deshalb blind sein.

Je Variante eine Kopie des Arbeitsbaums mit genau EINEM Eingriff; vorab festgelegt, was fallen muss:
  unveraendert          → alles grün (Vergleichslauf)
  schreib_aus           → ? (Lesestelle hält womöglich allein — genau das wird gemessen)
  lese_aus              → test_review11 rot
  beide_aus             → test_10 rot in den beiden „sperrt nicht“-Zeilen an `(w is not None) is sperrt`
  regel_sperrt_immer    → test_10 rot in den beiden „sperrt nicht“-Zeilen
  regel_sperrt_nie      → test_10 rot in der Zeile „berührt und gepaart bestätigt“
  ohne_ts_image         → test_10: 4 von 4 ÜBERSPRUNGEN (kein Rot möglich) — die Regression muss ts1 setzen
Aufruf: python sperre_gegenprobe.py [varianten…]
"""
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

R = Path('/root/biotop')
AUS = Path('/root/biotop-vor-t4/sperre')
PY = '/root/biotop-t3/venv/bin/python'
G = 'biotop/organe/gedaechtnis.py'
EINGRIFFE = {
    'schreib': (G, '    if klasse == "grenzmass" and not laufzeit_sperrt(k["grund"], k["diff"]):\n', '    if False:\n'),
    'lese': (G, 'def _sperrt(w) -> bool:\n', 'def _sperrt(w) -> bool:\n    return True\n'),
    'immer': (G, 'def laufzeit_sperrt(grund: str, diff: str | None = None, beruehrt: set[str] | None = None) -> bool:\n',
              'def laufzeit_sperrt(grund: str, diff: str | None = None, beruehrt: set[str] | None = None) -> bool:\n    return True\n'),
    'nie': (G, 'def laufzeit_sperrt(grund: str, diff: str | None = None, beruehrt: set[str] | None = None) -> bool:\n',
            'def laufzeit_sperrt(grund: str, diff: str | None = None, beruehrt: set[str] | None = None) -> bool:\n    return False\n'),
}
VARIANTEN = {'unveraendert': [], 'schreib_aus': ['schreib'], 'lese_aus': ['lese'], 'beide_aus': ['schreib', 'lese'],
             'regel_sperrt_immer': ['immer'], 'regel_sperrt_nie': ['nie'], 'ohne_ts_image': []}
AUSWAHL = 'test_10_sperre_am_laufweg or test_review11_altbestand'


def kopie(ziel: Path):
    shutil.rmtree(ziel, ignore_errors=True)
    ziel.mkdir(parents=True)
    liste = subprocess.run(['git', 'ls-files', '-z', '-co', '--exclude-standard'], cwd=R, capture_output=True, check=True).stdout
    p1 = subprocess.Popen(['tar', '--null', '-T', '-', '-cf', '-'], cwd=R, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['tar', '-x', '-C', str(ziel)], stdin=p1.stdout)
    p1.stdin.write(liste)
    p1.stdin.close()
    p2.wait()
    p1.wait()


def main(namen):
    ergebnis = json.loads((AUS / 'SPERRE-GEGENPROBE.json').read_text()) if (AUS / 'SPERRE-GEGENPROBE.json').exists() else {}
    for name in namen:
        ziel = Path(f'/tmp/sperre-gegenprobe/{name}')
        kopie(ziel)
        for e in VARIANTEN[name]:
            datei, anker, ersatz = EINGRIFFE[e]
            p = ziel / datei
            t = p.read_text()
            assert t.count(anker) == 1, (name, e, t.count(anker))
            p.write_text(t.replace(anker, ersatz))
        env = dict(os.environ, PYTHONPATH=str(ziel), TMPDIR='/tmp',
                   BIOTOP_KAMMER_IMAGE='biotop-kammer:1' if name == 'ohne_ts_image' else 'biotop-kammer:ts1')
        herkunft = subprocess.run([PY, '-c', 'import biotop.organe.gedaechtnis as g; print(g.__file__)'], cwd=ziel, env=env,
                                  capture_output=True, text=True).stdout.strip()
        junit = ziel / 'ergebnis.xml'
        p = subprocess.run([PY, '-m', 'pytest', 'tests/test_vor_t4.py', '-k', AUSWAHL, '-q', '-p', 'no:cacheprovider', '-rs',
                            '--tb=short', f'--junitxml={junit}'], cwd=ziel, env=env, capture_output=True, text=True, timeout=900)
        x = junit.read_text()
        faelle = {}
        for m in re.finditer(r'<testcase [^>]*name="([^"]+)"[^>]*?(?:/>|>(.*?)</testcase>)', x, re.S):
            body = m.group(2) or ''
            art = 'rot' if ('<failure' in body or '<error' in body) else 'uebersprungen' if '<skipped' in body else 'gruen'
            zeile = ''
            if art == 'rot':
                zeile = next((z.strip() for z in re.findall(r'^\s*&gt;?\s*(assert .*)$', body, re.M)), '')
                zeile = zeile or next((z.strip()[:200] for z in body.splitlines() if 'assert' in z), '')
            faelle[m.group(1)] = {'art': art, 'zusicherung': zeile.replace('&gt;', '>').replace('&lt;', '<')
                                  .replace('&apos;', "'").replace('&quot;', '"')[:220]}
        zaehl = {a: sum(1 for f in faelle.values() if f['art'] == a) for a in ('gruen', 'rot', 'uebersprungen')}
        ergebnis[name] = {'eingriffe': VARIANTEN[name], 'gedaechtnis_geladen_aus': herkunft, 'rc': p.returncode,
                          'zaehlung': zaehl, 'faelle': faelle, 'pytest_ende': p.stdout.strip().splitlines()[-1:]}
        print(f'{name:20} rc={p.returncode} {zaehl} | geladen aus {herkunft}')
        for n, f in faelle.items():
            if f['art'] != 'gruen':
                print(f"    {f['art']:13} {n[:110]} :: {f['zusicherung'][:140]}")
        shutil.rmtree(ziel, ignore_errors=True)
        (AUS / 'SPERRE-GEGENPROBE.json').write_text(json.dumps(ergebnis, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    AUS.mkdir(parents=True, exist_ok=True)
    main(sys.argv[1:] or list(VARIANTEN))
