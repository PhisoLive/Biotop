"""N13 + N14 (Prüfung 6): Welche Aufnahmestelle wurde belegt — und Beleg für die zweite.

N13: `#16010` und `#16014` tragen beide `sperrart: "norm"` → nur die Norm-Stelle war belegt.
N14: Ein zweiter gestellter Gegenstand durch den laufenden Kern, diesmal so gebaut, dass der Angriffstest
     am Kandidaten FÄLLT und damit als FUND läuft — dort sitzt die zweite Aufnahmestelle (aegis.py:621),
     auf der `aegis_k2500_preise` in Lauf 24 durchrutschte. Dazu eine ANDERE Doppelung als beim ersten Fall,
     damit zwei verschiedene Sperrfälle vorliegen statt eines zweimal.
Kein Modellaufruf: der Angriff wird gestellt, der Pfad ist echt.
Aufruf: nachgang_n13_n14.py <ausgaben-dir>
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
z = ["# N13 und N14 — Aufnahmestelle benennen und die zweite Stelle belegen (0 Modellaufrufe)", ""]

# ---------------------------------------------------------------- N13
z.append("## N13 — Welche Stelle hat `#16014` geschrieben?")
for nr in (16010, 16014):
    inhalt = con.execute("SELECT inhalt FROM protokoll WHERE nr=?", (nr,)).fetchone()[0]
    d = lj(inhalt) or {}
    z.append(f"  #{nr}: sperrart = **{d.get('sperrart')}** · bereich {d.get('bereich')} · "
             f"kandidat {d.get('kandidat')} · anzahl {d.get('anzahl')}")
z.append("")
z.append("  C hat zwei Aufrufstellen im Kern (`biotop/organe/aegis.py`):")
z.append("    Zeile 621: Aufnahme von **Funden**      → `aufnahmesperre(..., art='fund')`")
z.append("    Zeile 654: Aufnahme von **Norm-Tests**  → `aufnahmesperre(..., art='norm')`")
z.append("  Das Feld `sperrart` im Protokoll benennt die Stelle eindeutig.")
z.append("")
z.append("  **ANTWORT: Beide Protokollzeilen tragen `sperrart='norm'` — belegt war nur die NORM-Stelle.**")
z.append("  Die Fund-Stelle (Zeile 621) ist damit unbelegt. Der Prüfbefund trifft zu, und er trifft die")
z.append("  gefährlichere Stelle: `aegis_k2500_preise`, einer der beiden in Lauf 24 gemessenen Durchrutscher,")
z.append("  war ein Fund. N14 ist nötig.")
z.append("")

# ---------------------------------------------------------------- N14
z.append("## N14 — Beleg für die Fund-Stelle, mit einer ANDEREN Doppelung")
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

vorrat = aegis.bisherige_behauptungen(con, WERK, "preise", LAUF)
z.append(f"  Bereich `preise`, Vorrat: {len(vorrat)} Behauptungen — {', '.join(vorrat)}")
z.append("  Gewählte Doppelung: `preis_fuer|GtE:zahl` — **eine andere als im ersten Fall** "
         "(`reserviert|Eq:zahl`, Bereich lager) und genau die Behauptung, auf der `aegis_k2500_preise` durchrutschte.")
z.append("")

# Der Kandidat baut einen echten Fehler ein: rabatt() ignoriert die Untergrenze.
datei = pfad / paket / "preise" / "katalog.py"
quelle = datei.read_text()
z.append(f"  Kandidat ändert `{paket}/preise/katalog.py` (reiner Kommentar, keine Laufzeitwirkung);")
z.append("  der beigegebene Angriffstest FÄLLT am Kandidaten — nur dann entsteht ein Fund und C wird an")
z.append("  der Fund-Stelle erreicht.")

# Angriffstest: fällt am Kandidaten (Absturz im Werk → gilt als Fund nach 3.7a), trägt die Doppelung
ANGRIFF = '''from lagerhaus.preise import Katalog, Artikel


def test_rot2_preis_fuer_wiederholte_behauptung():
    """Vertrag test_vertrag_bericht_preise::test_preis_fuer_cent_gerundet_nie_negativ.

    Traegt `preis_fuer|GtE:zahl` — steht im Vorrat von `preise` (ROT, andere Doppelung als Fall 1).
    Nennt einen Vertrag ausdruecklich, damit die Norm-Regel 3.7 ihn als FUND anerkennt und C an der
    Fund-Stelle erreicht wird.
    """
    k = Katalog()
    k.aufnehmen(Artikel("A", "a", 10.0))
    assert k.preis_fuer("A", 5) >= 999.0


def test_gruen2_neue_behauptung_im_fund_zweig():
    """Vertrag test_vertrag_bericht_preise::test_schnittstelle_katalog.

    Traegt `anzahl|Lt:zahl` — nicht im Vorrat (GRUEN), ebenfalls mit Vertragsverweis.
    """
    k = Katalog()
    assert k.anzahl() < -1
'''
for n in ("test_rot2_preis_fuer_wiederholte_behauptung", "test_gruen2_neue_behauptung_im_fund_zweig"):
    s = aegis.behauptung(ANGRIFF, n, paket)
    z.append(f"    {n} → `{s}` (im Vorrat: {s in vorrat})")
z.append("")

zeilen = quelle.splitlines()
diff = (f"--- a/{paket}/preise/katalog.py\n+++ b/{paket}/preise/katalog.py\n"
        f"@@ -{len(zeilen)},1 +{len(zeilen)},2 @@\n"
        f" {zeilen[-1]}\n+# N14: gestellter Gegenstand für den Pfadnachweis der Fund-Stelle\n")
with transaktion(con):
    cur = con.execute("INSERT INTO kandidaten(lauf_id, generation, bereich, nische, anbieter, modell, diff,"
                      " begruendung, status, grund, erstellt_am, vertraege, ist_probe)"
                      " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,1)",
                      (LAUF, basis_gen["nummer"], "preise", "probe_pfadnachweis_fund", "hermes",
                       "hermes/n14", diff, "N14: gestellter Gegenstand für die Fund-Stelle von C", "erzeugt", "",
                       protokoll.jetzt(), "keine"))
    kid = cur.lastrowid
z.append(f"  Kandidat K{kid} eingeschleust (ist_probe=1).")

vor_fund = sum(1 for r in con.execute("SELECT inhalt FROM protokoll WHERE art='immun.aufnahme_geprueft'")
               if (lj(r["inhalt"]) or {}).get("lauf_id") == LAUF and (lj(r["inhalt"]) or {}).get("sperrart") == "fund")
echt = aegis._angriff
aegis._angriff = lambda *a, **k: (ANGRIFF, "hermes/gestellt-n14", "preis_fuer|GtE:zahl")
try:
    urteil = aegis.pruefen(con, LAUF, WERK, kid, pfad, paket, bereiche, bstr, basis, ausgang, ref,
                           mass.get("grenzen") or {})
finally:
    aegis._angriff = echt
nach_fund = sum(1 for r in con.execute("SELECT inhalt FROM protokoll WHERE art='immun.aufnahme_geprueft'")
                if (lj(r["inhalt"]) or {}).get("lauf_id") == LAUF and (lj(r["inhalt"]) or {}).get("sperrart") == "fund")

z.append("")
z.append("## Ergebnis")
z.append(f"  Urteil: {urteil.get('status')} — {(urteil.get('grund') or '')[:110]}")
z.append(f"  am Kandidaten bestätigt: {(urteil.get('angriff') or {}).get('bestaetigt_kandidat')}")
z.append(f"  als Norm: {urteil.get('norm')}")
z.append(f"  Aufnahmesperre: {urteil.get('aufnahmesperre')}")
z.append(f"  Aufrufe von C mit sperrart='fund': {vor_fund} → {nach_fund}")
z.append("")
for r in con.execute("SELECT nr, inhalt FROM protokoll WHERE art IN ('immun.aufnahme_geprueft','immun.aufnahme_gesperrt') ORDER BY nr DESC LIMIT 4"):
    d = lj(r["inhalt"]) or {}
    if d.get("lauf_id") == LAUF and d.get("sperrart") == "fund":
        z.append(f"  Protokoll #{r['nr']}: {r['inhalt'][:280]}")
(A / "25-31-n13-n14-aufnahmestellen.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
