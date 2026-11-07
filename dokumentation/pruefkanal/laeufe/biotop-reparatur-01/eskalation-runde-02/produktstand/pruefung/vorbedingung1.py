"""Phase 4, Vorbedingung 1: die zwei offenen Bauteile aus Fassung 6 am Übungswerk messen.

Bauteil A (3.7): Der Ankläger nennt seine Behauptung vorab; ist sie im Bereich schon aufgestellt, wird der
  Angriff gar nicht ausgeführt. Messung: Doppelungsanteil unter 20 % der erzeugten Tests, dazu die gesparten
  Aufrufe und Kammerläufe.
Bauteil B (3.12): Mindestanteil des werkübergreifenden Blocks. Messung: ein `lagerhaus`-Lauf mit ≥ 1
  werkübergreifendem Verweis (bisher 0, weil nur 3 fremde Muster gezeigt wurden).
Aufruf: vorbedingung1.py <ausgaben-dir>
"""
import ast
import json
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj
from biotop.organe import gedaechtnis as G
from biotop.organe.aegis import behauptung

A = Path(sys.argv[1])
con = verbinden()
z = ["# Phase 4, Vorbedingung 1 — die zwei offenen Bauteile aus Fassung 6, am Übungswerk gemessen", ""]


def namen(code):
    try:
        return [k.name for k in ast.walk(ast.parse(code)) if isinstance(k, ast.FunctionDef) and k.name.startswith("test_")]
    except SyntaxError:
        return []


# ---------------------------------------------------------------- Bauteil A
z.append("## Bauteil A (3.7): Ankläger nennt die Behauptung vorab")
z.append("")
z.append("### Ansagen je Lauf")
for lauf in (22, 23):
    ges = aus = 0
    doppelt, ohne = [], 0
    for r in con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.ansage'"):
        d = lj(r["inhalt"]) or {}
        if d.get("lauf_id") != lauf:
            continue
        ges += 1
        if d.get("ausgefuehrt"):
            aus += 1
        elif d.get("behauptung"):
            doppelt.append(d["behauptung"])
        else:
            ohne += 1
    if ges:
        z.append(f"  Lauf {lauf}: {ges} Ansagen, {aus} Angriffe ausgeführt, {ges - aus} NICHT ausgeführt "
                 f"({len(doppelt)} wegen bekannter Behauptung, {ohne} mangels Behauptung / KEIN ANGRIFF)")
        if doppelt:
            z.append(f"    verhinderte Wiederholungen: {', '.join(sorted(set(doppelt)))}")
    else:
        z.append(f"  Lauf {lauf}: keine Ansagen (Bauteil war noch nicht eingebaut)")
nicht = 0
for r in con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.ansage'"):
    d = lj(r["inhalt"]) or {}
    if d.get("lauf_id") == 23 and not d.get("ausgefuehrt"):
        nicht += 1
k_ansage = con.execute("SELECT COUNT(*) n, COALESCE(ROUND(SUM(kosten_eur),4),0) c FROM kasse WHERE lauf_id=23 AND zweck LIKE 'aegis.ansage%'").fetchone()
k_angriff = con.execute("SELECT COUNT(*) n, COALESCE(ROUND(SUM(kosten_eur),4),0) c FROM kasse WHERE lauf_id=23 AND zweck LIKE 'aegis.angriff%'").fetchone()
je_angriff = (k_angriff["c"] / k_angriff["n"]) if k_angriff["n"] else 0.0
nicht = con.execute("SELECT COUNT(*) FROM protokoll WHERE art='aegis.ansage' AND inhalt LIKE ? AND inhalt LIKE ?",
                    ('%"lauf_id": 23,%', '%"ausgefuehrt": false%')).fetchone()[0]
z.append("")
z.append(f"### Kosten der Ansage gegen gesparte Angriffe (Lauf 23)")
z.append(f"  Ansagen: {k_ansage['n']} Aufrufe, {k_ansage['c']:.4f} € · Angriffe: {k_angriff['n']} Aufrufe, {k_angriff['c']:.4f} € "
         f"({je_angriff:.4f} € je Angriff)")
z.append(f"  nicht ausgeführte Angriffe: {nicht} → gespart rund {nicht * je_angriff:.4f} € und {nicht} Kammerläufe")
z.append(f"  Saldo: {k_ansage['c'] - nicht * je_angriff:+.4f} € "
         f"({'die Ansage kostet mehr als sie spart' if k_ansage['c'] > nicht * je_angriff else 'die Ansage spart mehr als sie kostet'})")

z.append("")
z.append("### Doppelungsanteil (Tor 2 Zeile 8, Grenze 20 % der erzeugten Tests)")
for lauf, marke in ((20, "Lauf 20 — vor beiden Bauteilen"), (22, "Lauf 22 — nur Anweisung"), (23, "Lauf 23 — mit Ansage")):
    tests = [dict(r) for r in con.execute("SELECT name, bereich, code FROM immunsystem WHERE lauf_id=? AND name LIKE 'aegis_%'", (lauf,))]
    verworfen = 0
    for r in con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil' AND inhalt LIKE ?", (f'%"lauf_id": {lauf},%',)):
        verworfen += len(lj(r["inhalt"]).get("doppelungen") or [])
    gruppen = {}
    for t in tests:
        for n in namen(t["code"]):
            gruppen.setdefault((t["bereich"], behauptung(t["code"], n)), []).append(t["name"])
    doppel = sum(len(v) - 1 for v in gruppen.values() if len(v) > 1)
    erzeugt = len(tests) + verworfen
    groesste = max((len(v) for v in gruppen.values()), default=0)
    if erzeugt == 0:
        # Satz 6: Eine Prüfung ohne Gegenstand besteht nicht, sie meldet. 0 erzeugte Tests ergeben keine 0 %.
        z.append(f"  {marke}: 0 erzeugte Tests → KEIN GEGENSTAND, der Anteil ist nicht bestimmbar (nicht 0 %)")
        z.append(f"    Grund: In diesem Lauf hat der Ankläger keinen einzigen Angriffstest erzeugt.")
        continue
    anteil = 100 * (verworfen + doppel) / erzeugt
    z.append(f"  {marke}: {erzeugt} erzeugte Tests, {len(gruppen)} Behauptungen, "
             f"{verworfen + doppel} Doppelungen = {anteil:.1f} % → {'BESTANDEN' if anteil < 20 else 'GERISSEN'}")
    z.append(f"    Bezugsgröße: {verworfen} vom Ankläger verworfen, {doppel} unbemerkt aufgenommen, "
             f"größte Gruppe {groesste}")

# ---------------------------------------------------------------- Bauteil B
z.append("")
z.append("## Bauteil B (3.12): Mindestanteil des werkübergreifenden Blocks")
z.append("")
z.append("### Bestand und Vorlage")
z.append(f"  Muster je Werk: {[tuple(r) for r in con.execute(chr(34).join(['SELECT werk, COUNT(*) FROM artgedaechtnis WHERE muster IS NOT NULL AND muster!=', '', ' GROUP BY werk']))]}")
for wid, name in ((19, "lagerhaus-p3-22"), (20, "logmuehle-23")):
    t = G.art_text(con, wid)
    i = t.index("ANDERE WERKE")
    z.append(f"  Werk {wid} ({name}): eigene Instanzen {t[:i].count(chr(10))-1}, fremde Muster {t[i:].count(chr(10))-1}")
(A / "03-vorbedingung1-messung.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
