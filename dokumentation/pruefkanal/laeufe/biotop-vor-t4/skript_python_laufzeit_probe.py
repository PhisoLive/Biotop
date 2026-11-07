"""Review vor T4 Nr. 8b: den Python-Zweig der gepaarten Laufzeit einmal in der Kammer ausführen (T4 ist Python).

Werk: /root/uebungswerk-p2 (lagerhaus, Python, Phase-2-Ausgang), Referenzlast des Kerns, Kammerimage biotop-kammer:1.
Probe: Vorgeneration gegen denselben Stand (Kandidat ohne Änderung) → gültig, n = 5 je Seite, Verhältnis je Bereich nahe 1.
Gegenprobe: Kandidat mit Syntaxfehler in einem Modul → gültig False, Seite 'kandidat' (Messgerätausfall, kein Urteil).
Kein Modellaufruf. Ausgabe: PYTHON-LAUFZEIT-PROBE.json/.txt."""
import json
import sys
import time
import traceback
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop import lauf as L  # noqa: E402
from biotop.kern import messgeraet  # noqa: E402
from biotop.organe import kammer, landkarte  # noqa: E402

kammer.IMAGE = 'biotop-kammer:1'
W = Path('/root/uebungswerk-p2')
PAKET = 'lagerhaus'
aus = {'werk': str(W), 'image': kammer.IMAGE}
try:
    bereiche = landkarte.bereiche_finden(W, PAKET)
    ref = L._referenzlast('lagerhaus', PAKET)
    aus['bereiche'] = bereiche
    aus['referenzlast_vorhanden'] = bool(ref)
    t0 = time.monotonic()
    r = messgeraet.laufzeit_gepaart(W, bereiche, PAKET, ref, None, None)
    aus['probe'] = {'gueltig': r.get('gueltig'), 'n': r.get('n'), 'grund': r.get('grund'), 'dauer_s': round(time.monotonic() - t0, 1),
                    'bereiche': {b: {'basis': x.get('basis'), 'kandidat': x.get('kandidat'),
                                     'verhaeltnis': round(x['kandidat'] / x['basis'], 3) if x.get('basis') and x.get('kandidat') else None,
                                     'basis_werte': x.get('basis_werte'), 'kandidat_werte': x.get('kandidat_werte')}
                                 for b, x in (r.get('bereiche') or {}).items()}}
    # Lauf 1 brach lagerhaus/bericht/auswertung.py — ein Modul, das die Referenzlast nicht importiert: Gegenprobe blind
    # (gültig True). Jetzt ein Modul, das die Referenzlast ausdrücklich importiert (`from lagerhaus.formeln.auswertung import`).
    ziel = W / PAKET / 'formeln' / 'auswertung.py'
    rel = str(ziel.relative_to(W))
    t0 = time.monotonic()
    g = messgeraet.laufzeit_gepaart(W, bereiche, PAKET, ref, None, {rel: ziel.read_text() + '\ndef kaputt(:\n'})
    aus['gegenprobe'] = {'datei': rel, 'gueltig': g.get('gueltig'), 'seite': g.get('seite'), 'grund': str(g.get('grund'))[:400],
                         'dauer_s': round(time.monotonic() - t0, 1)}
except Exception as e:  # ein gescheiterter Probelauf ist ein Befund
    aus['fehler'] = f'{type(e).__name__}: {e}'
    aus['traceback'] = traceback.format_exc()[-2500:]
Path('/root/biotop-vor-t4/PYTHON-LAUFZEIT-PROBE.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1))
print(json.dumps(aus, ensure_ascii=False, indent=1)[:4000])
