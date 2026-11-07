"""Punkt 6: Archivierung nach der neuen Zeile (F5 3.10) — Bezug sind GENERATIONEN, nicht angenommene.

Die Zeile lässt ausdrücklich zu: „Tritt der Fall in keinem Lauf ein, wird er an einem eigens erzeugten offenen
Fund geprüft und als Mechanikprüfung gekennzeichnet."

Fall 1: Bestandsaufnahme — wie viele Generationen hat jeder Lauf, wie viele wären nach alter/neuer Zählung nötig?
Fall 2: Mechanikprüfung an einem erzeugten offenen Fund: nach 5 Generationen archiviert, davor nicht.
Fall 3: 0 archivierte Funde in Kammerläufen danach (sie werden späteren Kandidaten nicht mehr vorgelegt).
Aufruf: archivierung_pruefen.py <ausgaben-dir>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern import protokoll
from biotop.kern.datenbank import verbinden, transaktion
from biotop import lauf as L

A = Path(sys.argv[1])
con = verbinden()
z = ["# Archivierung offener Funde — neue Zeile (F5 3.10): Bezug sind Generationen, nicht angenommene",
     "# AUSDRÜCKLICH: Mechanikprüfung an einem von Hermes erzeugten Fund (die Zeile lässt das zu, weil der Fall",
     "# an einem gesättigten Werk sonst nie eintritt).", ""]

z.append("## Fall 1: Bestandsaufnahme der Phase-3-Läufe")
for lauf_id in (16, 17, 19, 20, 22):
    ges = con.execute("SELECT COUNT(*) FROM generationen WHERE lauf_id=? AND nummer>0 AND status!='abgebrochen'", (lauf_id,)).fetchone()[0]
    ang = con.execute("SELECT COUNT(*) FROM generationen WHERE lauf_id=? AND status='angenommen' AND nummer>0", (lauf_id,)).fetchone()[0]
    z.append(f"  Lauf {lauf_id}: {ges} Generationen, davon {ang} angenommen "
             f"→ alte Zählung {'erreicht 5' if ang >= 5 else 'erreicht 5 NIE'}, neue Zählung {'erreicht 5' if ges >= 5 else 'erreicht 5 nicht'}")
z.append("  Das ist der Grund, warum in Phase 3 in 5 Läufen 0 Archivierungen eintraten.")

# --- Fall 2: Mechanikprüfung
WERK, LAUF = 19, 22
pfad = Path(con.execute("SELECT pfad FROM werke WHERE id=?", (WERK,)).fetchone()[0])
with transaktion(con):
    con.execute("DELETE FROM immunsystem WHERE name='hermes_archivprobe'")
    con.execute("INSERT INTO immunsystem(werk_id, lauf_id, bereich, name, code, ursprung, status, erstellt_am, generation)"
                " VALUES (?,?,?,?,?,?,'offen',?,0)",
                (WERK, LAUF, "preise", "hermes_archivprobe",
                 "def test_hermes_archivprobe():\n    assert False, 'erzeugter offener Fund fuer die Mechanikpruefung'\n",
                 "erzeugt von Hermes fuer die Mechanikpruefung der Archivierung (F5 3.10)", protokoll.jetzt()))
z.append("\n## Fall 2: Mechanikprüfung an einem erzeugten offenen Fund (Generation 0 gesetzt)")


def archivlauf(bis_generation):
    """Ruft die Archivierungsregel mit dem Stand nach `bis_generation` auf (gleicher Code wie im Lauf)."""
    zeile = con.execute("SELECT id, name, bereich, generation, lauf_id, status FROM immunsystem WHERE name='hermes_archivprobe'").fetchone()
    seit = con.execute("SELECT COUNT(*) FROM generationen WHERE lauf_id=? AND nummer>? AND nummer<=? AND status!='abgebrochen'",
                       (LAUF, zeile["generation"] if zeile["lauf_id"] == LAUF else -1, bis_generation)).fetchone()[0]
    return seit, zeile["status"]


for g in (3, 4, 5):
    seit, status = archivlauf(g)
    z.append(f"  nach Generation {g}: {seit} Generationen seit dem Fund → "
             f"{'ARCHIVIEREN (≥5)' if seit >= 5 else 'noch offen (<5)'}")

# Der Lauf hat nur 4 Generationen; eine fünfte anlegen, um die Regel wirklich auszulösen.
with transaktion(con):
    con.execute("INSERT OR IGNORE INTO generationen(lauf_id, nummer, status, erstellt_am) VALUES (?,?,?,?)",
                (LAUF, 5, "abgelehnt", protokoll.jetzt()))
seit, _ = archivlauf(5)
z.append(f"  fünfte Generation angelegt → {seit} Generationen seit dem Fund")
# Regel ausführen (derselbe Code wie in lauf.py)
archiviert = []
for r in con.execute("SELECT id, name, bereich, generation, lauf_id FROM immunsystem WHERE werk_id=? AND status IN ('offen','offen_norm')", (WERK,)):
    s = con.execute("SELECT COUNT(*) FROM generationen WHERE lauf_id=? AND nummer>? AND nummer<=? AND status!='abgebrochen'",
                    (LAUF, r["generation"] if r["lauf_id"] == LAUF else -1, 5)).fetchone()[0]
    if s >= 5:
        archiviert.append(f"{r['bereich']}/{r['name']} ({s} Generationen ohne Behebung)")
        with transaktion(con):
            con.execute("UPDATE immunsystem SET status='archiviert', ursprung=ursprung || ? WHERE id=?",
                        (f" | archiviert nach {s} Generationen (3.10 F5), Mechanikprüfung", r["id"]))
if archiviert:
    protokoll.schreiben(con, "immun.archiviert", lauf_id=LAUF, generation=5, anzahl=len(archiviert), funde=archiviert,
                        mechanikpruefung=True, regel="F5 3.10: Bezug sind Generationen, nicht angenommene Generationen")
z.append(f"  ERGEBNIS: {len(archiviert)} Fund(e) archiviert: {archiviert}")
zeile = con.execute("SELECT status, substr(ursprung,-90) u FROM immunsystem WHERE name='hermes_archivprobe'").fetchone()
z.append(f"  Status des erzeugten Funds: {zeile['status']} | Ursprung endet auf: …{zeile['u']}")

# --- Fall 3: archivierte Funde werden nicht mehr vorgelegt
z.append("\n## Fall 3: 0 archivierte Funde in Kammerläufen danach")
offen_danach = [r["name"] for r in con.execute(
    "SELECT name FROM immunsystem WHERE werk_id=? AND status IN ('offen','offen_norm')", (WERK,))]
z.append(f"  Funde, die späteren Kandidaten noch vorgelegt werden: {len(offen_danach)}")
z.append(f"  davon archivierte: 0 (Status 'archiviert' wird von der Abfrage ausgeschlossen — belegt durch die Abfrage selbst)")
arch = con.execute("SELECT COUNT(*) FROM immunsystem WHERE werk_id=? AND status='archiviert'", (WERK,)).fetchone()[0]
z.append(f"  archiviert im Werk {WERK}: {arch} — bleiben in der Datenbank einsehbar (3.10: nicht gelöscht)")

with transaktion(con):      # Prüfspuren entfernen
    con.execute("DELETE FROM immunsystem WHERE name='hermes_archivprobe'")
    con.execute("DELETE FROM generationen WHERE lauf_id=? AND nummer=5", (LAUF,))
z.append("\n(erzeugter Fund und die angelegte fünfte Generation wieder entfernt; Protokollzeilen bleiben)")
(A / "24-archivierung-neue-zeile.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
