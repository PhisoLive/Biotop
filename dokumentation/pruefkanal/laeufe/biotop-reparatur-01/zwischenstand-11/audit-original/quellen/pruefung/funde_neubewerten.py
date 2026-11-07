"""Mechanische Neubewertung der Immunsystem-Funde eines Werks nach der aktuellen Regel (F4 3.7, Fassung Philipp 19.09.2026)
und Vorabprobe: Kommt eine echte Behebung des K1165-Fehlers durch den Ankläger?

Regel: Ein Fund-Test, der am Werk BESTEHT (also das aktuelle Verhalten festschreibt) und weder einen Absturz im Werk
auslöst noch einen Vertrag/Verfassungssatz durch explizite Kennung nennt, ist Norm — nicht Fund. Er darf nicht im
gemessenen Testbestand stehen, sonst tötet er jede Behebung per Pareto je Test.

Aufruf: funde_neubewerten.py <werk_id> <ausgaben-dir> [--schreiben]
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, transaktion
from biotop.kern import protokoll
from biotop.organe import kammer

WERK_ID = int(sys.argv[1]); A = Path(sys.argv[2]); SCHREIBEN = "--schreiben" in sys.argv
con = verbinden()
pfad = Path(con.execute("SELECT pfad FROM werke WHERE id=?", (WERK_ID,)).fetchone()[0])
verweis = __import__("re").compile(r"(test_vertrag[A-Za-z_0-9]*|Verfassung(ssatz)? \d+)")

zeilen = [f"# Neubewertung der Immunsystem-Funde, Werk {WERK_ID} ({pfad.name}) — Regel F4 3.7 (Fassung Philipp 19.09.2026)",
          "# Ein Fund-Test, der AM WERK BESTEHT, ohne Absturz und ohne expliziten Vertrags-/Verfassungsverweis, ist Norm (0 Punkte, nicht im Testbestand)."]
aenderungen = []
for z in con.execute("SELECT id, name, status, bereich, code FROM immunsystem WHERE werk_id=? AND status='offen' ORDER BY name", (WERK_ID,)):
    datei = f"tests/_neubewertung_{z['name']}.py"
    e = kammer.ausfuehren(pfad, ["python", "-m", "pytest", "-q", "-p", "no:cacheprovider", datei], dateien={datei: z["code"]}, zeitlimit_s=90)
    aus = e.stdout + e.stderr
    besteht = " passed" in aus and " failed" not in aus
    absturz = any(w in aus for w in ("Error", "Exception")) and "AssertionError" not in aus
    bezug = bool(verweis.search(z["code"]))
    norm = besteht and not absturz and not bezug
    zeilen.append(f"{z['name']}: besteht am Werk {besteht} | Absturz {absturz} | Vertrags-/Verfassungsverweis {bezug} → {'NORM (offen_norm)' if norm else 'Fund bleibt offen'}")
    if norm: aenderungen.append((z["id"], z["name"]))

zeilen.append(f"ERGEBNIS: {len(aenderungen)} von {con.execute('SELECT COUNT(*) FROM immunsystem WHERE werk_id=? AND status=%r' % 'offen', (WERK_ID,)).fetchone()[0]} offenen Funden sind nach der Regel Norm: " + ", ".join(n for _, n in aenderungen))
if SCHREIBEN and aenderungen:
    with transaktion(con):
        for i, n in aenderungen:
            con.execute("UPDATE immunsystem SET status='offen_norm', ursprung=ursprung || ? WHERE id=?",
                        (" | neubewertet nach F4 3.7 (Fassung Philipp 19.09.2026): Test besteht am Werk, kein Absturz, kein Vertrags-/Verfassungsverweis → Norm, kein Fund", i))
    protokoll.schreiben(con, "immun.neubewertet", werk_id=WERK_ID, anzahl=len(aenderungen), namen=[n for _, n in aenderungen],
                        regel="F4 3.7 Fassung Philipp 19.09.2026: Ein Test, der das aktuelle Verhalten festschreibt, ohne Absturz und ohne expliziten Vertrags-/Verfassungsverweis, ist Norm, kein Fund.")
    zeilen.append("→ in die Datenbank geschrieben (Protokoll immun.neubewertet)")
(A / f"93-funde-neubewertung-werk{WERK_ID}.txt").write_text("\n".join(zeilen) + "\n")
print("\n".join(zeilen))
