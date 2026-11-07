"""Prüft das Organ „Generation minus eins" (Rauschmessung mit bereichsweiser Sperre) an echten Kammerläufen.
Fall A: echtes Werk, echte Referenzlast → Toleranzen je Bereich, Sperren nur wenn wirklich unstet.
Fall B: Referenzlast eines Bereichs absichtlich unstet gemacht → dieser Bereich wird gesperrt, die anderen laufen.
Fall C: dreimal dieselbe Sperre → Befund über die Referenzlast statt über die Maschine.
Aufruf: eichung_pruefen.py <ausgaben-dir>
"""
import random
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden
from biotop.organe import eichung

A = Path(sys.argv[1])
con = verbinden()
pfad = Path("/root/biotop/daten/werke/lagerhaus-p3-20")
ref = Path("/root/biotop/biotop/kern/referenzlast/lagerhaus.py").read_text()
bereiche = ["bericht", "formeln", "lager", "preise"]
z = ["# Generation minus eins — Rauschmessung mit bereichsweiser Sperre (Fassung 5/6), an echten Kammerläufen"]

z.append("\n## Fall A: echtes Werk `lagerhaus` (Stand Lauf 20), echte Referenzlast")
a = eichung.rauschmessung(con, lauf_id=0, werk_id=18, pfad=pfad, bereiche=bereiche, paket="lagerhaus", ref=ref)
z += eichung.text(a)
z.append(f"  Lauf würde starten: {a['lauf_startet']} | Toleranzen an grenzen_f2: {a['toleranz']}")

# Fall B: Referenzlast von `preise` unstet machen (zufällige Schlafzeit) — die anderen Bereiche bleiben unberührt.
unstet = ref.replace("def last_preise(", """def last_preise(*_a, **_k):
    import random, time
    time.sleep(random.choice([0.0, 0.0, 0.05, 0.12]))
    return _last_preise_echt()


def _last_preise_echt(""", 1)
z.append("\n## Fall B: Referenzlast von `preise` absichtlich unstet (zufällige Wartezeit 0–120 ms)")
b = eichung.rauschmessung(con, lauf_id=0, werk_id=999, pfad=pfad, bereiche=bereiche, paket="lagerhaus", ref=unstet)
z += eichung.text(b)
z.append(f"  Lauf würde starten: {b['lauf_startet']} (gefordert: ja — nur `preise` gesperrt, die übrigen arbeiten)")
z.append(f"  Toleranzen, die in den Lauf gehen: {b['toleranz']}")

z.append("\n## Fall C: derselbe Bereich meldet dreimal hintereinander → Befund über die Referenzlast")
for i in (2, 3):
    c = eichung.rauschmessung(con, lauf_id=0, werk_id=999, pfad=pfad, bereiche=["preise"], paket="lagerhaus", ref=unstet)
    e = c["bereiche"]["preise"]
    z.append(f"  Messung {i+0}: gesperrt {e['gesperrt']}, Serie {e['serie']}, Befund über Referenzlast: {e['befund_referenzlast']}")
    if e.get("befund_referenzlast"):
        z.append(f"    Meldung: {e['meldung']}")

alle = eichung.rauschmessung(con, lauf_id=0, werk_id=998, pfad=pfad, bereiche=["preise"], paket="lagerhaus", ref=unstet)
z.append(f"\n## Fall D: einziger Bereich gesperrt → Lauf startet nicht: {not alle['lauf_startet']} (gefordert: ja)")
(A / "02-eichung-rauschmessung-geprueft.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
