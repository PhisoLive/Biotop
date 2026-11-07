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

Fassung 8 (Grundsatz 11, Vorbedingungen 2 und 3 für T4):
- Korpus: Zusätzlich zur Referenzlast ruft die Sonde JEDE exportierte Funktion der geänderten Module mit Randfällen
  auf, die aus ihrem Typvertrag (der deklarierten Signatur der Vorgeneration) erzeugt werden: leer, einzeln, doppelt,
  Grenzwerte (0, −1, leere Zeichenkette …); für Objekttypen aus den beobachteten Aufrufen geschrumpft. Befund T3:
  K3106 änderte `tabellenbreiten` für Tabellen aus leeren Zellen, und die Referenzlast rief keine der 7 Funktionen
  des Moduls — das Organ urteilte trotzdem „keine Abweichung“.
- Eine Funktion, die der Vergleich nicht erreicht hat, ist eine Enthaltung, kein bestandenes Urteil: jedes Urteil
  trägt „x von y Funktionen beobachtet“; ohne eine einzige beobachtete Funktion enthält sich das Organ (gezählt).
- Ein Sondenausfall (Kammerabbruch, Zeitlimit, beschädigter Transport — `art` 'infrastruktur'; fehlende Referenzlast)
  ist ein Messgerätausfall: `SondeAusgefallen` wird geworfen, der Aufrufer stellt den Kandidaten zurück. Keine
  Ablehnung, kein Gedächtniseintrag. Scheitert die Sonde mit Inhalt an der VORGENERATION, betrifft das den Kandidaten
  nicht: Enthaltung. Nur ein Inhaltsbefund am KANDIDATEN (Modul lädt nicht, Last bricht ab) bleibt ein Urteil über ihn.
"""
from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import Callable

KAPPE = 8   # je Funktion die ersten äußeren Aufrufe mit Alias-, Mutations- und Rücksetzmuster
ORGAN = "verhaltensvergleich"


class SondeAusgefallen(RuntimeError):
    """Die Sonde konnte nicht messen — ein Messgerätausfall, keine Aussage über den Kandidaten."""


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
    """'zahlen/statistik:quantil#0@mutation' → 'quantil' (auch Randfälle 'quantil~rand#3'); Korpuszeilen haben keine."""
    m = re.match(r"^[^:]+:([A-Za-z_$][\w$]*)(?:~rand)?#\d+", beobachtung)
    return m.group(1) if m else None


def _modul_funktion(beobachtung: str) -> tuple[str, str] | None:
    m = re.match(r"^([^:]+):([A-Za-z_$][\w$]*)(?:~rand)?#\d+", beobachtung)
    return (m.group(1), m.group(2)) if m else None


def _funktionen_in(beob: dict, nur_rand: bool = False) -> set[str]:
    """'modul:funktion' aller Funktionen mit mindestens einer Beobachtung (nur Randfälle: nur_rand)."""
    return {f"{mf[0]}:{mf[1]}" for k in beob if (not nur_rand or "~rand#" in k) and (mf := _modul_funktion(k))}


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
               bereiche: list[str], signaturen: dict | None = None, beispiele: dict | None = None) -> dict:
    """Ein Kammerlauf: Stand bauen, Module einwickeln, Referenzlast und Randfall-Korpus ausführen.
    `signaturen` (von der Vorgeneration): welche Funktionen mit welchen Parametertypen Randfälle bekommen —
    beide Seiten erhalten dieselben Aufrufe. Ohne Angabe liest die Sonde sie aus dem Quelltext dieses Stands."""
    from ..kern import typescript
    try:
        d, _ = typescript._aufruf(Path(werk), "verhalten", dateien=dateien, zeitlimit_s=240,
                                  referenzlast=referenzlast, module=module, bereiche=list(bereiche),
                                  kappe=KAPPE, signaturen=signaturen, beispiele=beispiele)
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
        # Konfiguration, kein Urteil über den Kandidaten (Review 03 Nr. 3): ohne Referenzlast misst die Sonde nicht.
        raise SondeAusgefallen("keine Referenzlast — die Verhaltenssonde kann nicht messen")
    alt = beobachten(werk, {}, referenzlast, module, bereiche)
    if not alt.get("gueltig"):
        if alt.get("art") != "inhalt":
            raise SondeAusgefallen(f"Sonde an der Vorgeneration ausgefallen ({alt.get('art')}): {str(alt.get('grund'))[:300]}")
        return {**basis, "ausgefuehrt": False, "geurteilt": False, "tragfaehig": True,
                "grund_art": "sonde_vorgeneration_inhalt",
                "grund": f"Vorgeneration nicht beobachtbar — Enthaltung, betrifft den Kandidaten nicht: {str(alt.get('grund'))[:300]}"}
    neu = beobachten(werk, dict(code), referenzlast, module, bereiche, signaturen=alt.get("signaturen"),
                     beispiele=alt.get("beispiele"))
    if not neu.get("gueltig"):
        if neu.get("art") != "inhalt":
            raise SondeAusgefallen(f"Sonde am Kandidaten ausgefallen ({neu.get('art')}): {str(neu.get('grund'))[:300]}")
        # Die Vorgeneration war eben beobachtbar; scheitert der Kandidat mit Inhalt an derselben Sonde (Modul lädt
        # nicht, Last bricht ab), ist das ein Befund über den Kandidaten.
        return {**basis, "ausgefuehrt": False, "geurteilt": False, "tragfaehig": False,
                "grund_art": "sonde_kandidat_inhalt",
                "grund": f"Sonde am Kandidaten nicht ausführbar ({neu.get('art')}): {str(neu.get('grund'))[:300]}"}
    a, n = dict(alt["beobachtungen"]), dict(neu["beobachtungen"])
    beobachtet = _funktionen_in(a) | _funktionen_in(n)
    # Randfälle einer Funktion, die der Kandidat nicht mehr exportiert (entfernt/umbenannt), sind kein Verhalten
    # des verbliebenen Codes: sie werden getrennt ausgewiesen; ob die Entfernung zulässig ist, entscheiden Tests,
    # Verträge und das Maß (tote Funktion), nicht diese Sonde. „Entfernt“ heißt: an der Vorgeneration gibt es
    # Randfall-Beobachtungen, am Kandidaten keine — auf BEIDEN Seiten aus den Beobachtungen bestimmt (Review vor T4
    # Nr. 1: bisher aus `eingewickelt`, das nur `export function` erfasst; ein `export const f = () =>` galt dann am
    # Kandidaten als entfernt und seine Randfälle standen einseitig als ungedeckte Abweichung).
    entfernt = sorted(_funktionen_in(a, nur_rand=True) - _funktionen_in(n, nur_rand=True))
    for k in [k for k in a if "~rand#" in k and (mf := _modul_funktion(k)) and f"{mf[0]}:{mf[1]}" in entfernt]:
        a.pop(k)
    roh = vergleichen(a, n, gedeckt=set())
    decke: dict[str, list[str]] = {}
    tests: dict[str, str] = {}
    if roh["abweichungen"]:
        tests = deckende() if callable(deckende) else dict(deckende or {})
        decke = deckung(roh["abweichungen"], tests)
    r = vergleichen(a, n, gedeckt=set(decke))
    eingewickelt = alt.get("eingewickelt") or {}
    gerufen = (beobachtet | set(alt.get("aufgerufen") or {}) | set(neu.get("aufgerufen") or {})
               | set(alt.get("aufgerufen_rand") or {}) | set(neu.get("aufgerufen_rand") or {}))
    # y = alle exportierten Funktionen der geänderten Module: eingewickelte UND aus den Signaturen gelesene (auch
    # `export const f = () =>`), ohne die vom Kandidaten entfernten.
    alle = sorted(({f"{m}:{f}" for m, fs in eingewickelt.items() for f in (fs or [])}
                   | {f"{m}:{f}" for m, fs in (alt.get("signaturen") or {}).items() for f in (fs or {})})
                  - set(entfernt))
    unbeobachtet = sorted(x for x in alle if x not in gerufen)
    x_von_y = f"{len(alle) - len(unbeobachtet)} von {len(alle)}"
    unbeobachtete_module = sorted(m for m, fs in eingewickelt.items() if fs and not any(f"{m}:{f}" in gerufen for f in fs))
    extra = {"beobachtete_funktionen": x_von_y, "unbeobachtet": unbeobachtet, "unbeobachtete_module": unbeobachtete_module,
             "entfernte_funktionen": entfernt, "randfaelle": len([k for k in n if "~rand#" in k and "@" not in k])}
    if r["tragfaehig"] and len(alle) - len(unbeobachtet) == 0:
        # Keine Abweichung, aber auch keine einzige Funktion erreicht: das ist kein bestandenes Urteil.
        return {**basis, **extra, "ausgefuehrt": True, "geurteilt": False, "tragfaehig": True, "grund_art": "unbeobachtet",
                "grund": f"Enthaltung: 0 von {len(alle)} Funktionen der geänderten Module beobachtet",
                "beobachtungen": r["beobachtungen"], "anzahl_abweichungen": 0, "abweichungen": [], "ungedeckt": [],
                "gedeckt": {}, "korpus": alt.get("korpus"), "eingewickelt": eingewickelt}
    return {**basis, **extra, "ausgefuehrt": True, "geurteilt": True, "tragfaehig": r["tragfaehig"],
            "grund": r["grund"] + f" ({x_von_y} Funktionen beobachtet)",
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
                  "eingewickelt", "unbeobachtet", "deckende_tests", "beobachtete_funktionen", "unbeobachtete_module",
                  "entfernte_funktionen", "randfaelle")
    return {k: e[k] for k in schluessel if k in e}
