"""Tor 3, Jury-Zeile, zweiter Teil: Die Zeile verlangt einen Fall OHNE Einstimmigkeit → kein Urteil, protokolliert.
Fünf echte Jury-Fälle (3 aus Läufen, 2 Proben mit Zielkonflikt) waren alle einstimmig. Hier wird deshalb die MECHANIK
geprüft: Was tut jury.entscheiden, wenn die Juroren uneins sind? Ein Juror wird durch einen Ersatz-Aufruf ersetzt, der
eine feste Gegenstimme liefert — die Auswertung (Einstimmigkeit, Gewinner, Protokoll) bleibt die echte.
Ausdrücklich gekennzeichnet: gestellte Uneinigkeit, kein echter Modelldissens.
Aufruf: jury_mechanik.py <ausgaben-dir> <lauf_id>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj
from biotop.organe import jury
from biotop import anbieter

A = Path(sys.argv[1]); LAUF = int(sys.argv[2])
con = verbinden()
ids = [r[0] for r in con.execute("SELECT id FROM kandidaten WHERE bereich='probe_jury_hermes' ORDER BY id DESC LIMIT 2")][::-1]

echt = jury.aufrufen
zaehler = {"n": 0}
class Antwort:
    def __init__(self, text): self.text = text
def gefaelscht(con_, lauf_id, anb, modell, system, nutzer, **kw):
    zaehler["n"] += 1
    if zaehler["n"] == 3:  # dritter Juror stimmt dagegen
        return Antwort('{"wahl": "A", "begruendung": "Gestellte Gegenstimme (Mechanikprobe Hermes): A ist kuerzer."}')
    return echt(con_, lauf_id, anb, modell, system, nutzer, **kw)

jury.aufrufen = gefaelscht
try:
    e = jury.entscheiden(con, LAUF, 0, "probe_jury_mechanik", ids[0], ids[1])
finally:
    jury.aufrufen = echt

zeilen = ["# Tor 3 — Jury-Mechanik bei Uneinigkeit (GESTELLTE Gegenstimme, kein echter Modelldissens — Kennzeichnung Hermes)",
          "Grund: fünf echte Jury-Fälle waren alle einstimmig; die Zeile verlangt den Nachweis, dass Uneinigkeit zu KEINEM Urteil führt.",
          f"Einstimmig: {bool(e.get('einstimmig'))} | Gewinner: {e.get('gewinner')} (None = kein Urteil)"]
for u in e.get("urteile", []):
    zeilen.append(f"  {u.get('modell')}: waehlt {u.get('wahl')} — {(u.get('begruendung') or '')[:150]}")
p = con.execute("SELECT nr, inhalt FROM protokoll WHERE art LIKE 'jury%' ORDER BY nr DESC LIMIT 1").fetchone()
zeilen.append(f"Protokollzeile: #{p['nr']} {str(lj(p['inhalt']))[:300]}" if p else "keine Protokollzeile")
zeilen.append(f"ERGEBNIS: {'kein Urteil bei Uneinigkeit — Mechanik belegt' if not e.get('einstimmig') and e.get('gewinner') is None else 'Mechanik NICHT belegt'}")
alle = [dict(r) for r in con.execute("SELECT lauf_id, generation, bereich, einstimmig, gewinner FROM jury ORDER BY id")]
zeilen.append(f"Jury-Fälle insgesamt: {len(alle)} — einstimmig {sum(1 for x in alle if x['einstimmig'])}, ohne Einstimmigkeit {sum(1 for x in alle if not x['einstimmig'])} (davon gestellt: 1)")
(A / "96-tor3-jury-mechanik.txt").write_text("\n".join(zeilen) + "\n")
print("\n".join(zeilen))
