"""Tor 3 — Geschmacksgedächtnis (Mechanikprüfung mit versiegelter Regel P1).
Aufruf: tor3_geschmack.py <ausgaben-dir>"""
import hashlib, json, sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj
from biotop.kern import protokoll
from biotop.organe import gedaechtnis as G

A = Path(sys.argv[1])
con = verbinden(); G.tabellen(con)
out = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s)

def regel_p1(m: dict) -> str:
    if m["diff_klasse"] == "gross" and m["zuwachs"] <= 0:
        return "ablehnen"
    if m["kommentare_hinzu"] >= 3:
        return "ablehnen"
    if m["wird_kleiner"]:
        return "frei"
    if m["zuwachs"] >= 1:
        return "frei"
    if m["laufzeit_gewinn"] and m["nische"] == "schnell" and m["diff_klasse"] != "gross":
        return "frei"
    return "ablehnen"

p("# Tor 3 — Geschmacksgedächtnis: Mechanikprüfung mit versiegelter Regel P1 (kein Nachweis über Philipps Geschmack)")
p("Regel: /root/versiegelt/GESCHMACK-regel-P1.md, sha256", hashlib.sha256(Path("/root/versiegelt/GESCHMACK-regel-P1.md").read_bytes()).hexdigest())
# 30 Kandidaten: angenommen/überlebt/abgelehnt mit Diff und Maß aus Lauf 13 und 12 — gemischt, in ID-Reihenfolge, damit die Regel beide Klassen trifft
ks = [dict(z) for z in con.execute("SELECT id, lauf_id, generation, status FROM kandidaten WHERE lauf_id IN (12,13) AND diff!='' AND masse IS NOT NULL AND nische!='probe' AND status IN ('angenommen','ueberlebt','abgelehnt') ORDER BY id")]
# gleichmäßig: jeder 6. Kandidat, bis 30 erreicht
ausw = [k for i, k in enumerate(ks) if i % max(1, len(ks) // 30) == 0][:30]
if len(ausw) < 30:
    ausw = ks[:30]
(A / "21-geschmack-eingaben.json").write_text(json.dumps(ausw, ensure_ascii=False, indent=1))
p(f"Eingaben: {len(ausw)} Kandidaten aus {len(ks)} mit Diff+Maß (Läufe 12/13), Liste in 21-geschmack-eingaben.json")
werk = G.werkname(con, con.execute("SELECT werk_id FROM laeufe WHERE id=13").fetchone()[0])
con.execute("DELETE FROM geschmack WHERE quelle='regel_P1'"); con.commit()
ents = []
for k in ausw:
    m = G.merkmale_kandidat(con, k["id"]); e = regel_p1(m)
    ents.append((k["id"], e, m))
p("Verteilung der Regel-Entscheidungen: frei %d, ablehnen %d" % (sum(1 for _, e, _ in ents if e == "frei"), sum(1 for _, e, _ in ents if e == "ablehnen")))
# Lernen aus den ersten 20
for kid, e, m in ents[:20]:
    k = next(x for x in ausw if x["id"] == kid)
    G.geschmack_merken(con, k["lauf_id"] and con.execute("SELECT werk_id FROM laeufe WHERE id=?", (k["lauf_id"],)).fetchone()[0], k["lauf_id"], k["generation"], kid, e, "Regel P1", "Simulation P1", quelle="regel_P1")
modell = G.geschmack_modell(con, quelle="regel_P1")
p(f"Modell gelernt aus {modell.gesamt if modell else 0} Entscheidungen (Naive Bayes, biotop/organe/gedaechtnis.py:Vorhersage)")
richtig = 0
p("\nHold-out (Kandidaten 21–30):")
for kid, e, m in ents[20:]:
    v, s, gr = modell.vorhersagen(m)
    ok = v == e; richtig += ok
    p(f"  K{kid}: Regel {e:8s} Vorhersage {v:8s} ({s*100:.0f} %) {'richtig' if ok else 'FALSCH'} — {', '.join(gr)}")
p(f"\nERGEBNIS: {richtig} von 10 richtig vorhergesagt (Ziel ≥ 7). Mechanikprüfung; Philipps echte Entscheidungen erst ab Phase 4.")
protokoll.schreiben(con, "geschmack.mechanikpruefung", regel="P1", gelernt=20, holdout=10, richtig=richtig, eingaben=[k["id"] for k in ausw])
(A / "21-tor3-geschmack.txt").write_text("\n".join(out) + "\n")
