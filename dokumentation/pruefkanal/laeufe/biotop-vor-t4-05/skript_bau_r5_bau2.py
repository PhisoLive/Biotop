"""Behebungsrunde 5 vor T4 — Umbau Teil 2 (alles oder nichts), auf dem Stand nach r5_bau.py.
- Entscheidung 3: Eingrenzung des Sondenausfalls von einem UNBERÜHRTEN Zustand aus (os.fork: eine Vorlage vor dem
  Lastlauf, jeder Versuch in einem eigenen Kindprozess) — ein Wiederholungslauf im selben Prozess erbte den vom ersten
  Lauf veränderten Modulzustand des Werks (eigener Befund beim Bau, vor jedem Test).
- Entscheidung 1: Beispiele (pack/unpack) mit allen Datenattributen, auch Slots.
- tor4: Endstand fehlt → Tor4Fehler statt TypeError."""
import sys
from pathlib import Path

R = Path(sys.argv[1] if len(sys.argv) > 1 else '/root/biotop')
AENDERUNGEN = {}


def ers(pfad, alt, neu):
    AENDERUNGEN.setdefault(pfad, []).append((alt, neu))


V = 'biotop/kern/py/verhalten.py'
ALT_REKORDER_BIS_KORPUS = ('_REKORDER = (', "def main():\n    global KAPPE, RAND_KAPPE, FORM_KAPPE\n")
NEU_KORPUS = r'''def _korpus_einmal(ns, k):
    try:
        ns[k]()
        return 'ok'
    except BaseException as e:  # noqa: B902
        return 'Fehler:' + type(e).__name__


def _im_kind(fn):
    """fn() in einem Kindprozess (os.fork) — vom Zustand des Aufrufers aus, danach verworfen. Rückgabe: JSON-Wert."""
    r, w = os.pipe()
    pid = os.fork()
    if pid == 0:                                            # Kind
        os.close(r)
        try:
            daten = json.dumps(fn()).encode()
        except BaseException as e:  # noqa: B902
            daten = json.dumps({'__kindfehler': repr(e)[:300]}).encode()
        while daten:
            daten = daten[os.write(w, daten):]
        os._exit(0)
    os.close(w)
    teile = []
    while True:
        b = os.read(r, 65536)
        if not b:
            break
        teile.append(b)
    os.close(r)
    os.waitpid(pid, 0)
    return json.loads(b''.join(teile) or b'null')


def _last_versuch(ns, k, modus, f=None):
    """Ein Lastlauf mit Sonde ('voll'), ohne jeden Eingriff ('ohne') oder nur mit dem Eingriff von f ('nur')."""
    IM_LAST[0] = set()
    if modus == 'ohne':
        TIEFE[0] += 1
    elif modus == 'nur':
        NUR[0] = f
    ergebnis = _korpus_einmal(ns, k)
    return {'ergebnis': ergebnis, 'gerufen': sorted(IM_LAST[0])}


def _eingrenzen_in_vorlage(ns, k):
    """Läuft in der Vorlage (Zustand vor dem Lastlauf): jeder Versuch in einem eigenen Kindprozess."""
    voll = _im_kind(lambda: _last_versuch(ns, k, 'voll')) or {}
    ohne = _im_kind(lambda: _last_versuch(ns, k, 'ohne')) or {}
    if ohne.get('ergebnis') != 'ok':
        return {'ohne_sonde': ohne.get('ergebnis'), 'schuldig': [], 'voll': voll.get('ergebnis')}
    schuldig = []
    for f in (voll.get('gerufen') or [])[:60]:
        v = _im_kind(lambda f=f: _last_versuch(ns, k, 'nur', f)) or {}
        if v.get('ergebnis') != 'ok':
            schuldig.append(f)
    return {'ohne_sonde': 'ok', 'schuldig': schuldig, 'voll': voll.get('ergebnis'), 'gerufen': voll.get('gerufen')}


def _vorlage_starten(ns, k):
    """Vorlage: ein Kindprozess mit dem Zustand VOR dem Lastlauf, der auf einen Befehl wartet ('x' beenden,
    'e' eingrenzen). Kostet nichts, solange die Last unter der Sonde läuft."""
    befehl_r, befehl_w = os.pipe()
    antwort_r, antwort_w = os.pipe()
    pid = os.fork()
    if pid == 0:                                            # Vorlage
        os.close(befehl_w)
        os.close(antwort_r)
        b = os.read(befehl_r, 1)
        if b == b'e':
            try:
                daten = json.dumps(_eingrenzen_in_vorlage(ns, k)).encode()
            except BaseException as e:  # noqa: B902
                daten = json.dumps({'__vorlagenfehler': repr(e)[:300]}).encode()
            while daten:
                daten = daten[os.write(antwort_w, daten):]
        os._exit(0)
    os.close(befehl_r)
    os.close(antwort_w)
    return pid, befehl_w, antwort_r


def _vorlage_befehl(vorlage, befehl):
    pid, befehl_w, antwort_r = vorlage
    os.write(befehl_w, befehl)
    os.close(befehl_w)
    teile = []
    while True:
        b = os.read(antwort_r, 65536)
        if not b:
            break
        teile.append(b)
    os.close(antwort_r)
    os.waitpid(pid, 0)
    return json.loads(b''.join(teile)) if teile else None


def _korpus_lauf(ns, k, eingrenzen):
    """Behebungsrunde 5 (Entscheidung 3, Review 04 Nr. 4): ein Sondenausfall trifft nur die betroffene Funktion. Bricht
    eine Bereichslast unter der Sonde ab, sucht die Vorlage (Zustand vor dem Lastlauf) in Kindprozessen, ob die Last
    ohne jeden Eingriff der Sonde läuft, und wenn ja, welche Funktion allein durch ihre Einwicklung den Abbruch auslöst.
    Diese Funktionen stehen in `sonde_ausfall` und werden durchlässig; der Wirt beobachtet die Vorgeneration danach neu
    (mit denselben durchlässigen Funktionen auf beiden Seiten), die betroffenen Funktionen enthalten sich, der Lauf geht
    weiter. Bricht die Last auch ohne Sonde ab, ist das Verhalten des Werks (`last_ohne_sonde`) — beobachtet wie bisher."""
    vorlage = None
    if eingrenzen and k.startswith('last_') and hasattr(os, 'fork'):
        try:
            vorlage = _vorlage_starten(ns, k)
        except OSError:
            vorlage = None
    IM_LAST[0] = set()
    ergebnis = _korpus_einmal(ns, k)
    LAST_AUFRUFE[k] = sorted(IM_LAST[0])
    IM_LAST[0] = None
    beob['korpus:' + k] = ergebnis
    if vorlage is None:
        return
    if ergebnis == 'ok' or not LAST_AUFRUFE[k]:
        _vorlage_befehl(vorlage, b'x')
        return
    befund = _vorlage_befehl(vorlage, b'e') or {}
    if befund.get('ohne_sonde') != 'ok':
        LAST_OHNE_SONDE[k] = befund.get('ohne_sonde') or str(befund.get('__vorlagenfehler') or 'unbekannt')
        return
    schuldig = befund.get('schuldig') or []
    grund = f'Last {k} bricht unter der Sonde ab ({ergebnis}), ohne Sonde läuft sie'
    if not schuldig:
        schuldig, grund = list(LAST_AUFRUFE[k]), grund + ' — Auslöser nicht auf eine Funktion eingrenzbar'
    for f in schuldig:
        sonde_ausfall[f] = grund
    TRANSPARENT.update(schuldig)


'''
ers(V, ('__BEREICH__',) + ALT_REKORDER_BIS_KORPUS, NEU_KORPUS)
ers(V, r'''    if _instanz(x) and not hasattr(type(x), '__slots__') and type(x).__module__ not in ('builtins',):
        return {'__obj': f'{type(x).__module__}:{type(x).__qualname__}',
                'z': {k: pack(v, t + 1) for k, v in vars(x).items()}}
''', r'''    if _instanz(x) and type(x).__module__ not in ('builtins',):
        # Behebungsrunde 5 (Entscheidung 1): alle Datenattribute, auch Slots der ganzen Hierarchie
        return {'__obj': f'{type(x).__module__}:{type(x).__qualname__}',
                'z': {k: pack(v, t + 1) for k, v in _felder(x).items()}}
''')
ers(V, r'''    if '__obj' in x:
        cls = _klasse(x['__obj'])
        o = cls.__new__(cls)
        o.__dict__.update({k: unpack(v) for k, v in x['z'].items()})
        return o
''', r'''    if '__obj' in x:
        cls = _klasse(x['__obj'])
        o = cls.__new__(cls)
        _felder_setzen(o, {k: unpack(v) for k, v in x['z'].items()})
        return o
''')

T = 'biotop/tor4.py'
ers(T, '''    end = L.letzte_angenommene(con, lauf_id)
    tmp = Path(tempfile.mkdtemp(prefix="tor4-"))''', '''    end = L.letzte_angenommene(con, lauf_id)
    if end is None:
        raise Tor4Fehler(f"Lauf {lauf_id}: keine angenommene Generation — kein Endstand")
    tmp = Path(tempfile.mkdtemp(prefix="tor4-"))''')


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
