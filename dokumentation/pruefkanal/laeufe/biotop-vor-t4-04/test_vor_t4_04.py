"""Behebungsrunde 4 vor T4 — Laufweg-Tests (tests/test_vor_t4_04.py). Je Punkt Probe und Gegenprobe; wo ein Organ im
Annahmepfad wirkt, durch `aegis.pruefen` in der echten Kammer (biotop-kammer:1), gestellt nur das Modell (KEIN ANGRIFF)
und die Laufzeit (Kandidat 20 % schneller) — derselbe Ablauf wie tests/test_vor_t4_03.py::_pruefen.

H. Die vier hohen Befunde des Reviews 03 (Proben des Prüfers, review-proben/, als Tests gefasst):
   H1 doppeltes Leerzeichen deckt keinen Tab-/Zeilenumbruch-Rückschritt mehr (x1) | Kontrolle: Test mit Tab/LF deckt
   H2 ein Tab-Aufruf ohne Zusicherung hält nichts fest (x2)                         | Kontrolle: mit Zusicherung deckt
   H3 Iterator-Objekt mit Attribut: Last läuft durch, Änderung gesehen (p18)         | Kontrolle p18b
   H4 __slots__ / dataclass(slots=True): Zustand von self verglichen (p19, p20)     | Kontrolle p19b
E3 Entscheidung 3: Merkmale nicht veränderter Argumente gehören nicht zum Muster.
E4 Entscheidung 4: ein Kandidat mit Rückschritt und eigenem Test, der genau ihn zusichert, wird abgelehnt.
R  Weitere Spezifikationen: R4-5 Instanz aus der Signatur erproben, R4-6 Koroutinen, R4-8 Annahmegrund, R4-9
   ungültige Gewinn-Nachmessung, R4-13 Iterator-Kappe gezählt, R4-14 instabile Funktion nicht beobachtet.
S  Entscheidung 1: Vergleichslast Stufe 2 — Suche, Stufe im Urteil, Vorspann-Grenze 60 s.
"""
import json
import sqlite3
import sys
import time
from pathlib import Path
from types import SimpleNamespace

import pytest

from biotop.kern import datenbank, messgeraet
from biotop.organe import aegis, kammer
from biotop.organe import verhaltensvergleich as vv

sys.path.insert(0, str(Path(__file__).parent))
import test_vor_t4_03 as R3  # noqa: E402

QUELLE = R3.QUELLE
ALT_NORMIEREN = '    return " ".join(text.split())\n'
T_NORM = R3.TEST_NORMIEREN


def _norm_tests(faelle: dict) -> dict:
    return {f"tests/test_werk_normieren_{n}.py": T_NORM.format(name=n, eingabe=e, erwartet=x) for n, (e, x) in faelle.items()}


SOLL = {"gewoehnlich": ("a b", "a_b"), "rand": (" a b ", "a_b"), "gross": ("A B", "A_B"),
        "lang": ("x " * 25, "_".join(["x"] * 25)), "zahlform": ("a 01 2.50", "a_01_2.50"), "nichtascii": ("Ä ö", "Ä_ö")}


# ================================================================ H1 grobes Weißraum-Merkmal
K1 = ('    if "\\t" in text or "\\n" in text:\n        raise ValueError("Steuerzeichen")\n'
      '    return "_".join(text.split())\n')


@pytest.mark.parametrize("fall,faelle,status", [
    # Review 03 Nr. 1 (x1): an 0aac612 überlebte der Kandidat, 14 von 14 ValueError-Beobachtungen „gedeckt“ durch den
    # Test mit doppeltem Leerzeichen. Jetzt: Tab und Zeilenumbruch sind eigene Merkmale — abgelehnt.
    ("x1_doppelt", {**SOLL, "doppelt": ("a  b", "a_b")}, "abgelehnt"),
    # Kontrolle: ohne den Test mit doppeltem Leerzeichen — abgelehnt (wie an 0aac612)
    ("x1k_ohne_doppelt", SOLL, "abgelehnt"),
])
def test_h1_doppeltes_leerzeichen_deckt_keinen_tab_rueckschritt(tmp_path, monkeypatch, fall, faelle, status):
    neu = QUELLE.replace(ALT_NORMIEREN, K1)
    u, v = R3._pruefen(tmp_path, monkeypatch, R3._diff(QUELLE, neu), nische="sicher", werk_extra=_norm_tests(faelle))
    assert u["status"] == status and u["grund"].startswith("Verhaltensvergleich:"), u["grund"]
    offen = v.get("ungedeckt_alle") or v.get("ungedeckt") or []
    assert any(k.startswith("probewerk.werk.kern:normieren~form#") for k in offen), offen
    auf = v.get("ungedeckt_aufschluesselung") or {}
    assert any("tab" in s.split(" | ")[1].split("+") for s in auf), auf


def test_h1_gegenprobe_tests_je_formvariante_decken_den_rueckschritt_nicht_und_die_behebung_schon(tmp_path, monkeypatch):
    """Gegenprobe: ein Test je Formvariante (auch Tab, Zeilenumbruch, CRLF, NBSP, doppelt) — die BEABSICHTIGTE Änderung
    „ _“ ist gedeckt, wer dieselben Tests hat, deckt auch Tab/LF: da K1 bei Tab/LF wirft, fallen die Tab/LF-Tests am
    Kandidaten und sind KEINE deckenden Tests — der Kandidat bleibt abgelehnt. Mit der richtigen Behebung (Tab/LF werden
    wie Leerzeichen behandelt) bestehen alle Tests: überlebt."""
    alle = {**SOLL, "tab": ("a\tb", "a_b"), "lf": ("a\nb", "a_b"), "crlf": ("a\r\nb", "a_b"), "nbsp": ("a\u00a0b", "a_b"),
            "doppelt": ("a  b", "a_b")}
    richtig = QUELLE.replace(ALT_NORMIEREN, '    return "_".join(text.split())\n')
    u, v = R3._pruefen(tmp_path, monkeypatch, R3._diff(QUELLE, richtig), nische="sicher", werk_extra=_norm_tests(alle))
    assert u["status"] == "ueberlebt" and v["ungedeckt"] == [], (u["grund"], v.get("ungedeckt_aufschluesselung"))


# ================================================================ H2 Verfälschung je Merkmal
K2 = '    if "\\t" in text:\n        return text\n    return "_".join(text.split())\n'


@pytest.mark.parametrize("mit_zusicherung,status", [
    # Review 03 Nr. 2 (x2): an 0aac612 „hielt“ der Test den Tab-Rückschritt fest, weil die Verfälschung JEDEN Aufruf von
    # normieren traf und die Zusicherung auf normieren("a b") fiel. Jetzt verfälscht der Aufzeichner nur Aufrufe mit Tab.
    (False, "abgelehnt"),
    # Gegenprobe: derselbe Test sichert den Tab-Aufruf zu — dann hält er ihn fest (und der Rückschritt wird sichtbar: der
    # Test fällt am Kandidaten; mit der richtigen Behebung überlebt er — siehe H1-Gegenprobe).
    (True, "abgelehnt"),
])
def test_h2_tab_aufruf_ohne_zusicherung_haelt_nichts_fest(tmp_path, monkeypatch, mit_zusicherung, status):
    tests = _norm_tests({k: v for k, v in SOLL.items() if k != "gewoehnlich"})
    koerper = ('    assert normieren("a\\tb c") == "a_b_c"\n' if mit_zusicherung else '    normieren("a\\tb c")\n')
    tests["tests/test_werk_normieren_x.py"] = ("from probewerk.werk.kern import normieren\n\n\ndef test_normieren_x():\n"
                                                + koerper + '    assert normieren("a b") == "a_b"\n')
    neu = QUELLE.replace(ALT_NORMIEREN, K2)
    u, v = R3._pruefen(tmp_path, monkeypatch, R3._diff(QUELLE, neu), nische="sicher", werk_extra=tests)
    assert u["status"] == status, u["grund"]
    if not mit_zusicherung:
        assert u["grund"].startswith("Verhaltensvergleich:"), u["grund"]
        fest = (v.get("deckung_zaehlung") or {}).get("festhaltend") or {}
        tab = [t for k, t in fest.items() if k.endswith("|tab")]
        assert tab and all(not any(x.endswith("test_normieren_x") for x in t) for t in tab), fest
    else:
        # der Test mit Zusicherung fällt am Kandidaten (Tab bleibt stehen) — er ist kein deckender Test, sondern ein
        # Werkstest, der den Rückschritt fängt: abgelehnt über das Maß (Regression je Test), nicht über die Deckung
        assert "test_normieren_x" in u["grund"] or u["grund"].startswith("Verhaltensvergleich:"), u["grund"]


def test_h2_fixture_fehler_zaehlt_nicht_als_festhalten(tmp_path, monkeypatch):
    """Review 03 Nr. 2 (gelesen, nicht gemessen): eine Fixture, die das Ergebnis von f verwendet, machte jeden Test zum
    „festhaltenden“. Jetzt ist ein Fehler im Aufbau 'fehler', nicht 'fail'. Gemessen am Aufzeichner (Kammer)."""
    import test_vor_t4_02 as R2
    w, code, _, ref, image = R2._deckungswerk(tmp_path, "py")
    monkeypatch.setattr(kammer, "IMAGE", image)
    test = ("import pytest\nfrom paket.m.a import f\n\n\n@pytest.fixture\ndef wert():\n    assert f('a') == 'A'\n    return 1\n\n\n"
            "def test_m_deckt_a(wert):\n    assert f('a') is not None\n")
    tests = {"tests/test_m_deckung.py": test}
    d = vv.deckende_aufrufe(w, code, tests, {"test_m_deckung.py::test_m_deckt_a"})
    assert d["aufrufe"], d
    assert d["haelt"]("paket.m.a:f", "rueckgabe", "") == [], "Fixture-Fehler darf nicht als Festhalten zählen"
    # Gegenprobe: dieselbe Zusicherung IM Test hält fest
    tests2 = {"tests/test_m_deckung.py": "from paket.m.a import f\n\n\ndef test_m_deckt_a():\n    assert f('a') == 'A'\n"}
    d2 = vv.deckende_aufrufe(w, code, tests2, {"test_m_deckung.py::test_m_deckt_a"})
    assert d2["haelt"]("paket.m.a:f", "rueckgabe", "") == ["test_m_deckung.py::test_m_deckt_a"]


# ================================================================ H3/H4 Sonde am Organ (Proben p18, p19, p20 des Prüfers)
def _organ(tmp_path, monkeypatch, quelle, neu, last, name="w"):
    monkeypatch.setattr(kammer, "IMAGE", "biotop-kammer:1")
    w = tmp_path / name
    (w / "paket" / "m").mkdir(parents=True)
    (w / "tests").mkdir()
    (w / "paket" / "__init__.py").write_text("")
    (w / "paket" / "m" / "__init__.py").write_text("")
    (w / "paket" / "m" / "a.py").write_text(quelle)
    ref = "import sys\nsys.path.insert(0, '/werk')\n\n\ndef last_m():\n" + "".join("    " + z + "\n" for z in last.splitlines())
    return vv.pruefen(w, {"paket/m/a.py": neu}, ref, ["m"], {"tests": [], "aufrufe": []})


LS = ("class Leser:\n    def __init__(self, text: str):\n        self.teile = text.split()\n        self.nummer = 0\n\n"
      "    def __iter__(self):\n        return self\n\n    def __next__(self) -> str:\n        if self.nummer >= len(self.teile):\n"
      "            raise StopIteration\n        self.nummer += 1\n        return self.teile[self.nummer - 1]\n\n\n"
      "def leser(text: str) -> 'Leser':\n    return Leser(text)\n\n\ndef doppel(x: int) -> int:\n    return {}\n")


@pytest.mark.parametrize("mit_attribut", [True, False])
def test_h3_iterator_objekt_bleibt_erhalten(tmp_path, monkeypatch, mit_attribut):
    """Review 03 Nr. 3 (p18): an 0aac612 ersetzte die Sonde das Iterator-Objekt durch einen Generator, die Last brach bei
    `r.nummer` still ab, die Änderung an doppel(3) blieb unsichtbar (0 Abweichungen, tragfähig). Kontrolle p18b ohne
    Attributzugriff: 6 Abweichungen. Jetzt in beiden Fällen gesehen; das Iterator-Objekt ist gezählt."""
    last = "from paket.m.a import leser, doppel\nr = leser('a b c')\nnext(r)\n" + ("n = r.nummer\n" if mit_attribut else "") + "doppel(3)"
    r = _organ(tmp_path, monkeypatch, LS.format("2 * x"), LS.format("2 * x + (1 if x == 3 else 0)"), last)
    assert r["tragfaehig"] is False and r["anzahl_abweichungen"] > 0, r
    assert any(k.startswith("paket.m.a:doppel#") for k in r["abweichungen"]), r["abweichungen"]
    assert (r.get("teilweise") or {}).get("paket.m.a:leser", {}).get("iterator_objekt"), r.get("teilweise")


KS = ("class Konto:\n{slots}    def __init__(self, stand: int):\n        self.stand = stand\n\n"
      "    def buchen(self, b: int) -> None:\n        self.stand += {faktor}b\n")
DC = ("import dataclasses\n\n\n@dataclasses.dataclass(slots=True)\nclass Konto:\n    stand: int\n\n"
      "    def buchen(self, b: int) -> None:\n        self.stand += {faktor}b\n")
LAST_K = "from paket.m.a import Konto\nk = Konto(1)\nk.buchen(2)\nk.buchen(3)"


@pytest.mark.parametrize("art", ["slots", "dataclass_slots", "ohne_slots"])
def test_h4_zustand_von_self_auch_mit_slots(tmp_path, monkeypatch, art):
    """Review 03 Nr. 4 (p19, p20): an 0aac612 0 Abweichungen bei __slots__ und dataclass(slots=True), Kontrolle ohne
    __slots__ 28. Jetzt wird der Zustand von self auch dort verglichen."""
    if art == "slots":
        alt, neu = KS.format(slots="    __slots__ = ('stand',)\n\n", faktor=""), KS.format(slots="    __slots__ = ('stand',)\n\n", faktor="2 * ")
    elif art == "dataclass_slots":
        alt, neu = DC.format(faktor=""), DC.format(faktor="2 * ")
    else:
        alt, neu = KS.format(slots="", faktor=""), KS.format(slots="", faktor="2 * ")
    r = _organ(tmp_path, monkeypatch, alt, neu, LAST_K)
    assert r["tragfaehig"] is False and any(">args" in k for k in r["abweichungen"]), r


def test_h4_gegenprobe_slots_umgeschrieben_ohne_abweichung(tmp_path, monkeypatch):
    alt = KS.format(slots="    __slots__ = ('stand',)\n\n", faktor="")
    neu = alt.replace("        self.stand += b\n", "        neu = self.stand + b\n        self.stand = neu\n")
    assert neu != alt
    r = _organ(tmp_path, monkeypatch, alt, neu, LAST_K)
    assert r["tragfaehig"] is True and r["anzahl_abweichungen"] == 0, r


# ================================================================ R4-5 Instanz aus der Signatur, R4-6 Koroutinen
KU = ("class Zaehler:\n    def __init__(self, start{ann}):\n        self.start = start\n\n    def weiter(self) -> int:\n"
      "        return self.start + {d}\n\n\ndef eins() -> int:\n    return 1\n")


@pytest.mark.parametrize("ann", ["", ": int"])
def test_r45_instanz_aus_der_signatur_wird_erprobt(tmp_path, monkeypatch, ann):
    """Review 03 Nr. 6 (p16): ohne Annotation und ohne Vertrag baute die Sonde Zaehler('a b'); weiter() warf, die Änderung
    blieb still („1 von 2“, tragfähig). Kontrolle p16b mit Annotation: 4 Abweichungen. Jetzt in beiden Fällen gesehen."""
    r = _organ(tmp_path, monkeypatch, KU.format(ann=ann, d=1), KU.format(ann=ann, d=2), "from paket.m.a import eins\neins()")
    assert r["tragfaehig"] is False and any("Zaehler.weiter" in k for k in r["abweichungen"]), r
    assert (r.get("instanzen") or {}).get("paket.m.a:Zaehler") in ("signatur_erprobt", "signatur"), r.get("instanzen")


AS = "async def hole(x: int) -> int:\n    return x + {}\n\n\ndef eins() -> int:\n    return 1\n"


@pytest.mark.parametrize("d,tragfaehig", [(2, False), (1, True)])
def test_r46_koroutine_wird_beobachtet(tmp_path, monkeypatch, d, tragfaehig):
    """Review 03 Nr. 7 (p13): an 0aac612 Enthaltung „unvergleichbar (asynchron)“, trotzdem tragfähig. Jetzt führt die
    Sonde die Koroutine in einer eigenen Ereignisschleife aus. Gegenprobe: unverändert → tragfähig, 0 Abweichungen."""
    r = _organ(tmp_path, monkeypatch, AS.format(1), AS.format(d),
               "import asyncio\nfrom paket.m.a import hole, eins\nasyncio.run(hole(3))\neins()")
    assert r["tragfaehig"] is tragfaehig, r
    assert "paket.m.a:hole" not in (r.get("enthaltungen") or {}), r.get("enthaltungen")


IT = "def zaehle(start: int):\n    n = start\n    while True:\n        yield n\n        n += {}\n"


def test_r413_iterator_kappe_ist_gezaehlt(tmp_path, monkeypatch):
    """Review 03 Nr. 16 (p14): eine Änderung ab dem 51. Element ist unsichtbar — jetzt als Teil-Enthaltung gezählt."""
    r = _organ(tmp_path, monkeypatch, IT.format("1"), IT.format("1 if n < start + 60 else 2"),
               "from itertools import islice\nfrom paket.m.a import zaehle\nlist(islice(zaehle(0), 100))")
    assert (r.get("teilweise") or {}).get("paket.m.a:zaehle", {}).get("iterator_gekappt"), r.get("teilweise")


def test_r414_instabile_funktion_zaehlt_nicht_als_beobachtet(tmp_path, monkeypatch):
    w = tmp_path / "w"
    (w / "paket").mkdir(parents=True)
    folge = iter([{"gueltig": True, "beobachtungen": {"paket.a:f#0": '["a","b"]', "paket.a:g#0": "1"}, "inhalt": {"paket.a:g": 1, "paket.a:f": 1},
                   "eingewickelt": {"paket.a": ["f", "g"]}},
                  {"gueltig": True, "beobachtungen": {"paket.a:f#0": '["b","a"]', "paket.a:g#0": "1"}, "inhalt": {"paket.a:g": 1, "paket.a:f": 1},
                   "eingewickelt": {"paket.a": ["f", "g"]}},
                  {"gueltig": True, "beobachtungen": {"paket.a:f#0": '["a","b"]', "paket.a:g#0": "1"}, "inhalt": {"paket.a:g": 1, "paket.a:f": 1},
                   "eingewickelt": {"paket.a": ["f", "g"]}}])
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: next(folge))
    r = vv.pruefen(w, {"paket/a.py": "x"}, "last", ["paket"], {})
    assert r["beobachtete_funktionen"] == "1 von 2" and r["enthaltungen"].get("paket.a:f", "").startswith("instabil"), r


# ================================================================ E3 Muster nur aus veränderten Argumenten
def test_e3_muster_nur_aus_veraenderten_argumenten():
    """Entscheidung 3 am Rechenweg der Sonde (kern/py/verhalten.py::_muster_von, in der Kammer dieselbe Funktion)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("vh", Path(__file__).parent.parent / "biotop/kern/py/verhalten.py")
    assert spec is not None and spec.loader is not None
    vh = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(vh)
    grund = ["grund + gewicht * 2", {"__dict": [["gewicht", 0], ["grund", 250]]}]
    tab = ["grund\t+\tgewicht\t*\t2", grund[1]]
    assert vh._muster_von(tab, grund, "form") == ["tab"]                 # nicht null_zahl aus dem unveränderten gewicht
    rand = ["a", grund[1]]
    assert vh._muster_von(rand, grund, "rand") == []                     # Randwert 'a': keine Formvariante → gewöhnlich
    assert vh._muster_von(grund, grund, "rand") == []
    # Gegenprobe: dieselbe Umformung an einem Argument, das schon Tab trägt, führt kein Merkmal ein
    assert vh._muster_von(["x\t\ty"], ["x\ty"], "form") == []


# ================================================================ E4 eigene Tests decken nicht
K_TAB = '    if "\\t" in text:\n        raise ValueError("Tab")\n    return "_".join(text.split())\n'
SOLL_OHNE_TAB = {**SOLL, "lf": ("a\nb", "a_b"), "crlf": ("a\r\nb", "a_b"), "nbsp": ("a\u00a0b", "a_b"),
                 "doppelt": ("a  b", "a_b")}
EIGENER_TEST = ("import pytest\nfrom probewerk.werk.kern import normieren\n\n\n"
                "def test_werk_rueckschritt_tab():\n    \"\"\"Verfassung Satz 2: Steuerzeichen werden abgewiesen.\"\"\"\n"
                "    with pytest.raises(ValueError):\n        normieren('a\\tb')\n    assert normieren('a b') == 'a_b'\n")
VERFASSUNG = {"text": "1. Zweck: Prüfwerk ohne Betriebszweck.\n2. Sicherheit: Eingaben sind Daten.\n", "regeln": {}}


def test_e4_kandidat_mit_rueckschritt_und_eigenem_test_wird_abgelehnt(tmp_path, monkeypatch):
    """Entscheidung 4: der Kandidat bricht Tab (wirft ValueError) und bringt einen eigenen Test mit, der genau diesen
    Rückschritt zusichert — gültig nach der Norm-Regel (Verweis auf Verfassung Satz 2), er kommt also in den
    Testbestand, fällt an der Vorgeneration und besteht am Kandidaten. Er deckt trotzdem nicht: abgelehnt, alle
    ungedeckten Abweichungen tragen `tab`, der Test steht als ausgeschlossen im Urteil."""
    monkeypatch.setattr(aegis.verfassung, "lesen", lambda *a: VERFASSUNG)
    neu = QUELLE.replace(ALT_NORMIEREN, K_TAB)
    diff = R3._diff(QUELLE, neu, tests={"tests/test_werk_eigen.py": EIGENER_TEST})
    u, v = R3._pruefen(tmp_path, monkeypatch, diff, nische="sicher", werk_extra=_norm_tests(SOLL_OHNE_TAB))
    assert u["status"] == "abgelehnt" and u["grund"].startswith("Verhaltensvergleich:"), u["grund"]
    assert any("test_werk_rueckschritt_tab" in t for t in v.get("eigene_tests_ausgeschlossen") or []), v.get("eigene_tests_ausgeschlossen")
    auf = v.get("ungedeckt_aufschluesselung") or {}
    assert auf and all("tab" in s.split(" | ")[1].split("+") for s in auf), auf


def test_e4_gegenprobe_derselbe_test_in_der_vorgeneration_deckt(tmp_path, monkeypatch):
    """Gegenprobe: derselbe Test liegt schon in der Vorgeneration (dort rot) — er deckt die Tab-Abweichungen, der
    Kandidat überlebt. Nur die Herkunft des Tests unterscheidet die beiden Fälle."""
    monkeypatch.setattr(aegis.verfassung, "lesen", lambda *a: VERFASSUNG)
    neu = QUELLE.replace(ALT_NORMIEREN, K_TAB)
    extra = {**_norm_tests(SOLL_OHNE_TAB), "tests/test_werk_eigen.py": EIGENER_TEST}
    u, v = R3._pruefen(tmp_path, monkeypatch, R3._diff(QUELLE, neu), nische="sicher", werk_extra=extra)
    assert u["status"] == "ueberlebt" and v["ungedeckt"] == [], (u["grund"], v.get("ungedeckt_aufschluesselung"))
    assert not (v.get("eigene_tests_ausgeschlossen") or []), v


def test_e4_eigene_tests_am_organ():
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        w = Path(d)
        (w / "tests").mkdir()
        (w / "tests" / "test_a.py").write_text("def test_alt():\n    assert 1\n")
        neu = "def test_alt():\n    assert 1\n\n\ndef test_neu():\n    assert 2\n"
        assert aegis.eigene_tests(w, {"tests/test_a.py": neu}, {}) == {"test_a.py::test_neu"}
        geaendert = "def test_alt():\n    assert 3\n"
        assert aegis.eigene_tests(w, {"tests/test_a.py": geaendert}, {}) == {"test_a.py::test_alt"}
        assert aegis.eigene_tests(w, {"tests/test_a.py": "def test_alt():\n    assert 1\n"}, {}) == set()


# ================================================================ R4-8 / R4-9 Gewinn
def test_r48_annahmegrund_nur_bestaetigte_gewinne():
    u = {"ok": True, "kern_basis": 0, "kern_kandidat": 0,
         "laufzeit_gewinne": ["bericht.laufzeit_ms: 5.0 → 4.0 (−20 %)", "planung.laufzeit_ms: 10.0 → 8.4 (−16 %)"]}
    g = messgeraet.gewinne_beschraenken(u, ["planung"])
    assert g["laufzeit_gewinne"] == ["planung.laufzeit_ms: 10.0 → 8.4 (−16 %)"] and "bericht" not in g["grund"], g
    assert messgeraet.gewinne_beschraenken(u, ["bericht", "planung"]) is u


def test_r49_ungueltige_gewinn_nachmessung_stellt_zurueck(tmp_path, monkeypatch):
    """Review 03 Nr. 12: der Zweig war gebaut, aber ungetestet. Erste Messung im Band (−12 %), Nachmessung ungültig →
    zurückgestellt (Messgerätausfall), nicht angenommen und nicht abgelehnt."""
    zaehler = {"n": 0}

    def laufzeit(werk, bereiche, paket, ref, dateien=None, zeitlimit_s=150):
        zaehler["n"] += 1
        if zaehler["n"] > 2 * messgeraet.LAUFZEIT_PAAR:
            return {"gueltig": False, "grund": "Kammer rc=137", "bereiche": {}}
        return {"gueltig": True, "grund": "", "bereiche": {"alpha": {"laufzeit_ms": 8.8 if dateien else 10.0}}}
    u, _ = _gewinn_mit_laufzeit(tmp_path, monkeypatch, laufzeit)
    assert u["status"] == aegis.ZURUECKGESTELLT and "Gewinn-Nachmessung" in u["grund"], u["grund"]


def test_r49_gegenprobe_gueltige_nachmessung_entscheidet(tmp_path, monkeypatch):
    def laufzeit(werk, bereiche, paket, ref, dateien=None, zeitlimit_s=150):
        return {"gueltig": True, "grund": "", "bereiche": {"alpha": {"laufzeit_ms": 8.8 if dateien else 10.0}}}
    u, _ = _gewinn_mit_laufzeit(tmp_path, monkeypatch, laufzeit)
    assert u["status"] == "abgelehnt" and "15 %" in u["grund"], u["grund"]


def _gewinn_mit_laufzeit(tmp_path, monkeypatch, laufzeit):
    """Wie test_vor_t4_03._gewinn_pruefen, aber mit einer frei gestellten Laufzeitfunktion."""
    con = sqlite3.connect(":memory:", isolation_level=None)
    con.row_factory = sqlite3.Row
    con.executescript(datenbank.SCHEMA)
    w = tmp_path / "w"
    (w / "src" / "alpha").mkdir(parents=True)
    (w / "package.json").write_text('{"type":"module"}')
    (w / "src" / "alpha" / "a.ts").write_text("export function a(x: number): number {\n  return x;\n}\n")
    diff = ("--- a/src/alpha/a.ts\n+++ b/src/alpha/a.ts\n@@ -1,3 +1,3 @@\n export function a(x: number): number {\n"
            "-  return x;\n+  return x + 0;\n }\n")
    con.execute("INSERT INTO kandidaten(id,lauf_id,generation,bereich,nische,status,diff) VALUES(7,1,1,'alpha','schnell','erzeugt',?)", (diff,))
    monkeypatch.setattr(aegis, "aufrufen", lambda *a, **k: SimpleNamespace(text="KEIN ANGRIFF"))

    def messen(werk, bereiche, paket, ref, dateien=None, **k):
        return {"gueltig": True, "kernmass": 0, "werk": {"baut": True, "zyklen": 0, "bauzeit_ms": 100,
                "tests_fehlgeschlagen_liste": [], "tests_fehlgeschlagen_ids": []},
                "bereiche": {"alpha": {"tests_bestanden": 1, "tests_fehlgeschlagen": 0, "sicherheit_punkte": 0,
                                       "sicherheit_befunde": [], "tote_funktionen": 0, "laufzeit_ms": None, "groesste_funktion": 3}}}
    monkeypatch.setattr(aegis.messgeraet, "messen", messen)
    monkeypatch.setattr(messgeraet, "laufzeit_messen", laufzeit)
    ok = {"gueltig": True, "beobachtungen": {"alpha/a:a#0": "1"}, "eingewickelt": {"alpha/a": ["a"]}, "inhalt": {"alpha/a:a": 1}}
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: dict(ok))
    basis = messen(w, ["alpha"], "src", None)
    u = aegis.pruefen(con, 1, 1, 7, w, "src", ["alpha"], [], basis, basis, "// last",
                      {"laufzeit_faktor": 2.0, "_rauschtoleranz": {"alpha": 1.2}}, referenzlast_laufzeit="// last stufe 2")
    return u, None


# ================================================================ S Vergleichslast Stufe 2
def test_s_stufe2_suche_und_ts_werk():
    from biotop import lauf as L
    r1 = L._referenzlast("versandwerk-t3-02", "src")
    r2 = L._referenzlast("versandwerk-t3-02", "src", 2)
    assert r1 and r2 and r1 != r2 and "ZWEITE STUFE" in r2 and "ZWEITE STUFE" not in r1
    assert L._referenzlast("gibt-es-nicht", None, 2) is None


def test_s_stufe2_wird_im_annahmepfad_genutzt(tmp_path, monkeypatch):
    """Die gepaarte Laufzeitmessung bekommt die Stufe-2-Last, die Sonde die Stufe-1-Last; die Stufe steht im Urteil."""
    gesehen = []

    def laufzeit(werk, bereiche, paket, ref, dateien=None, zeitlimit_s=150):
        gesehen.append(ref)
        return {"gueltig": True, "grund": "", "bereiche": {"alpha": {"laufzeit_ms": 8.0 if dateien else 10.0}}}
    u, _ = _gewinn_mit_laufzeit(tmp_path, monkeypatch, laufzeit)
    assert gesehen and set(gesehen) == {"// last stufe 2"}, set(gesehen)
    assert u["status"] == "ueberlebt", u["grund"]


def test_s_vorspann_verweigert_zu_langsame_stufe2():
    from biotop.organe import vorspann
    assert vorspann.STUFE2_KAMMERLAUF_S == 60


# ================================================================ Merkmale: dieselbe Rechnung in beiden Sprachen (Review 03 Nr. 17)
MERKMAL_PROBEN = ["a b", "a\tb", "a\nb", "a\r\nb", "a\rb", "a\u00a0b", "a  b", " a", "a ", "\ta b\n", "A B", "a b",
                  "a 01 2.50", "x" * 40, "Ä ö", "a\u2028b", "", "12", "0.50"]


def test_merkmale_gleich_in_python_und_typescript():
    """kern/py/verhalten.py::_text_merkmale und kern/ts/kanon.mjs::textMerkmale liefern dieselben Merkmale (Sonde und
    Aufzeichner beider Sprachen rechnen je Formvariante dasselbe). Gegenprobe: die Proben unterscheiden die Merkmale
    wirklich (mindestens 12 verschiedene Merkmale kommen vor)."""
    import importlib.util
    import subprocess
    kern = Path(__file__).parent.parent / "biotop/kern"
    spec = importlib.util.spec_from_file_location("vh", kern / "py/verhalten.py")
    assert spec is not None and spec.loader is not None
    vh = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(vh)
    py = [sorted(vh._text_merkmale(s)) if s else ["leer"] for s in MERKMAL_PROBEN]
    skript = ("import {textMerkmale} from " + json.dumps(str(kern / "ts/kanon.mjs")) + ";\n"
              "const p = JSON.parse(process.argv[1]);\n"
              "console.log(JSON.stringify(p.map(s => s ? [...textMerkmale(s)].sort() : ['leer'])));\n")
    r = subprocess.run(["node", "--input-type=module", "-e", skript, json.dumps(MERKMAL_PROBEN)],
                       capture_output=True, text=True, timeout=60)
    assert r.returncode == 0, r.stderr
    ts = json.loads(r.stdout)
    unterschiede = {MERKMAL_PROBEN[i]: (py[i], ts[i]) for i in range(len(py)) if py[i] != ts[i]}
    assert not unterschiede, unterschiede
    alle = {m for x in py for m in x}
    assert len(alle) >= 12 and {"tab", "zeilenumbruch", "crlf", "cr", "nbsp", "doppelleer", "rand_vorn", "rand_hinten"} <= alle, alle


# ================================================================ Nachtrag: R4-3 zweiter Teil — Lastabbruch unter der Sonde
def _gestellt(tmp_path, monkeypatch, alt_last, neu_last):
    w = tmp_path / "w"
    (w / "paket").mkdir(parents=True)
    alt = {"gueltig": True, "beobachtungen": {"korpus:last_paket": alt_last, "paket.a:f#0": "1"}, "inhalt": {"paket.a:f": 1},
           "eingewickelt": {"paket.a": ["f"]}}
    neu = {"gueltig": True, "beobachtungen": {"korpus:last_paket": neu_last, "paket.a:f#0": "1"}, "inhalt": {"paket.a:f": 1},
           "eingewickelt": {"paket.a": ["f"]}}
    folge = iter([alt, alt, neu])
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: dict(next(folge)))
    return w


def test_r43_lastabbruch_unter_der_sonde_an_der_vorgeneration_ist_ausfall(tmp_path, monkeypatch):
    """Review 03 Nr. 3: an 0aac612 fehlten die Lastbeobachtungen still, die Änderung blieb unsichtbar."""
    w = _gestellt(tmp_path, monkeypatch, "Fehler:AttributeError", "Fehler:AttributeError")
    with pytest.raises(vv.SondeAusgefallen, match="bricht unter der Sonde"):
        vv.pruefen(w, {"paket/a.py": "x"}, "last", ["paket"], {})


def test_r43_gegenprobe_abbruch_nur_am_kandidaten_ist_befund(tmp_path, monkeypatch):
    w = _gestellt(tmp_path, monkeypatch, "ok", "Fehler:AttributeError")
    r = vv.pruefen(w, {"paket/a.py": "x"}, "last", ["paket"], {})
    assert r["tragfaehig"] is False and "korpus:last_paket" in r["abweichungen"], r


# ================================================================ Nachtrag: Entscheidung 5 — Torzeile „Schwächen“
from biotop.kern import gegenzeugen  # noqa: E402

_WEG = {"verletzt": False}
_DA = {"verletzt": True}
_GLEICH = {"faelle": 100, "abweichungen": 0}
_ANDERS = {"faelle": 100, "abweichungen": 7}


@pytest.mark.parametrize("schwaechen,behoben,erfuellt", [
    ({f"S{i}": {"schwaeche": _WEG, "normal": _GLEICH} for i in range(1, 5)} | {"S5": {"schwaeche": _DA, "normal": _GLEICH}},
     4, True),                                                  # 4 von 5 doppelt behoben = 80 % → erfüllt
    ({f"S{i}": {"schwaeche": _WEG, "normal": _GLEICH} for i in range(1, 4)} | {"S4": {"schwaeche": _WEG, "normal": _ANDERS},
     "S5": {"schwaeche": _DA, "normal": _GLEICH}}, 3, False),   # Gegenprobe: S4 weg, aber Verhalten verändert → 3 von 5
    ({f"S{i}": {"schwaeche": _WEG, "normal": _GLEICH} for i in range(1, 4)} | {"S4": {"schwaeche": _WEG, "normal": None},
     "S5": {"schwaeche": _DA, "normal": _GLEICH}}, 3, False),   # nicht beurteilbar zählt nie als behoben
    ({}, 0, False),                                             # null Schwächen: nicht erfüllt
])
def test_torzeile_schwaechen_verlangt_beide_pruefungen(schwaechen, behoben, erfuellt):
    z = gegenzeugen.torzeile_schwaechen(schwaechen)
    assert len(z["behoben"]) == behoben and z["erfuellt"] is erfuellt, z["zeile"]


# ================================================================ Nachtrag: Nachspiel — Import überschreibt keine Fallvariable
def test_nachspiel_vorbereiten_import_ueberschreibt_keine_variable():
    """Fehler in 1d9a5aa: `from .organe import eichung` in nachspiel.vorbereiten band den Namen der Maßeichung des Falls
    neu; alle Nachspiele brachen mit AttributeError ab. Kein Import in vorbereiten darf einen Namen binden, dem die
    Funktion auch einen Wert zuweist. Gegenprobe: die fehlerhafte Fassung wird von derselben Prüfung erkannt."""
    import ast

    def konflikte(quelle: str) -> set[str]:
        fn = next(k for k in ast.parse(quelle).body if isinstance(k, ast.FunctionDef) and k.name == "vorbereiten")
        importiert = {a.asname or a.name.split(".")[0] for n in ast.walk(fn) if isinstance(n, (ast.Import, ast.ImportFrom))
                      for a in n.names}
        zugewiesen = {z.id for n in ast.walk(fn) if isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign))
                      for z in ast.walk(n) if isinstance(z, ast.Name) and isinstance(z.ctx, ast.Store)}
        return importiert & zugewiesen
    quelle = (Path(__file__).parent.parent / "biotop/nachspiel.py").read_text()
    assert konflikte(quelle) == set(), konflikte(quelle)
    kaputt = quelle.replace("from .organe import eichung as eichung_organ, vorspann", "from .organe import eichung, vorspann")
    assert kaputt != quelle and konflikte(kaputt) == {"eichung"}
