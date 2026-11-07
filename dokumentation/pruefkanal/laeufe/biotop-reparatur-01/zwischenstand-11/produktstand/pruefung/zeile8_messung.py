"""Tor 2 Zeile 8, gemessen mit beiden Bauteilen aus Fassung 6 (Phase 4, Vorbedingung 1).

Grenze: Doppelungsanteil unter 20 % der vom Ankläger erzeugten Tests.
Verglichen werden Läufe am selben Werkstand (lagerhaus) mit und ohne die Bauteile.
Aufruf: zeile8_messung.py <ausgaben-dir>
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


def messen(lauf):
    # Nur Tests, die IN DIESEM LAUF erzeugt wurden. Übernommene Altfunde tragen lauf_id des neuen Laufs, aber
    # generation=0 und einen Übernahme-Vermerk im Ursprung — sie sind nicht „vom Ankläger erzeugt" (Grundsatz 5:
    # die Nachrechnung muss dieselbe Menge messen wie die Regel).
    tests = [dict(r) for r in con.execute(
        "SELECT name, bereich, code FROM immunsystem WHERE lauf_id=? AND name LIKE 'aegis_%' "
        "AND generation > 0 AND ursprung NOT LIKE '%übernommen%'", (lauf,))]
    verworfen = 0
    for r in con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil'"):
        d = lj(r["inhalt"]) or {}
        if d.get("lauf_id") == lauf:
            verworfen += len(d.get("doppelungen") or [])
    gruppen = {}
    for t in tests:
        for n in namen(t["code"]):
            gruppen.setdefault((t["bereich"], behauptung(t["code"], n)), []).append(t["name"])
    doppel = sum(len(v) - 1 for v in gruppen.values() if len(v) > 1)
    ges = aus = verhindert = keiner = 0
    for r in con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.ansage'"):
        d = lj(r["inhalt"]) or {}
        if d.get("lauf_id") != lauf:
            continue
        ges += 1
        if d.get("ausgefuehrt"):
            aus += 1
        elif d.get("behauptung"):
            verhindert += 1
        else:
            keiner += 1
    return {"aufgenommen": len(tests), "verworfen": verworfen, "erzeugt": len(tests) + verworfen,
            "behauptungen": len(gruppen), "doppel_unbemerkt": doppel, "doppel_gesamt": verworfen + doppel,
            "groesste": max((len(v) for v in gruppen.values()), default=0),
            "ansagen": ges, "ausgefuehrt": aus, "verhindert": verhindert, "keinangriff": keiner}


z = ["# Tor 2 Zeile 8 — gemessen mit beiden Bauteilen aus Fassung 6",
     "# Grenze: Doppelungsanteil unter 20 % der vom Ankläger ERZEUGTEN Tests.",
     "#",
     "# Vergleichbarkeit: „erzeugt\" = aufgenommen + vom Ankläger als Doppelung verworfen. Ein durch die ANSAGE",
     "# verhinderter Angriff erzeugt gar keinen Test — er erscheint daher nicht im Nenner, sondern als eigene Zahl.",
     ""]
for lauf, marke in ((13, "Lauf 13 — Phase 2, ohne beide Bauteile (Ausgangsmessung 68,5 %)"),
                    (20, "Lauf 20 — ohne beide Bauteile"),
                    (22, "Lauf 22 — nur Anweisung (Zwischenstufe)"),
                    (24, "Lauf 24 — MIT Ansage und Behauptungsschlüssel, gefüllter Vorrat")):
    m = messen(lauf)
    if m["erzeugt"] == 0:
        z.append(f"{marke}: 0 erzeugte Tests → KEIN GEGENSTAND (Satz 6: meldet, besteht nicht)")
        z.append("")
        continue
    anteil = 100 * m["doppel_gesamt"] / m["erzeugt"]
    z.append(f"{marke}")
    z.append(f"  erzeugte Tests {m['erzeugt']} ({m['aufgenommen']} aufgenommen + {m['verworfen']} als Doppelung verworfen)")
    z.append(f"  verschiedene Behauptungen {m['behauptungen']}, größte Gruppe {m['groesste']}")
    z.append(f"  Doppelungen {m['doppel_gesamt']} ({m['verworfen']} erkannt + {m['doppel_unbemerkt']} unbemerkt) "
             f"= {anteil:.1f} % → {'BESTANDEN (< 20 %)' if anteil < 20 else 'GERISSEN (≥ 20 %)'}")
    if m["ansagen"]:
        z.append(f"  Ansagen: {m['ansagen']} — {m['ausgefuehrt']} ausgeführt, {m['verhindert']} Angriffe VERHINDERT "
                 f"(Wiederholung), {m['keinangriff']} KEIN ANGRIFF")
        z.append(f"  → {m['verhindert']} Tests wurden gar nicht erst erzeugt; ohne die Ansage stünden sie als "
                 f"Doppelungen im Nenner: {100*(m['doppel_gesamt']+m['verhindert'])/(m['erzeugt']+m['verhindert']):.1f} %")
    z.append("")

m24 = messen(24)
k_ansage = con.execute("SELECT COUNT(*) n, COALESCE(ROUND(SUM(kosten_eur),4),0) c FROM kasse WHERE lauf_id=24 AND zweck LIKE 'aegis.ansage%'").fetchone()
k_angriff = con.execute("SELECT COUNT(*) n, COALESCE(ROUND(SUM(kosten_eur),4),0) c FROM kasse WHERE lauf_id=24 AND zweck LIKE 'aegis.angriff%'").fetchone()
je = (k_angriff["c"] / k_angriff["n"]) if k_angriff["n"] else 0.0
z.append("## Kosten der Ansage (Lauf 24)")
z.append(f"  Ansagen {k_ansage['n']} Aufrufe, {k_ansage['c']:.4f} € · Angriffe {k_angriff['n']} Aufrufe, {k_angriff['c']:.4f} € ({je:.4f} € je Angriff)")
z.append(f"  verhinderte Angriffe: {m24['verhindert']} → gespart {m24['verhindert']*je:.4f} € und {m24['verhindert']} Kammerläufe")
z.append(f"  Saldo: {m24['verhindert']*je - k_ansage['c']:+.4f} € "
         f"({'die Ansage spart mehr als sie kostet' if m24['verhindert']*je > k_ansage['c'] else 'die Ansage kostet mehr als sie spart'})")
(A / "14-zeile8-messung.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
