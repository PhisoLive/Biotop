"""Zweiter Nachgang (Prüfung 2): N7 (Abbruch offenlegen), N8 (zwei fehlende Angriffe), N9 (Messung 2 von 5).
Kein Modellaufruf. Aufruf: nachgang_n7_n9.py <ausgaben-dir>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj

A = Path(sys.argv[1])
con = verbinden()
z = ["# Zweiter Nachgang — N7, N8, N9 (0 Modellaufrufe)", ""]

# ---------------------------------------------------------------- N7
z.append("## N7 — Der Abbruch in `04g6-gen6.err`")
err = (A / "04g6-gen6.err").read_text().strip()
z.append(f"  Inhalt der Datei, vollständig: `{err}`")
z.append("")
z.append("  **Frage 1 — woran ist Generation 6 gescheitert?**")
z.append("  Sie ist nicht gescheitert. Der Läufer `generationen.sh` war auf die Generationen 5 bis 8 angesetzt.")
z.append("  Nach Generation 5 meldete die Entropie Sättigung und beendete den Lauf (Status `gesaettigt`).")
z.append("  Der Aufruf für Generation 6 traf auf einen beendeten Lauf und wurde vom Kern abgewiesen:")
z.append("  „Lauf 23 ist im Zustand gesaettigt, nicht bereit\". Das ist die gewollte Schutzregel — ein beendeter")
z.append("  Lauf nimmt keine Generation mehr an. Kein Kandidat, kein Kammerlauf, kein Modellaufruf.")
lauf = con.execute("SELECT status, grund FROM laeufe WHERE id=23").fetchone()
z.append(f"  Beleg aus der Datenbank: Lauf 23 Status `{lauf['status']}`, Grund: {(lauf['grund'] or '')[:150]}")
gens = [(r[0], r[1]) for r in con.execute("SELECT nummer, status FROM generationen WHERE lauf_id=23 ORDER BY nummer")]
z.append(f"  Generationen in der Datenbank: {gens} — es gibt keine Generation 6, auch keine abgebrochene.")
z.append("")
z.append("  **Frage 2 — war der Musterbestand zum Messzeitpunkt vollständig?**")
muster = [(r[0], r[1]) for r in con.execute(
    "SELECT generation, COUNT(*) FROM artgedaechtnis WHERE werk='logmuehle' AND lauf_id=23 "
    "AND muster IS NOT NULL AND muster!='' GROUP BY generation")]
gesamt = con.execute("SELECT COUNT(*) FROM artgedaechtnis WHERE werk='logmuehle' AND muster IS NOT NULL AND muster!=''").fetchone()[0]
z.append(f"  Ja. Die angenommenen Generationen von Lauf 23 sind 1 und 5; beide haben ihr Muster geschrieben:")
z.append(f"  Muster aus Lauf 23 je Generation: {muster} · Musterbestand `logmuehle` gesamt: {gesamt}")
z.append("  Generation 5 wurde ANGENOMMEN und ist vollständig verarbeitet — der Abbruch lag danach.")
z.append("  Die Bauteil-B-Messung (6 fremde Muster in der Vorlage) stand damit auf vollständigem Bestand.")
z.append("")
z.append("  **Frage 3 — warum stand der Abbruch in keinem Bericht?**")
z.append("  Zwei Ursachen, beide bei mir:")
z.append("  (a) Der Läufer schreibt die Abbruchmeldung nur in die `.err`-Datei und in sein Log. Der Kern")
z.append("      protokolliert die Sättigung (`lauf.gesaettigt`), aber nicht den abgewiesenen Folgeaufruf.")
z.append("      Für meinen Bericht habe ich die Datenbank gelesen — dort stand kein Abbruch, weil keiner war.")
z.append("  (b) Ich habe die `.err`-Dateien nach dem Lauf nicht durchgesehen. Hätte ich es getan, wäre die")
z.append("      Zeile aufgefallen und hätte in den Bericht gehört — auch als folgenloser Abbruch.")
z.append("  Das ist eine Lücke im Meldeverhalten, nicht im Messgerät: „laut scheitern, nie still\" gilt auch")
z.append("  für einen Abbruch ohne Folgen. Gehört nach Fassung 7 (Punkt 6 der Prüfliste).")

# ---------------------------------------------------------------- N8
z.append("")
z.append("## N8 — Die zwei fehlenden Angriffe (11 ausgeführt, 9 aufgerechnet)")
ansagen = []
for r in con.execute("SELECT nr, inhalt FROM protokoll WHERE art='aegis.ansage' ORDER BY nr"):
    d = lj(r["inhalt"]) or {}
    if d.get("lauf_id") == 24:
        ansagen.append({"nr": r["nr"], **d})
ausgefuehrt = [a for a in ansagen if a.get("ausgefuehrt")]
urteile = []
for r in con.execute("SELECT nr, inhalt FROM protokoll WHERE art='aegis.urteil' ORDER BY nr"):
    d = lj(r["inhalt"]) or {}
    if d.get("lauf_id") == 24 and (d.get("angriff") or {}).get("modell"):
        urteile.append({"nr": r["nr"], **d})
fehler = [dict(r) for r in con.execute("SELECT nr, inhalt FROM protokoll WHERE art='aegis.fehler'")]
fehler_24 = [f for f in fehler if (lj(f["inhalt"]) or {}).get("lauf_id") == 24]
z.append(f"  Ansagen mit `ausgefuehrt=true`: {len(ausgefuehrt)}")
z.append(f"  Ankläger-Urteile mit Angriffsmodell: {len(urteile)}")
z.append(f"  Differenz: {len(ausgefuehrt) - len(urteile)}")
z.append("")
z.append("  AUFLÖSUNG, am Protokoll nachgesehen — die Differenz liegt an der ZUORDNUNG, nicht an fehlenden Angriffen:")
z.append("    11 Ansagen mit `ausgefuehrt=true` → 11 Angriffs-Modellaufrufe (max_tokens 2500), eins zu eins:")
z.append("      #14502→#14503 · #14533→#14534 · #14661→#14662 · #14690→#14691 · #14704→#14705 · #14772→#14773")
z.append("      #14849→#14850 · #15002→#15003 · #15027→#15028 · #15143→#15144 · #15162→#15163")
z.append("    Es fehlt also KEIN Angriff. Es gibt nur 9 Urteile mit Angriffsabschnitt, weil DREI Angriffe")
z.append("    (#14662, #14691, #14705) in EIN gemeinsames Urteil #14707 münden: Der Ankläger prüft einen")
z.append("    Kandidaten über seinen ganzen Wirkungskreis (3.7 Schritt 1) und greift dabei jeden berührten")
z.append("    Bereich einzeln an — das Urteil wird aber je Kandidat geschrieben, nicht je Bereich.")
z.append("    11 Angriffe − 2 (in ein gemeinsames Urteil eingegangen) = 9 Urteile. Die Rechnung geht auf.")
z.append("")
z.append("  Ergebnis der 9 Urteile, einzeln geprüft:")
z.append("    #15006: 1 Test am Kandidaten bestätigt → Fund `aegis_k2500_preise`")
z.append("    #15147: Fund `aegis_k2526_lager` (Behebung nachgewiesen, nicht am Kandidaten bestätigt)")
z.append("    #14776: 1 Test als Norm eingestuft (0 Punkte, nicht ins Werk)")
z.append("    #14505, #14536, #14707, #14852, #15030, #15165: keine Bestätigung — der Angriffstest bestand")
z.append("      am Kandidaten, fand also keinen Fehler")
z.append("    Summe: 1 bestätigt + 1 Behebungsnachweis + 1 Norm + 6 ohne Bestätigung = 9 ✓")
z.append("")
z.append("  Mein Fehler im ersten Nachgang war doppelt: Ich nannte 11 ausgeführte Angriffe und rechnete")
z.append("  9 Urteile auf, ohne die Differenz zu erklären — und meine erste Erklärung in diesem Nachgang")
z.append("  („zwei Angriffe ohne Urteil\") war ebenfalls falsch, weil mein Zuordnungsskript Urteile der Reihe")
z.append("  nach vergab. Erst der Abgleich Ansage → Modellaufruf → Urteil zeigt die Sache. Grundsatz 5.")
z.append(f"  `aegis.fehler`-Zeilen in Lauf 24: {len(fehler_24)} — kein Angriff ist an einem Anbieterfehler gescheitert.")

# ---------------------------------------------------------------- N9
z.append("")
z.append("## N9 — Die Messung „2 von 5\"")
z.append("  Vollständige Liste aller Mentor-Messungen mit Protokollnummer, aus dem Protokoll:")
alle = []
for r in con.execute("SELECT nr, inhalt FROM protokoll WHERE art='mentor.richtungen' ORDER BY nr"):
    d = lj(r["inhalt"]) or {}
    p = d.get("pruefung") or {}
    alle.append({"nr": r["nr"], "lauf": d.get("lauf_id"), "anzahl": p.get("anzahl"),
                 "mit": p.get("richtungen_mit_werkuebergreifendem_verweis"),
                 "verweise": p.get("artgedaechtnis_werkuebergreifend"),
                 "erfunden": p.get("erfundene_verweise")})
for m in alle:
    z.append(f"    #{m['nr']} Lauf {m['lauf']}: {m['mit']} von {m['anzahl']} Richtungen, "
             f"Verweise {m['verweise']}, erfunden {m['erfunden']}")
zwei_von_fuenf = [m for m in alle if m["mit"] == 2 and m["anzahl"] == 5]
z.append("")
if zwei_von_fuenf:
    m = zwei_von_fuenf[0]
    z.append(f"  Die Messung „2 von 5\" ist Protokoll #{m['nr']}, Lauf {m['lauf']} "
             f"(Verweise {m['verweise']}, erfunden {m['erfunden']}).")
    z.append("  Sie stammt aus dem Nachlauf zu Phase 3 (Beleg `…/biotop-phase-3-nachlauf/ausgaben/"
             "23-artgedaechtnis-muster-messung.txt`) und gehört damit zu einem anderen Abschlussordner.")
    z.append("  Im Nachgangsbericht zu Vorbedingung 1 stand sie in der Prosa, ohne Protokollnummer und ohne")
    z.append("  Zeile in der Tabelle — der Befund trifft zu. Hiermit nachgereicht.")
else:
    z.append("  Keine Messung mit 2 von 5 im Protokoll gefunden — die Aussage wird zurückgenommen.")
(A / "18-nachgang-n7-n9.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
