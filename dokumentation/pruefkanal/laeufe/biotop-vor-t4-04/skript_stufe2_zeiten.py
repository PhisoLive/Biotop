"""Stufe 2 der Vergleichslast (Behebungsrunde 4 vor T4, Entscheidung 1): Dauer eines Kammerlaufs der Laufzeitmessung
und Laufzeiten je Bereich, Stufe 1 gegen Stufe 2, an den Vorgenerationen von K2904 (Lauf 37) und K3091 (Lauf 38) und an
beiden Kandidaten. Zustand über nachspiel.vorbereiten (Lazarus-Vorgeneration, Prüfsumme), T3-DB nur gelesen (Kopie).
Je Stand und Stufe 3 Kammerläufe (typescript.laufzeit: 3 Aufwärm- und 5 Messdurchläufe je Bereich, Median).
Kein Modellaufruf. Aufruf: python stufe2_zeiten.py > STUFE2-ZEITEN.txt"""
import hashlib
import json
import shutil
import statistics
import sys
import time
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop import nachspiel  # noqa: E402
from biotop import lauf as L  # noqa: E402
from biotop.kern import typescript  # noqa: E402
from biotop.organe import aegis, kammer  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
QUELLE = Path('/root/biotop-t3/schnappschuss-abschluss3/t3.db')
AUS = Path(__file__).with_name('STUFE2-ZEITEN.json')
vorher = hashlib.sha256(QUELLE.read_bytes()).hexdigest()
ergebnis = {}
for kid in (2904, 3091):
    arbeit = Path(f'/tmp/stufe2-zeiten-k{kid}')
    shutil.rmtree(arbeit, ignore_errors=True)
    fall = nachspiel.vorbereiten(QUELLE, kid, arbeit)
    werk, bereiche = fall['werk'], fall['bereiche']
    ref1 = fall['ref']
    ref2 = L._referenzlast('versandwerk-t3-02', fall['paket'], 2)
    assert ref2 and ref2 != ref1, 'Stufe 2 fehlt'
    diff = fall['con'].execute('SELECT diff FROM kandidaten WHERE id=?', (kid,)).fetchone()[0]
    code = {p: i for p, i in (aegis.kandidat_dateien(werk, diff) or {}).items() if not p.startswith('tests/')}
    e = {'bereiche': bereiche, 'vorgeneration': fall['basis_generation'], 'lauf': fall['lauf_id']}
    for stand, dateien in (('vorgeneration', {}), ('kandidat', code)):
        for stufe, ref in (('stufe1', ref1), ('stufe2', ref2)):
            laeufe = []
            for _ in range(3):
                t0 = time.monotonic()
                r = typescript.laufzeit(werk, ref, bereiche, dateien)
                dauer = round(time.monotonic() - t0, 1)
                laeufe.append({'dauer_s': dauer, 'gueltig': r.get('gueltig'), 'grund': str(r.get('grund') or '')[:200],
                               'ms': {b: (r.get('bereiche') or {}).get(b, {}).get('laufzeit_ms') for b in bereiche}})
            e[f'{stand}_{stufe}'] = laeufe
            ms = {b: [x['ms'].get(b) for x in laeufe] for b in bereiche}
            print(f"K{kid} {stand:13} {stufe}: Kammerlauf {[x['dauer_s'] for x in laeufe]} s | "
                  + ' | '.join(f"{b} {[round(v, 2) if v else v for v in ms[b]]}" for b in bereiche), flush=True)
    for stufe in ('stufe1', 'stufe2'):
        q = {}
        for b in bereiche:
            vb = [x['ms'][b] for x in e[f'vorgeneration_{stufe}'] if x['ms'].get(b)]
            vk = [x['ms'][b] for x in e[f'kandidat_{stufe}'] if x['ms'].get(b)]
            if vb and vk:
                q[b] = {'quote_median': round(statistics.median(vk) / statistics.median(vb), 4),
                        'spannweite_vorgeneration': round((max(vb) - min(vb)) / statistics.median(vb), 4),
                        'spannweite_kandidat': round((max(vk) - min(vk)) / statistics.median(vk), 4)}
        e[f'quoten_{stufe}'] = q
        print(f"K{kid} Quoten {stufe}: " + json.dumps(q, ensure_ascii=False), flush=True)
    ergebnis[f'k{kid}'] = e
    fall['con'].close()
    shutil.rmtree(arbeit, ignore_errors=True)
ergebnis['_meta'] = {'t3_db_vorher': vorher, 't3_db_nachher': hashlib.sha256(QUELLE.read_bytes()).hexdigest(),
                     'ref2_sha256': hashlib.sha256(ref2.encode()).hexdigest(), 'kammer': kammer.IMAGE, 'modellaufrufe': 0}
AUS.write_text(json.dumps(ergebnis, ensure_ascii=False, indent=1))
print('t3.db unverändert:', ergebnis['_meta']['t3_db_vorher'] == ergebnis['_meta']['t3_db_nachher'])
