"""Torzeile 2: Versiegelte Schwächen — welche sind nach „behoben heißt verschwunden" weg?

Die fünf Schwächen wurden vor dem Lauf versiegelt und sind dem Schwarm nie gezeigt
worden. Der Gegenzeuge prüft je Schwäche ein Verhalten und meldet `verletzt` als
Boolean. Behoben heißt: der Gegenzeuge meldet am Endstand false, wo er am Ausgang
true meldete — nicht „ein Test wurde geschrieben".

Gemessen wird am Ausgang UND am Endstand, in derselben netzlosen Kammer.
"""
import hashlib
import json
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop.organe import kammer
kammer.IMAGE = 'biotop-kammer:ts1'

PRIV = Path('/root/versiegelt/t3-versandwerk')
STAENDE = {'ausgang': Path('/root/versandwerk-t3-02'),
           'endstand': Path('/root/biotop/daten/werke/versandwerk-t3-02')}

SKRIPT = ("import fs from 'node:fs';"
          "if(!fs.existsSync('node_modules'))fs.symlinkSync('/opt/biotop-ts/node_modules','node_modules','dir');"
          "import {quellenbau} from './_messgeraet/ts/bau.mjs';"
          "const b=quellenbau();if(!b.gueltig||!b.baut){console.error(JSON.stringify(b));process.exit(2);}"
          "process.argv[2]='/werk';await import('./_gegenzeugen.mjs');")

ts = Path('/root/biotop/biotop/kern/ts')
extra = {'_messgeraet/ts/' + p.name: p.read_text() for p in ts.iterdir() if p.is_file()}
extra['_gegenzeugen.mjs'] = (PRIV / 'gegenzeugen.mjs').read_text()
extra['_siegelpruefung.mjs'] = SKRIPT

erg = {}
for name, werk in STAENDE.items():
    e = kammer.ausfuehren(werk, ['node', '_siegelpruefung.mjs'], dateien=extra, zeitlimit_s=240)
    # rc ist das URTEIL des Gegenzeugen, nicht sein Gesundheitszustand: 0 = keine
    # Verletzung mehr, 1 = mindestens eine offen. Ein Absturz zeigt sich daran, dass
    # keine auswertbare Ausgabe kommt — nicht an rc.
    try:
        d = json.loads(e.stdout)
    except (ValueError, TypeError):
        print(f'{name}: keine auswertbare Ausgabe, rc={e.rc}\n{(e.stderr or "")[:800]}')
        erg[name] = {'fehler': (e.stderr or '')[:400], 'rc': e.rc}
        continue
    erg[name] = d
    print(f'\n=== {name.upper()} ===  rc={e.rc}  modus={d.get("modus")}')
    for x in d.get('ergebnisse', []):
        zusatz = ''
        if x.get('id') == 'S5':
            zusatz = f" preise={x.get('preise')} soll={x.get('soll')}"
        if x.get('id') == 'S3':
            zusatz = f" vorher={x.get('vorher')} nachher={x.get('nachher')}"
        if x.get('id') == 'S2':
            zusatz = f" zaehlungen={x.get('zaehlungen')}"
        if x.get('id') == 'S1':
            zusatz = f" abgewiesen={x.get('abgewiesen')} marker={x.get('marker')}"
        if x.get('id') == 'S4':
            zusatz = f" deklarationen={x.get('deklarationen')}"
        print(f"  {x.get('id','?'):<4} verletzt={str(x.get('verletzt')):<6}{zusatz[:110]}")

print('\n=== VERGLEICH: behoben heisst verschwunden ===')
a = {x['id']: x['verletzt'] for x in (erg.get('ausgang') or {}).get('ergebnisse', [])}
b = {x['id']: x['verletzt'] for x in (erg.get('endstand') or {}).get('ergebnisse', [])}
behoben = [i for i in a if a[i] and not b.get(i, True)]
offen = [i for i in a if a[i] and b.get(i, True)]
print(f'  Schwaechen versiegelt : {len(a)}')
print(f'  am Ausgang verletzt   : {sum(1 for v in a.values() if v)}')
print(f'  am Endstand verletzt  : {sum(1 for v in b.values() if v)}')
print(f'  BEHOBEN               : {len(behoben)} von {len(a)} = {100*len(behoben)/len(a):.0f} %  {behoben}')
print(f'  offen                 : {len(offen)}  {offen}')
print(f'  Torschwelle 80 %      : {"ERREICHT" if 100*len(behoben)/len(a) >= 80 else "NICHT ERREICHT"}')

json.dump({'ausgang': a, 'endstand': b, 'behoben': behoben, 'offen': offen,
           'anteil_prozent': round(100 * len(behoben) / len(a), 1) if a else None,
           'schwelle': 80},
          open('/root/biotop-t3/NACHTRAG-2-SCHWAECHEN.json', 'w'), ensure_ascii=False, indent=2)
