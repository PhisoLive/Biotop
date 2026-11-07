"""Lauf 18 verwerfen (Satz 2 F4) und Lauf 19 vom Schnappschuss Lauf 18 Gen 1 vorbereiten."""
import shutil, sys, tarfile
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, transaktion
from biotop.kern import protokoll
from biotop.organe.lazarus import pruefsumme_werk

con = verbinden()
with transaktion(con):
    con.execute("UPDATE generationen SET status='abgebrochen', grund='Lauf verworfen (Satz 2 F4: Immunsystem neubewertet, Testbestand geaendert)' WHERE lauf_id=19 AND status='laeuft'")
    con.execute("UPDATE laeufe SET status='verworfen', beendet_am=? WHERE id=19", (protokoll.jetzt(),))
protokoll.schreiben(con, "lauf.verworfen", lauf_id=19, von="Hermes (Vollmacht Abschnitt 4, Uebungswerk; Abbruch nach Satz 2 vom Freigabe-Gate ausgenommen, Vorgabe Philipp 19.09.2026)",
                    grund="Verfassungssatz 2 F4: Der gemessene Testbestand hat sich geaendert. Gemessener Fund in Lauf 19: 6 von 7 offenen Funden des Werks waren nach der Regel F4 3.7 (Fassung Philipp) Norm, nicht Fund — sie bestehen am Werk, stuerzen nicht ab und nennen keinen Vertrag; sie schrieben den K1165-Fehler als Norm fest und toeteten jede Behebung per Pareto je Test (K1753, K1755, K1784, K1895 u. a.). Belegt in ausgaben/93-funde-neubewertung-werk17.txt (mechanische Pruefung in der Kammer). Lauf 19 Gen 3 (angenommen, formeln 1.88 → 1.31 ms) bleibt als Schnappschuss gueltig und wird Ausgang von Lauf 20.")

z = con.execute("SELECT archiv, pruefsumme FROM lazarus WHERE lauf_id=19 AND generation=1").fetchone()
ziel = Path("/root/uebungswerk-p3d")
if ziel.exists(): shutil.rmtree(ziel)
ziel.mkdir()
with tarfile.open(z["archiv"]) as t: t.extractall(ziel, filter="data")
ps, n = pruefsumme_werk(ziel)
print("Lauf 18 verworfen. Ausgang Lauf 19:", ziel, "| Pruefsumme", ps[:16], "| Dateien", n, "| stimmt:", ps == z["pruefsumme"])
print("Laeufe:", [tuple(r) for r in con.execute("SELECT id, status FROM laeufe WHERE id>=14")])
