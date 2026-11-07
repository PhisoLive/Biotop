"""Behebungsrunde vor T4 (Masterprompt Fassung 8, Abschnitt 8, Vorbedingungen 1–11) — Einheitstests mit Gegenproben.

Die Gegenproben durch den Laufweg (Nachspiel der aufgezeichneten T3-Kandidaten durch aegis.pruefen, Kammer) stehen
in /root/biotop-vor-t4/; hier stehen die schnellen Nachweise, die in jeder Regression laufen. Jede Probe hat eine
Gegenprobe, die an der vorgesehenen Zusicherung scheitern muss (Grundsatz 8).
"""
import json
import sqlite3
from datetime import datetime, timedelta, timezone

import pytest

from biotop import lauf as L
from biotop.anbieter import AnbieterFehler, ist_drosselung
from biotop.kern import datenbank, messgeraet as M, protokoll
from biotop.organe import aegis, gedaechtnis, masseichung, nischen


# ================================================================ 1. Laufzeit gepaart (Grundsatz 14)
def test_1_grenze_misst_gegen_die_gepaarte_vorgeneration_nicht_gegen_das_minimum(messung):
    """T3 K3121: Bestwert (Minimum) 3,82 ms × 1,219 = 4,6586 < 4,6609 → gerissen, obwohl die Vorgeneration derselben
    Sitzung 4,80 ms lief. Gepaart ist die Grenze 4,80 × 1,219."""
    bestwert, basis, kandidat = messung(), messung(), messung()
    bestwert["bereiche"]["alpha"]["laufzeit_ms"] = 3.8216
    basis["bereiche"]["alpha"]["laufzeit_ms"] = 4.80
    kandidat["bereiche"]["alpha"]["laufzeit_ms"] = 4.6609
    tausch = {"_rauschtoleranz": {"alpha": 1.219, "beta": 1.15}}
    einzel = M.urteil_f2(basis, kandidat, bestwert, ["alpha", "beta"], ["alpha"], tausch)
    assert einzel["grenzen_gerissen"] and "alpha.laufzeit_ms" in einzel["grenzen_gerissen"][0]   # Gegenprobe: alter Weg
    b2, k2 = M.laufzeit_einsetzen(basis, kandidat, {"n": 5, "regel": "x", "bereiche": {
        "alpha": {"basis": 4.80, "kandidat": 4.6609, "basis_werte": [4.8] * 5, "kandidat_werte": [4.66] * 5}}})
    gepaart = M.urteil_f2(b2, k2, bestwert, ["alpha", "beta"], ["alpha"], tausch)
    assert gepaart["grenzen_gerissen"] == [] and gepaart["laufzeit_bezug"].startswith("gepaart")


def test_1_gepaart_reisst_eine_echte_verschlechterung_weiterhin(messung):
    """Gegenprobe: gepaart heißt nicht nachsichtig — Kandidat 2× langsamer als die gepaarte Vorgeneration reißt."""
    basis, kandidat = messung(), messung()
    b2, k2 = M.laufzeit_einsetzen(basis, kandidat, {"n": 5, "regel": "x", "bereiche": {
        "alpha": {"basis": 5.0, "kandidat": 10.0, "basis_werte": [5.0] * 5, "kandidat_werte": [10.0] * 5}}})
    u = M.urteil_f2(b2, k2, basis, ["alpha", "beta"], ["alpha"], {"_rauschtoleranz": {"alpha": 1.2, "beta": 1.2}})
    assert u["ok"] is False and "alpha.laufzeit_ms: 10.000 > Grenze 6.000" in u["grund"], u["grund"]


def test_1_grenzanzeige_ohne_irrefuehrende_rundung(messung):
    """T3: „4.66 > Grenze 4.7“ — die Anzeige hatte eine Nachkommastelle. Jetzt drei."""
    bestwert, kandidat = messung(), messung()
    bestwert["bereiche"]["alpha"]["laufzeit_ms"] = 3.8216269999999213
    kandidat["bereiche"]["alpha"]["laufzeit_ms"] = 4.660906999999952
    g = M.grenzen_f2(bestwert, kandidat, ["alpha"], {}, kernmassgewinn=False, rauschtoleranz={"alpha": 1.219})
    assert g == [] or "4.661 > Grenze 4.659" in g[0], g
    assert g and "Grenze 4.7 " not in g[0]


@pytest.mark.parametrize("u,nische,erwartet", [
    ({"zuwachs": 0, "grund": "x", "pareto_schlechter": [], "grenzen_gerissen": []}, "schnell", True),
    ({"zuwachs": 0, "grund": "x", "pareto_schlechter": [], "grenzen_gerissen": []}, "sicher", False),
    ({"zuwachs": 2, "grund": "x", "pareto_schlechter": [], "grenzen_gerissen": []}, "sicher", True),
    ({"zuwachs": 2, "grund": "Pareto verletzt", "pareto_schlechter": ["a"], "grenzen_gerissen": []}, "sicher", False),
    ({"zuwachs": 2, "grund": "x", "pareto_schlechter": [], "grenzen_gerissen": ["alpha.groesste_funktion"]}, "sicher", False),
    ({"zuwachs": 0, "grund": "x", "pareto_schlechter": [], "grenzen_gerissen": []}, "werk", True),
])
def test_1_laufzeit_wird_nur_gemessen_wo_sie_entscheidet(u, nische, erwartet):
    assert M.laufzeit_entscheidet(u, nische) is erwartet


def test_1_gepaarte_messung_wechselt_die_reihenfolge_und_bildet_median(monkeypatch):
    folge = []
    werte = {"basis": iter([10, 50, 11, 12, 13]), "kandidat": iter([7, 8, 90, 9, 7.5])}

    def messen(werk, bereiche, paket, ref, dateien, zeitlimit_s=150):
        seite = "kandidat" if dateien else "basis"
        folge.append(seite)
        return {"gueltig": True, "grund": "", "bereiche": {"alpha": {"laufzeit_ms": next(werte[seite])}}}
    monkeypatch.setattr(M, "laufzeit_messen", messen)
    r = M.laufzeit_gepaart("/w", ["alpha"], "src", "last", {}, {"src/a.ts": "x"}, n=5)
    assert folge[:4] == ["basis", "kandidat", "kandidat", "basis"]          # abwechselnd, nicht blockweise
    assert r["bereiche"]["alpha"]["basis"] == 12 and r["bereiche"]["alpha"]["kandidat"] == 8   # Median, Ausreißer egal


def test_1_messausfall_ist_kein_urteil(monkeypatch):
    monkeypatch.setattr(M, "laufzeit_messen", lambda *a, **k: {"gueltig": False, "grund": "Zeitlimit", "bereiche": {}})
    r = M.laufzeit_gepaart("/w", ["alpha"], "src", "last", {}, {"src/a.ts": "x"}, n=3)
    assert r["gueltig"] is False and r["seite"] == "basis" and "Zeitlimit" in r["grund"]


# ================================================================ 4. paar_bestanden
def test_4_paar_bestanden_verlangt_tragfaehigen_verhaltensvergleich():
    mass = {"ok": True, "grund": "Kernmaß -1 → 0", "kern_basis": -1, "kern_kandidat": 0, "zuwachs": 1,
            "pareto_schlechter": [], "grenzen_gerissen": []}
    u = {"status": "ueberlebt", "vertrag_verletzt": [], "mass": mass, "verhalten": {"tragfaehig": True, "geurteilt": True}}
    assert L.paar_bestanden(u) is True
    assert L.paar_bestanden({**u, "verhalten": {"tragfaehig": False, "geurteilt": True}}) is False
    assert L.paar_bestanden({**u, "status": aegis.ZURUECKGESTELLT}) is False


# ================================================================ 8. Kernmaß geeicht, roh gekennzeichnet
def test_8_kernmass_geeicht_und_roh_gekennzeichnet():
    m = {"gueltig": True, "belege": {"vitest": {}}, "kernmass": -11, "bereiche": {
        "zahlen": {"tests_bestanden": 5, "tests_fehlgeschlagen": 0, "sicherheit_punkte": 8, "tote_funktionen": 0,
                   "sicherheit_befunde": [{"test": "security/detect-object-injection", "punkte": 1}] * 8},
        "tarife": {"tests_bestanden": 5, "tests_fehlgeschlagen": 0, "sicherheit_punkte": 3, "tote_funktionen": 0,
                   "sicherheit_befunde": [{"test": "security/detect-object-injection", "punkte": 1}] * 3}}}
    g = masseichung.anwenden(m, {"sauberer_bereich": "zahlen", "stillgelegt": ["security/detect-object-injection"]})
    assert g["kernmass"] == 0 and g["kernmass_roh"] == -11 and g["kernmass_formel"] == "f2"
    assert L._kernmass_f2_roh(g) == -11 and M.kernmass_f2(g) == 0


def test_8_gegenprobe_ohne_eichung_bleibt_das_kernmass_unberuehrt():
    m = {"gueltig": True, "kernmass": -3, "bereiche": {"a": {"tests_bestanden": 0, "tests_fehlgeschlagen": 0,
                                                             "sicherheit_punkte": 3, "tote_funktionen": 0, "sicherheit_befunde": []}}}
    assert masseichung.anwenden(m, None) is m and "kernmass_roh" not in m


# ================================================================ 10. Gedächtnissperre nur bei berührtem Bereich
import difflib  # noqa: E402

PRUEFEN_ALT = ("export function pruefe(liste: string[]): number {\n  let doppelt = 0;\n"
               "  for (let i = 0; i < liste.length; i++) {\n    for (let j = 0; j < i; j++) {\n"
               "      if (liste[i] === liste[j]) doppelt++;\n    }\n  }\n  return doppelt;\n}\n")
PRUEFEN_NEU = ("export function pruefe(liste: string[]): number {\n  const gesehen = new Set<string>();\n  let doppelt = 0;\n"
               "  for (const kennung of liste) {\n    if (gesehen.has(kennung)) doppelt++;\n    gesehen.add(kennung);\n  }\n"
               "  return doppelt;\n}\n")
DIFF_PLANUNG = "".join(difflib.unified_diff(PRUEFEN_ALT.splitlines(True), PRUEFEN_NEU.splitlines(True),
                                            "a/src/planung/pruefen.ts", "b/src/planung/pruefen.ts"))


@pytest.mark.parametrize("grund,erwartet", [
    ("Grenzmaß gerissen: tarife.laufzeit_ms: 6.414 > Grenze 5.945 (Bestwert 5.169 × 1.150)", False),        # unberührt
    ("Grenzmaß gerissen: planung.laufzeit_ms: 12.000 > Grenze 10.000 (Bestwert 8.000 × 1.250)", False),      # berührt, nicht gepaart
    ("Grenzmaß gerissen: planung.laufzeit_ms: 12.000 > Grenze 10.000 (Vorgeneration gepaart, Median aus 5 8.000 × 1.250)", True),
    ("Grenzmaß gerissen: tarife.laufzeit_ms: 9.000 > Grenze 6.000 (Vorgeneration gepaart, Median aus 5 5.000 × 1.200)", False),
    ("Grenzmaß gerissen: planung.groesste_funktion: 80 > Grenze 60", True),                                    # kein Laufzeitriss
])
def test_10_laufzeitriss_sperrt_nur_beruehrt_und_gepaart(grund, erwartet):
    assert gedaechtnis.laufzeit_sperrt(grund, DIFF_PLANUNG) is erwartet


def _gedaechtnis_werk(tmp_path):
    con = datenbank.verbinden(tmp_path / "g.db")
    (tmp_path / "src" / "planung").mkdir(parents=True)
    (tmp_path / "src" / "planung" / "pruefen.ts").write_text(PRUEFEN_ALT)
    con.execute("INSERT INTO werke(id,name,pfad,bericht,status) VALUES(1,'w',?,?,?)", (str(tmp_path), datenbank.j({"paket": "src"}), "x"))
    con.execute("INSERT INTO laeufe(id,werk_id,budget_eur,status) VALUES(1,1,1,'laeuft')")
    return con


@pytest.mark.parametrize("grund,sperrt", [
    # T3 K3242: Riss in `tarife`, Diff ändert nur `planung` — darf später gleiche Kandidaten nicht sperren
    ("Grenzmaß gerissen: tarife.laufzeit_ms: 6.414 > Grenze 5.945 (Bestwert 5.169 × 1.150)", False),
    ("Grenzmaß gerissen: planung.laufzeit_ms: 12.000 > Grenze 10.000 (Bestwert 8.000 × 1.250)", False),
    # Gegenprobe: berührt UND gepaart bestätigt — sperrt (derselbe Diff, derselbe Laufweg)
    ("Grenzmaß gerissen: planung.laufzeit_ms: 12.000 > Grenze 10.000 (Vorgeneration gepaart, Median aus 5 8.000 × 1.250)", True),
    # Gegenprobe: eine andere Ablehnungsart sperrt wie bisher
    ("Kernmaß unverändert (0 → 0); bestandene Tests zählen nicht", True),
])
def test_10_sperre_am_laufweg_projekt_merken_und_wiederholung(tmp_path, grund, sperrt, ts_kammer):
    """Durch projekt_merken + wiederholung, die Funktionen, die der Lauf ruft (lauf._generation_koerper)."""
    con = _gedaechtnis_werk(tmp_path)
    neu = {"src/planung/pruefen.ts": PRUEFEN_NEU}
    con.execute("INSERT INTO kandidaten(id,lauf_id,generation,bereich,nische,diff,status,grund) VALUES(1,1,1,'planung','schnell',?,'abgelehnt',?)",
                (DIFF_PLANUNG, grund))
    gedaechtnis.projekt_merken(con, 1, 1, 1, tmp_path, neu)
    w = gedaechtnis.wiederholung(con, 1, "planung", tmp_path, DIFF_PLANUNG, neu, 1)
    assert (w is not None) is sperrt, (grund, w, [dict(r) for r in con.execute("SELECT grundklasse, funktionen FROM projektgedaechtnis")])
    assert con.execute("SELECT COUNT(*) FROM projektgedaechtnis").fetchone()[0] == 1   # immer gemerkt, sichtbar


# ================================================================ 11a. Erreichbarkeitsführung
def _db(tmp_path):
    con = datenbank.verbinden(tmp_path / "n.db")
    return con


def test_11_gedrosselter_anbieter_wird_ausgesetzt_bandit_bleibt(tmp_path):
    con = _db(tmp_path)
    for _ in range(nischen.AUSSETZEN_NACH):
        protokoll.schreiben(con, "anbieter.gedrosselt", lauf_id=7, modell="qwen/qwen3.8-flash", hersteller="qwen", fehler="HTTP 429")
    assert "qwen" in nischen.ausgesetzt(con, 7)
    for _ in range(20):
        gew = [h for h, _ in nischen.waehlen(con, 7, "sicher")]
        assert "qwen" not in gew and len(gew) == 2
    assert con.execute("SELECT COUNT(*) FROM bandit").fetchone()[0] == 0          # Bandit unberührt


def test_11_gegenprobe_antwort_beendet_die_folge_und_zeit_laeuft_ab(tmp_path):
    con = _db(tmp_path)
    for _ in range(nischen.AUSSETZEN_NACH - 1):
        protokoll.schreiben(con, "anbieter.gedrosselt", lauf_id=7, modell="qwen/qwen3.8-flash", hersteller="qwen", fehler="HTTP 429")
    protokoll.schreiben(con, "modell.antwort", lauf_id=7, modell="qwen/qwen3.8-flash")
    protokoll.schreiben(con, "anbieter.gedrosselt", lauf_id=7, modell="qwen/qwen3.8-flash", hersteller="qwen", fehler="HTTP 429")
    assert nischen.ausgesetzt(con, 7) == {}                                         # Folge unterbrochen
    for _ in range(nischen.AUSSETZEN_NACH):
        protokoll.schreiben(con, "anbieter.gedrosselt", lauf_id=7, modell="qwen/qwen3.8-flash", hersteller="qwen", fehler="HTTP 429")
    spaeter = (datetime.now(timezone.utc) + timedelta(minutes=nischen.AUSSETZEN_MINUTEN + 1)).isoformat(timespec="milliseconds")
    assert nischen.ausgesetzt(con, 7, jetzt=spaeter) == {}                          # Zeit abgelaufen
    assert nischen.ausgesetzt(con, 8) == {}                                         # anderer Lauf


def test_11_drosselung_ist_nicht_ablehnung():
    assert ist_drosselung(AnbieterFehler("x: HTTP 429 temporarily rate-limited upstream"))
    assert not ist_drosselung(AnbieterFehler("x: ablehnung — kein nutzbarer Beitrag", ausfallart="ablehnung"))
    assert not ist_drosselung(AnbieterFehler("x: HTTP 500 interner Fehler"))


# ================================================================ 11b. _beschleunigen entfernt
def test_11_beschleunigen_ist_entfernt():
    from biotop.organe import eichproben
    assert not hasattr(eichproben, "_beschleunigen")



# ================================================================ 6. Generation 0: nicht gemessen je Durchlauf
def _g0_con(tmp_path):
    from biotop.organe import generation0 as G0
    con = datenbank.verbinden(tmp_path / "g0.db")
    G0.zaehlkontext_setzen(con, 1)
    return con, G0


@pytest.mark.parametrize("neutral_anzahl,gemessen", [(3, False), (2, True), (0, True)])
def test_6_durchlauf_ueberwiegend_neutral_heisst_nicht_gemessen(tmp_path, monkeypatch, neutral_anzahl, gemessen):
    """Durch G0.messen — die Funktion, die lauf.generation0 je Durchlauf ruft. T3 Lauf 37: 100 von 100 neutral
    (Typbau gebrochen) wurden als „0 von 100 gefangen“ gebucht und lösten Tests für alle 100 Mutanten aus."""
    con, G0 = _g0_con(tmp_path)
    urteile = iter([{"gefangen": False, "neutral": True, "grund": "typbau_nicht_bestanden", "von": "x"}] * neutral_anzahl
                   + [{"gefangen": True, "neutral": False, "grund": None, "von": "t"}] * (4 - neutral_anzahl))
    monkeypatch.setattr(G0, "_testlauf_urteil", lambda werk, dateien: next(urteile))
    mut = [{"datei": "src/a/x.ts", "zeile": 1, "art": "a", "beschreibung": "b", "code": "c"} for _ in range(4)]
    if gemessen:
        r = G0.messen(con, 1, 1, tmp_path, mut, "vorher")
        assert r["neutral"] == neutral_anzahl and r["gefangen"] == 4 - neutral_anzahl
    else:
        with pytest.raises(G0.NichtGemessen, match="3 von 4 Mutantenläufen neutral"):
            G0.messen(con, 1, 1, tmp_path, mut, "vorher")
        z = [json.loads(r[0]) for r in con.execute("SELECT inhalt FROM protokoll WHERE art='generation0.nicht_gemessen'")]
        assert z and z[0]["neutral"] == 3


def test_6_tsc_meldung_wird_im_neutralfall_gespeichert(tmp_path, monkeypatch):
    con, G0 = _g0_con(tmp_path)
    from biotop.kern import sprachprofil, typescript
    monkeypatch.setattr(sprachprofil, "ist_typescript", lambda w: True)
    monkeypatch.setattr(typescript, "baulauf", lambda w, d=None: {"gueltig": True, "baut": False, "prozess": {
        "stdout": "tests/x.test.ts(4,9): error TS2322: Type 'string[]' is not assignable to type 'number[]'.\n"}})
    r = G0._testlauf_urteil(tmp_path, {})
    assert r["neutral"] is True and "TS2322" in r["von"]
    e = con.execute("SELECT einzelheit FROM neutralzaehler WHERE organ='generation0._testlauf'").fetchone()[0]
    assert "TS2322" in e and "tests/x.test.ts(4,9)" in e


@pytest.mark.parametrize("baut,aufgenommen", [(False, False), (True, True)])
def test_6_testkandidat_der_den_typbau_bricht_wird_nicht_aufgenommen(tmp_path, monkeypatch, baut, aufgenommen):
    """Durch G0._tests_typescript (der Testbau, den lauf.generation0 ruft). Gegenprobe: baut der Typbau, wird der Test
    aufgenommen — die Prüfung sperrt nicht pauschal."""
    con, G0 = _g0_con(tmp_path)
    from biotop.kern import typescript
    w = tmp_path / "werk"
    (w / "src" / "a").mkdir(parents=True)
    (w / "tests").mkdir()
    (w / "package.json").write_text('{"type":"module"}')
    (w / "src" / "a" / "wert.ts").write_text("export function wert(): number { return 2; }\n")

    class Antwort:
        text = "```typescript\nimport {test,expect} from 'vitest';\ntest('t', () => { expect(1).toBe(1); });\n```"
    monkeypatch.setattr(G0, "aufrufen", lambda *a, **k: Antwort())
    monkeypatch.setattr(G0.nischen, "waehlen", lambda *a, **k: [("qwen", "qwen/qwen3.8-flash")])
    monkeypatch.setattr(G0.nischen, "buchen", lambda *a, **k: None)
    monkeypatch.setattr(typescript, "testlauf", lambda werk, dateien=None, tests=None: {
        "gueltig": True, "faelle": {"tests/t.test.ts::t": {"ok": "src/a/wert.ts" not in (dateien or {}), "bestaetigt": True}}})
    monkeypatch.setattr(typescript, "baulauf", lambda werk, dateien=None: {"gueltig": True, "baut": baut, "prozess": {"stdout": "error TS1: x"}})
    m = {"datei": "src/a/wert.ts", "zeile": 1, "art": "zahl", "beschreibung": "2 → 3", "code": "export function wert(): number { return 3; }\n"}
    r = G0._tests_typescript(con, 1, 1, w, "src", [m], {id(m): 1})
    assert bool(r["neue_tests"]) is aufgenommen, r
    typbau = con.execute("SELECT COUNT(*) FROM protokoll WHERE art='generation0.testkandidat_typbau'").fetchone()[0]
    assert (typbau > 0) is (not baut)


# ================================================================ 9. Immunisierung auf dem TypeScript-Pfad
ALT_TS = "import { test, expect } from 'vitest';\nimport { plus } from '../src/beta/wert.js';\n\ntest('test_alt', () => {\n  expect(plus(1, 1)).toBe(2);\n});\n"
NEU_TS = ("import { test, expect } from 'vitest';\nimport { plus } from '../src/beta/wert.js';\nimport { halb } from '../src/beta/wert.js';\n\n"
          "test('test_alt', () => {\n  expect(plus(1, 1)).toBe(2);\n});\n\ntest('test_neu', () => {\n  expect(halb(4)).toBe(2);\n});\n")


def test_9_anhaengen_auf_dem_typescript_pfad_haengt_an_und_zaehlt(tmp_path, monkeypatch, ts_kammer):
    """T3: 0 von 0 Fällen, jeder TS-Aufruf endete neutral 'typescript_eigene_datei'. Jetzt echt angehängt (Kammer)."""
    from biotop.kern import typescript
    from biotop.organe import neutralzaehler
    con = datenbank.verbinden(tmp_path / "a.db")
    monkeypatch.setattr(aegis, "_zaehlkontext", lambda: (con, 9))
    g = aegis._anhaengen(ALT_TS, NEU_TS, {"test_neu"})
    assert g is not None and g.startswith(ALT_TS.split("\n\ntest(")[0])
    assert {t["name"] for t in typescript.testfunktionen(g)} == {"test_alt", "test_neu"}
    assert "import { halb }" in g and g.count("import { plus }") == 1
    assert neutralzaehler.stand(con, 9)["aegis._anhaengen"]["geurteilt"] == 1
    # Gegenprobe: nichts Neues zu behalten → nichts angehängt, neutral gezählt
    assert aegis._anhaengen(ALT_TS, NEU_TS, {"test_alt"}) is None
    assert neutralzaehler.stand(con, 9)["aegis._anhaengen"]["neutral"] == 1


# ================================================================ Entscheidung Chat-Claude: geeicht lesen
def test_geeicht_lesen_befundklassen_nur_aus_geeichter_messung(tmp_path, monkeypatch):
    """aegis.pruefen bildet die Befundklassen (und damit die Wahl des schweren Angriffsmodells) aus der geeichten
    Vorgeneration. Gegenprobe: ohne Eichung erscheint die Regel."""
    basis = {"bereiche": {"zahlen": {"sicherheit_punkte": 1, "sicherheit_befunde": [
        {"test": "security/detect-object-injection", "punkte": 1, "schwere": "LOW"}]}}}
    eich = {"sauberer_bereich": "zahlen", "stillgelegt": ["security/detect-object-injection"]}
    g = masseichung.anwenden(basis, eich)
    assert sorted({b["test"] for b in g["bereiche"]["zahlen"]["sicherheit_befunde"]}) == []
    assert sorted({b["test"] for b in masseichung.anwenden(basis, None)["bereiche"]["zahlen"]["sicherheit_befunde"]}) == \
        ["security/detect-object-injection"]
    import inspect
    quelle = inspect.getsource(aegis.pruefen)
    assert "basis_g = masseichung.anwenden(basis" in quelle and "befundklassen_tests(con, werk_id, b_, basis_g)" in quelle
    assert "basis_g = masseichung.anwenden(basis" in inspect.getsource(L._generation_koerper)



# ================================================================ Befundklassen auch für den Bereich des Nachbarn
def test_befundklassen_tests_fuer_jeden_geaenderten_bereich(monkeypatch):
    """aegis.pruefen legt Befundklassen-Immuntests für jeden Bereich an, dessen Quelltext der Kandidat (einschließlich
    der Anpassung des Nachbarn) ändert — nicht nur für den eigenen. Geprüft am Quelltext des Annahmepfads und an der
    Auswahl der Bereiche; die Wirkung zeigt das Nachspiel K2867+K2868 (Lauf 37) durch aegis.pruefen."""
    import inspect
    quelle = inspect.getsource(aegis.pruefen)
    assert 'for b_ in sorted({bereich} | {p.split("/")[1] for p in code' in quelle
    assert "bk.update(befundklassen_tests(con, werk_id, b_, basis_g))" in quelle
    code = {"src/zahlen/geld.ts": "x", "src/tarife/ausdruck.ts": "y", "tests/test_x.test.ts": "z"}
    bereiche = sorted({"zahlen"} | {p.split("/")[1] for p in code if p.startswith("src/") and p.count("/") >= 2})
    assert bereiche == ["tarife", "zahlen"]



# ================================================================ 3. Sondenausfall am Laufweg (aegis.pruefen)
def _pruefen_bis_zur_sonde(tmp_path, monkeypatch, beobachtung, basis_gueltig=True, laufzeit_gueltig=True):
    """aegis.pruefen — die Funktion, die ein Lauf zur Annahme ruft — mit gestellten Außenwirkungen: Modell (kein
    Angriff), Messgerät (beide Seiten gültig, Kernmaß +1), Kammer der Verhaltenssonde (`beobachten`). Gestellt ist die
    GRENZE, die das Organ überquert (Kammer), nie das Organ selbst."""
    import sqlite3 as _sql
    from types import SimpleNamespace
    from biotop.organe import verhaltensvergleich as vv
    con = _sql.connect(":memory:", isolation_level=None)
    con.row_factory = _sql.Row
    con.executescript(datenbank.SCHEMA)
    w = tmp_path / "w"
    (w / "src" / "alpha").mkdir(parents=True)
    (w / "package.json").write_text('{"type":"module"}')
    (w / "src" / "alpha" / "a.ts").write_text("export function a(x: number): number {\n  return x;\n}\n")
    diff = ("--- a/src/alpha/a.ts\n+++ b/src/alpha/a.ts\n@@ -1,3 +1,3 @@\n export function a(x: number): number {\n"
            "-  return x;\n+  return x + 0;\n }\n")
    con.execute("INSERT INTO kandidaten(id,lauf_id,generation,bereich,nische,status,diff) VALUES(7,1,1,'alpha','sicher','erzeugt',?)", (diff,))
    monkeypatch.setattr(aegis, "aufrufen", lambda *a, **k: SimpleNamespace(text="KEIN ANGRIFF"))

    def messen(werk, bereiche, paket, ref, dateien=None, **k):
        kand = any(p.startswith("src/") for p in (dateien or {}))
        if not kand and not basis_gueltig and dateien is not None:
            return {"gueltig": False, "grund": "Kammer abgebrochen (rc=137)", "rc": 137}
        return {"gueltig": True, "kernmass": 0, "werk": {"baut": True, "zyklen": 0, "bauzeit_ms": 100,
                "tests_fehlgeschlagen_liste": [], "tests_fehlgeschlagen_ids": []},
                "bereiche": {"alpha": {"tests_bestanden": 1, "tests_fehlgeschlagen": 0, "sicherheit_punkte": 0,
                                       "sicherheit_befunde": [], "tote_funktionen": 0 if kand else 1,
                                       "laufzeit_ms": None, "groesste_funktion": 3}}}
    monkeypatch.setattr(aegis.messgeraet, "messen", messen)
    # Grenze Kammer auch für die gepaarte Laufzeit: beide Seiten gleich schnell (die Laufzeit entscheidet hier nichts)
    monkeypatch.setattr(aegis.messgeraet, "laufzeit_messen",
                        lambda *a, **k: ({"gueltig": True, "grund": "", "bereiche": {"alpha": {"laufzeit_ms": 10.0}}} if laufzeit_gueltig
                                         else {"gueltig": False, "grund": "Zeitlimit", "bereiche": {}}))
    monkeypatch.setattr(vv, "beobachten", beobachtung)
    basis = messen(w, ["alpha"], "src", None)
    u = aegis.pruefen(con, 1, 1, 7, w, "src", ["alpha"], [], basis, basis, "// last", {})
    return con, u


def test_3_sondenausfall_am_laufweg_wird_zurueckgestellt_nicht_abgelehnt(tmp_path, monkeypatch):
    con, u = _pruefen_bis_zur_sonde(tmp_path, monkeypatch,
                                    lambda *a, **k: {"gueltig": False, "art": "infrastruktur", "grund": "Kammer: Zeitlimit 240 s"})
    assert u["status"] == aegis.ZURUECKGESTELLT and "Zeitlimit" in u["grund"], u["grund"]
    assert con.execute("SELECT status FROM kandidaten WHERE id=7").fetchone()[0] == aegis.ZURUECKGESTELLT


def test_3_gegenprobe_inhaltsbefund_am_kandidaten_bleibt_ablehnung(tmp_path, monkeypatch):
    seiten = iter([{"gueltig": True, "beobachtungen": {"alpha/a:a#0": "1"}, "eingewickelt": {"alpha/a": ["a"]},
                    "aufgerufen": {"alpha/a:a": 1}},
                   {"gueltig": False, "art": "inhalt", "grund": "Modul lädt nicht"}])
    con, u = _pruefen_bis_zur_sonde(tmp_path, monkeypatch, lambda *a, **k: next(seiten))
    assert u["status"] == "abgelehnt" and u["grund"].startswith("Verhaltensvergleich:"), u["grund"]



# ================================================================ Review vor T4 — Nachbesserungen mit Gegenprobe
def test_review1_pfeil_export_gilt_nicht_als_entfernt(tmp_path, monkeypatch):
    """Review Nr. 1: `export const f = () =>` wird nicht eingewickelt; bisher galt f am Kandidaten als entfernt und
    seine Randfälle standen einseitig als ungedeckte Abweichung. Jetzt aus den Beobachtungen beider Seiten bestimmt.
    Gestellt ist nur die Kammer (`beobachten`), `verhaltensvergleich.pruefen` läuft unverändert."""
    from biotop.organe import verhaltensvergleich as vv
    w = tmp_path / "w"
    (w / "src" / "alpha").mkdir(parents=True)
    (w / "package.json").write_text('{"type":"module"}')
    (w / "src" / "alpha" / "a.ts").write_text("export const f = (x: number): number => x;\nexport function g(x: number): number { return x; }\n")
    rand = {"alpha/a:f~rand#0": "1", "alpha/a:f~rand#0@alias": "1", "alpha/a:g~rand#0": "2"}
    seite = {"gueltig": True, "beobachtungen": rand, "eingewickelt": {"alpha/a": ["g"]},
             "signaturen": {"alpha/a": {"f": ["number"], "g": ["number"]}}, "aufgerufen": {}}
    seiten = iter([dict(seite), dict(seite)])
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: next(seiten))
    r = vv.pruefen(w, {"src/alpha/a.ts": "x"}, "last", ["alpha"], {})
    assert r["tragfaehig"] is True and r["entfernte_funktionen"] == [] and r["beobachtete_funktionen"] == "2 von 2", r


def test_review1_gegenprobe_wirklich_entfernte_funktion_wird_ausgewiesen_nicht_abgelehnt(tmp_path, monkeypatch):
    from biotop.organe import verhaltensvergleich as vv
    w = tmp_path / "w"
    (w / "src" / "alpha").mkdir(parents=True)
    (w / "package.json").write_text('{"type":"module"}')
    (w / "src" / "alpha" / "a.ts").write_text("export function f(x: number): number { return x; }\nexport function g(x: number): number { return x; }\n")
    alt = {"gueltig": True, "beobachtungen": {"alpha/a:f~rand#0": "1", "alpha/a:g~rand#0": "2"},
           "eingewickelt": {"alpha/a": ["f", "g"]}, "signaturen": {"alpha/a": {"f": ["number"], "g": ["number"]}}}
    neu = {"gueltig": True, "beobachtungen": {"alpha/a:g~rand#0": "2"}, "eingewickelt": {"alpha/a": ["g"]}}
    seiten = iter([alt, neu])
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: next(seiten))
    r = vv.pruefen(w, {"src/alpha/a.ts": "x"}, "last", ["alpha"], {})
    assert r["tragfaehig"] is True and r["entfernte_funktionen"] == ["alpha/a:f"] and r["beobachtete_funktionen"] == "1 von 1", r
    # und eine echte Änderung an g bleibt eine ungedeckte Abweichung
    neu2 = dict(neu, beobachtungen={"alpha/a:g~rand#0": "3"})
    seiten = iter([alt, neu2])
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: next(seiten))
    assert vv.pruefen(w, {"src/alpha/a.ts": "x"}, "last", ["alpha"], {})["tragfaehig"] is False


ALT_PLUS = "import { test, expect } from 'vitest';\nimport { plus } from '../src/beta/wert.js';\n\ntest('test_alt', () => {\n  expect(plus(1, 1)).toBe(2);\n});\n"


def test_review2_erweiterte_importzeile_ohne_doppelte_bindung(tmp_path, monkeypatch, ts_kammer):
    """Review Nr. 2: `import { plus, halb }` neben vorhandenem `import { plus }` ergab eine doppelte Bindung und wurde als
    geurteilt gezählt. Jetzt: nur halb kommt hinzu, die Datei hat jede Bindung genau einmal (Kammer-Parsing)."""
    from biotop.kern import typescript
    from biotop.organe import neutralzaehler
    con = datenbank.verbinden(tmp_path / "a.db")
    monkeypatch.setattr(aegis, "_zaehlkontext", lambda: (con, 9))
    neu = ("import { test, expect } from 'vitest';\nimport { plus, halb } from '../src/beta/wert.js';\n\n"
           "test('test_alt', () => {\n  expect(plus(1, 1)).toBe(2);\n});\n\ntest('test_neu', () => {\n  expect(halb(plus(2, 2))).toBe(2);\n});\n")
    g = aegis._anhaengen(ALT_PLUS, neu, {"test_neu"})
    assert g is not None, neutralzaehler.stand(con, 9)
    gebunden = aegis._gebundene_namen(g)
    assert sorted(gebunden) == sorted(set(gebunden)), gebunden            # keine Bindung doppelt
    assert {"plus", "halb", "test", "expect"} <= set(gebunden)
    assert {t["name"] for t in typescript.testfunktionen(g)} == {"test_alt", "test_neu"}
    assert neutralzaehler.stand(con, 9)["aegis._anhaengen"]["geurteilt"] == 1


def test_review2_gegenprobe_namenskonflikt_wird_nicht_angehaengt(tmp_path, monkeypatch, ts_kammer):
    """Derselbe Name aus einer anderen Quelle ist ein Konflikt: nichts angehängt, neutral gezählt."""
    from biotop.organe import neutralzaehler
    con = datenbank.verbinden(tmp_path / "a.db")
    monkeypatch.setattr(aegis, "_zaehlkontext", lambda: (con, 9))
    neu = ("import { test, expect } from 'vitest';\nimport { plus } from '../src/alpha/liste.js';\n\n"
           "test('test_neu', () => {\n  expect(plus(1, 1)).toBe(2);\n});\n")
    assert aegis._anhaengen(ALT_PLUS, neu, {"test_neu"}) is None
    assert neutralzaehler.stand(con, 9)["aegis._anhaengen"]["gruende"] == {"zusammenfuegen_gescheitert": 1}


def test_review12_kammerausfall_beim_anhaengen_ist_kein_syntaxfehler(tmp_path, monkeypatch):
    from biotop.kern import typescript
    con = datenbank.verbinden(tmp_path / "a.db")
    monkeypatch.setattr(aegis, "_zaehlkontext", lambda: (con, 9))

    def kaputt(code):
        raise typescript.TypeScriptFehler("Kammerabbruch: Zeitlimit")
    monkeypatch.setattr(typescript, "testfunktionen", kaputt)
    with pytest.raises(typescript.TypeScriptFehler, match="Kammerabbruch"):
        aegis._anhaengen(ALT_PLUS, ALT_PLUS, {"test_neu"})
    from biotop.organe import neutralzaehler
    assert "aegis._anhaengen" not in neutralzaehler.stand(con, 9)            # weder syntaxfehler noch sonst gezählt


# ---------------------------------------------------------------- Review Nr. 3: Zurückgestellte in der Generation
def _generation_mit(tmp_path, monkeypatch, status_je_kandidat):
    """lauf._generation_koerper — gestellt sind Schwarm (genesis.erzeugen) und Ankläger (aegis.pruefen) mit festen
    Urteilen; alles danach (Zusammenfassung, Entropie, Laufstatus) ist der echte Laufweg."""
    from biotop.organe import genesis
    con = datenbank.verbinden(tmp_path / "gen.db")
    (tmp_path / "werk").mkdir()
    con.execute("INSERT INTO werke(id,name,pfad,bericht,status) VALUES(1,'w',?,?,?)", (str(tmp_path / "werk"), datenbank.j({"paket": "src"}), "x"))
    con.execute("INSERT INTO laeufe(id,werk_id,budget_eur,status) VALUES(1,1,1,'laeuft')")
    zaehler = iter(range(1, 100))
    ids = []

    def erzeugen(*a, **k):
        kid = next(zaehler)
        con.execute("INSERT INTO kandidaten(id,lauf_id,generation,bereich,nische,modell,diff,status) VALUES(?,1,?,?,?,?,?,'erzeugt')",
                    (kid, a[3], a[6], k.get("nische"), "qwen/qwen3.8-flash", ""))
        ids.append(kid)
        return [kid] if kid <= len(status_je_kandidat) else []
    monkeypatch.setattr(genesis, "erzeugen", erzeugen)

    def pruefen(con_, lauf_id, werk_id, kid, *a, **k):
        st = status_je_kandidat[kid - 1]
        con.execute("UPDATE kandidaten SET status=?, grund=? WHERE id=?", (st, "gestellt: " + st, kid))
        return {"kandidat": kid, "status": st, "grund": "gestellt: " + st, "mass": {"zuwachs": 0}, "vertraege_benannt": ""}
    monkeypatch.setattr(aegis, "pruefen", pruefen)
    monkeypatch.setattr(L.gedaechtnis, "projekt_merken", lambda *a, **k: None)
    monkeypatch.setattr(L.gedaechtnis, "art_merken", lambda *a, **k: None)
    monkeypatch.setattr(L.gedaechtnis, "wiederholung", lambda *a, **k: None)
    basis = {"bereiche": {"alpha": {"sicherheit_befunde": [], "tests_bestanden": 1, "tests_fehlgeschlagen": 0,
                                    "sicherheit_punkte": 0, "tote_funktionen": 0, "laufzeit_ms": 1.0, "groesste_funktion": 1}}}
    for nummer in (1, 2):
        con.execute("INSERT INTO generationen(lauf_id,nummer,status,erstellt_am) VALUES(1,?,'laeuft','x')", (nummer,))
        r = L._generation_koerper(con, 1, nummer, {"id": 1, "name": "w"}, {"nischen": ["sicher"]}, "src", ["alpha"],
                                  tmp_path / "werk", None, basis, [], basis, {}, None)
        zaehler = iter(range(1, 100))                     # dieselben Urteile in der zweiten Generation
        ids.clear()
        con.execute("DELETE FROM kandidaten")
        if nummer == 1:
            erste = r
    return con, erste, r


def test_review3_ueberwiegend_zurueckgestellt_heisst_abgebrochen_und_danach_angehalten(tmp_path, monkeypatch):
    con, r1, r2 = _generation_mit(tmp_path, monkeypatch, [aegis.ZURUECKGESTELLT])
    assert r1["status"] == "abgebrochen" and "nicht gemessen" in r1["grund"], r1["grund"]
    assert "entropie" not in r1                                               # nicht mit 0 % in die Sättigung
    assert r2["status"] == "abgebrochen" and r2.get("angehalten")
    assert con.execute("SELECT status FROM laeufe WHERE id=1").fetchone()[0] == "angehalten"
    assert con.execute("SELECT COUNT(*) FROM bandit").fetchone()[0] == 0                         # kein Bandit


def test_review3_gegenprobe_echte_ablehnung_bleibt_abgelehnt(tmp_path, monkeypatch):
    con, r1, r2 = _generation_mit(tmp_path, monkeypatch, ["abgelehnt"])
    assert r1["status"] == "abgelehnt" and r1["grund"].startswith("kein Kandidat hat den Ankläger überlebt (0 von 1)")
    assert con.execute("SELECT status FROM laeufe WHERE id=1").fetchone()[0] in ("bereit", "gesaettigt")


# ---------------------------------------------------------------- Review Nr. 8c: Generation 0 Python
@pytest.mark.parametrize("rc,zeitlimit,neutral,gefangen", [(2, False, True, False), (5, False, True, False),
                                                          (1, False, False, True), (0, False, False, False),
                                                          (124, True, False, True)])
def test_review8c_python_pytest_rc_ausser_0_1_ist_neutral(tmp_path, monkeypatch, rc, zeitlimit, neutral, gefangen):
    from biotop.organe import generation0 as G0, kammer
    from biotop.kern import sprachprofil
    con = datenbank.verbinden(tmp_path / "g.db")
    G0.zaehlkontext_setzen(con, 1)
    monkeypatch.setattr(sprachprofil, "ist_typescript", lambda w: False)
    monkeypatch.setattr(kammer, "ausfuehren", lambda *a, **k: kammer.Ergebnis(rc, "", "", 1.0, zeitlimit, "x"))
    r = G0._testlauf_urteil(tmp_path, {})
    assert r["neutral"] is neutral and r["gefangen"] is gefangen, r


# ---------------------------------------------------------------- Review Nr. 9: Typbau zwischen den Runden (Laufweg)
@pytest.mark.parametrize("baut,erwartet_fehler", [(False, True), (True, False)])
def test_review9_rundenpruefung_in_lauf_generation0(tmp_path, monkeypatch, baut, erwartet_fehler):
    """Durch lauf.generation0 (Laufweg): Runde 1 schreibt einen neuen Test; bricht er den Typbau, wird die Ergänzung
    zurückgenommen und der Lauf hält mit Grund an; baut er, geht es weiter. Gestellt: Mutanten, Testbau (Modell),
    die Kammer (typescript.testlauf/baulauf) und die Mutantenmessung."""
    from biotop.organe import generation0 as G0
    from biotop.kern import typescript, sprachprofil
    con = datenbank.verbinden(tmp_path / "g.db")
    werk = tmp_path / "werk"
    (werk / "src" / "a").mkdir(parents=True)
    (werk / "tests").mkdir()
    con.execute("INSERT INTO werke(id,name,pfad,bericht,status) VALUES(1,'w',?,?,?)", (str(werk), datenbank.j({"paket": "src"}), "x"))
    con.execute("INSERT INTO laeufe(id,werk_id,budget_eur,status) VALUES(1,1,1,'bereit')")
    monkeypatch.setattr(L, "_vorspann_verlangen", lambda *a: {})
    monkeypatch.setattr(L.landkarte, "bereiche_finden", lambda *a: ["a"])
    monkeypatch.setattr(L, "_referenzlast", lambda *a: "// last")
    monkeypatch.setattr(sprachprofil, "ist_typescript", lambda w: True)
    m = {"datei": "src/a/x.ts", "zeile": 1, "art": "z", "beschreibung": "1 → 2", "code": "c"}
    mutanten = [m]
    monkeypatch.setattr(G0, "erzeugen", lambda *a, **k: mutanten)
    monkeypatch.setattr(G0, "aequivalenz_pruefen", lambda *a, **k: None)
    runden = iter([{"blind": [m], "gefangen": 0, "gesamt": 1, "nicht_aequivalent": 1, "neutral": 0}] +
                  [{"blind": [], "gefangen": 1, "gesamt": 1, "nicht_aequivalent": 1, "neutral": 0}] * 3)
    monkeypatch.setattr(G0, "messen", lambda *a, **k: next(runden))
    monkeypatch.setattr(G0, "tests_evolutionieren", lambda *a, **k: {"neue_tests": {"tests/test_a_gen0_m1.test.ts": "t"}})
    monkeypatch.setattr(typescript, "testlauf", lambda *a, **k: {"gueltig": True, "faelle": {"t::x": {"ok": True}}})
    monkeypatch.setattr(typescript, "baulauf", lambda *a, **k: {"gueltig": True, "baut": baut, "prozess": {"stdout": "x.test.ts(1,1): error TS2322: Typ"}})
    monkeypatch.setattr(L.lazarus, "sicherstellen_repo", lambda *a: None)
    monkeypatch.setattr(L.lazarus, "_git", lambda *a: "")
    if erwartet_fehler:
        with pytest.raises(L.LaufFehler, match="bricht den Typbau.*TS2322"):
            L.generation0(con, 1, None, 0.8)
        assert not (werk / "tests" / "test_a_gen0_m1.test.ts").exists()            # zurückgenommen
    else:
        r = L.generation0(con, 1, None, 0.8)
        assert r["neue_tests"] == ["tests/test_a_gen0_m1.test.ts"] and (werk / "tests" / "test_a_gen0_m1.test.ts").exists()


# ---------------------------------------------------------------- Review Nr. 11: Gedächtnissperre beim Lesen (Altbestand)
def test_review11_altbestand_grenzmass_laufzeit_sperrt_beim_lesen_nicht(tmp_path):
    """Durch gescheiterte_wege (Leseweg des Schwarms; wiederholung nutzt denselben Filter). Werkname = Paket (werkname())."""
    con = datenbank.verbinden(tmp_path / "g.db")
    con.execute("INSERT INTO werke(id,name,pfad,bericht,status) VALUES(1,'w',?,?,?)", (str(tmp_path), datenbank.j({"paket": "src"}), "x"))
    con.execute("INSERT INTO laeufe(id,werk_id,budget_eur,status) VALUES(1,1,1,'beendet')")
    gedaechtnis.tabellen(con)
    for kid, grund in ((1, "Grenzmaß gerissen: tarife.laufzeit_ms: 6.414 > Grenze 5.945 (Bestwert 5.169 × 1.150)"),   # Altbestand, unbestätigt
                       (2, "Grenzmaß gerissen: planung.groesste_funktion: 80 > Grenze 60")):                          # Gegenprobe: sperrt
        con.execute("INSERT INTO projektgedaechtnis(werk, werk_id, lauf_id, generation, kandidat_id, bereich, nische, dateien, "
                    "funktionen, ansatz, grund, grundklasse, begruendung, erstellt_am) VALUES('src',1,1,1,?,'planung','schnell',?,?,?,?,"
                    "'grenzmass','',?)", (kid, datenbank.j(["src/planung/pruefen.ts"]), datenbank.j(["src/planung/pruefen.ts::pruefe"]),
                                          datenbank.j(["gesehen", "set"]), grund, "x"))
    wege = gedaechtnis.gescheiterte_wege(con, 1, "planung")
    assert [w["grund"][:40] for w in wege] == ["Grenzmaß gerissen: planung.groesste_funk"]



# ---------------------------------------------------------------- Review Nr. 4: alle drei Ausfallarten durch aegis.pruefen
@pytest.mark.parametrize("art", ["vorgeneration", "laufzeit"])
def test_review4_messausfall_vorgeneration_und_laufzeit_zurueckgestellt(tmp_path, monkeypatch, art):
    ok = {"gueltig": True, "beobachtungen": {"alpha/a:a#0": "1"}, "eingewickelt": {"alpha/a": ["a"]}, "aufgerufen": {"alpha/a:a": 1}}
    con, u = _pruefen_bis_zur_sonde(tmp_path, monkeypatch, lambda *a, **k: dict(ok),
                                    basis_gueltig=(art != "vorgeneration"), laufzeit_gueltig=(art != "laufzeit"))
    assert u["status"] == aegis.ZURUECKGESTELLT, u["grund"]
    assert ("Kammer (Vorgeneration)" if art == "vorgeneration" else "Laufzeitmessung gepaart") in u["grund"], u["grund"]


def test_review4_gegenprobe_alles_gueltig_wird_geurteilt(tmp_path, monkeypatch):
    ok = {"gueltig": True, "beobachtungen": {"alpha/a:a#0": "1"}, "eingewickelt": {"alpha/a": ["a"]}, "aufgerufen": {"alpha/a:a": 1}}
    con, u = _pruefen_bis_zur_sonde(tmp_path, monkeypatch, lambda *a, **k: dict(ok))
    assert u["status"] == "ueberlebt", u["grund"]


# ---------------------------------------------------------------- Review Nr. 5: Nr. 4 durch lauf._verhandeln
@pytest.mark.parametrize("tragfaehig,bestanden", [(False, False), (True, True)])
def test_review5_verhandlung_am_laufweg(db_lauf, tmp_path, monkeypatch, messung, tragfaehig, bestanden):
    from biotop.organe import genesis, vertraege
    vertraege.einlegen(db_lauf, 1, tmp_path, {("alpha", "beta"): "def test_vertrag():\n assert True\n"}, "Unit")
    kid = db_lauf.execute("INSERT INTO kandidaten(lauf_id,generation,bereich,nische,status,diff,begruendung,vertraege) "
                          "VALUES(1,1,'alpha','wild','abgelehnt','d','b','test_vertrag_alpha_beta')").lastrowid
    aid = db_lauf.execute("INSERT INTO kandidaten(lauf_id,generation,bereich,nische,status,diff,begruendung,vertraege) "
                          "VALUES(1,1,'beta','sicher','erzeugt','e','b','test_vertrag_alpha_beta')").lastrowid
    monkeypatch.setattr(genesis, "erzeugen", lambda *a, **k: [aid])
    monkeypatch.setattr(L.aegis, "kandidat_dateien", lambda pfad, diff: {"paket/beta/x.py": "y = 1\n"})
    mass = {"ok": True, "grund": "Kernmaß -1 → 0 (+1)", "kern_basis": -1, "kern_kandidat": 0, "zuwachs": 1,
            "pareto_schlechter": [], "grenzen_gerissen": []}
    u2 = {"status": "ueberlebt" if tragfaehig else "abgelehnt", "grund": "gestellt", "mass": mass, "vertrag_verletzt": [],
          "verhalten": {"tragfaehig": tragfaehig, "geurteilt": True}}
    monkeypatch.setattr(L.aegis, "pruefen", lambda *a, **k: dict(u2))
    u = {"status": "abgelehnt", "grund": "Vertrag verletzt", "vertrag_verletzt": [],
         "vertrag_dateien": ["tests/vertraege/test_vertrag_alpha_beta.py"]}
    r = L._verhandeln(db_lauf, 1, {"id": 1}, 1, tmp_path, "paket", ["alpha", "beta"], [], messung(), messung(), None, {}, "alpha", kid, u)
    arten = [z[0] for z in db_lauf.execute("SELECT art FROM protokoll WHERE art LIKE 'verhandlung.%'")]
    assert ("verhandlung.bestanden" in arten) is bestanden and ("verhandlung.gescheitert" in arten) is (not bestanden), arten
    assert (r["status"] == "abgelehnt") is (not bestanden)


# ---------------------------------------------------------------- Review Nr. 5: Nr. 9 Behauptungen aller Angriffstests (aegis.pruefen)
def test_review5_behauptungen_aller_angriffstests_am_laufweg(tmp_path, monkeypatch):
    import sqlite3 as _sql
    from types import SimpleNamespace
    con = _sql.connect(":memory:", isolation_level=None)
    con.row_factory = _sql.Row
    con.executescript(datenbank.SCHEMA)
    p = tmp_path / "paket" / "bereich" / "quelle.py"
    p.parent.mkdir(parents=True)
    p.write_text("def wert():\n    return 1\n")
    diff = "--- a/paket/bereich/quelle.py\n+++ b/paket/bereich/quelle.py\n@@ -1,2 +1,2 @@\n def wert():\n-    return 1\n+    return 2\n"
    con.execute("INSERT INTO kandidaten(id,lauf_id,generation,bereich,nische,status,diff) VALUES(7,1,1,'bereich','test','erzeugt',?)", (diff,))
    code = ("from paket.bereich.quelle import wert\n\ndef test_a():\n    assert wert() == 1\n\n"
            "def test_b():\n    assert wert() > 0\n")
    replies = iter(["wert|Eq:zahl", f"```python\n{code}```"])
    monkeypatch.setattr(aegis, "aufrufen", lambda *a, **k: SimpleNamespace(text=next(replies)))

    def junit(werk, paket, dateien, testdateien):
        kand = "paket/bereich/quelle.py" in dateien
        out = {}
        for t in testdateien:
            out[f"{t}::test_a"] = ({"ok": False, "bestaetigt": True, "ort": "paket/bereich/quelle.py", "meldung": "ValueError"}
                                   if kand else {"ok": True, "bestaetigt": False, "ort": "", "meldung": ""})
            out[f"{t}::test_b"] = {"ok": True, "bestaetigt": False, "ort": "", "meldung": ""}
        return out
    monkeypatch.setattr(aegis, "junit_lauf", junit)
    monkeypatch.setattr(aegis.messgeraet, "messen", lambda *a, **k: {"gueltig": False, "grund": "Test-Endpunkt"})
    aegis.pruefen(con, 1, 1, 7, tmp_path, "paket", ["bereich"], [], {"bereiche": {"bereich": {}}}, {}, None, None)
    import json as _j
    u = _j.loads(con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil' ORDER BY nr DESC LIMIT 1").fetchone()[0])
    assert sorted(u["behauptungen"]) == ["test_a", "test_b"], u["behauptungen"]         # ALLE erzeugten Tests
    assert u["behauptungen_treffer"] == ["test_a"]                                         # Gegenprobe: Treffer getrennt


# ---------------------------------------------------------------- Review Nr. 5: Nr. 11 Schreiber und Leser zusammen
@pytest.mark.parametrize("fehler,ausgesetzt", [("qwen/qwen3.8-flash: HTTP 429 b'temporarily rate-limited upstream'", True),
                                              ("qwen/qwen3.8-flash: ablehnung — kein nutzbarer Beitrag", False)])
def test_review5_drosselung_von_aufrufen_bis_waehlen(tmp_path, monkeypatch, fehler, ausgesetzt):
    """anbieter.aufrufen (Schreiber, gestellt ist nur der Adapter und die Kasse) → nischen.ausgesetzt/waehlen (Leser)."""
    from biotop import anbieter
    from biotop.kern import kasse
    con = datenbank.verbinden(tmp_path / "d.db")

    class Adapter:
        _melder = None

        def senden(self, *a, **k):
            raise AnbieterFehler(fehler, ausfallart="ablehnung" if "ablehnung" in fehler else "infrastruktur")
    monkeypatch.setattr(anbieter, "adapter", lambda name: Adapter())
    monkeypatch.setattr(kasse, "vorpruefung", lambda *a, **k: 0.0)
    for _ in range(nischen.AUSSETZEN_NACH):
        with pytest.raises(AnbieterFehler):
            anbieter.aufrufen(con, 5, "openrouter", "qwen/qwen3.8-flash", "s", "n", zweck="schwarm.sicher.alpha.gen1")
    assert ("qwen" in nischen.ausgesetzt(con, 5)) is ausgesetzt
    gewaehlt = {h for _ in range(15) for h, _m in nischen.waehlen(con, 5, "sicher")}
    assert ("qwen" not in gewaehlt) is ausgesetzt


# ---------------------------------------------------------------- Review Nr. 5: Nr. 11 Rohwerte der Rauschmessung
def test_review5_rauschmessung_speichert_rohwerte_in_messreihenfolge(db_lauf, monkeypatch):
    from biotop.organe import eichung
    folge = [1.0, 1.2, 0.9, 1.1, 1.05]
    werte = iter(folge)
    monkeypatch.setattr(eichung, "_messen_einmal", lambda *a: {"alpha": next(werte)})
    eichung.rauschmessung(db_lauf, 1, 1, __import__("pathlib").Path("."), ["alpha"], "paket", "# Last")
    import json as _j
    z = _j.loads(db_lauf.execute("SELECT inhalt FROM protokoll WHERE art='eichung.rauschmessung'").fetchone()[0])
    assert z["rohwerte"]["alpha"] == folge                                        # ungerundet, in Messreihenfolge
    assert z["bereiche"]["alpha"]["werte"] != folge                               # Gegenprobe: `werte` ist sortiert
