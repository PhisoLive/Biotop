"""Behebungsrunde 5 vor T4 — Klassen statt Fälle (Entscheidungen Chat-Claude 24.09.2026 zum Review 04).
Je Entscheidung Probe und Gegenprobe; wo ein Organ im Annahmepfad wirkt, durch `aegis.pruefen` in der echten Kammer
(gestellt nur Modell und Laufzeit, wie tests/test_vor_t4_03.py::_pruefen), sonst am Organ `verhaltensvergleich.pruefen`
in der echten Kammer (Proben des Gutachtens 04: review-proben/kammerprobe.py).

V  Entscheidung 1 — Vollständigkeitsprüfung: p22 Slots der Basisklasse, p21 verschleierte Slots, p18c Elemente eines
   Iterator-Objekts, p14 Iterator-Kappe, Pfad als Wert (os.fspath). Nie „0 Abweichungen, tragfähig“.
F  Entscheidung 2 — Festhalten heißt fallende Zusicherung (x3 Idempotenz).
A  Entscheidung 3 — Sondenausfall trifft nur die betroffene Funktion (q2 Zählerlast; q1 csv.DictReader nicht ersetzt).
K  Entscheidung 4 — Verfälschungskappe: zurückstellen mit Grund, gezählt.
S  Entscheidung 6 — Vorspann verweigert ohne Stufe 2; Kammerlauf über 60 s (gestellt).
L  Entscheidung 7 — Lastaufrufe tragen die Formmerkmale ihrer Eingabe.
E  Entscheidung 8 — eigene Tests nach Testkennung inkl. Parametrisierung; Maße an der Stufe der Laufzeitgrenze.
(Entscheidung 5 — Register, Tor-4-Skript, Nachspiel-Durchlauf: tests/test_verdrahtung.py.)
Die Tests laden neue Module (register, tor4) erst in der Testfunktion — so läuft die Datei auch am alten Code (Vorher).
"""
import sqlite3
import sys
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


def _norm_tests(faelle: dict) -> dict:
    return {f"tests/test_werk_normieren_{n}.py": R3.TEST_NORMIEREN.format(name=n, eingabe=e, erwartet=x)
            for n, (e, x) in faelle.items()}


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


# ================================================================ V Entscheidung 1: Vollständigkeitsprüfung
KV = ("class Basis:\n    __slots__ = ('stand',)\n\n    def __init__(self, stand: int):\n        self.stand = stand\n\n\n"
      "class Konto(Basis):\n    __slots__ = ('name',)\n\n    def __init__(self, stand: int):\n        super().__init__(stand)\n"
      "        self.name = 'k'\n\n    def buchen(self, b: int) -> None:\n        {}\n")
KM = ("class Konto:\n    __slots__ = ('__stand',)\n\n    def __init__(self, stand: int):\n        self.__stand = stand\n\n"
      "    def buchen(self, b: int) -> None:\n        self.__stand += {}b\n")
LAST_K = "from paket.m.a import Konto\nk = Konto(1)\nk.buchen(2)\nk.buchen(3)"


@pytest.mark.parametrize("fall,alt,neu", [
    # Review 04 Nr. 2 (p22): an 43b8fad 0 Abweichungen, tragfähig — kan() las nur die Slots der eigenen Klasse.
    ("p22_basis_slot", KV.format("self.stand += b"), KV.format("self.stand += 2 * b")),
    # Review 04 Nr. 3 (p21): verschleierter Slot-Name `__stand` → gespeichert als `_Konto__stand`; an 43b8fad 0 Abw.
    ("p21_verschleiert", KM.format(""), KM.format("2 * ")),
    # Gegenprobe (p22k): der eigene Slot — schon an 43b8fad gesehen (28)
    ("p22k_eigener_slot", KV.format("self.name += str(b)"), KV.format("self.name += str(2 * b)")),
])
def test_v1_zustand_aller_slots_verglichen(tmp_path, monkeypatch, fall, alt, neu):
    r = _organ(tmp_path, monkeypatch, alt, neu, LAST_K)
    assert r["geurteilt"] is True and r["tragfaehig"] is False and any(">args" in k for k in r["abweichungen"]), r
    assert not r.get("unvollstaendig"), r.get("unvollstaendig")        # vollständig erfasst: keine Enthaltung


def test_v1_gegenprobe_slots_umgeschrieben_bleibt_tragfaehig(tmp_path, monkeypatch):
    """Gegenprobe gegen Fehlalarm: dieselbe Wirkung anders geschrieben — 0 Abweichungen, geurteilt, tragfähig."""
    alt = KV.format("self.stand += b")
    neu = KV.format("neu = self.stand + b\n        self.stand = neu")
    r = _organ(tmp_path, monkeypatch, alt, neu, LAST_K)
    assert r["geurteilt"] is True and r["tragfaehig"] is True and r["anzahl_abweichungen"] == 0, r


LS2 = ("class Leser:\n    def __init__(self, text: str):\n        self.teile = text.split()\n        self.nummer = 0\n\n"
       "    def __iter__(self):\n        return self\n\n    def __next__(self) -> str:\n        if self.nummer >= len(self.teile):\n"
       "            raise StopIteration\n        self.nummer += 1\n        return self.teile[self.nummer - 1]{}\n\n\n"
       "def leser(text: str) -> 'Leser':\n    return Leser(text)\n")
GEN = "def leser(text: str):\n    for t in text.split():\n        yield t{}\n"
IT = "def zaehle(start: int):\n    n = start\n    while True:\n        yield n\n        n += {}\n"


def test_v1_iterator_objekt_elemente_nie_tragfaehig(tmp_path, monkeypatch):
    """Review 04 Nr. 5 (p18c): der Kandidat ändert nur die Elemente eines Iterator-Objekts des Werks — an 43b8fad
    0 Abweichungen, „1 von 1 beobachtet“, tragfähig. Jetzt: Elemente nicht erfasst → gezählte Enthaltung."""
    r = _organ(tmp_path, monkeypatch, LS2.format(""), LS2.format(".upper()"),
               "from paket.m.a import leser\nr = leser('a b c')\nx = list(r)")
    assert r["geurteilt"] is False and r["grund_art"] == "unvollstaendig_erfasst" and r["tragfaehig"] is False, r
    assert "paket.m.a:leser" in (r.get("unvollstaendig") or {}), r.get("unvollstaendig")
    assert (r.get("enthaltungen") or {}).get("paket.m.a:leser", "").startswith("unvollständig erfasst"), r.get("enthaltungen")


def test_v1_gegenprobe_generator_wird_geurteilt(tmp_path, monkeypatch):
    """Gegenprobe (p18ck): dieselbe Änderung als Generator — ausgelesen, geurteilt, abgelehnt (40 Abweichungen)."""
    r = _organ(tmp_path, monkeypatch, GEN.format(""), GEN.format(".upper()"), "from paket.m.a import leser\nx = list(leser('a b c'))")
    assert r["geurteilt"] is True and r["tragfaehig"] is False and r["anzahl_abweichungen"] > 0, r
    assert not r.get("unvollstaendig"), r.get("unvollstaendig")


def test_v1_iterator_kappe_nie_tragfaehig(tmp_path, monkeypatch):
    """Review 04 Nr. 5 (p14): Änderung jenseits der Iterator-Kappe — an 43b8fad tragfähig (nur `teilweise` gezählt).
    Die Kappe ist seit Runde 5 1000 Elemente (Befund TEILLAUF-1: 50 riss der eigene Randfall-Korpus); die Änderung liegt
    darum ab Element 1.100, die Last liest 1.200."""
    r = _organ(tmp_path, monkeypatch, IT.format("1"), IT.format("1 if n < start + 1100 else 2"),
               "from itertools import islice\nfrom paket.m.a import zaehle\nlist(islice(zaehle(0), 1200))")
    assert r["geurteilt"] is False and r["grund_art"] == "unvollstaendig_erfasst", r
    assert "gekappt" in str((r.get("unvollstaendig") or {}).get("paket.m.a:zaehle")), r.get("unvollstaendig")


PF = "from pathlib import Path\n\n\ndef ablage(name: str) -> Path:\n    return Path('{}') / name\n"


@pytest.mark.parametrize("neu_wurzel,tragfaehig", [("b", False), ("a", True)])
def test_v1_pfad_ist_ein_wert(tmp_path, monkeypatch, neu_wurzel, tragfaehig):
    """Review 04 Nr. 10: `kan(Path)` war inhaltslos ({"__klasse": "PosixPath", "felder": {}}) — ein anderer Pfad blieb
    unsichtbar. Jetzt os.fspath als Wert. Gegenprobe: derselbe Pfad — tragfähig, ohne Enthaltung."""
    r = _organ(tmp_path, monkeypatch, PF.format("a"), PF.format(neu_wurzel), "from paket.m.a import ablage\nablage('x.txt')")
    assert r["geurteilt"] is True and r["tragfaehig"] is tragfaehig, r
    assert not r.get("unvollstaendig"), r.get("unvollstaendig")


# ================================================================ F Entscheidung 2: fallende Zusicherung
K2 = '    if "\\t" in text:\n        return text\n    return "_".join(text.split())\n'
X3_BASIS = {"rand": (" a b ", "a_b"), "gross": ("A B", "A_B"), "lang": ("x " * 25, "_".join(["x"] * 25)),
            "zahlform": ("a 01 2.50", "a_01_2.50"), "nichtascii": ("Ä ö", "Ä_ö"), "lf": ("a\nb", "a_b"),
            "crlf": ("a\r\nb", "a_b"), "nbsp": ("a\u00a0b", "a_b"), "doppelt": ("a  b", "a_b")}


@pytest.mark.parametrize("mit_idem", [True, False])
def test_f2_idempotenz_haelt_tab_nicht_fest(tmp_path, monkeypatch, mit_idem):
    """Review 04 Nr. 1 (x3): `normieren(normieren("a\\tb c")) == normieren("a\\tb c")` hielt `tab` fest, weil der innere
    verfälschte Wert im äußeren Aufruf eine Ausnahme im WERK auslöste — an 43b8fad überlebte der Tab-Rückschritt.
    Jetzt hält nur eine fallende Zusicherung im Test fest. Gegenprobe (x3k) ohne diese Zeile: abgelehnt."""
    tests = _norm_tests(X3_BASIS)
    koerper = (('    assert normieren(normieren("a\\tb c")) == normieren("a\\tb c")\n' if mit_idem else "")
               + '    assert normieren("a b") == "a_b"\n')
    tests["tests/test_werk_normieren_x.py"] = "from probewerk.werk.kern import normieren\n\n\ndef test_normieren_x():\n" + koerper
    u, v = R3._pruefen(tmp_path, monkeypatch, R3._diff(QUELLE, QUELLE.replace(ALT_NORMIEREN, K2)), nische="sicher",
                       werk_extra=tests)
    assert u["status"] == "abgelehnt" and u["grund"].startswith("Verhaltensvergleich:"), u["grund"]
    fest = (v.get("deckung_zaehlung") or {}).get("festhaltend") or {}
    assert not any(t for k, t in fest.items() if k.endswith("|tab")), fest
    assert any("tab" in s.split(" | ")[1].split("+") for s in v.get("ungedeckt_aufschluesselung") or {}), v


def test_f2_zusicherung_faellt_am_ort_und_an_der_art():
    """Die Regel am Rechenweg der Sonde (kern/py/verhalten.py::_zusicherung_faellt), mit den Meldungen, die pytest 8.3.3
    in der Kammer liefert (proben/VORPROBE-E2.txt): Zusicherung im Test → fällt; Ausnahme bzw. assert im Werk → nicht."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("vh", Path(__file__).parent.parent / "biotop/kern/py/verhalten.py")
    vh = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(vh)

    def bericht(pfad, meldung):
        return SimpleNamespace(longrepr=SimpleNamespace(reprcrash=SimpleNamespace(path=pfad, message=meldung)))
    t = "tests/test_x.py"
    assert vh._zusicherung_faellt(bericht("/werk/tests/test_x.py", "AssertionError: assert 'a' == 'b'"), t) is True
    assert vh._zusicherung_faellt(bericht("/werk/tests/test_x.py", "Failed: DID NOT RAISE <class 'ValueError'>"), t) is True
    assert vh._zusicherung_faellt(bericht("/werk/paket/werk.py", "AttributeError: 'V' object has no attribute 'strip'"), t) is False
    assert vh._zusicherung_faellt(bericht("/werk/paket/werk.py", "AssertionError: werk-assert"), t) is False
    assert vh._zusicherung_faellt(bericht("/werk/tests/test_x.py", "TypeError: nope"), t) is False
    assert vh._zusicherung_faellt(SimpleNamespace(longrepr="Text ohne reprcrash"), t) is False


# ================================================================ A Entscheidung 3: Sondenausfall nur der Funktion
ZL = ("_n = [0]\n\n\ndef naechste() -> int:\n    _n[0] += 1\n    return _n[0]\n\n\n"
      "def doppel(x: int) -> int:\n    return {}\n")


def test_a3_sondenausfall_trifft_nur_die_betroffene_funktion(tmp_path, monkeypatch):
    """Die Sonde ruft jede Funktion mehrfach (@alias, Kopie …). Eine Last, die sich auf einen nicht idempotenten Zähler
    verlässt, bricht darum unter der Sonde ab — ohne Sonde läuft sie. An 43b8fad: Messgerätausfall für den ganzen
    Kandidaten (SondeAusgefallen). Jetzt: `naechste` enthält sich (Sondenausfall), der Lauf geht weiter und sieht die
    Änderung an doppel(3)."""
    last = "from paket.m.a import naechste, doppel\na = naechste()\nb = naechste()\nassert b == a + 1\ndoppel(3)"
    r = _organ(tmp_path, monkeypatch, ZL.format("2 * x"), ZL.format("2 * x + (1 if x == 3 else 0)"), last)
    assert r["tragfaehig"] is False and any(k.startswith("paket.m.a:doppel#") for k in r["abweichungen"]), r
    assert list(r.get("sonde_ausfall") or {}) == ["paket.m.a:naechste"], r.get("sonde_ausfall")
    assert (r.get("enthaltungen") or {}).get("paket.m.a:naechste", "").startswith("Sondenausfall"), r.get("enthaltungen")


def test_a3_gegenprobe_abbruch_auch_ohne_sonde_ist_verhalten_des_werks(tmp_path, monkeypatch):
    """Gegenprobe: bricht die Last auch ohne Sonde ab, ist das Verhalten des Werks — kein Sondenausfall."""
    last = "from paket.m.a import doppel\ndoppel(3)\nraise ValueError('werk')"
    r = _organ(tmp_path, monkeypatch, ZL.format("2 * x"), ZL.format("2 * x + (1 if x == 3 else 0)"), last)
    assert not r.get("sonde_ausfall") and r["tragfaehig"] is False, r
    assert any(k.startswith("paket.m.a:doppel#") for k in r["abweichungen"]), r["abweichungen"]


CSV = ("import csv\nimport io\n\n\ndef lies(text: str):\n    return csv.DictReader(io.StringIO(text))\n\n\n"
       "def doppel(x: int) -> int:\n    return {}\n")


def test_a3_dictreader_bleibt_objekt_und_die_last_laeuft(tmp_path, monkeypatch):
    """Review 04 Nr. 4 (q1): csv.DictReader wurde durch einen Generator ersetzt, `r.fieldnames` brach die Last ab —
    Messgerätausfall für jeden Kandidaten. Jetzt bleibt das Objekt (Datenattribute), die Last läuft, doppel(3) wird
    gesehen; `lies` ist unvollständig erfasst (Iterator-Objekt)."""
    r = _organ(tmp_path, monkeypatch, CSV.format("2 * x"), CSV.format("2 * x + (1 if x == 3 else 0)"),
               "from paket.m.a import lies, doppel\nr = lies('a,b\\n1,2\\n')\nn = r.fieldnames\ndoppel(3)")
    assert r["tragfaehig"] is False and any(k.startswith("paket.m.a:doppel#") for k in r["abweichungen"]), r
    assert "paket.m.a:lies" in (r.get("unvollstaendig") or {}) and not r.get("sonde_ausfall"), r


# ================================================================ K Entscheidung 4: Verfälschungskappe
SOLL_ALLE = {"gewoehnlich": ("a b", "a_b"), "rand": (" a b ", "a_b"), "gross": ("A B", "A_B"),
             "lang": ("x " * 25, "_".join(["x"] * 25)), "zahlform": ("a 01 2.50", "a_01_2.50"), "nichtascii": ("Ä ö", "Ä_ö"),
             "tab": ("a\tb", "a_b"), "lf": ("a\nb", "a_b"), "crlf": ("a\r\nb", "a_b"), "nbsp": ("a\u00a0b", "a_b"),
             "doppelt": ("a  b", "a_b")}


@pytest.mark.parametrize("kappe,status", [(2, "zurueckgestellt"), (24, "ueberlebt")])
def test_k4_kappe_stellt_zurueck_mit_grund(tmp_path, monkeypatch, kappe, status):
    """Review 04 Nr. 6: jenseits der Kappe blieben Abweichungen ungedeckt — Ablehnung ohne Grund. Jetzt: hängt jede
    ungedeckte Abweichung an einer ausgelassenen Probe, stellt der Annahmepfad zurück, mit Grund und gezählt. Gegenprobe:
    dieselbe richtige Behebung mit der Kappe 24 (Bedarf darunter) überlebt."""
    monkeypatch.setattr(vv, "VERFAELSCHUNG_KAPPE", kappe)
    neu = QUELLE.replace(ALT_NORMIEREN, '    return "_".join(text.split())\n')
    u, v = R3._pruefen(tmp_path, monkeypatch, R3._diff(QUELLE, neu), nische="sicher", werk_extra=_norm_tests(SOLL_ALLE))
    assert u["status"] == status, u["grund"]
    if status == "zurueckgestellt":
        assert "Verfälschungsproben" in u["grund"] and "Kappe 2" in u["grund"], u["grund"]
        assert (v.get("deckung_zaehlung") or {}).get("ausgelassen", 0) > 0, v.get("deckung_zaehlung")


def test_k4_gegenprobe_ungedeckt_ohne_kappe_lehnt_ab(tmp_path, monkeypatch):
    """Gegenprobe: eine Abweichung, für die es gar keinen passenden Test gibt, lehnt weiter ab — auch mit kleiner Kappe."""
    monkeypatch.setattr(vv, "VERFAELSCHUNG_KAPPE", 2)
    neu = QUELLE.replace(ALT_NORMIEREN, '    return "_".join(text.split())\n')
    u, _ = R3._pruefen(tmp_path, monkeypatch, R3._diff(QUELLE, neu), nische="sicher",
                       werk_extra=_norm_tests({"gewoehnlich": ("a b", "a_b")}))
    assert u["status"] == "abgelehnt" and u["grund"].startswith("Verhaltensvergleich:"), u["grund"]


# ================================================================ S Entscheidung 6: Vorspann und Stufe 2
from test_vorspann import unit_vorspann  # noqa: E402,F401


def test_s6_vorspann_verweigert_ohne_stufe2(unit_vorspann, monkeypatch):
    from biotop import lauf as L
    from biotop.organe import vorspann as V
    con, raw = unit_vorspann
    monkeypatch.setattr(L, "_referenzlast", lambda name, paket=None, stufe=1: None if stufe == 2 else "# Unit-Referenzlast")
    with pytest.raises(V.VorspannFehler, match="Stufe 2 fehlt"):
        V.ausfuehren(con, 1)
    assert raw["reihenfolge"] == []             # keine Messung vor der Verweigerung


@pytest.mark.parametrize("dauer,verweigert", [(61.0, True), (59.0, False)])
def test_s6_vorspann_verweigert_kammerlauf_ueber_60s(unit_vorspann, monkeypatch, dauer, verweigert):
    """Entscheidung 6 (Review 04 Nr. 8): gestellte Dauer eines Kammerlaufs der Stufe 2; Gegenprobe knapp darunter."""
    from biotop.organe import eichung
    from biotop.organe import vorspann as V
    con, raw = unit_vorspann
    alt = eichung.rauschmessung

    def rauschen(*a, **k):
        return dict(alt(*a, **k), kammerlauf_s=[12.0, dauer, 11.0])
    monkeypatch.setattr(eichung, "rauschmessung", rauschen)
    if verweigert:
        with pytest.raises(V.VorspannFehler, match="60 s"):
            V.ausfuehren(con, 1)
    else:
        assert V.ausfuehren(con, 1)["laufzeit_stufe"] == 2


def test_s6_stufe2_eingang_bemessen():
    """Die Stufe-2-Last von eingang ist wie Stufe 1 gemessen gewählt (proben/STUFE2-EICHUNG: W 60 sperrte 3 von 8
    Rauschmessungen, W 240 0 von 8)."""
    from biotop import lauf as L
    s2 = L._referenzlast("versandwerk-t3-02", "src", 2)
    assert "const W = { eingang: 240," in s2 and "sendungen(900)" in s2


# ================================================================ L Entscheidung 7: Formmerkmale der Lastaufrufe
def test_l7_lastaufruf_traegt_formmerkmal_seiner_eingabe(tmp_path, monkeypatch):
    """Review 04 Nr. 9: Lastaufrufe hatten immer das gewöhnliche Muster — ein Test mit gewöhnlicher Eingabe deckte eine
    Regression, die nur der Tab der Last zeigt. Jetzt trägt der Lastaufruf `tab`: ungedeckt."""
    monkeypatch.setattr(R3, "REFERENZLAST", R3.REFERENZLAST.replace('normieren("  wort   wort  ")', 'normieren("wort\\twort wort")'))
    soll = {"gewoehnlich": ("a b", "a_b"), "rand": (" a b ", "a_b")}
    u, v = R3._pruefen(tmp_path, monkeypatch, R3._diff(QUELLE, QUELLE.replace(ALT_NORMIEREN, K2)), nische="sicher",
                       werk_extra=_norm_tests(soll))
    assert u["status"] == "abgelehnt", u["grund"]
    last = [s for s in v.get("ungedeckt_aufschluesselung") or {} if s.endswith("rueckgabe/last")]
    assert last and all("tab" in s.split(" | ")[1].split("+") for s in last), v.get("ungedeckt_aufschluesselung")


# ================================================================ E Entscheidung 8
EIGEN_PARAM = ("import pytest\nfrom probewerk.werk.kern import normieren\n\n\n"
               "@pytest.mark.parametrize('x', ['a\\tb'], ids=['tab'])\n"
               "def test_werk_rueckschritt_tab(x):\n    \"\"\"Verfassung Satz 2: Steuerzeichen werden abgewiesen.\"\"\"\n"
               "    with pytest.raises(ValueError):\n        normieren(x)\n    assert normieren('a b') == 'a_b'\n")
K_TAB = '    if "\\t" in text:\n        raise ValueError("Tab")\n    return "_".join(text.split())\n'
VERFASSUNG = {"text": "1. Zweck: Prüfwerk ohne Betriebszweck.\n2. Sicherheit: Eingaben sind Daten.\n", "regeln": {}}
SOLL_OHNE_TAB = {k: v for k, v in SOLL_ALLE.items() if k != "tab"}


@pytest.mark.parametrize("ausschluss,status", [("kennung", "abgelehnt"), ("exakt", "ueberlebt")])
def test_e8_parametrisierter_eigener_test_deckt_nicht(tmp_path, monkeypatch, ausschluss, status):
    """Review 04 Nr. 16: ein parametrisierter eigener Test (ID 'datei::name[tab]') — jetzt aufgenommen (gültig nach der
    Norm-Regel) und nach Testkennung ausgeschlossen: abgelehnt. Gegenprobe (Ausschluss nur nach exakter Kennung, der
    Stand von 43b8fad): derselbe Test deckt den eigenen Rückschritt — der Kandidat überlebt. Das ist die Lücke."""
    monkeypatch.setattr(aegis.verfassung, "lesen", lambda *a: VERFASSUNG)
    if ausschluss == "exakt":
        monkeypatch.setattr(aegis, "ist_eigener_test", lambda t, eigene: t in eigene)
    diff = R3._diff(QUELLE, QUELLE.replace(ALT_NORMIEREN, K_TAB), tests={"tests/test_werk_eigen.py": EIGEN_PARAM})
    u, v = R3._pruefen(tmp_path, monkeypatch, diff, nische="sicher", werk_extra=_norm_tests(SOLL_OHNE_TAB))
    assert u["status"] == status, u["grund"]
    if status == "abgelehnt":
        assert any(t.endswith("test_werk_rueckschritt_tab[tab]") for t in v.get("eigene_tests_ausgeschlossen") or []), v


def test_e8_ist_eigener_test_nach_kennung():
    eigene = {"test_a.py::test_x", "b.test.ts::fall %s", "b.test.ts::wert $n"}
    assert aegis.ist_eigener_test("test_a.py::test_x[1-2]", eigene) is True
    assert aegis.ist_eigener_test("test_a.py::test_xy", eigene) is False
    assert aegis.ist_eigener_test("b.test.ts::fall 3", eigene) is True
    assert aegis.ist_eigener_test("b.test.ts::wert 7", eigene) is True
    assert aegis.ist_eigener_test("b.test.ts::anderer", eigene) is False


def test_e8_messung_an_der_stufe_der_laufzeitgrenze(tmp_path, monkeypatch):
    """Review 04 Nr. 15: die Einzelmessung im Annahmepfad lief an Stufe 1, die gepaarte an Stufe 2 — gespeicherte Maße
    mischten die Stufen. Jetzt misst `messen` an derselben Stufe; die Stufe steht im gespeicherten Maß."""
    gesehen = []
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
        gesehen.append(ref)
        return {"gueltig": True, "kernmass": 0, "werk": {"baut": True, "zyklen": 0, "bauzeit_ms": 100,
                "tests_fehlgeschlagen_liste": [], "tests_fehlgeschlagen_ids": []},
                "bereiche": {"alpha": {"tests_bestanden": 1, "tests_fehlgeschlagen": 0, "sicherheit_punkte": 0,
                                       "sicherheit_befunde": [], "tote_funktionen": 0, "laufzeit_ms": None, "groesste_funktion": 3}}}
    monkeypatch.setattr(aegis.messgeraet, "messen", messen)
    monkeypatch.setattr(messgeraet, "laufzeit_messen", lambda werk, bereiche, paket, ref, dateien=None, zeitlimit_s=150:
                        {"gueltig": True, "grund": "", "bereiche": {"alpha": {"laufzeit_ms": 8.0 if dateien else 10.0}}})
    ok = {"gueltig": True, "beobachtungen": {"alpha/a:a#0": "1"}, "eingewickelt": {"alpha/a": ["a"]}, "inhalt": {"alpha/a:a": 1}}
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: dict(ok))
    basis = messen(w, ["alpha"], "src", None)
    gesehen.clear()
    u = aegis.pruefen(con, 1, 1, 7, w, "src", ["alpha"], [], basis, basis, "// last",
                      {"laufzeit_faktor": 2.0, "_rauschtoleranz": {"alpha": 1.2}}, referenzlast_laufzeit="// last stufe 2")
    import json
    masse = json.loads(con.execute("SELECT masse FROM kandidaten WHERE id=7").fetchone()[0])
    assert gesehen == ["// last stufe 2", "// last stufe 2"] and masse.get("laufzeit_stufe") == 2, (gesehen, u["grund"])
