"""Deckungsaufzeichner härten (TS + Python): (1) jeder deckende Test muss im Aufzeichnerlauf ebenfalls bestehen — sonst
verändert das Instrument das Verhalten: Messgerätausfall, kein Urteil; (2) Einträge eindeutig (Test, Funktion, Eingabe,
Ergebnis), Überlauf laut statt abgeschnitten; (3) TS: überladene Signaturen nur einmal einwickeln; (4) Zählung im Urteil
(Tests gelaufen, Aufrufe aufgezeichnet), damit ein leerer Aufzeichner sichtbar ist."""
from pathlib import Path

R = Path('/root/biotop')


def ersetze(p, alt, neu, n=1):
    s = p.read_text()
    assert s.count(alt) == n, (p.name, s.count(alt), alt[:90])
    p.write_text(s.replace(alt, neu))


TS = R / 'biotop/kern/ts'
ersetze(TS / 'vitest.deck.config.mjs', """  const namen = [];
  const neu = code.replace(/^export (async )?function (\\w+)\\s*(<[^>()]*>)?\\s*\\(/gm, (m, asy, name, gen) => {
    namen.push(name);""", """  const namen = [];
  const neu = code.replace(/^export (async )?function (\\w+)\\s*(<[^>()]*>)?\\s*\\(/gm, (m, asy, name, gen) => {
    if (!namen.includes(name)) namen.push(name);      // überladene Signaturen: ein Einwickler je Name""")
ersetze(TS / 'vitest.deck.config.mjs', "hookTimeout: 8000, setupFiles: ['/werk/_messgeraet/ts/deck-setup.mjs'], reporters: ['default'], watch: false,",
        "hookTimeout: 8000, setupFiles: ['/werk/_messgeraet/ts/deck-setup.mjs'], reporters: [new Nachweis()], watch: false,")
ersetze(TS / 'vitest.deck.config.mjs', "import fs from 'node:fs';\n", "import fs from 'node:fs';\nimport Nachweis from './reporter.mjs';\n")
ersetze(TS / 'deck-setup.mjs', """const aufrufe = [];
let aktuell = '';""", """const aufrufe = [], gesehen = new Set();
let aktuell = '';""")
ersetze(TS / 'deck-setup.mjs', """  const eintrag = {test: aktuell, f: name, args: eingabeText(args), erg: null};
  aufrufe.push(eintrag);
  try {
    const v = call(...args);
    eintrag.erg = ergebnisText(v);
    return v;
  } catch (e) {
    eintrag.erg = fehlerText(e);
    throw e;
  }
};""", """  const eintrag = {test: aktuell, f: name, args: eingabeText(args), erg: null};
  const merken = () => { const s = JSON.stringify(eintrag); if (!gesehen.has(s)) { gesehen.add(s); aufrufe.push(eintrag); } };
  try {
    const v = call(...args);
    eintrag.erg = ergebnisText(v);
    merken();
    return v;
  } catch (e) {
    eintrag.erg = fehlerText(e);
    merken();
    throw e;
  }
};""")
ersetze(TS / 'deckung.mjs', """  const aufrufe = fs.existsSync('/tmp/ts-deck.jsonl')
    ? fs.readFileSync('/tmp/ts-deck.jsonl', 'utf8').split('\\n').filter(Boolean).map(z => JSON.parse(z)) : [];
  return {gueltig: !p.fehler && !p.signal && [0, 1].includes(p.rc), rc: p.rc, aufrufe: aufrufe.slice(0, 20000),
          grund: p.rc === 0 || p.rc === 1 ? '' : 'Vitest-Abbruch rc=' + p.rc + ' ' + String(p.stderr).slice(-600)};""",
        """  const aufrufe = fs.existsSync('/tmp/ts-deck.jsonl')
    ? fs.readFileSync('/tmp/ts-deck.jsonl', 'utf8').split('\\n').filter(Boolean).map(z => JSON.parse(z)) : [];
  // Zustand je Test aus demselben Lauf (Nachweis-Reporter): der Wirt verlangt, dass jeder deckende Test auch hier besteht.
  let zustand = {};
  try {
    const n = JSON.parse(fs.readFileSync('/tmp/ts-nachweis.json', 'utf8'));
    for (const t of n.tests ?? []) zustand[path.basename(t.id.split('::')[0]) + '::' + t.id.split('::').slice(1).join('::')] = t.state;
  } catch { zustand = null; }
  const ueberlauf = aufrufe.length > 20000;       // laut statt abgeschnitten
  return {gueltig: !p.fehler && !p.signal && [0, 1].includes(p.rc) && zustand !== null && !ueberlauf, rc: p.rc,
          aufrufe: ueberlauf ? [] : aufrufe, zustand: zustand ?? {}, ueberlauf,
          grund: ueberlauf ? 'Aufzeichnung über 20000 eindeutige Aufrufe — nicht abgeschnitten, sondern verworfen'
               : zustand === null ? 'Nachweis des Aufzeichnerlaufs fehlt'
               : p.rc === 0 || p.rc === 1 ? '' : 'Vitest-Abbruch rc=' + p.rc + ' ' + String(p.stderr).slice(-600)};""")
ersetze(TS / 'deckung.mjs', "import fs from 'node:fs';\n", "import fs from 'node:fs';\nimport path from 'node:path';\n")

P = R / 'biotop/kern/py/verhalten.py'
ersetze(P, """def deck_wickeln(name, orig):""", """_GESEHEN = set()
ZUSTAND = {}


def deck_wickeln(name, orig):""")
ersetze(P, """        eintrag = {'test': AKTUELL[0], 'f': name, 'args': eingabe_text(args, kwargs), 'erg': None}
        aufrufe.append(eintrag)
        try:
            v = orig(*args, **kwargs)
        except BaseException as e:  # noqa: B902
            eintrag['erg'] = 'Fehler:' + type(e).__name__
            raise
        try:
            eintrag['erg'] = knapp(text_von(v)) if not (inspect.isgenerator(v) or inspect.iscoroutine(v)) else '__iterator'
        except Exception:  # noqa: BLE001
            eintrag['erg'] = '__unkanonisch'
        return v""", """        eintrag = {'test': AKTUELL[0], 'f': name, 'args': eingabe_text(args, kwargs), 'erg': None}

        def merken():
            s = json.dumps(eintrag, sort_keys=True)
            if s not in _GESEHEN:
                _GESEHEN.add(s)
                aufrufe.append(eintrag)
        try:
            v = orig(*args, **kwargs)
        except BaseException as e:  # noqa: B902
            eintrag['erg'] = 'Fehler:' + type(e).__name__
            merken()
            raise
        try:
            eintrag['erg'] = knapp(text_von(v)) if not (inspect.isgenerator(v) or inspect.iscoroutine(v)) else '__iterator'
        except Exception:  # noqa: BLE001
            eintrag['erg'] = '__unkanonisch'
        merken()
        return v""")
ersetze(P, """            def pytest_runtest_setup(self, item):
                datei, _, rest = item.nodeid.partition('::')
                AKTUELL[0] = os.path.basename(datei) + '::' + rest
        rc = pytest.main(['-q', '-p', 'no:cacheprovider', '--tb=no', *(REQ.get('testdateien') or [])], plugins=[Plugin()])
        return {'gueltig': int(rc) in (0, 1), 'rc': int(rc), 'aufrufe': aufrufe[:20000], 'eingewickelt': eingewickelt}""",
        """            def pytest_runtest_setup(self, item):
                datei, _, rest = item.nodeid.partition('::')
                AKTUELL[0] = os.path.basename(datei) + '::' + rest

            def pytest_runtest_logreport(self, report):
                datei, _, rest = report.nodeid.partition('::')
                tid = os.path.basename(datei) + '::' + rest
                if report.when == 'call' or report.outcome != 'passed':
                    ZUSTAND[tid] = 'pass' if report.outcome == 'passed' and ZUSTAND.get(tid, 'pass') == 'pass' else 'fail'
        rc = pytest.main(['-q', '-p', 'no:cacheprovider', '--tb=no', *(REQ.get('testdateien') or [])], plugins=[Plugin()])
        ueberlauf = len(aufrufe) > 20000        # laut statt abgeschnitten
        return {'gueltig': int(rc) in (0, 1) and not ueberlauf, 'rc': int(rc), 'aufrufe': [] if ueberlauf else aufrufe,
                'zustand': ZUSTAND, 'ueberlauf': ueberlauf, 'eingewickelt': eingewickelt,
                'grund': 'Aufzeichnung über 20000 eindeutige Aufrufe — verworfen, nicht abgeschnitten' if ueberlauf else ''}""")

V = R / 'biotop/organe/verhaltensvergleich.py'
ersetze(V, """    if not d.get("gueltig"):
        raise SondeAusgefallen(f"Deckungsaufzeichner ausgefallen: {str(d.get('grund') or d.get('rc'))[:300]}")
    return {"tests": sorted(behoben), "aufrufe": [c for c in d.get("aufrufe") or [] if c.get("test") in behoben]}""",
        """    if not d.get("gueltig"):
        raise SondeAusgefallen(f"Deckungsaufzeichner ausgefallen: {str(d.get('grund') or d.get('rc'))[:300]}")
    # Jeder deckende Test muss auch im Aufzeichnerlauf bestehen — sonst hat das Instrument das Verhalten verändert
    # (Messgerätausfall, kein Urteil über den Kandidaten).
    zustand = d.get("zustand") or {}
    anders = sorted(t for t in behoben if zustand.get(t) != "pass")
    if anders:
        raise SondeAusgefallen(f"Deckungsaufzeichner: {len(anders)} von {len(behoben)} deckenden Tests bestehen im "
                               f"Aufzeichnerlauf nicht ({anders[:3]} → {[zustand.get(t) for t in anders[:3]]})")
    aufrufe = [c for c in d.get("aufrufe") or [] if c.get("test") in behoben]
    return {"tests": sorted(behoben), "aufrufe": aufrufe, "gelaufen": sum(1 for t in behoben if zustand.get(t) == "pass")}""")
ersetze(V, """        tests = sorted(d.get("tests") or [])
        decke = deckung(roh["abweichungen"], d.get("aufrufe") or [], neu.get("argumente") or {}, n)""",
        """        tests = sorted(d.get("tests") or [])
        deckung_zaehlung = {"tests": len(tests), "aufrufe": len(d.get("aufrufe") or [])}
        decke = deckung(roh["abweichungen"], d.get("aufrufe") or [], neu.get("argumente") or {}, n)""")
ersetze(V, """    decke: dict[str, list[str]] = {}
    tests: list[str] = []
    if roh["abweichungen"]:""", """    decke: dict[str, list[str]] = {}
    tests: list[str] = []
    deckung_zaehlung = {"tests": 0, "aufrufe": 0}
    if roh["abweichungen"]:""")
ersetze(V, """            "unbeobachtet": unbeobachtet, "deckende_tests": tests}""",
        """            "unbeobachtet": unbeobachtet, "deckende_tests": tests, "deckung_zaehlung": deckung_zaehlung}""")
ersetze(V, """                  "entfernte_funktionen", "randfaelle", "formvarianten", "sprache", "eingaben")""",
        """                  "entfernte_funktionen", "randfaelle", "formvarianten", "sprache", "eingaben", "deckung_zaehlung")""")
print('gehärtet')
