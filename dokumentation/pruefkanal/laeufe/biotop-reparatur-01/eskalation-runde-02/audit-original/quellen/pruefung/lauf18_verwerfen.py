"""Lauf 18 verwerfen (Satz 2 F4) und Lauf 19 vom Schnappschuss Lauf 18 Gen 1 vorbereiten."""
import shutil, sys, tarfile
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, transaktion
from biotop.kern import protokoll
from biotop.organe.lazarus import pruefsumme_werk

con = verbinden()
with transaktion(con):
    con.execute("UPDATE generationen SET status='abgebrochen', grund='Lauf verworfen (Satz 2 F4: Projektgedaechtnis-Filter geaendert)' WHERE lauf_id=18 AND status='laeuft'")
    con.execute("UPDATE laeufe SET status='verworfen', beendet_am=? WHERE id=18", (protokoll.jetzt(),))
protokoll.schreiben(con, "lauf.verworfen", lauf_id=18, von="Hermes (Vollmacht Abschnitt 4, Uebungswerk; Abbruch nach Satz 2 ist vom Freigabe-Gate ausgenommen, Vorgabe Philipp 19.09.2026)",
                    grund="Verfassungssatz 2 F4: Das Projektgedaechtnis ist Teil des Messgeraets (es verwirft Kandidaten OHNE Kammerlauf). Gemessener Fund in Lauf 18 Gen 2/3: 12 von 13 Wiederholungs-Verwerfungen beriefen sich auf Lauf 16 — einen Lauf, der selbst wegen eines fehlerhaften Anklaegers verworfen wurde. Korrektur: gescheiterte Wege aus verworfenen Laeufen zaehlen nicht mehr (gedaechtnis.gescheiterte_wege und gedaechtnis.wiederholung filtern laeufe.status != 'verworfen'). Lauf 18 Gen 1 (angenommen, Laufzeit formeln 123,19 → 1,87 ms, preise 92,12 → 13,26 ms) bleibt als Schnappschuss gueltig und wird Ausgang von Lauf 19.")

z = con.execute("SELECT archiv, pruefsumme FROM lazarus WHERE lauf_id=18 AND generation=1").fetchone()
ziel = Path("/root/uebungswerk-p3c")
if ziel.exists(): shutil.rmtree(ziel)
ziel.mkdir()
with tarfile.open(z["archiv"]) as t: t.extractall(ziel, filter="data")
ps, n = pruefsumme_werk(ziel)
print("Lauf 18 verworfen. Ausgang Lauf 19:", ziel, "| Pruefsumme", ps[:16], "| Dateien", n, "| stimmt:", ps == z["pruefsumme"])
print("Laeufe:", [tuple(r) for r in con.execute("SELECT id, status FROM laeufe WHERE id>=14")])
