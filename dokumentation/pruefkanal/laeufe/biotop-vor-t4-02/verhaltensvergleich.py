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

Sonden: TypeScript (kern/ts/verhalten.mjs) und — seit der Behebungsrunde 2 vor T4 — Python (kern/py/verhalten.py),
im selben Umfang: einzeln, Folge (#0…#7), Alias, Mutation, Rücksetzung, Randfälle und Formvarianten. Entscheidung
Chat-Claude (23.09.): Grundsatz 11 gilt für jede Sprache; T4 ist Python.

Fassung 8 (Grundsatz 11, Vorbedingungen 2 und 3 für T4):
- Korpus: Zusätzlich zur Referenzlast ruft die Sonde JEDE exportierte Funktion der geänderten Module mit Randfällen
  auf, die aus ihrem Typvertrag (der deklarierten Signatur der Vorgeneration) erzeugt werden: leer, einzeln, doppelt,
  Grenzwerte (0, −1, leere Zeichenkette …); für Objekttypen aus den beobachteten Aufrufen geschrumpft. Befund T3:
  K3106 änderte `tabellenbreiten` für Tabellen aus leeren Zellen, und die Referenzlast rief keine der 7 Funktionen
  des Moduls — das Organ urteilte trotzdem „keine Abweichung“.
- Eine Funktion, die der Vergleich nicht erreicht hat, ist eine Enthaltung, kein bestandenes Urteil: jedes Urteil
  trägt „x von y Funktionen beobachtet“; ohne eine einzige beobachtete Funktion enthält sich das Organ (gezählt).
- Formvarianten (~form#j, Behebungsrunde 2): dieselben Eingaben in anderer Form — Weißraum (Tab, Zeilenumbruch,
  doppelt, CRLF, geschütztes Leerzeichen, am Rand), Groß/Klein, Zahlform im Text, Schlüsselfolge, in Python auch
  Zahltyp und Behälter. Befund: Die Weißraumlücke von K2868 (T3) lag in keinem Randwert.
- Deckung je Abweichung (Grundsatz 11, Entscheidung Chat-Claude): Eine Abweichung ist gedeckt, wenn ein Test, der an
  der Vorgeneration fällt und am Kandidaten besteht, die abweichende Funktion mit DERSELBEN Eingabe ruft (kanonische
  Form) und dasselbe Ergebnis bekommt, das die Sonde am Kandidaten sah. Beweis ist der aufgezeichnete Aufruf am
  Kandidaten, nicht der Quelltext des Tests:
  Bisher deckte jeder Test, der `f(` enthielt, JEDE Abweichung von f (T3/K2868: 3 Befundklassen-Tests deckten 12
  Abweichungen, auch eine konstruierte Weißraum-Abweichung).
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


def geaenderte_module(code: dict[str, str], python: bool = False) -> list[str]:
    """Quellmodule des Kandidaten. TypeScript: Pfade unter dist/ ohne Endung (src/zahlen/x.ts → zahlen/x).
    Python: Importnamen (paket/zahlen/x.py → paket.zahlen.x, paket/zahlen/__init__.py → paket.zahlen)."""
    if python:
        out = set()
        for p in code:
            if not p.endswith(".py") or p.startswith(("tests/", "_messgeraet/")) or "/" not in p:
                continue
            teile = p[:-3].split("/")
            if teile[-1] == "__init__":
                teile = teile[:-1]
            if teile and all(t.isidentifier() for t in teile):
                out.add(".".join(teile))
        return sorted(out)
    return sorted(p[len("src/"):-len(".ts")] for p in code
                  if p.startswith("src/") and p.endswith(".ts") and not p.endswith(".d.ts"))


def funktion_von(beobachtung: str) -> str | None:
    """'zahlen/statistik:quantil#0@mutation' → 'quantil' (auch Randfälle 'quantil~rand#3' und Formvarianten
    'quantil~form#1'); Korpuszeilen haben keine."""
    m = re.match(r"^[^:]+:([A-Za-z_$][\w$]*)(?:~rand|~form)?#\d+", beobachtung)
    return m.group(1) if m else None


def _modul_funktion(beobachtung: str) -> tuple[str, str] | None:
    m = re.match(r"^([^:]+):([A-Za-z_$][\w$]*)(?:~rand|~form)?#\d+", beobachtung)
    return (m.group(1), m.group(2)) if m else None


def _funktionen_in(beob: dict, nur_rand: bool = False) -> set[str]:
    """'modul:funktion' aller Funktionen mit mindestens einer Beobachtung (nur Randfälle: nur_rand)."""
    return {f"{mf[0]}:{mf[1]}" for k in beob if (not nur_rand or "~rand#" in k or "~form#" in k) and (mf := _modul_funktion(k))}


def deckung(abweichungen: list[str], aufrufe: list[dict], argumente: dict[str, str],
            neu: dict[str, str]) -> dict[str, list[str]]:
    """{abweichung: [test]} — Deckung JE ABWEICHUNG (Grundsatz 11, Entscheidung Chat-Claude 23.09.2026).

    Ein Test deckt eine Abweichung, wenn er an der Vorgeneration fällt und am Kandidaten besteht (das stellt der
    Aufrufer sicher: `aufrufe` stammen nur von solchen Tests, aufgezeichnet AM KANDIDATEN) und die abweichende Funktion
    mit DERSELBEN EINGABE gerufen und DASSELBE ERGEBNIS bekommen hat, das die Sonde am Kandidaten für diese Beobachtung
    sah — `argumente[k]` ist die Eingabe unmittelbar vor dem Aufruf des Musters (nach Mutation bzw. Rücksetzung),
    `neu[k]` das Ergebnis (kanonisch, auch Fehlerklasse). Damit hält der Test genau das neue Verhalten fest, das die
    Abweichung zeigt. Ein Zwischenspeicher, der nach einer Mutation das alte Ergebnis liefert, ist so nicht deckbar: ein
    frischer Aufruf mit der mutierten Eingabe bekommt am Kandidaten das richtige Ergebnis, nicht das veraltete.
    Bisher (Deckung je Funktion) deckte jeder Test, der `f(` enthielt, JEDE Abweichung von f."""
    je_test: dict[str, dict[str, set[tuple[str, str]]]] = {}
    for c in aufrufe or []:
        je_test.setdefault(c.get("test", ""), {}).setdefault(c.get("f", ""), set()).add((c.get("args"), c.get("erg")))
    out: dict[str, list[str]] = {}
    for k in abweichungen:
        mf = _modul_funktion(k)
        x, y = argumente.get(k), neu.get(k, _FEHLT)
        if not mf or x is None or y is _FEHLT:
            continue
        f = f"{mf[0]}:{mf[1]}"
        treffer = sorted(t for t, fs in je_test.items() if (x, y) in fs.get(f, set()))
        if treffer:
            out[k] = treffer
    return out


def _testdatei_pfade(werk: Path, testbestand: dict[str, str], behoben: set[str]) -> list[str]:
    """Pfade (relativ zum Werk) der Dateien, in denen die Tests aus `behoben` ('datei::name', Basisname) stehen."""
    werk = Path(werk)
    bekannt = {Path(p).name: p for p in (testbestand or {}) if p.startswith("tests/")}
    if (werk / "tests").is_dir():
        for f in sorted((werk / "tests").rglob("*")):
            if f.is_file():
                bekannt.setdefault(f.name, str(f.relative_to(werk)))
    return sorted({bekannt[d] for d in {t.partition("::")[0] for t in behoben} if d in bekannt})


def deckende_aufrufe(werk: Path, code: dict[str, str], testbestand: dict[str, str], behoben: set[str],
                     module: list[str] | None = None) -> dict:
    """Die Tests aus `behoben` (fallen an der Vorgeneration, bestehen am Kandidaten) AM KANDIDATEN mit Aufzeichner
    ausführen. Rückgabe {"tests", "aufrufe"}; ein Aufzeichnerausfall ist ein Messgerätausfall (SondeAusgefallen)."""
    from ..kern import sprachprofil
    behoben = set(behoben or ())
    if not behoben:
        return {"tests": [], "aufrufe": []}
    dateien = {**{p: c for p, c in (code or {}).items() if c is not None}, **{p: c for p, c in (testbestand or {}).items() if c is not None}}
    if module is None:
        module = geaenderte_module(code or {}, python=not sprachprofil.ist_typescript(Path(werk)))
    pfade = _testdatei_pfade(werk, testbestand, behoben)
    if not pfade:
        return {"tests": sorted(behoben), "aufrufe": [], "hinweis": "Testdateien der deckenden Tests nicht gefunden"}
    if sprachprofil.ist_typescript(Path(werk)):
        from ..kern import typescript
        try:
            d, _ = typescript._aufruf(Path(werk), "deckung", dateien=dateien, zeitlimit_s=240, module=module,
                                      testdateien=pfade)
        except typescript.TypeScriptFehler as e:
            raise SondeAusgefallen(f"Deckungsaufzeichner ausgefallen: {str(e)[:300]}") from e
    else:
        d = _python_sonde(Path(werk), dateien, {"modus": "deckung", "module": module, "testdateien": pfade}, None)
    if not d.get("gueltig"):
        raise SondeAusgefallen(f"Deckungsaufzeichner ausgefallen: {str(d.get('grund') or d.get('rc'))[:300]}")
    # Jeder deckende Test muss auch im Aufzeichnerlauf bestehen — sonst hat das Instrument das Verhalten verändert
    # (Messgerätausfall, kein Urteil über den Kandidaten).
    zustand = d.get("zustand") or {}
    anders = sorted(t for t in behoben if zustand.get(t) != "pass")
    if anders:
        raise SondeAusgefallen(f"Deckungsaufzeichner: {len(anders)} von {len(behoben)} deckenden Tests bestehen im "
                               f"Aufzeichnerlauf nicht ({anders[:3]} → {[zustand.get(t) for t in anders[:3]]})")
    aufrufe = [c for c in d.get("aufrufe") or [] if c.get("test") in behoben]
    return {"tests": sorted(behoben), "aufrufe": aufrufe, "gelaufen": sum(1 for t in behoben if zustand.get(t) == "pass")}


def _python_sonde(werk: Path, dateien: dict[str, str], anfrage: dict, referenzlast: str | None) -> dict:
    """Ein Kammerlauf der Python-Sonde (kern/py/verhalten.py). Infrastruktur (Zeitlimit, Kammer, fehlende Ausgabe)
    → art 'infrastruktur'; die Sonde meldet Inhaltsbefunde (Modul lädt nicht) selbst."""
    import json as _json
    from . import kammer
    sonde = (Path(__file__).resolve().parent.parent / "kern" / "py" / "verhalten.py").read_text()
    extra = {**(dateien or {}), "_messgeraet/verhalten.py": sonde,
             "_messgeraet/anfrage.json": _json.dumps(anfrage, ensure_ascii=False, default=str)}
    if referenzlast is not None:
        extra["_messgeraet/referenzlast.py"] = referenzlast
    e = kammer.ausfuehren(Path(werk), ["python", "_messgeraet/verhalten.py", "_messgeraet/anfrage.json"],
                          zeitlimit_s=240, dateien=extra)
    m = re.search(r"@@VV@@(.*)@@ENDE@@", e.stdout or "", re.S)
    if e.zeitlimit or not m:
        return {"gueltig": False, "art": "infrastruktur",
                "grund": ("Zeitlimit" if e.zeitlimit else f"Python-Sonde ohne Ergebnis (rc={e.rc})") + ": "
                         + (e.stderr or e.stdout or "")[-600:]}
    try:
        return _json.loads(m.group(1))
    except ValueError:
        return {"gueltig": False, "art": "infrastruktur", "grund": "Python-Sonde: Ergebnis nicht lesbar"}


def beobachten(werk: Path, dateien: dict[str, str], referenzlast: str, module: list[str],
               bereiche: list[str], signaturen: dict | None = None, beispiele: dict | None = None) -> dict:
    """Ein Kammerlauf: Stand bauen, Module einwickeln, Referenzlast und Randfall-Korpus ausführen.
    `signaturen` (von der Vorgeneration): welche Funktionen mit welchen Parametertypen Randfälle bekommen —
    beide Seiten erhalten dieselben Aufrufe. Ohne Angabe liest die Sonde sie aus dem Quelltext dieses Stands."""
    from ..kern import sprachprofil, typescript
    if not sprachprofil.ist_typescript(Path(werk)):
        return _python_sonde(Path(werk), dateien, {"modus": "beobachten", "module": module, "bereiche": list(bereiche),
                                                   "kappe": KAPPE, "signaturen": signaturen, "beispiele": beispiele},
                             referenzlast)
    try:
        d, _ = typescript._aufruf(Path(werk), "verhalten", dateien=dateien, zeitlimit_s=240,
                                  referenzlast=referenzlast, module=module, bereiche=list(bereiche),
                                  kappe=KAPPE, signaturen=signaturen, beispiele=beispiele)
    except typescript.TypeScriptFehler as e:
        return {"gueltig": False, "art": "infrastruktur", "grund": str(e)[:800]}
    return d


def pruefen(werk: Path, code: dict[str, str], referenzlast: str | None, bereiche: list[str],
            deckende: dict | Callable[[list[str]], dict]) -> dict:
    """Vorgeneration (Werk wie es ist) gegen Kandidat (Werk + `code`), dieselbe Sonde, dieselbe Last.

    `deckende`: {"tests": [...], "aufrufe": [...]} — die Tests, die an der Vorgeneration fallen und am Kandidaten
    bestehen, und ihre am Kandidaten aufgezeichneten Aufrufe (deckende_aufrufe) — oder ein Aufruf (Abweichungen →
    dieses dict), der erst ausgewertet wird, wenn es Abweichungen gibt (spart Kammerläufe).
    Rückgabe mit `ausgefuehrt` (beide Stände beobachtet), `geurteilt` (das Organ hat entschieden — auch
    „keine Quelländerung" ist ein sicheres Urteil), `tragfaehig`, `grund` und `grund_art` (für den
    Neutralzähler). Fehlt eine Seite, ist das kein Beleg für Gleichheit: `tragfaehig` ist dann False —
    außer bei einer Sprache ohne Sonde, dort enthält sich das Organ (gezählt).
    """
    from ..kern import sprachprofil
    python = not sprachprofil.ist_typescript(Path(werk))
    module = geaenderte_module(code, python=python)
    basis = {"module": module, "bereiche": sorted(bereiche), "kappe": KAPPE, "sprache": "python" if python else "typescript"}
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
    tests: list[str] = []
    deckung_zaehlung = {"tests": 0, "aufrufe": 0}
    if roh["abweichungen"]:
        d = deckende(roh["abweichungen"]) if callable(deckende) else dict(deckende or {})
        tests = sorted(d.get("tests") or [])
        deckung_zaehlung = {"tests": len(tests), "aufrufe": len(d.get("aufrufe") or [])}
        decke = deckung(roh["abweichungen"], d.get("aufrufe") or [], neu.get("argumente") or {}, n)
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
             "entfernte_funktionen": entfernt, "randfaelle": len([k for k in n if "~rand#" in k and "@" not in k]),
             "formvarianten": len([k for k in n if "~form#" in k and "@" not in k])}
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
            "eingaben": {k: (neu.get("argumente") or {}).get(k) for k in r["ungedeckt"][:10]},
            "korpus": alt.get("korpus"), "eingewickelt": eingewickelt,
            "nicht_eingewickelt": alt.get("nicht_eingewickelt") or {},
            "unbeobachtet": unbeobachtet, "deckende_tests": tests, "deckung_zaehlung": deckung_zaehlung}


def kurz(e: dict) -> dict:
    """Protokollform: ohne Beobachtungswerte außer den ersten Abweichungen."""
    schluessel = ("ausgefuehrt", "geurteilt", "tragfaehig", "grund", "grund_art", "module", "bereiche", "beobachtungen",
                  "anzahl_abweichungen", "abweichungen", "ungedeckt", "gedeckt", "werte", "korpus",
                  "eingewickelt", "unbeobachtet", "deckende_tests", "beobachtete_funktionen", "unbeobachtete_module",
                  "entfernte_funktionen", "randfaelle", "formvarianten", "sprache", "eingaben", "deckung_zaehlung")
    return {k: e[k] for k in schluessel if k in e}
