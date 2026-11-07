"""Altbestand: Behauptungs-Schlüssel in den `ursprung` vorhandener Immunsystem-Einträge nachtragen (F5 3.10).

Ohne Nachtrag sähe der Ankläger im ersten Lauf nach der Umstellung eine leere Liste bisheriger Behauptungen —
die Regel wäre eingebaut, aber wirkungslos, und die Neumessung wäre wertlos.
Aufruf: behauptungen_nachtragen.py <ausgaben-dir> [--schreiben]
"""
import ast
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern import protokoll
from biotop.kern.datenbank import verbinden, transaktion
from biotop.organe.aegis import behauptung

A = Path(sys.argv[1]); SCHREIBEN = "--schreiben" in sys.argv
con = verbinden()

def testnamen(code):
    try:
        return [k.name for k in ast.walk(ast.parse(code)) if isinstance(k, ast.FunctionDef) and k.name.startswith("test_")]
    except SyntaxError:
        return []

eintraege = [dict(r) for r in con.execute(
    "SELECT id, name, werk_id, bereich, code, ursprung FROM immunsystem WHERE ursprung NOT LIKE '%behauptung=%'")]
z = ["# Behauptungs-Schlüssel für den Altbestand nachtragen (F5 3.10)",
     f"Einträge ohne Schlüssel: {len(eintraege)} von "
     f"{con.execute('SELECT COUNT(*) FROM immunsystem').fetchone()[0]}"]
nachgetragen = 0
for e in eintraege:
    namen = testnamen(e["code"])
    schluessel = " ".join(sorted({behauptung(e["code"], t) for t in namen})) if namen else ""
    if not schluessel:
        z.append(f"  {e['name']}: kein Testname erkannt — übersprungen")
        continue
    if SCHREIBEN:
        with transaktion(con):
            con.execute("UPDATE immunsystem SET ursprung = ursprung || ? WHERE id=?",
                        (f" behauptung={schluessel}", e["id"]))
    nachgetragen += 1
z.append(f"nachgetragen: {nachgetragen}" + ("" if SCHREIBEN else " (Probelauf — nichts geschrieben)"))
if SCHREIBEN and nachgetragen:
    protokoll.schreiben(con, "immun.behauptung_nachgetragen", anzahl=nachgetragen,
                        grund="F5 3.10: Doppelungsschlüssel ist die Behauptung; Altbestand ohne Schlüssel nachgetragen, "
                              "damit der Ankläger seine bisherigen Behauptungen sieht")
# Wirkung zeigen
from biotop.organe.aegis import bisherige_behauptungen
for werk_id, bereich in ((18, "preise"), (18, "lager"), (15, "filtern")):
    b = bisherige_behauptungen(con, werk_id, bereich)
    z.append(f"  Werk {werk_id}, Bereich {bereich}: {len(b)} bisherige Behauptungen sichtbar — {', '.join(b[:6])}")
(A / "14-behauptungen-nachgetragen.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
