"""Verhaltensvergleich Vorgeneration gegen Kandidat — Abwehr gegen „schneller, aber falsch".

Befund aus Lauf 37 (T3): Kandidat K2934 führte einen WeakMap-Cache in
`zahlen/statistik.ts::geordnet()` ein, der sortierte Kopien an der Array-REFERENZ
festmacht und nur die LÄNGE gegenprüft. Wird derselbe Array in place geändert, liefert
die Funktion das veraltete Ergebnis. Am echten Werk gemessen: `quantil` gibt 3 statt 300,
`spannweite` 8 statt 80. Der Kandidat wurde angenommen — der Annahmegrund lautete
„zahlen.laufzeit_ms 2,73 → 1,39 ms (−49 %)", und kein Test im Werk prüfte das Verhalten.
Lauf 38 baute denselben Fehlertyp erneut ein (K3121, Modulvariablen-Cache, −66 %), weil
dieses Organ zwar gebaut und getestet, aber nirgends in den Annahmepfad eingehängt war.

Ein Einzelaufruf hätte den Fehler nie gesehen: Beim ersten Aufruf ist der Cache leer und
die Antwort richtig. Sichtbar wird er erst in der FOLGE — aufrufen, Eingabe an Ort und
Stelle ändern, erneut aufrufen — und beim ALIAS, wenn dieselbe Referenz zweimal auftritt.

Wie die Sonde beobachtet (kern/ts/verhalten.mjs, verhalten-runner.mjs): Die exportierten
Funktionen der vom Kandidaten geänderten Module werden im gebauten Stand eingewickelt; dann
läuft die Referenzlast — `beobachten()` und `last_<bereich>()`, also genau die Codepfade,
deren Laufzeit das Maß belohnt. Eine Beschleunigung, die das Maß sieht, liegt deshalb
zwingend auf einem beobachteten Pfad. Beide Stände laufen durch dieselbe Sonde.

Regel: Jede Abweichung zwischen Vorgeneration und Kandidat muss durch einen Test gedeckt
sein, den die Vorgeneration NICHT besteht, der Kandidat besteht und der die abweichende
Funktion aufruft. Eine Abweichung ohne solchen Test ist eine unbelegte Verhaltensänderung —
der Kandidat wird abgelehnt. Reine Beschleunigung bei identischen Ausgaben bleibt zulässig.

Die Sonde gibt es bisher nur für TypeScript. Für andere Sprachen enthält sich das Organ —
gezählt im Neutralzähler, so dass keine Torzeile auf einem schweigenden Organ ruht.
"""
from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import Callable

KAPPE = 8   # je Funktion die ersten äußeren Aufrufe mit Alias-, Mutations- und Rücksetzmuster
ORGAN = "verhaltensvergleich"


def vergleichen(alt: dict, neu: dict, gedeckt: set[str]) -> dict:
    """Vergleicht zwei Beobachtungsmengen. Rückgabe: Befund mit Tragfähigkeitsurteil.

    `alt`/`neu`: {beobachtungsname: wert}, erzeugt von derselben Sonde an beiden Ständen.
    `gedeckt`: Namen der Beobachtungen, für die ein Test vorliegt, der an der
    Vorgeneration fällt und am Kandidaten besteht.

    Eine Beobachtung, die auf einer Seite fehlt, zählt als Abweichung — fehlende
    Messung ist kein Beleg für Gleichheit.
    """
    namen = sorted(set(alt) | set(neu))
    abweichungen = [n for n in namen if alt.get(n, _FEHLT) != neu.get(n, _FEHLT)]
    ungedeckt = [n for n in abweichungen if n not in gedeckt]
    tragfaehig = not ungedeckt
    if tragfaehig:
        grund = (f"{len(abweichungen)} Abweichung(en), alle durch Tests gedeckt"
                 if abweichungen else "keine Verhaltensabweichung")
    else:
        grund = (f"{len(ungedeckt)} von {len(abweichungen)} Abweichung(en) ungedeckt: "
                 + ", ".join(ungedeckt[:5])
                 + " — Verhalten geändert, ohne dass ein Test die Änderung festhält")
    return {"abweichungen": abweichungen, "ungedeckt": ungedeckt,
            "tragfaehig": tragfaehig, "grund": grund,
            "beobachtungen": len(namen), "gedeckt": sorted(gedeckt)}


class _Fehlt:
    def __repr__(self):
        return "<nicht beobachtet>"

    def __eq__(self, other):
        return False        # fehlend ist nie gleich irgendetwas, auch nicht sich selbst

    __hash__ = object.__hash__


_FEHLT = _Fehlt()


def geaenderte_module(code: dict[str, str]) -> list[str]:
    """Quellmodule des Kandidaten als Pfade unter dist/ ohne Endung (src/zahlen/x.ts → zahlen/x)."""
    return sorted(p[len("src/"):-len(".ts")] for p in code
                  if p.startswith("src/") and p.endswith(".ts") and not p.endswith(".d.ts"))


def funktion_von(beobachtung: str) -> str | None:
    """'zahlen/statistik:quantil#0@mutation' → 'quantil'; Korpuszeilen haben keine Funktion."""
    m = re.match(r"^[^:]+:([A-Za-z_$][\w$]*)#\d+", beobachtung)
    return m.group(1) if m else None


def deckung(abweichungen: list[str], deckende_tests: dict[str, str]) -> dict[str, list[str]]:
    """{beobachtung: [test]} — ein Test deckt eine Abweichung, wenn er an der Vorgeneration fällt,
    am Kandidaten besteht (das stellt der Aufrufer sicher) und die abweichende Funktion aufruft."""
    out: dict[str, list[str]] = {}
    for b in abweichungen:
        f = funktion_von(b)
        if not f:
            continue
        muster = re.compile(r"(?<![\w$])" + re.escape(f) + r"\s*\(")
        treffer = sorted(n for n, c in deckende_tests.items() if muster.search(c or ""))
        if treffer:
            out[b] = treffer
    return out


def _einzeltest(datei: str, code: str, name: str, ts_cache: dict) -> str | None:
    """Code genau eines Tests; None, wenn er sich nicht sicher herauslösen lässt (dann deckt er nichts)."""
    if datei.endswith((".ts", ".mts", ".tsx")):
        if datei not in ts_cache:
            from ..kern import typescript
            try:
                ts_cache[datei] = typescript.testfunktionen(code) or []
            except typescript.TypeScriptFehler:
                ts_cache[datei] = []
        return next((t.get("code") for t in ts_cache[datei] if t.get("name") == name), None)
    try:
        baum = ast.parse(code)
    except SyntaxError:
        return None
    kurz = name.split("[")[0]
    for k in ast.walk(baum):
        if isinstance(k, (ast.FunctionDef, ast.AsyncFunctionDef)) and k.name == kurz:
            return ast.get_source_segment(code, k)
    return None


def deckende_tests(werk: Path, testbestand: dict[str, str], behoben: set[str]) -> dict[str, str]:
    """{test_id: Code des einzelnen Tests} für Tests, die an der Vorgeneration fielen und am Kandidaten bestehen.

    `behoben`: IDs 'datei::name' mit Basisnamen, wie tests_fehlgeschlagen_liste sie führt. Der Code
    kommt aus dem gemessenen Testbestand, sonst aus dem Werk. Lässt sich ein Test nicht sicher
    herauslösen, deckt er nichts — eine Datei, die irgendwo die Funktion ruft, ist kein Beleg.
    """
    werk = Path(werk)
    quellen: dict[str, str] = {}
    for p, c in (testbestand or {}).items():
        if c is not None:
            quellen.setdefault(Path(p).name, c)
    if (werk / "tests").is_dir():
        for f in sorted((werk / "tests").rglob("*")):
            if f.is_file() and f.name not in quellen:
                try:
                    quellen[f.name] = f.read_text()
                except (OSError, UnicodeDecodeError):
                    pass
    out: dict[str, str] = {}
    ts_cache: dict = {}
    for tid in sorted(behoben):
        datei, _, name = tid.partition("::")
        code = quellen.get(Path(datei).name)
        if not code or not name:
            continue
        einzel = _einzeltest(Path(datei).name, code, name, ts_cache)
        if einzel:
            out[tid] = einzel
    return out


def beobachten(werk: Path, dateien: dict[str, str], referenzlast: str, module: list[str],
               bereiche: list[str]) -> dict:
    """Ein Kammerlauf: Stand bauen, Module einwickeln, Referenzlast ausführen."""
    from ..kern import typescript
    try:
        d, _ = typescript._aufruf(Path(werk), "verhalten", dateien=dateien, zeitlimit_s=240,
                                  referenzlast=referenzlast, module=module, bereiche=list(bereiche),
                                  kappe=KAPPE)
    except typescript.TypeScriptFehler as e:
        return {"gueltig": False, "art": "infrastruktur", "grund": str(e)[:800]}
    return d


def pruefen(werk: Path, code: dict[str, str], referenzlast: str | None, bereiche: list[str],
            deckende: dict[str, str] | Callable[[], dict[str, str]]) -> dict:
    """Vorgeneration (Werk wie es ist) gegen Kandidat (Werk + `code`), dieselbe Sonde, dieselbe Last.

    `deckende`: Tests, die an der Vorgeneration fallen und am Kandidaten bestehen — als dict oder als
    Aufruf, der erst ausgewertet wird, wenn es Abweichungen gibt (spart Kammerläufe).
    Rückgabe mit `ausgefuehrt` (beide Stände beobachtet), `geurteilt` (das Organ hat entschieden — auch
    „keine Quelländerung" ist ein sicheres Urteil), `tragfaehig`, `grund` und `grund_art` (für den
    Neutralzähler). Fehlt eine Seite, ist das kein Beleg für Gleichheit: `tragfaehig` ist dann False —
    außer bei einer Sprache ohne Sonde, dort enthält sich das Organ (gezählt).
    """
    from ..kern import sprachprofil
    module = geaenderte_module(code)
    basis = {"module": module, "bereiche": sorted(bereiche), "kappe": KAPPE}
    if not sprachprofil.ist_typescript(Path(werk)):
        return {**basis, "ausgefuehrt": False, "geurteilt": False, "tragfaehig": True,
                "grund_art": "sprache_ohne_sonde",
                "grund": "Verhaltenssonde gibt es bisher nur für TypeScript — Enthaltung, gezählt"}
    if not module:
        return {**basis, "ausgefuehrt": False, "geurteilt": True, "tragfaehig": True,
                "grund_art": "keine_quellaenderung",
                "grund": "Kandidat ändert keine Quellmodule — Verhalten der Quellen unverändert",
                "beobachtungen": 0, "abweichungen": [], "ungedeckt": [], "gedeckt": {}}
    if not referenzlast:
        return {**basis, "ausgefuehrt": False, "geurteilt": False, "tragfaehig": False,
                "grund_art": "ohne_referenzlast",
                "grund": "keine Referenzlast — Verhalten nicht beobachtbar, Gleichheit unbelegt"}
    alt = beobachten(werk, {}, referenzlast, module, bereiche)
    if not alt.get("gueltig"):
        return {**basis, "ausgefuehrt": False, "geurteilt": False, "tragfaehig": False,
                "grund_art": f"sonde_vorgeneration_{alt.get('art', 'unbekannt')}",
                "grund": f"Sonde an der Vorgeneration nicht ausführbar ({alt.get('art')}): {str(alt.get('grund'))[:300]}"}
    neu = beobachten(werk, dict(code), referenzlast, module, bereiche)
    if not neu.get("gueltig"):
        # Die Vorgeneration war eben beobachtbar; scheitert der Kandidat an derselben Sonde, ist das ein
        # Befund über den Kandidaten (Modul lädt nicht, Last bricht ab, Zeitlimit), kein totes Messgerät.
        return {**basis, "ausgefuehrt": False, "geurteilt": False, "tragfaehig": False,
                "grund_art": f"sonde_kandidat_{neu.get('art', 'unbekannt')}",
                "grund": f"Sonde am Kandidaten nicht ausführbar ({neu.get('art')}): {str(neu.get('grund'))[:300]}"}
    a, n = alt["beobachtungen"], neu["beobachtungen"]
    roh = vergleichen(a, n, gedeckt=set())
    decke: dict[str, list[str]] = {}
    tests: dict[str, str] = {}
    if roh["abweichungen"]:
        tests = deckende() if callable(deckende) else dict(deckende or {})
        decke = deckung(roh["abweichungen"], tests)
    r = vergleichen(a, n, gedeckt=set(decke))
    eingewickelt = alt.get("eingewickelt") or {}
    gerufen = set(alt.get("aufgerufen") or {}) | set(neu.get("aufgerufen") or {})
    unbeobachtet = sorted(f"{m}:{f}" for m, fs in eingewickelt.items() for f in (fs or [])
                          if f"{m}:{f}" not in gerufen)
    return {**basis, "ausgefuehrt": True, "geurteilt": True, "tragfaehig": r["tragfaehig"], "grund": r["grund"],
            "grund_art": "geurteilt", "beobachtungen": r["beobachtungen"],
            "anzahl_abweichungen": len(r["abweichungen"]), "abweichungen": r["abweichungen"][:20],
            "ungedeckt": r["ungedeckt"][:20], "gedeckt": decke,
            "werte": {k: [a.get(k, "<nicht beobachtet>"), n.get(k, "<nicht beobachtet>")]
                      for k in r["abweichungen"][:10]},
            "korpus": alt.get("korpus"), "eingewickelt": eingewickelt,
            "nicht_eingewickelt": alt.get("nicht_eingewickelt") or {},
            "unbeobachtet": unbeobachtet, "deckende_tests": sorted(tests)}


def kurz(e: dict) -> dict:
    """Protokollform: ohne Beobachtungswerte außer den ersten Abweichungen."""
    schluessel = ("ausgefuehrt", "geurteilt", "tragfaehig", "grund", "grund_art", "module", "bereiche", "beobachtungen",
                  "anzahl_abweichungen", "abweichungen", "ungedeckt", "gedeckt", "werte", "korpus",
                  "eingewickelt", "unbeobachtet", "deckende_tests")
    return {k: e[k] for k in schluessel if k in e}
