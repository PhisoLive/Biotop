"""Nachzählungen für abschluss-03 (nur lesend, Schnappschuss mit WAL; t3.db einmal mit immutable=1 zum Vergleich).

1. Kasse: Sind die 49 wegen der WAL übersehenen Zeilen in 9,7286 € enthalten? Harte Grenze 10 €.
2. K3091: Annahmegrund und Laufzeit, gemessen im Lauf (REVIEW-03 Nr. 1).
3. Lauf 37: angenommene Kandidaten, die den sauberen Bereich `zahlen` ändern (REVIEW-03 Nr. 9).
4. Laufzeit-Grenzmaß als Ablehnungsgrund, direkt und über das Projektgedächtnis (REVIEW-03 Nr. 7).
5. Doppelung, drei Stufen: Ansagefilter, Aufnahmesperre C, VB1-Torzeile (REVIEW-03 Nr. 8).
"""
import json
import re
import sqlite3

S = '/root/biotop-t3/schnappschuss-abschluss3/t3.db'
c = sqlite3.connect(f'file:{S}?mode=ro', uri=True)
c.row_factory = sqlite3.Row
aus = {}
lj = json.loads

print('======== 1. Kasse ========')
alt = sqlite3.connect('file:/root/biotop-t3/t3.db?mode=ro&immutable=1', uri=True)
q = 'SELECT COUNT(*), SUM(kosten_eur) FROM kasse WHERE lauf_id >= 26'
n_alt, e_alt = alt.execute(q).fetchone()
n_neu, e_neu = c.execute(q).fetchone()
ids_alt = {r[0] for r in alt.execute('SELECT id FROM kasse')}
extra = [dict(r) for r in c.execute('SELECT id, lauf_id, zeit, kosten_eur, zweck FROM kasse ORDER BY id') if r['id'] not in ids_alt]
fehlend = sum(1 for (i,) in alt.execute('SELECT id FROM kasse') if not c.execute('SELECT 1 FROM kasse WHERE id=?', (i,)).fetchone())
je_lauf = [dict(r) for r in c.execute('SELECT lauf_id, COUNT(*) n, SUM(kosten_eur) eur FROM kasse WHERE lauf_id>=26 GROUP BY lauf_id ORDER BY lauf_id')]
k = {'ohne_wal': {'zeilen': n_alt, 'eur': round(e_alt, 6)}, 'mit_wal': {'zeilen': n_neu, 'eur': round(e_neu, 6)},
     'nur_in_wal': {'zeilen': len(extra), 'eur': round(sum(x['kosten_eur'] or 0 for x in extra), 6),
                    'laeufe': sorted({x['lauf_id'] for x in extra}), 'von': extra[0]['zeit'] if extra else None,
                    'bis': extra[-1]['zeit'] if extra else None, 'ids': [extra[0]['id'], extra[-1]['id']] if extra else None},
     'zeilen_ohne_wal_im_schnappschuss_fehlend': fehlend,
     'summe_der_gerundeten_teilbetraege': round(sum(round(x['eur'], 6) for x in je_lauf), 6),
     'grenze_eur': 10.0, 'rest_eur': round(10.0 - e_neu, 6)}
k['aufgeht'] = abs(k['ohne_wal']['eur'] + k['nur_in_wal']['eur'] - k['mit_wal']['eur']) < 1e-6 and k['ohne_wal']['zeilen'] + k['nur_in_wal']['zeilen'] == k['mit_wal']['zeilen']
aus['kasse'] = k
print(json.dumps(k, ensure_ascii=False, indent=1))
print('je Lauf:', [(x['lauf_id'], x['n'], round(x['eur'], 6)) for x in je_lauf])

print('\n======== 2. K3091 im Lauf 38 (Urteil 23639) ========')
u = lj(c.execute('SELECT inhalt FROM protokoll WHERE nr=23639').fetchone()[0])
m = u.get('mass') or {}
km = c.execute('SELECT masse FROM kandidaten WHERE id=3091').fetchone()[0]
km = lj(km) if km else {}
bp = (km.get('_basis_paar') or {}).get('bereiche') or {}
l0 = (bp.get('planung') or {}).get('laufzeit_ms')
l1 = ((km.get('bereiche') or {}).get('planung') or {}).get('laufzeit_ms')
z = {'grund': u.get('grund'), 'zuwachs': m.get('zuwachs'), 'laufzeit_gewinne': m.get('laufzeit_gewinne'),
     'sicherheit_gesunken_in': m.get('sicherheit_gesunken_in'), 'planung_vorgeneration_ms': l0, 'planung_kandidat_ms': l1,
     'planung_aenderung_prozent': round(100 * (l1 / l0 - 1), 1) if l0 and l1 else None}
aus['k3091_lauf'] = z
print(json.dumps(z, ensure_ascii=False))

print('\n======== 3. Lauf 37: angenommene Kandidaten mit Änderung in src/zahlen/ ========')
gen = [r['nummer'] for r in c.execute("SELECT nummer FROM generationen WHERE lauf_id=37 AND status='angenommen' AND nummer>0 ORDER BY nummer")]
ids = []
for r in c.execute("SELECT kandidaten FROM generationen WHERE lauf_id=37 AND status='angenommen' AND nummer>0 ORDER BY nummer"):
    ids += list(((lj(r['kandidaten']) or {}).get('_gewaehlt') or {}).values())
zahlen = []
for kid in ids:
    d = c.execute('SELECT generation, bereich, diff FROM kandidaten WHERE id=?', (kid,)).fetchone()
    if re.search(r'^\+\+\+ b/src/zahlen/', d['diff'] or '', re.M):
        zahlen.append((kid, d['generation'], d['bereich']))
gens_zahlen = sorted({g for _, g, _ in zahlen})
aus['lauf37_zahlen'] = {'angenommene_generationen': gen, 'gewaehlte_kandidaten': sorted(ids), 'aendern_zahlen': zahlen,
                        'generationen_mit_zahlen': gens_zahlen}
print(f'angenommene Generationen (ohne 0): {gen} = {len(gen)}; gewählte Kandidaten {len(ids)}')
print(f'davon ändern src/zahlen/: {zahlen} → Generationen {gens_zahlen} = {len(gens_zahlen)} von {len(gen)}')

print('\n======== 4. Laufzeit-Grenzmaß als Ablehnungsgrund (Kandidatenstatus) ========')
for lauf in (37, 38):
    abg = [dict(r) for r in c.execute("SELECT id, bereich, grund FROM kandidaten WHERE lauf_id=? AND status='abgelehnt'", (lauf,))]
    direkt = [a for a in abg if (a['grund'] or '').startswith('Grenzmaß gerissen') and 'laufzeit_ms' in (a['grund'] or '')]
    gedae = [a for a in abg if (a['grund'] or '').startswith('Wiederholung eines gescheiterten Wegs')
             and 'Grenzmaß gerissen' in (a['grund'] or '') and 'laufzeit_ms' in (a['grund'] or '')]
    fremd = [a for a in direkt + gedae if a['bereich'] not in set(re.findall(r'(\w+)\.laufzeit_ms', a['grund'] or ''))]
    aus[f'grenzmass_lauf{lauf}'] = {'abgelehnt': len(abg), 'direkt': len(direkt), 'ueber_gedaechtnis': len(gedae),
                                    'zusammen': len(direkt) + len(gedae), 'nur_fremde_bereiche': len(fremd)}
    print(f'Lauf {lauf}: abgelehnt {len(abg)}; Laufzeit-Grenzmaß direkt {len(direkt)}, über das Gedächtnis {len(gedae)}, '
          f'zusammen {len(direkt) + len(gedae)}; davon nur in fremden Bereichen gerissen {len(fremd)}')

print('\n======== 5. Doppelung: drei Stufen ========')
for lauf in (37, 38):
    ans = [lj(r['inhalt']) for r in c.execute("SELECT inhalt FROM protokoll WHERE art='aegis.ansage'")]
    ans = [a for a in ans if a.get('lauf_id') == lauf]
    mit = [a for a in ans if a.get('behauptung')]
    dop = [a for a in mit if a.get('ausgefuehrt') is False]      # VB1 auswerten.py: 'bekannt_gesperrt'
    tests = gesperrt = aufrufe = 0
    for r in c.execute("SELECT art, inhalt FROM protokoll WHERE art IN ('immun.aufnahme_geprueft','immun.aufnahme_gesperrt')"):
        d = lj(r['inhalt'])
        if d.get('lauf_id') != lauf:
            continue
        if r['art'] == 'immun.aufnahme_geprueft':
            aufrufe += 1
            tests += d.get('anzahl', 0)
        else:
            gesperrt += 1
    felder = sorted({k for a in ans for k in a})
    aus[f'doppelung_lauf{lauf}'] = {'ansagen': len(ans), 'mit_behauptung': len(mit), 'ansage_gesperrt': len(dop),
                                    'aufnahme_tests': tests, 'aufnahme_gesperrt': gesperrt, 'aufnahme_aufrufe': aufrufe,
                                    'ansage_felder': felder}
    print(f'Lauf {lauf}: Ansagen {len(ans)}, mit Behauptung {len(mit)}, davon gesperrt {len(dop)}'
          f' ({100 * len(dop) / len(mit):.1f} %)' if mit else '', end='')
    print(f' | Aufnahmesperre C: {gesperrt} von {tests} Tests ({100 * gesperrt / tests:.1f} %)' if tests else ' | Aufnahmesperre C: 0 Tests')
    print('   Felder der Ansage:', felder)
json.dump(aus, open('/root/biotop-t3/abschluss3/NACHZAEHLUNG-ABSCHLUSS3.json', 'w'), ensure_ascii=False, indent=1, default=str)
