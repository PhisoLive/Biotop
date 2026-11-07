"""Behebungsrunde 2 vor T4 — Deckung je Abweichung, einheitliche Regel: Ein Test deckt eine Abweichung, wenn er (an der
Vorgeneration fallend, am Kandidaten bestehend) die Funktion AM KANDIDATEN mit derselben Eingabe gerufen und dasselbe
Ergebnis bekommen hat, das die Sonde am Kandidaten für diese Beobachtung sah (kanonische Form, auch Fehlerklasse).
Dafür schreibt die Sonde die Eingabe JE AUFRUFMUSTER (vor dem Aufruf, also nach Mutation bzw. Rücksetzung) und der
Aufzeichner das Ergebnis je Aufruf. Ersetzt benannte Anker (je genau einmal)."""
from pathlib import Path

R = Path('/root/biotop')


def ersetze(p, alt, neu, n=1):
    s = p.read_text()
    assert s.count(alt) == n, (p.name, s.count(alt), alt[:100])
    p.write_text(s.replace(alt, neu))


# ---------------------------------------------------------------- TypeScript
K = R / 'biotop/kern/ts/kanon.mjs'
K.write_text(K.read_text() + """
// Ergebnistext eines Aufrufs — genau wie verhalten-runner.mjs/wert() ihn für die Beobachtung bildet.
export function ergebnisText(v) {
  if (v && typeof v.then === 'function') return '__promise';
  try { return knapp(JSON.stringify(kan(v, new Set()))); } catch { return '__unkanonisch'; }
}
export function fehlerText(e) { return 'Fehler:' + (e?.constructor?.name ?? 'unbekannt'); }
export function eingabeText(args) {
  try { return knapp(JSON.stringify(kan(args, new Set()))); } catch { return '__unkanonisch'; }
}
""")
V = R / 'biotop/kern/ts/verhalten-runner.mjs'
ersetze(V, "import {kan, knapp} from './kanon.mjs';", "import {kan, knapp, eingabeText} from './kanon.mjs';")
ersetze(V, """    try { argtext[schluessel] = knapp(JSON.stringify(kan(args, new Set()))); } catch { argtext[schluessel] = '__unkanonisch'; }
    const erst = wert(() => call(...args));
    beob[schluessel] = knapp(erst.text);
    const stand = schnappschuss(args);
    beob[`${schluessel}@alias`] = knapp(wert(() => call(...args)).text);
    zuruecksetzen(stand);
    if (mutieren(args) > 0) {
      beob[`${schluessel}@mutation`] = knapp(wert(() => call(...args)).text);
      zuruecksetzen(stand);
      beob[`${schluessel}@nach_ruecksetzung`] = knapp(wert(() => call(...args)).text);
      zuruecksetzen(stand);
    }""", """    // Eingabe JE AUFRUFMUSTER, unmittelbar vor dem Aufruf (nach Mutation bzw. Rücksetzung) — Grundlage der Deckung je
    // Abweichung: ein deckender Test muss dieselbe Eingabe mit demselben Ergebnis gerufen haben.
    const beiAufruf = k => { argtext[k] = eingabeText(args); };
    beiAufruf(schluessel);
    const erst = wert(() => call(...args));
    beob[schluessel] = knapp(erst.text);
    const stand = schnappschuss(args);
    beiAufruf(`${schluessel}@alias`);
    beob[`${schluessel}@alias`] = knapp(wert(() => call(...args)).text);
    zuruecksetzen(stand);
    if (mutieren(args) > 0) {
      beiAufruf(`${schluessel}@mutation`);
      beob[`${schluessel}@mutation`] = knapp(wert(() => call(...args)).text);
      zuruecksetzen(stand);
      beiAufruf(`${schluessel}@nach_ruecksetzung`);
      beob[`${schluessel}@nach_ruecksetzung`] = knapp(wert(() => call(...args)).text);
      zuruecksetzen(stand);
    }""")
D = R / 'biotop/kern/ts/deck-setup.mjs'
ersetze(D, "import {kan, knapp} from './kanon.mjs';", "import {ergebnisText, fehlerText, eingabeText} from './kanon.mjs';")
ersetze(D, """const kennung = x => (x === null || typeof x !== 'object') ? null : (ids.has(x) ? ids.get(x) : (ids.set(x, naechste), naechste++));
const text = x => { try { return knapp(JSON.stringify(kan(x, new Set()))); } catch { return '__unkanonisch'; } };
globalThis.__vvDeck = (name, args, call) => {
  try {
    aufrufe.push({test: aktuell, f: name, args: text(args), ids: args.map(kennung),
                  inhalt: args.map(a => (a !== null && typeof a === 'object') ? text(a) : null)});
  } catch { /* der Aufzeichner darf den Test nie beeinflussen */ }
  return call(...args);
};""", """// Je Aufruf: Test, Funktion, Eingabe (kanonisch, vor dem Aufruf) und Ergebnis (wie die Sonde es schreibt).
globalThis.__vvDeck = (name, args, call) => {
  const eintrag = {test: aktuell, f: name, args: eingabeText(args), erg: null};
  aufrufe.push(eintrag);
  try {
    const v = call(...args);
    eintrag.erg = ergebnisText(v);
    return v;
  } catch (e) {
    eintrag.erg = fehlerText(e);
    throw e;
  }
};""")
ersetze(D, "const ids = new WeakMap();\nlet naechste = 1;\n", "")

# ---------------------------------------------------------------- Python-Sonde
P = R / 'biotop/kern/py/verhalten.py'
ersetze(P, """sys.path.insert(0, '/werk')
REQ = json.load(open(sys.argv[1], encoding='utf-8'))
KAPPE = REQ.get('kappe') or 8
RAND_KAPPE = REQ.get('rand_kappe') or 16
FORM_KAPPE = REQ.get('form_kappe') or 16
""", """REQ = {}
KAPPE, RAND_KAPPE, FORM_KAPPE = 8, 16, 16
""")
ersetze(P, """    TIEFE[0] += 1
    try:
        argtext[schl] = knapp(text_von([list(args), kwargs]))
        erst = wert(lambda: call(*args, **kwargs))
        beob[schl] = knapp(erst['text'])
        werte = list(args) + list(kwargs.values())
        stand = schnappschuss(werte)
        beob[schl + '@alias'] = knapp(wert(lambda: call(*args, **kwargs))['text'])
        zuruecksetzen(stand)
        if mutieren(werte) > 0:
            beob[schl + '@mutation'] = knapp(wert(lambda: call(*args, **kwargs))['text'])
            zuruecksetzen(stand)
            beob[schl + '@nach_ruecksetzung'] = knapp(wert(lambda: call(*args, **kwargs))['text'])
            zuruecksetzen(stand)
        return erst""", """    TIEFE[0] += 1
    try:
        def bei_aufruf(k):          # Eingabe je Aufrufmuster, unmittelbar vor dem Aufruf (Deckung je Abweichung)
            argtext[k] = eingabe_text(args, kwargs)
        bei_aufruf(schl)
        erst = wert(lambda: call(*args, **kwargs))
        beob[schl] = knapp(erst['text'])
        werte = list(args) + list(kwargs.values())
        stand = schnappschuss(werte)
        bei_aufruf(schl + '@alias')
        beob[schl + '@alias'] = knapp(wert(lambda: call(*args, **kwargs))['text'])
        zuruecksetzen(stand)
        if mutieren(werte) > 0:
            bei_aufruf(schl + '@mutation')
            beob[schl + '@mutation'] = knapp(wert(lambda: call(*args, **kwargs))['text'])
            zuruecksetzen(stand)
            bei_aufruf(schl + '@nach_ruecksetzung')
            beob[schl + '@nach_ruecksetzung'] = knapp(wert(lambda: call(*args, **kwargs))['text'])
            zuruecksetzen(stand)
        return erst""")
ersetze(P, """def knapp(t):""", """def eingabe_text(args, kwargs):
    try:
        return knapp(text_von([list(args), kwargs]))
    except Exception:  # noqa: BLE001
        return '__unkanonisch'


def knapp(t):""")
ersetze(P, """def deck_wickeln(name, orig):
    def w(*args, **kwargs):
        try:
            werte = list(args) + list(kwargs.values())
            aufrufe.append({'test': AKTUELL[0], 'f': name, 'args': knapp(text_von([list(args), kwargs])),
                            'ids': [id(v) if _veraenderlich(v) else None for v in werte],
                            'inhalt': [knapp(text_von(v)) if _veraenderlich(v) else None for v in werte]})
        except Exception:  # noqa: BLE001 — der Aufzeichner darf den Test nie beeinflussen
            pass
        return orig(*args, **kwargs)
    return _metadaten(w, orig)""", """def deck_wickeln(name, orig):
    \"\"\"Aufzeichner der deckenden Tests: je Aufruf Test, Funktion, Eingabe (vor dem Aufruf) und Ergebnis — genau so
    geschrieben, wie die Sonde Beobachtungen schreibt (wert/knapp). Ausnahmen gehen unverändert an den Test.\"\"\"
    def w(*args, **kwargs):
        eintrag = {'test': AKTUELL[0], 'f': name, 'args': eingabe_text(args, kwargs), 'erg': None}
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
        return v
    return _metadaten(w, orig)""")
ersetze(P, """def main():
    modus = REQ.get('modus', 'beobachten')""", """def main():
    global KAPPE, RAND_KAPPE, FORM_KAPPE
    REQ.clear()
    REQ.update(json.load(open(sys.argv[1], encoding='utf-8')))
    KAPPE, RAND_KAPPE, FORM_KAPPE = REQ.get('kappe') or 8, REQ.get('rand_kappe') or 16, REQ.get('form_kappe') or 16
    if '/werk' not in sys.path:
        sys.path.insert(0, '/werk')
    modus = REQ.get('modus', 'beobachten')""")

# ---------------------------------------------------------------- Organ: einheitliche Deckungsregel
O = R / 'biotop/organe/verhaltensvergleich.py'
s = O.read_text()
a0 = s.index('def _muster_erfuellt(')
a1 = s.index('def _testdatei_pfade(')
s = s[:a0] + '''def deckung(abweichungen: list[str], aufrufe: list[dict], argumente: dict[str, str],
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


''' + s[a1:]
alt_d = s[s.index('def deckung(abweichungen: list[str], aufrufe: list[dict], argumente: dict[str, str],\n            alt: dict | None = None'):]
alt_d = alt_d[:alt_d.index('def _testdatei_pfade(')]
s = s.replace(alt_d, '')
s = s.replace('''        argumente = {**(neu.get("argumente") or {}), **(alt.get("argumente") or {})}
        decke = deckung(roh["abweichungen"], d.get("aufrufe") or [], argumente, a, n)''',
              '''        decke = deckung(roh["abweichungen"], d.get("aufrufe") or [], neu.get("argumente") or {}, n)''')
s = s.replace('''            "eingaben": {k: (alt.get("argumente") or {}).get(k.partition("@")[0]) for k in r["ungedeckt"][:10]},''',
              '''            "eingaben": {k: (neu.get("argumente") or {}).get(k) for k in r["ungedeckt"][:10]},''')
s = s.replace('''  Form) — bei @mutation und @nach_ruecksetzung zusätzlich im selben Aufrufmuster (dasselbe Objekt, an Ort und Stelle
  geändert, erneut gerufen). Beweis ist der aufgezeichnete Aufruf am Kandidaten, nicht der Quelltext des Tests:''',
              '''  Form) und dasselbe Ergebnis bekommt, das die Sonde am Kandidaten sah. Beweis ist der aufgezeichnete Aufruf am
  Kandidaten, nicht der Quelltext des Tests:''')
assert s.count('def deckung(') == 1 and '_muster_erfuellt' not in s, (s.count('def deckung('),)
O.write_text(s)
print('Deckungsregel vereinheitlicht')
