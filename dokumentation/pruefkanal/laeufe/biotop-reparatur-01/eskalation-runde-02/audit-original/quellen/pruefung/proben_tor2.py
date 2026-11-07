"""Tor 2 Proben: Nebenwirkungsprobe, Regressionsprobe, Norm-Probe, Vertragsprobe (ohne/mit Anpassung).
Hermes schleust Kandidaten ein (als Kandidaten-Zeilen mit nische='probe'), der Ankläger prüft sie wie jeden anderen.
Aufruf: proben_tor2.py <lauf_id> <ausgaben-dir>. Schreibt 5x-*.txt."""
import json, sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj, transaktion, j
from biotop.kern import protokoll, messgeraet
from biotop.organe import aegis, landkarte, vertraege
from biotop import lauf as L

LAUF = int(sys.argv[1]); A = Path(sys.argv[2])
con = verbinden()
lauf = L._lauf(con, LAUF); werk = L._werk(con, lauf["werk_id"]); wid = werk["id"]; pfad = Path(werk["pfad"])
mass = lj(lauf["mass"]); paket, bereiche = mass["paket"], mass["bereiche"]
ref = L._referenzlast(werk["name"], paket)
basis_gen = L.letzte_angenommene(con, LAUF); basis = lj(basis_gen["masse"])
ausgang = lj(con.execute("SELECT masse FROM generationen WHERE lauf_id=? AND nummer=0", (LAUF,)).fetchone()["masse"])
tausch = mass.get("grenzen") or {}
kanten = [(z["von"], z["nach"], z["art"]) for z in con.execute("SELECT von, nach, art FROM strassen WHERE werk_id=?", (wid,))]
bstr = landkarte.bereichs_strassen(kanten, paket)
gen = basis_gen["nummer"]


def einschleusen(bereich, diff, begruendung, vertraege_txt, name):
    with transaktion(con):
        cur = con.execute("INSERT INTO kandidaten(lauf_id, generation, bereich, nische, anbieter, modell, diff, begruendung, status, grund, erstellt_am, ist_probe) VALUES (?,?,?,?,?,?,?,?,?,?,?,1)",
                          (LAUF, gen, bereich, "probe", "hermes", f"hermes/probe-{name}", diff, begruendung, "erzeugt", "", protokoll.jetzt()))
        kid = cur.lastrowid
        # 'vertraege' Spalte existiert nicht in der Tabelle → über begruendung? Nein: Spalte ergänzen falls fehlt
    try:
        con.execute("ALTER TABLE kandidaten ADD COLUMN vertraege TEXT")
    except Exception:
        pass
    with transaktion(con):
        con.execute("UPDATE kandidaten SET vertraege=? WHERE id=?", (vertraege_txt, kid))
    protokoll.schreiben(con, "probe.eingeschleust", lauf_id=LAUF, kandidat=kid, probe=name, bereich=bereich)
    return kid


def pruefe(kid, extra=None):
    return aegis.pruefen(con, LAUF, wid, kid, pfad, paket, bereiche, bstr, basis, ausgang, ref, tausch, extra_code=extra)


def lies(rel):
    return (pfad / rel).read_text()


def diff_ersetzen(rel, alt, neu):
    """Unified diff (ein Hunk) für eine eindeutige Ersetzung."""
    src = lies(rel); assert src.count(alt) == 1, (rel, alt)
    vor = src[:src.index(alt)].count("\n")
    zeilen = src.splitlines()
    alt_z = alt.splitlines(); neu_z = neu.splitlines()
    ctx_vor = zeilen[max(0, vor - 2):vor]; ctx_nach = zeilen[vor + len(alt_z):vor + len(alt_z) + 2]
    body = [" " + l for l in ctx_vor] + ["-" + l for l in alt_z] + ["+" + l for l in neu_z] + [" " + l for l in ctx_nach]
    return f"--- a/{rel}\n+++ b/{rel}\n@@ -{max(1, vor - 1)},{len(ctx_vor) + len(alt_z) + len(ctx_nach)} +{max(1, vor - 1)},{len(ctx_vor) + len(neu_z) + len(ctx_nach)} @@\n" + "\n".join(body) + "\n"


def neue_datei_diff(rel, inhalt):
    z = inhalt.splitlines()
    return f"--- /dev/null\n+++ b/{rel}\n@@ -0,0 +1,{len(z)} @@\n" + "\n".join("+" + l for l in z) + "\n"


out = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

# ------------------------------------------------------------------ 1. Nebenwirkungsprobe
p("# Tor 2 — Nebenwirkungsprobe: Kandidat hebt Bereich A (preise) messbar, senkt Bereich B (formeln) messbar")
p("Zeit:", protokoll.jetzt(), f"| Basis: Lauf {LAUF} Generation {gen}")
# A: preise — eine tote Funktion einfügen wäre Verschlechterung; heben = ein Ankläger-offener Fund? Einfacher: A hebt durch Entfernen eines echten Fehlers, den wir zuerst brauchen.
# Wir nehmen: A = preise bekommt einen Test, der einen echten Absturz beweist? Zu komplex. Stattdessen: A = preise wird an der Referenzlast schneller (Nischenmaß, messbar),
# B = formeln bekommt einen Vertragsbruch (auswerten akzeptiert unbekannten Namen 'rabatt' → Vertragstest preise_formeln fällt) — Diff berührt formeln (fremde Datei) → wir schleusen als Bereich formeln ein
# und heben formeln selbst nicht; das ist die Nebenwirkung auf preise (Vertragstest zählt beim Lieferanten formeln, Konsument preise bricht). Einfacher, sauber messbar:
# Kandidat im Bereich lager: hebt lager (Laufzeit −50 %: Bestandscache) UND senkt bericht (Wirkungskreis!) indem er artikel() nicht mehr sortiert → test_bericht fällt.
src = lies("lagerhaus/lager/bestand.py")
alt_art = "        return sorted(a for a, s in self.journal._summen.items() if s > 0)"
neu_art = "        return [a for a, s in self.journal._summen.items() if s > 0]"
alt_inv = "    def inventur(self) -> dict[str, int]:\n        return {a: self.bestand(a) for a in self.artikel()}"
neu_inv = "    def inventur(self) -> dict[str, int]:\n        return {a: s for a, s in self.journal._summen.items() if s > 0}"
assert alt_art in src and alt_inv in src, "Nebenwirkungsprobe: Quelltext hat sich geändert"
neu_src = src.replace(alt_art, neu_art).replace(alt_inv, neu_inv)
import difflib
def voll_diff(rel, neu_text):
    alt_text = lies(rel)
    d = difflib.unified_diff(alt_text.splitlines(keepends=True), neu_text.splitlines(keepends=True), fromfile="a/" + rel, tofile="b/" + rel, n=3)
    return "".join(d)
diff1 = voll_diff("lagerhaus/lager/bestand.py", neu_src)
k1 = einschleusen("lager", diff1, "PROBE: inventur() direkt aus _summen (hebt lager) + artikel() unsortiert (senkt bericht: textbericht-Reihenfolge, Vertrag bericht→lager)", "keine", "nebenwirkung")
u1 = pruefe(k1)
p(f"Kandidat K{k1}: Status {u1['status']} — {u1['grund'][:300]}")
m1 = u1.get("mass") or {}
p("Pareto schlechter:", m1.get("pareto_schlechter")); p("Laufzeit lager (paarweise):", (lj(con.execute("SELECT masse FROM kandidaten WHERE id=?", (k1,)).fetchone()["masse"]) or {}).get("_basis_paar", {}).get("bereiche", {}).get("lager", {}).get("laufzeit_ms"), "→", ((lj(con.execute("SELECT masse FROM kandidaten WHERE id=?", (k1,)).fetchone()["masse"]) or {}).get("bereiche") or {}).get("lager", {}).get("laufzeit_ms"))
p("Wirkungskreis:", u1["wirkungskreis"], "| nennt B (bericht):", any("bericht" in x for x in (m1.get("pareto_schlechter") or [])))
p(f"ERGEBNIS Nebenwirkungsprobe: {'0 von 1 angenommen' if u1['status'] != 'ueberlebt' else '1 von 1 ANGENOMMEN (FEHLER)'}; Anklägerbericht nennt bericht: {any('bericht' in x for x in (m1.get('pareto_schlechter') or []))}")
(A / "50-nebenwirkungsprobe.txt").write_text("\n".join(out) + "\n"); out.clear()

# ------------------------------------------------------------------ 2. Regressionsprobe
p("# Tor 2 — Regressionsprobe (aus Lauf 7): Kandidat macht frühere Behebung rückgängig (S3: Reservierung nach Einlösen) und bringt 3 neue bestandene Tests mit")
p("Zeit:", protokoll.jetzt())
src = lies("lagerhaus/lager/bestand.py")
alt_s3 = "        self.entnehmen(artikel, menge, grund)\n        self._reserviert[artikel] = aktueller_reserviert - reduktion\n"
assert alt_s3 in src, "Regressionsprobe: Quelltext hat sich geändert"
neu_s3 = "        self.entnehmen(artikel, menge, grund)\n"
diff2 = diff_ersetzen("lagerhaus/lager/bestand.py", alt_s3, neu_s3)
tests3 = '''"""Drei Tests, die an Vorgeneration UND Kandidat bestehen (Bestandene zählen nicht) — plus die Regression."""
from lagerhaus.lager import Lager

def test_zugang_erhoeht_bestand():
    l = Lager(); l.zugang("A", 3); assert l.bestand("A") == 3

def test_entnahme_senkt_bestand():
    l = Lager(); l.zugang("A", 3); l.entnehmen("A", 1); assert l.bestand("A") == 2

def test_inventur_listet():
    l = Lager(); l.zugang("A", 3); assert l.inventur() == {"A": 3}
'''
diff2 += neue_datei_diff("tests/test_lager_probe_regression.py", tests3)
k2 = einschleusen("lager", diff2, "PROBE: entfernt Reservierungsabbau beim Einlösen (Regression S3), bringt 3 grüne Tests mit", "keine", "regression")
u2 = pruefe(k2)
m2 = u2.get("mass") or {}
p(f"Kandidat K{k2}: Status {u2['status']} — {u2['grund'][:400]}")
p("Pareto schlechter (je Test):", m2.get("pareto_schlechter"))
p("Kernmaß paarweise:", m2.get("kern_basis"), "→", m2.get("kern_kandidat"), "| tests_verworfen:", u2.get("tests_verworfen"))
regress = [x for x in (m2.get("pareto_schlechter") or []) if "Regression je Test" in x]
p(f"ERGEBNIS Regressionsprobe: {'0 von 1 angenommen' if u2['status'] != 'ueberlebt' else '1 von 1 ANGENOMMEN (FEHLER)'}; Protokoll nennt gefallenen Einzeltest: {bool(regress)} → {regress[:1]}")
(A / "51-regressionsprobe.txt").write_text("\n".join(out) + "\n"); out.clear()

# ------------------------------------------------------------------ 3. Norm-Probe
p("# Tor 2 — Norm-Probe (aus Lauf 7): Angriffstest fällt an der Vorgeneration, besteht am Kandidaten, ohne Absturz und ohne Vertrags-/Verfassungsbezug")
p("Zeit:", protokoll.jetzt())
# Kandidat: Katalog.alle() liefert absteigend sortiert (Meinung, kein Vertrag sagt aufsteigend? — doch: gen0-Test m4 prüft aufsteigend → würde fallen). Anderes Beispiel:
# Kandidat ändert formel_beschreibung: Kürzung bei > 60 statt > 40 Zeichen; mitgebrachter Test behauptet „bis 60 Zeichen ungekürzt“ — fällt an Basis, besteht am Kandidaten, kein Vertrag, kein Absturz.
alt_fb = '    if len(kurz) > 40:\n        kurz = kurz[:37] + "..."'
neu_fb = '    if len(kurz) > 60:\n        kurz = kurz[:57] + "..."'
diff3 = diff_ersetzen("lagerhaus/formeln/auswertung.py", alt_fb, neu_fb)
test_norm = '''from lagerhaus.formeln.auswertung import formel_beschreibung

def test_beschreibung_bis_60_zeichen_ungekuerzt():
    f = "a" * 55
    assert formel_beschreibung(f) == "Formel „" + f + "“"
'''
diff3 += neue_datei_diff("tests/test_formeln_probe_norm.py", test_norm)
k3 = einschleusen("formeln", diff3, "PROBE: Kürzungsgrenze 40 → 60 Zeichen; Test kodiert die neue Grenze als Norm (kein Vertrag, kein Absturz)", "keine", "norm")
u3 = pruefe(k3)
m3 = u3.get("mass") or {}
p(f"Kandidat K{k3}: Status {u3['status']} — {u3['grund'][:300]}")
p("tests_neu (gezählt):", u3.get("tests_neu"), "| tests_verworfen:", u3.get("tests_verworfen"), "| norm (Ankläger):", u3.get("norm"))
p("Kernmaß paarweise:", m3.get("kern_basis"), "→", m3.get("kern_kandidat"), "(Zuwachs", m3.get("zuwachs"), ")")
im_werk = con.execute("SELECT COUNT(*) FROM immunsystem WHERE werk_id=? AND status='im_werk' AND name LIKE ?", (wid, f"%k{k3}%")).fetchone()[0]
offen = con.execute("SELECT name, status FROM immunsystem WHERE werk_id=? AND name LIKE ?", (wid, f"%k{k3}%")).fetchall()
p("Immunsystem-Einträge zu diesem Kandidaten:", [(r[0], r[1]) for r in offen], "| im Werk:", im_werk)
p(f"ERGEBNIS Norm-Probe: Zuwachs {m3.get('zuwachs')} (Soll 0); Status {u3['status']} (Soll abgelehnt/unverändert); mitgebrachter Norm-Test ins Werk: {'nein' if 'tests/test_formeln_probe_norm.py' not in ((lj(con.execute('SELECT masse FROM kandidaten WHERE id=?', (k3,)).fetchone()['masse']) or {}).get('_dateien') or {}) else 'JA (FEHLER)'}")
(A / "52-normprobe.txt").write_text("\n".join(out) + "\n"); out.clear()

# ------------------------------------------------------------------ 4. Vertragsprobe
p("# Tor 2 — Vertragsprobe: Änderung an der Grenze preise→formeln (auswerten bekommt Pflichtparameter 'waehrung')")
p("Zeit:", protokoll.jetzt())
src = lies("lagerhaus/formeln/auswertung.py")
alt_sig = "def auswerten(formel: str, menge: int, preis: float, summe: float):"
neu_sig = "def auswerten(formel: str, menge: int, preis: float, summe: float, waehrung: str):"
diff4 = diff_ersetzen("lagerhaus/formeln/auswertung.py", alt_sig, neu_sig)
# Vertragsdatei anpassen (Signatur-Test) — Teil des Kandidaten, Vertrag benannt
vt_src = lies("tests/vertraege/test_vertrag_preise_formeln.py")
vt_neu = vt_src.replace('assert p == ["formel", "menge", "preis", "summe"]', 'assert p == ["formel", "menge", "preis", "summe", "waehrung"]')
vt_neu = vt_neu.replace('auswerten("summe * 0.05", 3, 10.0, 30.0)', 'auswerten("summe * 0.05", 3, 10.0, 30.0, "EUR")').replace('auswerten("menge >= 10", 10, 1.0, 10.0)', 'auswerten("menge >= 10", 10, 1.0, 10.0, "EUR")').replace('auswerten("menge >= 10", 9, 1.0, 9.0)', 'auswerten("menge >= 10", 9, 1.0, 9.0, "EUR")').replace('auswerten("rabatt * 2", 1, 1.0, 1.0)', 'auswerten("rabatt * 2", 1, 1.0, 1.0, "EUR")').replace('auswerten("min(summe, 20)", 5, 10.0, 50.0)', 'auswerten("min(summe, 20)", 5, 10.0, 50.0, "EUR")').replace('auswerten("max(menge, 7)", 5, 10.0, 50.0)', 'auswerten("max(menge, 7)", 5, 10.0, 50.0, "EUR")').replace('auswerten("abs(0 - 3)", 1, 1.0, 1.0)', 'auswerten("abs(0 - 3)", 1, 1.0, 1.0, "EUR")').replace('auswerten("summe + menge", menge, preis, summe)', 'auswerten("summe + menge", menge, preis, summe, "EUR")')
diff4_mit_vertrag = diff4 + voll_diff("tests/vertraege/test_vertrag_preise_formeln.py", vt_neu)
# Fall 1: ohne Anpassung des Nachbarn (preise ruft weiterhin mit 4 Argumenten) → Vertragstest + test_preise fallen → abgelehnt
k4a = einschleusen("formeln", diff4_mit_vertrag, "PROBE: neuer Pflichtparameter waehrung an auswerten(); Vertrag preise→formeln benannt; OHNE Anpassung von preise", "tests/vertraege/test_vertrag_preise_formeln.py (Signatur auswerten)", "vertrag-ohne")
u4a = pruefe(k4a)
m4a = u4a.get("mass") or {}
p(f"Fall 1 (ohne Anpassung) K{k4a}: Status {u4a['status']} — {u4a['grund'][:300]}")
p("  vertrag_verletzt:", u4a.get("vertrag_verletzt"), "| Pareto schlechter:", (m4a.get("pareto_schlechter") or [])[:3])
# Fall 2: mit Anpassung des Nachbarn preise (rabatt.py ruft mit 'EUR') → Paar
alt_call1 = "    if not auswerten(regel.bedingung, menge, preis, summe):"
neu_call1 = '    if not auswerten(regel.bedingung, menge, preis, summe, "EUR"):'
alt_call2 = "    betrag = auswerten(regel.betrag, menge, preis, summe)"
neu_call2 = '    betrag = auswerten(regel.betrag, menge, preis, summe, "EUR")'
rab = lies("lagerhaus/preise/rabatt.py").replace(alt_call1, neu_call1).replace(alt_call2, neu_call2)
# alte formeln-Tests rufen mit 4 Argumenten → sie sind Teil des Werks und würden fallen. Vertragsänderung an der Grenze heißt auch: Tests des Lieferanten müssen mitziehen —
# das darf der Kandidat NICHT (Verfassung Satz 6: keine vorhandenen Tests ändern). Deshalb: waehrung als OPTIONALER Parameter mit Pflicht-Prüfung im Vertrag? Dann bricht nichts →
# Vertragstest muss die neue Signatur fordern (Pflichtparameter für den Konsumenten): Wir machen waehrung optional (Default "EUR"), Vertragstest prüft, dass der Parameter existiert
# und dass preise ihn übergibt (Vertragsänderung = beide Seiten). Fall 1 (nur formeln) fällt dann am Vertragstest „preise übergibt waehrung“.
neu_sig2 = 'def auswerten(formel: str, menge: int, preis: float, summe: float, waehrung: str = "EUR"):'
# Fall 2: reiner Vertragsumbau (beide Seiten). Er bringt keinen Kernmaßgewinn; gemessen wird, ob der Vertrag im Paar bestanden ist.
diff4b = diff_ersetzen("lagerhaus/formeln/auswertung.py", alt_sig, neu_sig2)
vt2 = vt_src.replace('assert p == ["formel", "menge", "preis", "summe"]', 'assert p == ["formel", "menge", "preis", "summe", "waehrung"]')
vt2 += '''

def test_konsument_preise_uebergibt_waehrung():
    """Vertragsänderung (beide Seiten): preise.rabatt ruft auswerten mit waehrung."""
    import inspect
    from lagerhaus.preise import rabatt
    src = inspect.getsource(rabatt)
    assert 'auswerten(regel.bedingung, menge, preis, summe, "EUR")' in src
'''
diff4b_mit_vertrag = diff4b + voll_diff("tests/vertraege/test_vertrag_preise_formeln.py", vt2)
k4c = einschleusen("formeln", diff4b_mit_vertrag, "PROBE Fall 1b: optionaler Parameter waehrung + Vertrag verlangt, dass preise ihn übergibt; OHNE Anpassung von preise", "tests/vertraege/test_vertrag_preise_formeln.py", "vertrag-ohne-b")
u4c = pruefe(k4c)
p(f"Fall 1b (ohne Anpassung, optionaler Parameter) K{k4c}: Status {u4c['status']} — {u4c['grund'][:300]}")
p("  vertrag_verletzt:", u4c.get("vertrag_verletzt"))
k4b = einschleusen("formeln", diff4b_mit_vertrag, "PROBE Fall 2: wie 1b, MIT Anpassung des Nachbarn preise (rabatt.py übergibt waehrung)", "tests/vertraege/test_vertrag_preise_formeln.py", "vertrag-mit")
u4b = pruefe(k4b, extra={"lagerhaus/preise/rabatt.py": rab})
m4b = u4b.get("mass") or {}
p(f"Fall 2 (mit Anpassung des Nachbarn) K{k4b}: Status {u4b['status']} — {u4b['grund'][:300]}")
p("  vertrag_verletzt:", u4b.get("vertrag_verletzt"), "| Pareto schlechter:", m4b.get("pareto_schlechter"), "| Kernmaß", m4b.get("kern_basis"), "→", m4b.get("kern_kandidat"))
p("  Hinweis: Fall 2 ist ein Vertragsumbau ohne Kernmaßgewinn — nach 3.5 F2 'Kernmaß unverändert' → nicht angenommen. Die Vertragsprobe misst: Fall 1 am Vertrag abgelehnt (ja/nein), Fall 2 Vertrag bestanden (ja/nein).")
p(f"ERGEBNIS Vertragsprobe: ohne Anpassung → {'abgelehnt am Vertrag' if u4c.get('vertrag_verletzt') else 'NICHT am Vertrag abgelehnt (FEHLER)'} ({u4c.get('vertrag_verletzt')}); mit Anpassung → Vertrag {'bestanden (0 verletzt)' if not u4b.get('vertrag_verletzt') else 'VERLETZT (FEHLER)'}; Paar-Status {u4b['status']} ({u4b['grund'][:80]})")
(A / "53-vertragsprobe.txt").write_text("\n".join(out) + "\n"); out.clear()

# Proben-Kandidaten dürfen nie ins Werk: Status sichern
with transaktion(con):
    con.execute("UPDATE kandidaten SET status='probe_' || status WHERE lauf_id=? AND nische='probe' AND status NOT LIKE 'probe_%'", (LAUF,))
print("Proben-Kandidaten markiert:", [dict(r) for r in con.execute("SELECT id, status FROM kandidaten WHERE lauf_id=? AND nische='probe'", (LAUF,))])
