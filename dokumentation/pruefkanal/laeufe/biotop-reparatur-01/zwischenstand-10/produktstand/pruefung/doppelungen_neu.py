"""Punkt 4: Doppelungsschlüssel auf die Behauptung — Tor 2 Zeile 8 neu gemessen (F5 3.10).

Zeile 8 verlangt: Doppelungsanteil unter 20 % DER VOM ANKLÄGER ERZEUGTEN TESTS (nicht der Ablehnungen).
Gemessen wird an den echten Ankläger-Tests in der Datenbank, mit dem neuen Schlüssel `aegis.behauptung`.

Teil A: Der Schlüssel selbst — die sechs Tests der Phase-3-Falle müssen auf EINE Behauptung fallen.
Teil B: Lauf 13 (Phase 2) mit altem und neuem Schlüssel; die 2,5 % und die 83,6 % aus dem Phase-3-Bericht
        werden mit dem gebauten Schlüssel nachgerechnet, nicht mit einer Heuristik.
Teil C: Lauf 20 (der jüngste abgeschlossene Lauf) — hier gilt die Grenze von 20 % für die Neumessung.
Aufruf: doppelungen_neu.py <ausgaben-dir>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj
from biotop.organe.aegis import behauptung

A = Path(sys.argv[1])
con = verbinden()
z = ["# Tor 2 Zeile 8 neu gemessen — Doppelungsschlüssel ist die BEHAUPTUNG (F5 3.10)",
     "# Schlüssel: <aufgerufene Werk-Funktion>|<Zusicherungsart>, aus dem Syntaxbaum des Tests."]


def testnamen(code):
    import ast
    try:
        return [k.name for k in ast.walk(ast.parse(code)) if isinstance(k, ast.FunctionDef) and k.name.startswith("test_")]
    except SyntaxError:
        return []


# --- Teil A: die sechs Tests der Phase-3-Falle
z.append("\n## Teil A: die sechs Tests, die in Phase 3 einzeln ins Immunsystem kamen")
sechs = [dict(r) for r in con.execute(
    "SELECT name, bereich, code FROM immunsystem WHERE name LIKE 'aegis_k119%' OR name LIKE 'aegis_k120%'"
    " OR name LIKE 'aegis_k129%' OR name LIKE 'aegis_k137%' ORDER BY name")]
schluessel = {}
for s in sechs:
    for t in testnamen(s["code"]):
        k = behauptung(s["code"], t, "lagerhaus")
        schluessel.setdefault(k, []).append(s["name"])
        z.append(f"  {s['name']:<28} {t:<50} → {k}")
z.append(f"  ERGEBNIS: {len(sechs)} Tests → {len(schluessel)} verschiedene Behauptungen "
         f"({'alle auf eine — die Falle wäre verhindert worden' if len(schluessel) == 1 else 'mehrere'})")
for k, namen in schluessel.items():
    z.append(f"    {k}: {len(namen)} Tests")

# --- Teile B und C: Anteil je Lauf
for lauf_id, marke in ((13, "Lauf 13 (Phase 2, Tor 2 Zeile 8)"), (20, "Lauf 20 (jüngster abgeschlossener Lauf)")):
    z.append(f"\n## {marke}")
    tests = [dict(r) for r in con.execute(
        "SELECT name, bereich, code, ursprung FROM immunsystem WHERE lauf_id=? AND name LIKE 'aegis_%'", (lauf_id,))]
    verworfen = 0
    for r in con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil' AND inhalt LIKE ?",
                         (f'%"lauf_id": {lauf_id},%',)):
        verworfen += len(lj(r["inhalt"]).get("doppelungen") or [])
    erzeugt = len(tests) + verworfen
    # neuer Schlüssel je Bereich
    gruppen = {}
    for t in tests:
        for name in testnamen(t["code"]):
            gruppen.setdefault((t["bereich"], behauptung(t["code"], name, "lagerhaus")), []).append(t["name"])
    doppel_neu = sum(len(v) - 1 for v in gruppen.values() if len(v) > 1)
    z.append(f"  vom Ankläger erzeugte Tests: {erzeugt} ({len(tests)} aufgenommen + {verworfen} als Doppelung verworfen)")
    z.append(f"  alter Schlüssel (Meldungsklasse, Ort): {verworfen} Doppelungen = "
             f"{100*verworfen/max(1,erzeugt):.1f} % der erzeugten Tests")
    z.append(f"  neuer Schlüssel (Behauptung): {len(gruppen)} verschiedene Behauptungen unter {len(tests)} aufgenommenen "
             f"→ zusätzlich {doppel_neu} Doppelungen")
    gesamt = verworfen + doppel_neu
    z.append(f"  ANTEIL NEU: ({verworfen}+{doppel_neu})/{erzeugt} = {100*gesamt/max(1,erzeugt):.1f} % "
             f"— Grenze Tor 2 Zeile 8: unter 20 % → {'BESTANDEN' if 100*gesamt/max(1,erzeugt) < 20 else 'GERISSEN'}")
    for (b, k), namen in sorted(gruppen.items(), key=lambda x: -len(x[1]))[:5]:
        if len(namen) > 1:
            z.append(f"    mehrfach ({b}, {k}): {len(namen)} Tests — {', '.join(sorted(namen)[:6])}")

z.append("\n## Bedeutung")
z.append("  Der Anteil misst, wie viele der erzeugten Tests dieselbe Behauptung wiederholen. Ein hoher Anteil heißt:")
z.append("  Der Ankläger findet wenig Verschiedenes; die Grenze von 20 % ist eine Aussage über SEINE Vielfalt,")
z.append("  nicht über das Werk. Mit dem neuen Schlüssel wird dieser Anteil zum ersten Mal richtig gemessen.")
(A / "13-doppelungen-behauptung.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
