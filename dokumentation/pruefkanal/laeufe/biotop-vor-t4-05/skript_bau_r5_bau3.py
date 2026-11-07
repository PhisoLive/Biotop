"""Behebungsrunde 5 — Umbau Teil 3 (alles oder nichts): Eingrenzung per Halbierung (Kammer-Zeitlimit: höchstens wenige
Lastläufe statt einer je Funktion), gescheiterte Eingrenzung = Enthaltung (nie „Werk“), Nachspiel nutzt eine Rauschmessung
der Stufe 2 aus dem Nachweis, kan: deque/object/ungekürzte Darstellung, Tor4Fehler als LaufFehler, Wirt: Abbruch ohne
gerufene Funktion bleibt Messgerätausfall."""
import sys
from pathlib import Path

R = Path(sys.argv[1] if len(sys.argv) > 1 else '/root/biotop')
AENDERUNGEN = {}


def ers(pfad, alt, neu):
    AENDERUNGEN.setdefault(pfad, []).append((alt, neu))


V = 'biotop/kern/py/verhalten.py'
ers(V, "        if name in TRANSPARENT or (NUR[0] is not None and name != NUR[0]):\n",
    "        if name in TRANSPARENT or (NUR[0] is not None and name not in NUR[0]):\n")
ers(V, "NUR = [None]            # Behebungsrunde 5: Eingrenzung — nur diese Funktion greift ein\n",
    "NUR = [None]            # Behebungsrunde 5: Eingrenzung — nur diese Funktionen greifen ein (Menge)\n")
ers(V, ('__BEREICH__', 'def _last_versuch(ns, k, modus, f=None):\n', 'def _vorlage_starten(ns, k):\n'), r'''def _last_versuch(ns, k, modus, menge=None):
    """Ein Lastlauf mit Sonde ('voll'), ohne jeden Eingriff ('ohne') oder nur mit dem Eingriff der Funktionen `menge`."""
    IM_LAST[0] = set()
    if modus == 'ohne':
        TIEFE[0] += 1
    elif modus == 'nur':
        NUR[0] = set(menge or ())
    ergebnis = _korpus_einmal(ns, k)
    return {'ergebnis': ergebnis, 'gerufen': sorted(IM_LAST[0])}


def _eingrenzen_in_vorlage(ns, k):
    """Läuft in der Vorlage (Zustand vor dem Lastlauf); jeder Versuch in einem eigenen Kindprozess. Halbierung: je
    Auslöser etwa 1 + 2·log2(n) Lastläufe; höchstens sechs unabhängige Auslöser, danach bleibt der Rest eingreifend."""
    voll = _im_kind(lambda: _last_versuch(ns, k, 'voll'))
    ohne = _im_kind(lambda: _last_versuch(ns, k, 'ohne'))
    if not isinstance(voll, dict) or not isinstance(ohne, dict) or 'ergebnis' not in ohne or 'ergebnis' not in voll:
        return {'__vorlagenfehler': f'Kindprozess ohne Ergebnis (voll={voll!r:.80}, ohne={ohne!r:.80})'}
    if ohne['ergebnis'] != 'ok':
        return {'ohne_sonde': ohne['ergebnis'], 'schuldig': []}
    kandidaten = list(voll.get('gerufen') or [])
    schuldig, laeufe = [], 2

    def faellt(menge):
        nonlocal laeufe
        laeufe += 1
        v = _im_kind(lambda: _last_versuch(ns, k, 'nur', menge))
        return not (isinstance(v, dict) and v.get('ergebnis') == 'ok')
    for _ in range(6):
        rest = [f for f in kandidaten if f not in schuldig]
        if not rest or not faellt(rest):
            break
        menge = rest
        while len(menge) > 1:
            h = len(menge) // 2
            if faellt(menge[:h]):
                menge = menge[:h]
            elif faellt(menge[h:]):
                menge = menge[h:]
            else:
                break                                   # nur zusammen lösen sie den Abbruch aus — die Menge bleibt
        schuldig += menge
    return {'ohne_sonde': 'ok', 'schuldig': schuldig, 'laeufe': laeufe}


''')
ers(V, r'''    befund = _vorlage_befehl(vorlage, b'e') or {}
    if befund.get('ohne_sonde') != 'ok':
        LAST_OHNE_SONDE[k] = befund.get('ohne_sonde') or str(befund.get('__vorlagenfehler') or 'unbekannt')
        return
    schuldig = befund.get('schuldig') or []
    grund = f'Last {k} bricht unter der Sonde ab ({ergebnis}), ohne Sonde läuft sie'
    if not schuldig:
        schuldig, grund = list(LAST_AUFRUFE[k]), grund + ' — Auslöser nicht auf eine Funktion eingrenzbar'
''', r'''    befund = _vorlage_befehl(vorlage, b'e') or {}
    if befund.get('ohne_sonde') not in (None, 'ok'):
        LAST_OHNE_SONDE[k] = befund['ohne_sonde']          # bricht auch ohne Sonde ab: Verhalten des Werks
        return
    schuldig = befund.get('schuldig') or []
    grund = f'Last {k} bricht unter der Sonde ab ({ergebnis}), ohne Sonde läuft sie'
    if befund.get('ohne_sonde') is None:
        # Eingrenzung gescheitert: nie als Verhalten des Werks werten — alle Funktionen dieser Last enthalten sich.
        schuldig, grund = [], f'Last {k} bricht unter der Sonde ab ({ergebnis}); Eingrenzung gescheitert: ' \
                              f'{str(befund.get("__vorlagenfehler") or "keine Antwort der Vorlage")[:160]}'
    if not schuldig:
        schuldig, grund = list(LAST_AUFRUFE[k]), grund + ' — Auslöser nicht auf eine Funktion eingrenzbar'
''')
ers(V, r'''        roh = repr(x)
        if fehlend is not None and _ADRESSE.search(roh):
            fehlend.append(f'{type(x).__qualname__}: Objekt ohne erfassbare Daten (Darstellung nur mit Adresse)')
        return {'__objekt': type(x).__qualname__, 'repr': _ADRESSE.sub(' at 0x…', roh)[:200]}
''', r'''        if type(x) is object:
            return '__objekt_leer'                     # reiner Platzhalter ohne Daten
        if type(x).__name__ == 'deque' and type(x).__module__ == 'collections':
            return {'__deque': [kan(v, anc, t + 1, fehlend) for v in x], 'maxlen': x.maxlen}
        roh = repr(x)
        if fehlend is not None and _ADRESSE.search(roh):
            fehlend.append(f'{type(x).__qualname__}: Objekt ohne erfassbare Daten (Darstellung nur mit Adresse)')
        # ungekürzt (Behebungsrunde 5): knapp() kürzt den ganzen Text mit Prüfsumme, nichts fällt still weg
        return {'__objekt': type(x).__qualname__, 'repr': _ADRESSE.sub(' at 0x…', roh)}
''')

O = 'biotop/organe/verhaltensvergleich.py'
ers(O, r'''        gerufen = (alt.get("last_aufrufe") or {}).get(last)
        if gerufen is None:
''', r'''        gerufen = (alt.get("last_aufrufe") or {}).get(last)
        if not gerufen:
''')

N = 'biotop/nachspiel.py'
ers(N, r'''    rauschen_herkunft = "aus dem versiegelten Vorspann-Nachweis (Stufe 1)"
    if tausch["_referenzlast_laufzeit"] and rauschen_stufe2:
''', r'''    stufe_nachweis = nachweis.get("laufzeit_stufe") or 1
    rauschen_herkunft = f"aus dem versiegelten Vorspann-Nachweis (Stufe {stufe_nachweis})"
    # Behebungsrunde 5: trägt der Nachweis schon die Rauschmessung der Stufe 2 (Läufe mit dem neuen Vorspann), gilt sie.
    if tausch["_referenzlast_laufzeit"] and rauschen_stufe2 and stufe_nachweis != 2:
''')

T = 'biotop/tor4.py'
ers(T, '''class Tor4Fehler(RuntimeError):
''', '''class Tor4Fehler(L.LaufFehler):
''')


def main():
    neu_inhalt, fehler = {}, []
    for pfad, liste in AENDERUNGEN.items():
        text = (R / pfad).read_text()
        for alt, neu in liste:
            if isinstance(alt, tuple):
                _, start, ende_vor = alt
                if text.count(start) != 1 or text.count(ende_vor) != 1:
                    fehler.append(f'{pfad}: Bereich {start[:30]!r}/{ende_vor[:30]!r} {text.count(start)}×/{text.count(ende_vor)}×')
                    continue
                i, j = text.index(start), text.index(ende_vor)
                text = text[:i] + neu + text[j:]
            else:
                n = text.count(alt)
                if n != 1:
                    fehler.append(f'{pfad}: Anker {n}×: {alt[:90]!r}')
                    continue
                text = text.replace(alt, neu)
        neu_inhalt[pfad] = text
    if fehler:
        print('ABBRUCH — nichts geschrieben:\n' + '\n'.join(fehler))
        sys.exit(2)
    for pfad, text in neu_inhalt.items():
        (R / pfad).write_text(text)
    print(f'geschrieben: {len(neu_inhalt)} Dateien, {sum(len(v) for v in AENDERUNGEN.values())} Ersetzungen')


if __name__ == '__main__':
    main()
