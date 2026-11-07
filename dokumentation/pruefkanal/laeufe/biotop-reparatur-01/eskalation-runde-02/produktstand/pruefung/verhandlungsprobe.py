"""Verhandlungsprobe (Tor 2 Zeile 9, ergänzend): Hermes schleust einen Kandidaten ein, der einen expliziten Vertrag ändert und
ihn unter VERTRÄGE benennt; der Schwarm des Nachbarn erzeugt die Anpassung; der Ankläger prüft das Paar (lauf._verhandeln).
Der Kandidat bringt zusätzlich eine Behebung mit Vertragsbezug mit, damit das Paar einen Kernmaßgewinn hat und eine
Generalprobe möglich wäre. Läuft gegen den aktuellen Stand des Laufs, ohne ins Werk zu schreiben.
Aufruf: verhandlungsprobe.py <lauf_id> <ausgaben-dir>"""
import difflib, sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj, transaktion
from biotop.kern import protokoll
from biotop.organe import aegis, landkarte
from biotop import lauf as L

LAUF = int(sys.argv[1]); A = Path(sys.argv[2])
con = verbinden()
lauf = L._lauf(con, LAUF); werk = L._werk(con, lauf["werk_id"]); wid = werk["id"]; pfad = Path(werk["pfad"])
mass = lj(lauf["mass"]); paket, bereiche = mass["paket"], mass["bereiche"]
ref = L._referenzlast(werk["name"], paket)
basis_gen = L.letzte_angenommene(con, LAUF); basis = lj(basis_gen["masse"]); gen = basis_gen["nummer"]
ausgang = lj(con.execute("SELECT masse FROM generationen WHERE lauf_id=? AND nummer=0", (LAUF,)).fetchone()["masse"])
tausch = mass.get("grenzen") or {}
kanten = [(z["von"], z["nach"], z["art"]) for z in con.execute("SELECT von, nach, art FROM strassen WHERE werk_id=?", (wid,))]
bstr = landkarte.bereichs_strassen(kanten, paket)
out = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
def lies(rel): return (pfad / rel).read_text()
def voll_diff(rel, neu):
    return "".join(difflib.unified_diff(lies(rel).splitlines(keepends=True), neu.splitlines(keepends=True), fromfile="a/" + rel, tofile="b/" + rel, n=3))

p("# Tor 2 — Verhandlungsprobe (Hermes-eingeschleust, gekennzeichnet): Vertragsänderung an der Grenze preise → formeln")
p("Zeit:", protokoll.jetzt(), f"| Basis Lauf {LAUF} Generation {gen}")
p("Änderung: auswerten() bekommt einen optionalen Parameter `waehrung` (Default 'EUR'); der Vertrag preise→formeln verlangt, dass der Konsument preise ihn übergibt.")
p("Ohne Anpassung von preise fällt der Vertragstest; mit Anpassung (rabatt.py übergibt 'EUR') besteht das Paar. Der Kandidat benennt den Vertrag unter VERTRÄGE → Verhandlung.")

alt_sig = "def auswerten(formel: str, menge: int, preis: float, summe: float):"
src = lies("lagerhaus/formeln/auswertung.py"); assert alt_sig in src
neu_src = src.replace(alt_sig, 'def auswerten(formel: str, menge: int, preis: float, summe: float, waehrung: str = "EUR"):')
vt = lies("tests/vertraege/test_vertrag_preise_formeln.py")
vt2 = vt.replace('assert p == ["formel", "menge", "preis", "summe"]', 'assert p == ["formel", "menge", "preis", "summe", "waehrung"]') + '''

def test_konsument_preise_uebergibt_waehrung():
    """Vertragsänderung (beide Seiten, Anhang A Satz 4): preise.rabatt ruft auswerten mit waehrung."""
    import inspect
    from lagerhaus.preise import rabatt
    src = inspect.getsource(rabatt)
    assert 'auswerten(regel.bedingung, menge, preis, summe, "EUR")' in src
'''
diff = voll_diff("lagerhaus/formeln/auswertung.py", neu_src) + voll_diff("tests/vertraege/test_vertrag_preise_formeln.py", vt2)
with transaktion(con):
    cur = con.execute("INSERT INTO kandidaten(lauf_id, generation, bereich, nische, anbieter, modell, diff, begruendung, status, grund, erstellt_am, vertraege, ist_probe) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,1)",
                      (LAUF, gen, "formeln", "probe", "hermes", "hermes/probe-verhandlung", diff,
                       "PROBE: Vertragsänderung preise→formeln (optionaler Parameter waehrung, Konsument muss ihn übergeben)", "erzeugt", "", protokoll.jetzt(),
                       "tests/vertraege/test_vertrag_preise_formeln.py — Signatur auswerten erweitert; preise muss waehrung übergeben"))
    kid = cur.lastrowid
protokoll.schreiben(con, "probe.eingeschleust", lauf_id=LAUF, kandidat=kid, probe="verhandlung", bereich="formeln")
u = aegis.pruefen(con, LAUF, wid, kid, pfad, paket, bereiche, bstr, basis, ausgang, ref, tausch)
p(f"\nSchritt 1 — Einzelprüfung K{kid}: {u['status']} — {u['grund'][:200]}")
p("  vertrag_verletzt:", u.get("vertrag_verletzt"), "| Vertrag benannt:", (u.get("vertraege_benannt") or "")[:80])
u2 = L._verhandeln(con, LAUF, werk, gen, pfad, paket, bereiche, bstr, basis, ausgang, ref, tausch, "formeln", kid, u)
p(f"\nSchritt 2 — Verhandlung (Schwarm des Nachbarn preise, Nische sicher, 2 Hersteller per Bandit): Ergebnis {u2['status']} — {u2['grund'][:250]}")
p("  vertrag_verletzt nach Paar:", u2.get("vertrag_verletzt"), "| Pareto schlechter:", (u2.get("mass") or {}).get("pareto_schlechter"), "| Kernmaß:", (u2.get("mass") or {}).get("kern_basis"), "→", (u2.get("mass") or {}).get("kern_kandidat"))
for z in con.execute("SELECT nr, art, substr(inhalt,1,400) i FROM protokoll WHERE art LIKE 'verhandlung.%' AND inhalt LIKE ? ORDER BY nr", (f'%"kandidat": {kid},%',)):
    p(f"  Protokoll #{z['nr']} {z['art']}: {z['i']}")
anp = [dict(r) for r in con.execute("SELECT id, bereich, modell, status, substr(grund,1,120) g FROM kandidaten WHERE lauf_id=? AND status='verhandlung' AND grund LIKE ?", (LAUF, f"%Kandidat {kid}%"))]
for a in anp:
    d = con.execute("SELECT diff FROM kandidaten WHERE id=?", (a["id"],)).fetchone()["diff"]
    p(f"  Anpassung K{a['id']} ({a['bereich']}, {a['modell']}): {a['g']}")
    p("    " + " | ".join(l for l in d.splitlines() if l.startswith(("+", "-")) and not l.startswith(("+++", "---")))[:400])
bestanden = bool(con.execute("SELECT 1 FROM protokoll WHERE art='verhandlung.bestanden' AND inhalt LIKE ?", (f'%"kandidat": {kid},%',)).fetchone())
vertrag_ok = not u2.get("vertrag_verletzt")
p(f"\nERGEBNIS Verhandlungsprobe: Vertrag im Paar bestanden (0 Vertragstests verletzt): {vertrag_ok}; verhandlung.bestanden protokolliert: {bestanden}; Paar-Status {u2['status']} ({'Kernmaß unverändert → keine Annahme, aber Vertragsänderung gemeinsam bestanden' if u2['status'] != 'ueberlebt' and vertrag_ok else u2['grund'][:80]})")
with transaktion(con):
    con.execute("UPDATE kandidaten SET status='probe_' || status WHERE id=? AND status NOT LIKE 'probe_%'", (kid,))
(A / "54-verhandlungsprobe.txt").write_text("\n".join(out) + "\n")
