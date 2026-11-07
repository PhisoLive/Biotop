"""Kern: Messgerät — die harten Maße. Läuft ausschließlich in der Kammer.

Maße je Bereich (Richtung: ↑ = größer ist besser, ↓ = kleiner ist besser):
  tests_bestanden        ↑  bestandene Tests des Bereichs (Bezug: tests_gesamt)
  tests_fehlgeschlagen   ↓
  sicherheit_punkte      ↓  bandit: HIGH=10, MEDIUM=3, LOW=1 je Befund
  tote_funktionen        ↓  vulture, Vertrauen ≥ 60 %, nur Funktionen/Methoden/Klassen
  laufzeit_ms            ↓  Referenzlast (Kern-Skript je Werk), Minimum aus 3 Läufen
  groesste_funktion      ↓  Zeilen der längsten Funktion
Werkebene zusätzlich:  zyklen ↓ (Import-Zyklen zwischen Bereichen), bauzeit_ms ↓

Kernmaß FASSUNG 2 (Masterprompt v2, 3.5) — gilt ab Lauf 3:
  kern_bereich = −tests_fehlgeschlagen − sicherheit_punkte − tote_funktionen
  (sicherheit_punkte = 10·HIGH + 3·MEDIUM + 1·LOW). Höchstwert 0. Bestandene
  Tests zählen nicht. Paarweise Messung: Vorgeneration und Kandidat mit demselben
  Testbestand (dem des Kandidaten). Pareto-Maße (nie schlechter im Wirkungskreis):
  tests_fehlgeschlagen, sicherheit_punkte, tote_funktionen, baut. Grenzmaße
  (gegen den Ausgangszustand des Laufs; Vorgabe ohne Verfassung: laufzeit ×2,
  sonst +25 %; Tauschregel der Verfassung kann laufzeit auf ×5 heben, wenn im
  Bereich ein Sicherheitsbefund verschwindet): laufzeit_ms, groesste_funktion,
  bauzeit_ms, zyklen. Speicher: nicht gemessen (Liste für danach).
Kernmaß FASSUNG 1 (nur noch zur Nachrechnung der Kurve von Lauf 2):
  kern = tests_bestanden − tests_fehlgeschlagen − 3·sicherheit_punkte − tote_funktionen.

Pareto-Vergleich (`vergleichen`): ein Maß gilt als gesunken, wenn es sich in
der schlechten Richtung ändert; für laufzeit_ms erst ab +15 % (Messrauschen der
Kammer; als gestiegen gilt es erst ab −15 %). Alle anderen Maße: jede Änderung
zählt.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from ..organe import kammer

RICHTUNG = {
    "tests_bestanden": +1, "tests_fehlgeschlagen": -1, "sicherheit_punkte": -1,
    "tote_funktionen": -1, "laufzeit_ms": -1, "groesste_funktion": -1,
    "zyklen": -1, "bauzeit_ms": -1,
}
TOLERANZ = {"laufzeit_ms": 0.15, "bauzeit_ms": 0.50, "groesste_funktion": 0.25}
BANDIT_GEWICHT = {"HIGH": 10, "MEDIUM": 3, "LOW": 1}

MESSSKRIPT = r'''
import ast, json, os, subprocess, sys, time, importlib, io, contextlib
werk = "/werk"
bereiche = json.loads(sys.argv[1])
paket = sys.argv[2]
ref_pfad = sys.argv[3] if len(sys.argv) > 3 else ""
ergebnis = {"bereiche": {}, "werk": {}}

def lauf(cmd, timeout=100):
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=werk, timeout=timeout)
    return p.returncode, p.stdout, p.stderr

# --- Bauzeit (Import aller Bereiche) ---
t0 = time.monotonic()
rc, out, err = lauf([sys.executable, "-c", "import " + ",".join(paket + "." + b for b in bereiche)])
ergebnis["werk"]["bauzeit_ms"] = round((time.monotonic() - t0) * 1000, 1)
ergebnis["werk"]["baut"] = (rc == 0)
ergebnis["werk"]["bau_fehler"] = err[-2000:] if rc != 0 else ""

# --- Tests je Bereich (Datei-Zuordnung über Namen) ---
tests_dir = os.path.join(werk, "tests")
testdateien = sorted(f for f in os.listdir(tests_dir) if f.startswith("test_") and f.endswith(".py")) if os.path.isdir(tests_dir) else []
erwartete_testdateien = {os.path.relpath(os.path.join(w, f), werk)
    for w, _, dateien in os.walk(tests_dir) for f in dateien if f.startswith("test_") and f.endswith(".py")}
def zuordnung(f):
    # Vertragstests (tests/vertraege/test_vertrag_<konsument>_<lieferant>.py) zaehlen beim Lieferanten
    if f.startswith("test_vertrag_"):
        t = f[:-3].split("_")
        return t[-1] if t[-1] in bereiche else None
    for b in bereiche:
        if f == f"test_{b}.py" or f.startswith(f"test_immun_{b}_") or f.startswith(f"test_{b}_"):
            return b
    return None
ergebnis["werk"]["tests_ohne_bereich"] = [f for f in testdateien if zuordnung(f) is None]
# Begleitbeleg aus DEM Testlauf: rc=1 kann ein vollständiger Fehlschlag oder
# ein abgebrochener Teillauf sein; JUnit allein nennt nur die berichteten Fälle.
pytest_start = r"""
import json, pytest, sys
nachweis = {"gesammelt": [], "aufrufe": [], "beendet": [], "sammlungsfehler": [], "abgewaehlt": []}
class Nachweis:
    def pytest_deselected(self, items):
        nachweis["abgewaehlt"].extend(item.nodeid for item in items)
    def pytest_collection_finish(self, session):
        nachweis["gesammelt"] = [item.nodeid for item in session.items]
    def pytest_collectreport(self, report):
        if report.failed:
            nachweis["sammlungsfehler"].append(report.nodeid)
    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            nachweis["aufrufe"].append(report.nodeid)
        if report.when == "teardown":
            nachweis["beendet"].append(report.nodeid)
rc = pytest.main(sys.argv[1:], plugins=[Nachweis()])
with open('/tmp/pytest-nachweis.json', 'w') as f:
    json.dump(nachweis, f)
sys.exit(rc)
"""
rc, out, err = lauf([sys.executable, "-c", pytest_start, "-q", "-p", "no:cacheprovider", "--tb=short", "-rN", "tests", "--junitxml=/tmp/junit.xml"], timeout=110)
ergebnis["werk"]["pytest_rc"] = rc
ergebnis["werk"]["pytest_tail"] = out[-3000:]
import xml.etree.ElementTree as ET
je_datei = {}
fehler_liste = []
if rc not in (0, 1):
    raise ValueError(f"pytest-Nachweis abgebrochen/leer (rc={rc}): {out[-1000:]} {err[-1000:]}")
testfaelle = list(ET.parse("/tmp/junit.xml").getroot().iter("testcase"))
if not testfaelle:
    raise ValueError("JUnit-Nachweis leer")
with open('/tmp/pytest-nachweis.json') as f:
    nachweis = json.load(f)
gesammelt = sorted(nachweis["gesammelt"])
if (nachweis["sammlungsfehler"] or nachweis["abgewaehlt"] or not gesammelt
        or len(testfaelle) != len(gesammelt)
        or not erwartete_testdateien <= {n.split("::")[0] for n in gesammelt}
        or sorted(nachweis["aufrufe"]) != gesammelt or sorted(nachweis["beendet"]) != gesammelt):
    raise ValueError("pytest-Nachweis unvollständig/abgebrochen: " + repr(nachweis))
for tc in testfaelle:
    datei = (tc.get("classname") or "").split(".")[-1] + ".py"
    if datei.startswith("tests."): datei = datei[6:]
    if tc.find("skipped") is not None:
        raise ValueError("JUnit-Nachweis übersprungen: " + str(tc.get("name")))
    ok = tc.find("failure") is None and tc.find("error") is None
    b = zuordnung(datei)
    je_datei.setdefault(b, [0, 0])
    je_datei[b][0 if ok else 1] += 1
    if not ok:
        fehler_liste.append(f"{datei}::{tc.get('name')}")
ergebnis["werk"]["tests_fehlgeschlagen_liste"] = fehler_liste[:100]

# --- bandit / vulture / groesste Funktion je Bereich ---
def bandit(pfad):
    rc, out, err = lauf([sys.executable, "-m", "bandit", "-q", "-r", pfad, "-f", "json"])
    if rc not in (0, 1):
        raise ValueError(f"Bandit abgebrochen (rc={rc}): {out[-500:]} {err[-500:]}")
    d = json.loads(out)
    if (not isinstance(d["results"], list) or d["errors"] != []
            or not any(f.startswith(pfad + "/") for f in d["metrics"])):
        raise ValueError("Bandit-Nachweis fehlt/unvollständig: " + out[-1000:])
    gew = {"HIGH": 10, "MEDIUM": 3, "LOW": 1}
    befunde = [{"test": r["test_id"], "schwere": r["issue_severity"], "datei": r["filename"], "zeile": r["line_number"], "text": r["issue_text"][:160]} for r in d["results"]]
    return sum(gew.get(b["schwere"], 0) for b in befunde), befunde, ""

def vulture(pfad):
    rc, out, err = lauf([sys.executable, "-m", "vulture", pfad, "tests", "--min-confidence", "60"])
    import re
    meldungen = [z for z in out.splitlines() if z.strip()]
    # Vulture: 0 = sauber (leere stdout ist regulär), 3 = Befunde, 1/2 = Fehler.
    if (rc not in (0, 3) or (rc == 3 and not meldungen)
            or any(not re.match(r"^.+:\d+: (?:unused .+|unreachable code .+) \(\d+% confidence\)$", z) for z in meldungen)):
        raise ValueError(f"Vulture-Nachweis fehlt/abgebrochen (rc={rc}): {out[-1000:]} {err[-1000:]}")
    zeilen = [z for z in meldungen if pfad in z and ("function" in z or "method" in z or "class" in z)]
    return len(zeilen), zeilen[:50]

def groesste_funktion(pfad):
    m = 0; name = ""
    for wurzel, _, dateien in os.walk(pfad):
        for f in dateien:
            if not f.endswith(".py"): continue
            p = os.path.join(wurzel, f)
            try:
                baum = ast.parse(open(p).read())
            except Exception:
                continue
            for kn in ast.walk(baum):
                if isinstance(kn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    n = kn.end_lineno - kn.lineno + 1
                    if n > m: m, name = n, f"{os.path.relpath(p, werk)}:{kn.name}"
    return m, name

for b in bereiche:
    if b not in je_datei:
        raise ValueError("Testnachweis für Bereich fehlt: " + b)
    pfad = os.path.join(paket, b)
    sp, befunde, sfehler = bandit(pfad)
    tf, tote = vulture(pfad)
    gf, gfname = groesste_funktion(pfad)
    ok, schlecht = je_datei.get(b, [0, 0])
    ergebnis["bereiche"][b] = {
        "tests_bestanden": ok, "tests_fehlgeschlagen": schlecht, "tests_gesamt": ok + schlecht,
        "sicherheit_punkte": sp, "sicherheit_befunde": befunde, "sicherheit_fehler": sfehler,
        "tote_funktionen": tf, "tote_liste": tote,
        "groesste_funktion": gf, "groesste_funktion_name": gfname,
    }

# --- Referenzlast ---
if ref_pfad and os.path.exists(ref_pfad):
    ns = {}
    exec(open(ref_pfad).read(), ns)
    for b in bereiche:
        fn = ns.get("last_" + b)
        if fn is None:
            ergebnis["bereiche"][b]["laufzeit_ms"] = None
            continue
        # Fassung 5 (3.5): Laufzeit ist der MEDIAN aus drei Durchläufen, nie ein Einzelwert und nie das Minimum.
        # Das Minimum belohnt Ausreißer nach unten: es drückt den Bestwert des Laufs künstlich, und spätere
        # Kandidaten reißen dann das Grenzmaß am Messrauschen statt an einer Verschlechterung.
        werte = []
        for _ in range(3):
            try:
                t0 = time.perf_counter(); fn(); d = (time.perf_counter() - t0) * 1000
            except Exception as e:
                werte = []; ergebnis["bereiche"][b]["laufzeit_fehler"] = repr(e)[:300]; break
            werte.append(d)
        if werte:
            werte.sort()
            ergebnis["bereiche"][b]["laufzeit_ms"] = round(werte[len(werte) // 2], 2)
            ergebnis["bereiche"][b]["laufzeit_roh"] = [round(x, 2) for x in werte]
        else:
            ergebnis["bereiche"][b]["laufzeit_ms"] = None

# --- Zyklen zwischen Bereichen ---
kanten = set()
for b in bereiche:
    for wurzel, _, dateien in os.walk(os.path.join(werk, paket, b)):
        for f in dateien:
            if f.endswith(".py"):
                for zeile in open(os.path.join(wurzel, f)):
                    for b2 in bereiche:
                        if b2 != b and (f"{paket}.{b2}" in zeile or f"from ..{b2}" in zeile or f"from .{b2}" in zeile and False):
                            kanten.add((b, b2))
def zyklen():
    adj = {}
    for a, c in kanten: adj.setdefault(a, set()).add(c)
    z = 0
    for start in bereiche:
        stapel = [start]; gesehen = set()
        while stapel:
            k = stapel.pop()
            for n in adj.get(k, ()):
                if n == start: z += 1; stapel = []; break
                if n not in gesehen: gesehen.add(n); stapel.append(n)
    return z
ergebnis["werk"]["zyklen"] = zyklen()
ergebnis["werk"]["kanten"] = sorted(kanten)
print("@@MESSUNG@@" + json.dumps(ergebnis) + "@@ENDE@@")
'''


def messen(werk: Path, bereiche: list[str], paket: str, referenzlast: str | None,
           dateien: dict[str, str] | None = None, zeitlimit_s: int = 150) -> dict:
    """Misst alle harten Maße in der Kammer. Rückgabe: Messung (dict) inkl. Rohausgabe."""
    extra = {"_messgeraet/messen.py": MESSSKRIPT}
    if referenzlast:
        extra["_messgeraet/referenzlast.py"] = referenzlast
    extra.update(dateien or {})
    e = kammer.ausfuehren(
        werk, ["python", "_messgeraet/messen.py", json.dumps(bereiche), paket,
               "_messgeraet/referenzlast.py" if referenzlast else ""],
        zeitlimit_s=zeitlimit_s, dateien=extra,
    )
    m = re.search(r"@@MESSUNG@@(.*)@@ENDE@@", e.stdout, re.S)
    ungueltig = {"gueltig": False, "rc": e.rc, "stdout": e.stdout[-4000:],
                 "stderr": e.stderr[-4000:], "dauer_s": e.dauer_s}
    if e.zeitlimit or e.rc != 0 or not m:
        ungueltig["grund"] = "Zeitlimit" if e.zeitlimit else (f"Kammer abgebrochen (rc={e.rc})" if e.rc != 0 else "keine Messausgabe")
        return ungueltig
    try:
        d = json.loads(m.group(1))
        if not bereiche or set(d["bereiche"]) != set(bereiche):
            raise ValueError("angeforderte Bereiche fehlen in der Messausgabe")
        w = d["werk"]
        for k in ("baut", "pytest_rc", "tests_fehlgeschlagen_liste", "zyklen", "bauzeit_ms"):
            if k not in w or w[k] is None:
                raise ValueError("Werk-Pflichtnachweis fehlt: " + k)
        if w["pytest_rc"] not in (0, 1) or not isinstance(w["tests_fehlgeschlagen_liste"], list):
            raise ValueError("pytest-/Einzeltestnachweis unbrauchbar")
        if referenzlast:
            for b in bereiche:
                if d["bereiche"][b].get("laufzeit_ms") is None:
                    raise ValueError("angeforderter Laufzeitnachweis fehlt/abgebrochen: " + b)
        d["kernmass"] = kernmass(d)
    except (ValueError, KeyError, TypeError) as exc:
        ungueltig["grund"] = "unvollständige Messausgabe: " + str(exc)
        return ungueltig
    d["gueltig"] = True
    d["dauer_s"] = round(e.dauer_s, 2)
    return d


def kernmass(m: dict) -> int:
    k = 0
    for b in m["bereiche"].values():
        k += b["tests_bestanden"] - b["tests_fehlgeschlagen"] - 3 * b["sicherheit_punkte"] - b["tote_funktionen"]
    return k


def bereich_masse(m: dict, bereich: str) -> dict:
    b = m["bereiche"][bereich]
    return {k: b.get(k) for k in ("tests_bestanden", "tests_fehlgeschlagen", "sicherheit_punkte",
                                  "tote_funktionen", "laufzeit_ms", "groesste_funktion")}


def werk_masse(m: dict) -> dict:
    return {"zyklen": m["werk"]["zyklen"], "bauzeit_ms": m["werk"]["bauzeit_ms"], "kernmass": m["kernmass"]}


def vergleichen(vorher: dict, nachher: dict) -> dict:
    """Vergleicht zwei Maßsätze (gleiche Schlüssel). Rückgabe:
    {"gesunken": [...], "gestiegen": [...], "gleich": [...]} mit Angaben."""
    r = {"gesunken": [], "gestiegen": [], "gleich": []}
    for k, v0 in vorher.items():
        v1 = nachher.get(k)
        if v0 is None or v1 is None:
            r["gleich"].append(f"{k}: nicht messbar ({v0}→{v1})")
            continue
        richtung = RICHTUNG.get(k, +1)
        tol = TOLERANZ.get(k, 0.0)
        delta = (v1 - v0) * richtung  # positiv = besser
        schwelle = abs(v0) * tol
        text = f"{k}: {v0} → {v1}"
        if delta > schwelle:
            r["gestiegen"].append(text)
        elif delta < -schwelle:
            r["gesunken"].append(text)
        else:
            r["gleich"].append(text)
    return r


# =============================================================== Fassung 2
PARETO_F2 = ("tests_fehlgeschlagen", "sicherheit_punkte", "tote_funktionen")
GRENZ_F2 = {"laufzeit_ms": 2.0, "groesste_funktion": 1.25}          # Faktor gegen Ausgangszustand, je Bereich
GRENZ_WERK_F2 = {"bauzeit_ms": 1.25, "zyklen": 1.25}                  # Werkebene


def kernmass_f2_bereich(b: dict) -> int:
    return -b["tests_fehlgeschlagen"] - b["sicherheit_punkte"] - b["tote_funktionen"]


def kernmass_f2(m: dict) -> int:
    return sum(kernmass_f2_bereich(b) for b in m["bereiche"].values())


def kernmass_f1(m: dict) -> int:
    return kernmass(m)


def pareto_f2(basis: dict, kandidat: dict, bereiche: list[str]) -> tuple[list[str], list[str]]:
    """Paarweiser Vergleich (beide mit demselben Testbestand gemessen).
    Rückgabe (schlechter, besser) als Texte 'bereich.maß: a → b'."""
    schlechter, besser = [], []
    for b in bereiche:
        v0, v1 = basis["bereiche"][b], kandidat["bereiche"][b]
        for k in PARETO_F2:
            if v1[k] > v0[k]:
                schlechter.append(f"{b}.{k}: {v0[k]} → {v1[k]}")
            elif v1[k] < v0[k]:
                besser.append(f"{b}.{k}: {v0[k]} → {v1[k]}")
    if basis["werk"]["baut"] and not kandidat["werk"]["baut"]:
        schlechter.append("werk.baut: True → False")
    # JE TEST (Lehre aus Lauf 7): ein Test, der an der Vorgeneration besteht und am Kandidaten fällt, ist eine
    # Regression — auch wenn die Fehlschlags-Summe des Bereichs sinkt. Tests, die an beiden fallen, sind offen, keine Regression.
    for name, messung in (("Basis", basis), ("Kandidat", kandidat)):
        if not isinstance(messung["werk"].get("tests_fehlgeschlagen_liste"), list):
            schlechter.append(f"{name}: Nachweis je Test fehlt/unbrauchbar (tests_fehlgeschlagen_liste)")
            return schlechter, besser
    fehl_basis = set(basis["werk"]["tests_fehlgeschlagen_liste"])
    fehl_kand = set(kandidat["werk"]["tests_fehlgeschlagen_liste"])
    regress = sorted(fehl_kand - fehl_basis)
    if regress:
        schlechter.append("Regression je Test (bestand an der Vorgeneration, fällt am Kandidaten): " + ", ".join(regress[:6]) + (" …" if len(regress) > 6 else ""))
    return schlechter, besser


def streuung(messungen: list[float], ebene: str = "zwischen") -> dict:
    """Streuung einer Kennzahl über WIEDERHOLTE MESSUNGEN (Fassung 6, allgemeine Regel).

    Regel: **Streuung wird immer zwischen Messungen gebildet, nie innerhalb einer.** Der Median glättet
    innerhalb (drei Durchläufe je Messwert, 3.5), die Streuung misst zwischen — wer beides auf derselben Ebene
    bildet, misst die Glättung statt der Sache. Das gilt für jede Kennzahl, die das Biotop über wiederholte
    Messungen bildet, nicht nur für die Rauschmessung.

    Gefunden an der Probe zu „Generation minus eins": Eine Referenzlast, die jeden zweiten EINZELAUFRUF um 150 ms
    verzögerte, ergab fünf stabile Messwerte (Toleranz 1,20) — der Median hatte die Unstetigkeit weggeglättet.
    Erst als die Verzögerung zwischen ganzen MESSUNGEN wechselte, wurde sie sichtbar (Spannweite 56 %).

    `messungen` muss die Liste der bereits geglätteten Messwerte sein (je Wert ein Median aus n Durchläufen),
    niemals die Rohwerte einer einzelnen Messung. `ebene="innerhalb"` ist verboten und wirft — der Aufrufer soll
    den Fehler beim Schreiben sehen, nicht in der Zahl.
    """
    if ebene != "zwischen":
        raise ValueError("Streuung wird zwischen Messungen gebildet, nie innerhalb einer (Fassung 6, 3.5). "
                         "Die Rohwerte einer einzelnen Messung ergeben die Glättung, nicht die Streuung.")
    w = sorted(float(x) for x in messungen)
    if len(w) < 2:
        return {"spannweite": None, "median": (w[0] if w else None), "n": len(w),
                "hinweis": "weniger als zwei Messungen — keine Streuung bestimmbar"}
    mitte = w[1:-1] if len(w) >= 3 else w
    return {"spannweite": round((max(mitte) - min(mitte)) / min(mitte), 3) if min(mitte) > 0 else 0.0,
            "median": w[len(w) // 2], "n": len(w), "getrimmt": len(w) - len(mitte), "werte": [round(x, 2) for x in w]}


RAUSCH_F4 = 1.15  # F4: ohne Kernmaßgewinn darf kein Grenzmaß über Bestwert + 15 % (Kammer-Rauschen)

# --- Rauschmessung (Fassung 6, Festlegung Chat-Claude 19.09.2026) -------------------------------------------------
RAUSCH_MESSUNGEN = 5      # fünf Werte je Bereich
RAUSCH_DECKEL = 2.0       # Toleranz nie über Faktor 2,0
RAUSCH_MELDESCHWELLE = 1.5  # darüber ist es kein Rauschen mehr, sondern ein Messproblem
RAUSCH_AUSSETZER = 5.0    # Einzelwert über dem Fünffachen des Medians = Maschinenaussetzer, nicht Rauschen
RAUSCH_ZUSCHLAG = 0.10    # gemessene Spannweite + 10 Prozentpunkte


def rauschtoleranz_aus_werten(werte: list[float]) -> dict:
    """Aus fünf Messwerten eines Bereichs die Rauschtoleranz bestimmen (Fassung 6).

    Regeln, in dieser Reihenfolge:
    1. Aussetzer: Ein Einzelwert über dem Fünffachen des Medians ist ein Maschinenaussetzer (Container-Hänger,
       fremde Last), kein Eigenrauschen des Werks. Er wird verworfen und muss einmal nachgemessen werden.
       Grund: [1,31 / 1,51 / 35,22] ms ergäbe sonst eine Toleranz von 2.600 % — ein Fenster, in dem danach
       jede echte Verschlechterung durchgeht.
    2. Getrimmte Spannweite: höchsten und niedrigsten Wert streichen, Spannweite aus den mittleren drei.
    3. Toleranz = Spannweite + 10 Prozentpunkte, mindestens 1,15, höchstens 2,0 (Deckel).
    4. Über 1,5 ist das Ergebnis kein brauchbares Maß mehr: `meldung` wird gesetzt, der Aufrufer meldet ein
       Messproblem, statt die Zahl als Toleranz hinzunehmen.
    Rückgabe: {"toleranz", "spannweite", "median", "werte", "aussetzer", "nachmessen", "meldung"}.
    """
    import math
    if any(isinstance(w, bool) or not math.isfinite(float(w)) or float(w) <= 0 for w in werte):
        raise ValueError("Rauschwerte müssen endlich und positiv sein; Bool-Werte sind keine Messung")
    sortiert = sorted(float(w) for w in werte)
    if len(sortiert) != RAUSCH_MESSUNGEN:
        return {"toleranz": RAUSCH_F4, "spannweite": None, "median": None, "werte": sortiert, "aussetzer": [],
                "nachmessen": True, "meldung": f"{len(sortiert)} von {RAUSCH_MESSUNGEN} erforderlichen Messwerten — keine gültige Rauschmessung"}
    median = sortiert[len(sortiert) // 2]
    aussetzer = [w for w in sortiert if median > 0 and w > median * RAUSCH_AUSSETZER]
    rest = [w for w in sortiert if w not in aussetzer]
    if len(rest) < 3:
        return {"toleranz": RAUSCH_F4, "spannweite": None, "median": round(median, 2), "werte": [round(w, 2) for w in sortiert],
                "aussetzer": list(aussetzer), "nachmessen": True,
                "meldung": f"nur {len(rest)} brauchbare Werte nach Aussetzer-Abzug — nachmessen"}
    # Streuung IMMER zwischen Messungen, nie innerhalb einer (Fassung 6) — eine Stelle, eine Regel.
    s = streuung(rest)
    mitte = rest[1:-1] if len(rest) >= 3 else rest
    spannweite = s["spannweite"] or 0.0
    toleranz = min(RAUSCH_DECKEL, max(RAUSCH_F4, 1.0 + spannweite + RAUSCH_ZUSCHLAG))
    meldung = None
    if toleranz > RAUSCH_MELDESCHWELLE:
        meldung = (f"Messproblem: Eigenrauschen {spannweite*100:.0f} % über die mittleren {len(mitte)} von "
                   f"{len(sortiert)} Werten — Toleranz {toleranz:.2f} über der Meldeschwelle {RAUSCH_MELDESCHWELLE}. "
                   f"Das ist kein Rauschen mehr, das ist ein kaputtes Messgerät oder eine unstete Referenzlast.")
    return {"toleranz": round(toleranz, 3), "spannweite": round(spannweite, 3), "median": round(median, 2),
            "werte": [round(w, 2) for w in sortiert], "mittlere": [round(w, 2) for w in mitte],
            "aussetzer": list(aussetzer), "nachmessen": bool(aussetzer), "meldung": meldung}


def bestwerte(angenommene: list[dict], bereiche: list[str]) -> dict:
    """F4 3.5: je Maß und Bereich der beste Wert aller bisher angenommenen Generationen einschließlich Ausgang.
    Eingabe: Messungen (Generation 0 … letzte angenommene). Rückgabe im Format einer Messung (nur die Grenzmaße)."""
    best = {"bereiche": {b: {} for b in bereiche}, "werk": {}}
    for m in angenommene:
        if not m:
            continue
        for b in bereiche:
            mb = m["bereiche"].get(b) or {}
            for k in ("laufzeit_ms", "groesste_funktion"):
                v = mb.get(k)
                if v is None:
                    continue
                bb = best["bereiche"][b]
                bb[k] = v if bb.get(k) is None else min(bb[k], v)
        for k in ("zyklen", "bauzeit_ms"):
            v = (m.get("werk") or {}).get(k)
            if v is None:
                continue
            best["werk"][k] = v if best["werk"].get(k) is None else min(best["werk"][k], v)
    return best


def grenzen_f2(ausgang: dict, kandidat: dict, bereiche: list[str], tausch: dict | None = None,
               sicherheit_gesunken: set[str] = frozenset(), kernmassgewinn: bool = True,
               rauschtoleranz: dict | None = None) -> list[str]:
    """Grenzmaße gegen den Bezug `ausgang` — seit F4 der Bestwert des Laufs (bestwerte()), nicht der Ausgang allein.
    F4-Regel: ohne Kernmaßgewinn nur Rauschtoleranz; mit Kernmaßgewinn Tauschregel der Verfassung
    (Vorgabe Laufzeit × 2, Speicher/Bauzeit/Zyklen +25 %). `tausch` z. B. {"laufzeit_faktor": 2,
    "laufzeit_faktor_bei_sicherheitsgewinn": 5, "sonst_faktor": 1.25}. `sicherheit_gesunken` = Bereiche, in denen der
    Kandidat sicherheit_punkte senkt.
    F5 3.5: `rauschtoleranz` = {bereich: faktor} aus der Rauschmessung vor dem Lauf (gemessene Spannweite + 10
    Prozentpunkte, mindestens 1,15). Fehlt sie, gilt der feste Wert RAUSCH_F4 — dann steht das aber im Grund.
    Rückgabe: Liste gerissener Grenzen (leer = alles innerhalb)."""
    t = tausch or {}
    rt = rauschtoleranz or {}
    gesperrt = set(t.get("_gesperrte_bereiche") or [])
    lf = float(t.get("laufzeit_faktor", GRENZ_F2["laufzeit_ms"]))
    lf_s = float(t.get("laufzeit_faktor_bei_sicherheitsgewinn", lf))
    sf = float(t.get("sonst_faktor", 1.25))
    bezug = "Bestwert" if (ausgang.get("bezug") == "bestwert") else "Ausgang"
    gerissen = []
    for b in bereiche:
        a, k = ausgang["bereiche"][b], kandidat["bereiche"][b]
        # Ohne Kernmaßgewinn zählt allein die Rauschtoleranz — je Bereich gemessen, sonst der feste Rückfallwert.
        if kernmassgewinn:
            b_lf, b_lf_s, b_sf, quelle = lf, lf_s, sf, "Tauschregel"
        else:
            gemessen = rt.get(b)
            b_lf = b_lf_s = b_sf = float(gemessen or RAUSCH_F4)
            quelle = f"gemessene Rauschtoleranz {b_lf:.2f}" if gemessen else f"Rückfallwert {RAUSCH_F4} (keine Rauschmessung)"
        if b not in gesperrt and a.get("laufzeit_ms") and k.get("laufzeit_ms"):
            faktor = b_lf_s if b in sicherheit_gesunken else b_lf
            grenze = a["laufzeit_ms"] * faktor
            if k["laufzeit_ms"] > grenze:
                gerissen.append(f"{b}.laufzeit_ms: {k['laufzeit_ms']} > Grenze {grenze:.1f} ({bezug} {a['laufzeit_ms']} × {faktor:.2f}"
                                f"{'' if kernmassgewinn else ', ohne Kernmaßgewinn nur ' + quelle})")
        # F3: größte Funktion absolut 60 Zeilen; +25 % nur, wenn sie im Ausgang schon darüber lag
        g_abs = float(t.get("groesste_funktion_absolut", 60))
        grenze_g = max(g_abs, a["groesste_funktion"] * b_sf) if a["groesste_funktion"] > g_abs else g_abs
        if k["groesste_funktion"] > grenze_g:
            gerissen.append(f"{b}.groesste_funktion: {k['groesste_funktion']} > Grenze {grenze_g:.0f} (absolut {g_abs:.0f} / +25 % falls {bezug} darüber)")
    sf_werk = sf if kernmassgewinn else RAUSCH_F4
    if kandidat["werk"]["zyklen"] > ausgang["werk"]["zyklen"] * sf_werk:
        gerissen.append(f"werk.zyklen: {kandidat['werk']['zyklen']} > {ausgang['werk']['zyklen'] * sf_werk:.0f} ({bezug} {ausgang['werk']['zyklen']})")
    # Bauzeit: Kammer-Start schwankt um ±200 ms unabhängig vom Code — absolute Toleranz bleibt (seit Phase 1 gemessen)
    if kandidat["werk"]["bauzeit_ms"] > max(ausgang["werk"]["bauzeit_ms"] * sf_werk, ausgang["werk"]["bauzeit_ms"] + 200):
        gerissen.append(f"werk.bauzeit_ms: {kandidat['werk']['bauzeit_ms']} > {ausgang['werk']['bauzeit_ms'] * sf_werk:.0f} ({bezug} {ausgang['werk']['bauzeit_ms']})")
    return gerissen


def urteil_f2(basis: dict, kandidat: dict, ausgang: dict, bereiche: list[str], wirkungskreis: list[str],
              tausch: dict | None = None, nische: str | None = None) -> dict:
    """Vollständiges Maß-Urteil Fassung 2. Rückgabe mit 'ok', 'zuwachs', 'grund', Belegen."""
    schlechter, besser = pareto_f2(basis, kandidat, bereiche)
    sich = {b for b in bereiche if kandidat["bereiche"][b]["sicherheit_punkte"] < basis["bereiche"][b]["sicherheit_punkte"]}
    k0, k1 = kernmass_f2(basis), kernmass_f2(kandidat)
    # F4: `ausgang` ist der Bezug der Grenzmaße — Bestwert des Laufs (lauf.py übergibt bestwerte()); ohne Kernmaßgewinn nur +15 %
    gerissen = grenzen_f2(ausgang, kandidat, bereiche, tausch, sich, kernmassgewinn=(k1 - k0) > 0,
                         rauschtoleranz=(tausch or {}).get("_rauschtoleranz"))
    r = {"kern_basis": k0, "kern_kandidat": k1, "zuwachs": k1 - k0, "pareto_schlechter": schlechter,
         "pareto_besser": besser, "grenzen_gerissen": gerissen, "sicherheit_gesunken_in": sorted(sich)}
    gesperrt = sorted(set((tausch or {}).get("_gesperrte_bereiche") or []) & set(wirkungskreis))
    if gesperrt:
        r.update(ok=False, grund="Rauschmessung: Wirkungskreis gesperrt: " + ", ".join(gesperrt))
    elif not kandidat["werk"]["baut"]:
        r.update(ok=False, grund="baut nicht")
    elif schlechter:
        r.update(ok=False, grund="Pareto verletzt: " + "; ".join(schlechter))
    elif gerissen:
        r.update(ok=False, grund="Grenzmaß gerissen: " + "; ".join(gerissen))
    elif nische == "schnell":
        # Nischenmaß (3.5): Laufzeit; angenommen nur, wenn Kernmaß gleich bleibt oder steigt und die Laufzeit
        # eines Bereichs im Wirkungskreis um ≥ 15 % sinkt (Kammer-Rauschen liegt unter 15 %).
        gewinne = []
        for b in wirkungskreis:
            l0, l1 = basis["bereiche"][b].get("laufzeit_ms"), kandidat["bereiche"][b].get("laufzeit_ms")
            if l0 and l1 and l1 <= l0 * 0.85:
                gewinne.append(f"{b}.laufzeit_ms: {l0} → {l1} (−{(1 - l1 / l0) * 100:.0f} %)")
        r["laufzeit_gewinne"] = gewinne
        if k1 - k0 < 0:
            r.update(ok=False, grund=f"Nische schnell: Kernmaß gesunken ({k0} → {k1})")
        elif not gewinne and k1 - k0 <= 0:
            r.update(ok=False, grund="Nische schnell: Laufzeit nicht um ≥ 15 % gesunken, Kernmaß unverändert")
        else:
            r.update(ok=True, grund=f"Nische schnell: {'; '.join(gewinne) or ''} Kernmaß {k0} → {k1}")
    elif k1 - k0 <= 0:
        r.update(ok=False, grund=f"Kernmaß unverändert ({k0} → {k1}); bestandene Tests zählen nicht")
    else:
        r.update(ok=True, grund=f"Kernmaß {k0} → {k1} (+{k1 - k0}): " + "; ".join(besser))
    return r
