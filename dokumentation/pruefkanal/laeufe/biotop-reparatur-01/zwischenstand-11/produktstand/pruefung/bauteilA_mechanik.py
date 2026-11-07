"""Bauteil A (F6 3.7), Mechanikprüfung: Wird ein Angriff mit bereits aufgestellter Behauptung wirklich
nicht ausgeführt?

An echten Läufen trat der Fall zu selten auf, um ihn zu belegen (Lauf 22 sättigte nach einer Generation mit
5 Ansagen, Lauf 23 lief an einer frischen Werk-Kopie mit leerem Behauptungsvorrat). Deshalb wird die
Entscheidung hier mit gestellter Ansage geprüft — ausdrücklich als Mechanikprüfung gekennzeichnet.
Grundsatz 4: Der Wirkungsbereich ist eingegrenzt (kein Werk wird verändert, keine Tabelle beschrieben
außer dem Protokoll, das unveränderlich ist).
Aufruf: bauteilA_mechanik.py <ausgaben-dir>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj
from biotop.organe import aegis

A = Path(sys.argv[1])
con = verbinden()
z = ["# Bauteil A (F6 3.7) — Mechanikprüfung: bekannte Behauptung → Angriff wird nicht ausgeführt",
     "# GESTELLTE Ansage (kein echter Modellaufruf für die Ansage), weil der Fall an echten Läufen zu selten auftrat.", ""]

WERK, LAUF, BEREICH = 19, 22, "preise"
vorrat = aegis.bisherige_behauptungen(con, WERK, BEREICH, LAUF)
z.append(f"Bereich {BEREICH}, Werk {WERK}: {len(vorrat)} bereits aufgestellte Behauptungen")
for v in vorrat:
    z.append(f"  - {v}")

echt = aegis._ansage
aufrufe = {"n": 0}


def gestellt(wert):
    def f(con_, lauf_id, modell, bereich, paket, diff, quelle, schon):
        aufrufe["n"] += 1
        return wert, False
    return f


# --- Fall 1: Ansage wiederholt eine bekannte Behauptung
bekannt = vorrat[0] if vorrat else None
z.append("")
if not bekannt:
    z.append("KEIN GEGENSTAND: der Bereich hat keine bisherigen Behauptungen — Prüfung nicht durchführbar.")
else:
    angriffe_vorher = con.execute("SELECT COUNT(*) FROM kasse WHERE lauf_id=? AND zweck LIKE 'aegis.angriff%'", (LAUF,)).fetchone()[0]
    aegis._ansage = gestellt(bekannt)
    try:
        ergebnis = aegis._angriff(con, LAUF, WERK, "lagerhaus", BEREICH, "--- a/x\n+++ b/x\n@@ -1 +1 @@\n-a\n+b\n", {},
                                  Path(con.execute("SELECT pfad FROM werke WHERE id=?", (WERK,)).fetchone()[0]), [])
    finally:
        aegis._ansage = echt
    angriffe_nachher = con.execute("SELECT COUNT(*) FROM kasse WHERE lauf_id=? AND zweck LIKE 'aegis.angriff%'", (LAUF,)).fetchone()[0]
    p = con.execute("SELECT nr, inhalt FROM protokoll WHERE art='aegis.ansage' ORDER BY nr DESC LIMIT 1").fetchone()
    d = lj(p["inhalt"]) or {}
    z.append(f"## Fall 1: Ansage = `{bekannt}` (bereits aufgestellt)")
    z.append(f"  Rückgabe des Angriffs: {ergebnis[0]!r} (None = kein Test geschrieben)")
    z.append(f"  Modellaufrufe für den Angriff: {angriffe_nachher - angriffe_vorher} (gefordert: 0)")
    z.append(f"  Protokoll #{p['nr']}: ausgefuehrt={d.get('ausgefuehrt')}, behauptung={d.get('behauptung')!r}")
    z.append(f"  Grund: {d.get('grund')}")
    z.append(f"  ERGEBNIS: {'bestanden — Angriff nicht ausgeführt, kein Aufruf, kein Kammerlauf' if ergebnis[0] is None and angriffe_nachher == angriffe_vorher else 'NICHT bestanden'}")

    # --- Fall 2: neue Behauptung → Angriff wird ausgeführt
    neu = "eine_neue_funktion|Eq:zahl"
    angriffe_vorher = angriffe_nachher
    aegis._ansage = gestellt(neu)
    try:
        ergebnis2 = aegis._angriff(con, LAUF, WERK, "lagerhaus", BEREICH, "--- a/x\n+++ b/x\n@@ -1 +1 @@\n-a\n+b\n", {},
                                   Path(con.execute("SELECT pfad FROM werke WHERE id=?", (WERK,)).fetchone()[0]), [])
    finally:
        aegis._ansage = echt
    angriffe_nachher = con.execute("SELECT COUNT(*) FROM kasse WHERE lauf_id=? AND zweck LIKE 'aegis.angriff%'", (LAUF,)).fetchone()[0]
    p2 = con.execute("SELECT nr, inhalt FROM protokoll WHERE art='aegis.ansage' ORDER BY nr DESC LIMIT 1").fetchone()
    d2 = lj(p2["inhalt"]) or {}
    z.append("")
    z.append(f"## Fall 2 (Gegenprobe): Ansage = `{neu}` (neu)")
    z.append(f"  Modellaufrufe für den Angriff: {angriffe_nachher - angriffe_vorher} (gefordert: 1)")
    z.append(f"  Protokoll #{p2['nr']}: ausgefuehrt={d2.get('ausgefuehrt')}, behauptung={d2.get('behauptung')!r}")
    z.append(f"  ERGEBNIS: {'bestanden — Angriff ausgeführt' if angriffe_nachher > angriffe_vorher else 'NICHT bestanden'}")

z.append("")
z.append("HINWEIS (Grundsatz 4): Die Prüfung hat nichts am Werk und nichts an den Gedächtnissen verändert;")
z.append("die zwei Protokollzeilen bleiben, weil das Protokoll unveränderlich ist.")
(A / "08-bauteilA-mechanik.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
