"""Behebungsrunde 2 vor T4 — verhaltensvergleich.py: Python-Sonde anbinden, Deckung je Abweichung, ~form-Beobachtungen.
Ersetzt benannte Anker (je genau einmal)."""
from pathlib import Path

P = Path('/root/biotop/biotop/organe/verhaltensvergleich.py')
s = P.read_text()


def ersetze(alt, neu):
    global s
    assert s.count(alt) == 1, (s.count(alt), alt[:100])
    s = s.replace(alt, neu)


ersetze('''Die Sonde gibt es bisher nur für TypeScript. Für andere Sprachen enthält sich das Organ —
gezählt im Neutralzähler, so dass keine Torzeile auf einem schweigenden Organ ruht.
''', '''Sonden: TypeScript (kern/ts/verhalten.mjs) und — seit der Behebungsrunde 2 vor T4 — Python (kern/py/verhalten.py),
im selben Umfang: einzeln, Folge (#0…#7), Alias, Mutation, Rücksetzung, Randfälle und Formvarianten. Entscheidung
Chat-Claude (23.09.): Grundsatz 11 gilt für jede Sprache; T4 ist Python.
''')
ersetze('''- Ein Sondenausfall (Kammerabbruch, Zeitlimit, beschädigter Transport — `art` 'infrastruktur'; fehlende Referenzlast)''',
        '''- Formvarianten (~form#j, Behebungsrunde 2): dieselben Eingaben in anderer Form — Weißraum (Tab, Zeilenumbruch,
  doppelt, CRLF, geschütztes Leerzeichen, am Rand), Groß/Klein, Zahlform im Text, Schlüsselfolge, in Python auch
  Zahltyp und Behälter. Befund: Die Weißraumlücke von K2868 (T3) lag in keinem Randwert.
- Deckung je Abweichung (Grundsatz 11, Entscheidung Chat-Claude): Eine Abweichung ist gedeckt, wenn ein Test, der an
  der Vorgeneration fällt und am Kandidaten besteht, die abweichende Funktion mit DERSELBEN Eingabe ruft (kanonische
  Form) — bei @mutation und @nach_ruecksetzung zusätzlich im selben Aufrufmuster (dasselbe Objekt, an Ort und Stelle
  geändert, erneut gerufen). Beweis ist der aufgezeichnete Aufruf am Kandidaten, nicht der Quelltext des Tests:
  Bisher deckte jeder Test, der `f(` enthielt, JEDE Abweichung von f (T3/K2868: 3 Befundklassen-Tests deckten 12
  Abweichungen, auch eine konstruierte Weißraum-Abweichung).
- Ein Sondenausfall (Kammerabbruch, Zeitlimit, beschädigter Transport — `art` 'infrastruktur'; fehlende Referenzlast)''')

# ---- Modulnamen je Sprache
ersetze('''def geaenderte_module(code: dict[str, str]) -> list[str]:
    """Quellmodule des Kandidaten als Pfade unter dist/ ohne Endung (src/zahlen/x.ts → zahlen/x)."""
    return sorted(p[len("src/"):-len(".ts")] for p in code
                  if p.startswith("src/") and p.endswith(".ts") and not p.endswith(".d.ts"))''',
        '''def geaenderte_module(code: dict[str, str], python: bool = False) -> list[str]:
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
                  if p.startswith("src/") and p.endswith(".ts") and not p.endswith(".d.ts"))''')

# ---- Schlüssel mit ~form
ersetze('''    """'zahlen/statistik:quantil#0@mutation' → 'quantil' (auch Randfälle 'quantil~rand#3'); Korpuszeilen haben keine."""
    m = re.match(r"^[^:]+:([A-Za-z_$][\\w$]*)(?:~rand)?#\\d+", beobachtung)''',
        '''    """'zahlen/statistik:quantil#0@mutation' → 'quantil' (auch Randfälle 'quantil~rand#3' und Formvarianten
    'quantil~form#1'); Korpuszeilen haben keine."""
    m = re.match(r"^[^:]+:([A-Za-z_$][\\w$]*)(?:~rand|~form)?#\\d+", beobachtung)''')
ersetze('''    m = re.match(r"^([^:]+):([A-Za-z_$][\\w$]*)(?:~rand)?#\\d+", beobachtung)
    return (m.group(1), m.group(2)) if m else None''',
        '''    m = re.match(r"^([^:]+):([A-Za-z_$][\\w$]*)(?:~rand|~form)?#\\d+", beobachtung)
    return (m.group(1), m.group(2)) if m else None''')
ersetze('''    return {f"{mf[0]}:{mf[1]}" for k in beob if (not nur_rand or "~rand#" in k) and (mf := _modul_funktion(k))}''',
        '''    return {f"{mf[0]}:{mf[1]}" for k in beob if (not nur_rand or "~rand#" in k or "~form#" in k) and (mf := _modul_funktion(k))}''')

# ---- Deckung je Abweichung
alt_deckung_anfang = s.index('def deckung(abweichungen: list[str], deckende_tests: dict[str, str]) -> dict[str, list[str]]:')
alt_deckung_ende = s.index('def beobachten(werk: Path, dateien: dict[str, str], referenzlast: str, module: list[str],')
s = s[:alt_deckung_anfang] + '''def _muster_erfuellt(aufrufe_f: list[dict], x: str, muster: str) -> bool:
    """Ruft ein Test die Funktion mit der Eingabe `x` (kanonisch) — und bei Mustern im selben Aufrufmuster?
    `aufrufe_f`: die aufgezeichneten Aufrufe EINES Tests an DIESE Funktion, in Reihenfolge; je Aufruf `args` (kanonisch),
    `ids` (Identität je Objektargument, sonst None) und `inhalt` (kanonischer Inhalt je Objektargument)."""
    idx = [i for i, c in enumerate(aufrufe_f) if c.get("args") == x]
    if not idx:
        return False
    if not muster:
        return True
    if muster == "alias":
        return any(aufrufe_f[j].get("args") == x and aufrufe_f[j].get("ids") == aufrufe_f[i].get("ids")
                   for i in idx for j in range(i + 1, len(aufrufe_f)))
    if muster in ("mutation", "nach_ruecksetzung"):
        for i in idx:
            ids = aufrufe_f[i].get("ids") or []
            if not any(k is not None for k in ids):
                continue
            for j in range(i + 1, len(aufrufe_f)):
                if aufrufe_f[j].get("ids") == ids and aufrufe_f[j].get("inhalt") != aufrufe_f[i].get("inhalt"):
                    if muster == "mutation":
                        return True
                    if any(aufrufe_f[k].get("ids") == ids and aufrufe_f[k].get("inhalt") == aufrufe_f[i].get("inhalt")
                           for k in range(j + 1, len(aufrufe_f))):
                        return True
    return False


def deckung(abweichungen: list[str], aufrufe: list[dict], argumente: dict[str, str],
            alt: dict | None = None, neu: dict | None = None) -> dict[str, list[str]]:
    """{abweichung: [test]} — Deckung JE ABWEICHUNG (Grundsatz 11, Entscheidung Chat-Claude 23.09.2026).

    Ein Test deckt eine Abweichung, wenn er an der Vorgeneration fällt und am Kandidaten besteht (das stellt der Aufrufer
    sicher: `aufrufe` stammen nur von solchen Tests, aufgezeichnet AM KANDIDATEN) und die abweichende Funktion mit
    derselben Eingabe ruft wie die Sonde (`argumente[beobachtung ohne @muster]`, kanonisch). Muster:
      @alias, @nach_ruecksetzung — zeigt das Muster auf BEIDEN Seiten denselben Wert wie der Aufruf selbst, ist es keine
        eigene Verhaltensaussage und gilt mit dem Aufruf als gedeckt; sonst muss der Test das Muster selbst ausführen;
      @mutation — immer das Muster selbst: dieselbe Eingabe, dann dasselbe Objekt an Ort und Stelle geändert und erneut
        gerufen (die Stelle, an der ein Zwischenspeicher an der Referenz veraltete Ergebnisse liefert).
    Eine Abweichung ohne aufgezeichnete Eingabe (z. B. aus einer Korpuszeile) ist nie gedeckt."""
    je_test: dict[str, dict[str, list[dict]]] = {}
    for c in aufrufe or []:
        je_test.setdefault(c.get("test", ""), {}).setdefault(c.get("f", ""), []).append(c)
    a, n = alt or {}, neu or {}

    def gedeckt_durch(schluessel: str) -> list[str]:
        mf = _modul_funktion(schluessel)
        if not mf:
            return []
        basis, _, muster = schluessel.partition("@")
        x = argumente.get(basis)
        if x is None:
            return []
        f = f"{mf[0]}:{mf[1]}"
        abgeleitet = muster in ("alias", "nach_ruecksetzung") and a.get(schluessel, _FEHLT) == a.get(basis, _FEHLT) \\
            and n.get(schluessel, _FEHLT) == n.get(basis, _FEHLT)
        return sorted(t for t, fs in je_test.items()
                      if _muster_erfuellt(fs.get(f, []), x, "" if abgeleitet else muster))

    out: dict[str, list[str]] = {}
    for b in abweichungen:
        treffer = gedeckt_durch(b)
        if treffer:
            out[b] = treffer
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
                     module: list[str]) -> dict:
    """Die Tests aus `behoben` (fallen an der Vorgeneration, bestehen am Kandidaten) AM KANDIDATEN mit Aufzeichner
    ausführen. Rückgabe {"tests", "aufrufe"}; ein Aufzeichnerausfall ist ein Messgerätausfall (SondeAusgefallen)."""
    from ..kern import sprachprofil
    behoben = set(behoben or ())
    if not behoben:
        return {"tests": [], "aufrufe": []}
    dateien = {**{p: c for p, c in (code or {}).items() if c is not None}, **{p: c for p, c in (testbestand or {}).items() if c is not None}}
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
    return {"tests": sorted(behoben), "aufrufe": [c for c in d.get("aufrufe") or [] if c.get("test") in behoben]}


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


''' + s[alt_deckung_ende:]

# ---- _einzeltest/deckende_tests lagen zwischen deckung und beobachten und sind mit dem Ersatz oben entfallen
assert 'def _einzeltest(' not in s and 'def deckende_tests(' not in s

# ---- beobachten: Sprache wählen
ersetze('''    from ..kern import typescript
    try:
        d, _ = typescript._aufruf(Path(werk), "verhalten", dateien=dateien, zeitlimit_s=240,
                                  referenzlast=referenzlast, module=module, bereiche=list(bereiche),
                                  kappe=KAPPE, signaturen=signaturen, beispiele=beispiele)
    except typescript.TypeScriptFehler as e:
        return {"gueltig": False, "art": "infrastruktur", "grund": str(e)[:800]}
    return d''', '''    from ..kern import sprachprofil, typescript
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
    return d''')

# ---- pruefen: keine Enthaltung mehr für Python; Deckung je Abweichung
ersetze('''            deckende: dict[str, str] | Callable[[], dict[str, str]]) -> dict:''',
        '''            deckende: dict | Callable[[list[str]], dict]) -> dict:''')
ersetze('''    `deckende`: Tests, die an der Vorgeneration fallen und am Kandidaten bestehen — als dict oder als
    Aufruf, der erst ausgewertet wird, wenn es Abweichungen gibt (spart Kammerläufe).''',
        '''    `deckende`: {"tests": [...], "aufrufe": [...]} — die Tests, die an der Vorgeneration fallen und am Kandidaten
    bestehen, und ihre am Kandidaten aufgezeichneten Aufrufe (deckende_aufrufe) — oder ein Aufruf (Abweichungen →
    dieses dict), der erst ausgewertet wird, wenn es Abweichungen gibt (spart Kammerläufe).''')
ersetze('''    from ..kern import sprachprofil
    module = geaenderte_module(code)
    basis = {"module": module, "bereiche": sorted(bereiche), "kappe": KAPPE}
    if not sprachprofil.ist_typescript(Path(werk)):
        return {**basis, "ausgefuehrt": False, "geurteilt": False, "tragfaehig": True,
                "grund_art": "sprache_ohne_sonde",
                "grund": "Verhaltenssonde gibt es bisher nur für TypeScript — Enthaltung, gezählt"}
''', '''    from ..kern import sprachprofil
    python = not sprachprofil.ist_typescript(Path(werk))
    module = geaenderte_module(code, python=python)
    basis = {"module": module, "bereiche": sorted(bereiche), "kappe": KAPPE, "sprache": "python" if python else "typescript"}
''')
ersetze('''    roh = vergleichen(a, n, gedeckt=set())
    decke: dict[str, list[str]] = {}
    tests: dict[str, str] = {}
    if roh["abweichungen"]:
        tests = deckende() if callable(deckende) else dict(deckende or {})
        decke = deckung(roh["abweichungen"], tests)''', '''    roh = vergleichen(a, n, gedeckt=set())
    decke: dict[str, list[str]] = {}
    tests: list[str] = []
    if roh["abweichungen"]:
        d = deckende(roh["abweichungen"]) if callable(deckende) else dict(deckende or {})
        tests = sorted(d.get("tests") or [])
        argumente = {**(neu.get("argumente") or {}), **(alt.get("argumente") or {})}
        decke = deckung(roh["abweichungen"], d.get("aufrufe") or [], argumente, a, n)''')
ersetze('''             "entfernte_funktionen": entfernt, "randfaelle": len([k for k in n if "~rand#" in k and "@" not in k])}''',
        '''             "entfernte_funktionen": entfernt, "randfaelle": len([k for k in n if "~rand#" in k and "@" not in k]),
             "formvarianten": len([k for k in n if "~form#" in k and "@" not in k])}''')
ersetze('''            "werte": {k: [a.get(k, "<nicht beobachtet>"), n.get(k, "<nicht beobachtet>")]
                      for k in r["abweichungen"][:10]},''', '''            "werte": {k: [a.get(k, "<nicht beobachtet>"), n.get(k, "<nicht beobachtet>")]
                      for k in r["abweichungen"][:10]},
            "eingaben": {k: (alt.get("argumente") or {}).get(k.partition("@")[0]) for k in r["ungedeckt"][:10]},''')
ersetze('''            "unbeobachtet": unbeobachtet, "deckende_tests": sorted(tests)}''',
        '''            "unbeobachtet": unbeobachtet, "deckende_tests": tests}''')
ersetze('''                  "entfernte_funktionen", "randfaelle")''',
        '''                  "entfernte_funktionen", "randfaelle", "formvarianten", "sprache", "eingaben")''')
P.write_text(s)
print('verhaltensvergleich.py umgebaut,', len(s.splitlines()), 'Zeilen')
