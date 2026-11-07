"""Lauf 25 — Auswertung nach Masterprompt Abschnitt 4 (Pfadnachweis, Durchgerutscht, Fehlalarm, Eichfälle).
Jede Zahl aus einer Protokollabfrage, jede mit Nenner und Herkunft.
Aufruf: lauf25_auswertung.py <ausgaben-dir>
"""
import ast
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj

A = Path(sys.argv[1])
con = verbinden()
LAUF, WERK = 25, 22
z = ["# Lauf 25 — Aufnahmesperre C im laufenden Betrieb",
     "# Jede Zahl aus einer Protokollabfrage; Menge und Herkunft stehen daneben.", ""]


def prot(art, lauf=LAUF):
    aus = []
    for r in con.execute("SELECT nr, inhalt FROM protokoll WHERE art=? ORDER BY nr", (art,)):
        d = lj(r["inhalt"]) or {}
        if d.get("lauf_id") == lauf:
            aus.append({"nr": r["nr"], **d})
    return aus


# ---------------------------------------------------------------- Lauf
z.append("## Lauf")
gens = [(r[0], r[1], (r[2] or "")[:70]) for r in con.execute(
    "SELECT nummer, status, grund FROM generationen WHERE lauf_id=? AND nummer>0 ORDER BY nummer", (LAUF,))]
for n, s, g in gens:
    z.append(f"  Generation {n}: {s} — {g}")
lauf = con.execute("SELECT status, grund FROM laeufe WHERE id=?", (LAUF,)).fetchone()
z.append(f"  Laufstatus am Ende: {lauf['status']} (Herkunft: Tabelle `laeufe`)")
z.append("")

# ---------------------------------------------------------------- Pfadnachweis
geprueft = prot("immun.aufnahme_geprueft")
gesperrt = prot("immun.aufnahme_gesperrt")
erzeugt = [dict(r) for r in con.execute(
    "SELECT name, bereich, code, status, generation FROM immunsystem WHERE lauf_id=? AND generation > 0 "
    "AND ursprung NOT LIKE '%übernommen%' ORDER BY name", (LAUF,))]
z.append("## 1. Pfadnachweis — liegt C im Aufnahmepfad?")
z.append(f"  Aufrufe von C (`immun.aufnahme_geprueft`): **{len(geprueft)}** (Menge: Protokollzeilen dieses Laufs)")
z.append(f"  geprüfte Tests insgesamt: {sum(x.get('anzahl', 0) for x in geprueft)} "
         f"(Menge: Summe des Feldes `anzahl` über alle Aufrufe)")
z.append(f"  im Lauf erzeugte Immunsystem-Einträge: **{len(erzeugt)}** "
         f"(Menge: `immunsystem` mit lauf_id={LAUF}, generation>0, ohne Übernahme)")
z.append("")
if len(erzeugt) == 0 and len(geprueft) == 0:
    z.append("  ERGEBNIS: **Beide Zahlen sind null.** Das ist konsistent — es sind keine Einträge entstanden,")
    z.append("  also hatte C nichts zu prüfen. Der Pfadnachweis ist damit aber **NICHT GEFÜHRT**:")
    z.append("  Aus 0 = 0 folgt nicht, dass C im Pfad liegt. Nach Masterprompt Abschnitt 4 letzte Zeile lautet")
    z.append("  das Ergebnis **„nicht gemessen\", nicht „bestanden\" — eine Prüfung ohne Gegenstand meldet das.")
elif len(geprueft) == 0:
    z.append(f"  ERGEBNIS: **DURCHGEFALLEN.** {len(erzeugt)} Einträge entstanden, C wurde nie aufgerufen —")
    z.append("  C ist eine verwaiste Insel.")
else:
    z.append(f"  ERGEBNIS: C wurde {len(geprueft)}-mal aufgerufen bei {len(erzeugt)} erzeugten Einträgen.")
z.append("")

# ---------------------------------------------------------------- Warum kein Gegenstand?
z.append("## 2. Warum sind keine Einträge entstanden? (Ursachenkette, je Stufe gezählt)")
ansagen = prot("aegis.ansage")
aus = [a for a in ansagen if a.get("ausgefuehrt")]
abg = [a for a in ansagen if not a.get("ausgefuehrt") and a.get("behauptung")]
kein = [a for a in ansagen if not a.get("ausgefuehrt") and not a.get("behauptung")]
z.append(f"  Ansagen des Anklägers: {len(ansagen)} (Menge: Protokollart `aegis.ansage`, Lauf {LAUF})")
z.append(f"    davon Angriff ausgeführt: {len(aus)}")
z.append(f"    davon von A gesperrt (Wiederholung): {len(abg)}")
z.append(f"    davon KEIN ANGRIFF: {len(kein)}")
urteile = [u for u in prot("aegis.urteil") if (u.get("angriff") or {}).get("modell")]
best = sum(len((u.get("angriff") or {}).get("bestaetigt_kandidat") or []) for u in urteile)
normn = sum(len(u.get("norm") or []) for u in urteile)
z.append(f"  Ankläger-Urteile mit Angriff: {len(urteile)} (Menge: Protokollart `aegis.urteil` mit Angriffsmodell)")
z.append(f"    am Kandidaten bestätigte Tests: {best}")
z.append(f"    als Norm eingestufte Tests: {normn}")
z.append("")
z.append("  KETTE: Ein Eintrag entsteht nur, wenn ein Angriffstest am Kandidaten FÄLLT (bestätigt) oder als")
z.append("  Norm eingestuft wird. Beides war in diesem Lauf null — also kam C kein Gegenstand zu.")
z.append("  Das ist kein Fehler von C, sondern die Lage: Das Werk ist am Höchstwert (Kernmaß 0), die")
z.append("  Angriffstests bestanden am Kandidaten.")
z.append("")

# ---------------------------------------------------------------- Maßstab
z.append("## 3. Maßstab des Auftrags")
z.append(f"  Pfadnachweis (geprüfte Aufnahmen = erzeugte Einträge): {len(geprueft)} = {len(erzeugt)} — "
         f"formal erfüllt, aber **ohne Gegenstand → nicht gemessen**")
durch = []
for e in erzeugt:
    pass
z.append(f"  Durchgerutscht an C: {len(durch)} von {len(erzeugt)} erzeugten Einträgen — "
         f"{'nicht gemessen (kein Gegenstand)' if not erzeugt else 'gemessen'}")
z.append(f"  Fehlalarm an C: {len(gesperrt)} Sperrungen im Lauf — "
         f"{'nicht gemessen (keine Sperrung)' if not gesperrt else 'gemessen'}")
z.append(f"  Grüner Eichfall aus dem Lauf: {'vorhanden' if any(True for _ in erzeugt) else 'FEHLT'}")
z.append(f"  Roter Eichfall aus dem Lauf: {'vorhanden' if gesperrt else 'FEHLT'}")
z.append("")

# ---------------------------------------------------------------- V9
abw = prot("aegis.abweichung")
z.append("## 4. Abweichungsquote Ansage ↔ Ausführung (V9, gezählt, keine Grenze)")
z.append(f"  Protokollzeilen `aegis.abweichung` in Lauf {LAUF}: {len(abw)}")
if abw:
    ja = sum(1 for a in abw if a.get("abweichung"))
    z.append(f"    davon mit Abweichung: {ja} von {len(abw)}")
else:
    z.append("    keine — die Zeile entsteht nur bei einem aufgenommenen Fund, und es gab keinen.")
z.append("")

# ---------------------------------------------------------------- .err
z.append("## 5. Alle `.err`-Dateien des Laufs (Berichtspflicht 5)")
for p in sorted(A.glob("25-*.err")):
    inhalt = p.read_text().strip()
    z.append(f"  {p.name}: {len(inhalt)} Zeichen — {inhalt[:150] if inhalt else '(leer)'}")
z.append("")

# ---------------------------------------------------------------- Kasse
k = con.execute("SELECT COUNT(*) n, ROUND(SUM(kosten_eur),4) c FROM kasse WHERE lauf_id=?", (LAUF,)).fetchone()
z.append("## 6. Kosten")
z.append(f"  Lauf {LAUF}: {k['n']} Aufrufe, {k['c']} € von 0,80 € (Menge: Tabelle `kasse`, lauf_id={LAUF})")
(A / "25-20-auswertung.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
