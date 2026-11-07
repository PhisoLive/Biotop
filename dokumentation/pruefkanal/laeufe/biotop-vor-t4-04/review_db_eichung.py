"""Review vor T4-04 — Lauf-DB nur lesend (mode=ro): Rauschmessung/Sperren der Läufe 37/38 an Stufe 1 (Tabelle eichung)."""
import sqlite3

con = sqlite3.connect('file:/root/biotop-t3/schnappschuss-abschluss3/t3.db?mode=ro', uri=True)
con.row_factory = sqlite3.Row
spalten = [r[1] for r in con.execute('PRAGMA table_info(eichung)')]
print('Spalten:', spalten)
for r in con.execute('SELECT lauf_id, bereich, median, werte, gesperrt, meldung, erstellt_am FROM eichung '
                     'WHERE lauf_id IN (37, 38) ORDER BY lauf_id, id'):
    werte = r['werte'] or ''
    print(r['lauf_id'], r['bereich'], 'median', r['median'], 'gesperrt', r['gesperrt'], '| werte', werte[:90],
          '|', (r['meldung'] or '')[:80])
con.close()
