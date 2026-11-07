"""Torzeile 1: Halluzinationsprobe — war `zahlen` der saubere Vergleichsbereich?

Die Verfassung nennt `zahlen` als sauberen Bereich. Gemessen wurden dort acht
Sicherheitspunkte im Ausgangszustand, und drei angenommene Generationen änderten ihn.
Beides zusammen geht nicht. Diese Prüfung stellt fest, WAS geändert wurde und WELCHE
Regel der Prüfer jeweils meldete — ohne Deutung vorweg.
"""
import json
import sqlite3
from pathlib import Path

c = sqlite3.connect('file:/root/biotop-t3/t3.db?mode=ro', uri=True)
c.row_factory = sqlite3.Row

print('=== A) SICHERHEITSBEFUNDE IN `zahlen` JE GENERATION ===')
for g in c.execute("select nummer,status,masse from generationen where lauf_id=37 "
                   "and status='angenommen' order by nummer"):
    m = json.loads(g['masse'])
    z = m['bereiche']['zahlen']
    print(f"\n  Gen {g['nummer']}: {z['sicherheit_punkte']} Punkte, "
          f"{z['tests_bestanden']}/{z['tests_gesamt']} Tests, tote {z['tote_funktionen']}")
    for b in z.get('sicherheit_befunde', []):
        print(f"      {b['test']:<34} {b['schwere']:<7} {b['punkte']}P  "
              f"{b['datei']}:{b['zeile']}  {b['text'][:44]}")

print('\n\n=== B) DIE ANGENOMMENEN KANDIDATEN IN `zahlen` ===')
for k in c.execute("select id,generation,bereich,status,substr(grund,1,120) g,diff,"
                   "substr(begruendung,1,200) b from kandidaten "
                   "where lauf_id=37 and bereich='zahlen' and status='angenommen' "
                   "order by generation"):
    print(f"\n  --- Gen {k['generation']}, Kandidat {k['id']} ---")
    print(f"  Grund: {k['g']}")
    print(f"  Begründung des Vorschlags: {k['b']}")
    print('  Diff:')
    for zeile in (k['diff'] or '').splitlines():
        if zeile.startswith(('+++', '---', '@@', '+', '-')):
            print(f'    {zeile[:150]}')

print('\n\n=== C) WELCHE REGEL VERSCHWAND JEWEILS? ===')
vorher = None
for g in c.execute("select nummer,masse from generationen where lauf_id=37 "
                   "and status='angenommen' order by nummer"):
    m = json.loads(g['masse'])
    z = m['bereiche']['zahlen']
    jetzt = {(b['test'], b['datei'], b['zeile']) for b in z.get('sicherheit_befunde', [])}
    if vorher is not None:
        weg = vorher - jetzt
        neu = jetzt - vorher
        if weg or neu:
            print(f"  Gen {g['nummer']}: -{len(weg)} +{len(neu)}")
            for t, d, zl in sorted(weg):
                print(f"      weg: {t} in {d}:{zl}")
            for t, d, zl in sorted(neu):
                print(f"      neu: {t} in {d}:{zl}")
    vorher = jetzt
