"""Fall D nachgemessen: EINZIGER Bereich gesperrt → der Lauf startet nicht (Satz 6: laut scheitern).
Die Referenzlast wird hier sicher unstet gemacht (abwechselnd schnell/langsam), nicht zufällig.
Aufruf: eichung_falld.py <ausgaben-dir>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden
from biotop.organe import eichung

A = Path(sys.argv[1])
con = verbinden()
pfad = Path("/root/biotop/daten/werke/lagerhaus-p3-20")
ref = Path("/root/biotop/biotop/kern/referenzlast/lagerhaus.py").read_text()

# Sicher unstet ZWISCHEN den Messungen: Der Median aus drei Durchläufen glättet Schwankungen INNERHALB einer
# Messung — genau dafür ist er da. Die Rauschmessung sieht Unstetigkeit also nur, wenn sich ganze Messungen
# unterscheiden. Deshalb hängt die Wartezeit hier am Messungs-Index ((Aufruf-1)//3), nicht am Einzelaufruf.
# (Erster Versuch mit Wartezeit je Einzelaufruf ergab fünf stabile Werte — die Probe war falsch, nicht das Organ.)
unstet = ref.replace("def last_preise(", """_ZAEHLER = [0]


def last_preise(*_a, **_k):
    import time
    _ZAEHLER[0] += 1
    messung = (_ZAEHLER[0] - 1) // 3          # drei Durchläufe je Messwert (Median-Regel F5 3.5)
    if messung % 2 == 1:
        time.sleep(0.15)
    return _last_preise_echt()


def _last_preise_echt(""", 1)

d = eichung.rauschmessung(con, lauf_id=0, werk_id=997, pfad=pfad, bereiche=["preise"], paket="lagerhaus", ref=unstet)
z = ["# Fall D nachgemessen — einziger Bereich gesperrt, Referenzlast sicher unstet (jeder zweite Aufruf +150 ms)"]
z += eichung.text(d)
e = d["bereiche"]["preise"]
z.append(f"  Werte {e.get('werte')} | Median {e.get('median')} | Spannweite {100*(e.get('spannweite') or 0):.0f} % | Toleranz {e['toleranz']}")
z.append(f"  lauf_startet = {d['lauf_startet']} (gefordert: False, weil 1 von 1 Bereichen gesperrt ist)")
z.append(f"  ERGEBNIS: {'bestanden — der Lauf startet nicht' if not d['lauf_startet'] else 'NICHT bestanden'}")
p = con.execute("SELECT nr, inhalt FROM protokoll WHERE art='eichung.lauf_startet_nicht' ORDER BY nr DESC LIMIT 1").fetchone()
z.append(f"  Protokoll: #{p['nr']} {p['inhalt'][:220]}" if p else "  Protokoll: keine Zeile (FEHLER)")
(A / "03-eichung-falld.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
