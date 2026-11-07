"""Rauschmessung: bericht.laufzeit_ms fünfmal am UNVERÄNDERTEN Werk von Lauf 19 messen.
Prüft, ob die Ablehnungen von Gen 1/2 (12,10 und 14,78 ms gegen Grenze 9,90) echte Verschlechterung oder Messrauschen sind.
Aufruf: rauschprobe_lauf19.py <ausgaben-dir>"""
import statistics, sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern import messgeraet

A = Path(sys.argv[1])
w = Path("/root/biotop/daten/werke/lagerhaus-p3-19")
ref = Path("/root/biotop/biotop/kern/referenzlast/lagerhaus.py").read_text()
zeilen = ["# Rauschprobe Lauf 19 — bericht.laufzeit_ms am UNVERÄNDERTEN Werk (jede Messung = Minimum aus 3 Läufen in der Kammer)"]
werte = {}
for i in range(5):
    m = messgeraet.messen(w, ["bericht", "formeln", "lager", "preise"], "lagerhaus", ref)
    for b in ("bericht", "formeln"):
        werte.setdefault(b, []).append(m["bereiche"][b]["laufzeit_ms"])
    zeilen.append(f"Messung {i+1}: bericht {m['bereiche']['bericht']['laufzeit_ms']:.2f} ms | formeln {m['bereiche']['formeln']['laufzeit_ms']:.2f} ms")
for b, v in werte.items():
    zeilen.append(f"{b}: min {min(v):.2f} | max {max(v):.2f} | median {statistics.median(v):.2f} | Spanne {(max(v)-min(v))/min(v)*100:.1f} % über 5 Messungen")
zeilen.append("Im Lauf gesetzte Grenze bericht: 9.90 ms (Bestwert 8.64 × 1.15). Abgelehnt wurden Gen 1 mit 12.10 und Gen 2 mit 14.78 ms.")
b = werte["bericht"]
zeilen.append(f"BEFUND: {'Messrauschen erreicht die abgelehnten Werte (Höchstwert ohne jede Änderung: %.2f ms) → die Ablehnungen sind nicht beweisbar echte Verschlechterung' % max(b) if max(b) >= 12.10 else 'Messrauschen bleibt unter den abgelehnten Werten (Höchstwert ohne Änderung: %.2f ms) → die Ablehnungen sind echte Verschlechterung' % max(b)}")
(A / "92-rauschprobe-lauf19.txt").write_text("\n".join(zeilen) + "\n")
print("\n".join(zeilen))
