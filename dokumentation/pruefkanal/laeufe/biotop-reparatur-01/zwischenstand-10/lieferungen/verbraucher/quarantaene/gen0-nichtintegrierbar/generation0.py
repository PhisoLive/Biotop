"""Generation 0 (3.5): Mutanten — prüft, ob die Tests Fehler überhaupt bemerken.

Mutanten (Kern, deterministisch, aus dem Syntaxbaum): Vergleich umgedreht
(< ↔ >=, == ↔ !=, …), Grenze um eins verschoben (Konstante n → n±1),
Rückgabewert vertauscht (return x → return None / not x), Bedingung negiert,
arithmetischer Operator getauscht (+ ↔ -, * ↔ /).
Ein Mutant gilt als gefangen, wenn mindestens ein Test fällt (in der Kammer,
mit dem aktuellen Testbestand). Ungefangene Mutanten sind blinde Flecken; der
Schwarm (Nische „sicher“, Auftrag Testbau) erzeugt dann Tests, die den Mutanten
fangen und am unmutierten Werk bestehen. Ziel: ≥ 80 von 100 (Tor 2: ≥ 16 von 20
für die 20 von Hermes gesetzten Mutanten).
"""

from __future__ import annotations

import ast
import copy
import hashlib
import re
import sqlite3
from pathlib import Path

from ..anbieter import AnbieterFehler, aufrufen
from ..kern import protokoll
from ..kern.datenbank import j, transaktion
from . import kammer, nischen
from .fundpruefung import _pytest_nachweis

_VERGLEICH = {ast.Lt: ast.GtE, ast.LtE: ast.Gt, ast.Gt: ast.LtE, ast.GtE: ast.Lt, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
_ARITH = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}


def _tabelle(con):
    con.executescript("""
    CREATE TABLE IF NOT EXISTS mutanten (id INTEGER PRIMARY KEY, lauf_id INTEGER, werk_id INTEGER, nummer INTEGER, datei TEXT, zeile INTEGER,
        art TEXT, beschreibung TEXT, code TEXT, quelle TEXT, gefangen_vorher INTEGER, gefangen_nachher INTEGER, gefangen_von TEXT, erstellt_am TEXT);""")


def erzeugen(werk: Path, paket: str, bereiche: list[str], max_je_datei: int = 6) -> list[dict]:
    """Deterministische Mutanten über alle Bereichsdateien. Rückgabe: [{datei, zeile, art, beschreibung, code}]."""
    out = []
    for b in bereiche:
        for d in sorted((werk / paket / b).rglob("*.py")):
            if d.name == "__init__.py":
                continue
            rel = str(d.relative_to(werk))
            quelle = d.read_text()
            baum = ast.parse(quelle)
            kandidaten = []
            for kn in ast.walk(baum):
                if isinstance(kn, ast.Compare) and len(kn.ops) == 1 and type(kn.ops[0]) in _VERGLEICH:
                    kandidaten.append(("vergleich", kn))
                elif isinstance(kn, ast.Constant) and isinstance(kn.value, (int, float)) and not isinstance(kn.value, bool) and kn.value not in (0, 1) and abs(kn.value) < 10000:
                    kandidaten.append(("grenze", kn))
                elif isinstance(kn, ast.Return) and kn.value is not None and not isinstance(kn.value, ast.Constant):
                    kandidaten.append(("rueckgabe", kn))
                elif isinstance(kn, ast.If) and not isinstance(kn.test, ast.UnaryOp):
                    kandidaten.append(("bedingung", kn))
                elif isinstance(kn, ast.BinOp) and type(kn.op) in _ARITH:
                    kandidaten.append(("arithmetik", kn))
            # gleichmäßig über Arten verteilen
            je_art: dict[str, list] = {}
            for art, kn in kandidaten:
                je_art.setdefault(art, []).append(kn)
            gewaehlt = []
            i = 0
            while len(gewaehlt) < max_je_datei and any(je_art.values()):
                for art in ("vergleich", "grenze", "rueckgabe", "bedingung", "arithmetik"):
                    if je_art.get(art) and len(gewaehlt) < max_je_datei:
                        gewaehlt.append((art, je_art[art].pop(0)))
                i += 1
            for art, kn in gewaehlt:
                m = copy.deepcopy(baum)
                ziel = None
                for k2 in ast.walk(m):
                    if getattr(k2, "lineno", None) == kn.lineno and getattr(k2, "col_offset", None) == kn.col_offset and type(k2) is type(kn):
                        ziel = k2
                        break
                if ziel is None:
                    continue
                if art == "vergleich":
                    alt = type(ziel.ops[0]).__name__
                    ziel.ops[0] = _VERGLEICH[type(ziel.ops[0])]()
                    beschr = f"Vergleich {alt} → {type(ziel.ops[0]).__name__}"
                elif art == "grenze":
                    alt = ziel.value
                    ziel.value = alt + 1
                    beschr = f"Konstante {alt} → {alt + 1}"
                elif art == "rueckgabe":
                    ziel.value = ast.Constant(value=None)
                    beschr = "return <ausdruck> → return None"
                elif art == "bedingung":
                    ziel.test = ast.UnaryOp(op=ast.Not(), operand=ziel.test)
                    beschr = "if <bedingung> → if not <bedingung>"
                else:
                    alt = type(ziel.op).__name__
                    ziel.op = _ARITH[type(ziel.op)]()
                    beschr = f"Operator {alt} → {type(ziel.op).__name__}"
                ast.fix_missing_locations(m)
                try:
                    code = ast.unparse(m) + "\n"
                    compile(code, rel, "exec")
                except Exception:  # noqa: BLE001
                    continue
                out.append({"datei": rel, "zeile": kn.lineno, "art": art, "beschreibung": beschr, "code": code})
    return out


def _testlauf(werk: Path, dateien: dict[str, str]) -> tuple[bool, str]:
    """True = mindestens ein Test fällt (Mutant gefangen). Rückgabe (gefangen, fallende Tests)."""
    e, tests = _pytest_nachweis(werk, dateien)
    if tests is None:
        raise RuntimeError("Generation 0: ausgeführter Test-Nachweis fehlt: " + (e.stdout + e.stderr)[-400:])
    fallen = [t.get("classname", "") + "::" + t.get("name") for t in tests if t.find("failure") is not None]
    return bool(fallen), ", ".join(fallen[:3])


_AEQUIVALENZ_SKRIPT = """
import sys, json, hashlib, importlib, inspect
sys.path.insert(0, "/werk")
# Beobachtbares Verhalten: Ausgabe der Referenzlast-Funktionen (Rückgabe + repr aller öffentlichen Zustände) und aller
# Modulfunktionen des Bereichs auf einem festen Eingaberaster — als Prüfsumme. Gleiche Prüfsumme bei Original und
# Mutant auf demselben Raster = Verhaltensgleichheit auf diesem Raster (Beleg, kein Beweis; deshalb zusätzlich die Tests).
import referenzlast_werk as R
h = hashlib.sha256()
# beobachten(): Referenzlast liefert je Werk beobachtbare Werte auf einem festen Raster (Teil des Messgeräts, Kern)
fn = getattr(R, "beobachten", None)
if fn is None:
    print("AEQ keine-beobachtung"); sys.exit(0)
n = 0
try:
    for wert in fn():
        h.update(repr(wert).encode()); n += 1
except Exception as e:
    # Laut scheitern: eine Referenzlast, die selbst abstürzt, ist kein Äquivalenz-Beleg
    print("AEQ-ABBRUCH nach", n, "Beobachtungen:", type(e).__name__, str(e)[:200]); sys.exit(3)
print("AEQ", h.hexdigest(), n)
"""


def aequivalenz_pruefen(con: sqlite3.Connection, lauf_id: int, werk: Path, referenzlast: str | None, mutanten: list[dict]) -> list[dict]:
    """F4 3.5: Äquivalente Mutanten VOR der Zählung aussortieren, mit Beleg: (1) alle vorhandenen Tests bestehen am
    Mutanten (= kein Test fängt ihn), (2) die Referenzlast liefert am Mutanten dieselbe Ausgabe-Prüfsumme wie am
    Original, (3) Begründung am Code (mechanisch: die Mutation liegt in einem Zweig, der auf Raster und Tests nie
    anders entscheidet — ausgewiesen als „Beleg auf Raster + Tests", nicht als Beweis). Rückgabe: Liste der Mutanten
    mit Feld `aequivalent` (bool) und `aequivalenz_beleg`."""
    if not referenzlast:
        for m in mutanten:
            m["aequivalent"] = False; m["aequivalenz_beleg"] = "keine Referenzlast — nicht geprüft"
        return mutanten
    ref = referenzlast  # Text der Referenzlast (Kern), wird als Modul in die Kammer gelegt
    dateien_basis = {"referenzlast_werk.py": ref, "_aeq.py": _AEQUIVALENZ_SKRIPT}
    e0 = kammer.ausfuehren(werk, ["python", "_aeq.py"], zeitlimit_s=120, dateien=dateien_basis)
    h0 = re.search(r"AEQ (\w+)", e0.stdout)
    if e0.rc != 0 or not h0:
        raise RuntimeError("Äquivalenzprüfung: Referenzlast-Beobachtung am Original gescheitert (laut scheitern): " + (e0.stdout + e0.stderr)[-400:])
    for i, m in enumerate(mutanten, 1):
        m["aequivalent"] = False
        g, von = _testlauf(werk, {m["datei"]: m["code"]})
        if g:
            m["aequivalenz_beleg"] = f"nicht äquivalent: Test fängt ({von})"
            continue
        e1 = kammer.ausfuehren(werk, ["python", "_aeq.py"], zeitlimit_s=120, dateien={**dateien_basis, m["datei"]: m["code"]})
        h1 = re.search(r"AEQ (\w+)", e1.stdout)
        if h0 and h0.group(1) == "keine-beobachtung":
            m["aequivalenz_beleg"] = "Referenzlast ohne beobachten() — Äquivalenz nicht prüfbar, zählt als nicht-äquivalent"
            continue
        if e1.rc != 0 or not h1:
            m["aequivalenz_beleg"] = "nicht äquivalent: Referenzlast-Beobachtung am Mutanten bricht ab (" + (e1.stdout + e1.stderr)[-160:].strip() + ")"
            continue
        if h0 and h1 and h0.group(1) == h1.group(1):
            m["aequivalent"] = True
            m["aequivalenz_beleg"] = (f"äquivalent auf Raster+Tests: Referenzlast-Prüfsumme {h0.group(1)[:12]} identisch, "
                                      f"alle vorhandenen Tests bestehen; Mutation: {m['beschreibung']} in {m['datei']}:{m['zeile']}")
        else:
            m["aequivalenz_beleg"] = f"nicht äquivalent: Referenzlast-Prüfsumme weicht ab ({(h0 and h0.group(1)[:12])} vs {(h1 and h1.group(1)[:12])}) — kein Test fängt (blind)"
    protokoll.schreiben(con, "generation0.aequivalenz", lauf_id=lauf_id, geprueft=len(mutanten),
                        aequivalent=[f"#{i} {m['aequivalenz_beleg']}" for i, m in enumerate(mutanten, 1) if m["aequivalent"]])
    return mutanten


def messen(con: sqlite3.Connection, lauf_id: int, werk_id: int, werk: Path, mutanten: list[dict], phase: str) -> dict:
    """Lässt jeden Mutanten gegen den aktuellen Testbestand laufen. phase: 'vorher' | 'nachher'."""
    _tabelle(con)
    gefangen = 0
    for i, m in enumerate(mutanten, 1):
        g, von = _testlauf(werk, {m["datei"]: m["code"]})
        if not m.get("aequivalent"):
            gefangen += g
        with transaktion(con):
            if phase == "vorher":
                con.execute("INSERT INTO mutanten(lauf_id, werk_id, nummer, datei, zeile, art, beschreibung, code, quelle, gefangen_vorher, gefangen_von, erstellt_am) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                            (lauf_id, werk_id, i, m["datei"], m["zeile"], m["art"], m["beschreibung"], m["code"], m.get("quelle", "biotop"), int(g), von, protokoll.jetzt()))
            else:
                con.execute("UPDATE mutanten SET gefangen_nachher=?, gefangen_von=? WHERE lauf_id=? AND nummer=?", (int(g), von, lauf_id, i))
        m["gefangen_" + phase] = g
        m["gefangen_von"] = von
    nicht_aeq = [m for m in mutanten if not m.get("aequivalent")]
    protokoll.schreiben(con, f"generation0.{phase}", lauf_id=lauf_id, gefangen=gefangen, gesamt=len(mutanten), nicht_aequivalent=len(nicht_aeq),
                        blind=[f"#{i} {m['datei']}:{m['zeile']} {m['beschreibung']}" for i, m in enumerate(mutanten, 1) if not m["gefangen_" + phase] and not m.get("aequivalent")])
    return {"gefangen": gefangen, "gesamt": len(mutanten), "nicht_aequivalent": len(nicht_aeq),
            "blind": [m for m in nicht_aeq if not m["gefangen_" + phase]]}


SYSTEM_TESTBAU = """Du schreibst pytest-Tests, die einen konkreten Mutanten fangen. Du bekommst: die Originaldatei, den mutierten Ausschnitt
(Zeile und Art der Mutation) und die vorhandenen Tests des Bereichs. Liefere 1–3 Tests, die am ORIGINAL bestehen und am MUTANTEN fallen.
Die Antwort ist eine EIGENSTÄNDIGE neue Testdatei: sie beginnt mit allen nötigen Imports (import pytest; from lagerhaus.<bereich> import ...)
— nichts wird an eine vorhandene Datei angehängt. Benutze nur Klassen/Funktionen, die im Quelltext stehen.
Antwortformat:
```python
import pytest
from lagerhaus.<bereich> import ...

def test_...():
    ...
```"""


def tests_evolutionieren(con: sqlite3.Connection, lauf_id: int, werk_id: int, werk: Path, paket: str, blind: list[dict], nummern: dict) -> dict:
    """Für jeden blinden Mutanten: Schwarm (Nische sicher, 2 Hersteller) erzeugt Tests; ein Test wird ins Werk übernommen,
    wenn er am Original besteht UND den Mutanten fängt. Rückgabe: Zahlen + Dateien."""
    neu: dict[str, str] = {}
    gefangen_neu = 0
    for m in blind:
        bereich = m["datei"].split("/")[1]
        original = (werk / m["datei"]).read_text()
        zeilen = original.splitlines()
        z = m["zeile"]
        ausschnitt = "\n".join(f"{i+1:4d}: {l}" for i, l in enumerate(zeilen) if abs(i + 1 - z) <= 8)
        tests_alt = (werk / "tests" / f"test_{bereich}.py").read_text() if (werk / "tests" / f"test_{bereich}.py").exists() else ""
        nutzer = (f"DATEI {m['datei']} (Original, Paket {paket}):\n```python\n{original}\n```\n\nMUTATION in Zeile {z}: {m['beschreibung']} ({m['art']})\n"
                  f"Ausschnitt um Zeile {z}:\n{ausschnitt}\n\nVORHANDENE TESTS (tests/test_{bereich}.py, nur lesen):\n```python\n{tests_alt[:6000]}\n```")
        gefunden = False
        # F4: der Testbau ist stochastisch — je blindem Mutanten zwei Durchläufe (je 2 Hersteller), bevor er als ungefangen gilt
        for durchlauf, (hersteller, modell) in [(d, hm) for d in (1, 2) for hm in nischen.waehlen(con, lauf_id, "sicher")]:
            try:
                a = aufrufen(con, lauf_id, "openrouter", modell, SYSTEM_TESTBAU, nutzer, zweck=f"generation0.testbau.{bereich}", max_tokens=1500, temperatur=0.2)
            except AnbieterFehler as e:
                protokoll.schreiben(con, "generation0.fehler", lauf_id=lauf_id, modell=modell, fehler=str(e)[:200])
                continue
            mm = re.search(r"```python\s*\n(.*?)```", a.text, re.S)
            if not mm:
                continue  # F4: keine Antwort = neutral für den Bandit
            code = mm.group(1)
            pfad = f"tests/test_{bereich}_gen0_m{nummern[id(m)]}.py"
            # am Original bestehen?
            e_o = kammer.ausfuehren(werk, ["python", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--tb=no", pfad], zeitlimit_s=60, dateien={pfad: code})
            besteht = e_o.rc == 0 and "passed" in e_o.stdout
            # Mutanten fangen?
            e_m = kammer.ausfuehren(werk, ["python", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--tb=no", pfad], zeitlimit_s=60, dateien={pfad: code, m["datei"]: m["code"]})
            faengt = e_m.rc != 0
            nischen.buchen(con, lauf_id, "sicher", hersteller, besteht and faengt)
            protokoll.schreiben(con, "generation0.testkandidat", lauf_id=lauf_id, mutant=nummern[id(m)], durchlauf=durchlauf, modell=modell, besteht_am_original=besteht, faengt_mutant=faengt)
            if besteht and faengt:
                neu[pfad] = code
                gefunden = True
                break
        gefangen_neu += gefunden
    return {"neue_tests": neu, "gefangen_neu": gefangen_neu, "blind_gesamt": len(blind)}


def pruefsumme(code: str) -> str:
    return hashlib.sha256(code.encode()).hexdigest()[:12]
