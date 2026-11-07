"""Auswertung der Nachtrag-Belege (Behebungsrunde 4 vor T4): Nachspiele N1–N3 (K2904/K3091 je Durchgang, K2868 im
Einzelnen), Regression-2 (JUnit), Verdrahtung-2, Stufe 1 unverändert (git diff), Codestand der Belege. Nur lesend.
Aufruf: python auswertung_nachtrag.py > AUSWERTUNG-NACHTRAG.txt"""
import json
import re
import subprocess
from pathlib import Path

A = Path('/root/biotop-vor-t4-04')
print('== Nachspiele N1–N3 am Nachtrag')
for d in ('n1', 'n2', 'n3'):
    for f in sorted((A / 'nachspiel' / d).glob('*.json')):
        b = json.loads(f.read_text())
        g = b.get('gewinn_nachmessung') or {}
        cs = b.get('code_stand_nach_fall') or {}
        pl = ((b.get('laufzeit_gepaart') or {}).get('bereiche') or {}).get('planung') or {}
        q = round(pl['kandidat'] / pl['basis'], 4) if pl.get('basis') else None
        print(f"{d} {f.stem:9} status={b.get('status'):10} erwartung_erfuellt={b.get('erwartung_erfuellt')} stufe={b.get('laufzeit_stufe')} "
              f"planung_quote={q} gewinn={g.get('ergebnis')} commit={cs.get('commit', '')[:7]} sauber={cs.get('arbeitsbaum_sauber')} "
              f"db_gleich={b.get('quelle_db_sha256_vorher') == b.get('quelle_db_sha256_nachher')} "
              f"lz_nachmessung={bool(b.get('laufzeit_nachmessung'))}")
k = json.loads((A / 'nachspiel/n1/k2868.json').read_text())
v = k['verhalten']
gedeckt = v.get('gedeckt') or {}
print('\n== K2868 (N1) im Einzelnen')
print('abweichungen', v.get('anzahl_abweichungen'), '| gedeckt', len(gedeckt), '| ungedeckt', len(v.get('ungedeckt_alle') or v.get('ungedeckt') or []))
art = {}
for s in gedeckt:
    m = re.search(r'~(rand|form)#(\d+)', s)
    art[m.group(0) if m else s.split(':')[-1]] = art.get(m.group(0) if m else s.split(':')[-1], 0) + 1
print('gedeckt je Aufruf (mit @-Mustern):', dict(sorted(art.items())))
print('deckende Tests:', sorted({t for ts in gedeckt.values() for t in ts}))
print('ungedeckt_aufschluesselung:', json.dumps(v.get('ungedeckt_aufschluesselung'), ensure_ascii=False))
dz = v.get('deckung_zaehlung') or {}
print('deckung_zaehlung:', {x: dz.get(x) for x in ('tests', 'aufrufe', 'verfaelschungen', 'kappe', 'ausgelassen')})
print('festhaltend:', json.dumps(dz.get('festhaltend'), ensure_ascii=False)[:1200])
print('klassen_je_test:', json.dumps(dz.get('klassen_je_test'), ensure_ascii=False)[:1200])
print('eingaben (ungedeckt, erste):', json.dumps(dict(list((v.get('eingaben') or {}).items())[:6]), ensure_ascii=False)[:1500])
print('werte (erste):', json.dumps(dict(list((v.get('werte') or {}).items())[:6]), ensure_ascii=False)[:1500])
print('eigene_tests_ausgeschlossen:', v.get('eigene_tests_ausgeschlossen'))
print('\n== Regression-2 (JUnit)')
x = (A / 'REGRESSION-2.junit.xml').read_text()
print({k2: re.search(rf'{k2}="(\d+)"', x).group(1) for k2 in ('tests', 'failures', 'errors', 'skipped')})
print('test_vor_t4_04 Fälle:', len(re.findall(r'classname="tests\.test_vor_t4_04"', x)))
print(subprocess.run(['tail', '-3', str(A / 'REGRESSION-2.txt')], capture_output=True, text=True).stdout)
vb = json.loads((A / 'VERDRAHTUNG-BELEG-REGRESSION-2.json').read_text())
print('verdrahtung-2:', vb.get('gerufen'), 'von', vb.get('organe'), 'nie', vb.get('nie_gerufen'), 'kosten', vb.get('modellkosten_eur'),
      'nachmessungen', len(vb.get('nachmessungen') or []))
vb1 = json.loads((A / 'VERDRAHTUNG-BELEG-REGRESSION.json').read_text())
print('verdrahtung-1:', vb1.get('gerufen'), 'von', vb1.get('organe'), 'kosten', vb1.get('modellkosten_eur'))
x1 = (A / 'REGRESSION.junit.xml').read_text()
print('Regression-1 JUnit:', {k2: re.search(rf'{k2}="(\d+)"', x1).group(1) for k2 in ('tests', 'failures', 'errors', 'skipped')})
print('\n== Stufe 1 unverändert, Commits')
print('diff Stufe 1 0aac612..HEAD:', repr(subprocess.run(['git', '-C', '/root/biotop', 'diff', '--stat', '0aac612', 'HEAD', '--',
                                                         'biotop/kern/referenzlast/versandwerk-t3-02.mjs'], capture_output=True, text=True).stdout))
print(subprocess.run(['git', '-C', '/root/biotop', 'log', '--oneline', '-3'], capture_output=True, text=True).stdout)
print('status:', repr(subprocess.run(['git', '-C', '/root/biotop', 'status', '--short'], capture_output=True, text=True).stdout))
print(subprocess.run(['git', '-C', '/root/biotop', 'show', '--stat', '--format=%h', '1d9a5aa'], capture_output=True, text=True).stdout.splitlines()[-1])
print(subprocess.run(['git', '-C', '/root/biotop', 'show', '--stat', '--format=%h', '43b8fad'], capture_output=True, text=True).stdout.splitlines()[-1])
