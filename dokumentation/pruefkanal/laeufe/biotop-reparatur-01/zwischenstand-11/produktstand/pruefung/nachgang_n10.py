"""N10 (Prüfung 3): Wie viele Einträge hat Lauf 24 erzeugt, welche tragen einen Behauptungsschlüssel,
und ändert das die Filtergüte „Durchgerutscht"?

Kein Modellaufruf. Aufruf: nachgang_n10.py <ausgaben-dir>
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
z = ["# N10 — Zwei oder drei? Alle in Lauf 24 erzeugten Immunsystem-Einträge", ""]


def testnamen(code):
    try:
        return [k.name for k in ast.walk(ast.parse(code)) if isinstance(k, ast.FunctionDef) and k.name.startswith("test_")]
    except SyntaxError:
        return []


alle = [dict(r) for r in con.execute(
    "SELECT name, bereich, status, generation, code, ursprung FROM immunsystem "
    "WHERE lauf_id=? AND generation > 0 AND ursprung NOT LIKE '%übernommen%' ORDER BY name", (LAUF,))]
z.append(f"## Alle in Lauf {LAUF} erzeugten Einträge: {len(alle)}")
z.append("")
for e in alle:
    schl = "; ".join(f"{t} → {behauptung(e['code'], t)}" for t in testnamen(e["code"])) or "(kein Testname erkannt)"
    hat = "behauptung=" in (e["ursprung"] or "")
    z.append(f"  {e['name']}")
    z.append(f"    Bereich {e['bereich']} · Generation {e['generation']} · Status {e['status']}")
    z.append(f"    Schlüssel im Ursprung gespeichert: {hat}")
    z.append(f"    Behauptung aus dem Code: {schl}")
    z.append("")

aegis_e = [e for e in alle if e["name"].startswith("aegis_")]
norm_e = [e for e in alle if e["name"].startswith("norm_")]
z.append("## Antwort auf N10")
z.append(f"  Erzeugte Einträge gesamt: {len(alle)}")
z.append(f"    davon Ankläger-FUNDE (`aegis_…`): {len(aegis_e)} — {', '.join(e['name'] for e in aegis_e)}")
z.append(f"    davon NORM-Einträge (`norm_…`): {len(norm_e)} — {', '.join(e['name'] for e in norm_e)}")
z.append("")
z.append("  Die drei Einträge aus N4 und N8 sind diese drei. Sie sind NICHT drei Funde:")
z.append("    Ein `norm_…`-Eintrag entsteht aus einem Test, den die Norm-Regel (3.7) als Meinung eingestuft hat.")
z.append("    Er bringt 0 Punkte, kommt nicht ins Werk und ist kein vom Ankläger bestätigter Fehler.")
z.append("")
mit_schluessel = [e for e in alle if "behauptung=" in (e["ursprung"] or "")]
z.append(f"  Einträge mit gespeichertem Behauptungsschlüssel: {len(mit_schluessel)} von {len(alle)}")
for e in alle:
    hat = "behauptung=" in (e["ursprung"] or "")
    z.append(f"    {e['name']}: {'ja' if hat else 'NEIN'}")
z.append("")
z.append("## Folge für die Bezugsgrößen")
z.append("")
z.append("### Zeile 8 (Doppelungsanteil): Bezugsgröße bleibt 2")
z.append("  Zeile 8 misst den Anteil unter den vom ANKLÄGER ERZEUGTEN TESTS, also unter den Funden.")
z.append("  Ein Norm-Eintrag ist kein erzeugter Fund — er ist das Gegenteil: ein verworfener Test.")
z.append(f"  Erzeugte Funde in Lauf {LAUF}: {len(aegis_e)}. Die Zahl 2 in der Zeile-8-Tabelle ist richtig.")
z.append("")
z.append("### Durchgerutscht: über ALLE drei neu gemessen")
z.append("  Der Prüfer hat recht, dass die Frage gestellt werden muss: Trägt der Norm-Eintrag einen Schlüssel,")
z.append("  kann auch er eine vorhandene Behauptung wiederholen. Deshalb hier die Messung über alle drei.")
z.append("")
# Vorrat zum Ansagezeitpunkt rekonstruieren
uebernommen = {}
for r in con.execute("SELECT bereich, ursprung FROM immunsystem WHERE werk_id=? AND generation=0 AND ursprung LIKE '%behauptung=%'", (WERK,)):
    for s in r["ursprung"].split("behauptung=", 1)[1].strip().split(" "):
        if s.count("|") != 1 or not all(x.strip() for x in s.split("|")):
            break
        uebernommen.setdefault(r["bereich"], set()).add(s)
ansagen = []
for r in con.execute("SELECT nr, inhalt FROM protokoll WHERE art='aegis.ansage' ORDER BY nr"):
    d = lj(r["inhalt"]) or {}
    if d.get("lauf_id") == LAUF:
        ansagen.append({"nr": r["nr"], **d})

durch = []
for e in alle:
    for t in testnamen(e["code"]):
        schl = behauptung(e["code"], t)
        eigene = [a for a in ansagen if a.get("bereich") == e["bereich"] and a.get("behauptung") == schl]
        grenze = eigene[0]["nr"] if eigene else 10**9
        vorher = {a["behauptung"] for a in ansagen
                  if a.get("bereich") == e["bereich"] and a.get("behauptung") and a["nr"] < grenze}
        vorrat = (uebernommen.get(e["bereich"], set()) | vorher) - {schl} if not eigene else \
                 (uebernommen.get(e["bereich"], set()) | vorher)
        treffer = schl in (uebernommen.get(e["bereich"], set()) | vorher)
        z.append(f"  {e['name']} / {schl}: im Vorrat zum Ansagezeitpunkt? {'JA → DURCHGERUTSCHT' if treffer else 'nein'}")
        if treffer:
            durch.append((e["name"], schl))
z.append("")
z.append(f"  ERGEBNIS Durchgerutscht über alle {len(alle)} erzeugten Einträge: {len(durch)} "
         f"(Maßstab 0 → {'ERFÜLLT' if not durch else 'GERISSEN'})")
z.append("")
if durch:
    z.append("## Der Maßstab ist gerissen — und zwar schärfer, als die erste Messung zeigte")
    z.append("")
    z.append("  Beide durchgerutschten Behauptungen standen bereits im ÜBERNOMMENEN Vorrat:")
    z.append("    `preis_fuer|GtE:zahl` (preise) — aus der Übernahme aus Werk 11")
    z.append("    `reservierung_einloesen|raises:NichtGenugBestand` (lager) — aus der Übernahme aus Werk 11")
    z.append("  Für KEINE der beiden gab es eine Ansage in Lauf 24. Die Tests entstanden aus Angriffen, die")
    z.append("  etwas ANDERES angekündigt hatten:")
    z.append("    `aegis_k2500_preise` folgte der Ansage `aufnehmen|raises:ValueError` (#15027)")
    z.append("    `norm_k2458_lager` entstand ohne zugehörige Ansage dieser Behauptung")
    z.append("")
    z.append("  DAMIT IST DIE URSACHE DIESELBE WIE BEIM ZUSATZBEFUND: Der Ankläger weicht von seiner Ansage ab.")
    z.append("  Die Sperre prüft die angesagte Behauptung und lässt den Angriff durch; geschrieben wird dann ein")
    z.append("  Test über eine Behauptung, die längst im Vorrat steht. Die Sperre kann das nicht verhindern,")
    z.append("  weil sie die geschriebene Behauptung nie sieht.")
    z.append("")
    z.append("  BERICHTIGUNG meiner ersten Messung (N3): Dort galt Durchgerutscht = 0, gemessen über die zwei")
    z.append("  Funde. Das war zu eng gefasst — ich habe nur geprüft, ob der Test die EIGENE Ansage wiederholt,")
    z.append("  und dabei den Fall übersehen, dass er eine ANDERE vorhandene Behauptung wiederholt.")
    z.append(f"  Richtig ist: **Durchgerutscht = {len(durch)}**, der Maßstab (0) ist GERISSEN.")
    z.append("")
    z.append("  Was das für Vorbedingung 1 heißt: Von den zwei Hälften des Maßstabs ist eine erfüllt")
    z.append("  (Fehlalarm 0 von 10) und eine gerissen (Durchgerutscht 2). Das Bauteil sperrt zuverlässig, was")
    z.append("  angesagt wird, aber es sperrt nicht, was geschrieben wird. Die von Chat-Claude unter V9")
    z.append("  geforderte Prüfung „Ansage gegen Ausführung\" ist damit nicht nur Vorbedingung für Tor 4,")
    z.append("  sondern die Behebung genau dieses Befunds.")
(A / "19-nachgang-n10.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
