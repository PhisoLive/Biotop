"""Zusatzmessungen für abschluss-03 (kein Modellaufruf).

1. Ablehnungsgründe der Anklägerurteile in Lauf 37 und 38 (Schnappschuss mit WAL, nur gelesen), letztes Urteil je
   Kandidat, mit Nenner. Frage: Wie oft entschied ein Laufzeit-Grenzmaß — und in welchem Bereich? Anlass: Im Nachspiel
   auf ruhiger Maschine (0 fremde Container) rissen 8 von 31 Fällen ein Laufzeit-Grenzmaß, die im Lauf bestanden hatten.
   `messgeraet.bestwerte` bildet den Bezug als MINIMUM über alle angenommenen Generationen; die Toleranz ist die Streuung
   von 5 Messungen des unveränderten Werks.
2. Eigene Kammerprobe K3106 (Lauf 38 Gen 5, bericht): Vorgeneration lauf38-gen4 gegen gen4 + Diff K3106, jede
   exportierte Funktion der geänderten Module mit tabellenartigen Eingaben. Frage: Ändert K3106 Verhalten, obwohl der
   Verhaltensvergleich am Annahmepfad (Referenzlast als Korpus) 0 Abweichungen fand (nachspiel/l38_k3106_ohne_eichung)?
"""
import json
import re
import shutil
import sqlite3
import sys
import tarfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop.organe import aegis, kammer, lazarus  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
DB = '/root/biotop-t3/schnappschuss-abschluss3/t3.db'
c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
c.row_factory = sqlite3.Row
aus = {}

print('======== 1. Ablehnungsgründe der Anklägerurteile (letztes Urteil je Kandidat) ========')
for lauf in (37, 38):
    je = {}
    for r in c.execute("SELECT nr, inhalt FROM protokoll WHERE art='aegis.urteil' ORDER BY nr"):
        u = json.loads(r['inhalt'])
        if u.get('lauf_id') == lauf:
            je[u['kandidat']] = u
    status = Counter(u.get('status') for u in je.values())
    arten, lz_eigen, lz_fremd, lz_ids = Counter(), 0, 0, []
    for kid, u in je.items():
        if u.get('status') != 'abgelehnt':
            continue
        g = u.get('grund') or ''
        if g.startswith('Grenzmaß gerissen') and 'laufzeit_ms' in g:
            arten['Grenzmaß Laufzeit'] += 1
            gerissen = set(re.findall(r'(\w+)\.laufzeit_ms', g))
            if u.get('bereich') in gerissen:
                lz_eigen += 1
            else:
                lz_fremd += 1
            lz_ids.append(kid)
        elif g.startswith('Grenzmaß'):
            arten['Grenzmaß sonst'] += 1
        elif g.startswith('Pareto'):
            arten['Pareto'] += 1
        elif g.startswith('Kernmaß unverändert'):
            arten['Kernmaß unverändert'] += 1
        elif g.startswith('Nische schnell'):
            arten['Nische schnell'] += 1
        elif g.startswith('Kammer'):
            arten['Kammer'] += 1
        elif 'Verfassung' in g[:40]:
            arten['Verfassung'] += 1
        else:
            arten['sonst: ' + g[:45]] += 1
    abgelehnt = status.get('abgelehnt', 0)
    print(f'Lauf {lauf}: Kandidaten mit Urteil {len(je)}; Status {dict(status)}')
    for a, n in arten.most_common():
        print(f'   {a:55} {n:>4} von {abgelehnt} Ablehnungen')
    print(f'   davon Laufzeit-Grenzmaß im eigenen Bereich {lz_eigen}, nur in anderen Bereichen {lz_fremd}')
    aus[f'lauf{lauf}'] = {'kandidaten': len(je), 'status': dict(status), 'ablehnungsarten': dict(arten),
                          'laufzeit_grenzmass_eigener_bereich': lz_eigen, 'laufzeit_grenzmass_nur_fremd': lz_fremd,
                          'laufzeit_grenzmass_kandidaten': sorted(lz_ids)}

print('\n======== 2. Kammerprobe K3106 gegen seine Vorgeneration lauf38-gen4 ========')
z = c.execute('SELECT archiv, pruefsumme FROM lazarus WHERE lauf_id=38 AND generation=4').fetchone()
ziel = Path('/tmp/k3106-probe/gen4')
shutil.rmtree(ziel.parent, ignore_errors=True)
ziel.mkdir(parents=True)
with tarfile.open(z['archiv']) as t:
    t.extractall(ziel, filter='data')
ps, n = lazarus.pruefsumme_werk(ziel)
print(f'lauf38-gen4: Prüfsumme {"stimmt" if ps == z["pruefsumme"] else "WEICHT AB"} ({n} Dateien)')
if ps != z['pruefsumme']:
    raise SystemExit('Vorgeneration weicht von der DB ab — keine Probe')
diff = c.execute('SELECT diff FROM kandidaten WHERE id=3106').fetchone()['diff']
dateien = aegis.kandidat_dateien(ziel, diff)
geaendert = sorted(p for p in dateien if p.startswith('src/') and p.endswith('.ts'))
print('K3106 ändert:', sorted(dateien))
module = ['/werk/dist/' + p[len('src/'):-len('.ts')] + '.js' for p in geaendert]
SONDE = """
import fs from 'node:fs';
if (!fs.existsSync('node_modules')) fs.symlinkSync('/opt/biotop-ts/node_modules','node_modules','dir');
import { quellenbau } from './_messgeraet/ts/bau.mjs';
const b = quellenbau();
if (!b.gueltig || !b.baut) { console.error(JSON.stringify(b).slice(0, 1500)); process.exit(2); }
const MODULE = %s;
const FAELLE = [[["",""]], [["a","bb"],["ccc",""]], [], [[""]], [["x"]], [["",""],["",""]], [["1","22","333"]]];
const beob = {};
for (const pfad of MODULE) {
  const m = await import(pfad);
  beob[pfad + ':exporte'] = Object.keys(m).sort().join(',');
  for (const [name, f] of Object.entries(m)) {
    if (typeof f !== 'function') continue;
    for (const [i, fall] of FAELLE.entries()) {
      try { beob[`${pfad}:${name}#${i}`] = JSON.stringify(f(JSON.parse(JSON.stringify(fall)))); }
      catch (e) { beob[`${pfad}:${name}#${i}`] = 'Fehler:' + (e && e.constructor ? e.constructor.name : '?'); }
    }
  }
}
console.log(JSON.stringify(beob));
""" % json.dumps(module)
ts = Path('/root/biotop/biotop/kern/ts')
extra = {'_messgeraet/ts/' + p.name: p.read_text() for p in ts.iterdir() if p.is_file()}
extra['_sonde.mjs'] = SONDE
ergebnisse = {}
for seite, overlay in (('vorgeneration', {}), ('kandidat', {p: (i or '') for p, i in dateien.items()})):
    e = kammer.ausfuehren(ziel, ['node', '_sonde.mjs'], dateien={**extra, **overlay}, zeitlimit_s=240)
    try:
        ergebnisse[seite] = json.loads(e.stdout)
    except (ValueError, TypeError):
        print(f'{seite}: keine auswertbare Ausgabe, rc={e.rc}: {(e.stderr or "")[:600]}')
        ergebnisse[seite] = None
alt, neu = ergebnisse.get('vorgeneration'), ergebnisse.get('kandidat')
if alt and neu:
    schluessel = sorted(set(alt) | set(neu))
    abw = [k for k in schluessel if alt.get(k) != neu.get(k)]
    print(f'Beobachtungen {len(schluessel)}, abweichend {len(abw)}')
    for k in abw:
        print(f'   ≠ {k}: vorher {alt.get(k)}  nachher {neu.get(k)}')
    aus['k3106'] = {'geaendert': sorted(dateien), 'beobachtungen': len(schluessel), 'abweichend': abw,
                    'vorher': {k: alt.get(k) for k in abw}, 'nachher': {k: neu.get(k) for k in abw}}
Path('/root/biotop-t3/abschluss3/ZUSATZ-ABSCHLUSS3.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1))
