"""Auswertung der Belege der Behebungsrunde 5 (nur lesen): Nachspiele N1–N3, Vorher/Nachher, T4-Größe, Regression,
Verdrahtung, Stufe-2-Eichung. Schreibt AUSWERTUNG.txt und AUSWERTUNG.json (Grundlage für das Füllen des Berichts)."""
import collections
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

A = Path('/root/biotop-vor-t4-05')
aus, z = {}, []


def zeile(s):
    z.append(s)
    print(s)


# Nachspiele
ns = []
for d in ('n1', 'n2', 'n3', 'vorprobe'):
    for f in sorted((A / 'nachspiel' / d).glob('*.json')):
        b = json.loads(f.read_text())
        lz = b.get('laufzeit_gepaart') or {}
        q = {bb: round(x['kandidat'] / x['basis'], 4) for bb, x in (lz.get('bereiche') or {}).items()
             if x.get('basis') and x.get('kandidat')}
        v = b.get('verhalten') or {}
        e = {'durchgang': d, 'fall': b.get('fall'), 'status': b.get('status'), 'erwartet': b.get('erwartung'),
             'erfuellt': b.get('erwartung_erfuellt'), 'stufe': b.get('laufzeit_stufe'), 'planung': q.get('planung'),
             'quoten': q, 'gewinn': (b.get('gewinn_nachmessung') or {}).get('ergebnis'),
             'gesperrt': b.get('gesperrte_bereiche'), 'toleranz': b.get('rauschtoleranz'),
             'commit': (b.get('code_stand_beim_import') or {}).get('commit', '')[:7],
             'sauber': (b.get('code_stand_beim_import') or {}).get('arbeitsbaum_sauber'),
             'db_gleich': b.get('quelle_db_sha256_vorher') == b.get('quelle_db_sha256_nachher'),
             'modell': b.get('modellaufrufe_echt'), 'fehler': str(b.get('fehler') or '')[:200],
             'grund': str(b.get('grund') or '')[:240], 'vv_grund_art': v.get('grund_art'),
             'abweichungen': v.get('anzahl_abweichungen'), 'ungedeckt': len(v.get('ungedeckt_alle') or v.get('ungedeckt') or []),
             'gedeckt': len(v.get('gedeckt') or {}), 'unvollstaendig': v.get('unvollstaendig'),
             'sonde_ausfall': v.get('sonde_ausfall'), 'aufschluesselung': v.get('ungedeckt_aufschluesselung'),
             'rauschen': b.get('rauschen_herkunft'), 'laufzeit_nachmessung': bool(b.get('laufzeit_nachmessung'))}
        ns.append(e)
        zeile(f"{d} {e['fall']:9} status={e['status']} erwartet={e['erwartet']} erfuellt={e['erfuellt']} stufe={e['stufe']} "
              f"planung={e['planung']} gewinn={e['gewinn']} gesperrt={e['gesperrt']} commit={e['commit']} sauber={e['sauber']} "
              f"db_gleich={e['db_gleich']} vv={e['vv_grund_art']} abw={e['abweichungen']} ungedeckt={e['ungedeckt']} "
              f"gedeckt={e['gedeckt']} unvollst={e['unvollstaendig']} ausfall={e['sonde_ausfall']} fehler={e['fehler']}")
aus['nachspiele'] = ns
for fall in ('s2_k2904', 's2_k3091'):
    zs = [e for e in ns if e['fall'] == fall and e['durchgang'] in ('n1', 'n2', 'n3')]
    zeile(f"{fall}: {sum(e['status'] == 'ueberlebt' for e in zs)} von {len(zs)} überlebt; planung "
          f"{[e['planung'] for e in zs]}; eingang gesperrt in {sum('eingang' in (e['gesperrt'] or []) for e in zs)} von {len(zs)}")
k = [e for e in ns if e['fall'] == 'k2868']
if k:
    zeile(f"k2868: {k[0]['status']} abw={k[0]['abweichungen']} ungedeckt={k[0]['ungedeckt']} gedeckt={k[0]['gedeckt']} "
          f"aufschl={json.dumps(k[0]['aufschluesselung'], ensure_ascii=False)}")

# Vorher/Nachher
for n in ('VORHER-43b8fad', 'NACHHER-HEAD'):
    p = A / 'proben' / f'{n}.json'
    if p.exists():
        d = json.loads(p.read_text())
        aus[n] = d
        zeile(f"{n}: {d['gruen']} von {d['n']} grün (commit {d['commit']})")

# T4-Größe
p = A / 'proben' / 'T4-GROESSE.txt'
if p.exists():
    aus['t4'] = [json.loads(l) for l in p.read_text().splitlines() if l.startswith('{')]
    for x in aus['t4']:
        zeile('T4-GROESSE ' + json.dumps(x, ensure_ascii=False)[:500])

# Regression, Verdrahtung, Teilläufe
for n in ('REGRESSION.txt',):
    p = A / n
    if p.exists():
        zeile(f"{n}: {p.read_text().strip().splitlines()[-1]}")
p = A / 'REGRESSION.junit.xml'
if p.exists():
    r = ET.parse(p).getroot()
    tc = list(r.iter('testcase'))
    aus['junit'] = {'faelle': len(tc), 'failure': sum(t.find('failure') is not None for t in tc),
                    'error': sum(t.find('error') is not None for t in tc), 'skipped': sum(t.find('skipped') is not None for t in tc),
                    'vor_t4_05': sum(1 for t in tc if 'test_vor_t4_05' in (t.get('classname') or ''))}
    zeile(f"JUnit: {aus['junit']}")
for n in ('VERDRAHTUNG-BELEG-REGRESSION.json', 'VERDRAHTUNG-BELEG-TEILLAUF3.json'):
    p = A / n
    if p.exists():
        d = json.loads(p.read_text())
        aus[n] = {k: d.get(k) for k in ('organe', 'gerufen', 'nie_gerufen', 'register', 'tor4', 'nachspiel', 'modellkosten_eur')}
        aus[n]['stufen'] = collections.Counter(str(x.get('stufe')) for x in d.get('nachmessungen') or [])
        zeile(f"{n}: " + json.dumps(aus[n], ensure_ascii=False, default=str)[:900])
for n in sorted((A / 'bau').glob('TEILLAUF-*.txt')):
    t = n.read_text().strip().splitlines()
    zeile(f"{n.name}: {t[-1] if t else '(leer)'}")

# Stufe-2-Eichung
zs = [json.loads(l) for l in (A / 'proben' / 'STUFE2-EICHUNG.jsonl').read_text().splitlines()]
je = collections.defaultdict(list)
for x in zs:
    je[x['variante']].append(x)
aus['eichung'] = {v: {'n': len(rs), 'mit_sperre': sum(1 for r in rs if r['gesperrt']),
                      'laengster_s': max(max(r['kammerlauf_s'] or [0]) for r in rs)} for v, rs in je.items()}
zeile(f"STUFE2-EICHUNG: {aus['eichung']}")
(A / 'AUSWERTUNG.txt').write_text('\n'.join(z) + '\n')
(A / 'AUSWERTUNG.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1, default=str))
