"""Kernmaß von Lauf 37 ohne die Punkte, die nur den Prüfer zufriedenstellten.

Befund: Alle Sicherheitsminderungen außer einer stammen aus
`security/detect-object-injection` — einer Regel, die jeden variablen Index meldet,
unabhängig von der Herkunft. Die versiegelten Kriterien nennen keine solche Schwäche.

Die eine Ausnahme: `no-new-func` in tarife/ausdruck.ts, 10 Punkte, HIGH — das ist S1,
die echte Schwäche. Sie wurde in Gen 3 durch einen echten Parser ersetzt.

Hier wird das Kernmaß neu gerechnet, wenn detect-object-injection nicht zählt.
"""
import json
import sqlite3

c = sqlite3.connect('file:/root/biotop-t3/t3.db?mode=ro', uri=True)
c.row_factory = sqlite3.Row
L = 37
FEHLALARM = 'security/detect-object-injection'

print('=== KERNMASS MIT UND OHNE DIE FEHLALARM-REGEL ===')
print(f'{"Gen":>4} {"gemeldet":>9} {"bereinigt":>10} {"Diff":>6}   Zusammensetzung bereinigt')
zeilen = []
for g in c.execute("select nummer,masse from generationen where lauf_id=? and status='angenommen' "
                   "order by nummer", (L,)):
    m = json.loads(g['masse'])
    roh = echt = 0
    teile = []
    for b in sorted(m['bereiche']):
        e = m['bereiche'][b]
        sp_roh = e['sicherheit_punkte']
        sp_echt = sum(x['punkte'] for x in e.get('sicherheit_befunde', [])
                      if x['test'] != FEHLALARM)
        roh += e['tests_fehlgeschlagen'] + sp_roh + e['tote_funktionen']
        echt += e['tests_fehlgeschlagen'] + sp_echt + e['tote_funktionen']
        if sp_echt or e['tests_fehlgeschlagen'] or e['tote_funktionen']:
            teile.append(f"{b}:{sp_echt}s/{e['tests_fehlgeschlagen']}t/{e['tote_funktionen']}d")
    zeilen.append((g['nummer'], -roh, -echt))
    print(f"{g['nummer']:>4} {-roh:>9} {-echt:>10} {roh-echt:>6}   {' '.join(teile) or '(alles null)'}")

start_roh, start_echt = zeilen[0][1], zeilen[0][2]
ende_roh, ende_echt = zeilen[-1][1], zeilen[-1][2]
print(f'\n  gemeldet : {start_roh} → {ende_roh}  (Gewinn {ende_roh - start_roh})')
print(f'  bereinigt: {start_echt} → {ende_echt}  (Gewinn {ende_echt - start_echt})')
print(f'\n  Von {ende_roh - start_roh} gemeldeten Punkten Gewinn sind')
print(f'  {ende_echt - start_echt} echt und {(ende_roh - start_roh) - (ende_echt - start_echt)} Fehlalarm-Bereinigung.')

print('\n=== WAS DER ECHTE GEWINN IST ===')
erste = json.loads(c.execute("select masse from generationen where lauf_id=? and nummer=0",
                             (L,)).fetchone()['masse'])
letzte = json.loads(c.execute("select masse from generationen where lauf_id=? and status='angenommen' "
                              "order by nummer desc limit 1", (L,)).fetchone()['masse'])
for b in sorted(erste['bereiche']):
    a, z = erste['bereiche'][b], letzte['bereiche'][b]
    ae = sum(x['punkte'] for x in a.get('sicherheit_befunde', []) if x['test'] != FEHLALARM)
    ze = sum(x['punkte'] for x in z.get('sicherheit_befunde', []) if x['test'] != FEHLALARM)
    if ae != ze or a['tote_funktionen'] != z['tote_funktionen'] or a['tests_fehlgeschlagen'] != z['tests_fehlgeschlagen']:
        print(f'  {b}: echte Sicherheit {ae}→{ze}, tote {a["tote_funktionen"]}→{z["tote_funktionen"]}, '
              f'Testfehler {a["tests_fehlgeschlagen"]}→{z["tests_fehlgeschlagen"]}')

json.dump({'verlauf': [{'gen': n, 'gemeldet': r, 'bereinigt': e} for n, r, e in zeilen],
           'gemeldet_gewinn': ende_roh - start_roh,
           'bereinigt_gewinn': ende_echt - start_echt,
           'fehlalarm_anteil': (ende_roh - start_roh) - (ende_echt - start_echt),
           'regel': FEHLALARM},
          open('/root/biotop-t3/NACHTRAG-3-KERNMASS.json', 'w'), ensure_ascii=False, indent=2)
