"""Behebungsrunde 2 vor T4 — Laufweg-Tests (tests/test_vor_t4_02.py). Probe und Gegenprobe je Punkt des Auftrags.

1. Python-Sonde am Python-Prüfwerk (speicherwerk) DURCH aegis.pruefen, echte Kammer (biotop-kammer:1):
   eingebauter Zwischenspeicher-Fehler scheitert („Verhaltensvergleich: … @mutation …“); derselbe Speicher am Inhalt
   überlebt; die Weißraum-Änderung scheitert an einer Formvariante (~form). Gestellt: Modell (KEIN ANGRIFF), sonst nichts.
2. Deckung je Abweichung durch verhaltensvergleich.pruefen: ein Test, der die Funktion mit derselben Eingabe ruft und
   dasselbe Ergebnis bekommt, deckt genau diese Abweichung — nicht die Nachbarabweichung derselben Funktion.
3. Bestätigungsmessung vor jeder Laufzeitablehnung durch aegis.pruefen: ein Riss, den die Nachmessung nicht bestätigt,
   lehnt nicht ab; ein bestätigter lehnt ab; eine ungültige Nachmessung stellt zurück.
4. Gepaarte Messung mit fehlenden Werten ist ungültig (die rote Spezifikation aus laeufe/biotop-vor-t4/spez/, übernommen).
"""
import json
import sqlite3
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from biotop.kern import datenbank, messgeraet
from biotop.organe import aegis, kammer
from biotop.organe import verhaltensvergleich as vv

sys.path.insert(0, str(Path(__file__).parent))
import speicherwerk as SW  # noqa: E402


# ================================================================ 4. Rote Spezifikation Teilausfall (übernommen, jetzt grün)
def test_teilausfall_kandidat_ist_messgeraetausfall(monkeypatch):
    """Aus laeufe/biotop-vor-t4/spez/test_spez_laufzeit_gepaart_teilausfall.py (an 330b4ec rot)."""
    def messen(werk, bereiche, paket, ref, dateien, zeitlimit_s=150):
        kand = dateien is not None
        return {"gueltig": True, "grund": "", "bereiche": {
            "a": {"laufzeit_ms": 1.0}, "b": ({"laufzeit_ms": None, "laufzeit_fehler": "SyntaxError"} if kand else {"laufzeit_ms": 2.0})}}
    monkeypatch.setattr(messgeraet, "laufzeit_messen", messen)
    r = messgeraet.laufzeit_gepaart(".", ["a", "b"], "p", "last", None, {"x": "y"}, n=3)
    assert r["gueltig"] is False and r.get("seite") == "kandidat", r
    assert r.get("bereich") == "b" and "SyntaxError" in r["grund"], r


def test_gegenprobe_vollstaendige_messung_bleibt_gueltig(monkeypatch):
    monkeypatch.setattr(messgeraet, "laufzeit_messen", lambda *a, **k: {"gueltig": True, "grund": "", "bereiche": {
        "a": {"laufzeit_ms": 1.0}, "b": {"laufzeit_ms": 2.0}}})
    r = messgeraet.laufzeit_gepaart(".", ["a", "b"], "p", "last", None, {"x": "y"}, n=3)
    assert r["gueltig"] is True and r["bereiche"]["b"]["kandidat"] == 2.0, r


# ================================================================ 2. Deckung je Abweichung
def _ts_werk(tmp_path):
    w = tmp_path / "werk"
    (w / "src" / "m").mkdir(parents=True)
    (w / "package.json").write_text('{"type":"module"}')
    (w / "src" / "m" / "a.ts").write_text("export function f(x: string): string { return x; }\n")
    return w


@pytest.mark.parametrize("aufrufe,gedeckt", [
    # der Test ruft f("a") und bekommt am Kandidaten "A": deckt genau f~rand#2 (Eingabe "a"), nicht f~form#0 ("\t")
    ([{"test": "t::a", "f": "m/a:f", "args": '["a"]', "erg": '"A"'}], {"m/a:f~rand#2": ["t::a"]}),
    # Gegenprobe: dieselbe Funktion, andere Eingabe — deckt nichts (früher, je Funktion: alles)
    ([{"test": "t::b", "f": "m/a:f", "args": '["b"]', "erg": '"B"'}], {}),
    # Gegenprobe: dieselbe Eingabe, anderes Ergebnis (der Test sah am Kandidaten etwas anderes als die Sonde) — nichts
    ([{"test": "t::a", "f": "m/a:f", "args": '["a"]', "erg": '"a"'}], {}),
])
def test_deckung_je_abweichung_am_organ(tmp_path, monkeypatch, aufrufe, gedeckt):
    w = _ts_werk(tmp_path)
    alt = {"m/a:f~rand#2": '"a"', "m/a:f~form#0": '"\\t"'}
    neu = {"m/a:f~rand#2": '"A"', "m/a:f~form#0": '"\\t!"'}
    arg = {"m/a:f~rand#2": '["a"]', "m/a:f~form#0": '["\\t"]'}
    seiten = iter([{"gueltig": True, "beobachtungen": alt, "argumente": arg, "eingewickelt": {"m/a": ["f"]}},
                   {"gueltig": True, "beobachtungen": neu, "argumente": arg, "eingewickelt": {"m/a": ["f"]}}])
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: next(seiten))
    r = vv.pruefen(w, {"src/m/a.ts": "x"}, "last", ["m"], {"tests": sorted({c["test"] for c in aufrufe}), "aufrufe": aufrufe})
    assert r["gedeckt"] == gedeckt, r
    assert r["tragfaehig"] is False and "m/a:f~form#0" in r["ungedeckt"]         # die Nachbarabweichung bleibt ungedeckt


def test_deckung_mutationsmuster_nicht_durch_frischen_aufruf(tmp_path, monkeypatch):
    """Ein veralteter Zwischenspeicher (@mutation liefert das alte Ergebnis) ist durch einen frischen Aufruf mit der
    mutierten Eingabe nicht deckbar: der frische Aufruf bekommt am Kandidaten das richtige Ergebnis, nicht das veraltete."""
    w = _ts_werk(tmp_path)
    alt = {"m/a:f#0": "3", "m/a:f#0@mutation": "37"}
    neu = {"m/a:f#0": "3", "m/a:f#0@mutation": "3"}
    arg = {"m/a:f#0": "[[1,2]]", "m/a:f#0@mutation": "[[17,27]]"}
    seiten = iter([{"gueltig": True, "beobachtungen": alt, "argumente": arg, "eingewickelt": {"m/a": ["f"]}},
                   {"gueltig": True, "beobachtungen": neu, "argumente": arg, "eingewickelt": {"m/a": ["f"]}}])
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: next(seiten))
    frisch = [{"test": "t::frisch", "f": "m/a:f", "args": "[[17,27]]", "erg": "37"}]
    r = vv.pruefen(w, {"src/m/a.ts": "x"}, "last", ["m"], {"tests": ["t::frisch"], "aufrufe": frisch})
    assert r["tragfaehig"] is False and r["ungedeckt"] == ["m/a:f#0@mutation"], r


# ================================================================ 1. Python-Sonde durch aegis.pruefen (echte Kammer)
def _python_pruefen(tmp_path, monkeypatch, diff, nische="schnell"):
    """aegis.pruefen am Python-Prüfwerk, echte Kammer (Messgerät, Bandit, Vulture, pytest, Python-Sonde). Gestellt sind
    das Modell (KEIN ANGRIFF) und die Laufzeitmessung: der Kandidat ist in `zahlen` 20 % schneller (so erreicht ein
    „schneller“-Kandidat den Verhaltensvergleich — wie K2934/K3121 in T3), `text` gleich schnell."""
    monkeypatch.setattr(kammer, "IMAGE", "biotop-kammer:1")
    w = tmp_path / "werk"
    SW.anlegen(w)
    con = sqlite3.connect(":memory:", isolation_level=None)
    con.row_factory = sqlite3.Row
    con.executescript(datenbank.SCHEMA)
    con.execute("INSERT INTO kandidaten(id,lauf_id,generation,bereich,nische,status,diff) VALUES(7,1,1,?,?,'erzeugt',?)",
                ("zahlen" if "statistik" in diff else "text", nische, diff))
    monkeypatch.setattr(aegis, "aufrufen", lambda *a, **k: SimpleNamespace(text="KEIN ANGRIFF"))
    basis = messgeraet.messen(w, ["zahlen", "text"], SW.PAKET, SW.REFERENZLAST)
    assert basis["gueltig"], basis.get("grund")
    def laufzeit(werk, bereiche, paket, ref, dateien=None, zeitlimit_s=150):
        kand = bool(dateien)
        return {"gueltig": True, "grund": "", "bereiche": {
            "zahlen": {"laufzeit_ms": 4.0 if kand else 5.0}, "text": {"laufzeit_ms": 5.0}}}
    monkeypatch.setattr(messgeraet, "laufzeit_messen", laufzeit)
    tausch = {"_rauschtoleranz": {"zahlen": 1.2, "text": 1.2}}
    u = aegis.pruefen(con, 1, 1, 7, w, SW.PAKET, ["zahlen", "text"], [], basis, basis, SW.REFERENZLAST, tausch)
    return con, u


def _verhalten(con):
    z = con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil' ORDER BY nr DESC LIMIT 1").fetchone()
    return json.loads(z[0]).get("verhalten") or {}


def test_py_zwischenspeicher_fehler_scheitert_am_laufweg(tmp_path, monkeypatch):
    con, u = _python_pruefen(tmp_path, monkeypatch, SW.zwischenspeicher_falsch())
    v = _verhalten(con)
    assert u["status"] == "abgelehnt" and u["grund"].startswith("Verhaltensvergleich:"), u["grund"]
    assert v["sprache"] == "python" and v["geurteilt"] is True
    assert any(k.startswith("speicherwerk.zahlen.statistik:spannweite#") and k.endswith("@mutation") for k in v["ungedeckt"]), v


def test_py_gegenprobe_speicher_am_inhalt_ueberlebt(tmp_path, monkeypatch):
    con, u = _python_pruefen(tmp_path, monkeypatch, SW.zwischenspeicher_richtig())
    v = _verhalten(con)
    assert v["sprache"] == "python" and v["geurteilt"] is True and v["anzahl_abweichungen"] == 0, v
    assert v["beobachtete_funktionen"] == "2 von 2", v
    assert not u["grund"].startswith("Verhaltensvergleich:"), u["grund"]


def test_py_weissraum_scheitert_an_formvariante(tmp_path, monkeypatch):
    """Der Kandidat entfernt toten Code (Kernmaß +1, besteht das Maß) und ändert nebenbei `normieren` für Tab und
    Zeilenumbruch — kein Test, keine Last nutzt das. Nur die Formvarianten des Korpus sehen es (T3-Muster K2868)."""
    con, u = _python_pruefen(tmp_path, monkeypatch, SW.weissraum_falsch(), nische="sicher")
    v = _verhalten(con)
    assert u["status"] == "abgelehnt" and u["grund"].startswith("Verhaltensvergleich:"), u["grund"]
    assert v["ungedeckt"] and all("~form#" in k for k in v["ungedeckt"]), v["ungedeckt"]


def test_py_gegenprobe_nur_toter_code_entfernt_ueberlebt(tmp_path, monkeypatch):
    con, u = _python_pruefen(tmp_path, monkeypatch, SW.toter_code_entfernt(), nische="sicher")
    v = _verhalten(con)
    assert u["status"] == "ueberlebt" and v["anzahl_abweichungen"] == 0 and v["geurteilt"] is True, (u["grund"], v)


# ================================================================ 3. Bestätigungsmessung vor der Laufzeitablehnung (aegis.pruefen)
def pruefen_mit_laufzeit(tmp_path, monkeypatch, erste, zweite):
    """aegis.pruefen (TS-Werk, Kernmaß +1, Tauschfaktor Laufzeit 1,1) mit gestellter Kammer: Messgerät, Sonde, Modell
    und Laufzeitmessung. `erste`/`zweite` = (Kandidat, Vorgeneration) in ms für `alpha` in der ersten gepaarten Messung
    bzw. der Nachmessung; zweite None = Nachmessung ungültig (Zeitlimit). Gezählt: Aufrufe von laufzeit_gepaart."""
    con = sqlite3.connect(":memory:", isolation_level=None)
    con.row_factory = sqlite3.Row
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
        return {"gueltig": True, "kernmass": 0, "werk": {"baut": True, "zyklen": 0, "bauzeit_ms": 100,
                "tests_fehlgeschlagen_liste": [], "tests_fehlgeschlagen_ids": []},
                "bereiche": {"alpha": {"tests_bestanden": 1, "tests_fehlgeschlagen": 0, "sicherheit_punkte": 0,
                                       "sicherheit_befunde": [], "tote_funktionen": 0 if kand else 1,
                                       "laufzeit_ms": None, "groesste_funktion": 3}}}
    monkeypatch.setattr(aegis.messgeraet, "messen", messen)
    zaehl = {"paare": 0}
    original = messgeraet.laufzeit_gepaart

    def gepaart(*a, **k):
        zaehl["paare"] += 1
        return original(*a, **k)
    monkeypatch.setattr(messgeraet, "laufzeit_gepaart", gepaart)

    def laufzeit(werk, bereiche, paket, ref, dateien=None, zeitlimit_s=150):
        werte = erste if zaehl["paare"] == 1 else zweite
        if werte is None:
            return {"gueltig": False, "grund": "Zeitlimit", "bereiche": {}}
        return {"gueltig": True, "grund": "", "bereiche": {"alpha": {"laufzeit_ms": werte[0] if dateien else werte[1]}}}
    monkeypatch.setattr(messgeraet, "laufzeit_messen", laufzeit)
    ok = {"gueltig": True, "beobachtungen": {"alpha/a:a#0": "1"}, "eingewickelt": {"alpha/a": ["a"]}, "aufgerufen": {"alpha/a:a": 1}}
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: dict(ok))
    basis = messen(w, ["alpha"], "src", None)
    u = aegis.pruefen(con, 1, 1, 7, w, "src", ["alpha"], [], basis, basis, "// last", {"laufzeit_faktor": 1.1})
    return u, zaehl


@pytest.mark.parametrize("zweite,erwartet", [
    ((12.0, 10.0), "abgelehnt"),        # Nachmessung bestätigt den Riss (×1,2 > Toleranz 1,15) → Ablehnung
    ((10.1, 10.0), "ueberlebt"),        # Nachmessung bestätigt ihn nicht → keine Ablehnung (Gegenprobe)
    (None, "zurueckgestellt"),          # Nachmessung ungültig → Messgerätausfall, zurückgestellt
])
def test_laufzeitriss_wird_vor_der_ablehnung_nachgemessen(tmp_path, monkeypatch, zweite, erwartet):
    u, messungen = pruefen_mit_laufzeit(tmp_path, monkeypatch, erste=(12.0, 10.0), zweite=zweite)
    assert u["status"] == (aegis.ZURUECKGESTELLT if erwartet == "zurueckgestellt" else erwartet), u["grund"]
    assert messungen["paare"] == 2                                    # erste Messung + genau eine Nachmessung
    if erwartet == "abgelehnt":
        assert "alpha.laufzeit_ms" in u["grund"], u["grund"]
    if erwartet == "ueberlebt":
        assert "laufzeit" not in u["grund"].lower() or "Nische" in u["grund"], u["grund"]


def test_gegenprobe_ohne_riss_keine_nachmessung(tmp_path, monkeypatch):
    u, messungen = pruefen_mit_laufzeit(tmp_path, monkeypatch, erste=(10.0, 10.0), zweite=(99.0, 10.0))
    assert u["status"] == "ueberlebt" and messungen["paare"] == 1, (u["grund"], messungen)


# ================================================================ Deckungsaufzeichner in der echten Kammer (TS und Python)
# Probe: ein Test, der die Funktion mit genau der Eingabe der Sonde ruft und am Kandidaten das neue Ergebnis bekommt,
# deckt GENAU diese Abweichung (und ihr Alias-Muster). Gegenprobe: ohne diesen Test ist sie ungedeckt. Beide Richtungen
# zeigen, dass der Aufzeichner wirklich aufzeichnet — ein leerer Aufzeichner ergäbe in beiden Fällen „ungedeckt“.
TS_QUELLE = "export function f(x: string): string {\n  return x;\n}\n"
TS_NEU = "export function f(x: string): string {\n  return x.toUpperCase();\n}\n"
TS_TEST = ("import { test, expect } from 'vitest';\nimport { f } from '../src/m/a.js';\n\n"
           "test('test_m_deckt_a', () => {\n  expect(f('a')).toBe('A');\n});\n")
PY_QUELLE = "def f(x: str) -> str:\n    return x\n"
PY_NEU = "def f(x: str) -> str:\n    return x.upper()\n"
PY_TEST = "from paket.m.a import f\n\n\ndef test_m_deckt_a():\n    assert f('a') == 'A'\n"


def _deckungswerk(tmp_path, sprache):
    w = tmp_path / f"werk_{sprache}"
    if sprache == "ts":
        (w / "src" / "m").mkdir(parents=True)
        (w / "tests").mkdir()
        (w / "package.json").write_text('{"type":"module"}')
        (w / "src" / "m" / "a.ts").write_text(TS_QUELLE)
        ref = "import { f } from './dist/m/a.js';\nexport function last_m() { for (let i = 0; i < 100; i++) f('z'); }\n"
        return w, {"src/m/a.ts": TS_NEU}, {"tests/test_m_deckung.test.ts": TS_TEST}, ref, "biotop-kammer:ts1"
    for d in ("paket/m", "tests"):
        (w / d).mkdir(parents=True)
    (w / "paket" / "__init__.py").write_text("")
    (w / "paket" / "m" / "__init__.py").write_text("")
    (w / "paket" / "m" / "a.py").write_text(PY_QUELLE)
    ref = "import sys\nsys.path.insert(0, '/werk')\n\ndef last_m():\n    from paket.m.a import f\n    for _ in range(100):\n        f('z')\n"
    return w, {"paket/m/a.py": PY_NEU}, {"tests/test_m_deckung.py": PY_TEST}, ref, "biotop-kammer:1"


@pytest.mark.parametrize("mit_test", [True, False])
@pytest.mark.parametrize("sprache", ["ts", "py"])
def test_deckungsaufzeichner_in_der_kammer_je_abweichung(tmp_path, monkeypatch, sprache, mit_test, ts_kammer):
    w, code, tests, ref, image = _deckungswerk(tmp_path, sprache)
    monkeypatch.setattr(kammer, "IMAGE", image)
    behoben = {("test_m_deckung.test.ts" if sprache == "ts" else "test_m_deckung.py") + "::test_m_deckt_a"} if mit_test else set()
    r = vv.pruefen(w, code, ref, ["m"], lambda abw: vv.deckende_aufrufe(w, code, tests, behoben))
    gedeckt = sorted((r.get("gedeckt") or {}))
    y = r["anzahl_abweichungen"]
    assert r["geurteilt"] is True and r["tragfaehig"] is False and y > 2, r      # 'x'×40, Formvarianten u. a. bleiben ungedeckt
    # `ungedeckt` im Urteil ist auf 20 gekürzt; die Zahl steht vollständig im Grund („x von y Abweichung(en) ungedeckt“).
    if mit_test:
        assert r["deckung_zaehlung"]["aufrufe"] >= 1, r["deckung_zaehlung"]     # der Aufzeichner hat aufgezeichnet
        assert gedeckt and all(k.split("@")[0].endswith("~rand#2") for k in gedeckt), r["gedeckt"]   # genau f('a')
        assert r["grund"].startswith(f"{y - len(gedeckt)} von {y} Abweichung(en) ungedeckt"), r["grund"]
    else:
        assert gedeckt == [] and r["grund"].startswith(f"{y} von {y} Abweichung(en) ungedeckt"), r["grund"]
