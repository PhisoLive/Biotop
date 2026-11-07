"""Selbstprüfung der Rauschregeln (Fassung 6, Festlegung Chat-Claude 19.09.2026).
Jeder Fall mit erwartetem Verhalten; Ausgabe zeilenweise. Aufruf: rauschregeln_pruefen.py [<ausgaben-dir>]"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.messgeraet import rauschtoleranz_aus_werten as R, RAUSCH_DECKEL, RAUSCH_MELDESCHWELLE

faelle = [
    ("Aussetzer wie gemessen (formeln, 3 Werte + 2 stabile)", [1.31, 1.51, 35.22, 1.40, 1.45],
     "35,22 als Aussetzer verworfen, nachmessen, Toleranz nahe 1,15"),
    ("stabiler Bereich (bericht, Phase-3-Rauschprobe)", [7.90, 8.15, 8.24, 8.31, 8.46],
     "kein Aussetzer, getrimmte Spannweite 2 % → Mindesttoleranz 1,15"),
    ("echtes hohes Eigenrauschen ohne Aussetzer", [1.6, 1.9, 2.2, 2.5, 2.4],
     "kein Aussetzer, 26 % Spannweite → Toleranz 1,36, UNTER der Meldeschwelle 1,5, keine Meldung"),
    ("zwei Aussetzer", [1.3, 1.4, 1.5, 40.0, 38.0], "beide verworfen, 3 Werte übrig → getrimmt, nachmessen True"),
    ("Meldeschwelle greift ohne Deckel", [1.0, 1.0, 1.6, 1.7, 1.2], "Spannweite 60 % → Toleranz 1,70 > 1,5 → Messproblem gemeldet"),
    ("Deckel greift", [1.0, 1.0, 3.0, 3.0, 2.0], "Toleranz nie über %.1f" % RAUSCH_DECKEL),
    ("alle gleich", [5.0, 5.0, 5.0, 5.0, 5.0], "Spannweite 0 → Mindesttoleranz 1,15, keine Meldung"),
]
z = ["# Selbstprüfung der Rauschregeln (Fassung 6): 5 Werte, höchsten+niedrigsten streichen, Deckel %.1f, Meldeschwelle %.1f, Aussetzer > 5x Median"
     % (RAUSCH_DECKEL, RAUSCH_MELDESCHWELLE)]
for name, werte, erwartet in faelle:
    e = R(werte)
    z.append(f"\n{name}\n  Werte {werte}")
    z.append(f"  Median {e['median']} | Aussetzer {e['aussetzer']} | mittlere {e.get('mittlere')} | Spannweite {e['spannweite']} "
             f"| TOLERANZ {e['toleranz']} | nachmessen {e['nachmessen']}")
    z.append(f"  Meldung: {e['meldung'] or '(keine)'}")
    z.append(f"  erwartet: {erwartet}")
print("\n".join(z))
if len(sys.argv) > 1:
    (Path(sys.argv[1]) / "01-rauschregeln-selbstpruefung.txt").write_text("\n".join(z) + "\n")
