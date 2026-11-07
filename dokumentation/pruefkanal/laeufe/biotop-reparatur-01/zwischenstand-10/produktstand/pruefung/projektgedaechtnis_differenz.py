"""Punkt 7: Projektgedächtnis-Differenz an den drei strittigen Fällen entscheiden (Nachlauf Phase 3).

Im Phase-3-Bericht standen zwei Zahlen nebeneinander: Das Biotop meldete 0 durchgerutschte Wiederholungen,
meine Nachrechnung fand 2 von 187 (gegen Lauf 13) und 1 von 44 (gegen Lauf 16). Die Differenz kam aus zwei
Ableitungen der berührten Funktionen:

  A) Hunk-Köpfe (meine Nachrechnung): Funktionsnamen aus `@@ … def name` — grob, findet auch Funktionen,
     die nur im Kontext stehen, ohne verändert zu sein.
  B) angewandter Diff (das Biotop): Der Diff wird angewandt, alte und neue Fassung jeder Funktion verglichen;
     nur Funktionen mit tatsächlich geändertem Körper zählen.

Hier werden BEIDE Ableitungen auf denselben Kandidatensatz angewandt und die strittigen Fälle einzeln
entschieden: Ist der Kandidat wirklich derselbe Weg wie der gescheiterte, oder nur benachbart?
Aufruf: projektgedaechtnis_differenz.py <ausgaben-dir>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj
from biotop.organe import gedaechtnis as G
from biotop.kern import diffwerk

A = Path(sys.argv[1])
con = verbinden()
z = ["# Projektgedächtnis: die drei strittigen Fälle, beide Ableitungen auf denselben Kandidatensatz",
     "# A = Hunk-Köpfe (Nachrechnung Hermes) · B = angewandter Diff (Biotop)", ""]

STRITTIG = [(2032, 952, 13, "lagerhaus-p3-20"), (2035, 882, 13, "lagerhaus-p3-20"), (2056, 1344, 16, "lagerhaus-p3-20")]


def ziele(werk_pfad, diff, angewandt):
    """Beide Ableitungen: (A ohne dateien_neu, B mit angewandtem Diff)."""
    a = G.aenderungsziel(werk_pfad, diff, None)
    neu = None
    if angewandt:
        try:
            neu = {}
            for d in diffwerk.parsen(diff):
                datei = werk_pfad / d.pfad
                alt = datei.read_text() if datei.exists() else None
                neu[d.pfad] = diffwerk.anwenden(alt, d)
        except Exception:
            neu = None
    b = G.aenderungsziel(werk_pfad, diff, neu) if neu else (a[0], [], a[2])
    return a, b, neu is not None


for kid, weg_kid, weg_lauf, werkname in STRITTIG:
    k = con.execute("SELECT id, lauf_id, generation, bereich, nische, status, diff, substr(grund,1,120) g FROM kandidaten WHERE id=?", (kid,)).fetchone()
    w = con.execute("SELECT kandidat_id, lauf_id, generation, bereich, dateien, funktionen, ansatz, substr(grund,1,120) g"
                    " FROM projektgedaechtnis WHERE kandidat_id=?", (weg_kid,)).fetchone()
    z.append(f"## K{kid} (Lauf {k['lauf_id']} Gen {k['generation']}, {k['bereich']}/{k['nische']}, Status {k['status']})")
    if not w:
        z.append(f"  gescheiterter Weg K{weg_kid} nicht mehr im Projektgedächtnis — Fall entfällt\n")
        continue
    pfad = Path(con.execute("SELECT pfad FROM werke WHERE name=?", (werkname,)).fetchone()[0])
    a, b, anwendbar = ziele(pfad, k["diff"], True)
    wf = set(lj(w["funktionen"]) or [])
    z.append(f"  gescheiterter Weg: K{weg_kid} (Lauf {weg_lauf} Gen {w['generation']}), Funktionen {sorted(wf)}")
    z.append(f"  A) Hunk-Köpfe:      Funktionen {a[1]}  → gemeinsam mit dem Weg: {sorted(wf & set(a[1]))}")
    z.append(f"  B) angewandter Diff: Funktionen {b[1]}  → gemeinsam mit dem Weg: {sorted(wf & set(b[1]))}"
             + ("" if anwendbar else "   (Diff ließ sich nicht anwenden — B leer)"))
    aehnlich = G._jaccard(a[2], lj(w["ansatz"]) or [])
    z.append(f"  Ansatz-Ähnlichkeit (beide Ableitungen gleich): {aehnlich:.2f} (Schwelle {G.SCHWELLE_WIEDERHOLUNG})")
    treffer_a = bool(wf & set(a[1])) and aehnlich >= G.SCHWELLE_WIEDERHOLUNG
    treffer_b = bool(wf & set(b[1])) and aehnlich >= G.SCHWELLE_WIEDERHOLUNG
    z.append(f"  → A wertet als Wiederholung: {treffer_a} | B wertet als Wiederholung: {treffer_b}")
    z.append(f"  Grund der Ablehnung im Lauf: {k['g']}")
    z.append(f"  damaliger Grund des Wegs:    {w['g']}")
    z.append("")

(A / "25-projektgedaechtnis-differenz.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
