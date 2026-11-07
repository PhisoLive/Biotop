"""Kammerprobe der neuen Verhaltenssonde (Vorbedingung 2), vor dem Nachspiel durch den Annahmepfad.

K3106 gegen lauf38-gen4 und K3121 gegen lauf38-gen4, direkt über verhaltensvergleich.pruefen. Die Lauf-DB wird nur
gelesen (Schnappschuss, mode=ro), die Werkstände werden nach /tmp entpackt. Kein Modellaufruf.
Erwartung: K3106 wird erkannt (ungedeckte Abweichung in tabellenbreiten, Randfall), K3121 weiterhin erkannt,
x von y Funktionen beobachtet steht im Urteil.
"""
import json
import shutil
import sqlite3
import sys
import tarfile
import time
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop import lauf as L  # noqa: E402
from biotop.organe import aegis, kammer, landkarte, lazarus  # noqa: E402
from biotop.organe import verhaltensvergleich as vv  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
c = sqlite3.connect('file:/root/biotop-t3/schnappschuss-abschluss3/t3.db?mode=ro', uri=True)
c.row_factory = sqlite3.Row
REF = L._referenzlast('versandwerk-t3-02', 'src')
aus = {}
for kid, gen in ((3106, 4), (3121, 4), (3324, 13)):
    z = c.execute('SELECT archiv, pruefsumme FROM lazarus WHERE lauf_id=38 AND generation=?', (gen,)).fetchone()
    ziel = Path(f'/tmp/vv-probe/{kid}')
    shutil.rmtree(ziel, ignore_errors=True)
    ziel.mkdir(parents=True)
    with tarfile.open(z['archiv']) as t:
        t.extractall(ziel, filter='data')
    ps, _ = lazarus.pruefsumme_werk(ziel)
    assert ps == z['pruefsumme'], f'K{kid}: Vorgeneration weicht ab'
    diff = c.execute('SELECT diff FROM kandidaten WHERE id=?', (kid,)).fetchone()[0]
    dateien = aegis.kandidat_dateien(ziel, diff)
    code = {p: (i or '') for p, i in dateien.items() if not p.startswith('tests/')}
    t0 = time.monotonic()
    r = vv.pruefen(ziel, code, REF, landkarte.bereiche_finden(ziel, 'src'), {})
    k = vv.kurz(r)
    aus[f'K{kid}'] = {**{x: k.get(x) for x in ('geurteilt', 'tragfaehig', 'grund_art', 'beobachtete_funktionen', 'beobachtungen',
                                                  'anzahl_abweichungen', 'randfaelle', 'unbeobachtet', 'entfernte_funktionen')},
                      'ungedeckt': (k.get('ungedeckt') or [])[:8], 'werte': k.get('werte'), 'dauer_s': round(time.monotonic() - t0, 1)}
    print(f'K{kid}: {json.dumps(aus[f"K{kid}"], ensure_ascii=False)[:1500]}')
Path('/root/biotop-vor-t4/VV-KAMMERPROBE.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1))
