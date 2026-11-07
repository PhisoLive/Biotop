"""Prüft die Zeitraum-Deutung des Serienzählers (Fassung 6, Festlegung Chat-Claude):
Drei Meldungen in einer Sitzung → Deutung „Maschine"; drei an verschiedenen Tagen → Deutung „Referenzlast".
Die Vorgeschichte wird dafür direkt in die Tabelle `eichung` gelegt (keine Kammerläufe nötig), die Deutung
kommt aus dem echten Organ. Aufruf: eichung_zeitraum_pruefen.py <ausgaben-dir>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, transaktion
from biotop.organe import eichung

A = Path(sys.argv[1])
con = verbinden()
eichung._tabelle(con)

def vorgeschichte(werk_id, bereich, zeiten):
    with transaktion(con):
        con.execute("DELETE FROM eichung WHERE werk_id=?", (werk_id,))
        for t in zeiten:
            con.execute("INSERT INTO eichung(lauf_id, werk_id, bereich, toleranz, spannweite, median, werte,"
                        " aussetzer, nachgemessen, gesperrt, meldung, erstellt_am) VALUES (0,?,?,1.8,0.7,10,'[]','[]',0,1,'Messproblem',?)",
                        (werk_id, bereich, t))

# Die Rauschwerte stellt Hermes; geprüft wird allein die Deutung des Zeitraums.
WERTE = [10.0, 10.2, 16.0, 17.0, 17.5]   # Spannweite über der Meldeschwelle → Sperre
z = ["# Serienzähler mit Zeitraum (Fassung 6): drei Meldungen in einer Sitzung = Maschine, an verschiedenen Tagen = Referenzlast",
     f"# Rauschwerte für alle Fälle gleich: {WERTE}"]

for name, werk_id, zeiten in [
    ("Fall 1: zwei Vormeldungen innerhalb EINER Sitzung (14:02, 14:31), dritte jetzt", 9001,
     ["2026-09-19T14:02:00+00:00", "2026-09-19T14:31:00+00:00"]),
    ("Fall 2: zwei Vormeldungen an VERSCHIEDENEN TAGEN (17.09., 18.09.), dritte heute", 9002,
     ["2026-09-17T09:10:00+00:00", "2026-09-18T11:40:00+00:00"]),
]:
    vorgeschichte(werk_id, "preise", zeiten)
    e = eichung.messgeraet.rauschtoleranz_aus_werten(WERTE)
    # Deutung über das Organ bestimmen lassen: dazu die gespeicherte Vorgeschichte lesen wie rauschmessung() es tut
    vorher = [dict(r) for r in con.execute(
        "SELECT gesperrt, erstellt_am FROM eichung WHERE werk_id=? AND bereich='preise' ORDER BY id DESC LIMIT 10", (werk_id,))]
    from biotop.kern import protokoll
    jetzt = protokoll.jetzt()
    zt = [x["erstellt_am"] for x in vorher if x["gesperrt"]]
    serie = len(zt) + 1
    tage = len({t[:10] for t in zt + [jetzt]})
    minuten = eichung._minuten(min(zt + [jetzt]), max(zt + [jetzt]))
    z.append(f"\n{name}")
    z.append(f"  Toleranz {e['toleranz']} (Spannweite {100*(e['spannweite'] or 0):.0f} %) | Serie {serie} | verschiedene Tage: {tage} | Spanne {minuten:.0f} Minuten")
    z.append(f"  Befund über Referenzlast: {serie >= eichung.SPERR_MELDUNGEN_BIS_BEFUND}")
    z.append(f"  DEUTUNG: {'referenzlast' if tage >= 2 else 'maschine'}"
             f" — {'sie misst etwas Unstetes, unabhängig vom Zustand der Maschine' if tage >= 2 else 'fremde Last oder Container-Hänger; vor einem Befund an einem anderen Tag nachmessen'}")
    if tage < 2:
        z.append(f"  VORBEHALT (gilt fuer ALLE Laufzeitmessungen des Zeitraums, nicht nur fuer preise):")
        z.append(f"    Zwischen {min(zt+[jetzt])[:16]} und {max(zt+[jetzt])[:16]} war die Maschine unruhig ({serie} Sperrmeldungen in Folge in einer Sitzung).")
        z.append(f"    Jede Laufzeit- und Grenzmasszahl aus diesem Zeitraum steht unter Vorbehalt — auch die der nicht gesperrten Bereiche.")

(A / "04-serienzaehler-zeitraum.txt").write_text("\n".join(z) + "\n")
with transaktion(con):
    con.execute("DELETE FROM eichung WHERE werk_id IN (9001, 9002)")
print("\n".join(z))
