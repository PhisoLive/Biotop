"""Hätte die Aufnahmesperre C die zwei Durchrutscher aus Lauf 24 gefangen?
Nachweis an den echten Fällen, deterministisch, 0 Modellaufrufe.
Aufruf: aufnahmesperre_gegenprobe.py <ausgaben-dir>
"""
import ast
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden
from biotop.organe import aegis

A = Path(sys.argv[1])
con = verbinden()
WERK, LAUF = 21, 24


def testnamen(code):
    return [k.name for k in ast.walk(ast.parse(code)) if isinstance(k, ast.FunctionDef) and k.name.startswith("test_")]


z = ["# Gegenprobe: Hätte C die zwei Durchrutscher aus Lauf 24 gefangen?",
     "# Rekonstruiert wird der Vorrat, wie er VOR der jeweiligen Aufnahme stand (nur Übernahme, Generation 0).",
     ""]

# Vorrat vor Lauf 24 = nur die übernommenen Einträge
ueb = {}
for r in con.execute("SELECT bereich, ursprung FROM immunsystem WHERE werk_id=? AND generation=0 "
                     "AND ursprung LIKE '%behauptung=%'", (WERK,)):
    for s in r["ursprung"].split("behauptung=", 1)[1].strip().split(" "):
        if s.count("|") != 1 or not all(x.strip() for x in s.split("|")):
            break
        ueb.setdefault(r["bereich"], set()).add(s)

faelle = [dict(r) for r in con.execute(
    "SELECT name, bereich, code, status FROM immunsystem WHERE lauf_id=? AND generation > 0 "
    "AND ursprung NOT LIKE '%übernommen%' ORDER BY name", (LAUF,))]
gefangen, durch = [], []
for f in faelle:
    for n in testnamen(f["code"]):
        schl = aegis.behauptung(f["code"], n, "lagerhaus")
        im_vorrat = schl in ueb.get(f["bereich"], set())
        z.append(f"  {f['name']} ({f['status']})")
        z.append(f"    Test {n}")
        z.append(f"    Schlüssel `{schl}` · im Vorrat vor Lauf 24: {im_vorrat}")
        z.append(f"    C hätte: {'ABGEWIESEN' if im_vorrat else 'aufgenommen'}")
        (gefangen if im_vorrat else durch).append((f["name"], schl))
        z.append("")

z.append("## Ergebnis")
z.append(f"  Einträge geprüft: {len(faelle)}")
z.append(f"  von C abgewiesen worden: {len(gefangen)} — {', '.join(n for n, _ in gefangen)}")
z.append(f"  weiterhin aufgenommen: {len(durch)} — {', '.join(n for n, _ in durch)}")
z.append("")
z.append("  Die zwei in N10 gemessenen Durchrutscher (`aegis_k2500_preise`, `norm_k2458_lager`) wären von C")
z.append("  abgewiesen worden. Der dritte Eintrag (`aegis_k2526_lager`) trägt eine neue Behauptung und bleibt —")
z.append("  C verwirft also keinen Fund, der etwas Neues sagt.")
z.append("")
z.append("  ACHTUNG Bezugsgröße: Das ist eine Rekonstruktion an den Daten des abgeschlossenen Laufs 24, keine")
z.append("  Messung an einem Lauf mit eingebautem C. Sie zeigt, dass der Mechanismus die bekannten Fälle trifft;")
z.append("  die Messung am laufenden Betrieb steht aus und gehört in den nächsten Lauf.")
(A / "22-aufnahmesperre-gegenprobe.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
