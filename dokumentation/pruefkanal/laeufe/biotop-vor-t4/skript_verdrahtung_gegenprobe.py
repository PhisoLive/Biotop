"""Gegenproben am Laufweg für den Verdrahtungstest (Vorbedingung 7). Aufruf: python verdrahtung_gegenprobe.py <kopie> <art>

Baut in einer KOPIE des Arbeitsbaums genau einen Fehler ein, der die neue Prüfung rot machen muss:
  phase    — `lauf.annahme_tausch` trägt die Eichung nicht mehr (`_masseichung` None): Die Eichproben des Vorspanns
             rufen `masseichung.anwenden` weiter aus `aegis.pruefen`, die Generationen nicht mehr mit Wirkung.
             Form des Befunds aus Lauf 38 (Review 03 Nr. 6d). Erwartung: rot an „Maßeichung wirkt nicht in der Generation“.
  vv       — `aegis.pruefen` ignoriert das Urteil des Verhaltensvergleichs (ruft ihn, wertet ihn nicht aus).
             Erwartung: rot an „Ungedeckte Abweichung am Laufweg nicht abgelehnt“.
  schwarm  — nur die neue Zeile in lauf._generation_koerper abgeklemmt. Ergebnis 23.09.: GRÜN — die gespeicherte Messung
             jeder Generation ist seit f821707 schon geeicht; die Probe allein war blind (Grundsatz 8).
  mass_roh — nur die zweite Schutzstelle abgeklemmt (Ausgangsmaß roh gespeichert). Erwartung: grün (die neue Zeile hält).
  beide    — schwarm + mass_roh. Erwartung: rot an „Schwarm liest die stillgelegte Regel“.
"""
import sys
from pathlib import Path

kopie, art = Path(sys.argv[1]), sys.argv[2]
ERSATZ = {
    "phase": ("biotop/lauf.py",
              '                  _rauschbelege=rausch["bereiche"], _vorspann_sha256=nachweis["nachweis_sha256"],\n'
              '                  _masseichung=nachweis.get("masseichung"))',
              '                  _rauschbelege=rausch["bereiche"], _vorspann_sha256=nachweis["nachweis_sha256"],\n'
              '                  _masseichung=None)  # GEGENPROBE: Eichung erreicht die Generationen nicht'),
    "vv": ("biotop/organe/aegis.py",
           '    if not vv["tragfaehig"]:\n        u = {**u, "ok": False, "grund": "Verhaltensvergleich: " + vv["grund"]}',
           '    if False and not vv["tragfaehig"]:  # GEGENPROBE: Urteil des Verhaltensvergleichs ignoriert\n'
           '        u = {**u, "ok": False, "grund": "Verhaltensvergleich: " + vv["grund"]}'),
    "schwarm": ("biotop/lauf.py",
                '    basis_g = masseichung.anwenden(basis, tausch.get("_masseichung"))\n    for b in bereiche:',
                '    basis_g = basis  # GEGENPROBE: Schwarm liest ungeeicht\n    for b in bereiche:'),
    # Zweite Schutzstelle: das eingefrorene Ausgangsmaß (Generation 0) wird roh gespeichert (seit f821707 geeicht).
    "mass_roh": ("biotop/lauf.py",
                 '    mess = masseichung.anwenden(mess, eichung_mass)\n    mess["kernmass_f2"] = messgeraet.kernmass_f2(mess)',
                 '    pass  # GEGENPROBE: Ausgangsmaß roh gespeichert\n    mess["kernmass_f2"] = messgeraet.kernmass_f2(mess)'),
}
KOMBI = {"beide": ("schwarm", "mass_roh")}
for teil in KOMBI.get(art, (art,)):
    datei, alt, neu = ERSATZ[teil]
    p = kopie / datei
    t = p.read_text()
    n = t.count(alt)
    if n != 1:
        raise SystemExit(f"Gegenprobe {teil} nicht herstellbar: Anker {n}× gefunden")
    p.write_text(t.replace(alt, neu))
    print(f"Gegenprobe {art}/{teil}: {datei} geändert (1 Stelle)")
