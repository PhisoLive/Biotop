"""Sicherheitsminderungen in Lauf 38 durch die Fehlalarm-Regel: Welche waren bloße Umformungen?

Eigene Messung statt der Dateien des Unteragenten (Entscheidung Chat-Claude, 23.09.). Geprüft werden die Kandidaten
K3045, K3212, K3260, K3324 und zum Vergleich K3106. Jeder Kandidat steht gegen seine Vorgeneration aus dem
Lazarus-Archiv, deren Prüfsumme gegen die Lauf-DB geprüft ist (Schnappschuss mit WAL, mode=ro).
Zwei Beobachtungsarten:
(i)  verhaltensvergleich.pruefen, dieselbe Sonde wie im Annahmepfad: die Referenzlast als Korpus, dazu Alias,
     Mutation und Rücksetzung.
(ii) eine allgemeine Randfallsonde: jede exportierte Funktion der geänderten Module mit denselben 30 festen
     Argumentlisten (leere Felder, Negative, Null, Brüche, Zeichenketten, Objekte, null/undefined). Das Ergebnis oder
     die Fehlerklasse wird aufgezeichnet, ebenso die Argumente nach dem Aufruf, weil Eingaben verändert werden können.
Kein Modellaufruf. Kammerläufe laufen netzlos.
"""
import json
import shutil
import sqlite3
import sys
import tarfile
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop import lauf as L  # noqa: E402
from biotop.organe import aegis, kammer, landkarte, lazarus  # noqa: E402
from biotop.organe import verhaltensvergleich as vv  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
S = '/root/biotop-t3/schnappschuss-abschluss3/t3.db'
AUS = Path('/root/biotop-t3/abschluss3/UMFORMUNG-LAUF38.json')
c = sqlite3.connect(f'file:{S}?mode=ro', uri=True)
c.row_factory = sqlite3.Row
REF = L._referenzlast('versandwerk-t3-02', 'src')
FAELLE = [
    '[]', '[[]]', '[[1,2,3]]', '[[3,1,2]]', '[[-5,0,5]]', '[[0.1,0.2,0.3]]', '[[2,2,2,2]]', '[[1000000,2500000]]',
    '[[1,2,3],0]', '[[1,2,3],0.5]', '[[1,2,3],1]', '[[1,2,3],2]', '[[5],1]', '[[10,20,30,40],0.25]', '[[],0.5]',
    '[1]', '[0]', '[-1]', '[2.5]', "['1+2*3']", "['(2+3)*4']", "['10/4']", "['2-5']", "['x']", "['']", "['1+']",
    "[[{menge:1,preis:1000}]]", '[{}]', '[null]', '[undefined]',
]
SONDE = """
import fs from 'node:fs';
if (!fs.existsSync('node_modules')) fs.symlinkSync('/opt/biotop-ts/node_modules','node_modules','dir');
import { quellenbau } from './_messgeraet/ts/bau.mjs';
const b = quellenbau();
if (!b.gueltig || !b.baut) { console.error(JSON.stringify(b).slice(0, 1500)); process.exit(2); }
const MODULE = %s;
const FAELLE = () => [%s];
const kodiere = v => { const s = JSON.stringify(v, (k, x) => (typeof x === 'number' && !Number.isFinite(x)) ? '#' + x : (x === undefined ? '#undefined' : x)); return s === undefined ? '#undefined' : s; };
const beob = {};
for (const pfad of MODULE) {
  const m = await import(pfad);
  beob[pfad + ':exporte'] = Object.keys(m).sort().join(',');
  for (const [name, f] of Object.entries(m)) {
    if (typeof f !== 'function') continue;
    FAELLE().forEach((args, i) => {
      let v;
      try { v = kodiere(f(...args)); } catch (e) { v = 'Fehler:' + (e && e.constructor ? e.constructor.name : '?'); }
      beob[`${pfad}:${name}#${i}`] = v;
      beob[`${pfad}:${name}#${i}:args_danach`] = kodiere(args);
    });
  }
}
console.log(JSON.stringify(beob));
"""
ts = Path('/root/biotop/biotop/kern/ts')
extra = {'_messgeraet/ts/' + p.name: p.read_text() for p in ts.iterdir() if p.is_file()}
FAELLE_JS = ', '.join(FAELLE)
FAELLE_PY = FAELLE

aus = {'faelle': FAELLE_PY}
for kid, basis_gen in ((3045, 0), (3212, 9), (3260, 12), (3324, 13), (3106, 4)):
    k = c.execute('SELECT generation, bereich, diff FROM kandidaten WHERE id=?', (kid,)).fetchone()
    z = c.execute('SELECT archiv, pruefsumme FROM lazarus WHERE lauf_id=38 AND generation=?', (basis_gen,)).fetchone()
    ziel = Path(f'/tmp/umformung/{kid}')
    shutil.rmtree(ziel, ignore_errors=True)
    ziel.mkdir(parents=True)
    with tarfile.open(z['archiv']) as t:
        t.extractall(ziel, filter='data')
    ps, n = lazarus.pruefsumme_werk(ziel)
    if ps != z['pruefsumme']:
        print(f'K{kid}: Vorgeneration lauf38-gen{basis_gen} weicht von der DB ab — übersprungen')
        aus[f'K{kid}'] = {'fehler': 'Prüfsumme'}
        continue
    dateien = aegis.kandidat_dateien(ziel, k['diff'])
    code = {p: (i or '') for p, i in dateien.items() if p.startswith('src/')}
    bereiche = landkarte.bereiche_finden(ziel, 'src')
    r = vv.pruefen(ziel, code, REF, bereiche, {})
    kurz = vv.kurz(r)
    module = ['/werk/dist/' + p[len('src/'):-len('.ts')] + '.js' for p in sorted(code) if p.endswith('.ts')]
    sonde = SONDE % (json.dumps(module), FAELLE_JS)
    seiten = {}
    for seite, overlay in (('vorgeneration', {}), ('kandidat', {p: (i or '') for p, i in dateien.items()})):
        e = kammer.ausfuehren(ziel, ['node', '_sonde.mjs'], dateien={**extra, '_sonde.mjs': sonde, **overlay}, zeitlimit_s=240)
        try:
            seiten[seite] = json.loads(e.stdout)
        except (ValueError, TypeError):
            seiten[seite] = None
            print(f'K{kid} {seite}: Sonde ohne auswertbare Ausgabe, rc={e.rc}: {(e.stderr or "")[:400]}')
    alt, neu = seiten.get('vorgeneration'), seiten.get('kandidat')
    abw = sorted(x for x in set(alt or {}) | set(neu or {}) if (alt or {}).get(x) != (neu or {}).get(x)) if alt and neu else None
    aus[f'K{kid}'] = {'generation': k['generation'], 'bereich': k['bereich'], 'vorgeneration': f'lauf38-gen{basis_gen}',
                      'geaendert': sorted(dateien), 'vv': {x: kurz.get(x) for x in ('ausgefuehrt', 'geurteilt', 'grund_art', 'beobachtungen', 'anzahl_abweichungen')},
                      'vv_abweichungen': (kurz.get('abweichungen') or [])[:12],
                      'rand_beobachtungen': len(set(alt or {}) | set(neu or {})) if alt and neu else None,
                      'rand_abweichend': abw, 'rand_vorher': {x: (alt or {}).get(x) for x in (abw or [])[:12]},
                      'rand_nachher': {x: (neu or {}).get(x) for x in (abw or [])[:12]}}
    a = aus[f'K{kid}']
    print(f"K{kid} (Gen {k['generation']}, {k['bereich']}, gegen lauf38-gen{basis_gen}): ändert {a['geaendert']}")
    print(f"   Verhaltensvergleich: {a['vv']}  {a['vv_abweichungen'][:4]}")
    print(f"   Randfallsonde: {len(abw) if abw is not None else '—'} von {a['rand_beobachtungen']} Beobachtungen abweichend")
    for x in (abw or [])[:8]:
        print(f"      ≠ {x}: vorher {(alt or {}).get(x)!s:.90}  nachher {(neu or {}).get(x)!s:.90}")
AUS.write_text(json.dumps(aus, ensure_ascii=False, indent=1, default=str))
print('\nBeleg:', AUS)
