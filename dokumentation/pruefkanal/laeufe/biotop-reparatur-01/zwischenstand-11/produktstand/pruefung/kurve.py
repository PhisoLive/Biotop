"""Verlaufskurve je Werk als SVG + Textfassung: Kernmaß F2 und Laufzeiten je angenommener Generation, über die
gültigen Läufe des Werks hinweg (verworfene Läufe mit ihrem Beitrag markiert, weil ihr Schnappschuss Ausgang des
nächsten Laufs war). Aufruf: kurve.py <ausgaben-dir> <werkname> <lauf-id...>"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj

A = Path(sys.argv[1]); WERK = sys.argv[2]; LAEUFE = [int(x) for x in sys.argv[3:]]
con = verbinden()
punkte = []  # (beschriftung, kernmass_f2, {bereich: laufzeit}, tests_gesamt, status_lauf)
for L in LAEUFE:
    lstatus = con.execute("SELECT status FROM laeufe WHERE id=?", (L,)).fetchone()[0]
    for z in con.execute("SELECT generation, tag, masse FROM lazarus WHERE lauf_id=? ORDER BY generation", (L,)):
        m = lj(z["masse"]) or {}
        b = m.get("bereiche") or {}
        if not b: continue
        punkte.append((f"L{L}G{z['generation']}", m.get("kernmass_f2"), {k: v.get("laufzeit_ms") for k, v in b.items()},
                       sum(v.get("tests_gesamt") or 0 for v in b.values()), lstatus))
# Textfassung
zeilen = [f"# Verlaufskurve {WERK} — Läufe {LAEUFE} (Phase 3)",
          "Punkt        Kernmaß_F2  Tests  " + "  ".join(f"{b:>10}" for b in sorted(punkte[0][2])) + "   Lauf-Status"]
for p in punkte:
    zeilen.append(f"{p[0]:<12} {str(p[1]):>10}  {p[3]:>5}  " + "  ".join(f"{(p[2].get(b) or 0):>10.2f}" for b in sorted(punkte[0][2])) + f"   {p[4]}")
(A / f"kurve-{WERK}.txt").write_text("\n".join(zeilen) + "\n")

# SVG: Kernmaß (links) und Laufzeit je Bereich (rechts, logarithmisch nicht nötig)
W, H, PL, PR, PT, PB = 900, 430, 70, 150, 40, 70
n = max(1, len(punkte) - 1)
bereiche = sorted(punkte[0][2])
lmax = max(max((p[2].get(b) or 0) for b in bereiche) for p in punkte) or 1
kmin = min(p[1] for p in punkte if p[1] is not None)
farben = {"bericht": "#c0392b", "formeln": "#27ae60", "lager": "#2980b9", "preise": "#8e44ad",
          "lesen": "#c0392b", "filtern": "#27ae60", "zaehlen": "#2980b9", "ausgabe": "#8e44ad"}
def x(i): return PL + i * (W - PL - PR) / n
def yk(v): return PT + (0 - v) / max(1, abs(kmin)) * (H - PT - PB) * 0.35 + 10
def yl(v): return H - PB - (v / lmax) * (H - PT - PB) * 0.55
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="sans-serif" font-size="11">',
     f'<rect width="{W}" height="{H}" fill="white"/>',
     f'<text x="{PL}" y="20" font-size="14" font-weight="bold">Verlauf {WERK} — Phase 3 (Läufe {", ".join(map(str, LAEUFE))})</text>',
     f'<line x1="{PL}" y1="{H-PB}" x2="{W-PR}" y2="{H-PB}" stroke="#333"/>']
for i, p in enumerate(punkte):
    s.append(f'<text x="{x(i)}" y="{H-PB+16}" text-anchor="middle" font-size="9" fill="{"#999" if p[4]=="verworfen" else "#333"}">{p[0]}</text>')
    if p[4] == "verworfen": s.append(f'<text x="{x(i)}" y="{H-PB+28}" text-anchor="middle" font-size="8" fill="#999">verw.</text>')
for b in bereiche:
    d = " ".join(f"{'M' if i==0 else 'L'}{x(i):.1f},{yl(p[2].get(b) or 0):.1f}" for i, p in enumerate(punkte))
    s.append(f'<path d="{d}" fill="none" stroke="{farben.get(b, "#555")}" stroke-width="2"/>')
    s.append(f'<text x="{W-PR+8}" y="{yl(punkte[-1][2].get(b) or 0):.1f}" fill="{farben.get(b, "#555")}">{b} {punkte[-1][2].get(b):.1f} ms</text>')
d = " ".join(f"{'M' if i==0 else 'L'}{x(i):.1f},{yk(p[1] or 0):.1f}" for i, p in enumerate(punkte))
s.append(f'<path d="{d}" fill="none" stroke="#111" stroke-width="3" stroke-dasharray="5,3"/>')
s.append(f'<text x="{W-PR+8}" y="{yk(punkte[-1][1] or 0):.1f}" font-weight="bold">Kernmaß F2 = {punkte[-1][1]}</text>')
s.append(f'<text x="{PL}" y="{H-14}" font-size="10" fill="#555">Durchgezogen: Laufzeit je Bereich (ms, Referenzlast). Gestrichelt: Kernmaß F2 (Höchstwert 0). Endtestbestand: {punkte[-1][3]} Tests.</text>')
s.append("</svg>")
(A / f"kurve-{WERK}.svg").write_text("\n".join(s))
print("\n".join(zeilen))
print(f"→ kurve-{WERK}.svg, kurve-{WERK}.txt")
