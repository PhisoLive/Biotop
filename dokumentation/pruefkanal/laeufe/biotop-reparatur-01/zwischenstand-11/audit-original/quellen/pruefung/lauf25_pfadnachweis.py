"""Lauf 25, Pfadnachweis durch den laufenden Kern (Masterprompt Abschnitt 4.1).

Der Lauf selbst hat C keinen Gegenstand geliefert: 0 erzeugte Einträge, 0 Aufrufe von C. Der Auftrag lässt
für den roten Eichfall einen GESTELLTEN Fall zu, sofern er **durch den laufenden Kern** geht — nicht offline
rekonstruiert. Genau das wird hier getan, und zwar über den echten Anklägerpfad `aegis.pruefen`:

  Ein Kandidat wird in Lauf 25 eingeschleust, dem ein Angriffstest beigegeben wird (`extra_code`), der
  am Kandidaten fällt und eine Behauptung trägt, die im Vorrat des Bereichs bereits steht. Der Ankläger
  läuft vollständig durch — Wirkungskreis, Verträge, Verfassung, Kammer, Urteil — und erreicht damit die
  Aufnahmestelle, an der C sitzt.

Gestellt ist der Gegenstand. Der Pfad ist echt.
Aufruf: lauf25_pfadnachweis.py <ausgaben-dir>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern import protokoll
from biotop.kern.datenbank import verbinden, lj, transaktion
from biotop.organe import aegis, landkarte
from biotop import lauf as L

A = Path(sys.argv[1])
con = verbinden()
LAUF, WERK = 25, 22
lauf = L._lauf(con, LAUF)
werk = L._werk(con, lauf["werk_id"])
pfad = Path(werk["pfad"])
mass = lj(lauf["mass"])
paket, bereiche = mass["paket"], mass["bereiche"]
ref = L._referenzlast(werk["name"], paket)
basis_gen = L.letzte_angenommene(con, LAUF)
basis = lj(basis_gen["masse"])
ausgang = lj(con.execute("SELECT masse FROM generationen WHERE lauf_id=? AND nummer=0", (LAUF,)).fetchone()["masse"])
kanten = [(r["von"], r["nach"], r["art"]) for r in con.execute("SELECT von, nach, art FROM strassen WHERE werk_id=?", (WERK,))]
bstr = landkarte.bereichs_strassen(kanten, paket)

z = ["# Lauf 25 — Pfadnachweis für C durch den laufenden Kern (gestellter Gegenstand, echter Pfad)",
     "# Masterprompt Abschnitt 4.1: Der Unterschied ist nicht „natürlich gegen gestellt“, sondern",
     "# „durch den laufenden Pfad gegen offline rekonstruiert“.", ""]

vorrat = aegis.bisherige_behauptungen(con, WERK, "lager", LAUF)
z.append(f"Vorrat des Bereichs `lager` vor der Prüfung: {len(vorrat)} Behauptungen")
z.append(f"  darunter: {', '.join(vorrat[:6])} …")
z.append("")

# Ein Angriffstest, der am Kandidaten FÄLLT und eine bereits vorhandene Behauptung trägt (ROT),
# plus einer mit neuer Behauptung (GRÜN). Beide gehen durch denselben Aufnahmepfad.
ANGRIFF = '''from lagerhaus.lager import Lager


def test_rot_wiederholt_vorhandene_behauptung():
    """Trägt `reserviert|Eq:zahl` — steht bereits im Vorrat (ROT)."""
    lager = Lager()
    lager.zugang("A", 10)
    assert lager.reserviert("A") == 99


def test_gruen_neue_behauptung():
    """Trägt `inventur|Eq:text` — im Vorrat nicht vorhanden (GRÜN)."""
    lager = Lager()
    assert lager.inventur() == "unmoeglicher-wert"
'''
z.append("Zwei Angriffstests werden dem Kandidaten beigegeben:")
for n in ("test_rot_wiederholt_vorhandene_behauptung", "test_gruen_neue_behauptung"):
    s = aegis.behauptung(ANGRIFF, n, paket)
    z.append(f"  {n} → `{s}` (im Vorrat: {s in vorrat})")
z.append("")

# Kandidat einschleusen: kleine, echte Änderung im Bereich lager
datei = pfad / paket / "lager" / "bestand.py"
quelle = datei.read_text()
marke = "\n\n# Eichfall Lauf 25: unveränderte Wirkung, nur Kommentar\n"
neu = quelle + marke
zeilen_alt = quelle.splitlines()
diff = (f"--- a/{paket}/lager/bestand.py\n+++ b/{paket}/lager/bestand.py\n"
        f"@@ -{len(zeilen_alt)},1 +{len(zeilen_alt)},3 @@\n"
        f" {zeilen_alt[-1]}\n+\n+# Eichfall Lauf 25: unveränderte Wirkung, nur Kommentar\n")
with transaktion(con):
    cur = con.execute("INSERT INTO kandidaten(lauf_id, generation, bereich, nische, anbieter, modell, diff,"
                      " begruendung, status, grund, erstellt_am, vertraege, ist_probe)"
                      " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,1)",
                      (LAUF, basis_gen["nummer"], "lager", "probe_pfadnachweis", "hermes", "hermes/pfadnachweis",
                       diff, "Gestellter Gegenstand für den Pfadnachweis von C (Masterprompt 4.1)", "erzeugt", "",
                       protokoll.jetzt(), "keine"))
    kid = cur.lastrowid
z.append(f"Kandidat K{kid} eingeschleust (ist_probe=1, kommt in kein Gedächtnis).")
z.append("")

vor_g = sum(1 for r in con.execute("SELECT inhalt FROM protokoll WHERE art='immun.aufnahme_geprueft'")
            if (lj(r["inhalt"]) or {}).get("lauf_id") == LAUF)
vor_s = sum(1 for r in con.execute("SELECT inhalt FROM protokoll WHERE art='immun.aufnahme_gesperrt'")
            if (lj(r["inhalt"]) or {}).get("lauf_id") == LAUF)

# Der Ankläger läuft vollständig; der Angriff wird über extra_code beigegeben, damit kein Modellaufruf nötig ist.
echt_angriff = aegis._angriff
aegis._angriff = lambda *a, **k: (ANGRIFF, "hermes/gestellt", "reserviert|Eq:zahl")
try:
    urteil = aegis.pruefen(con, LAUF, WERK, kid, pfad, paket, bereiche, bstr, basis, ausgang, ref,
                           mass.get("grenzen") or {})
finally:
    aegis._angriff = echt_angriff

nach_g = sum(1 for r in con.execute("SELECT inhalt FROM protokoll WHERE art='immun.aufnahme_geprueft'")
             if (lj(r["inhalt"]) or {}).get("lauf_id") == LAUF)
nach_s = sum(1 for r in con.execute("SELECT inhalt FROM protokoll WHERE art='immun.aufnahme_gesperrt'")
             if (lj(r["inhalt"]) or {}).get("lauf_id") == LAUF)

z.append("## Ergebnis des Anklägerlaufs")
z.append(f"  Urteil: {urteil.get('status')} — {(urteil.get('grund') or '')[:120]}")
z.append(f"  Angriffstests am Kandidaten bestätigt: {(urteil.get('angriff') or {}).get('bestaetigt_kandidat')}")
z.append(f"  als Norm eingestuft: {urteil.get('norm')}")
z.append(f"  Aufnahmesperre im Urteil: {urteil.get('aufnahmesperre')}")
z.append("")
z.append("## Pfadnachweis")
z.append(f"  Aufrufe von C vor der Prüfung: {vor_g} · nach der Prüfung: {nach_g} → **{nach_g - vor_g} Aufruf(e)**")
z.append(f"  Sperrungen vor: {vor_s} · nach: {nach_s} → **{nach_s - vor_s} Sperrung(en)**")
z.append(f"  ERGEBNIS: C liegt im Aufnahmepfad und wird erreicht: {nach_g > vor_g}")
z.append("")

for r in con.execute("SELECT nr, inhalt FROM protokoll WHERE art IN ('immun.aufnahme_geprueft','immun.aufnahme_gesperrt') ORDER BY nr DESC LIMIT 4"):
    d = lj(r["inhalt"]) or {}
    if d.get("lauf_id") == LAUF:
        z.append(f"  Protokoll #{r['nr']}: {r['inhalt'][:260]}")
z.append("")
z.append("## Eichfälle (aus dem Immunsystem nachgelesen, nicht aus dem Rückgabewert)")
sperr = urteil.get("aufnahmesperre") or {}
angelegt = [dict(r) for r in con.execute(
    "SELECT name, bereich, substr(ursprung,1,200) u FROM immunsystem WHERE lauf_id=? AND ursprung LIKE ?",
    (LAUF, f"%Kandidat {kid}%"))]
z.append(f"  ROT   `test_rot_wiederholt_vorhandene_behauptung` (`reserviert|Eq:zahl`, im Vorrat): "
         f"von C ABGEWIESEN → {sperr.get('abgewiesen')}")
for e in angelegt:
    z.append(f"  GRÜN  Eintrag `{e['name']}` wurde angelegt: {e['u']}")
if not angelegt:
    z.append("  GRÜN  KEIN Eintrag angelegt — grüner Eichfall FEHLT")
z.append("")
z.append("  Hinweis zur Herkunft: Der Rückgabewert `aufnahmesperre.aufgenommen` im Urteil führt nur die Funde;")
z.append("  Norm-Einträge werden in einem eigenen Zweig angelegt und erscheinen dort nicht. Die Eichfälle sind")
z.append("  deshalb am Immunsystem und am Protokoll `immun.norm` abgelesen, nicht am Rückgabewert.")
(A / "25-21-pfadnachweis.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
