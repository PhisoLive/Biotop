"""Nachmessung am Commit: der Teilausfall der gepaarten Laufzeit (Befund Runde 1, NACHLESE.json) an echtem Python-Werk.
Werk lagerhaus (Phase-2-Ausgang), Kandidat mit Syntaxfehler in lagerhaus/formeln/auswertung.py (die Referenzlast lädt
das Modul). Erwartung jetzt: gepaarte Messung UNGÜLTIG, Seite kandidat, Bereich benannt. Gegenprobe: gleicher Stand
gegen gleichen Stand → gültig, alle Bereiche mit Wert. Kein Modellaufruf."""
import json
import sys
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop import lauf as L  # noqa: E402
from biotop.kern import messgeraet  # noqa: E402
from biotop.organe import kammer, landkarte  # noqa: E402

kammer.IMAGE = 'biotop-kammer:1'
W = Path('/root/uebungswerk-p2')
bereiche = landkarte.bereiche_finden(W, 'lagerhaus')
ref = L._referenzlast('lagerhaus', 'lagerhaus')
ziel = W / 'lagerhaus' / 'formeln' / 'auswertung.py'
kaputt = messgeraet.laufzeit_gepaart(W, bereiche, 'lagerhaus', ref, None, {'lagerhaus/formeln/auswertung.py': ziel.read_text() + '\ndef kaputt(:\n'}, n=2)
gleich = messgeraet.laufzeit_gepaart(W, bereiche, 'lagerhaus', ref, None, None, n=2)
aus = {'bereiche': bereiche,
       'probe_teilausfall': {k: kaputt.get(k) for k in ('gueltig', 'seite', 'bereich', 'grund')},
       'gegenprobe_gleicher_stand': {'gueltig': gleich.get('gueltig'),
                                     'werte': {b: (x.get('basis'), x.get('kandidat')) for b, x in (gleich.get('bereiche') or {}).items()}}}
Path('/root/biotop-vor-t4-02/py/PYTHON-LAUFZEIT-TEILAUSFALL.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1))
print(json.dumps(aus, ensure_ascii=False, indent=1)[:2000])
