"""Behebungsrunde 3 vor T4 — Laufweg-Tests (tests/test_vor_t4_03.py). Je Punkt Probe und Gegenprobe; wo ein Organ im
Annahmepfad wirkt, durch `aegis.pruefen` (die Funktion, die ein Lauf je Kandidat ruft).

A. Die fünf Lücken der Python-Sonde aus Review 02 — je ein Fall, der an 6243377 unentdeckt blieb oder Fehlalarm gab,
   an einem Python-Prüfwerk durch aegis.pruefen in der echten Kammer (biotop-kammer:1); gestellt sind nur das Modell
   (KEIN ANGRIFF) und die Laufzeitmessung (Kandidat 20 % schneller: so erreicht er den Verhaltensvergleich):
   1 Generator-Ausgabe geändert → abgelehnt (vorher 0 Abweichungen) | Gegenprobe gleiche Ausgabe → überlebt
   2 in-place-Sortierung umgedreht → abgelehnt (vorher 0)            | Gegenprobe gleiche Sortierung → überlebt
   3 Funktion, deren Aufrufe nur Fehler liefern → Enthaltung, nicht „beobachtet“ (vorher „1 von 1“)
   4 Mengenreihenfolge (verhaltensgleicher Kandidat) → überlebt (vorher 22 Fehlalarme, abgelehnt)
   5 @lru_cache auf reiner Funktion → überlebt (vorher 16 von 16 „ungedeckt“, abgelehnt) | Gegenprobe falscher Cache
B. Entscheidung 1 (Deckung je Muster): ein Test je Muster lässt eine richtige Behebung durch; fehlt der Test für das
   Weißraum-Muster, bleibt sie abgelehnt; ein Test, der die Funktion nur nebenbei ruft, deckt nichts.
C. Entscheidung 2 (Gewinnschwelle in beiden Richtungen, nur im Rauschband): durch aegis.pruefen.
D. Entscheidung 3 (Methoden): geänderte Methode → abgelehnt; Zustand von self; Instanz aus dem Vertrag.
E. Spezifikationen S-6, S-8, S-9 (laufzeitrisse), S-11, S-12 (Zeitlimit, blinder Aufzeichner), Wurzelmodul (S-3).
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


# ================================================================ Prüfwerk „probewerk“ (Python) und Laufweg
PAKET = "probewerk"
QUELLE = '''"""Kleines Python-Prüfwerk für die Lücken der Sonde (Behebungsrunde 3 vor T4)."""
import functools


def zahlen(n: int):
    """Die ersten n natürlichen Zahlen als Generator."""
    yield from range(n)


def sortiere(xs: list[int]) -> None:
    """Sortiert an Ort und Stelle, aufsteigend."""
    xs.sort()


def verbinde(a, b):
    """Hilfsfunktion ohne Annotation, von der Last nicht gerufen."""
    return a.strip() + b


def woerter(s: str) -> list:
    """Die verschiedenen Wörter eines Textes (Reihenfolge unbestimmt)."""
    return list(set(s.split()))


def quadrat(x: int) -> int:
    """Quadrat einer ganzen Zahl."""
    return x * x


def normieren(text: str) -> str:
    """Weißraumfolgen (Leerzeichen, Tab, Zeilenumbruch) zu einem Leerzeichen, Ränder entfernt."""
    return " ".join(text.split())


def _alt(text: str) -> str:
    """Frühere Fassung, nirgends aufgerufen (toter Code — Vulture zählt ihn)."""
    return text.strip()


class Konto:
    """Ein Konto mit Stand in Cent."""

    def __init__(self, stand: int):
        self.stand = stand

    def buchen(self, betrag: int) -> int:
        """Bucht einen Betrag und liefert den neuen Stand."""
        self.stand += betrag
        return self.stand

    @property
    def doppelt(self) -> int:
        return self.stand * 2
'''
TESTS = '''from probewerk.werk.kern import zahlen, sortiere, woerter, quadrat, normieren, Konto


def test_zahlen():
    assert list(zahlen(3)) == [0, 1, 2]


def test_sortiere():
    xs = [3, 1, 2]
    sortiere(xs)
    assert xs == [1, 2, 3]


def test_woerter():
    assert sorted(woerter("b a b")) == ["a", "b"]


def test_quadrat():
    assert quadrat(4) == 16


def test_konto():
    assert Konto(3).buchen(1) == 4
'''
VERTRAG = '''from probewerk.werk.kern import Konto


def test_vertrag_konto():
    k = Konto(100)
    assert k.buchen(5) == 105
'''
# `normieren` hat bewusst KEINEN Werkstest: Gruppe B ändert sein Verhalten absichtlich (eine „richtige Behebung“); ein
# Werkstest auf das alte Verhalten fiele am Kandidaten, und die Verfassung verbietet, ihn zu ändern — der Kandidat
# schiede dann am Pareto-Maß aus, bevor der Verhaltensvergleich urteilt (gemessen in TEILLAUF-3/-4).
REFERENZLAST = '''import sys
sys.path.insert(0, "/werk")


def last_werk():
    from probewerk.werk.kern import zahlen, sortiere, woerter, quadrat, normieren, Konto
    for i in range(30):
        list(zahlen(5))
        xs = [(i * 7) % 11, 3, 1, 8]
        sortiere(xs)
        woerter("alpha beta gamma delta epsilon zeta eta theta")
        quadrat(i % 5)
        normieren("  wort   wort  ")
        Konto(i).buchen(2)
'''


def _anlegen(w: Path, extra: dict | None = None):
    for rel, text in {**(extra or {}), "probewerk/__init__.py": "", "probewerk/werk/__init__.py": "", "probewerk/werk/kern.py": QUELLE, "tests/test_werk.py": TESTS,
                      "tests/vertraege/__init__.py": "", "tests/vertraege/test_vertrag_werk.py": VERTRAG,
                      "pyproject.toml": '[project]\nname = "probewerk"\nversion = "0.1.0"\n',
                      "README.md": "# probewerk\n\nPrüfwerk ohne Betriebszweck.\n"}.items():
        (w / rel).parent.mkdir(parents=True, exist_ok=True)
        (w / rel).write_text(text)


def _diff(alt: str, neu: str, rel: str = "probewerk/werk/kern.py", tests: dict | None = None) -> str:
    import difflib
    d = "".join(difflib.unified_diff(alt.splitlines(True), neu.splitlines(True), f"a/{rel}", f"b/{rel}"))
    for p, t in (tests or {}).items():
        d += "".join(difflib.unified_diff([], t.splitlines(True), "/dev/null", f"b/{p}"))
    return d


def _ersetzen(alt: str, neu: str) -> str:
    assert QUELLE.count(alt) == 1, alt
    return QUELLE.replace(alt, neu)


def _pruefen(tmp_path, monkeypatch, diff, nische="schnell", werk_extra=None):
    monkeypatch.setattr(kammer, "IMAGE", "biotop-kammer:1")
    w = tmp_path / "werk"
    _anlegen(w, werk_extra)
    con = sqlite3.connect(":memory:", isolation_level=None)
    con.row_factory = sqlite3.Row
    con.executescript(datenbank.SCHEMA)
    con.execute("INSERT INTO kandidaten(id,lauf_id,generation,bereich,nische,status,diff) VALUES(7,1,1,'werk',?,'erzeugt',?)",
                (nische, diff))
    monkeypatch.setattr(aegis, "aufrufen", lambda *a, **k: SimpleNamespace(text="KEIN ANGRIFF"))
    basis = messgeraet.messen(w, ["werk"], PAKET, REFERENZLAST)
    assert basis["gueltig"], basis.get("grund")

    def laufzeit(werk, bereiche, paket, ref, dateien=None, zeitlimit_s=150):
        return {"gueltig": True, "grund": "", "bereiche": {b: {"laufzeit_ms": 4.0 if dateien else 5.0} for b in bereiche}}
    monkeypatch.setattr(messgeraet, "laufzeit_messen", laufzeit)
    u = aegis.pruefen(con, 1, 1, 7, w, PAKET, ["werk"], [], basis, basis, REFERENZLAST, {"_rauschtoleranz": {"werk": 1.2}})
    z = con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil' ORDER BY nr DESC LIMIT 1").fetchone()
    return u, json.loads(z[0]).get("verhalten") or {}


# ---------------------------------------------------------------- A1 Generator
def test_a1_generator_ausgabe_geaendert_wird_abgelehnt(tmp_path, monkeypatch):
    """Review 02 Nr. 1 (p1): an 6243377 0 Abweichungen, „beobachtet“, tragfähig. Die Änderung wirkt erst ab n = 5: der
    Werkstest (zahlen(3)) sieht sie nicht — nur die Sonde kann sie finden (Last: zahlen(5))."""
    neu = _ersetzen("    yield from range(n)\n", "    yield from (range(n) if n < 5 else range(1, n + 1))\n")
    u, v = _pruefen(tmp_path, monkeypatch, _diff(QUELLE, neu))
    assert u["status"] == "abgelehnt" and u["grund"].startswith("Verhaltensvergleich:"), u["grund"]
    assert any(k.startswith("probewerk.werk.kern:zahlen#") for k in v["ungedeckt"]), v


def test_a1_gegenprobe_generator_gleiche_ausgabe_ueberlebt(tmp_path, monkeypatch):
    neu = _ersetzen("    yield from range(n)\n", "    for i in range(n):\n        yield i\n")
    u, v = _pruefen(tmp_path, monkeypatch, _diff(QUELLE, neu))
    assert u["status"] == "ueberlebt" and v["anzahl_abweichungen"] == 0, (u["grund"], v)


# ---------------------------------------------------------------- A2 Nebenwirkung an der Eingabe
def test_a2_inplace_sortierung_umgedreht_wird_abgelehnt(tmp_path, monkeypatch):
    """Review 02 Nr. 2 (p2): Rückgabe None auf beiden Seiten, an 6243377 0 Abweichungen."""
    # Die Änderung wirkt erst ab 4 Elementen: der Werkstest (3 Elemente) sieht sie nicht, die Last (4 Elemente) schon.
    neu = _ersetzen("    xs.sort()\n", "    xs.sort(reverse=len(xs) > 3)\n")
    u, v = _pruefen(tmp_path, monkeypatch, _diff(QUELLE, neu))
    assert u["status"] == "abgelehnt" and u["grund"].startswith("Verhaltensvergleich:"), u["grund"]
    assert any(k.startswith("probewerk.werk.kern:sortiere#") and ">args" in k for k in v["ungedeckt"]), v


def test_a2_gegenprobe_gleiche_sortierung_anders_geschrieben_ueberlebt(tmp_path, monkeypatch):
    """Erste Fassung `xs[:] = sorted(xs)` wurde an der Behälter-Formvariante (Tupel) abgelehnt: dort wirft die
    Vorgeneration AttributeError, die Fassung TypeError — eine echte Abweichung bei ungültiger Eingabe, die nach
    Grundsatz 11 einen deckenden Test braucht. Die Gegenprobe ist deshalb eine auch im Fehlerfall gleiche Fassung."""
    neu = _ersetzen("    xs.sort()\n", "    xs.sort(key=lambda v: v)\n")
    u, v = _pruefen(tmp_path, monkeypatch, _diff(QUELLE, neu))
    assert u["status"] == "ueberlebt" and v["anzahl_abweichungen"] == 0, (u["grund"], v)


# ---------------------------------------------------------------- A3 nur Fehleraufrufe
def test_a3_funktion_ohne_annotation_wird_mit_tastendem_korpus_gesehen(tmp_path, monkeypatch):
    """Review 02 Nr. 3 (p4): `verbinde` ohne Annotation, nicht von der Last gerufen; an 6243377 endeten 3 von 3
    Randfällen ([None, None], [[], None], [None, []]) mit `AttributeError` auf beiden Seiten — die Änderung blieb
    unsichtbar, und die Funktion zählte trotzdem als „beobachtet“. Jetzt tastet der Korpus mit 'a b', 1, 0, [], None,
    und nur inhaltliche Aufrufe zählen (Gegenprobe am Organ unten)."""
    neu = _ersetzen("    return a.strip() + b\n", "    return a.strip().upper() + b\n")
    u, v = _pruefen(tmp_path, monkeypatch, _diff(QUELLE, neu))
    assert u["status"] == "abgelehnt" and any(k.startswith("probewerk.werk.kern:verbinde~") for k in v["ungedeckt"]), (u["grund"], v)


def test_a3_gegenprobe_zaehlung_nur_inhaltliche_aufrufe(tmp_path, monkeypatch):
    """Am Organ: eine Funktion, deren Beobachtungen auf beiden Seiten nur Fehler sind, zählt nicht als beobachtet."""
    w = tmp_path / "w"
    (w / "paket").mkdir(parents=True)
    seite = {"gueltig": True, "beobachtungen": {"paket.a:f~rand#0": "Fehler:AttributeError", "paket.a:g#0": "1"},
             "eingewickelt": {"paket.a": ["f", "g"]}, "inhalt": {"paket.a:g": 1}, "muster": {}}
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: dict(seite))
    r = vv.pruefen(w, {"paket/a.py": "x"}, "last", ["paket"], {})
    assert r["beobachtete_funktionen"] == "1 von 2" and r["enthaltungen"] == {"paket.a:f": "nur Fehler oder nicht vergleichbar"}, r


# ---------------------------------------------------------------- A4 Hash-Reihenfolge
def test_a4_mengenreihenfolge_ist_kein_fehlalarm(tmp_path, monkeypatch):
    """Review 02 Nr. 4 (p5): der Kandidat ändert nur `quadrat` verhaltensgleich; `woerter` liefert list(set(…)).
    An 6243377: 22 ungedeckte Abweichungen an `woerter`, abgelehnt, 2 von 2 Wiederholungen."""
    neu = _ersetzen("    return x * x\n", "    return x ** 2\n")
    u, v = _pruefen(tmp_path, monkeypatch, _diff(QUELLE, neu))
    assert u["status"] == "ueberlebt" and v["anzahl_abweichungen"] == 0, (u["grund"], v)
    assert v["hashsaat"] == "0", v


def test_a4_gegenprobe_instabile_vorgeneration_wird_enthaltung(tmp_path, monkeypatch):
    """Ohne feste Saat (oder bei anderem Nichtdeterminismus) schwankt die Vorgeneration zwischen zwei Beobachtungen:
    diese Beobachtungen sind Enthaltungen (`instabil`), keine Abweichungen — am Organ, Kammer gestellt."""
    w = tmp_path / "w"
    (w / "paket").mkdir(parents=True)
    folge = iter([{"gueltig": True, "beobachtungen": {"paket.a:f#0": '["a","b"]', "paket.a:g#0": "1"}, "inhalt": {"paket.a:g": 1, "paket.a:f": 1}},
                  {"gueltig": True, "beobachtungen": {"paket.a:f#0": '["b","a"]', "paket.a:g#0": "1"}, "inhalt": {"paket.a:g": 1, "paket.a:f": 1}},
                  {"gueltig": True, "beobachtungen": {"paket.a:f#0": '["a","b"]', "paket.a:g#0": "1"}, "inhalt": {"paket.a:g": 1, "paket.a:f": 1}}])
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: next(folge))
    r = vv.pruefen(w, {"paket/a.py": "x"}, "last", ["paket"], {})
    assert r["instabil"] == 1 and r["tragfaehig"] is True and r["anzahl_abweichungen"] == 0, r


# ---------------------------------------------------------------- A5 lru_cache
def test_a5_lru_cache_auf_reiner_funktion_ist_kein_fehlalarm(tmp_path, monkeypatch):
    """Review 02 Nr. 5 (p12): an 6243377 fehlten am Kandidaten alle Lastbeobachtungen — 16 von 16 „ungedeckt“."""
    neu = _ersetzen("def quadrat(x: int) -> int:\n", "@functools.lru_cache(maxsize=None)\ndef quadrat(x: int) -> int:\n")
    u, v = _pruefen(tmp_path, monkeypatch, _diff(QUELLE, neu))
    assert u["status"] == "ueberlebt" and v["anzahl_abweichungen"] == 0, (u["grund"], v)
    assert "quadrat" in (v.get("eingewickelt") or {}).get("probewerk.werk.kern", []), v


def test_a5_gegenprobe_falscher_cache_wird_abgelehnt(tmp_path, monkeypatch):
    """Ein Cache, der an der Identität der Liste hängt (T3-Muster), bleibt ein Befund — auch dekoriert."""
    neu = _ersetzen('''def sortiere(xs: list[int]) -> None:
    """Sortiert an Ort und Stelle, aufsteigend."""
    xs.sort()
''', '''_GESEHEN: dict[int, list] = {}


def sortiere(xs: list[int]) -> None:
    """Sortiert an Ort und Stelle, aufsteigend."""
    if id(xs) in _GESEHEN:
        xs[:] = _GESEHEN[id(xs)]
        return
    xs.sort()
    _GESEHEN[id(xs)] = list(xs)
''')
    u, v = _pruefen(tmp_path, monkeypatch, _diff(QUELLE, neu))
    assert u["status"] == "abgelehnt" and u["grund"].startswith("Verhaltensvergleich:"), u["grund"]


# ================================================================ D. Methoden (Entscheidung 3)
def test_d_geaenderte_methode_wird_abgelehnt(tmp_path, monkeypatch):
    """Review 02 Nr. 11 (p3): an 6243377 „1 von 1 beobachtet“, tragfähig — Klassen gingen nicht in y ein."""
    # wirkt nur bei betrag == 2 (Last); Werkstest (1) und Vertrag (5) sehen es nicht
    neu = _ersetzen("        self.stand += betrag\n", "        self.stand += 2 * betrag if betrag == 2 else betrag\n")
    u, v = _pruefen(tmp_path, monkeypatch, _diff(QUELLE, neu))
    assert u["status"] == "abgelehnt" and any("Konto.buchen" in k for k in v["ungedeckt"]), (u["grund"], v)
    assert v["instanzen"].get("probewerk.werk.kern:Konto") == "vertrag", v       # Instanz aus dem Vertrag


def test_d_gegenprobe_methode_umgeschrieben_ueberlebt(tmp_path, monkeypatch):
    neu = _ersetzen("        self.stand += betrag\n        return self.stand\n",
                    "        neu = self.stand + betrag\n        self.stand = neu\n        return neu\n")
    u, v = _pruefen(tmp_path, monkeypatch, _diff(QUELLE, neu))
    assert u["status"] == "ueberlebt" and v["anzahl_abweichungen"] == 0, (u["grund"], v)
    y = int(v["beobachtete_funktionen"].split(" von ")[1])
    assert y >= 8, v          # 6 Funktionen + Konto.buchen + Konto.doppelt


def test_d_zustand_von_self_nach_dem_aufruf_wird_verglichen(tmp_path, monkeypatch):
    """Die Rückgabe bleibt gleich, nur der Zustand von self nach dem Aufruf ändert sich."""
    neu = _ersetzen("        self.stand += betrag\n        return self.stand\n",
                    "        alt = self.stand\n        self.stand += betrag\n        self.letzte = betrag\n        return alt + betrag\n")
    u, v = _pruefen(tmp_path, monkeypatch, _diff(QUELLE, neu))
    assert u["status"] == "abgelehnt" and any("Konto.buchen" in k and k.endswith(">args") for k in v["ungedeckt"]), (u["grund"], v)


# ================================================================ B. Deckung je Muster (Entscheidung 1) durch aegis.pruefen
# Die Tests der Gruppe B stehen als Soll-Tests IM WERK und sind an der Vorgeneration rot; der Kandidat ändert nur die
# Quelle und macht sie grün. So steigt das Kernmaß (neue Tests eines Kandidaten zählen nicht: „bestandene Tests zählen
# nicht“, und vorhandene Testdateien darf er nicht ändern — Verfassung, Anhang A Satz 6), und der Verhaltensvergleich
# urteilt mit genau diesen Tests als deckenden Tests (fallen an der Vorgeneration, bestehen am Kandidaten).
TEST_NORMIEREN = '''from probewerk.werk.kern import normieren


def test_normieren_{name}():
    assert normieren({eingabe!r}) == {erwartet!r}
'''


def test_b_richtige_behebung_mit_test_je_muster_kommt_durch(tmp_path, monkeypatch):
    """Eine beabsichtigte Verhaltensänderung (normieren ersetzt Weißraum jetzt durch '_') mit einem Test je Muster, das
    die Sonde zeigt — gewöhnlich, Weißraum, Randweißraum, groß/klein, lang, Zahlform, leer, Nicht-ASCII: überlebt."""
    neu = _ersetzen('    return " ".join(text.split())\n', '    return "_".join(text.split())\n')
    # Jeder Test fällt an der Vorgeneration (dort " " statt "_") und besteht am Kandidaten; je Muster einer.
    faelle = {"gewoehnlich": ("a b", "a_b"), "weissraum": ("a\tb\nc", "a_b_c"), "rand": (" a b ", "a_b"),
              "gross": ("A B", "A_B"), "lang": ("x " * 25, "_".join(["x"] * 25)),
              "zahlform": ("a 01 2.50", "a_01_2.50"), "nichtascii": ("Ä ö", "Ä_ö"), "doppelt": ("a  b", "a_b")}
    tests = {f"tests/test_werk_normieren_{n}.py": TEST_NORMIEREN.format(name=n, eingabe=e, erwartet=x) for n, (e, x) in faelle.items()}
    u, v = _pruefen(tmp_path, monkeypatch, _diff(QUELLE, neu), nische="sicher", werk_extra=tests)
    assert v.get("anzahl_abweichungen", 0) > 0, v
    assert v["ungedeckt"] == [], (v.get("ungedeckt_aufschluesselung"), v.get("deckung_zaehlung"))
    assert u["status"] != "abgelehnt" or not u["grund"].startswith("Verhaltensvergleich:"), u["grund"]


def test_b_gegenprobe_ohne_test_fuer_das_weissraum_muster_bleibt_abgelehnt(tmp_path, monkeypatch):
    """Dieselbe Behebung, aber ohne Tests für Weißraum (Tab/Zeilenumbruch/doppelt): die Weißraum-Abweichungen bleiben
    ungedeckt — die K2868-Lage."""
    neu = _ersetzen('    return " ".join(text.split())\n', '    return "_".join(text.split())\n')
    faelle = {"gewoehnlich": ("a b", "a_b"), "rand": (" a b ", "a_b"), "gross": ("A B", "A_B"),
              "lang": ("x " * 25, "_".join(["x"] * 25)), "zahlform": ("a 01 2.50", "a_01_2.50"),
              "nichtascii": ("Ä ö", "Ä_ö")}
    tests = {f"tests/test_werk_normieren_{n}.py": TEST_NORMIEREN.format(name=n, eingabe=e, erwartet=x) for n, (e, x) in faelle.items()}
    u, v = _pruefen(tmp_path, monkeypatch, _diff(QUELLE, neu), nische="sicher", werk_extra=tests)
    assert u["status"] == "abgelehnt" and u["grund"].startswith("Verhaltensvergleich:"), u["grund"]
    assert v["ungedeckt"] and all("weissraum" in s for s in v["ungedeckt_aufschluesselung"]), v["ungedeckt_aufschluesselung"]


@pytest.mark.parametrize("haelt_fest", [False, True])
def test_b_test_der_nur_nebenbei_ruft_deckt_nicht(tmp_path, monkeypatch, haelt_fest):
    """Review 02 Nr. 8 (p6): `test_g_neu` sicherte nur g(1) == 2 zu und rief f('a') nebenbei — und deckte f. Hier: der
    Kandidat ändert normieren und quadrat; der Test ruft normieren("a b") und sichert nur quadrat zu. Verfälscht der
    Aufzeichner das Ergebnis von normieren, besteht der Test weiter — er hält normieren nicht fest: die gewöhnlichen
    normieren-Abweichungen bleiben ungedeckt. Gegenprobe (haelt_fest): derselbe Test sichert auch normieren zu — dann
    sind sie gedeckt."""
    neu = _ersetzen('    return " ".join(text.split())\n', '    return "_".join(text.split())\n')
    # quadrat ändert sich nur bei x == 1 — der Werkstest quadrat(4) == 16 sieht es nicht; der neue Test fällt an der
    # Vorgeneration (quadrat(1) == 1) und besteht am Kandidaten: ein deckender Test im Sinne von Grundsatz 11.
    neu = neu.replace("    return x * x\n", "    return x * x + (1 if x == 1 else 0)\n")
    # dieselbe Eingabe wie die Last: der Aufruf trifft jedes Merkmal der Lastabweichungen von normieren
    zusicherung = ('    assert normieren("  wort   wort  ") == "wort_wort"\n' if haelt_fest
                   else '    normieren("  wort   wort  ")\n')
    tests = {"tests/test_werk_nebenbei.py": ('from probewerk.werk.kern import normieren, quadrat\n\n\ndef test_nebenbei():\n'
                                        + zusicherung + '    assert quadrat(1) == 2\n')}
    u, v = _pruefen(tmp_path, monkeypatch, _diff(QUELLE, neu), nische="sicher", werk_extra=tests)
    assert u["status"] == "abgelehnt", u["grund"]          # die Muster gross/lang/zahlform von normieren deckt er nicht
    gedeckt_n = [k for k in v["gedeckt"] if k.startswith("probewerk.werk.kern:normieren#")]
    assert bool(gedeckt_n) is haelt_fest, (v["gedeckt"], v.get("ungedeckt_aufschluesselung"))
    festhaltend = (v.get("deckung_zaehlung") or {}).get("festhaltend") or {}
    halter = festhaltend.get("probewerk.werk.kern:normieren|rueckgabe") or []
    assert any(x.endswith("test_nebenbei") for x in halter) is haelt_fest, festhaltend


# ================================================================ E. Spezifikationen am Organ/Messgerät
def test_s9_laufzeitrisse_aus_der_liste_auch_mit_bindestrich():
    """Review 02 Nr. 20 (p9): 'daten-import' ergab [] und lehnte ohne Nachmessung ab."""
    assert messgeraet.laufzeitrisse({"grenzen_gerissen": ["daten-import.laufzeit_ms: 12.000 > Grenze 10.000 (x)"]}) == ["daten-import"]
    assert messgeraet.laufzeitrisse({"laufzeit_risse": ["daten-import"], "grenzen_gerissen": []}) == ["daten-import"]
    # Gegenprobe: eine andere gerissene Grenze ist kein Laufzeitriss
    assert messgeraet.laufzeitrisse({"grenzen_gerissen": ["daten-import.groesste_funktion: 90 > Grenze 60"]}) == []


def test_s9_urteil_fuehrt_risse_als_liste(messung):
    b = messung()
    k = messung()
    for x in (b, k):
        x["bereiche"]["daten-import"] = dict(x["bereiche"]["alpha"])
    b["bereiche"]["daten-import"]["laufzeit_ms"] = 10.0
    k["bereiche"]["daten-import"]["laufzeit_ms"] = 30.0
    u = messgeraet.urteil_f2(b, k, b, ["alpha", "beta", "daten-import"], ["daten-import"], {"laufzeit_faktor": 1.1})
    assert u["laufzeit_risse"] == ["daten-import"] and messgeraet.laufzeitrisse(u) == ["daten-import"], u


def test_s12_zeitlimit_am_kandidaten_zweimal_ist_inhaltsbefund(tmp_path, monkeypatch):
    """Review 02 Nr. 21: bei gültiger Vorgeneration ist ein wiederholtes Zeitlimit am Kandidaten ein Befund über ihn."""
    w = tmp_path / "w"
    (w / "paket").mkdir(parents=True)
    ok = {"gueltig": True, "beobachtungen": {"paket.a:f#0": "1"}, "inhalt": {"paket.a:f": 1}}
    tot = {"gueltig": False, "art": "infrastruktur", "zeitlimit": True, "grund": "Zeitlimit"}
    folge = iter([ok, ok, tot, tot])
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: dict(next(folge)))
    r = vv.pruefen(w, {"paket/a.py": "x"}, "last", ["paket"], {})
    assert r["tragfaehig"] is False and r["grund_art"] == "sonde_kandidat_zeitlimit", r


def test_s12_gegenprobe_einmaliges_zeitlimit_wird_wiederholt(tmp_path, monkeypatch):
    w = tmp_path / "w"
    (w / "paket").mkdir(parents=True)
    ok = {"gueltig": True, "beobachtungen": {"paket.a:f#0": "1"}, "inhalt": {"paket.a:f": 1}}
    tot = {"gueltig": False, "art": "infrastruktur", "zeitlimit": True, "grund": "Zeitlimit"}
    folge = iter([ok, ok, tot, ok])
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: dict(next(folge)))
    r = vv.pruefen(w, {"paket/a.py": "x"}, "last", ["paket"], {})
    assert r["tragfaehig"] is True and r["sonde_wiederholt"] is True, r


def test_s12_blinder_aufzeichner_ist_messgeraetausfall(tmp_path, monkeypatch):
    """Review 02 Nr. 22: ein deckender Test, der das geänderte Modul lädt, zeichnet 0 Aufrufe auf — Ausfall, nicht
    Ablehnung (die Deckung ist nicht beurteilbar)."""
    w = tmp_path / "w"
    (w / "paket").mkdir(parents=True)
    alt = {"gueltig": True, "beobachtungen": {"paket.a:f#0": "1"}, "inhalt": {"paket.a:f": 1}, "muster": {"paket.a:f#0": []}}
    neu = {"gueltig": True, "beobachtungen": {"paket.a:f#0": "2"}, "inhalt": {"paket.a:f": 1}, "muster": {"paket.a:f#0": []}}
    folge = iter([alt, alt, neu])
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: dict(next(folge)))
    with pytest.raises(vv.SondeAusgefallen, match="blind"):
        vv.pruefen(w, {"paket/a.py": "x"}, "last", ["paket"], {"tests": ["t.py::a"], "aufrufe": [], "blind": ["t.py::a"]})


def test_s12_gegenprobe_aufzeichner_nicht_blind_lehnt_ab(tmp_path, monkeypatch):
    w = tmp_path / "w"
    (w / "paket").mkdir(parents=True)
    alt = {"gueltig": True, "beobachtungen": {"paket.a:f#0": "1"}, "inhalt": {"paket.a:f": 1}, "muster": {"paket.a:f#0": []}}
    neu = {"gueltig": True, "beobachtungen": {"paket.a:f#0": "2"}, "inhalt": {"paket.a:f": 1}, "muster": {"paket.a:f#0": []}}
    folge = iter([alt, alt, neu])
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: dict(next(folge)))
    r = vv.pruefen(w, {"paket/a.py": "x"}, "last", ["paket"], {"tests": ["t.py::a"], "aufrufe": [], "blind": []})
    assert r["tragfaehig"] is False, r


def test_s3_wurzelmodul_wird_beobachtet_werkzeugdatei_gezaehlt():
    """Review 02 Nr. 12: 'app.py' ergab „keine Quelländerung“."""
    assert vv.geaenderte_module({"app.py": "x", "paket/a.py": "y"}, python=True) == ["app", "paket.a"]
    assert vv.geaenderte_module({"setup.py": "x", "conftest.py": "y"}, python=True) == []
    assert vv.werkzeugdateien({"setup.py": "x", "app.py": "y"}) == ["setup.py"]


# ================================================================ C. Gewinnschwelle (Entscheidung 2) durch aegis.pruefen
def _gewinn_pruefen(tmp_path, monkeypatch, erste, zweite, toleranz=1.2):
    """aegis.pruefen (TS-Werk, Nische schnell, Kernmaß unverändert) mit gestellter Kammer: Messgerät, Sonde, Modell,
    Laufzeit. erste/zweite = (Kandidat, Vorgeneration) in ms — erste gepaarte Messung bzw. Nachmessung."""
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
    zaehl = {"paare": 0}
    original = messgeraet.laufzeit_gepaart

    def gepaart(*a, **k):
        zaehl["paare"] += 1
        return original(*a, **k)
    monkeypatch.setattr(messgeraet, "laufzeit_gepaart", gepaart)

    def laufzeit(werk, bereiche, paket, ref, dateien=None, zeitlimit_s=150):
        kand, basis = erste if zaehl["paare"] == 1 else zweite
        return {"gueltig": True, "grund": "", "bereiche": {"alpha": {"laufzeit_ms": kand if dateien else basis}}}
    monkeypatch.setattr(messgeraet, "laufzeit_messen", laufzeit)
    ok = {"gueltig": True, "beobachtungen": {"alpha/a:a#0": "1"}, "eingewickelt": {"alpha/a": ["a"]}, "inhalt": {"alpha/a:a": 1}}
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: dict(ok))
    basis = messen(w, ["alpha"], "src", None)
    u = aegis.pruefen(con, 1, 1, 7, w, "src", ["alpha"], [], basis, basis, "// last",
                      {"laufzeit_faktor": 2.0, "_rauschtoleranz": {"alpha": toleranz}})
    return u, zaehl


@pytest.mark.parametrize("erste,zweite,paare,status", [
    ((8.8, 10.0), (8.0, 10.0), 2, "ueberlebt"),     # −12 % im Band, Nachmessung −20 %: gepoolt −16 % → Gewinn
    ((8.8, 10.0), (9.0, 10.0), 2, "abgelehnt"),     # beide im Band, beide ohne Gewinn → bestätigt abgelehnt
    ((8.0, 10.0), (9.5, 10.0), 2, "abgelehnt"),     # −20 % im Band, Nachmessung −5 %: gepoolt −12,5 % → kein Gewinn
    ((8.0, 10.0), (8.1, 10.0), 2, "ueberlebt"),     # beide Gewinn → bestätigt angenommen
    ((6.0, 10.0), None, 1, "ueberlebt"),            # −40 %: klar unter dem Band, keine Nachmessung
    ((10.5, 10.0), None, 1, "abgelehnt"),           # +5 %: klar über dem Band, keine Nachmessung
])
def test_c_gewinnschwelle_in_beiden_richtungen_nur_im_band(tmp_path, monkeypatch, erste, zweite, paare, status):
    """Entscheidung Chat-Claude 2: Band = Schwelle 0,85 ÷/× Rauschtoleranz 1,2 → [0,708; 1,02]."""
    u, z = _gewinn_pruefen(tmp_path, monkeypatch, erste, zweite)
    assert z["paare"] == paare and u["status"] == status, (z, u["status"], u["grund"])


# ================================================================ F. Entscheidung 4: Gegenzeugen prüfen zweierlei
from biotop.kern import gegenzeugen  # noqa: E402


@pytest.mark.parametrize("schwaeche,normal,behoben", [
    ({"verletzt": False}, {"faelle": 100, "abweichungen": 0}, True),      # beides gemessen, beides hält
    ({"verletzt": False}, {"faelle": 100, "abweichungen": 5}, False),     # K3044-Lage: Schwäche weg, Verhalten verändert
    ({"verletzt": True}, {"faelle": 100, "abweichungen": 0}, False),      # Schwäche noch da
    ({"verletzt": False}, None, None),                                    # (b) fehlt: nie „behoben“
    ({"verletzt": False}, {"faelle": 0, "abweichungen": 0}, None),        # leerer Vergleich: nie „behoben“
    (None, {"faelle": 100, "abweichungen": 0}, None),                     # (a) fehlt
    (None, {"faelle": 100, "abweichungen": 3}, False),                    # gemessen gescheitert schlägt „fehlt“
])
def test_f_gegenzeuge_behoben_nur_wenn_beides_gemessen_und_haelt(schwaeche, normal, behoben):
    assert gegenzeugen.doppelurteil(schwaeche, normal)["behoben"] is behoben


def test_f_s1_k3044_aus_der_messung_der_runde_2_ist_nicht_behoben():
    """Zahlen aus laeufe/biotop-vor-t4-02/s1/S1-STAENDE.json (K3044): Marker 0, Tab 0 von 12.206, LF 12.206 von 12.206."""
    e = {"marker_neu_gesamt": 0, "K": {"neu_ungleich_norm": 0, "faelle": 120008, "vertrag_zahl": 93320},
         "W": {"tab": {"neu_weist_ab_alt_und_norm_zahl": 0, "norm_zahl": 12206},
               "lf": {"neu_weist_ab_alt_und_norm_zahl": 12206, "norm_zahl": 12206}}}
    u = gegenzeugen.doppelurteil(*gegenzeugen.s1_aus_messung(e))
    assert u["schwaeche_weg"] is True and u["normal_unveraendert"] is False and u["behoben"] is False, u
    assert "lf 12206 von 12206" in u["grund"] and "leerzeichen 0 von 120008" in u["grund"], u["grund"]
    # Gegenprobe: dieselbe Messung ohne die Zeilenumbruch-Abweisungen wäre behoben
    e["W"]["lf"]["neu_weist_ab_alt_und_norm_zahl"] = 0
    assert gegenzeugen.doppelurteil(*gegenzeugen.s1_aus_messung(e))["behoben"] is True
