"""Prüft die Einschränkung der zweiten Quelle (Chat-Claude, Fassung 6):
Die Ableitung des tragenden Pfades aus dem Verfassungstext ist eine Wortstatistik und gilt NUR für Übungswerke.
Bei einem Werk mit Betriebszweck ohne ausdrücklichen `tragender_pfad` meldet das Organ und wartet.

Fall 1: Übungswerk (uebungswerk: true)      → Ableitung zulässig, Gegenstand wird versiegelt.
Fall 2: Betriebszweck (uebungswerk entfernt) → KEINE Ableitung, Meldung + Warten, kein Gegenstand.
Fall 3: Betriebszweck MIT tragender_pfad     → Gegenstand wird versiegelt, Pfad aus der Verfassung.
Aufruf: eichgegenstand_betriebszweck.py <ausgaben-dir>
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
alt = con.execute("SELECT regeln FROM verfassung_werk WHERE werk_id=?", (WERK_ID,)).fetchone()["regeln"]
z = ["# Tragender Pfad: Ableitung nur bei Übungswerken (Fassung 6)"]

def lauf(marke, regeln, lauf_id):
    global z
    with transaktion(con):
        con.execute("UPDATE verfassung_werk SET regeln=? WHERE werk_id=?", (json.dumps(regeln, ensure_ascii=False), WERK_ID))
        con.execute("DELETE FROM eichgegenstand WHERE werk_id=?", (WERK_ID,))
    e = EG.sichern(con, WERK_ID, lauf_id=lauf_id, pfad=pfad)
    z.append(f"\n{marke}")
    z += ["  " + s for s in EG.text(e)]
    return e

try:
    r1 = lj(alt) or {}
    e1 = lauf("## Fall 1: Übungswerk (uebungswerk: true) — Ableitung zulässig", r1, 910)
    z.append(f"  Gegenstand versiegelt: {e1['gegenstand'] is not None} (gefordert: True) | wartet: {e1.get('wartet', False)}")

    r2 = dict(r1); r2.pop("uebungswerk", None)
    e2 = lauf("## Fall 2: Werk mit Betriebszweck, kein tragender_pfad — melden und warten", r2, 911)
    z.append(f"  Gegenstand versiegelt: {e2['gegenstand'] is not None} (gefordert: False) | wartet: {e2.get('wartet', False)} (gefordert: True)")
    p = con.execute("SELECT nr, inhalt FROM protokoll WHERE art='eichgegenstand.wartet' ORDER BY nr DESC LIMIT 1").fetchone()
    z.append(f"  Protokoll #{p['nr']}: {p['inhalt'][:260]}" if p else "  KEINE Protokollzeile (Fehler)")

    r3 = dict(r2); r3["tragender_pfad"] = [["preise", "formeln"]]
    e3 = lauf("## Fall 3: Werk mit Betriebszweck MIT tragender_pfad — Gegenstand aus der Verfassung", r3, 912)
    g = e3["gegenstand"]
    z.append(f"  gewählt: {g['von_bereich']}→{g['nach_bereich']} | wartet: {e3.get('wartet', False)} (gefordert: False)")
    z.append(f"  Begründung: {g['begruendung'][:200]}")
finally:
    with transaktion(con):
        con.execute("UPDATE verfassung_werk SET regeln=? WHERE werk_id=?", (alt, WERK_ID))
        con.execute("DELETE FROM eichgegenstand WHERE werk_id=?", (WERK_ID,))
    EG.sichern(con, WERK_ID, lauf_id=913, pfad=pfad)
    g = EG.lesen(con, WERK_ID)
    z.append(f"\n(Regeln wiederhergestellt, echter Gegenstand neu versiegelt: {g['von_bereich']}→{g['nach_bereich']})")

(A / "07-tragender-pfad-nur-uebungswerk.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
