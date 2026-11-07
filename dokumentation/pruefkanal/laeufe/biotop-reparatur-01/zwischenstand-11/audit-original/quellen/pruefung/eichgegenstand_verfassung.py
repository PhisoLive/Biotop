"""Beweist, dass die Verfassung der Vertragsgröße vorgeht (Fassung 6, Festlegung Chat-Claude).
Gegenprobe: `tragender_pfad` zeigt auf das Paar mit dem KLEINSTEN Vertrag — wählt das Organ trotzdem dieses,
geht die Verfassung der Größe vor. Ohne diese Probe wäre die Regel am `lagerhaus` nicht nachweisbar, weil dort
das größte und das tragende Paar zufällig dasselbe sind.
Aufruf: eichgegenstand_verfassung.py <ausgaben-dir>
"""
import json
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj, transaktion
from biotop.organe import eichgegenstand as EG

A = Path(sys.argv[1])
con = verbinden()
WERK_ID = 18
pfad = Path(con.execute("SELECT pfad FROM werke WHERE id=?", (WERK_ID,)).fetchone()[0])
EG._tabelle(con)
paare = EG._kandidatenpaare(con, WERK_ID, pfad)
z = ["# Eichgegenstand: Verfassung geht der Vertragsgröße vor (Fassung 6)",
     f"Bereichspaare mit Vertrag: " + ", ".join(f"{p['von_bereich']}→{p['nach_bereich']} ({p['zeilen']} Z.)" for p in paare)]

def waehlen(marke):
    with transaktion(con):
        con.execute("DELETE FROM eichgegenstand WHERE werk_id=?", (WERK_ID,))
    e = EG.sichern(con, WERK_ID, lauf_id=906, pfad=pfad)
    g = e["gegenstand"]
    z.append(f"\n{marke}")
    z.append(f"  gewählt: {g['von_bereich']}→{g['nach_bereich']} ({[p['zeilen'] for p in paare if p['von_bereich']==g['von_bereich'] and p['nach_bereich']==g['nach_bereich']][0]} Zeilen)")
    z.append(f"  Begründung: {g['begruendung']}")
    return g

alt = con.execute("SELECT regeln FROM verfassung_werk WHERE werk_id=?", (WERK_ID,)).fetchone()["regeln"]
t, h = EG._tragende_paare(con, WERK_ID, paare)
z.append(f"tragende Paare aus der Verfassung: {({f'{a}→{b}': g for (a, b), g in t.items()})} — {h}")
g1 = waehlen("## (a) Verfassung wie hinterlegt (abgeleitet aus dem Text)")

# Gegenprobe: ausdrücklicher tragender Pfad auf das Paar mit dem KLEINSTEN Vertrag
klein = sorted(paare, key=lambda p: p["zeilen"])[0]
regeln = lj(alt) or {}
regeln["tragender_pfad"] = [[klein["von_bereich"], klein["nach_bereich"]]]
try:
    with transaktion(con):
        con.execute("UPDATE verfassung_werk SET regeln=? WHERE werk_id=?", (json.dumps(regeln, ensure_ascii=False), WERK_ID))
    g2 = waehlen(f"## (b) Gegenprobe: Verfassung benennt ausdrücklich {klein['von_bereich']}→{klein['nach_bereich']} "
                 f"— das Paar mit dem KLEINSTEN Vertrag ({klein['zeilen']} Zeilen)")
    treffer = (g2["von_bereich"], g2["nach_bereich"]) == (klein["von_bereich"], klein["nach_bereich"])
    z.append(f"  ERGEBNIS: Verfassung schlägt Vertragsgröße: {treffer} (gefordert: True)")
finally:
    with transaktion(con):
        con.execute("UPDATE verfassung_werk SET regeln=? WHERE werk_id=?", (alt, WERK_ID))
    with transaktion(con):
        con.execute("DELETE FROM eichgegenstand WHERE werk_id=?", (WERK_ID,))
    EG.sichern(con, WERK_ID, lauf_id=907, pfad=pfad)   # Ausgangszustand wieder versiegeln
    z.append(f"\n(Regeln des Werks wiederhergestellt, Gegenstand neu versiegelt: "
             f"{EG.lesen(con, WERK_ID)['von_bereich']}→{EG.lesen(con, WERK_ID)['nach_bereich']})")

(A / "06-eichgegenstand-verfassung-vor-groesse.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
