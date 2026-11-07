"""Ändert der Cache aus Gen 6 das Verhalten? Selbst gemessen, nicht übernommen.

Der Review behauptet: `geordnet()` cacht auf der Array-REFERENZ und prüft nur die
Länge. Wird derselbe Array in place geändert, liefert der Cache veraltete Werte.

Hier wird der ECHTE Endstand des Werks in der Kammer ausgeführt — nicht ein Nachbau.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop.organe import kammer
kammer.IMAGE = 'biotop-kammer:ts1'

AUSGANG = Path('/root/versandwerk-t3-02')
ENDE = Path('/root/biotop/daten/werke/versandwerk-t3-02')

PROBE = """
import fs from 'node:fs';
if (!fs.existsSync('node_modules')) fs.symlinkSync('/opt/biotop-ts/node_modules','node_modules','dir');
import { quellenbau } from './_messgeraet/ts/bau.mjs';
const b = quellenbau();
if (!b.gueltig || !b.baut) { console.error(JSON.stringify(b).slice(0,1200)); process.exit(2); }
const { quantil, spannweite } = await import('/werk/dist/zahlen/statistik.js');

const werte = [1, 2, 3];
const q1 = quantil(werte, 1);
const s1 = spannweite([1, 9]);

// Denselben Array in place aendern: gleiche Referenz, gleiche Laenge.
werte[0] = 100; werte[1] = 200; werte[2] = 300;
const q2 = quantil(werte, 1);

const werte2 = [1, 9];
const s2a = spannweite(werte2);
werte2[0] = 1; werte2[1] = 81;
const s2b = spannweite(werte2);

console.log(JSON.stringify({
  quantil_vor_mutation: q1,
  quantil_nach_mutation: q2,
  quantil_erwartet_nach_mutation: 300,
  quantil_korrekt: q2 === 300,
  spannweite_vor: s2a,
  spannweite_nach_mutation: s2b,
  spannweite_erwartet: 80,
  spannweite_korrekt: s2b === 80,
}));
"""

ts = Path('/root/biotop/biotop/kern/ts')
extra = {'_messgeraet/ts/' + p.name: p.read_text() for p in ts.iterdir() if p.is_file()}
extra['_probe.mjs'] = PROBE

for name, werk in (('AUSGANG (ohne Cache)', AUSGANG), ('ENDSTAND (mit Cache)', ENDE)):
    e = kammer.ausfuehren(werk, ['node', '_probe.mjs'], dateien=extra, zeitlimit_s=180)
    print(f'=== {name} ===  rc={e.rc}')
    if e.rc != 0:
        print('  stderr:', (e.stderr or '')[:500])
        continue
    d = json.loads(e.stdout)
    for k, v in d.items():
        print(f'  {k:<34} {v}')
    print()
