"""Versiegelte Schwächen S1–S5 nach „behoben heißt verschwunden" — eigene Messung für abschluss-03.

Wie nachtrag_2_schwaechen.py (Lauf 37), aber an drei Ständen: Ausgang (Quelle /root/versandwerk-t3-02), Endstand
Lauf 37 (lauf37-gen8) und Endstand Lauf 38 (lauf38-gen16). Die Endstände kommen aus den Lazarus-Archiven und werden vor
der Messung gegen die Prüfsumme der Lauf-DB geprüft (Schnappschuss mit WAL, nur gelesen). Der Gegenzeuge ist versiegelt
und wird nur gelesen. rc des Gegenzeugen ist sein Urteil (0 = keine Verletzung, 1 = mindestens eine), kein
Gesundheitszustand; ein Absturz zeigt sich an fehlender auswertbarer Ausgabe.
Kein Modellaufruf. Ausgabe: S1S5-ABSCHLUSS3.json (+ stdout).
"""
import json
import shutil
import sqlite3
import sys
import tarfile
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop.organe import kammer, lazarus  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
PRIV = Path('/root/versiegelt/t3-versandwerk')
DB = '/root/biotop-t3/schnappschuss-abschluss3/t3.db'
AUS = Path('/root/biotop-t3/abschluss3/S1S5-ABSCHLUSS3.json')

SKRIPT = ("import fs from 'node:fs';"
          "if(!fs.existsSync('node_modules'))fs.symlinkSync('/opt/biotop-ts/node_modules','node_modules','dir');"
          "import {quellenbau} from './_messgeraet/ts/bau.mjs';"
          "const b=quellenbau();if(!b.gueltig||!b.baut){console.error(JSON.stringify(b));process.exit(2);}"
          "process.argv[2]='/werk';await import('./_gegenzeugen.mjs');")

ts = Path('/root/biotop/biotop/kern/ts')
extra = {'_messgeraet/ts/' + p.name: p.read_text() for p in ts.iterdir() if p.is_file()}
extra['_gegenzeugen.mjs'] = (PRIV / 'gegenzeugen.mjs').read_text()
extra['_siegelpruefung.mjs'] = SKRIPT

c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
c.row_factory = sqlite3.Row
staende = {'ausgang': Path('/root/versandwerk-t3-02')}
pruef = {}
for lauf, gen in ((37, 8), (38, 16)):
    z = c.execute('SELECT tag, pruefsumme, archiv FROM lazarus WHERE lauf_id=? AND generation=?', (lauf, gen)).fetchone()
    ziel = Path(f'/tmp/s1s5-abschluss3/{z["tag"]}')
    shutil.rmtree(ziel, ignore_errors=True)
    ziel.mkdir(parents=True)
    with tarfile.open(z['archiv']) as t:
        t.extractall(ziel, filter='data')
    ps, n = lazarus.pruefsumme_werk(ziel)
    pruef[z['tag']] = {'erwartet': z['pruefsumme'], 'gemessen': ps, 'stimmt': ps == z['pruefsumme'], 'dateien': n}
    print(f'{z["tag"]}: Prüfsumme {"stimmt" if ps == z["pruefsumme"] else "WEICHT AB"} ({n} Dateien)')
    if ps != z['pruefsumme']:
        raise SystemExit(f'Lazarus-Stand {z["tag"]} weicht von der DB ab — keine Messung')
    staende[z['tag']] = ziel

erg = {}
for name, werk in staende.items():
    e = kammer.ausfuehren(werk, ['node', '_siegelpruefung.mjs'], dateien=extra, zeitlimit_s=240)
    try:
        d = json.loads(e.stdout)
    except (ValueError, TypeError):
        print(f'{name}: keine auswertbare Ausgabe, rc={e.rc}\n{(e.stderr or "")[:800]}')
        erg[name] = {'fehler': (e.stderr or '')[:400], 'rc': e.rc}
        continue
    erg[name] = d
    print(f'\n=== {name} ===  rc={e.rc}  modus={d.get("modus")}')
    for x in d.get('ergebnisse', []):
        rest = {k: v for k, v in x.items() if k not in ('id', 'verletzt')}
        print(f"  {x.get('id', '?'):<4} verletzt={str(x.get('verletzt')):<6} {json.dumps(rest, ensure_ascii=False)[:160]}")

a = {x['id']: x['verletzt'] for x in (erg.get('ausgang') or {}).get('ergebnisse', [])}
vergleich = {}
for name in staende:
    if name == 'ausgang':
        continue
    b = {x['id']: x['verletzt'] for x in (erg.get(name) or {}).get('ergebnisse', [])}
    behoben = [i for i in a if a[i] and b.get(i) is False]
    offen = [i for i in a if a[i] and b.get(i) is not False]
    vergleich[name] = {'endstand': b, 'behoben': behoben, 'offen': offen,
                       'anteil_prozent': round(100 * len(behoben) / len(a), 1) if a else None}
    print(f'\n{name}: behoben {len(behoben)} von {len(a)} = {vergleich[name]["anteil_prozent"]} %  {behoben} | offen {offen}'
          f' | Schwelle 80 %: {"erreicht" if a and 100 * len(behoben) / len(a) >= 80 else "NICHT erreicht"}')

AUS.write_text(json.dumps({'pruefsummen': pruef, 'ausgang': a, 'vergleich': vergleich, 'roh': erg, 'schwelle_prozent': 80},
                          ensure_ascii=False, indent=1))
