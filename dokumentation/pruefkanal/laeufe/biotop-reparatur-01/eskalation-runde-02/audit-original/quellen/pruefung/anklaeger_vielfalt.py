"""Wirkung der Ankläger-Anweisung (F6): Doppelungsanteil vor und nach der Umstellung, gleiche Rechnung.
Aufruf: anklaeger_vielfalt.py <ausgaben-dir>
"""
import ast
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj
from biotop.organe.aegis import behauptung

A = Path(sys.argv[1])
con = verbinden()


def namen(code):
    try:
        return [k.name for k in ast.walk(ast.parse(code)) if isinstance(k, ast.FunctionDef) and k.name.startswith("test_")]
    except SyntaxError:
        return []


z = ["# Wirkung der Ankläger-Anweisung (Fassung 6): dieselbe Rechnung vor und nach der Umstellung",
     "# Anweisung: Dem Ankläger werden vor jedem Angriff seine bisherigen Behauptungen des Bereichs vorgelegt,",
     "# mit dem Auftrag, eine andere zu finden. Grenze Tor 2 Zeile 8: unter 20 % der erzeugten Tests.",
     "#",
     "# ACHTUNG Vergleichbarkeit (Vorgabe Philipp): Die Prozentzahlen vor und nach dem Schlüsselwechsel zählen",
     "# NICHT dieselbe Menge. Vor dem Wechsel wanderten Wiederholungen unbemerkt ins Immunsystem (der alte",
     "# Schlüssel Meldungsklasse+Ort erkannte sie nie); nach dem Wechsel werden sie erkannt und verworfen.",
     "# Ein Vergleich 63,6 % → 54,5 % liest sich als kleine Verbesserung und verfehlt damit die Sache:",
     "# entscheidend sind die erkannten Doppelungen und die Größe der größten Gruppe gleicher Behauptung.", ""]
for lauf, marke in ((13, "Lauf 13 (Phase 2, vor der Umstellung)"),
                    (20, "Lauf 20 (vor der Umstellung)"),
                    (22, "Lauf 22 (nach der Umstellung, Anweisung aktiv)")):
    tests = [dict(r) for r in con.execute(
        "SELECT name, bereich, code FROM immunsystem WHERE lauf_id=? AND name LIKE 'aegis_%'", (lauf,))]
    verworfen = 0
    for r in con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil' AND inhalt LIKE ?",
                         (f'%"lauf_id": {lauf},%',)):
        verworfen += len(lj(r["inhalt"]).get("doppelungen") or [])
    gruppen = {}
    for t in tests:
        for n in namen(t["code"]):
            gruppen.setdefault((t["bereich"], behauptung(t["code"], n)), []).append(t["name"])
    doppel = sum(len(v) - 1 for v in gruppen.values() if len(v) > 1)
    erzeugt = len(tests) + verworfen
    anteil = 100 * (verworfen + doppel) / max(1, erzeugt)
    z.append(f"{marke}")
    z.append(f"  erzeugte Tests {erzeugt} ({len(tests)} aufgenommen + {verworfen} als Doppelung verworfen), "
             f"{len(gruppen)} verschiedene Behauptungen")
    z.append(f"  Doppelungen gesamt {verworfen + doppel} = {anteil:.1f} % → "
             f"{'unter 20 %, Zeile 8 BESTANDEN' if anteil < 20 else 'über 20 %, Zeile 8 GERISSEN'}")
    groesste = max((len(v) for v in gruppen.values()), default=0)
    z.append(f"  BEZUGSGRÖSSE: {verworfen} vom Ankläger erkannt und verworfen (kamen NICHT ins Immunsystem), "
             f"{doppel} unbemerkt aufgenommen; größte Gruppe gleicher Behauptung: {groesste} Test(s)")
    for (b, k), nm in sorted(gruppen.items(), key=lambda x: -len(x[1]))[:4]:
        z.append(f"    {b} / {k}: {len(nm)} Test(s)")
    z.append("")

# Angriffe ohne Vorschlag: zählt die Anweisung „KEIN ANGRIFF ist kein Fehlschlag"?
for lauf in (20, 22):
    ohne = con.execute("SELECT COUNT(*) FROM protokoll WHERE art='aegis.urteil' AND inhalt LIKE ?",
                       (f'%"lauf_id": {lauf},%"angriff": null%',)).fetchone()[0]
    z.append(f"Lauf {lauf}: Anklägeraufrufe ohne Angriffstest (KEIN ANGRIFF): {ohne}")
(A / "18-anklaeger-vielfalt.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
