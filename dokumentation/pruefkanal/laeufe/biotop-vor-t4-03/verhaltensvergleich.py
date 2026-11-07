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

Wie die Sonde beobachtet (kern/ts/verhalten.mjs + verhalten-runner.mjs, kern/py/verhalten.py): Die öffentlichen
Funktionen (Python auch Methoden und Eigenschaften von Klassen) der vom Kandidaten geänderten Module werden
eingewickelt; dann läuft die Referenzlast — `beobachten()` und `last_<bereich>()`, also genau die Codepfade, deren
Laufzeit das Maß belohnt — und der Korpus aus Randfällen und Formvarianten. Beide Stände laufen durch dieselbe Sonde
mit denselben Eingaben (Signaturen, Beispiele und Instanzrezepte der Vorgeneration).

Regel (Grundsatz 11): Jede Abweichung zwischen Vorgeneration und Kandidat muss durch einen Test gedeckt sein, den die
Vorgeneration NICHT besteht und der Kandidat besteht. Eine Abweichung ohne solchen Test ist eine unbelegte
Verhaltensänderung — der Kandidat wird abgelehnt. Reine Beschleunigung bei identischen Ausgaben bleibt zulässig.

Fassung 8 (Grundsatz 11, Vorbedingungen 2 und 3 für T4):
- Korpus: Zusätzlich zur Referenzlast ruft die Sonde JEDE öffentliche Funktion der geänderten Module mit Randfällen
  aus ihrem Typvertrag (der deklarierten Signatur der Vorgeneration) auf. Befund T3: K3106 änderte `tabellenbreiten`
  für Tabellen aus leeren Zellen, und die Referenzlast rief keine der 7 Funktionen des Moduls.
- Eine Funktion, die der Vergleich nicht erreicht hat, ist eine Enthaltung, kein bestandenes Urteil: jedes Urteil
  trägt „x von y Funktionen beobachtet“; ohne eine einzige beobachtete Funktion enthält sich das Organ (gezählt).
- Ein Sondenausfall (Kammerabbruch, beschädigter Transport — `art` 'infrastruktur'; fehlende Referenzlast) ist ein
  Messgerätausfall: `SondeAusgefallen`, der Aufrufer stellt den Kandidaten zurück. Scheitert die Sonde mit Inhalt an
  der VORGENERATION, betrifft das den Kandidaten nicht: Enthaltung.

Behebungsrunde 2 vor T4: Formvarianten (~form#j: Weißraum, Groß/Klein, Zahlform, Schlüsselfolge, in Python Zahltyp
und Behälter) — die Weißraumlücke von K2868 (T3) lag in keinem Randwert; Python-Sonde im Umfang der TS-Sonde.

Behebungsrunde 3 vor T4 (Entscheidungen Chat-Claude 24.09.2026, Review 02, SPEZIFIKATIONEN-NAECHSTER-AUFTRAG S-1…S-13):
- Deckung je MUSTER (Entscheidung 1): Jede Beobachtung trägt das Muster ihrer Eingabe (`muster` der Sonde: die
  Merkmalsklassen des variierten Werts — leer, null, negativ, Weißraum, Randweißraum, groß, klein, Zahlform, lang,
  Nicht-ASCII, Zahltyp, Behälter, Schlüsselfolge — bzw. die Art der Formvariante; [] = gewöhnliche Eingabe). Ein Test
  deckt eine Abweichung, wenn er (a) an der Vorgeneration fällt und am Kandidaten besteht, (b) am Kandidaten die
  abweichende Funktion mit einer Eingabe ruft, deren Merkmalsklassen das Muster der Abweichung enthalten (die Argumente
  über die Signatur vereinheitlicht, Standardwerte eingesetzt), und (c) FÄLLT, wenn im Aufzeichnerlauf das Ergebnis
  dieser Funktion verfälscht wird (bei Zustandsbeobachtungen: der Zustand der Argumente) — so zählt nur ein Test, der das
  Verhalten festhält, nicht einer, der die Funktion nebenbei ruft (Review 02 Nr. 8). Je Eingabe war zu fein (ein
  richtiger Test deckte 2 von 28), je Funktion zu grob (dahinter lag die Weißraumlücke).
  Nicht deckbar ist eine Abweichung, deren Ergebnis am Kandidaten an Referenz oder verborgenem Zustand hängt: die Sonde
  ruft jedes Muster zusätzlich mit einer tiefen Kopie derselben Eingabe (`kopien`); weicht das nur am Kandidaten ab, ist
  es ein veralteter Zwischenspeicher, den kein Test „festhalten“ kann.
- Die Vorgeneration wird ZWEIMAL beobachtet (gleicher Korpus); Beobachtungen, die dabei schwanken, sind Enthaltungen
  (`instabil`, gezählt) — Befund Review 02 Nr. 4: Mengenreihenfolge ergab 22 Fehlalarme. Die Python-Sonde läuft
  zusätzlich mit fester Hash-Saat.
- „x von y“: beobachtet ist eine Funktion nur mit mindestens einem fehlerfreien, vergleichbaren Aufruf auf BEIDEN Seiten
  (`inhalt`, Review 02 Nr. 3). y umfasst auch Methoden und Eigenschaften von Klassen (Entscheidung 3) und in Python die
  nicht einwickelbaren öffentlichen Mitglieder; jede nicht beobachtete Funktion steht mit Grund in `enthaltungen`.
- Python-Module auf Wurzelebene gehören dazu (Review 02 Nr. 12); Werkzeugdateien (setup.py, conftest.py …) werden
  gezählt ausgewiesen.
- Zeitlimit der Sonde am Kandidaten bei gültiger Vorgeneration: einmal wiederholt; ein zweites Zeitlimit ist ein
  Inhaltsbefund über den Kandidaten (Review 02 Nr. 21), kein Messgerätausfall.
- Aufzeichner blind (Review 02 Nr. 22): ein deckender Test, der ein geändertes Modul lädt und im Aufzeichnerlauf keinen
  einzigen Aufruf einer eingewickelten Funktion zeigt, macht bei ungedeckten Abweichungen das Urteil unmöglich — das
  ist ein Messgerätausfall (zurückgestellt, gezählt), keine Ablehnung und keine Annahme.
- `korpus_erweitert` / `deckungsregel` ('muster' | 'funktion') schalten für die getrennte Messung von K2868 (S-7) auf
  den Korpus bzw. die Deckungsregel von 330b4ec zurück; der Lauf nutzt immer die Vorgabe.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Callable

KAPPE = 8   # je Funktion die ersten äußeren Aufrufe mit Alias-, Mutations- und Rücksetzmuster
ORGAN = "verhaltensvergleich"
# Wurzeldateien eines Python-Werks, die kein Werkmodul sind: Laden hätte Nebenwirkungen (setup) oder ist Testgerüst.
WERKZEUGDATEIEN = frozenset({"setup", "conftest", "noxfile", "fabfile", "manage", "tasks"})


class SondeAusgefallen(RuntimeError):
    """Die Sonde konnte nicht messen — ein Messgerätausfall, keine Aussage über den Kandidaten."""


def vergleichen(alt: dict, neu: dict, gedeckt: set[str]) -> dict:
    """Vergleicht zwei Beobachtungsmengen. Rückgabe: Befund mit Tragfähigkeitsurteil.

    `alt`/`neu`: {beobachtungsname: wert}, erzeugt von derselben Sonde an beiden Ständen.
    `gedeckt`: Namen der Beobachtungen, für die ein deckender Test vorliegt.
    Eine Beobachtung, die auf einer Seite fehlt, zählt als Abweichung — fehlende Messung ist kein Beleg für Gleichheit.
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
    Python: Importnamen (paket/zahlen/x.py → paket.zahlen.x, paket/zahlen/__init__.py → paket.zahlen), auch auf
    Wurzelebene (app.py → app; Review 02 Nr. 12) — ohne Werkzeugdateien (werkzeugdateien())."""
    if python:
        out = set()
        for p in code:
            if not p.endswith(".py") or p.startswith(("tests/", "_messgeraet/")):
                continue
            teile = p[:-3].split("/")
            if teile[-1] == "__init__":
                teile = teile[:-1]
            if len(teile) == 1 and teile[0] in WERKZEUGDATEIEN:
                continue
            if teile and all(t.isidentifier() for t in teile):
                out.add(".".join(teile))
        return sorted(out)
    return sorted(p[len("src/"):-len(".ts")] for p in code
                  if p.startswith("src/") and p.endswith(".ts") and not p.endswith(".d.ts"))


def werkzeugdateien(code: dict[str, str]) -> list[str]:
    """Geänderte Python-Werkzeugdateien auf Wurzelebene (setup.py, conftest.py …) — nicht beobachtbar, gezählt."""
    return sorted(p for p in code if "/" not in p and p.endswith(".py") and p[:-3] in WERKZEUGDATEIEN)


# ---------------------------------------------------------------- Beobachtungsschlüssel
# modul:funktion[#i | ~rand#i | ~form#i | ~instanz#i][@alias|@mutation|@nach_ruecksetzung][>args]
# Methoden heißen 'Klasse.methode'; der Zustand einer frischen Instanz 'Klasse.__init__~instanz#0'.
_SCHLUESSEL = re.compile(r"^(?P<modul>[^:]+):(?P<f>[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)?)"
                         r"(?:~(?P<korpus>rand|form|instanz))?#(?P<i>\d+)(?P<muster>@\w+)?(?P<zustand>>args)?$")


def zerlegen(beobachtung: str) -> dict | None:
    m = _SCHLUESSEL.match(beobachtung)
    return m.groupdict() if m else None


def funktion_von(beobachtung: str) -> str | None:
    """'zahlen/statistik:quantil#0@mutation' → 'quantil' (auch '~rand#3', '~form#1', Methoden 'Konto.buchen');
    Korpuszeilen haben keine."""
    z = zerlegen(beobachtung)
    return z["f"] if z else None


def _modul_funktion(beobachtung: str) -> tuple[str, str] | None:
    z = zerlegen(beobachtung)
    return (z["modul"], z["f"]) if z else None


def _aufruf(beobachtung: str) -> str:
    """Schlüssel des Aufrufs, zu dem eine Beobachtung gehört (ohne @muster und >args) — unter ihm führt die Sonde
    Muster und Kopienprobe."""
    return re.sub(r"(@\w+)?(>args)?$", "", beobachtung)


def _funktionen_in(beob: dict, nur_rand: bool = False) -> set[str]:
    """'modul:funktion' aller Funktionen mit mindestens einer Beobachtung (nur Korpus: nur_rand)."""
    out = set()
    for k in beob:
        z = zerlegen(k)
        if z and z["korpus"] != "instanz" and (not nur_rand or z["korpus"] in ("rand", "form")):
            out.add(f"{z['modul']}:{z['f']}")
    return out


# ---------------------------------------------------------------- Deckung je Muster
def _verfaelschungsart(beobachtung: str) -> str:
    z = zerlegen(beobachtung) or {}
    return "zustand" if z.get("zustand") or z.get("korpus") == "instanz" else "rueckgabe"


def _deckungsfunktion(beobachtung: str) -> str | None:
    z = zerlegen(beobachtung)
    return f"{z['modul']}:{z['f']}" if z else None


def zustandsabhaengig(abweichungen: list[str], kopien_alt: dict, kopien_neu: dict) -> set[str]:
    """Abweichungen, deren Ergebnis am KANDIDATEN an Referenz oder verborgenem Zustand hängt (die Kopie derselben
    Eingabe ergibt etwas anderes), an der Vorgeneration aber nicht — ein veralteter Zwischenspeicher: nicht deckbar."""
    out = set()
    for k in abweichungen:
        a = re.sub(r">args$", "", k)          # die Kopienprobe gehört zum Aufruf samt Muster (@alias, @mutation …)
        wert = (kopien_neu or {}).get(a)
        if wert is not None and wert != "__nicht_kopierbar" and a not in (kopien_alt or {}):
            out.add(k)
    return out


def _je_test(aufrufe: list[dict]) -> dict[str, dict[str, list[set[str]]]]:
    je: dict[str, dict[str, list[set[str]]]] = {}
    for c in aufrufe or []:
        je.setdefault(c.get("test", ""), {}).setdefault(c.get("f", ""), []).append(set(c.get("klassen") or []))
    return je


def _merkmal_treffer(p: set[str], je: dict, f: str, zugelassen: set[str] | None = None) -> list[str] | None:
    """Deckung je Muster, je MERKMAL gelesen (eigene Festlegung vor der Messung, Behebungsrunde 3): das Muster p einer
    Abweichung von f ist gedeckt, wenn JEDES seiner Merkmale (weissraum, gross, lang …) von mindestens einem Test
    getroffen wird, der f mit einer Eingabe dieses Merkmals ruft — „ein Test je Muster“. Alle Merkmale in einem
    einzigen Aufruf zu verlangen, käme der zu feinen Regel „je Eingabe“ nahe. Das gewöhnliche Muster (leer) deckt jeder
    Test, der f ruft. `zugelassen`: nur diese Tests (die f festhalten). Rückgabe: deckende Tests oder None."""
    tests = [t for t, fs in je.items() if fs.get(f) and (zugelassen is None or t in zugelassen)]
    if not tests:
        return None
    if not p:
        return sorted(tests)
    treffer: set[str] = set()
    for c in sorted(p):
        tc = {t for t in tests if any(c in kl for kl in je[t][f])}
        if not tc:
            return None
        treffer |= tc
    return sorted(treffer)


def verfaelschungsbedarf(abweichungen: list[str], aufrufe: list[dict], muster: dict,
                         nicht_deckbar: set[str]) -> set[tuple[str, str]]:
    """(Funktion, Art) je Abweichung, für die ein Kandidatentest mit passendem Muster existiert — nur für diese muss
    der Aufzeichner die Verfälschungsprobe fahren."""
    je = _je_test(aufrufe)
    out = set()
    for k in abweichungen:
        f = _deckungsfunktion(k)
        if not f or k in nicht_deckbar or _aufruf(k) not in (muster or {}):
            continue
        if _merkmal_treffer(set(muster[_aufruf(k)] or []), je, f) is not None:
            out.add((f, _verfaelschungsart(k)))
    return out


def deckung(abweichungen: list[str], aufrufe: list[dict], muster: dict | None = None,
            nicht_deckbar: set[str] | None = None, haelt: dict | None = None,
            regel: str = "muster") -> dict[str, list[str]]:
    """{abweichung: [test]} — Deckung JE MUSTER (Grundsatz 11, Entscheidung Chat-Claude 24.09.2026).

    `aufrufe`: [{test, f, klassen}] der Tests, die an der Vorgeneration fallen und am Kandidaten bestehen, am KANDIDATEN
    aufgezeichnet (klassen = Merkmalsklassen der vereinheitlichten Argumente). `muster`: {aufruf: [klassen]} der Sonde.
    `haelt`: {(funktion, art): {tests}} — Tests, die fallen, wenn der Aufzeichner das Ergebnis ('rueckgabe') bzw. den
    Argumentzustand ('zustand') dieser Funktion verfälscht. `nicht_deckbar`: zustandsabhängige Abweichungen.
    Die Abweichung k von f ist gedeckt, wenn jedes Merkmal von Muster(k) von einem Test getroffen wird, der f mit einer
    Eingabe dieses Merkmals ruft und f festhält (_merkmal_treffer); das gewöhnliche Muster deckt jeder festhaltende
    Test, der f ruft.
    `regel='funktion'`: die Regel von 330b4ec (je Funktion: ein deckender Test, der f ruft, deckt jede Abweichung von
    f) — nur für die getrennte Messung (S-7)."""
    je = _je_test(aufrufe)
    nicht_deckbar = nicht_deckbar or set()
    haelt = haelt or {}
    out: dict[str, list[str]] = {}
    for k in abweichungen:
        f = _deckungsfunktion(k)
        if not f:
            continue
        if regel == "funktion":
            treffer = sorted(t for t, fs in je.items() if f in fs)
        else:
            if k in nicht_deckbar or _aufruf(k) not in (muster or {}):
                continue
            festhaltend = set(haelt.get((f, _verfaelschungsart(k))) or ())
            treffer = _merkmal_treffer(set(muster[_aufruf(k)] or []), je, f, festhaltend) or []
        if treffer:
            out[k] = treffer
    return out


def _haelt_lesen(d: dict, bedarf: set[tuple[str, str]]) -> dict[tuple[str, str], set[str]]:
    """Verfälschungsproben ausführen (d['haelt'] aufrufbar) oder aus einer festen Tabelle {'f|art': [tests]} lesen."""
    h = d.get("haelt")
    out = {}
    for f, art in sorted(bedarf):
        if callable(h):
            out[(f, art)] = set(h(f, art))
        else:
            out[(f, art)] = set((h or {}).get(f"{f}|{art}") or ())
    return out


# ---------------------------------------------------------------- Aufzeichner der deckenden Tests
def _testdatei_pfade(werk: Path, testbestand: dict[str, str], behoben: set[str]) -> list[str]:
    """Pfade (relativ zum Werk) der Dateien, in denen die Tests aus `behoben` ('datei::name', Basisname) stehen."""
    werk = Path(werk)
    bekannt = {Path(p).name: p for p in (testbestand or {}) if p.startswith("tests/")}
    if (werk / "tests").is_dir():
        for f in sorted((werk / "tests").rglob("*")):
            if f.is_file():
                bekannt.setdefault(f.name, str(f.relative_to(werk)))
    return sorted({bekannt[d] for d in {t.partition("::")[0] for t in behoben} if d in bekannt})


def _laedt_modul(text: str, modul: str, python: bool) -> bool:
    """Grob: lädt diese Testdatei das geänderte Modul? (TS: Pfad im Import; Python: Modul- oder Paketpfad.)"""
    if not python:
        return modul in text
    teile = modul.split(".")
    return modul in text or (len(teile) > 1 and f"from {'.'.join(teile[:-1])} import" in text and teile[-1] in text)


def _aufzeichnen(werk: Path, dateien: dict, module: list[str], pfade: list[str], verfaelschen: dict | None) -> dict:
    from ..kern import sprachprofil
    if sprachprofil.ist_typescript(Path(werk)):
        from ..kern import typescript
        try:
            d, _ = typescript._aufruf(Path(werk), "deckung", dateien=dateien, zeitlimit_s=240, module=module,
                                      testdateien=pfade, verfaelschen=verfaelschen)
        except typescript.TypeScriptFehler as e:
            raise SondeAusgefallen(f"Deckungsaufzeichner ausgefallen: {str(e)[:300]}") from e
    else:
        d = _python_sonde(Path(werk), dateien, {"modus": "deckung", "module": module, "testdateien": pfade,
                                                "verfaelschen": verfaelschen}, None)
    if not d.get("gueltig"):
        raise SondeAusgefallen(f"Deckungsaufzeichner ausgefallen: {str(d.get('grund') or d.get('rc'))[:300]}")
    return d


def deckende_aufrufe(werk: Path, code: dict[str, str], testbestand: dict[str, str], behoben: set[str],
                     module: list[str] | None = None) -> dict:
    """Die Tests aus `behoben` (fallen an der Vorgeneration, bestehen am Kandidaten) AM KANDIDATEN mit Aufzeichner
    ausführen. Rückgabe {"tests", "aufrufe", "gelaufen", "blind", "haelt"}: `haelt(f, art)` fährt die Verfälschungsprobe
    (ein Kammerlauf) und liefert die Tests aus `behoben`, die dabei fallen. Ein Aufzeichnerausfall ist ein
    Messgerätausfall (SondeAusgefallen)."""
    from ..kern import sprachprofil
    behoben = set(behoben or ())
    if not behoben:
        return {"tests": [], "aufrufe": [], "blind": [], "haelt": {}}
    python = not sprachprofil.ist_typescript(Path(werk))
    dateien = {**{p: c for p, c in (code or {}).items() if c is not None}, **{p: c for p, c in (testbestand or {}).items() if c is not None}}
    if module is None:
        module = geaenderte_module(code or {}, python=python)
    pfade = _testdatei_pfade(werk, testbestand, behoben)
    if not pfade:
        return {"tests": sorted(behoben), "aufrufe": [], "blind": [], "haelt": {},
                "hinweis": "Testdateien der deckenden Tests nicht gefunden"}
    d = _aufzeichnen(werk, dateien, module, pfade, None)
    # Jeder deckende Test muss auch im Aufzeichnerlauf bestehen — sonst hat das Instrument das Verhalten verändert
    # (Messgerätausfall, kein Urteil über den Kandidaten).
    zustand = d.get("zustand") or {}
    anders = sorted(t for t in behoben if zustand.get(t) != "pass")
    if anders:
        raise SondeAusgefallen(f"Deckungsaufzeichner: {len(anders)} von {len(behoben)} deckenden Tests bestehen im "
                               f"Aufzeichnerlauf nicht ({anders[:3]} → {[zustand.get(t) for t in anders[:3]]})")
    aufrufe = [c for c in d.get("aufrufe") or [] if c.get("test") in behoben]
    mit_aufruf = {c.get("test") for c in aufrufe}
    texte = {Path(p).name: (dateien.get(p) if dateien.get(p) is not None else
                            ((Path(werk) / p).read_text() if (Path(werk) / p).exists() else "")) for p in pfade}
    blind = sorted(t for t in behoben if t not in mit_aufruf
                   and any(_laedt_modul(texte.get(t.partition("::")[0], ""), m, python) for m in module))

    def haelt(f: str, art: str) -> list[str]:
        v = _aufzeichnen(werk, dateien, module, pfade, {"f": f, "art": art})
        z = v.get("zustand") or {}
        return sorted(t for t in behoben if z.get(t) == "fail")
    return {"tests": sorted(behoben), "aufrufe": aufrufe, "gelaufen": sum(1 for t in behoben if zustand.get(t) == "pass"),
            "blind": blind, "haelt": haelt}


# ---------------------------------------------------------------- Kammerläufe der Sonde
def _python_sonde(werk: Path, dateien: dict[str, str], anfrage: dict, referenzlast: str | None) -> dict:
    """Ein Kammerlauf der Python-Sonde (kern/py/verhalten.py). Infrastruktur (Zeitlimit, Kammer, fehlende Ausgabe)
    → art 'infrastruktur' (Zeitlimit mit `zeitlimit`); die Sonde meldet Inhaltsbefunde (Modul lädt nicht) selbst."""
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
        return {"gueltig": False, "art": "infrastruktur", "zeitlimit": bool(e.zeitlimit),
                "grund": ("Zeitlimit" if e.zeitlimit else f"Python-Sonde ohne Ergebnis (rc={e.rc})") + ": "
                         + (e.stderr or e.stdout or "")[-600:]}
    try:
        return _json.loads(m.group(1))
    except ValueError:
        return {"gueltig": False, "art": "infrastruktur", "grund": "Python-Sonde: Ergebnis nicht lesbar"}


def beobachten(werk: Path, dateien: dict[str, str], referenzlast: str, module: list[str],
               bereiche: list[str], signaturen: dict | None = None, beispiele: dict | None = None,
               konstruktion: dict | None = None, korpus_erweitert: bool = True) -> dict:
    """Ein Kammerlauf: Stand bauen, Module einwickeln, Referenzlast und Korpus ausführen.
    `signaturen`, `beispiele`, `konstruktion` (von der Vorgeneration): welche Funktionen mit welchen Eingaben und
    Instanzen gerufen werden — beide Seiten erhalten dieselben Aufrufe. Ohne Angabe liest die Sonde sie selbst."""
    from ..kern import sprachprofil, typescript
    if not sprachprofil.ist_typescript(Path(werk)):
        return _python_sonde(Path(werk), dateien, {"modus": "beobachten", "module": module, "bereiche": list(bereiche),
                                                   "kappe": KAPPE, "signaturen": signaturen, "beispiele": beispiele,
                                                   "konstruktion": konstruktion, "korpus_erweitert": korpus_erweitert},
                             referenzlast)
    try:
        d, _ = typescript._aufruf(Path(werk), "verhalten", dateien=dateien, zeitlimit_s=240,
                                  referenzlast=referenzlast, module=module, bereiche=list(bereiche),
                                  kappe=KAPPE, signaturen=signaturen, beispiele=beispiele,
                                  korpus_erweitert=korpus_erweitert)
    except typescript.TypeScriptFehler as e:
        return {"gueltig": False, "art": "infrastruktur", "grund": str(e)[:800],
                "zeitlimit": '"zeitlimit": true' in str(e)}
    return d


def erreicht(werk: Path, referenzlast: str, module: list[str], bereiche: list[str]) -> dict[str, int]:
    """Welche öffentlichen Funktionen der Module erreicht die Referenzlast (auch über andere Module)? Ein Kammerlauf der
    Sonde an der Vorgeneration; Rückgabe {'modul:funktion': Aufrufe}. Für die Vertragsprobe der Eichproben (S-10)."""
    from ..kern import sprachprofil
    if sprachprofil.ist_typescript(Path(werk)):
        d = beobachten(werk, {}, referenzlast, module, bereiche)
        schluessel = "aufgerufen"
    else:
        d = _python_sonde(Path(werk), {}, {"modus": "erreichbarkeit", "module": module, "bereiche": list(bereiche)},
                          referenzlast)
        schluessel = "erreicht"
    if not d.get("gueltig"):
        raise SondeAusgefallen(f"Sonde (Erreichbarkeit) ausgefallen: {str(d.get('grund'))[:300]}")
    return dict(d.get(schluessel) or {})


# ---------------------------------------------------------------- Urteil
def _enthaltungsgrund(x: str, a: dict, n: dict, alt: dict, neu: dict, eigene: set[str]) -> str:
    if x not in eigene:
        return "nicht erreicht"
    if (alt.get("unvergleichbar") or {}).get(x) or (neu.get("unvergleichbar") or {}).get(x):
        return "unvergleichbar (asynchron)"
    klasse = x.rpartition(".")[0]
    zustand = (alt.get("instanzen") or {}).get(klasse) if klasse else None
    if zustand and str(zustand).startswith("fehlgeschlagen"):
        return f"keine Instanz ({zustand})"
    return "nur Fehler oder nicht vergleichbar"


def pruefen(werk: Path, code: dict[str, str], referenzlast: str | None, bereiche: list[str],
            deckende: dict | Callable[[list[str]], dict], *, korpus_erweitert: bool = True,
            deckungsregel: str = "muster") -> dict:
    """Vorgeneration (Werk wie es ist) gegen Kandidat (Werk + `code`), dieselbe Sonde, dieselbe Last.

    `deckende`: {"tests", "aufrufe", "haelt", "blind"} (deckende_aufrufe) — oder ein Aufruf (Abweichungen → dieses
    dict), der erst ausgewertet wird, wenn es Abweichungen gibt (spart Kammerläufe).
    Rückgabe mit `ausgefuehrt`, `geurteilt`, `tragfaehig`, `grund` und `grund_art` (für den Neutralzähler)."""
    from ..kern import sprachprofil
    python = not sprachprofil.ist_typescript(Path(werk))
    module = geaenderte_module(code, python=python)
    basis = {"module": module, "bereiche": sorted(bereiche), "kappe": KAPPE, "sprache": "python" if python else "typescript",
             "deckungsregel": deckungsregel, "korpus_erweitert": korpus_erweitert,
             "werkzeugdateien": werkzeugdateien(code) if python else []}
    if not module:
        return {**basis, "ausgefuehrt": False, "geurteilt": True, "tragfaehig": True,
                "grund_art": "keine_quellaenderung",
                "grund": "Kandidat ändert keine Quellmodule — Verhalten der Quellen unverändert"
                         + (f" (Werkzeugdateien nicht beobachtbar: {basis['werkzeugdateien']})" if basis["werkzeugdateien"] else ""),
                "beobachtungen": 0, "abweichungen": [], "ungedeckt": [], "gedeckt": {}}
    if not referenzlast:
        # Konfiguration, kein Urteil über den Kandidaten (Review 03 Nr. 3): ohne Referenzlast misst die Sonde nicht.
        raise SondeAusgefallen("keine Referenzlast — die Verhaltenssonde kann nicht messen")
    alt = beobachten(werk, {}, referenzlast, module, bereiche, korpus_erweitert=korpus_erweitert)
    if not alt.get("gueltig"):
        if alt.get("art") != "inhalt":
            raise SondeAusgefallen(f"Sonde an der Vorgeneration ausgefallen ({alt.get('art')}): {str(alt.get('grund'))[:300]}")
        return {**basis, "ausgefuehrt": False, "geurteilt": False, "tragfaehig": True,
                "grund_art": "sonde_vorgeneration_inhalt",
                "grund": f"Vorgeneration nicht beobachtbar — Enthaltung, betrifft den Kandidaten nicht: {str(alt.get('grund'))[:300]}"}
    gleich = dict(signaturen=alt.get("signaturen"), beispiele=alt.get("beispiele"), konstruktion=alt.get("konstruktion"),
                  korpus_erweitert=korpus_erweitert)
    # S-4: die Vorgeneration ein zweites Mal, mit demselben Korpus — was dabei schwankt, ist kein Verhalten des Codes.
    alt2 = beobachten(werk, {}, referenzlast, module, bereiche, **gleich)
    if not alt2.get("gueltig"):
        raise SondeAusgefallen(f"zweite Beobachtung der Vorgeneration ausgefallen ({alt2.get('art')}): {str(alt2.get('grund'))[:300]}")
    b1, b2 = alt.get("beobachtungen") or {}, alt2.get("beobachtungen") or {}
    instabil = sorted(k for k in set(b1) | set(b2) if b1.get(k, _FEHLT) != b2.get(k, _FEHLT))
    neu = beobachten(werk, dict(code), referenzlast, module, bereiche, **gleich)
    wiederholt = False
    if not neu.get("gueltig") and neu.get("zeitlimit"):
        # Review 02 Nr. 21: die Vorgeneration war eben in der Zeit beobachtbar — ein zweites Zeitlimit am Kandidaten
        # ist ein Befund über ihn (z. B. endlos für einen Randfall), kein Messgerätausfall.
        wiederholt = True
        neu = beobachten(werk, dict(code), referenzlast, module, bereiche, **gleich)
        if not neu.get("gueltig") and neu.get("zeitlimit"):
            return {**basis, "ausgefuehrt": False, "geurteilt": True, "tragfaehig": False,
                    "grund_art": "sonde_kandidat_zeitlimit",
                    "grund": f"Sonde am Kandidaten zweimal im Zeitlimit, an der Vorgeneration nicht: {str(neu.get('grund'))[:200]}"}
    if not neu.get("gueltig"):
        if neu.get("art") != "inhalt":
            raise SondeAusgefallen(f"Sonde am Kandidaten ausgefallen ({neu.get('art')}): {str(neu.get('grund'))[:300]}")
        # Die Vorgeneration war eben beobachtbar; scheitert der Kandidat mit Inhalt an derselben Sonde (Modul lädt
        # nicht, Last bricht ab), ist das ein Befund über den Kandidaten.
        return {**basis, "ausgefuehrt": False, "geurteilt": False, "tragfaehig": False,
                "grund_art": "sonde_kandidat_inhalt",
                "grund": f"Sonde am Kandidaten nicht ausführbar ({neu.get('art')}): {str(neu.get('grund'))[:300]}"}
    a, n = dict(b1), dict(neu.get("beobachtungen") or {})
    for k in instabil:
        a.pop(k, None)
        n.pop(k, None)
    # Randfälle einer Funktion, die der Kandidat nicht mehr hat (entfernt/umbenannt), sind kein Verhalten des
    # verbliebenen Codes: getrennt ausgewiesen; ob die Entfernung zulässig ist, entscheiden Tests, Verträge und das Maß.
    entfernt = sorted(_funktionen_in(a, nur_rand=True) - _funktionen_in(n, nur_rand=True))
    for k in [k for k in a if (mf := _modul_funktion(k)) and f"{mf[0]}:{mf[1]}" in entfernt
              and (zerlegen(k) or {}).get("korpus") in ("rand", "form")]:
        a.pop(k)
    roh = vergleichen(a, n, gedeckt=set())
    decke: dict[str, list[str]] = {}
    tests: list[str] = []
    blind: list[str] = []
    deckung_zaehlung = {"tests": 0, "aufrufe": 0, "verfaelschungen": 0}
    muster = {**(neu.get("muster") or {}), **(alt.get("muster") or {})}
    nicht_deckbar = zustandsabhaengig(roh["abweichungen"], alt.get("kopien") or {}, neu.get("kopien") or {})
    if roh["abweichungen"]:
        d = deckende(roh["abweichungen"]) if callable(deckende) else dict(deckende or {})
        tests = sorted(d.get("tests") or [])
        aufrufe = d.get("aufrufe") or []
        blind = sorted(d.get("blind") or [])
        haelt = {}
        if deckungsregel == "muster":
            bedarf = verfaelschungsbedarf(roh["abweichungen"], aufrufe, muster, nicht_deckbar)
            haelt = _haelt_lesen(d, bedarf)
        deckung_zaehlung = {"tests": len(tests), "aufrufe": len(aufrufe), "verfaelschungen": len(haelt),
                            "festhaltend": {f"{f}|{art}": sorted(t) for (f, art), t in haelt.items()}}
        decke = deckung(roh["abweichungen"], aufrufe, muster, nicht_deckbar, haelt, regel=deckungsregel)
    r = vergleichen(a, n, gedeckt=set(decke))
    if not r["tragfaehig"] and blind:
        raise SondeAusgefallen(f"Deckungsaufzeichner blind: {len(blind)} von {len(tests)} deckenden Tests laden ein "
                               f"geändertes Modul und zeigen keinen einzigen aufgezeichneten Aufruf ({blind[:3]}) — "
                               f"{len(r['ungedeckt'])} Abweichung(en) nicht beurteilbar")
    eingewickelt = alt.get("eingewickelt") or {}
    nicht_eingewickelt = alt.get("nicht_eingewickelt") or {}
    alle = ({f"{m}:{f}" for m, fs in eingewickelt.items() for f in (fs or [])}
            | {f"{m}:{f}" for m, fs in (alt.get("signaturen") or {}).items() for f in (fs or {})})
    # Nicht einwickelbare öffentliche Mitglieder (Python: aufrufbare Objekte ohne __wrapped__, TS: Klassen, default,
    # export-Listen) gehören in y — gezählte Enthaltungen, nicht stillschweigend außerhalb des Nenners (Review 02 Nr. 11).
    alle |= {f"{m}:{x.split(' ')[0]}" for m, xs in nicht_eingewickelt.items() for x in (xs or [])}
    alle = sorted(alle - set(entfernt))
    ia, in_ = alt.get("inhalt"), neu.get("inhalt")
    eigene = _funktionen_in(a) | _funktionen_in(n)
    if ia is not None and in_ is not None:
        beobachtet = {x for x in alle if ia.get(x) and in_.get(x)}
    else:        # Sonde ohne Inhaltszählung: wie vor Runde 3 (irgendeine Beobachtung oder ein Aufruf)
        gerufen = (eigene | set(alt.get("aufgerufen") or {}) | set(neu.get("aufgerufen") or {})
                   | set(alt.get("aufgerufen_rand") or {}) | set(neu.get("aufgerufen_rand") or {}))
        beobachtet = {x for x in alle if x in gerufen}
    enthaltungen = {x: _enthaltungsgrund(x, a, n, alt, neu, eigene) for x in alle if x not in beobachtet}
    for m, xs in nicht_eingewickelt.items():
        for x in xs or []:
            name = f"{m}:{x.split(' ')[0]}"
            if name in enthaltungen:
                enthaltungen[name] = "nicht eingewickelt: " + x.partition(" ")[2].strip("()")
    zaehlung: dict[str, int] = {}
    for g in enthaltungen.values():
        zaehlung[g.split(" (")[0].split(":")[0]] = zaehlung.get(g.split(" (")[0].split(":")[0], 0) + 1
    x_von_y = f"{len(beobachtet)} von {len(alle)}"
    unbeobachtet = sorted(enthaltungen)
    unbeobachtete_module = sorted(m for m, fs in eingewickelt.items() if fs and not any(f"{m}:{f}" in beobachtet for f in fs))
    aufschl: dict[str, int] = {}
    for k in r["ungedeckt"]:
        z = zerlegen(k) or {}
        art = ("zustand" if z.get("zustand") else "rueckgabe") + ("/" + z["korpus"] if z.get("korpus") else "/last")
        schl = f"{z.get('modul')}:{z.get('f')} | {'+'.join(muster.get(_aufruf(k)) or ['gewöhnlich'])} | {art}"
        if k in nicht_deckbar:
            schl += " | zustandsabhängig"
        aufschl[schl] = aufschl.get(schl, 0) + 1
    mit_form = {f"{z['modul']}:{z['f']}" for k in n if (z := zerlegen(k)) and z["korpus"] == "form"}
    ohne_form = sorted(x for x in alle if x not in mit_form)
    extra = {"beobachtete_funktionen": x_von_y, "unbeobachtet": unbeobachtet, "unbeobachtete_module": unbeobachtete_module,
             "ohne_formvariante": f"{len(ohne_form)} von {len(alle)}", "ohne_formvariante_namen": ohne_form[:20],
             "enthaltungen": enthaltungen, "enthaltungen_zaehlung": zaehlung,
             "entfernte_funktionen": entfernt, "randfaelle": len([k for k in n if "~rand#" in k and "@" not in k and ">" not in k]),
             "formvarianten": len([k for k in n if "~form#" in k and "@" not in k and ">" not in k]),
             "instabil": len(instabil), "instabil_beispiele": instabil[:10],
             "zustandsabhaengig": sorted(nicht_deckbar)[:20], "zustandsabhaengig_anzahl": len(nicht_deckbar),
             "nicht_eingewickelt": nicht_eingewickelt, "instanzen": alt.get("instanzen") or {},
             "sonde_wiederholt": wiederholt, "hashsaat": neu.get("hashsaat"),
             "ungedeckt_aufschluesselung": dict(sorted(aufschl.items())), "blind": blind}
    if r["tragfaehig"] and not beobachtet:
        # Keine Abweichung, aber auch keine einzige Funktion inhaltlich erreicht: das ist kein bestandenes Urteil.
        return {**basis, **extra, "ausgefuehrt": True, "geurteilt": False, "tragfaehig": True, "grund_art": "unbeobachtet",
                "grund": f"Enthaltung: 0 von {len(alle)} Funktionen der geänderten Module beobachtet",
                "beobachtungen": r["beobachtungen"], "anzahl_abweichungen": 0, "abweichungen": [], "ungedeckt": [],
                "gedeckt": {}, "korpus": alt.get("korpus"), "eingewickelt": eingewickelt}
    return {**basis, **extra, "ausgefuehrt": True, "geurteilt": True, "tragfaehig": r["tragfaehig"],
            "grund": r["grund"] + f" ({x_von_y} Funktionen beobachtet)",
            "grund_art": "geurteilt", "beobachtungen": r["beobachtungen"],
            "anzahl_abweichungen": len(r["abweichungen"]), "abweichungen": r["abweichungen"][:20],
            "ungedeckt": r["ungedeckt"][:20], "ungedeckt_alle": r["ungedeckt"], "gedeckt": decke,
            "werte": {k: [a.get(k, "<nicht beobachtet>"), n.get(k, "<nicht beobachtet>")]
                      for k in r["abweichungen"][:10]},
            "eingaben": {k: (neu.get("argumente") or {}).get(_aufruf(k)) for k in r["ungedeckt"][:10]},
            "korpus": alt.get("korpus"), "eingewickelt": eingewickelt,
            "deckende_tests": tests, "deckung_zaehlung": deckung_zaehlung}


def kurz(e: dict) -> dict:
    """Protokollform: ohne Beobachtungswerte außer den ersten Abweichungen."""
    schluessel = ("ausgefuehrt", "geurteilt", "tragfaehig", "grund", "grund_art", "module", "bereiche", "beobachtungen",
                  "anzahl_abweichungen", "abweichungen", "ungedeckt", "gedeckt", "werte", "korpus",
                  "eingewickelt", "unbeobachtet", "deckende_tests", "beobachtete_funktionen", "unbeobachtete_module",
                  "entfernte_funktionen", "randfaelle", "formvarianten", "sprache", "eingaben", "deckung_zaehlung",
                  "nicht_eingewickelt", "enthaltungen", "enthaltungen_zaehlung", "instabil", "instabil_beispiele",
                  "zustandsabhaengig", "zustandsabhaengig_anzahl", "instanzen", "sonde_wiederholt", "hashsaat",
                  "ungedeckt_aufschluesselung", "blind", "deckungsregel", "korpus_erweitert", "werkzeugdateien",
                  "ohne_formvariante", "ohne_formvariante_namen")
    return {k: e[k] for k in schluessel if k in e}
