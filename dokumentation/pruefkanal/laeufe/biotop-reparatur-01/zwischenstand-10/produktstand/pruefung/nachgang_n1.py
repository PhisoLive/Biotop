"""N1: Welche Verbesserung gehört welchem Bauteil? (Nachgang Vorbedingung 1, Befund F1)
Kein Modellaufruf. Aufruf: nachgang_n1.py <ausgaben-dir>
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


def kennzahlen(lauf):
    tests = [dict(r) for r in con.execute(
        "SELECT name, bereich, code FROM immunsystem WHERE lauf_id=? AND name LIKE 'aegis_%' "
        "AND generation > 0 AND ursprung NOT LIKE '%übernommen%'", (lauf,))]
    verworfen = 0
    for r in con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil'"):
        d = lj(r["inhalt"]) or {}
        if d.get("lauf_id") == lauf:
            verworfen += len(d.get("doppelungen") or [])
    g = {}
    for t in tests:
        for n in namen(t["code"]):
            g.setdefault((t["bereich"], behauptung(t["code"], n)), []).append(t["name"])
    ansagen = sum(1 for r in con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.ansage'")
                  if (lj(r["inhalt"]) or {}).get("lauf_id") == lauf)
    return {"erzeugt": len(tests) + verworfen, "aufgenommen": len(tests), "verworfen": verworfen,
            "groesste": max((len(v) for v in g.values()), default=0),
            "unbemerkt": sum(len(v) - 1 for v in g.values() if len(v) > 1), "ansagen": ansagen}


z = ["# N1 — Zuordnung der Verbesserungen zu den Bauteilen (Befund F1 der Prüfung)",
     "#",
     "# Drei Bauteile sind zu unterscheiden:",
     "#   S = Behauptungs-Schlüssel (Doppelungen werden überhaupt erst erkannt), ab Lauf 22",
     "#   W = Anweisung an den Ankläger (bisherige Behauptungen im Angriffsprompt), ab Lauf 22",
     "#   A = Ansage vorab mit Sperre (Angriff wird nicht ausgeführt), ab Lauf 23/24",
     ""]
z.append(f"{'Lauf':>5} {'S':>2} {'W':>2} {'A':>2} {'erzeugt':>8} {'größte':>7} {'unbemerkt':>10} {'verworfen':>10} {'Ansagen':>8}")
for lauf, s, w, a in ((13, " ", " ", " "), (20, " ", " ", " "), (22, "x", "x", " "), (24, "x", "x", "x")):
    k = kennzahlen(lauf)
    z.append(f"{lauf:>5} {s:>2} {w:>2} {a:>2} {k['erzeugt']:>8} {k['groesste']:>7} {k['unbemerkt']:>10} "
             f"{k['verworfen']:>10} {k['ansagen']:>8}")
z.append("")
z.append("## Zuordnung, berichtigt")
z.append("  größte Gruppe 8 → 1: gehört dem SCHLÜSSEL (S) und der ANWEISUNG (W), erreicht in Lauf 22 OHNE Ansage.")
z.append("  unbemerkte Doppelungen 31 → 0: dasselbe — Lauf 22, ohne Ansage.")
z.append("  Meine Meldung führte beide als Beleg für Bauteil A an. Das war falsch; der Befund F1 trifft zu.")
z.append("")
z.append("  Bauteil A allein zuzurechnen ist:")
z.append("    10 von 27 Ansagen abgewiesen, der Angriff lief gar nicht (Lauf 24) — vorher gab es diesen")
z.append("    Mechanismus nicht, jede Wiederholung kostete einen vollen Angriff plus Kammerlauf.")
z.append("    18 von 65 Ansagen mit „KEIN ANGRIFF\" über die Läufe 22–24 — vorher 0 von allen Aufrufen.")
z.append("    Fehlalarm 0 von 10, Durchgerutscht 0 (N3).")
z.append("")
z.append("## Nebenbefund: auch die Zahlen für Lauf 20 waren falsch gezählt")
z.append("  Meine Meldung wies für Lauf 20 „11 erzeugte Tests, 63,6 %\" aus. 7 der 11 waren übernommener")
z.append("  Altbestand aus Werk 18 (Generation 0), nicht in Lauf 20 erzeugt. Richtig sind 4 erzeugte Tests")
z.append("  mit 3 unbemerkten Doppelungen = 75,0 %. Dieselbe Fehlerklasse wie bei Lauf 24 (dort 41 statt 2),")
z.append("  nur habe ich sie beim ersten Mal nur an einer Stelle korrigiert statt an allen.")
z.append("  Die Richtung der Aussage ändert sich nicht — Zeile 8 war vorher gerissen und ist es geblieben —,")
z.append("  aber die Zahl im Phase-3-Nachlaufbericht (63,6 %) ist hiermit berichtigt auf 75,0 %.")
(A / "17-nachgang-n1-zuordnung.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
