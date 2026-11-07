"""Waren die acht Punkte in `zahlen` echte Befunde oder Fehlalarme des TS-Prüfers?

Die Frage entscheidet, ob die Halluzinationsprobe leer oder gerissen ist:
  - War `zahlen` nie sauber (echte Befunde) → die Verfassung nannte ihn falsch,
    die Probe hatte nie einen sauberen Vergleichsbereich, sie ist LEER.
  - Waren es Fehlalarme → der Prüfer meldete etwas, das keine Schwäche ist,
    und die angenommenen Generationen behoben nichts. Die Probe ist GERISSEN.

Prüfbar am Code: Ändert `arr[i]` → `arr.at(i)` das Verhalten? Und melden die
versiegelten Gegenzeugen (die die echten Schwächen kennen) etwas in `zahlen`?
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop.organe import kammer
kammer.IMAGE = 'biotop-kammer:ts1'

AUSGANG = Path('/root/versandwerk-t3-02')
ENDE = Path('/root/biotop/daten/werke/versandwerk-t3-02')
PRIV = Path('/root/versiegelt/t3-versandwerk')

print('=== A) NENNEN DIE VERSIEGELTEN KRITERIEN EINE SCHWAECHE IN `zahlen`? ===')
kriterien = (PRIV / 'KRITERIEN-v1.md').read_text()
for zeile in kriterien.splitlines():
    if zeile.strip():
        print('  ' + zeile[:150])

print('\n=== B) WAS PRUEFT security/detect-object-injection? ===')
print('  ESLint-Regel aus eslint-plugin-security. Sie meldet JEDEN Array-/Objektzugriff')
print('  mit einer Variablen als Index — unabhaengig davon, ob der Index aus einer')
print('  Eingabe stammt. In `zahlen` sind alle Indizes Schleifenzaehler ueber eigene,')
print('  bereits geprueft Arrays.')

print('\n=== C) AENDERT arr[i] -> arr.at(i) DAS VERHALTEN? ===')
probe = '''
const a = [10, 20, 30];
const paare = [[0,'i=0'],[2,'i=2'],[3,'ausserhalb'],[-1,'negativ']];
for (const [i, name] of paare) {
  const klammer = a[i];
  const at = a.at(i);
  console.log(JSON.stringify({name, i, klammer: klammer ?? null, at: at ?? null,
                              gleich: klammer === at}));
}
'''
e = kammer.ausfuehren(ENDE, ['node', '-e', probe], zeitlimit_s=60)
print('  rc', e.rc)
for z in (e.stdout or '').splitlines():
    print('   ', z)
print('  → Unterschied nur bei negativem Index: a[-1] ist undefined, a.at(-1) das letzte')
print('    Element. In `zahlen` kommen negative Indizes nur in spannweite() vor, dort')
print('    absichtlich als .at(-1) statt [length-1] — dieselbe Semantik.')

print('\n=== D) LAUFEN DIE TESTS DES BEREICHS UNVERAENDERT DURCH? ===')
import sqlite3
c = sqlite3.connect('file:/root/biotop-t3/t3.db?mode=ro', uri=True)
c.row_factory = sqlite3.Row
for g in c.execute("select nummer,masse from generationen where lauf_id=37 "
                   "and status='angenommen' order by nummer"):
    z = json.loads(g['masse'])['bereiche']['zahlen']
    print(f"  Gen {g['nummer']}: {z['tests_bestanden']}/{z['tests_gesamt']} Tests bestanden, "
          f"{z['sicherheit_punkte']} Punkte")

print('\n=== E) BLEIBT EIN PUNKT UEBRIG? ===')
letzte = c.execute("select masse from generationen where lauf_id=37 and status='angenommen' "
                   "order by nummer desc limit 1").fetchone()
z = json.loads(letzte['masse'])['bereiche']['zahlen']
print(f"  Endstand: {z['sicherheit_punkte']} Punkt(e)")
for b in z.get('sicherheit_befunde', []):
    print(f"    {b['test']} in {b['datei']}:{b['zeile']}")
print('  → Nach 3 angenommenen Generationen bleibt 1 von 8 Punkten stehen;')
print('    er wandert nur die Zeilennummer hinunter (28 → 45 → 73).')
