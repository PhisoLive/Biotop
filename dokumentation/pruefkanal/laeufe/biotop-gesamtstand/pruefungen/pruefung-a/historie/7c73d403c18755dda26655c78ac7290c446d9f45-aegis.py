"""Organ 3.7: Aegis — der Ankläger. Fassung 2 (Masterprompt v2).

Schritte 1 (Wirkungskreis), 3 (Verfassung: mechanisch prüfbare Sätze), 4 (Angriff)
und 5 (Ausführung, paarweise Messung nach 3.5 F2). Schritt 2 (explizite Verträge) = Phase 2.

Paarweise Messung: Vorgeneration und Kandidat werden mit DEMSELBEN Testbestand
gemessen — dem des Kandidaten: vorhandene Tests + gültige neue Tests des Kandidaten
+ offene Immuntests des Bereichs + Befundklassen-Immuntests (3.5 „behoben heißt
verschwunden") + Angriffstests, die einen Fehler bestätigen. Zuwachs = Differenz
des Kernmaßes F2. Bestandene Tests zählen nicht.

Sicherheitsbefunde (3.7 F2): Trägt der Bereich in der Vorgeneration einen
statischen Befund, bekommt der Ankläger die Befundklasse mit Beschreibung, muss
deren bekannte Umgehungen angreifen, und der Angriff läuft mit einem schweren Modell.

Klassifikation von Angriffstests: nur AssertionError oder Ausnahme im Werk zählt
als bestätigter Fehler; ein Test, der an sich selbst stirbt, zählt nicht.
"""

from __future__ import annotations

import ast
import re
import sqlite3
import xml.etree.ElementTree as ET
from pathlib import Path

from ..anbieter import AnbieterFehler, aufrufen
from ..kern import befundklassen, diffwerk, messgeraet, protokoll
from ..kern.datenbank import j, lj, transaktion
from . import kammer, landkarte, verfassung, vertraege

MODELL_ANGRIFF = ("openrouter", "google/gemini-3.5-flash-lite")
MODELL_ANGRIFF_SCHWER = ("openrouter", "anthropic/claude-sonnet-5")

ANGRIFF_SYSTEM = """Du bist der Ankläger. Dein einziger Auftrag: den Fehler, den Grenzfall, die Nebenwirkung in einem vorgeschlagenen Änderungssatz finden.
Du wirst nach Fehlern bewertet, die sich durch Ausführung BESTÄTIGEN lassen — nicht nach Bedenken. Ein Test, der an einem falschen Import oder falschen Methodennamen stirbt, zählt gegen dich.
Du bekommst den Quelltext des Bereichs (nach Anwendung des Diffs), den Diff selbst, die Verträge des Bereichs und — falls vorhanden — die statische Befundklasse der berührten Stelle mit ihren bekannten Umgehungen.
Benutze NUR die Klassen, Funktionen und Signaturen, die im Quelltext stehen.
Liefere bis zu 4 pytest-Tests, die je einen konkreten Vertragsbruch, Fehler oder eine Sicherheits-Umgehung NACHWEISEN: Der Test schlägt mit AssertionError fehl (oder pytest.raises greift nicht), wenn der Fehler vorliegt, und besteht, wenn das Verhalten dem Vertrag entspricht.
Bei einer Befundklasse mit eval/exec: greife die Erreichbarkeit von Objektklassen über Introspektion an (().__class__.__base__.__subclasses__(), __globals__ von Funktionen, Format-String-Zugriffe, Ausdrucks-Explosion), nicht nur den naiven __import__-Aufruf. Der Vertrag verlangt, dass jede solche Eingabe mit der Fehlerklasse des Bereichs abgewiesen wird.
Keine Stilkritik, keine Tests über Sortierreihenfolgen, die kein Vertrag zusichert.
Wenn du nichts findest, antworte genau: KEIN ANGRIFF.

Antwortformat:
```python
# je Test eine Funktion test_..., Importe aus dem Werk-Paket
```
"""


# ---------------------------------------------------------------- Diff
def kandidat_dateien(werk: Path, diff: str) -> dict[str, str | None] | None:
    try:
        out: dict[str, str | None] = {}
        for d in diffwerk.parsen(diff):
            f = werk / d.pfad
            out[d.pfad] = diffwerk.anwenden(f.read_text() if f.exists() else None, d)
        return out if out else None
    except Exception:  # noqa: BLE001
        return None


def diff_grund(werk: Path, diff: str) -> str:
    try:
        for d in diffwerk.parsen(diff):
            f = werk / d.pfad
            diffwerk.anwenden(f.read_text() if f.exists() else None, d)
        return ""
    except Exception as e:  # noqa: BLE001
        return str(e)[:300]


# ---------------------------------------------------------------- Testläufe
def junit_lauf(werk: Path, paket: str, dateien: dict[str, str], testdateien: list[str]) -> dict[str, dict]:
    """Führt `testdateien` in der Kammer aus. Rückgabe je „datei::name“ → {ok, bestaetigt, meldung}."""
    if not testdateien:
        return {}
    skript = ("import subprocess,sys;subprocess.run([sys.executable,'-m','pytest','-q','-p','no:cacheprovider','--tb=short',"
              "'--junitxml=/tmp/j.xml',*sys.argv[1:]]);print('@@J@@'+open('/tmp/j.xml').read()+'@@E@@')")
    e = kammer.ausfuehren(werk, ["python", "_messgeraet/lauf.py", *testdateien], zeitlimit_s=120,
                          dateien={**dateien, "_messgeraet/lauf.py": skript})
    m = re.search(r"@@J@@(.*)@@E@@", e.stdout, re.S)
    out: dict[str, dict] = {}
    if not m:
        for t in testdateien:
            out[f"{t}::*"] = {"ok": False, "bestaetigt": False, "meldung": "Sammelfehler/Zeitlimit: " + (e.stderr or e.stdout)[-300:]}
        return out
    for tc in ET.fromstring(m.group(1)).iter("testcase"):
        datei = (tc.get("classname") or "").replace(".", "/") + ".py"
        name = tc.get("name")
        f = tc.find("failure"); er = tc.find("error")
        if f is None and er is None:
            out[f"{datei}::{name}"] = {"ok": True, "bestaetigt": False, "meldung": ""}
            continue
        kn = f if f is not None else er
        msg = (kn.get("message") or "")[:300]
        text = kn.text or ""
        orte = re.findall(r"^([\w./-]+\.py):\d+: in ", text, re.M)
        im_werk = bool(orte) and orte[-1].startswith(paket + "/")
        bestaetigt = msg.startswith(("AssertionError", "assert", "Failed", "TimeoutError")) or im_werk
        out[f"{datei}::{name}"] = {"ok": False, "bestaetigt": bestaetigt, "meldung": msg, "ort": orte[-1] if orte else ""}
    for t in testdateien:
        if not any(k.startswith(t + "::") for k in out):
            out[f"{t}::*"] = {"ok": False, "bestaetigt": False, "meldung": "Sammelfehler (Import) in " + t}
    return out


def nur_funktionen(code: str, behalten: set[str]) -> str | None:
    try:
        baum = ast.parse(code)
    except SyntaxError:
        return None
    koerper = [k for k in baum.body if not (isinstance(k, ast.FunctionDef) and k.name.startswith("test")) or k.name in behalten]
    if not any(isinstance(k, ast.FunctionDef) and k.name.startswith("test") for k in koerper):
        return None
    return ast.unparse(ast.Module(body=koerper, type_ignores=[])) + "\n"


def _fehlende_oder_geaenderte_tests(alt: str, neu: str) -> list[str]:
    """Namen vorhandener Testfunktionen, die in der Kandidatenfassung fehlen oder anders lauten (AST-Vergleich)."""
    try:
        ba, bn = ast.parse(alt), ast.parse(neu)
    except SyntaxError:
        return ["(Syntaxfehler)"]
    neu_fn = {k.name: ast.unparse(k) for k in bn.body if isinstance(k, ast.FunctionDef)}
    out = []
    for k in ba.body:
        if isinstance(k, ast.FunctionDef) and k.name.startswith("test"):
            if neu_fn.get(k.name) != ast.unparse(k):
                out.append(k.name)
    return out


def _anhaengen(alt: str, neu: str, behalten: set[str]) -> str | None:
    """Alte Testdatei unverändert + die gültigen neuen Funktionen (und neue Imports) des Kandidaten angehängt."""
    try:
        ba, bn = ast.parse(alt), ast.parse(neu)
    except SyntaxError:
        return None
    alt_namen = {k.name for k in ba.body if isinstance(k, ast.FunctionDef)}
    alt_imports = {ast.unparse(k) for k in ba.body if isinstance(k, (ast.Import, ast.ImportFrom))}
    zusatz = [k for k in bn.body if isinstance(k, (ast.Import, ast.ImportFrom)) and ast.unparse(k) not in alt_imports]
    zusatz += [k for k in bn.body if isinstance(k, ast.FunctionDef) and k.name in behalten and k.name not in alt_namen]
    if not any(isinstance(k, ast.FunctionDef) for k in zusatz):
        return None
    return alt.rstrip("\n") + "\n\n\n" + ast.unparse(ast.Module(body=zusatz, type_ignores=[])) + "\n"


def _namen(r: dict, praefix: str, **filt) -> set[str]:
    out = set()
    for n, x in r.items():
        if not n.startswith(praefix + "::") or n.endswith("::*"):
            continue
        if all(x.get(k) == v for k, v in filt.items()):
            out.add(n.split("::")[1])
    return out


# ---------------------------------------------------------------- Befundklassen
def befundklassen_tests(con, werk_id: int, bereich: str, basis: dict) -> dict[str, str]:
    """Befundklassen-Immuntests für alle statischen Befunde des Bereichs in der Vorgeneration,
    sofern die Verfassung einen Einstieg für die Klasse nennt."""
    verf = verfassung.lesen(con, werk_id)
    einstiege = ((verf or {}).get("regeln") or {}).get("einstiege", {})
    out = {}
    for b in basis["bereiche"][bereich].get("sicherheit_befunde", []):
        kl = b["test"]
        e = einstiege.get(kl, {}).get(bereich) or einstiege.get(kl, {}).get("*")
        if not e:
            continue
        code = befundklassen.immuntest_code(kl, e["import"], e["aufruf"], e["fehler_import"], e["fehler"])
        if code:
            out[f"tests/test_{bereich}_immun_befundklasse_{kl}.py"] = code
    return out


# ---------------------------------------------------------------- Norm & Doppelung
_VERTRAG_WOERTER = ("vertrag", "verfassung", "satz ", "anhang a", "zusicherung", "docstring")


_VERWEIS_MUSTER = re.compile(r"(test_vertrag_[a-z0-9_]+(?:::test_[a-z0-9_]+)?|verfassung(?:ssatz)?\s*(?:satz\s*)?(\d{1,2})|anhang\s*a\s*satz\s*(\d{1,2})|\bsatz\s*(\d{1,2})\b)", re.I)


def _nennt_vertrag(code: str, testname: str, verf: dict | None, con, werk_id: int, bereich: str, zusatz_vertraege: dict | None = None) -> bool:
    """F4 3.7: Vertrags-/Verfassungsbezug NUR durch expliziten Verweis — Vertragstest-Kennung (Dateiname
    `test_vertrag_<a>_<b>` oder `…::test_…`, muss als expliziter Vertrag des Werks existieren) oder
    Verfassungssatz-Nummer (muss existieren) — im Testnamen oder Docstring. Wortüberdeckung (F3) zählt nicht mehr,
    weil sie sich durch Vokabular erzeugen lässt. Rückgabe True nur bei aufgelöstem Verweis."""
    try:
        baum = ast.parse(code)
    except SyntaxError:
        return False
    fn = next((k for k in baum.body if isinstance(k, ast.FunctionDef) and k.name == testname), None)
    if fn is None:
        return False
    text = (fn.name + " " + (ast.get_docstring(fn) or "")).lower()
    vertragsdateien = {Path(v["pfad"]).stem for v in vertraege.alle(con, werk_id)}
    vertragstests = set()
    # Verträge des Werks + die vom Kandidaten mitgebrachte (zu verhandelnde) Fassung der Vertragsdatei
    quellen = [(v["pfad"], v["code"]) for v in vertraege.alle(con, werk_id)] + list((zusatz_vertraege or {}).items())
    for pf, cd in quellen:
        try:
            for k in ast.parse(cd or "").body:
                if isinstance(k, ast.FunctionDef) and k.name.startswith("test_"):
                    vertragstests.add(f"{Path(pf).stem}::{k.name}")
        except SyntaxError:
            pass
    saetze = set()
    if verf:
        for z in verf["text"].splitlines():
            m = re.match(r"\s*(\d{1,2})[.)]", z)
            if m:
                saetze.add(int(m.group(1)))
    for m in _VERWEIS_MUSTER.finditer(text):
        ganz = m.group(1)
        if ganz.startswith("test_vertrag_"):
            if "::" in ganz:
                if ganz in vertragstests:
                    return True
            elif ganz in vertragsdateien:
                return True
            continue
        nr = next((g for g in m.groups()[1:] if g), None)
        if nr and int(nr) in saetze:
            return True
    return False


def behauptung(code: str, testname: str, paket: str = "") -> str:
    """Die BEHAUPTUNG eines Tests als Schlüssel: Ziel-Funktion des Werks + Art der Zusicherung (Fassung 5, 3.10).

    Nicht (Meldungsklasse, Ort): Jeder Test liegt in seiner eigenen Datei und Zeile, also ist der Ort nie derselbe —
    die Prüfung lief leer. Sechs Tests derselben Behauptung kamen so einzeln ins Immunsystem und hielten einen
    Fehler am Leben (Phase 3, `Katalog.wert` liefert Staffel- statt Grundpreis).

    Schlüssel = `<aufgerufene Werk-Funktion>|<Zusicherungsart>`:
      - Ziel: die letzte im Test aufgerufene Funktion/Methode des Werks (Aufbauhilfen wie `aufnehmen`, `append`
        werden übersprungen), sonst der importierte Name.
      - Zusicherungsart: `raises:<Ausnahme>` bei erwarteter Ausnahme, sonst der Vergleichsoperator plus die Form
        der erwarteten Seite (`zahl`, `text`, `name`) — NICHT der Zahlenwert selbst. Zwei Tests, die dasselbe über
        dieselbe Funktion behaupten und sich nur in den eingesetzten Zahlen unterscheiden, sind eine Doppelung.
    """
    try:
        baum = ast.parse(code)
    except SyntaxError:
        return f"?|{testname}"
    fn = next((k for k in ast.walk(baum) if isinstance(k, ast.FunctionDef) and k.name == testname), None)
    if fn is None:
        return f"?|{testname}"
    hilfen = {"aufnehmen", "append", "add", "update", "extend", "insert", "raises", "approx", "len", "str",
              "int", "float", "list", "dict", "set", "sorted", "print", "range"}
    ziel, zusicherung = "?", "?"
    for k in ast.walk(fn):
        if isinstance(k, ast.Call):
            f = k.func
            name = f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else None)
            if name and name not in hilfen:
                ziel = name
        if isinstance(k, ast.With) and zusicherung == "?":
            for eintrag in k.items:
                if isinstance(eintrag.context_expr, ast.Call):
                    args = eintrag.context_expr.args
                    if args and isinstance(args[0], ast.Name):
                        zusicherung = f"raises:{args[0].id}"
    for k in ast.walk(fn):
        if isinstance(k, ast.Assert) and zusicherung == "?":
            pruef = k.test
            if isinstance(pruef, ast.Compare) and pruef.comparators:
                op = type(pruef.ops[0]).__name__
                rechts = pruef.comparators[0]
                form = ("zahl" if isinstance(rechts, ast.Constant) and isinstance(rechts.value, (int, float))
                        else "text" if isinstance(rechts, ast.Constant) and isinstance(rechts.value, str)
                        else "name")
                zusicherung = f"{op}:{form}"
            else:
                zusicherung = "wahrheit"
    return f"{ziel}|{zusicherung}"


def _doppelungen(treffer: set[str], ergebnisse: dict, ad: str, con, werk_id: int, bereich: str,
                 code: str = "", paket: str = "") -> tuple[set[str], set[str]]:
    """Gleiche BEHAUPTUNG = Doppelung (Fassung 5, 3.10) — Schlüssel ist die Behauptung, nicht die Fundstelle.
    Auch gegen bereits im Immunsystem/Werk liegende Funde des Bereichs (deren Schlüssel im Ursprung steht)."""
    bekannt = set()
    for z in con.execute("SELECT ursprung FROM immunsystem WHERE werk_id=? AND bereich=? AND status IN ('im_werk','gefunden','offen')",
                         (werk_id, bereich)):
        t = z["ursprung"] or ""
        if "behauptung=" in t:
            bekannt.add(t.split("behauptung=", 1)[1].split(" ")[0].strip())
    einzig, doppel, gesehen = set(), set(), set()
    for n in sorted(treffer):
        schl = behauptung(code, n, paket) if code else f"?|{n}"
        if schl in gesehen or schl in bekannt:
            doppel.add(n)
        else:
            gesehen.add(schl); einzig.add(n)
    return einzig, doppel


# ---------------------------------------------------------------- Angriff
def bisherige_behauptungen(con, werk_id: int, bereich: str, limit: int = 25) -> list[str]:
    """Welche Behauptungen hat der Ankläger in diesem Bereich schon aufgestellt? (Fassung 6)

    Gemessen in Phase 2/3: 68,5 % der erzeugten Angriffstests wiederholten eine bereits vorhandene Behauptung —
    acht Tests sagten dasselbe über `lager/reserviert`. Zwei Drittel der Aufrufe brachten also nichts Neues und
    kosteten trotzdem. Deshalb werden dem Ankläger vor jedem Angriff seine bisherigen Behauptungen dieses Bereichs
    vorgelegt, mit dem Auftrag, eine andere zu finden. Das ist Text im ohnehin fälligen Aufruf, kostet nichts extra.
    """
    aus = []
    for z in con.execute("SELECT ursprung FROM immunsystem WHERE werk_id=? AND bereich=? ORDER BY id DESC LIMIT 200",
                         (werk_id, bereich)):
        t = z["ursprung"] or ""
        if "behauptung=" in t:
            for s in t.split("behauptung=", 1)[1].strip().split(" "):
                if "|" in s and s not in aus:
                    aus.append(s)
    return aus[:limit]


def _angriff(con, lauf_id, werk_id, paket, bereich, diff, dateien, werk, klassen: list[str]) -> tuple[str | None, str]:
    quelle = []
    for d in sorted((werk / paket / bereich).rglob("*.py")):
        rel = str(d.relative_to(werk))
        inhalt = dateien.get(rel, d.read_text())
        if inhalt is not None:
            quelle.append(f"### {rel}\n```python\n{inhalt}\n```")
    vertraege = "\n".join(f"- {z['text']} ({z['quelle']})" for z in con.execute(
        "SELECT text, quelle FROM vertraege WHERE werk_id=? AND bereich=? AND herkunft='docstring'", (werk_id, bereich)))
    verf = verfassung.lesen(con, werk_id)
    verf_text = ("\n\nVERFASSUNG DES WERKS:\n" + verf["text"]) if verf else ""
    befund_text = ""
    modell = MODELL_ANGRIFF
    if klassen:
        befund_text = "\n\nSTATISCHE BEFUNDKLASSE(N) DER BERÜHRTEN STELLE (3.7 F2 — greife die bekannten Umgehungen an):\n" + "\n".join(
            "- " + befundklassen.beschreibung(k) for k in klassen)
        modell = MODELL_ANGRIFF_SCHWER
    # Fassung 6: bisherige Behauptungen vorlegen — gegen Wiederholung derselben Zusicherung (68,5 % gemessen).
    schon = bisherige_behauptungen(con, werk_id, bereich)
    schon_text = ("\n\nDIESE BEHAUPTUNGEN HAST DU IN DIESEM BEREICH SCHON AUFGESTELLT "
                  "(Form: <Funktion>|<Zusicherung>):\n" + "\n".join(f"- {s}" for s in schon) +
                  "\n\nStelle eine ANDERE Behauptung auf: ein anderes Ziel oder eine andere Art von Zusicherung. "
                  "Ein Test, der eine dieser Behauptungen wiederholt, wird als Doppelung verworfen und bringt nichts. "
                  "Findest du nichts Neues, antworte mit KEIN ANGRIFF — das ist kein Fehlschlag.") if schon else ""
    try:
        a = aufrufen(con, lauf_id, *modell, ANGRIFF_SYSTEM,
                     f"BEREICH {bereich} (Paket {paket})\n\nVERTRÄGE:\n{vertraege or 'keine dokumentiert'}{verf_text}{befund_text}{schon_text}\n\nDIFF:\n```diff\n{diff}\n```\n\nQUELLTEXT NACH DIFF:\n" + "\n\n".join(quelle),
                     zweck=("schwer." if klassen else "") + f"aegis.angriff.{bereich}", max_tokens=2500, temperatur=0.3)
    except AnbieterFehler as e:
        protokoll.schreiben(con, "aegis.fehler", lauf_id=lauf_id, fehler=str(e)[:300])
        return None, modell[1]
    if "KEIN ANGRIFF" in a.text[:200]:
        return None, modell[1]
    m = re.search(r"```python\s*\n(.*?)```", a.text, re.S)
    return (m.group(1) if m else None), modell[1]


# ---------------------------------------------------------------- Anklage
def pruefen(con: sqlite3.Connection, lauf_id: int, werk_id: int, kandidat_id: int, werk: Path, paket: str,
            bereiche: list[str], bstrassen: list[tuple[str, str]], basis: dict, ausgang: dict,
            referenzlast: str | None, tausch: dict | None, extra_code: dict[str, str] | None = None) -> dict:
    """extra_code: zusätzliche Dateien (z. B. Anpassung des Nachbarn bei Verhandlung), die zusammen mit dem
    Kandidaten gemessen werden."""
    """Vollständige Anklage (F2). Rückgabe: Urteil mit Belegen; Status in der DB gesetzt."""
    k = con.execute("SELECT * FROM kandidaten WHERE id=?", (kandidat_id,)).fetchone()
    bereich = k["bereich"]
    urteil = {"kandidat": kandidat_id, "bereich": bereich, "status": "abgelehnt", "grund": "", "wirkungskreis": [],
              "immun": [], "tests_neu": [], "tests_verworfen": [], "immun_bestanden": [], "befundklassen": [],
              "verfassung_verstoesse": [], "angriff": None, "mass": None, "tests_offen": [], "norm": [], "doppelungen": [],
              "vertrag_verletzt": [], "vertraege_benannt": (k["vertraege"] if "vertraege" in k.keys() else "") or ""}

    def fertig(status, grund, masse=None, dateien_final=None, basis_paar=None):
        urteil["status"], urteil["grund"] = status, grund
        if masse is not None:
            masse = {**masse, "_dateien": dateien_final or {}, "_basis_paar": basis_paar, "_urteil_f2": urteil["mass"]}
        with transaktion(con):
            con.execute("UPDATE kandidaten SET status=?, grund=?, masse=?, wirkungskreis=? WHERE id=?",
                        (status, grund, j(masse) if masse else None, j(urteil["wirkungskreis"]), kandidat_id))
        protokoll.schreiben(con, "aegis.urteil", lauf_id=lauf_id, kandidat=kandidat_id, bereich=bereich, status=status,
                            grund=grund[:500], wirkungskreis=urteil["wirkungskreis"], immun=urteil["immun"],
                            tests_neu=urteil["tests_neu"], tests_verworfen=urteil["tests_verworfen"],
                            immun_bestanden=urteil["immun_bestanden"], befundklassen=urteil["befundklassen"],
                            verfassung=urteil["verfassung_verstoesse"], angriff=urteil["angriff"], mass=urteil["mass"], tests_offen=urteil["tests_offen"],
                            norm=urteil["norm"], doppelungen=urteil["doppelungen"], vertrag_verletzt=urteil["vertrag_verletzt"], nische=k["nische"])
        return urteil

    if k["status"] != "erzeugt":
        return fertig(k["status"], k["grund"] or "nicht geprüft")

    # Schritt 1: Wirkungskreis
    urteil["wirkungskreis"] = landkarte.wirkungskreis(bereich, bstrassen)

    dateien = kandidat_dateien(werk, k["diff"])
    if dateien is None:
        return fertig("abgelehnt", "Diff nicht anwendbar: " + (diff_grund(werk, k["diff"]) or "kein Inhalt"))
    code = {p: (i if i is not None else "") for p, i in dateien.items() if not p.startswith("tests/")}
    code.update(extra_code or {})
    tests_kandidat = {p: i for p, i in dateien.items() if p.startswith("tests/") and i is not None and not p.startswith("tests/vertraege/")}
    vertrag_dateien_kandidat = {p: i for p, i in dateien.items() if p.startswith("tests/vertraege/") and i is not None}
    if not code and not tests_kandidat:
        return fertig("abgelehnt", "Diff ändert nichts")

    # Schritt 2: explizite Verträge — Vertragsdateien des Kandidaten nur, wenn er den Vertrag unter VERTRÄGE benannt hat
    if vertrag_dateien_kandidat and urteil["vertraege_benannt"].strip().lower() in ("", "keine"):
        return fertig("abgelehnt", f"ändert Vertragsdatei {sorted(vertrag_dateien_kandidat)} ohne den Vertrag unter VERTRÄGE zu benennen (3.8 Schritt 2)")
    urteil["vertrag_dateien"] = sorted(vertrag_dateien_kandidat)  # Anhang A Satz 4: geänderte Vertragsdatei ⇒ Verhandlung (lauf.py)

    # Schritt 3: Verfassung (mechanisch prüfbare Sätze)
    verf = verfassung.lesen(con, werk_id)
    urteil["verfassung_verstoesse"] = verfassung.mechanisch_pruefen(verf, k["diff"], dateien, paket, bereich)
    if urteil["verfassung_verstoesse"]:
        return fertig("abgelehnt", "Verfassung verletzt: " + "; ".join(urteil["verfassung_verstoesse"]))

    # Testbestand des Kandidaten aufbauen
    testbestand: dict[str, str] = {}
    # a) Befundklassen-Immuntests (Bereich trägt in der Vorgeneration einen statischen Befund)
    bk = befundklassen_tests(con, werk_id, bereich, basis)
    testbestand.update(bk)
    urteil["befundklassen"] = sorted({b["test"] for b in basis["bereiche"][bereich].get("sicherheit_befunde", [])})
    # b) offene Immuntests des Bereichs
    for z in con.execute("SELECT name, code FROM immunsystem WHERE werk_id=? AND bereich=? AND status IN ('gefunden','offen')", (werk_id, bereich)):
        testbestand[f"tests/test_{bereich}_immun_{z['name']}.py"] = z["code"]
    # c) neue Tests des Kandidaten: nur die, die an der Vorgeneration FEHLSCHLAGEN (bestätigt) und am Kandidaten BESTEHEN
    if tests_kandidat:
        r_b = junit_lauf(werk, paket, tests_kandidat, list(tests_kandidat))
        r_k = junit_lauf(werk, paket, {**code, **tests_kandidat}, list(tests_kandidat))
        for p, inhalt in tests_kandidat.items():
            faellt_b = _namen(r_b, p, ok=False, bestaetigt=True)
            ok_k = _namen(r_k, p, ok=True)
            fehl_k = _namen(r_k, p, ok=False)
            if fehl_k:
                urteil["angriff"] = {"eigene_tests_fehlgeschlagen": sorted(fehl_k)}
                return fertig("abgelehnt", f"eigene Tests des Kandidaten schlagen am Kandidaten fehl: {sorted(fehl_k)}")
            gueltig_roh = faellt_b & ok_k
            # Norm-Regel (3.7 F3) gilt auch für mitgebrachte Tests: Nachweis einer Behebung nur bei Absturz im Werk an der
            # Vorgeneration ODER Vertrags-/Verfassungsbezug im Test. Sonst kodiert der Test eine Meinung → 0, nicht ins Werk.
            # (Norm-Probe Lauf 12: ein mitgebrachter Test ohne Bezug kam ins Werk — hier geschlossen.)
            gueltig = set()
            for n in gueltig_roh:
                x = r_b.get(f"{p}::{n}", {})
                absturz = bool(x.get("ort")) and x["ort"].startswith(paket + "/") and not x.get("meldung", "").startswith(("AssertionError", "assert", "Failed"))
                if absturz or _nennt_vertrag(inhalt, n, verf, con, werk_id, bereich, vertrag_dateien_kandidat):
                    gueltig.add(n)
                else:
                    urteil["norm"].append(f"{p}::{n}")
            urteil["tests_verworfen"] += [f"{p}::{n} (besteht schon an der Vorgeneration — zählt nicht)" for n in sorted(_namen(r_b, p, ok=True))]
            urteil["tests_verworfen"] += [f"{p}::{n} (fehlerhafter Test)" for n in sorted(_namen(r_b, p, ok=False, bestaetigt=False))]
            urteil["tests_verworfen"] += [f"{p}::{n} (Norm ohne Absturz/Vertragsbezug — 0 Punkte, nicht ins Werk)" for n in sorted(gueltig_roh - gueltig)]
            # Vorhandene Testdatei: kein vorhandener Test darf verschwinden oder sich ändern (Anhang A Satz 6) —
            # ins Werk kommt die alte Datei plus die gültigen neuen Funktionen (Lücke bis Lauf 15: nur_funktionen hätte
            # die alte Datei durch die neuen Funktionen ersetzt).
            alt_datei = (werk / p)
            if alt_datei.exists():
                alt_code = alt_datei.read_text()
                fehlend = _fehlende_oder_geaenderte_tests(alt_code, inhalt)
                if fehlend:
                    return fertig("abgelehnt", f"Verfassung verletzt: entfernt oder ändert vorhandene Tests in {p}: {fehlend[:5]} (Anhang A Satz 6)")
                g = _anhaengen(alt_code, inhalt, gueltig) if gueltig else None
            else:
                g = nur_funktionen(inhalt, gueltig) if gueltig else None
            if g:
                testbestand[p] = g
                urteil["tests_neu"] += [f"{p}::{n}" for n in sorted(gueltig)]

    # Schritt 4: Angriff (schweres Modell bei Befundklasse)
    angriff, angriff_modell = _angriff(con, lauf_id, werk_id, paket, bereich, k["diff"], dateien, werk, urteil["befundklassen"])
    if angriff:
        ad = f"tests/test_{bereich}_immun_aegis_k{kandidat_id}_{bereich}.py"
        r_k = junit_lauf(werk, paket, {**code, ad: angriff}, [ad])
        r_b = junit_lauf(werk, paket, {ad: angriff}, [ad])
        best_k = _namen(r_k, ad, ok=False, bestaetigt=True)
        best_b = _namen(r_b, ad, ok=False, bestaetigt=True)
        fehlerhaft = _namen(r_k, ad, ok=False, bestaetigt=False) | _namen(r_b, ad, ok=False, bestaetigt=False)
        urteil["angriff"] = {"modell": angriff_modell, "bestaetigt_kandidat": sorted(best_k), "bestaetigt_basis": sorted(best_b),
                             "fehlerhaft": sorted(fehlerhaft), "gesamt": len(_namen(r_k, ad))}
        # Norm-Regel (3.7 F3): Ein Test, der an der Vorgeneration fällt und am Kandidaten besteht, ist nur dann Nachweis
        # einer Behebung, wenn (a) die Vorgeneration dabei mit einer Ausnahme IM WERK abstürzt oder (b) der Test einen
        # Vertrag/Verfassungssatz nennt. Sonst kodiert er eine Meinung → „offen“, 0 Punkte, nicht ins Werk.
        behoben_kand = best_b & _namen(r_k, ad, ok=True)
        nachweis, norm = set(), set()
        for n in behoben_kand:
            x = r_b.get(f"{ad}::{n}", {})
            absturz = bool(x.get("ort")) and x["ort"].startswith(paket + "/") and not x.get("meldung", "").startswith(("AssertionError", "assert", "Failed"))
            bezug = _nennt_vertrag(angriff, n, verf, con, werk_id, bereich, vertrag_dateien_kandidat)
            (nachweis if (absturz or bezug) else norm).add(n)
        # Regel (Philipp, 19.09.2026, Fassung 4 zu 3.7/3.5): Pareto je Test gilt für Tests IM WERK, für VERTRÄGE und für die
        # VERFASSUNG. Ein NEUER Angriffstest, der an der Vorgeneration besteht und am Kandidaten fällt, tötet nur dann,
        # wenn (a) der Kandidat dabei mit einer Ausnahme im Werk abstürzt oder (b) der Test einen Vertrag oder
        # Verfassungssatz durch explizite Kennung nennt. Sonst bleibt er „offen“, bringt 0 Punkte und tötet nicht —
        # er kommt weder als Fund ins Immunsystem noch in den gemessenen Testbestand, sonst schriebe er das ALTE
        # Verhalten als Norm fest (Lauf 16 Gen 4: K1191-Test kodierte den K1165-Fehler als Norm und tötete per
        # Pareto je Test jede Behebung — Lauf 16 deshalb nach Satz 2 F4 verworfen).
        best_k_norm = set()
        for n in set(best_k):
            x = r_k.get(f"{ad}::{n}", {})
            absturz_k = bool(x.get("ort")) and x["ort"].startswith(paket + "/") and not x.get("meldung", "").startswith(("AssertionError", "assert", "Failed"))
            if not (absturz_k or _nennt_vertrag(angriff, n, verf, con, werk_id, bereich, vertrag_dateien_kandidat)):
                best_k_norm.add(n)
        best_k = best_k - best_k_norm
        norm |= best_k_norm
        urteil["norm"] = sorted(norm)
        urteil["angriff"]["bestaetigt_kandidat"] = sorted(best_k)
        urteil["angriff"]["norm_am_kandidaten"] = sorted(best_k_norm)
        # Doppelungen (3.10 F5): je bestätigtem Fehler ein Test; gleiche BEHAUPTUNG = Doppelung (nicht gleiche Fundstelle)
        treffer = (best_k | nachweis) - fehlerhaft
        einzig, doppel = _doppelungen(treffer, {**r_k, **{k2: v for k2, v in r_b.items() if k2 not in r_k or r_k[k2]["ok"]}},
                                      ad, con, werk_id, bereich, code=angriff, paket=paket)
        urteil["doppelungen"] = sorted(doppel)
        urteil["behauptungen"] = {n: behauptung(angriff, n, paket) for n in sorted(treffer)}
        gefunden = einzig
        if gefunden:
            name = f"aegis_k{kandidat_id}_{bereich}"
            code_immun = nur_funktionen(angriff, gefunden)
            if code_immun:
                schluessel = " ".join(sorted({behauptung(angriff, n, paket) for n in gefunden}))
                with transaktion(con):
                    con.execute("INSERT OR IGNORE INTO immunsystem(werk_id, lauf_id, bereich, name, code, ursprung, status, erstellt_am, generation) VALUES (?,?,?,?,?,?,?,?,?)",
                                (werk_id, lauf_id, bereich, name, code_immun,
                                 f"Ankläger ({angriff_modell}), Kandidat {kandidat_id}: am Kandidaten {sorted(best_k)}, Behebung nachgewiesen {sorted(nachweis)}, Norm (offen) {sorted(norm)}, Doppelungen {sorted(doppel)} behauptung={schluessel}",
                                 "gefunden", protokoll.jetzt(), k["generation"]))
                urteil["immun"].append(name)
                protokoll.schreiben(con, "immun.gefunden", lauf_id=lauf_id, kandidat=kandidat_id, bereich=bereich, name=name,
                                    modell=angriff_modell, bestaetigt_kandidat=sorted(best_k), behebung_nachgewiesen=sorted(nachweis),
                                    norm_offen=sorted(norm), doppelungen=sorted(doppel), fehlerhaft=sorted(fehlerhaft))
                testbestand[ad] = code_immun
        if norm:
            # Norm-Tests bleiben als offener Fund im Immunsystem (separat), zählen nicht, kommen nicht ins Werk
            code_norm = nur_funktionen(angriff, norm)
            if code_norm:
                with transaktion(con):
                    con.execute("INSERT OR IGNORE INTO immunsystem(werk_id, lauf_id, bereich, name, code, ursprung, status, erstellt_am, generation) VALUES (?,?,?,?,?,?,?,?,?)",
                                (werk_id, lauf_id, bereich, f"norm_k{kandidat_id}_{bereich}", code_norm,
                                 f"Norm-Test ohne Absturz/Vertragsbezug (3.7 F3), Kandidat {kandidat_id}", "offen_norm", protokoll.jetzt(), k["generation"]))
                protokoll.schreiben(con, "immun.norm", lauf_id=lauf_id, kandidat=kandidat_id, bereich=bereich, tests=sorted(norm), zaehlt=0)

    testbestand_mit_vertraegen = {**testbestand, **vertrag_dateien_kandidat}

    # Schritt 5: paarweise Messung — Vorgeneration und Kandidat mit demselben Testbestand
    basis_paar = messgeraet.messen(werk, bereiche, paket, referenzlast, dateien=testbestand)
    mess = messgeraet.messen(werk, bereiche, paket, referenzlast, dateien={**code, **testbestand_mit_vertraegen})
    for name, mm in (("Vorgeneration", basis_paar), ("Kandidat", mess)):
        if not mm["gueltig"]:
            return fertig("abgelehnt", f"Kammer ({name}): {mm['grund']} (rc={mm.get('rc')})", mess if name == "Kandidat" else None)
    u = messgeraet.urteil_f2(basis_paar, mess, ausgang, bereiche, urteil["wirkungskreis"], tausch, nische=k["nische"])
    urteil["mass"] = u
    fb = set(basis_paar["werk"]["tests_fehlgeschlagen_liste"]); fk = set(mess["werk"]["tests_fehlgeschlagen_liste"])
    urteil["vertrag_verletzt"] = vertraege.verletzt(fb, fk)
    if urteil["vertrag_verletzt"] and not extra_code:
        # ohne Anpassung des Nachbarn: tot (Verhandlung übernimmt lauf.py, wenn der Kandidat den Vertrag benannt hat)
        u = {**u, "ok": False, "grund": "Vertrag verletzt (Schritt 2): " + ", ".join(urteil["vertrag_verletzt"])}
        urteil["mass"] = u
    # Ins Werk kommt nur, was der Kandidat BESTEHT (3.10: der Test beweist, dass der Fehler das Werk nicht
    # mehr trifft). Tests, die auch am Kandidaten fehlschlagen, bleiben im Immunsystem ('offen') und werden
    # späteren Kandidaten des Bereichs paarweise vorgelegt — sie kommen erst mit ihrer Behebung ins Werk.
    # (Lehre aus Lauf 6: sonst landen Fehler verworfener Kandidaten und unbelegte Modell-„Verträge" als rote Tests im Werk.)
    fehl_dateien = {f.split("::")[0] for f in mess["werk"]["tests_fehlgeschlagen_liste"]}
    tests_ins_werk = {p: c for p, c in testbestand.items() if p.split("/")[-1] not in fehl_dateien}
    urteil["tests_offen"] = sorted(p for p in testbestand if p not in tests_ins_werk)
    for p in tests_ins_werk:
        if "_immun_" in p and p not in bk:
            urteil["immun_bestanden"].append(p.split("_immun_")[1][:-3])
    dateien_final = {**code, **tests_ins_werk, **{p: c for p, c in vertrag_dateien_kandidat.items() if p.split("/")[-1] not in fehl_dateien}}
    if not u["ok"]:
        return fertig("abgelehnt", u["grund"], mess, dateien_final, basis_paar)
    return fertig("ueberlebt", u["grund"], mess, dateien_final, basis_paar)
