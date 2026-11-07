"""Nachabstraktion: Für alle ANGENOMMENEN Einträge beider Werke das Muster nachbilden (F5 3.12, einmalig).
Ohne Nachabstraktion stünde der werkübergreifende Block leer, und die Torzeile wäre nicht messbar.
Aufruf: muster_nachtragen.py <ausgaben-dir> [--schreiben]
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern import protokoll
from biotop.kern.datenbank import verbinden, transaktion
from biotop.organe import gedaechtnis as G

A = Path(sys.argv[1]); SCHREIBEN = "--schreiben" in sys.argv
con = verbinden()
G.tabellen(con)
offen = [dict(r) for r in con.execute(
    "SELECT a.id, a.werk, a.werkklasse, a.bereich, a.kategorie, a.zuwachs, a.laufzeit_prozent, a.lauf_id,"
    " a.kandidat_id, a.beschreibung, k.diff FROM artgedaechtnis a LEFT JOIN kandidaten k ON k.id = a.kandidat_id"
    " WHERE a.ergebnis='angenommen' AND (a.muster IS NULL OR a.muster='') ORDER BY a.id")]
z = ["# Nachabstraktion des Artgedächtnisses (F5 3.12): Instanzen → Muster",
     f"Angenommene Einträge ohne Muster: {len(offen)} "
     f"(gesamt angenommen: {con.execute(chr(39).join(['SELECT COUNT(*) FROM artgedaechtnis WHERE ergebnis=', 'angenommen', ''])).fetchone()[0]})", ""]
gebildet = nicht = fehlgeschlagen = 0
for e in offen:
    if not (e["diff"] or "").strip():
        z.append(f"  [A{e['id']}] {e['werk']}/{e['bereich']} ({e['kategorie']}): kein Diff mehr vorhanden — übersprungen")
        continue
    try:
        m, von = G.muster_bilden(con, e["kandidat_id"], e["bereich"], e["kategorie"], e["beschreibung"] or "",
                                 e["diff"], e["lauf_id"])
    except Exception as fehler:
        z.append(f"  [A{e['id']}] {e['werk']}/{e['bereich']}: AUFRUFFEHLER {type(fehler).__name__}: {str(fehler)[:120]}")
        fehlgeschlagen += 1
        continue
    if m:
        gebildet += 1
        if SCHREIBEN:
            with transaktion(con):
                con.execute("UPDATE artgedaechtnis SET muster=?, muster_von=? WHERE id=?", (m, von, e["id"]))
        z.append(f"  [A{e['id']}] {e['werk']}/{e['bereich']} ({e['kategorie']}, Zuwachs {e['zuwachs']}):")
        z.append(f"      Instanz: {(e['beschreibung'] or '')[:110]}")
        z.append(f"      MUSTER:  {m}")
    else:
        nicht += 1
        z.append(f"  [A{e['id']}] {e['werk']}/{e['bereich']}: NICHT ÜBERTRAGBAR (kein Muster gebildet)")
z.append(f"\nERGEBNIS: {gebildet} Muster gebildet, {nicht} vom Modell als nicht übertragbar gemeldet, "
         f"{fehlgeschlagen} Aufruffehler (zählen NICHT als inhaltliches Urteil)"
         + ("" if SCHREIBEN else " (Probelauf — nichts geschrieben)"))
if SCHREIBEN:
    protokoll.schreiben(con, "gedaechtnis.muster_nachgetragen", anzahl=gebildet, nicht_uebertragbar=nicht,
                        grund="F5 3.12: Artgedächtnis speichert Muster statt Instanzen; Altbestand beider Werke nachabstrahiert")
    k = con.execute("SELECT COUNT(*) n, ROUND(SUM(kosten_eur),4) c FROM kasse WHERE zweck LIKE 'gedaechtnis.muster%'").fetchone()
    z.append(f"Kosten der Nachabstraktion: {k['n']} Modellaufrufe, {k['c']} €")
(A / "19-muster-nachabstraktion.txt").write_text("\n".join(z) + "\n")
print("\n".join(z[-14:]))
