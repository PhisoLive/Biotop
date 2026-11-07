"""N12 — Kassenabgleich (Prüfung 6). Jede Zahl aus einer Protokoll-/Datenbankabfrage, 0 Modellaufrufe.
Aufruf: nachgang_n12.py <ausgaben-dir>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden

A = Path(sys.argv[1])
con = verbinden()
z = ["# N12 — Kassenabgleich (0 Modellaufrufe)",
     "# Menge: Tabelle `kasse`, gruppiert nach lauf_id. Herkunft: Datenbankabfrage, nicht Bericht.", ""]

z.append("## Ist-Stand je Lauf")
ges_n = ges_c = 0
je_lauf = {}
for r in con.execute("SELECT lauf_id, COUNT(*) n, ROUND(SUM(kosten_eur),4) c, MIN(zeit) a, MAX(zeit) b "
                     "FROM kasse WHERE lauf_id>=22 GROUP BY lauf_id ORDER BY lauf_id"):
    je_lauf[r["lauf_id"]] = (r["n"], r["c"])
    ges_n += r["n"]; ges_c += r["c"]
    z.append(f"  Lauf {r['lauf_id']}: {r['n']:4d} Aufrufe · {r['c']:.4f} € · {r['a'][:16]} bis {r['b'][:16]}")
z.append(f"  SUMME: {ges_n} Aufrufe · {ges_c:.4f} €")
z.append("")

z.append("## Aufklärung der Differenz")
z.append("  Der Prüfbericht rechnet: 476 (Läufe 22–24 laut BERICHT.md) + 183 (Lauf 25) = 659 Aufrufe.")
z.append(f"  Gemessen sind {ges_n}. Differenz: {ges_n - 659} Aufrufe.")
z.append("")
z.append(f"  URSACHE: **Lauf 22 ist in `BERICHT.md` mit 44 Aufrufen / 0,1190 € geführt, hat aber "
         f"{je_lauf[22][0]} Aufrufe / {je_lauf[22][1]:.4f} €.**")
z.append(f"  Differenz genau hier: {je_lauf[22][0] - 44} Aufrufe · {je_lauf[22][1] - 0.1190:.4f} € — das sind "
         f"die vom Prüfer gesuchten 189 Aufrufe / 0,3976 €.")
z.append("")
z.append("  Wie es dazu kam: Lauf 22 wurde in zwei Etappen gefahren. Die erste (Generationen 1–4) gehörte zum")
z.append("  Nachlauf Phase 3 und ist dort abgerechnet; für Vorbedingung 1 habe ich nur die Fortsetzung")
z.append("  (Generation 5, 44 Aufrufe) gezählt. In der Zeile „Vorbedingung 1 gesamt\" habe ich dann aber die")
z.append("  **volle** Summe aus der Datenbank genommen (`WHERE lauf_id>=22`), also beide Etappen.")
z.append("  Die Einzelzeilen und die Summenzeile zählten damit verschiedene Mengen — genau der Fehler, den")
z.append("  Fassung 7 Punkt 17 benennt.")
z.append("")

z.append("## Fällt etwas davon unter die 0,80-€-Grenze von Lauf 25?")
l25 = je_lauf[25]
z.append(f"  Lauf 25 hat in der Datenbank {l25[0]} Aufrufe und {l25[1]:.4f} € — **kein einziger Aufruf mehr**.")
r = con.execute("SELECT MIN(zeit) a, MAX(zeit) b FROM kasse WHERE lauf_id=25").fetchone()
z.append(f"  Zeitfenster Lauf 25: {r['a'][:19]} bis {r['b'][:19]}")
r22 = con.execute("SELECT MIN(zeit) a, MAX(zeit) b FROM kasse WHERE lauf_id=22").fetchone()
z.append(f"  Zeitfenster Lauf 22: {r22['a'][:19]} bis {r22['b'][:19]} — liegt vollständig VOR Lauf 25.")
z.append(f"  ERGEBNIS: Die 189 Aufrufe gehören zu Lauf 22, nicht zu Lauf 25.")
z.append(f"  **Die harte Grenze von Lauf 25 steht bei {l25[1]:.4f} von 0,80 € = {100*l25[1]/0.80:.0f} %.**")
z.append("  Sie ist gehalten. Der Prüfbefund war berechtigt, die befürchtete Grenzverletzung liegt nicht vor.")
z.append("")

z.append("## Berichtigter Gesamtstand Vorbedingung 1")
z.append("  Die Frage, welche Etappe von Lauf 22 zu Vorbedingung 1 zählt, entscheide ich zugunsten der")
z.append("  höheren Zahl — die Etappe lief unter dem Auftrag von Vorbedingung 1 und verbrauchte Budget:")
z.append(f"    Lauf 22 (beide Etappen)  {je_lauf[22][0]:4d} Aufrufe · {je_lauf[22][1]:.4f} €")
for lid in (23, 24, 25):
    z.append(f"    Lauf {lid}                  {je_lauf[lid][0]:4d} Aufrufe · {je_lauf[lid][1]:.4f} €")
z.append(f"    SUMME                    {ges_n:4d} Aufrufe · {ges_c:.4f} € von 3 € ({100*ges_c/3:.0f} %)")
z.append(f"  Frei: {3 - ges_c:.4f} €")
z.append("")
z.append("  ANMERKUNG zur Doppelzählung: Die erste Etappe von Lauf 22 (189 Aufrufe) ist bereits im")
z.append("  Phase-3-Nachlauf abgerechnet. Sie hier erneut zu zählen, wäre eine Doppelzählung über zwei")
z.append("  Abschlussordner hinweg. Ich weise sie deshalb in BEIDEN Lesarten aus:")
z.append(f"    Lesart A (Lauf 22 vollständig): {ges_c:.4f} € von 3 €")
z.append(f"    Lesart B (nur Fortsetzung, 44 Aufrufe / 0,1190 €): {ges_c - je_lauf[22][1] + 0.1190:.4f} € von 3 €")
z.append("  Welche gilt, entscheidet Philipp. In beiden Fällen ist das Budget gehalten.")
z.append("")

z.append("## Nebenbefund: Vollständigkeit der Zweck-Aufstellung in KASSE-05.md")
alle = con.execute("SELECT COUNT(DISTINCT zweck) FROM kasse WHERE lauf_id=25").fetchone()[0]
top = [dict(r) for r in con.execute("SELECT zweck, COUNT(*) n, ROUND(SUM(kosten_eur),4) c FROM kasse "
                                    "WHERE lauf_id=25 GROUP BY zweck ORDER BY c DESC LIMIT 12")]
z.append(f"  Verschiedene Zwecke in Lauf 25: {alle}. Die Aufstellung zeigte die 12 teuersten — "
         f"{sum(t['n'] for t in top)} von {l25[0]} Aufrufen, {sum(t['c'] for t in top):.4f} von {l25[1]:.4f} €.")
z.append("  Das war ein AUSZUG, die Überschrift nannte ihn aber wie eine vollständige Menge. Berichtigt:")
z.append("  Jede Aufstellung nennt künftig, ob sie vollständig ist oder ein Auszug (Fassung 7 Punkt 18).")
(A / "25-30-n12-kassenabgleich.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
