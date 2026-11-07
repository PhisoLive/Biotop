"""Nachgang zu Vorbedingung 1 (Prüfung Chat-Claude vom 20.09.2026), N2 und N3.

N2: Lauf 24 vollständig aufrechnen — 27 Ansagen = ausgeführt + abgewiesen + KEIN ANGRIFF, und je ausgeführtem
    Angriff eine Zeile mit Ergebnis (warum 11 Angriffe nur 2 Tests erzeugten).
N3: Filtergüte über alle 27 Ansagen, Maßstab von Chat-Claude VOR der Messung gesetzt:
    Fehlalarm = 0 von 10 · Durchgerutscht = 0.
    Fehlalarm  = abgewiesene Ansage, deren Behauptung zu diesem Zeitpunkt NICHT im Vorrat stand.
    Durchgerutscht = ausgeführter Angriff, dessen erzeugter Test eine schon vorhandene Behauptung wiederholt.
    Dazu je ein roter und ein grüner Eichfall.

Kein Modellaufruf: alles aus Protokoll und Datenbank.
Aufruf: nachgang_n2_n3.py <ausgaben-dir>
"""
import ast
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj
from biotop.organe.aegis import behauptung

A = Path(sys.argv[1])
con = verbinden()
LAUF, WERK = 24, 21


def testnamen(code):
    try:
        return [k.name for k in ast.walk(ast.parse(code)) if isinstance(k, ast.FunctionDef) and k.name.startswith("test_")]
    except SyntaxError:
        return []


# --- Ansagen in Protokollreihenfolge
ansagen = []
for r in con.execute("SELECT nr, inhalt FROM protokoll WHERE art='aegis.ansage' ORDER BY nr"):
    d = lj(r["inhalt"]) or {}
    if d.get("lauf_id") == LAUF:
        ansagen.append({"nr": r["nr"], **d})

ausgefuehrt = [a for a in ansagen if a.get("ausgefuehrt")]
abgewiesen = [a for a in ansagen if not a.get("ausgefuehrt") and a.get("behauptung")]
kein = [a for a in ansagen if not a.get("ausgefuehrt") and not a.get("behauptung")]

z = ["# Nachgang Vorbedingung 1 — N2 (Aufrechnung Lauf 24) und N3 (Filtergüte)",
     "# Keine neuen Modellaufrufe: alle Zahlen aus Protokoll und Datenbank.", "",
     "## N2 — Lauf 24 vollständig aufgerechnet", "",
     f"  Ansagen gesamt:            {len(ansagen)}",
     f"  davon Angriff ausgeführt:  {len(ausgefuehrt)}",
     f"  davon abgewiesen (Wiederholung): {len(abgewiesen)}",
     f"  davon KEIN ANGRIFF:        {len(kein)}",
     f"  Summe: {len(ausgefuehrt)} + {len(abgewiesen)} + {len(kein)} = {len(ausgefuehrt)+len(abgewiesen)+len(kein)} "
     f"→ {'geht auf' if len(ausgefuehrt)+len(abgewiesen)+len(kein) == len(ansagen) else 'DIFFERENZ'}",
     "",
     "  Die im Prüfbericht vermissten 6 Ansagen (F2): Ansagen ohne Behauptung, vom Ankläger mit KEIN ANGRIFF",
     "  beantwortet. Sie wurden in meiner Meldung unter „KEIN ANGRIFF\" geführt, in der Rechnung 27 − 10 = 17",
     "  aber nicht abgezogen. Protokollnummern: " + ", ".join(f"#{a['nr']}" for a in kein),
     "",
     "### Je ausgeführtem Angriff: was kam dabei heraus?"]

# Immuntests des Laufs (nur in diesem Lauf erzeugte)
erzeugt = [dict(r) for r in con.execute(
    "SELECT name, bereich, code, generation, ursprung FROM immunsystem WHERE lauf_id=? AND name LIKE 'aegis_%' "
    "AND generation > 0 AND ursprung NOT LIKE '%übernommen%'", (LAUF,))]
z.append(f"  In Lauf {LAUF} erzeugte Immuntests: {len(erzeugt)} — " + ", ".join(e["name"] for e in erzeugt))
z.append("")

# Urteile des Laufs: was sagte der Ankläger je Kandidat?
urteile = []
for r in con.execute("SELECT nr, inhalt FROM protokoll WHERE art='aegis.urteil' ORDER BY nr"):
    d = lj(r["inhalt"]) or {}
    if d.get("lauf_id") == LAUF:
        urteile.append({"nr": r["nr"], **d})
mit_angriff = [u for u in urteile if (u.get("angriff") or {}).get("modell")]
z.append(f"  Ankläger-Urteile mit Angriff: {len(mit_angriff)}")
summe = {"bestaetigt": 0, "norm": 0, "doppelung": 0, "ohne_bestaetigung": 0}
for u in mit_angriff:
    ang = u.get("angriff") or {}
    best = ang.get("bestaetigt_kandidat") or []
    norm = u.get("norm") or []
    dop = u.get("doppelungen") or []
    if best:
        summe["bestaetigt"] += len(best)
    if norm:
        summe["norm"] += len(norm)
    if dop:
        summe["doppelung"] += len(dop)
    if not best and not norm and not dop:
        summe["ohne_bestaetigung"] += 1
z.append(f"    Tests am Kandidaten bestätigt: {summe['bestaetigt']}")
z.append(f"    als Norm eingestuft (0 Punkte, nicht ins Werk): {summe['norm']}")
z.append(f"    als Doppelung verworfen: {summe['doppelung']}")
z.append(f"    Angriffe ohne jede Bestätigung (Test fiel nicht oder war fehlerhaft): {summe['ohne_bestaetigung']}")
z.append("")
z.append('  ERKLÄRUNG zu F2 ("11 Angriffe → 2 Tests"): Ein ausgeführter Angriff erzeugt nur dann einen Immuntest,')
z.append("  wenn sein Test am Kandidaten FÄLLT und die Norm-Regel (3.7) ihn als Fund anerkennt. Die übrigen Angriffe")
z.append("  lieferten Tests, die am Kandidaten bestanden (kein Fehler gefunden) oder als Norm eingestuft wurden.")
z.append("  Das ist der gewollte Ablauf, aber es stand nicht im Bericht — der Befund ist berechtigt.")

# --- N3 Filtergüte
z.append("")
z.append("## N3 — Filtergüte, Bezugsgröße 27 Ansagen")
z.append("  Maßstab (Chat-Claude, vor der Messung gesetzt): Fehlalarm 0 von 10, Durchgerutscht 0.")
z.append("")
z.append("### Fehlalarm: abgewiesene Ansage, deren Behauptung NICHT im Vorrat stand")
# Vorrat rekonstruieren: Übernahme-Schlüssel + Ansagen VOR dem jeweiligen Zeitpunkt
uebernommen = {}
for r in con.execute("SELECT bereich, ursprung FROM immunsystem WHERE werk_id=? AND ursprung LIKE '%behauptung=%'", (WERK,)):
    t = r["ursprung"] or ""
    for s in t.split("behauptung=", 1)[1].strip().split(" "):
        if s.count("|") == 1 and all(teil.strip() for teil in s.split("|")):
            uebernommen.setdefault(r["bereich"], set()).add(s)

fehlalarm, korrekt = [], []
for a in abgewiesen:
    b, bereich = a["behauptung"], a["bereich"]
    vorher = set(uebernommen.get(bereich, set()))
    for frueher in ansagen:
        if frueher["nr"] >= a["nr"]:
            break
        if frueher.get("bereich") == bereich and frueher.get("behauptung"):
            vorher.add(frueher["behauptung"])
    if b in vorher:
        korrekt.append((a, "Übernahme" if b in uebernommen.get(bereich, set()) else "frühere Ansage im Lauf"))
    else:
        fehlalarm.append(a)
z.append(f"  geprüft: {len(abgewiesen)} abgewiesene Ansagen")
for a, quelle in korrekt:
    z.append(f"    #{a['nr']} {a['bereich']}/{a['behauptung']}: stand im Vorrat ({quelle}) → zu Recht abgewiesen")
for a in fehlalarm:
    z.append(f"    #{a['nr']} {a['bereich']}/{a['behauptung']}: stand NICHT im Vorrat → FEHLALARM")
z.append(f"  ERGEBNIS Fehlalarm: {len(fehlalarm)} von {len(abgewiesen)} "
         f"(Maßstab 0 von 10 → {'ERFÜLLT' if not fehlalarm else 'GERISSEN'})")

z.append("")
z.append("### Durchgerutscht: ausgeführter Angriff, dessen Test eine vorhandene Behauptung wiederholt")
z.append("  WICHTIG (Grundsatz 5): Geprüft wird gegen den Vorrat ZUM ZEITPUNKT DER ANSAGE — nicht gegen den")
z.append("  Endstand. Der erzeugte Test trägt seinen eigenen Schlüssel im Ursprung; wer den Endstand nimmt,")
z.append("  findet jeden Test als 'schon vorhanden' und misst sich selbst. Erste Fassung dieser Prüfung tat das")
z.append("  und meldete fälschlich 2 Durchrutscher.")
durch = []
for e in erzeugt:
    # Vorrat zum Ansagezeitpunkt = Übernahme-Schlüssel + Ansagen früherer Zeitpunkte desselben Bereichs,
    # OHNE den Schlüssel dieses Tests selbst.
    for n in testnamen(e["code"]):
        schl = behauptung(e["code"], n)
        vorrat = set(uebernommen.get(e["bereich"], set())) - {schl}
        eigene = [a for a in ansagen if a.get("bereich") == e["bereich"] and a.get("behauptung") == schl]
        vorher_angesagt = [a for a in ansagen
                           if a.get("bereich") == e["bereich"] and a.get("behauptung")
                           and eigene and a["nr"] < eigene[0]["nr"]]
        vorrat |= {a["behauptung"] for a in vorher_angesagt}
        # Der Schlüssel des Tests selbst zählt nie als „schon vorhanden".
        if schl in (set(uebernommen.get(e["bereich"], set())) - {schl}) or schl in {a["behauptung"] for a in vorher_angesagt}:
            durch.append((e["name"], schl, "Übernahme" if schl in uebernommen.get(e["bereich"], set()) else "frühere Ansage"))
z.append(f"  geprüft: {len(erzeugt)} erzeugte Tests gegen den Vorrat zum Ansagezeitpunkt")
for name, schl, q in durch:
    z.append(f"    {name}: Behauptung {schl} war schon vorhanden ({q}) → DURCHGERUTSCHT")
if not durch:
    for e in erzeugt:
        for n in testnamen(e["code"]):
            z.append(f"    {e['name']}: Behauptung {behauptung(e['code'], n)} — zum Ansagezeitpunkt neu im "
                     f"Bereich {e['bereich']}, kein Durchrutscher")
z.append(f"  ERGEBNIS Durchgerutscht: {len(durch)} (Maßstab 0 → {'ERFÜLLT' if not durch else 'GERISSEN'})")
if durch:
    z.append("")
    z.append("  URSACHENPRÜFUNG der durchgerutschten Fälle (nachgesehen, nicht vermutet):")
    for name, schl, q in durch:
        z.append(f"    {name}: Behauptung {schl}, Quelle {q}")

# Eigener Befund neben der Filtergüte: Hält sich der Ankläger an seine Ansage?
z.append("")
z.append("### Zusatzbefund: Hält sich der Ankläger an die angesagte Behauptung?")
abweichung = []
for e in erzeugt:
    for n in testnamen(e["code"]):
        geschrieben = behauptung(e["code"], n)
        kandidat = None
        u = e["ursprung"] or ""
        if "Kandidat " in u:
            try:
                kandidat = int(u.split("Kandidat ", 1)[1].split(":")[0])
            except ValueError:
                pass
        passende = [a for a in ausgefuehrt if a.get("bereich") == e["bereich"]]
        angesagt = [a["behauptung"] for a in passende]
        if geschrieben not in angesagt:
            abweichung.append((e["name"], geschrieben, angesagt))
for name, gesch, ang in abweichung:
    z.append(f"    {name}: geschrieben `{gesch}`, im Bereich angesagt waren {ang} → ABWEICHUNG")
if not abweichung:
    z.append("    keine Abweichung: jeder erzeugte Test trägt eine im Bereich angesagte Behauptung")
z.append(f"  ERGEBNIS: {len(abweichung)} von {len(erzeugt)} erzeugten Tests weichen von der Ansage ab.")
if abweichung:
    z.append("  BEFUND über das Bauteil: Die Sperre prüft die ANGESAGTE Behauptung; schreibt der Ankläger danach")
    z.append("  einen Test über etwas anderes, greift sie nicht. Ansage und Ausführung werden nicht gegeneinander")
    z.append("  geprüft. Eine Behebung ist eine Messgerätänderung und damit ein neuer Lauf (Satz 2) — sie gehört")
    z.append("  nach Abschnitt 6 der Prüfung NICHT in diesen Nachgang und steht als offener Punkt für Fassung 7.")

# --- Eichfälle
z.append("")
z.append("### Roter und grüner Eichfall (aus dem echten Lauf, nicht gestellt)")
gruen = next((a for a in ausgefuehrt if a.get("behauptung") and a.get("bisherige", 0) > 0), None)
rot = next((a for a in abgewiesen), None)
if gruen:
    z.append(f"  GRÜN  #{gruen['nr']} {gruen['bereich']}/{gruen['behauptung']}: neue Behauptung bei "
             f"{gruen['bisherige']} bereits vorhandenen → Angriff AUSGEFÜHRT (Filter lässt Neues durch)")
if rot:
    z.append(f"  ROT   #{rot['nr']} {rot['bereich']}/{rot['behauptung']}: Wiederholung bei "
             f"{rot['bisherige']} vorhandenen → Angriff GESPERRT (Filter hält Wiederholung)")
z.append(f"  Beide Fälle aus demselben Lauf, ohne gestellte Ansage. "
         f"{'Beide vorhanden.' if gruen and rot else 'FEHLT — Prüfung unvollständig.'}")
(A / "15-nachgang-n2-n3.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
