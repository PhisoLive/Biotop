"""Diagnose Python-Sonde am speicherwerk (Kammer biotop-kammer:1): drei Kandidaten durch verhaltensvergleich.pruefen,
ohne deckende Tests. Erwartung: zwischenspeicher_falsch → nicht tragfähig mit @mutation-/@nach_ruecksetzung-Abweichung;
zwischenspeicher_richtig → tragfähig, 0 Abweichungen; weissraum_falsch → nicht tragfähig mit ~form-Abweichung."""
import json
import shutil
import sys
import time
from pathlib import Path

sys.path.insert(0, '/root/biotop')
sys.path.insert(0, '/root/biotop/tests')
import speicherwerk as SW  # noqa: E402
from biotop.organe import aegis, kammer  # noqa: E402
from biotop.organe import verhaltensvergleich as vv  # noqa: E402

kammer.IMAGE = 'biotop-kammer:1'
W = Path('/tmp/speicherwerk-diagnose')
shutil.rmtree(W, ignore_errors=True)
SW.anlegen(W)
aus = {}
for name, diff in (('zwischenspeicher_falsch', SW.zwischenspeicher_falsch()), ('zwischenspeicher_richtig', SW.zwischenspeicher_richtig()),
                   ('weissraum_falsch', SW.weissraum_falsch())):
    code = {p: i for p, i in aegis.kandidat_dateien(W, diff).items() if not p.startswith('tests/')}
    t0 = time.monotonic()
    r = vv.pruefen(W, code, SW.REFERENZLAST, ['zahlen', 'text'], {"tests": [], "aufrufe": []})
    k = vv.kurz(r)
    aus[name] = {x: k.get(x) for x in ('sprache', 'geurteilt', 'tragfaehig', 'grund_art', 'beobachtete_funktionen', 'beobachtungen',
                                       'anzahl_abweichungen', 'randfaelle', 'formvarianten', 'ungedeckt', 'werte', 'eingaben', 'korpus')}
    aus[name]['dauer_s'] = round(time.monotonic() - t0, 1)
    print(name, json.dumps(aus[name], ensure_ascii=False)[:1400], '\n')
Path('/root/biotop-vor-t4-02/py/DIAGNOSE-PY-SONDE.json').parent.mkdir(parents=True, exist_ok=True)
Path('/root/biotop-vor-t4-02/py/DIAGNOSE-PY-SONDE.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1))
