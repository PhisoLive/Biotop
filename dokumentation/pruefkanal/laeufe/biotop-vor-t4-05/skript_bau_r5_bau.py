"""Behebungsrunde 5 vor T4 — Umbau (alles oder nichts: jeder Anker wird geprüft, bevor eine Datei geschrieben wird).
Entscheidungen Chat-Claude 24.09.2026 zum Review 04. Aufruf: python r5_bau.py /root/biotop"""
import sys
from pathlib import Path

R = Path(sys.argv[1] if len(sys.argv) > 1 else '/root/biotop')
AENDERUNGEN = {}   # pfad → [(alt, neu)]


def ers(pfad, alt, neu):
    AENDERUNGEN.setdefault(pfad, []).append((alt, neu))


# ======================================================================== kern/py/verhalten.py
V = 'biotop/kern/py/verhalten.py'
ers(V, r'''teilweise = {}          # Behebungsrunde 4: je Funktion gezählte Teil-Enthaltungen (Iterator-Kappe, Iterator-Objekt)
''', r'''teilweise = {}          # Behebungsrunde 4: je Funktion gezählte Teil-Enthaltungen (Iterator-Kappe, Iterator-Objekt)
unvollstaendig = {}     # Behebungsrunde 5 (Entscheidung 1): je Funktion unvollständige Erfassungen (Grund → Anzahl)
sonde_ausfall = {}      # Behebungsrunde 5 (Entscheidung 3): Funktion → Grund (ihre Einwicklung ließ eine Bereichslast abbrechen)
TRANSPARENT = set()     # Behebungsrunde 5: durchlässige Funktionen (keine Beobachtung, kein Eingriff)
NUR = [None]            # Behebungsrunde 5: Eingrenzung — nur diese Funktion greift ein
IM_LAST = [None]        # Behebungsrunde 5: Funktionen, in die die Sonde während der laufenden Bereichslast eingriff
LAST_AUFRUFE = {}       # Behebungsrunde 5: Bereichslast → Funktionen, in die die Sonde eingriff
LAST_OHNE_SONDE = {}    # Behebungsrunde 5: Bereichslast → Abbruch, der auch ohne jeden Eingriff der Sonde auftritt (Werk)
''')

KAN_NEU = r'''_HEAPTYPE = 1 << 9          # Py_TPFLAGS_HEAPTYPE: in Python definierte Klasse (nicht C)


def _zustand_unabhaengig(x):
    """Unabhängige Aufzählung der Datenattribute (Behebungsrunde 5, Entscheidung 1): der Zustand, den Python selbst zum
    Kopieren liest — object.__getstate__ (__dict__ und belegte Slots der ganzen Hierarchie, verschleierte Namen
    aufgelöst). Rückgabe (namen, grund); grund gesetzt, wenn der Zustand nicht aufzählbar ist."""
    try:
        s = object.__getstate__(x)
    except Exception as e:  # noqa: BLE001
        return set(), f'Zustand nicht aufzählbar ({type(e).__name__})'
    if s is None:
        return set(), None
    if isinstance(s, tuple) and len(s) == 2:
        return set(s[0] or {}) | set(s[1] or {}), None
    if isinstance(s, dict):
        return set(s), None
    return set(), f'Zustand in unbekannter Form ({type(s).__name__})'


def _pruefen_vollstaendig(x, erfasst, fehlend):
    """Vollständigkeitsprüfung nach jedem Erfassen eines Objekts (Behebungsrunde 5, Entscheidung 1): fehlt ein
    Datenattribut in der Erfassung, steht das in `fehlend` — der Wirt zählt es als Enthaltung, nie als
    „0 Abweichungen, tragfähig“."""
    if fehlend is None:
        return
    namen, grund = _zustand_unabhaengig(x)
    if grund:
        fehlend.append(f'{type(x).__qualname__}: {grund}')
    rest = sorted(namen - set(erfasst))
    if rest:
        fehlend.append(f'{type(x).__qualname__}: nicht erfasst {rest[:5]}')


def kan(x, anc=None, t=0, fehlend=None):
    """Kanonische Form eines beobachteten Werts. `fehlend` (Liste): Befunde der Vollständigkeitsprüfung (Entscheidung 1)."""
    anc = set() if anc is None else anc
    if x is None or type(x) in (bool, str, int):
        return x
    if isinstance(x, enum.Enum):
        return {'__enum': type(x).__qualname__ + '.' + x.name}
    if isinstance(x, (str, int)):                  # Unterklasse: Wert; eigene Attribute geprüft
        _pruefen_vollstaendig(x, (), fehlend)
        return str(x) if isinstance(x, str) else int(x)
    if isinstance(x, float):
        if type(x) is not float:
            _pruefen_vollstaendig(x, (), fehlend)
        if math.isnan(x):
            return '__NaN'
        if math.isinf(x):
            return '__Inf' if x > 0 else '__-Inf'
        return '__-0' if x == 0 and math.copysign(1, x) < 0 else float(x)
    if isinstance(x, (bytes, bytearray)):
        # Behebungsrunde 5 (Entscheidung 1): ganz — knapp() kürzt lange Texte mit Prüfsumme, nichts fällt weg
        return {'__bytes': x.hex(), 'typ': type(x).__name__}
    if isinstance(x, Verfaelscht):
        return '__verfaelscht'
    if isinstance(x, os.PathLike):
        # Behebungsrunde 5 (Entscheidung 1, Review 04 Nr. 10): ein Pfad ist ein Wert (os.fspath), nicht seine
        # Zwischenspeicher
        try:
            p = os.fspath(x)
        except Exception:  # noqa: BLE001
            p = None
        if isinstance(p, (str, bytes)):
            return {'__pfad': p if isinstance(p, str) else p.hex(), 'typ': type(x).__qualname__}
    if id(x) in anc:
        return '__zyklus'
    if t > 12:
        if fehlend is not None:
            fehlend.append(f'{type(x).__qualname__}: tiefer als 12 Ebenen, nicht erfasst')
        return '__tief'
    anc.add(id(x))
    try:
        if isinstance(x, list):
            if type(x) is not list:
                _pruefen_vollstaendig(x, (), fehlend)
            return [kan(v, anc, t + 1, fehlend) for v in x]
        if isinstance(x, tuple):
            r = {'__tupel': [kan(v, anc, t + 1, fehlend) for v in x]}
            if type(x) is not tuple:
                r['typ'] = type(x).__qualname__
                _pruefen_vollstaendig(x, (), fehlend)
            return r
        if isinstance(x, dict):
            if type(x) is not dict:
                _pruefen_vollstaendig(x, (), fehlend)
            if all(isinstance(k, str) for k in x):
                return {'__dict': {k: kan(v, anc, t + 1, fehlend) for k, v in x.items()}}
            paare = [[kan(k, anc, t + 1, fehlend), kan(v, anc, t + 1, fehlend)] for k, v in x.items()]
            return {'__dictk': sorted(paare, key=lambda p: json.dumps(p[0], sort_keys=True, default=str))}
        if isinstance(x, (set, frozenset)):
            if type(x) not in (set, frozenset):
                _pruefen_vollstaendig(x, (), fehlend)
            return {'__set': sorted((kan(v, anc, t + 1, fehlend) for v in x),
                                    key=lambda v: json.dumps(v, sort_keys=True, default=str))}
        if isinstance(x, BaseException):
            return {'__fehler': type(x).__name__, 'meldung': _ADRESSE.sub(' at 0x…', str(x))[:200]}
        if isinstance(x, (types.FunctionType, types.BuiltinFunctionType, types.MethodType, type, types.ModuleType,
                          functools.partial)) or (callable(x) and callable(getattr(x, '__wrapped__', None))):
            return '__fn'
        if (dataclasses.is_dataclass(x) and not isinstance(x, type)) or _instanz(x):
            # Behebungsrunde 5 (Entscheidung 1, Review 04 Nr. 2/3): alle Datenattribute — __dict__ und die Slots der
            # ganzen Klassenhierarchie unter ihren gespeicherten (auch verschleierten) Namen —, danach die Prüfung.
            felder = _felder(x)
            _pruefen_vollstaendig(x, felder, fehlend)
            return {'__klasse': type(x).__qualname__,
                    'felder': {k: kan(v, anc, t + 1, fehlend) for k, v in sorted(felder.items())}}
        roh = repr(x)
        if fehlend is not None and _ADRESSE.search(roh):
            fehlend.append(f'{type(x).__qualname__}: Objekt ohne erfassbare Daten (Darstellung nur mit Adresse)')
        return {'__objekt': type(x).__qualname__, 'repr': _ADRESSE.sub(' at 0x…', roh)[:200]}
    finally:
        anc.discard(id(x))


def text_von(x, fehlend=None):
    return json.dumps(kan(x, None, 0, fehlend), sort_keys=True, ensure_ascii=False, default=str)
'''
ers(V, ('__BEREICH__', 'def kan(x, anc=None, t=0):\n',
        "def text_von(x):\n    return json.dumps(kan(x), sort_keys=True, ensure_ascii=False, default=str)\n", None), KAN_NEU)

ers(V, r'''    if inspect.isgenerator(v) or type(v).__module__ in ('builtins', 'itertools', 'collections', '_collections', 'csv'):
        return 'iter'
    return 'objekt'
''', r'''    # Behebungsrunde 5 (Entscheidung 3, Review 04 Nr. 4): ersetzt werden nur echte Iteratoren — Generatoren und
    # Iteratoren der Standardbibliothek ohne Datenattribute. Objekte mit Attributen (csv.DictReader: fieldnames,
    # line_num; Dateien; Cursor) und groupby (seine Gruppen hängen am Ausgangsiterator) bleiben unverändert.
    if inspect.isgenerator(v):
        return 'iter'
    if (type(v).__module__ in ('builtins', 'itertools', 'collections', '_collections')
            and type(v).__name__ not in ('groupby', '_grouper') and not _hat_datenattribute(v)):
        return 'iter'
    return 'objekt'


def _hat_datenattribute(v):
    if getattr(v, '__dict__', None):
        return True
    for n in dir(type(v)):
        if n.startswith('_'):
            continue
        d = inspect.getattr_static(type(v), n, None)
        if isinstance(d, (property, types.MemberDescriptorType, types.GetSetDescriptorType)):
            return True
    return False
''')

ers(V, r'''def _teil(name, art):
    if name:
        d = teilweise.setdefault(name, {})
        d[art] = d.get(art, 0) + 1
''', r'''def _teil(name, art):
    if name:
        d = teilweise.setdefault(name, {})
        d[art] = d.get(art, 0) + 1


def _unvoll(name, gruende):
    """Behebungsrunde 5 (Entscheidung 1): gezählte Enthaltung einer Funktion — ihre Erfassung war unvollständig."""
    if not name:
        return
    d = unvollstaendig.setdefault(name, {})
    for g in gruende:
        d[g] = d.get(g, 0) + 1
''')

WERT_NEU = r'''def wert(f, name=None):
    """Ruft f(). Rückgabe {text, roh | fehler, inhaltlich}. Generatoren und eingebaute Iteratoren ohne Datenattribute
    werden begrenzt ausgelesen; `roh` ist dann ein Iterator über dieselben Elemente (der Aufrufer merkt nichts).
    Behebungsrunde 5 (Entscheidung 1): jede Erfassung wird auf Vollständigkeit geprüft. Ein Iterator-Objekt (Elemente
    nicht erfasst), ein gekappter Iterator und ein Objekt mit nicht erfasstem Datenattribut sind je eine gezählte
    Enthaltung der Funktion (`unvollstaendig`)."""
    fehl = []

    def melden(text):
        if name and fehl:
            _unvoll(name, fehl)
        return text

    try:
        v = f()
    except BaseException as e:  # noqa: B902 — jede Ausnahme ist ein beobachtetes Verhalten
        return {'text': 'Fehler:' + type(e).__name__, 'fehler': e, 'inhaltlich': False}
    art = _iter_art(v)
    if art == 'async' and inspect.iscoroutine(v):
        r = _koroutine_ausfuehren(v)
        if r is not None:
            ergebnis, fehler = r
            if fehler is not None:
                return {'text': 'Fehler:' + type(fehler).__name__, 'roh': _fertig(None, fehler), 'inhaltlich': False}
            try:
                text = text_von({'__async': ergebnis}, fehl)
            except Exception as e:  # noqa: BLE001
                return {'text': '__unkanonisch:' + type(e).__name__, 'roh': _fertig(ergebnis, None), 'inhaltlich': False}
            if name:
                inhalt[name] = inhalt.get(name, 0) + 1
            return {'text': melden(text), 'roh': _fertig(ergebnis, None), 'inhaltlich': True}
    if art == 'async':
        if name:
            unvergleichbar[name] = unvergleichbar.get(name, 0) + 1
        return {'text': '__async', 'roh': v, 'inhaltlich': False}
    if art == 'objekt':
        _teil(name, 'iterator_objekt')
        fehl.append(f'{type(v).__qualname__}: Iterator-Objekt, Elemente nicht erfasst')
        try:
            text = text_von({'__iterator_objekt': v}, fehl)
        except Exception as e:  # noqa: BLE001
            melden(None)
            return {'text': '__unkanonisch:' + type(e).__name__, 'roh': v, 'inhaltlich': False}
        if name:
            inhalt[name] = inhalt.get(name, 0) + 1
        return {'text': melden(text), 'roh': v, 'inhaltlich': True}
    if art == 'iter':
        elemente, fehler = [], None
        try:
            for x in itertools.islice(v, ITER_KAPPE + 1):
                elemente.append(x)
        except BaseException as e:  # noqa: B902
            fehler = e
        mehr = fehler is None and len(elemente) > ITER_KAPPE
        if mehr:
            _teil(name, 'iterator_gekappt')         # Review 03 Nr. 16: ab Element ITER_KAPPE + 1 unsichtbar — gezählt
            fehl.append(f'Iterator nach {ITER_KAPPE} Elementen gekappt, der Rest nicht erfasst')
        try:
            text = text_von({'__iter': elemente[:ITER_KAPPE], 'ende': ('Fehler:' + type(fehler).__name__) if fehler
                             else ('mehr' if mehr else 'ende')}, fehl)
        except Exception as e:  # noqa: BLE001
            text = '__unkanonisch:' + type(e).__name__
        ok = not text.startswith('__unkanonisch')
        if name and ok:
            inhalt[name] = inhalt.get(name, 0) + 1
        return {'text': melden(text), 'roh': _weiter(elemente, v if mehr else None, fehler), 'inhaltlich': ok}
    try:
        text = text_von(v, fehl)
    except Exception as e:  # noqa: BLE001
        return {'text': '__unkanonisch:' + type(e).__name__, 'roh': v, 'inhaltlich': False}
    if name:
        inhalt[name] = inhalt.get(name, 0) + 1
    return {'text': melden(text), 'roh': v, 'inhaltlich': True}


'''
ers(V, ('__BEREICH__', 'def wert(f, name=None):\n',
        None, '# ---------------------------------------------------------------- Zustand der Eingaben\n'), WERT_NEU)

ers(V, r'''def _slotnamen(x):
    namen = []
    for k in type(x).__mro__:
        s = k.__dict__.get('__slots__', ())
        if isinstance(s, str):
            s = (s,)
        namen += [n for n in s if n not in ('__dict__', '__weakref__') and n not in namen]
    return namen
''', r'''def _slotnamen(x):
    """Slots über die ganze Klassenhierarchie — die Member-Deskriptoren der in Python definierten Klassen, also mit den
    gespeicherten (auch verschleierten, `_Klasse__name`) Namen (Behebungsrunde 5, Review 04 Nr. 2, 3)."""
    namen = []
    for k in type(x).__mro__:
        if not (getattr(k, '__flags__', 0) & _HEAPTYPE):
            continue
        for n, d in list(vars(k).items()):
            if isinstance(d, types.MemberDescriptorType) and n not in namen:
                namen.append(n)
    return namen
''')
ers(V, r'''            functools.partial)) and not callable(getattr(x, '__wrapped__', None))
''', r'''            functools.partial)) and not callable(getattr(x, '__wrapped__', None)) and not isinstance(x, os.PathLike)
''')
ers(V, r'''def _zustand_obs(schl, args, kwargs):
    """Zustand der veränderlichen Argumente NACH dem Aufruf als eigene Beobachtung (Review 02 Nr. 2)."""
    if any(_veraenderlich(v) for v in list(args) + list(kwargs.values())):
        try:
            beob[schl + '>args'] = knapp(text_von([list(args), kwargs]))
        except Exception:  # noqa: BLE001
            beob[schl + '>args'] = '__unkanonisch'
''', r'''def _zustand_obs(schl, args, kwargs, name=None):
    """Zustand der veränderlichen Argumente NACH dem Aufruf als eigene Beobachtung (Review 02 Nr. 2); die Erfassung wird
    auf Vollständigkeit geprüft (Behebungsrunde 5, Entscheidung 1)."""
    if any(_veraenderlich(v) for v in list(args) + list(kwargs.values())):
        fehl = []
        try:
            beob[schl + '>args'] = knapp(text_von([list(args), kwargs], fehl))
        except Exception:  # noqa: BLE001
            beob[schl + '>args'] = '__unkanonisch'
        if name and fehl:
            _unvoll(name, fehl)
''')
ers(V, "        _zustand_obs(schl, args, kwargs)\n", "        _zustand_obs(schl, args, kwargs, name)\n")
ers(V, "            _zustand_obs(k, args, kwargs)\n", "            _zustand_obs(k, args, kwargs, name)\n")
ers(V, r'''    def w(*args, **kwargs):
        if LAST[0]:
            erreicht[name] = erreicht.get(name, 0) + 1
        if TIEFE[0] > 0:
            return orig(*args, **kwargs)
        i = zaehler[name] = zaehler.get(name, -1) + 1
''', r'''    def w(*args, **kwargs):
        if LAST[0]:
            erreicht[name] = erreicht.get(name, 0) + 1
        if name in TRANSPARENT or (NUR[0] is not None and name != NUR[0]):
            return orig(*args, **kwargs)        # Behebungsrunde 5 (Entscheidung 3): durchlässig bzw. Eingrenzung
        if TIEFE[0] > 0:
            return orig(*args, **kwargs)
        if IM_LAST[0] is not None:
            IM_LAST[0].add(name)
        i = zaehler[name] = zaehler.get(name, -1) + 1
''')
ers(V, r'''        # Lastaufruf: die Sonde hat kein Argument verändert — Muster gewöhnlich (Entscheidung Chat-Claude 3,
        # Behebungsrunde 4: Merkmale nicht veränderter Argumente gehören nicht zum Muster).
        erst = muster(f'{name}#{i}', args, kwargs, orig, name, kl=[])
''', r'''        # Behebungsrunde 5 (Entscheidung 7, Review 04 Nr. 9): der Lastaufruf trägt die Formmerkmale seiner Eingabe —
        # sonst deckt ein Test mit gewöhnlicher Eingabe eine Regression, die nur Tab/Zeilenumbruch der Last zeigt.
        kl = [m for m in _klassen_sicher(lambda: klassen_von(_gebunden(orig, args, kwargs, ohne_erstes)))
              if m in FORM_MERKMALE or m == '__unbestimmt']
        erst = muster(f'{name}#{i}', args, kwargs, orig, name, kl=kl)
''')
ers(V, r'''def main():
    global KAPPE, RAND_KAPPE, FORM_KAPPE
''', r'''def _zusicherung_faellt(report, datei):
    """Behebungsrunde 5 (Entscheidung 2, Review 04 Nr. 1): fällt eine Zusicherung im Test? AssertionError (auch das
    umgeschriebene assert) oder ein pytest-Fehlschlag („Failed: DID NOT RAISE …“, pytest.fail), ausgelöst in der
    Testdatei selbst (Absturzstelle des Berichts). Gemessen (proben/VORPROBE-E2.txt, pytest 8.3.3 in der Kammer): eine
    Ausnahme aus Werkcode meldet die Werkdatei, ein assert im Werkcode ebenso — beides hält nichts fest."""
    crash = getattr(getattr(report, 'longrepr', None), 'reprcrash', None)
    if crash is None:
        return False
    meldung = str(getattr(crash, 'message', '') or '')
    ort = os.path.basename(str(getattr(crash, 'path', '') or ''))
    return meldung.startswith(('AssertionError', 'Failed')) and ort == os.path.basename(datei)


_REKORDER = ('beob', 'argtext', 'zaehler', 'zaehler_rand', 'zaehler_form', 'beispiele', 'musterkarte', 'kopien',
             'inhalt', 'unvergleichbar', 'instanzen', 'teilweise', 'unvollstaendig', 'erreicht', 'KONSTRUKTION')


def _rekorder_sichern():
    g = globals()
    return {n: copy.deepcopy(g[n]) for n in _REKORDER}


def _rekorder_setzen(stand):
    g = globals()
    for n, v in stand.items():
        g[n].clear()
        g[n].update(copy.deepcopy(v))


def _korpus_einmal(ns, k):
    try:
        ns[k]()
        return 'ok'
    except BaseException as e:  # noqa: B902
        return 'Fehler:' + type(e).__name__


def _korpus_lauf(ns, k, eingrenzen):
    """Behebungsrunde 5 (Entscheidung 3, Review 04 Nr. 4): ein Sondenausfall trifft nur die betroffene Funktion. Bricht
    eine Bereichslast unter der Sonde ab, läuft sie aber ohne jeden Eingriff der Sonde, sucht die Sonde die Funktion,
    deren Einwicklung allein den Abbruch auslöst (je Funktion ein Lauf, in dem nur sie eingreift), macht sie
    durchlässig und wiederholt die Last. Die Funktion steht in `sonde_ausfall` (der Wirt zählt sie als Enthaltung), der
    Lauf geht weiter. Bricht die Last auch ohne Sonde ab, ist das Verhalten des Werks — beobachtet wie bisher."""
    stand = _rekorder_sichern()
    IM_LAST[0] = set()
    ergebnis = _korpus_einmal(ns, k)
    gerufen = sorted(IM_LAST[0])
    IM_LAST[0] = None
    LAST_AUFRUFE[k] = gerufen
    if ergebnis == 'ok' or not eingrenzen or not k.startswith('last_') or not gerufen:
        beob['korpus:' + k] = ergebnis
        return
    nach = _rekorder_sichern()
    _rekorder_setzen(stand)
    TIEFE[0] += 1
    try:
        ohne = _korpus_einmal(ns, k)
    finally:
        TIEFE[0] -= 1
    if ohne != 'ok':
        _rekorder_setzen(nach)
        LAST_OHNE_SONDE[k] = ohne
        beob['korpus:' + k] = ergebnis
        return
    schuldig = []
    for f in gerufen[:60]:
        _rekorder_setzen(stand)
        NUR[0] = f
        try:
            if _korpus_einmal(ns, k) != 'ok':
                schuldig.append(f)
        finally:
            NUR[0] = None
    grund = f'Last {k} bricht unter der Sonde ab ({ergebnis}), ohne Sonde läuft sie'
    if not schuldig:
        schuldig, grund = list(gerufen), grund + ' — Auslöser nicht auf eine Funktion eingrenzbar'
    for f in schuldig:
        sonde_ausfall[f] = grund
    TRANSPARENT.update(schuldig)
    _rekorder_setzen(stand)
    IM_LAST[0] = set()
    beob['korpus:' + k] = _korpus_einmal(ns, k)
    LAST_AUFRUFE[k] = sorted(IM_LAST[0])
    IM_LAST[0] = None


def main():
    global KAPPE, RAND_KAPPE, FORM_KAPPE
''')
ers(V, r'''                # Behebungsrunde 4 (Review 03 Nr. 2): festhalten heißt „die Zusicherung im Test fällt“ — ein Fehler in
                # Aufbau/Abbau (Fixture) oder ein Skip ist 'fehler', kein 'fail'.
                if report.when == 'call' and ZUSTAND.get(tid) != 'fehler':
                    ZUSTAND[tid] = 'pass' if report.outcome == 'passed' else ('fail' if report.outcome == 'failed' else 'fehler')
                elif report.when != 'call' and report.outcome != 'passed':
                    ZUSTAND[tid] = 'fehler'
''', r'''                # Behebungsrunde 4 (Review 03 Nr. 2): ein Fehler in Aufbau/Abbau (Fixture) oder ein Skip ist 'fehler'.
                # Behebungsrunde 5 (Entscheidung 2, Review 04 Nr. 1): festhalten heißt „eine Zusicherung im Test fällt“ —
                # jede andere Ausnahme (etwa aus Werkcode, dem ein verfälschtes Ergebnis gereicht wurde) ist 'fehler'.
                if report.when == 'call' and ZUSTAND.get(tid) != 'fehler':
                    if report.outcome == 'passed':
                        ZUSTAND[tid] = 'pass'
                    elif report.outcome == 'failed' and _zusicherung_faellt(report, datei):
                        ZUSTAND[tid] = 'fail'
                    else:
                        ZUSTAND[tid] = 'fehler'
                elif report.when != 'call' and report.outcome != 'passed':
                    ZUSTAND[tid] = 'fehler'
''')
ers(V, r'''    LAST[0] = True
    for k in korpus:
        try:
            ns[k]()
            beob['korpus:' + k] = 'ok'
        except BaseException as e:  # noqa: B902
            beob['korpus:' + k] = 'Fehler:' + type(e).__name__
    LAST[0] = False
''', r'''    TRANSPARENT.update(REQ.get('transparent') or [])
    LAST[0] = True
    for k in korpus:
        # Behebungsrunde 5 (Entscheidung 3): eingegrenzt wird nur beim ersten Blick auf die Vorgeneration (ohne Vorgabe
        # `transparent`); danach bekommen beide Stände dieselben durchlässigen Funktionen.
        _korpus_lauf(ns, k, eingrenzen=REQ.get('transparent') is None)
    LAST[0] = False
''')
ers(V, "            beob[k] = knapp(text_von(instanz(n)))\n",
    "            fehl = []\n            beob[k] = knapp(text_von(instanz(n), fehl))\n            if fehl:\n"
    "                _unvoll(f'{n}.__init__', fehl)\n")
ers(V, "           'korpus_erweitert': ERWEITERT[0], 'nicht_ladbar': nicht_ladbar, 'erreicht': erreicht, 'teilweise': teilweise}\n",
    "           'korpus_erweitert': ERWEITERT[0], 'nicht_ladbar': nicht_ladbar, 'erreicht': erreicht, 'teilweise': teilweise,\n"
    "           'unvollstaendig': unvollstaendig, 'sonde_ausfall': sonde_ausfall, 'transparent': sorted(TRANSPARENT),\n"
    "           'last_aufrufe': LAST_AUFRUFE, 'last_ohne_sonde': LAST_OHNE_SONDE}\n")

# ======================================================================== kern/ts/verhalten-runner.mjs
T = 'biotop/kern/ts/verhalten-runner.mjs'
ers(T, "const teilweise = {};\nfunction teil(name, art) { if (name) { const d = teilweise[name] ??= {}; d[art] = (d[art] ?? 0) + 1; } }\n",
    r'''const teilweise = {};
function teil(name, art) { if (name) { const d = teilweise[name] ??= {}; d[art] = (d[art] ?? 0) + 1; } }
// Behebungsrunde 5 (Entscheidung 1): gezählte Enthaltung je Funktion, wenn die Erfassung unvollständig war
// (Iterator-Objekt: Elemente nicht erfasst; Iterator nach ITER_KAPPE Elementen gekappt).
const unvollstaendig = {};
function unvoll(name, g) { if (name) { const d = unvollstaendig[name] ??= {}; d[g] = (d[g] ?? 0) + 1; } }
// Behebungsrunde 5 (Entscheidung 3): welche Funktionen jede Bereichslast rief — bricht sie an der Vorgeneration unter
// der Sonde ab, enthalten sich genau diese (im Wirt), nicht der ganze Kandidat.
const lastAufrufe = {};
let imLast = null;
''')
ers(T, "    teil(name, 'iterator_objekt');\n",
    "    teil(name, 'iterator_objekt');\n    unvoll(name, 'Iterator-Objekt, Elemente nicht erfasst');\n")
ers(T, "    if (mehr) teil(name, 'iterator_gekappt');\n",
    "    if (mehr) { teil(name, 'iterator_gekappt'); unvoll(name, 'Iterator nach ' + ITER_KAPPE + ' Elementen gekappt, der Rest nicht erfasst'); }\n")
ers(T, "globalThis.__vvAufzeichnen = (name, args, call) => {\n  if (tiefe > 0) return call(...args);\n",
    r'''// Behebungsrunde 5 (Entscheidung 7, Review 04 Nr. 9): der Lastaufruf trägt die Formmerkmale seiner Eingabe.
function formMerkmale(args) { try { return klassenVon(args).filter(m => FORM_MERKMALE.has(m)); } catch { return ['__unbestimmt']; } }
globalThis.__vvAufzeichnen = (name, args, call) => {
  if (tiefe > 0) return call(...args);
  if (imLast) imLast.add(name);
''')
ers(T, "  const erst = muster(`${name}#${i}`, args, call, name, []);      // Lastaufruf: kein Argument verändert — gewöhnlich\n",
    "  const erst = muster(`${name}#${i}`, args, call, name, formMerkmale(args));\n")
ers(T, r'''  for (const k of korpus) {
    try { await ref[k](); beob['korpus:' + k] = 'ok'; }
    catch (e) { beob['korpus:' + k] = 'Fehler:' + (e?.constructor?.name ?? 'unbekannt'); }
  }
''', r'''  for (const k of korpus) {
    imLast = new Set();
    try { await ref[k](); beob['korpus:' + k] = 'ok'; }
    catch (e) { beob['korpus:' + k] = 'Fehler:' + (e?.constructor?.name ?? 'unbekannt'); }
    lastAufrufe[k] = [...imLast].sort();
    imLast = null;
  }
''')
ers(T, "         kopien, inhalt, unvergleichbar, teilweise, korpus_erweitert: ERWEITERT, ...(req.beispiele ? {} : {beispiele})};\n",
    "         kopien, inhalt, unvergleichbar, teilweise, unvollstaendig, last_aufrufe: lastAufrufe, korpus_erweitert: ERWEITERT,\n"
    "         ...(req.beispiele ? {} : {beispiele})};\n")

# ======================================================================== kern/ts/deckung.mjs
D = 'biotop/kern/ts/deckung.mjs'
ers(D, r'''    for (const t of n.tests ?? []) {
      const haken = Object.values(t.hooks ?? {}).some(s => s === 'fail');
      zustand[path.basename(t.id.split('::')[0]) + '::' + t.id.split('::').slice(1).join('::')] = haken ? 'fehler' : t.state;
    }
''', r'''    // Behebungsrunde 5 (Entscheidung 2, Review 04 Nr. 1): nur eine fallende Zusicherung hält fest.
    for (const t of n.tests ?? []) {
      const haken = Object.values(t.hooks ?? {}).some(s => s === 'fail');
      let st = haken ? 'fehler' : t.state;
      if (st === 'fail' && !zusicherungFaellt(t)) st = 'fehler';
      zustand[path.basename(t.id.split('::')[0]) + '::' + t.id.split('::').slice(1).join('::')] = st;
    }
''')
ers(D, "export function deckung(req) {\n",
    r'''// Behebungsrunde 5 (Entscheidung 2): festhalten heißt „eine Zusicherung im Test fällt“ — AssertionError (expect/assert),
// ausgelöst in der Testdatei (erste Werkstelle im Stapel unter tests/); eine Ausnahme aus Werkcode, dem ein verfälschtes
// Ergebnis gereicht wurde, hält nichts fest.
function zusicherungFaellt(t) {
  const errs = t.errors ?? [];
  if (!errs.length) return false;
  return errs.every(e => {
    const name = e?.name ?? e?.nameStr ?? '';
    const stapel = String(e?.stackStr ?? e?.stack ?? '');
    const ort = stapel.match(/\/werk\/((?:src|tests|dist)\/[^\s():]+):\d+:\d+/)?.[1] ?? '';
    return name === 'AssertionError' && ort.startsWith('tests/');
  });
}
export function deckung(req) {
''')

# ======================================================================== organe/verhaltensvergleich.py
O = 'biotop/organe/verhaltensvergleich.py'
ers(O, "- Vom Kandidaten mitgebrachte Tests decken nicht (Entscheidung 4, in aegis.pruefen: `behoben` ohne sie).\n\"\"\"\n",
    "- Vom Kandidaten mitgebrachte Tests decken nicht (Entscheidung 4, in aegis.pruefen: `behoben` ohne sie).\n\n"
    "Behebungsrunde 5 vor T4 (Entscheidungen Chat-Claude 24.09.2026, Review 04 — Klassen statt Fälle):\n"
    "- Vollständigkeitsprüfung (Entscheidung 1): nach jedem Erfassen eines Objekts prüft die Sonde, ob alle Datenattribute\n"
    "  erfasst sind; fehlt eines (auch: Iterator-Objekt, gekappter Iterator), enthält sich die Funktion (`unvollstaendig`)\n"
    "  und das Urteil sagt nie „0 Abweichungen, tragfähig“ (Enthaltung, aegis stellt zurück).\n"
    "- Sondenausfall nur der betroffenen Funktion (Entscheidung 3): `sonde_ausfall`, ihre Beobachtungen enthalten sich.\n"
    "- Verfälschungskappe (Entscheidung 4): hängt jede ungedeckte Abweichung an einer ausgelassenen Probe: Enthaltung.\n"
    "- Lastaufrufe tragen die Formmerkmale ihrer Eingabe (Entscheidung 7).\n\"\"\"\n")
ers(O, r'''    # Behebungsrunde 4 (R4-3, Review 03 Nr. 3): eine Bereichslast, die unter der Sonde an der VORGENERATION abbricht, hat
    # die Sonde gestört (ohne Sonde lief sie — die Messung der Vorgeneration verlangt einen Laufzeitwert je Bereich):
    # Messgerätausfall statt stiller Lücke.
    b_alt = alt.get("beobachtungen") or {}
    abbruch = sorted(k for k, w in b_alt.items() if k.startswith("korpus:last_") and str(w).startswith("Fehler"))
    if abbruch:
        raise SondeAusgefallen("Referenzlast bricht unter der Sonde an der Vorgeneration ab ("
                               + ", ".join(f"{k} {b_alt.get(k)}" for k in abbruch[:3])
                               + ") — die Sonde stört die Last; ohne Sonde lief sie")
    gleich = dict(signaturen=alt.get("signaturen"), beispiele=alt.get("beispiele"), konstruktion=alt.get("konstruktion"),
                  korpus_erweitert=korpus_erweitert)
''', r'''    # Behebungsrunde 5 (Entscheidung 3, Review 04 Nr. 4): ein Sondenausfall trifft nur die betroffene Funktion. Bricht
    # eine Bereichslast unter der Sonde an der Vorgeneration ab, grenzt die Python-Sonde die Funktion ein, deren
    # Einwicklung den Abbruch auslöst (sonde_ausfall), und macht sie durchlässig. Die Vorgeneration wird dann frisch mit
    # denselben durchlässigen Funktionen beobachtet (die Eingrenzung hat Last und Modulzustand mehrfach durchlaufen); die
    # betroffenen Funktionen enthalten sich, der Lauf geht weiter.
    ausfall = dict(alt.get("sonde_ausfall") or {})
    durchlaessig = sorted(alt.get("transparent") or [])
    if ausfall:
        alt = beobachten(werk, {}, referenzlast, module, bereiche, korpus_erweitert=korpus_erweitert,
                         transparent=durchlaessig)
        if not alt.get("gueltig"):
            raise SondeAusgefallen(f"Sonde an der Vorgeneration (durchlässig: {durchlaessig[:3]}) ausgefallen "
                                   f"({alt.get('art')}): {str(alt.get('grund'))[:300]}")
    b_alt = alt.get("beobachtungen") or {}
    # Bricht eine Bereichslast an der Vorgeneration trotzdem ab, enthalten sich die Funktionen, die diese Last rief —
    # nicht der ganze Kandidat (TypeScript: die Sonde grenzt nicht selbst ein). Bricht sie auch ohne Sonde ab
    # (`last_ohne_sonde`, Python), ist das Verhalten des Werks und wird beobachtet wie bisher. Ohne Angabe, welche
    # Funktionen die Last rief, bleibt es beim Messgerätausfall (Runde 4).
    werk_abbruch = alt.get("last_ohne_sonde") or {}
    for k in sorted(k for k, w in b_alt.items() if k.startswith("korpus:last_") and str(w).startswith("Fehler")):
        last = k.split(":", 1)[1]
        if last in werk_abbruch:
            continue
        gerufen = (alt.get("last_aufrufe") or {}).get(last)
        if gerufen is None:
            raise SondeAusgefallen(f"Referenzlast bricht unter der Sonde an der Vorgeneration ab ({k} {b_alt.get(k)}) — "
                                   f"die Sonde stört die Last; ohne Sonde lief sie")
        for f in gerufen:
            ausfall.setdefault(f, f"{k} bricht unter der Sonde ab ({b_alt.get(k)}), Auslöser nicht eingegrenzt")
    gleich = dict(signaturen=alt.get("signaturen"), beispiele=alt.get("beispiele"), konstruktion=alt.get("konstruktion"),
                  korpus_erweitert=korpus_erweitert, transparent=durchlaessig)
''')
ers(O, r'''    a, n = dict(b1), dict(neu.get("beobachtungen") or {})
    for k in instabil:
        a.pop(k, None)
        n.pop(k, None)
''', r'''    a, n = dict(b1), dict(neu.get("beobachtungen") or {})
    for k in instabil:
        a.pop(k, None)
        n.pop(k, None)
    # Behebungsrunde 5 (Entscheidung 3): die Beobachtungen einer Funktion mit Sondenausfall enthalten sich — beide Seiten.
    for k in list(a) + list(n):
        mf = _modul_funktion(k)
        if mf and f"{mf[0]}:{mf[1]}" in ausfall:
            a.pop(k, None)
            n.pop(k, None)
    # Behebungsrunde 5 (Entscheidung 1): Funktionen mit unvollständiger Erfassung (an einer der beiden Seiten).
    unvoll: dict[str, set[str]] = {}
    for seite in (alt, neu):
        for f, gr in (seite.get("unvollstaendig") or {}).items():
            unvoll.setdefault(f, set()).update(gr or {})
''')
ers(O, r'''    nicht_deckbar = zustandsabhaengig(roh["abweichungen"], alt.get("kopien") or {}, neu.get("kopien") or {})
    if roh["abweichungen"]:
''', r'''    nicht_deckbar = zustandsabhaengig(roh["abweichungen"], alt.get("kopien") or {}, neu.get("kopien") or {})
    ausgelassen: list = []
    if roh["abweichungen"]:
''')
ers(O, "        haelt, ausgelassen = {}, []\n", "        haelt = {}\n")
ers(O, "    r = vergleichen(a, n, gedeckt=set(decke))\n", r'''    r = vergleichen(a, n, gedeckt=set(decke))
    # Behebungsrunde 5 (Entscheidung 4, Review 04 Nr. 6): hängt JEDE ungedeckte Abweichung an einer ausgelassenen
    # Verfälschungsprobe (Kappe), ist sie nicht beurteilt — Enthaltung mit Grund, gezählt. Eine Abweichung, die auch
    # ohne die Kappe ungedeckt bliebe, lehnt weiter ab.
    kappe_offen: list[str] = []
    if ausgelassen and r["ungedeckt"]:
        ausgel = set(ausgelassen)

        def _an_kappe(k: str) -> bool:
            f = _deckungsfunktion(k)
            merk = sorted(set(muster.get(_aufruf(k)) or [])) or [""]
            return bool(f) and any((f, _verfaelschungsart(k), c) in ausgel for c in merk)
        if all(_an_kappe(k) for k in r["ungedeckt"]):
            kappe_offen = list(r["ungedeckt"])
''')
ers(O, "    enthaltungen = {x: _enthaltungsgrund(x, a, n, alt, neu, eigene, instabil_fn) for x in alle if x not in beobachtet}\n",
    r'''    # Behebungsrunde 5 (Entscheidungen 1 und 3): unvollständig erfasste Funktionen und Funktionen mit Sondenausfall
    # gelten nicht als beobachtet — gezählte Enthaltungen mit Grund.
    beobachtet = {x for x in beobachtet if x not in unvoll and x not in ausfall}
    enthaltungen = {x: _enthaltungsgrund(x, a, n, alt, neu, eigene, instabil_fn) for x in alle if x not in beobachtet}
    for x in list(enthaltungen):
        if x in ausfall:
            enthaltungen[x] = "Sondenausfall: " + ausfall[x]
        elif x in unvoll:
            enthaltungen[x] = "unvollständig erfasst: " + sorted(unvoll[x])[0]
''')
ers(O, r'''             "teilweise": {s: {**(alt.get("teilweise") or {}).get(s, {}), **(neu.get("teilweise") or {}).get(s, {})}
                           for s in sorted(set(alt.get("teilweise") or {}) | set(neu.get("teilweise") or {}))}}
''', r'''             "teilweise": {s: {**(alt.get("teilweise") or {}).get(s, {}), **(neu.get("teilweise") or {}).get(s, {})}
                           for s in sorted(set(alt.get("teilweise") or {}) | set(neu.get("teilweise") or {}))},
             # Behebungsrunde 5 (Entscheidungen 1 und 3)
             "unvollstaendig": {f: sorted(g) for f, g in sorted(unvoll.items())},
             "sonde_ausfall": dict(sorted(ausfall.items()))}
    if kappe_offen:
        return {**basis, **extra, "ausgefuehrt": True, "geurteilt": False, "tragfaehig": False, "enthaltung": True,
                "grund_art": "verfaelschungskappe",
                "grund": (f"Enthaltung (Entscheidung 4): {len(kappe_offen)} ungedeckte Abweichung(en) hängen an "
                          f"{deckung_zaehlung.get('ausgelassen')} ausgelassenen Verfälschungsproben (Kappe "
                          f"{VERFAELSCHUNG_KAPPE} Läufe je Kandidat) — nicht beurteilt ({x_von_y} Funktionen beobachtet)"),
                "beobachtungen": r["beobachtungen"], "anzahl_abweichungen": len(r["abweichungen"]),
                "abweichungen": r["abweichungen"][:20], "ungedeckt": r["ungedeckt"][:20], "ungedeckt_alle": r["ungedeckt"],
                "gedeckt": decke, "korpus": alt.get("korpus"), "eingewickelt": eingewickelt,
                "deckende_tests": tests, "deckung_zaehlung": deckung_zaehlung}
    if r["tragfaehig"] and unvoll:
        beispiel = "; ".join(f"{f}: {sorted(g)[0]}" for f, g in sorted(unvoll.items())[:3])
        return {**basis, **extra, "ausgefuehrt": True, "geurteilt": False, "tragfaehig": False, "enthaltung": True,
                "grund_art": "unvollstaendig_erfasst",
                "grund": (f"Enthaltung (Entscheidung 1): {len(unvoll)} Funktion(en) unvollständig erfasst ({beispiel}) — "
                          f"keine Aussage „{len(r['abweichungen'])} Abweichungen, tragfähig“ ({x_von_y} Funktionen "
                          f"beobachtet)"),
                "beobachtungen": r["beobachtungen"], "anzahl_abweichungen": len(r["abweichungen"]),
                "abweichungen": r["abweichungen"][:20], "ungedeckt": [], "gedeckt": decke, "korpus": alt.get("korpus"),
                "eingewickelt": eingewickelt, "deckende_tests": tests, "deckung_zaehlung": deckung_zaehlung}
''')
ers(O, "                  \"teilweise\", \"eigene_tests_ausgeschlossen\",\n",
    "                  \"teilweise\", \"eigene_tests_ausgeschlossen\", \"unvollstaendig\", \"sonde_ausfall\", \"enthaltung\",\n")
ers(O, "               konstruktion: dict | None = None, korpus_erweitert: bool = True) -> dict:\n",
    "               konstruktion: dict | None = None, korpus_erweitert: bool = True,\n"
    "               transparent: list | None = None) -> dict:\n")
ers(O, "                                                   \"konstruktion\": konstruktion, \"korpus_erweitert\": korpus_erweitert},\n",
    "                                                   \"konstruktion\": konstruktion, \"korpus_erweitert\": korpus_erweitert,\n"
    "                                                   **({\"transparent\": list(transparent)} if transparent is not None else {})},\n")

# ======================================================================== organe/aegis.py
A = 'biotop/organe/aegis.py'
ers(A, r'''        for n, q in _testquellen(inhalt).items():
            if alt.get(n) != q:
                out.add(f"{Path(p).name}::{n}")
    return out
''', r'''        for n, q in _testquellen(inhalt).items():
            if alt.get(n) != q:
                out.add(f"{Path(p).name}::{n}")
    return out


def _testbasis(t: str) -> str:
    """Testkennung ohne Parametrisierung: 'datei::name[p]' → 'datei::name' (Behebungsrunde 5, Review 04 Nr. 16)."""
    return re.sub(r"\[.*\]$", "", t)


def ist_eigener_test(t: str, eigene: set[str]) -> bool:
    """Behebungsrunde 5 (Entscheidung 8, Review 04 Nr. 16): gehört die ausgeführte Testkennung `t` zu einem eigenen Test
    des Kandidaten? Nach Testkennung einschließlich Parametrisierung — Python 'datei::name[p]' gehört zu 'datei::name';
    TypeScript test.each: der Syntaxbaum kennt die Vorlage ('fall %s', '$wert'), ausgeführt wird der eingesetzte Name.
    Sonst unterläuft ein parametrisierter Test Entscheidung 4."""
    if t in eigene or _testbasis(t) in eigene:
        return True
    datei, _, name = t.partition("::")
    for e in eigene:
        ed, _, en = e.partition("::")
        if ed == datei and re.search(r"%[sdifjoc#%]|\$\w+", en):
            muster = re.sub(r"%[sdifjoc#%]|\\\$\w+", ".*", re.escape(en))
            if re.fullmatch(muster, name):
                return True
    return False
''')
ers(A, r'''    eigene = eigene_tests(werk, tests_kandidat, vertrag_dateien_kandidat)
    behoben = (fb - fk) - eigene
    eigene_ausgeschlossen = sorted((fb - fk) & eigene)
''', r'''    eigene = eigene_tests(werk, tests_kandidat, vertrag_dateien_kandidat)
    # Behebungsrunde 5 (Entscheidung 8): nach Testkennung einschließlich Parametrisierung
    behoben = {t for t in (fb - fk) if not ist_eigener_test(t, eigene)}
    eigene_ausgeschlossen = sorted(t for t in (fb - fk) if ist_eigener_test(t, eigene))
''')
ers(A, r'''    if not vv["tragfaehig"]:
        u = {**u, "ok": False, "grund": "Verhaltensvergleich: " + vv["grund"]}
''', r'''    if vv.get("enthaltung"):
        # Behebungsrunde 5 (Entscheidungen 1 und 4): der Verhaltensvergleich enthält sich — unvollständig erfasst bzw.
        # Verfälschungskappe. Gezählt (Neutralzähler, oben); keine Annahme, keine Ablehnung, kein Gedächtniseintrag.
        return fertig(ZURUECKGESTELLT, "Verhaltensvergleich enthält sich — zurückgestellt: " + str(vv.get("grund"))[:400],
                      mess, dateien_final, basis_paar)
    if not vv["tragfaehig"]:
        u = {**u, "ok": False, "grund": "Verhaltensvergleich: " + vv["grund"]}
''')
ers(A, r'''    basis_paar = messgeraet.messen(werk, bereiche, paket, referenzlast, dateien=testbestand)
    mess = messgeraet.messen(werk, bereiche, paket, referenzlast, dateien={**code, **testbestand_mit_vertraegen})
''', r'''    # Behebungsrunde 5 (Entscheidung 8, Review 04 Nr. 15): an der Stufe der Laufzeitgrenze (Stufe 2) — gespeicherte Maße,
    # Rauschtoleranz und gepaarte Messung haben dieselbe Stufe.
    ref_messung = referenzlast_laufzeit or referenzlast
    basis_paar = messgeraet.messen(werk, bereiche, paket, ref_messung, dateien=testbestand)
    mess = messgeraet.messen(werk, bereiche, paket, ref_messung, dateien={**code, **testbestand_mit_vertraegen})
''')
ers(A, '            masse = {**masse, "_dateien": dateien_final or {}, "_basis_paar": basis_paar, "_urteil_f2": urteil["mass"]}\n',
    '            masse = {**masse, "_dateien": dateien_final or {}, "_basis_paar": basis_paar, "_urteil_f2": urteil["mass"],\n'
    '                     "laufzeit_stufe": urteil.get("laufzeit_stufe")}\n')
ers(A, "                if absturz or _nennt_vertrag(inhalt, n, verf, con, werk_id, bereich, vertrag_dateien_kandidat):\n",
    "                # Behebungsrunde 5: parametrisierte Tests ('name[p]') am Funktionsnamen prüfen und aufnehmen\n"
    "                if absturz or _nennt_vertrag(inhalt, _testbasis(n), verf, con, werk_id, bereich, vertrag_dateien_kandidat):\n")
ers(A, "                    g = _anhaengen(alt_code, inhalt, gueltig) if gueltig else None\n",
    "                    g = _anhaengen(alt_code, inhalt, {_testbasis(x) for x in gueltig}) if gueltig else None\n")
ers(A, "                g = nur_funktionen(inhalt, gueltig) if gueltig else None\n",
    "                g = nur_funktionen(inhalt, {_testbasis(x) for x in gueltig}) if gueltig else None\n")

# ======================================================================== lauf.py
L = 'biotop/lauf.py'
ers(L, r'''    mess = messgeraet.messen(Path(werk["pfad"]), bereiche, paket, ref)
    if not mess["gueltig"]:
        raise LaufFehler(f"Ausgangsmessung ungültig: {mess['grund']}")
''', r'''    # Behebungsrunde 5 (Entscheidung 8, Review 04 Nr. 15): das eingefrorene Ausgangsmaß an der Stufe der Laufzeitgrenze.
    ref2 = _referenzlast(werk["name"], paket, 2)
    mess = messgeraet.messen(Path(werk["pfad"]), bereiche, paket, ref2 or ref)
    if not mess["gueltig"]:
        raise LaufFehler(f"Ausgangsmessung ungültig: {mess['grund']}")
''')
ers(L, r'''    mess = masseichung.anwenden(mess, eichung_mass)
    mess["kernmass_f2"] = messgeraet.kernmass_f2(mess)
''', r'''    mess = masseichung.anwenden(mess, eichung_mass)
    mess["kernmass_f2"] = messgeraet.kernmass_f2(mess)
    mess["laufzeit_stufe"] = 2 if ref2 else 1
''')
ers(L, '''"tausch_quelle": verf["quelle"], "bereiche": bereiche, "paket": paket, "referenzlast": f"{werk['name']}.py",''',
    '''"tausch_quelle": verf["quelle"], "bereiche": bereiche, "paket": paket, "referenzlast": f"{werk['name']}.py",
            "laufzeit_stufe": 2 if ref2 else 1,''')
ers(L, r'''    testbestand = {p: i for p, i in dateien.items() if p.startswith("tests/")}
    basis_paar = messgeraet.messen(pfad, bereiche, paket, ref, dateien=testbestand)
    mess = messgeraet.messen(pfad, bereiche, paket, ref, dateien=dateien)
''', r'''    testbestand = {p: i for p, i in dateien.items() if p.startswith("tests/")}
    # Behebungsrunde 5 (Entscheidung 8): Generalprobe an der Stufe der Laufzeitgrenze — gespeicherte Maße, Toleranz und
    # gepaarte Messung haben dieselbe Stufe (Rückfall Stufe 1 nur ohne Stufe 2; der Vorspann verweigert das).
    ref_lz = tausch.get("_referenzlast_laufzeit") or ref
    basis_paar = messgeraet.messen(pfad, bereiche, paket, ref_lz, dateien=testbestand)
    mess = messgeraet.messen(pfad, bereiche, paket, ref_lz, dateien=dateien)
''')
ers(L, r'''    mess = masseichung.anwenden(mess, tausch.get("_masseichung"))
    wirkungskreis = set()
''', r'''    mess = masseichung.anwenden(mess, tausch.get("_masseichung"))
    mess["laufzeit_stufe"] = basis_paar["laufzeit_stufe"] = 2 if tausch.get("_referenzlast_laufzeit") else 1
    wirkungskreis = set()
''')
ers(L, r'''    ref_lz = tausch.get("_referenzlast_laufzeit") or ref
    zusammenfassung["_laufzeit_stufe"] = 2 if tausch.get("_referenzlast_laufzeit") else 1
''', r'''    zusammenfassung["_laufzeit_stufe"] = 2 if tausch.get("_referenzlast_laufzeit") else 1
''')
ers(L, r'''    paket, bereiche = mass["paket"], mass["bereiche"]
    ref = _referenzlast(werk["name"], paket)
    gens = [''', r'''    paket, bereiche = mass["paket"], mass["bereiche"]
    ref = _referenzlast(werk["name"], paket, 2) or _referenzlast(werk["name"], paket)   # Behebungsrunde 5: Stufe der Maße
    gens = [''')

# ======================================================================== organe/vorspann.py
S = 'biotop/organe/vorspann.py'
ers(S, r'''    # (zehnfache Eingabegröße je Bereich). Fehlt sie, ist die Stufe-1-Last Rückfall — das steht im Nachweis.
    ref2 = L._referenzlast(werk['name'], paket, 2)
    r['laufzeit_stufe'] = 2 if ref2 else 1
''', r'''    # (zehnfache Eingabegröße je Bereich). Behebungsrunde 5 (Entscheidung 6, Review 04 Nr. 8): fehlt sie, verweigert der
    # Vorspann den Lauf — kein stiller Rückfall auf Stufe 1.
    ref2 = L._referenzlast(werk['name'], paket, 2)
    if not ref2:
        raise ValueError(f"Vergleichslast Stufe 2 fehlt ({werk['name']}.stufe2.* bzw. {paket}.stufe2.* im Kern) — "
                         f"Entscheidung Chat-Claude 6: ohne Stufe 2 kein Lauf")
    r['laufzeit_stufe'] = 2
''')
ers(S, r'''    if ref2:
        r['rauschen'] = eichung.rauschmessung(con, lauf_id, werk['id'], pfad, bereiche, paket, ref2, eichung.laufzeit_einmal)
        dauer = max(r['rauschen'].get('kammerlauf_s') or [0.0])
        if dauer >= STUFE2_KAMMERLAUF_S:
            raise ValueError(f'Vergleichslast Stufe 2: ein Kammerlauf dauerte {dauer:.1f} s (Grenze {STUFE2_KAMMERLAUF_S} s, '
                             f'Entscheidung Chat-Claude 1) — Referenzlast Stufe 2 verkleinern')
    else:
        r['rauschen'] = eichung.rauschmessung(con, lauf_id, werk['id'], pfad, bereiche, paket, ref)
''', r'''    r['rauschen'] = eichung.rauschmessung(con, lauf_id, werk['id'], pfad, bereiche, paket, ref2, eichung.laufzeit_einmal)
    dauer = max(r['rauschen'].get('kammerlauf_s') or [0.0])
    if dauer >= STUFE2_KAMMERLAUF_S:
        raise ValueError(f'Vergleichslast Stufe 2: ein Kammerlauf dauerte {dauer:.1f} s (Grenze {STUFE2_KAMMERLAUF_S} s, '
                         f'Entscheidung Chat-Claude 1) — Referenzlast Stufe 2 verkleinern')
''')
ers(S, "    r['basis'] = messgeraet.messen(pfad, bereiche, paket, ref)\n",
    "    r['basis'] = messgeraet.messen(pfad, bereiche, paket, ref2)      # Behebungsrunde 5 (Entscheidung 8): Stufe 2\n")
ers(S, "    tausch['_masseichung'] = r['masseichung']\n",
    "    tausch['_masseichung'] = r['masseichung']\n"
    "    tausch['_referenzlast_laufzeit'] = ref2          # Behebungsrunde 5 (Entscheidung 8): Eichproben an Stufe 2\n")

# ======================================================================== organe/eichproben.py
E = 'biotop/organe/eichproben.py'
ers(E, r'''        u = aegis.pruefen(db, lauf_id, werk_id, kid, werk, paket, bereiche, bstrassen, basis, ausgang, ref, tausch,
                          probe_ohne_modell=True, probe_angriff=angriff)
''', r'''        # Behebungsrunde 5 (Entscheidung 8, Review 04 Nr. 14): dieselbe Stufe wie der Lauf (Laufzeit an Stufe 2)
        u = aegis.pruefen(db, lauf_id, werk_id, kid, werk, paket, bereiche, bstrassen, basis, ausgang, ref, tausch,
                          probe_ohne_modell=True, probe_angriff=angriff,
                          referenzlast_laufzeit=(tausch or {}).get('_referenzlast_laufzeit'))
''')

# ======================================================================== Stufe-2-Last versandwerk
W = 'biotop/kern/referenzlast/versandwerk-t3-02.stufe2.mjs'
ers(W, "const W = { eingang: 60, tarife: 25, planung: 30, bericht: 40, zahlen: 400 };\n",
    "// Behebungsrunde 5 (Entscheidung 6): eingang wie Stufe 1 „gemessen gewählt“ — bemessen und geeicht, bis eingang nicht\n"
    "// mehr sperrt (proben/STUFE2-EICHUNG: W 60 sperrte 3 von 8 Rauschmessungen, W 240 0 von 8, längster Kammerlauf 12,3 s).\n"
    "const W = { eingang: 240, tarife: 25, planung: 30, bericht: 40, zahlen: 400 };\n")

# ======================================================================== __main__.py
M = 'biotop/__main__.py'
ers(M, '    s = sub.add_parser("vorspann"); s.add_argument("lauf", type=int)\n',
    '    s = sub.add_parser("vorspann"); s.add_argument("lauf", type=int)\n'
    '    s = sub.add_parser("tor4"); s.add_argument("lauf", type=int); s.add_argument("--altlasten", required=True)\n')
ers(M, '        elif a.cmd == "vorspann":\n            _p(L.vorspann.ausfuehren(con, a.lauf))\n',
    '        elif a.cmd == "vorspann":\n            _p(L.vorspann.ausfuehren(con, a.lauf))\n'
    '        elif a.cmd == "tor4":\n            from . import tor4 as T4\n'
    '            _p(T4.ausfuehren(con, a.lauf, a.altlasten))\n')
ers(M, "  biotop vorspann <lauf>            (Generation minus eins, vor gen0 und mass)\n",
    "  biotop vorspann <lauf>            (Generation minus eins, vor gen0 und mass)\n"
    "  biotop tor4 <lauf> --altlasten <liste.json>   (Tor-4-Skript: Torzeile „Schwächen“ mit doppelter Prüfung)\n")


# ======================================================================== ausführen (alles oder nichts)
def main():
    neu_inhalt, fehler = {}, []
    for pfad, liste in AENDERUNGEN.items():
        text = (R / pfad).read_text()
        for alt, neu in liste:
            if isinstance(alt, tuple) and alt[0] == '__BEREICH__':
                _, start, ende_inkl, ende_vor = alt
                if text.count(start) != 1:
                    fehler.append(f'{pfad}: Bereichsanfang {start!r} {text.count(start)}×')
                    continue
                i = text.index(start)
                if ende_inkl is not None:
                    if text.count(ende_inkl) != 1:
                        fehler.append(f'{pfad}: Bereichsende {ende_inkl[:40]!r} {text.count(ende_inkl)}×')
                        continue
                    j = text.index(ende_inkl) + len(ende_inkl)
                else:
                    if text.count(ende_vor) != 1:
                        fehler.append(f'{pfad}: Bereichsende {ende_vor[:40]!r} {text.count(ende_vor)}×')
                        continue
                    j = text.index(ende_vor)
                text = text[:i] + neu + text[j:]
            else:
                n = text.count(alt)
                if n != 1:
                    fehler.append(f'{pfad}: Anker {n}× (statt 1×): {alt[:90]!r}')
                    continue
                text = text.replace(alt, neu)
        neu_inhalt[pfad] = text
    if fehler:
        print('ABBRUCH — nichts geschrieben:')
        print('\n'.join(fehler))
        sys.exit(2)
    for pfad, text in neu_inhalt.items():
        (R / pfad).write_text(text)
    print(f'geschrieben: {len(neu_inhalt)} Dateien, {sum(len(v) for v in AENDERUNGEN.values())} Ersetzungen')
    for pfad in neu_inhalt:
        print('  ', pfad, len(AENDERUNGEN[pfad]))


if __name__ == '__main__':
    main()
