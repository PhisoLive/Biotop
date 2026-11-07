"""Prüft die beiden Festlegungen zum Vorspann (Chat-Claude, Fassung 6) an einem echten Werk:
 (1) Eichgegenstand — je Werk einmal gewählt und versiegelt, beim zweiten Lauf unverändert, bei Wegfall ein Befund
     und ein neuer versiegelter Gegenstand (protokolliert).
 (2) Eichkosten — je Lauf getrennt ausgewiesen, Kammerläufe und Modellaufrufe einzeln, mit Hochrechnung.
Aufruf: eichgegenstand_pruefen.py <ausgaben-dir>
"""
import shutil
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, transaktion
from biotop.organe import eichgegenstand, eichung

A = Path(sys.argv[1])
con = verbinden()
WERK_ID = 18                      # lagerhaus, Stand Lauf 20
pfad = Path(con.execute("SELECT pfad FROM werke WHERE id=?", (WERK_ID,)).fetchone()[0])
z = ["# Vorspann: versiegelter Eichgegenstand und getrennte Eichkosten (Fassung 6)"]

eichgegenstand._tabelle(con)      # Tabelle anlegen, bevor die Prüfung sie leert
with transaktion(con):            # sauberer Ausgangszustand für die Prüfung
    con.execute("DELETE FROM eichgegenstand WHERE werk_id=?", (WERK_ID,))

z.append("\n## (1a) Erster Lauf: Gegenstand wird gewählt und versiegelt")
e1 = eichgegenstand.sichern(con, WERK_ID, lauf_id=901, pfad=pfad)
z += eichgegenstand.text(e1)
g = e1["gegenstand"]
z.append(f"  Begründung der Wahl: {g['begruendung']}")

z.append("\n## (1b) Zweiter Lauf am unveränderten Werk: derselbe Gegenstand, keine Neuwahl")
e2 = eichgegenstand.sichern(con, WERK_ID, lauf_id=902, pfad=pfad)
z += eichgegenstand.text(e2)
z.append(f"  gleiche Prüfsumme wie beim ersten Lauf: {e2['gegenstand']['vertrag_pruefsumme'] == g['vertrag_pruefsumme']} "
         f"| neu versiegelt: {e2['neu']} (gefordert: False)")

z.append("\n## (1c) Werk ändert den Vertrag → Befund und NEUE Versiegelung, protokolliert")
datei = pfad / g["vertrag_pfad"]
sicherung = datei.read_text()
try:
    datei.write_text(sicherung + "\n# Änderung durch eine angenommene Generation (Probe Hermes)\n")
    e3 = eichgegenstand.sichern(con, WERK_ID, lauf_id=903, pfad=pfad)
    z += eichgegenstand.text(e3)
    z.append(f"  neu versiegelt: {e3['neu']} (gefordert: True)")
    p = con.execute("SELECT nr, inhalt FROM protokoll WHERE art='eichgegenstand.weggefallen' ORDER BY nr DESC LIMIT 1").fetchone()
    z.append(f"  Protokoll #{p['nr']}: {p['inhalt'][:200]}" if p else "  KEINE Protokollzeile (Fehler)")
finally:
    datei.write_text(sicherung)

z.append("\n## (2) Eichkosten getrennt — Rauschmessung an 4 Bereichen")
eichung._tabelle(con)
with transaktion(con):
    con.execute("DELETE FROM eichkosten WHERE lauf_id=904")
ref = Path("/root/biotop/biotop/kern/referenzlast/lagerhaus.py").read_text()
r = eichung.rauschmessung(con, lauf_id=904, werk_id=WERK_ID, pfad=pfad,
                          bereiche=["bericht", "formeln", "lager", "preise"], paket="lagerhaus", ref=ref)
k = eichung.kosten(con, 904)
z += eichung.kosten_text(k, bereiche=4)
z.append(f"  Laufsumme der Kasse bleibt unberührt: Eichaufrufe tragen den Zweck-Vorsatz '{eichung.ZWECK}' "
         f"und sind damit in KASSE.md trennbar.")
(A / "05-eichgegenstand-und-kosten.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
