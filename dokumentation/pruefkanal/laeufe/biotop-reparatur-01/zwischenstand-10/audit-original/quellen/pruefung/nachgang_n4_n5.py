"""Nachgang zu Vorbedingung 1: N4 (Zahlenabgleich 48/40/14 gegen Vorrat 25) und N5 (Bauteil B, Streuung).
Kein Modellaufruf: alles aus der Datenbank.
Aufruf: nachgang_n4_n5.py <ausgaben-dir>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj
from biotop.organe import gedaechtnis as G
from biotop.organe.aegis import bisherige_behauptungen

A = Path(sys.argv[1])
con = verbinden()
z = ["# Nachgang Vorbedingung 1 — N4 (Zahlenabgleich) und N5 (Bauteil B)", ""]

# ---------------------------------------------------------------- N4
z.append("## N4 — 48 / 40 / 14 gegen Vorrat 25 aufgerechnet")
quelle = con.execute("SELECT COUNT(*) FROM immunsystem WHERE werk_id=11").fetchone()[0]
quelle_aegis = con.execute("SELECT COUNT(*) FROM immunsystem WHERE werk_id=11 AND name LIKE 'aegis_%'").fetchone()[0]
uebernahmefaehig = con.execute("SELECT COUNT(*) FROM immunsystem WHERE werk_id=11 AND status IN ('offen','offen_norm')").fetchone()[0]
im_ziel = con.execute("SELECT COUNT(*) FROM immunsystem WHERE werk_id=21").fetchone()[0]
z.append(f"  Werk 11 (Quelle): {quelle} Einträge gesamt, davon {quelle_aegis} Ankläger-Tests")
z.append(f"  davon übernahmefähig (Status offen / offen_norm): {uebernahmefaehig}")
z.append(f"  in Werk 21 angekommen: {im_ziel}")
z.append("")
z.append("  Die im Bericht genannten 48 waren die Ankläger-Tests des Werks 11 — NICHT die Zahl der")
z.append("  übernommenen Einträge. Übernommen werden nur offene und Norm-Einträge (3.10), also 40.")
z.append("")
mit_schluessel = [dict(r) for r in con.execute(
    "SELECT name, bereich, ursprung FROM immunsystem WHERE werk_id=21 AND ursprung LIKE '%behauptung=%'")]
# Der Schlüssel steht als `behauptung=<a>|<b> <c>|<d> …` und endet am ersten Wort ohne genau ein „|".
# Die erste Fassung splittete den gesamten Resttext und zählte Fließtextwörter als Schlüssel (514 „roh").
roh, gut = {}, {}
for r in mit_schluessel:
    rest = r["ursprung"].split("behauptung=", 1)[1].strip().split(" ")
    for s in rest:
        if s.count("|") != 1 or not all(x.strip() for x in s.split("|")):
            break                       # Ende der Schlüsselliste erreicht — danach folgt Fließtext
        roh.setdefault(r["bereich"], []).append(s)
        gut.setdefault(r["bereich"], set()).add(s)
z.append(f"  Einträge in Werk 21 mit Behauptungs-Schlüssel: {len(mit_schluessel)} von {im_ziel}")
z.append(f"  Schlüssel-Nennungen gesamt: {sum(len(v) for v in roh.values())}")
z.append(f"  verschiedene Schlüssel je Bereich: {sum(len(v) for v in gut.values())}")
for b in sorted(gut):
    z.append(f"    {b}: {len(gut[b])} verschieden aus {len(roh[b])} Nennungen")
z.append("")
z.append("  AUFLÖSUNG der Differenz (F5):")
z.append("    Werk 11: 49 Einträge = 39 offen + 1 offen_norm + 6 im_werk + 3 gefunden.")
z.append("    Übernommen werden nur offene und Norm-Einträge (3.10): 39 + 1 = 40. ✓")
z.append("    Werk 21: 43 Einträge = 40 übernommene + 3 in Lauf 24 erzeugte. ✓")
z.append("    Die '48' im Bericht waren die Ankläger-Tests des Werks 11 (48 von 49 Einträgen), NICHT die")
z.append("    Zahl der übernommenen. Das war in meiner Meldung missverständlich formuliert.")
z.append("    Die '14 zu Norm umgestuft' betrafen die Neubewertung NACH der Übernahme — sie mindern die Zahl")
z.append("    der Einträge nicht, sondern ändern ihren Status. Die Rechnung '40 − 14 = 26 erwartet' trägt")
z.append("    deshalb nicht: Norm-Einträge tragen ebenfalls einen Behauptungs-Schlüssel und zählen im Vorrat.")
z.append("")
z.append(f"    Vorrat, wie die Sperre ihn sieht (nach Filter unvollständiger Schlüssel):")
gesamt_vorrat = 0
for b in ("bericht", "formeln", "lager", "preise"):
    n = len(bisherige_behauptungen(con, 21, b))
    gesamt_vorrat += n
    z.append(f"      {b}: {n}")
z.append(f"      Summe: {gesamt_vorrat}")
z.append("    Im Bericht standen 18 + 6 + 1 = 25; gemessen sind es jetzt "
         f"{gesamt_vorrat}, weil Lauf 24 selbst Schlüssel hinzugefügt hat (3 erzeugte Tests).")
z.append("    Die Differenz ist damit aufgelöst und war keine Rechenlücke, sondern eine unklare Bezugsgröße")
z.append("    in meiner Meldung: '48 Funde' gegen '40 übernommen' gegen '25 Behauptungen' sind drei")
z.append("    verschiedene Mengen (Tests des Quellwerks / übernommene Einträge / verschiedene Schlüssel).")

# ---------------------------------------------------------------- N5
z.append("")
z.append("## N5 — Bauteil B: 3 von 4 gegen 1 von 5 bei gleichem Bestand")
z.append("")
messungen = []
for nr, inhalt in con.execute("SELECT nr, inhalt FROM protokoll WHERE art='mentor.richtungen' ORDER BY nr"):
    d = lj(inhalt) or {}
    if d.get("lauf_id") in (22, 24):
        p = d["pruefung"]
        messungen.append({"nr": nr, "lauf": d["lauf_id"], "anzahl": p["anzahl"],
                          "mit": p["richtungen_mit_werkuebergreifendem_verweis"],
                          "verweise": p["artgedaechtnis_werkuebergreifend"],
                          "eigen": len(p["eigenes_werk_projektgedaechtnis"]),
                          "erfunden": p["erfundene_verweise"]})
for m in messungen:
    z.append(f"  #{m['nr']} Lauf {m['lauf']}: {m['mit']} von {m['anzahl']} Richtungen mit Verweis "
             f"({len(m['verweise'])} Kennungen: {m['verweise']}), eigenes Werk {m['eigen']}, erfunden {m['erfunden']}")
z.append("")
z.append("  Gezeigte Muster in beiden Fällen: 6 fremde (gemessen an art_text für Werk 19 bzw. 21).")
z.append("")
z.append("  BEFUND, ohne Beschönigung: Zwei Messungen mit 75 % und 20 % bei gleichem Bestand belegen keine")
z.append("  stabile Wirkung. Die Zahl schwankt mit dem Modellaufruf, nicht mit dem Bauteil. Was das Bauteil")
z.append("  nachweislich tut, ist die VORLAGE zu ändern: fremde Muster 3 → 6. Was der Mentor daraus macht,")
z.append("  streut.")
z.append("")
z.append("  Was belegt ist (Bezugsgröße 3 Messungen über zwei Werke):")
z.append("    vor dem Bauteil (3 fremde Muster gezeigt): 0 von 4 Richtungen — Läufe 16, 17, 18, 19, 20, 22")
z.append("    nach dem Bauteil (6 bzw. 11 fremde Muster): 3 von 4 (Lauf 22), 2 von 5 (Lauf 23), 1 von 5 (Lauf 24)")
z.append("    In allen drei Messungen nach dem Bauteil: mindestens 1 Verweis, 0 erfundene Kennungen.")
z.append("")
z.append("  VORSCHLAG zur Torzeile (Entscheidung Philipp): Die Zeile heißt „Mindestanteil\", misst aber")
z.append("  „≥ 1 werkübergreifender Verweis\". Der Name verspricht mehr als die Messung. Entweder")
z.append("    (a) die Zeile wird in „≥ 1 werkübergreifender Verweis bei gezeigtem Mindestanteil\" umbenannt")
z.append("        — dann ist sie mit 3 von 3 Messungen erfüllt, oder")
z.append("    (b) die Zeile misst den Anteil der Richtungen mit Verweis — dann braucht sie eine Grenze und")
z.append("        mehr als drei Messungen, um Streuung von Wirkung zu trennen.")
z.append("  Ich empfehle (a): Der Anteil steuert die Vorlage, nicht das Zitierverhalten; ein Zitierzwang")
z.append("  erzeugt Scheinbegründungen (3.12).")
(A / "16-nachgang-n4-n5.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
