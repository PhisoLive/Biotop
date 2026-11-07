"""Gegenprobe am Laufweg für die verschärfte Verdrahtungsregel („Pflicht im Annahmepfad").

Baut eine Kopie des Arbeitsbaums, in der `aegis.pruefen` `masseichung.anwenden` NICHT ruft — das Organ bleibt aber im
Lauf gerufen (Vorspann: eichen/sauberer_bereich; mass_einfrieren und Generalprobe: anwenden). Das ist die Form des
Befunds aus Lauf 38: existiert, wird gerufen, aber nicht in der Funktion, die über die Annahme entscheidet.
Erwartung: test_jedes_organ_wird_im_lauf_aufgerufen wird rot mit „['masseichung.anwenden'] wird nicht aus
biotop.organe.aegis:pruefen gerufen"; die Organliste selbst ist vollständig (23 von 23 gerufen).
"""
import sys
from pathlib import Path

ziel = Path(sys.argv[1]) / 'biotop' / 'organe' / 'aegis.py'
alt = ziel.read_text()
block = ('    basis_paar = masseichung.anwenden(basis_paar, eichung_mass)\n'
         '    mess = masseichung.anwenden(mess, eichung_mass)\n')
n = alt.count(block)
if n != 1:
    raise SystemExit(f'Gegenprobe nicht herstellbar: Block {n}× gefunden statt 1×')
ziel.write_text(alt.replace(block, '    pass  # GEGENPROBE: Maßeichung im Annahmepfad abgeklemmt\n'))
rest = ziel.read_text().count('masseichung.anwenden(')
print(f'aegis.py der Kopie: masseichung.anwenden-Aufrufe entfernt (2), verbleibend in aegis.py: {rest}')
