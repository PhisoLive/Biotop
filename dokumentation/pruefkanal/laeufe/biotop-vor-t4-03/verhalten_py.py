"""Verhaltenssonde für Python-Werke (T4, Grundsatz 11). Läuft in der netzlosen Kammer (cwd /werk):
    python _messgeraet/verhalten.py _messgeraet/anfrage.json
Gegenstück zu kern/ts/verhalten.mjs + verhalten-runner.mjs.

Beobachtet werden die öffentlichen Funktionen UND die öffentlichen Methoden und Eigenschaften der Klassen der
geänderten Module (Behebungsrunde 3 vor T4, Entscheidung Chat-Claude 3). Eingewickelt wird jede Funktion und jedes
aufrufbare Objekt mit `__wrapped__` (functools.lru_cache, wraps; Review 02 Nr. 5), auch dort, wo andere Module sie
gebunden haben.
- Referenzlast (`beobachten()`, `last_<bereich>()`): je Funktion die ersten KAPPE äußeren Aufrufe (#0…#7), je Aufruf
  vier Muster — der Aufruf, @alias (dieselben Referenzen noch einmal), @mutation (Zahlenblätter der Eingaben an Ort und
  Stelle geändert), @nach_ruecksetzung. Nach jedem Aufruf ist der ZUSTAND der veränderlichen Argumente eine eigene
  Beobachtung (`>args`, Review 02 Nr. 2; bei Methoden gehört self dazu). Den Zustand von self VOR den Korpusaufrufen
  hält je Klasse `Klasse.__init__~instanz#0` fest (die frische Instanz aus dem Rezept).
- Zu jedem Aufruf (auch dem echten) ruft die Sonde die Funktion zusätzlich mit einer tiefen KOPIE der Eingabe vor dem
  Aufruf; weicht das Ergebnis ab, hängt es an Referenz oder verborgenem Zustand statt am Inhalt (`kopien`). Eine solche
  Abweichung deckt kein Test (verhaltensvergleich.deckung).
- Generatoren und Iteratoren werden begrenzt ausgelesen (erste ITER_KAPPE Elemente, Review 02 Nr. 1); der Aufrufer
  bekommt einen Iterator über dieselben Elemente. Koroutinen sind nicht vergleichbar (gezählt: `unvergleichbar`).
- Als inhaltlich beobachtet zählt nur ein fehlerfreier Aufruf mit vergleichbarem Ergebnis (`inhalt`, Review 02 Nr. 3).
- Randfall-Korpus (~rand#i) aus der deklarierten Signatur der Vorgeneration und beobachteten Beispielen; Parameter ohne
  Annotation und ohne Beispiel bekommen einen tastenden Satz. Formvarianten (~form#j) aus der ersten Argumentliste UND
  aus jeder Randliste mit Leerzeichen (Review 02 Nr. 10). Jede Beobachtung trägt ihr MUSTER (`muster`): Formart bzw.
  Merkmalsklassen der Eingabe (klassen_von) — Grundlage der Deckung je Muster (Entscheidung Chat-Claude 1).
- Methoden: Instanzen aus den Verträgen (tests/vertraege: erster Konstruktoraufruf je Klasse), sonst aus der Last
  (erster Konstruktoraufruf, sonst Zustand der ersten beobachteten Instanz), sonst aus der Signatur von __init__. Beide
  Stände bekommen dieselben Rezepte (die der Vorgeneration) und führen die Verträge an derselben Stelle aus.
- Feste Hash-Saat (PYTHONHASHSEED=0, Review 02 Nr. 4): die Sonde startet sich sonst mit ihr neu.
- Modus 'deckung': führt Tests (pytest) mit Aufzeichnern aus; je Test und Funktion die Merkmalsklassen der über die
  Signatur vereinheitlichten Argumente (Review 02 Nr. 9a). Mit `verfaelschen` {f, art} wird das Ergebnis bzw. der
  Argumentzustand dieser Funktion verfälscht: ein Test, der dann fällt, hält dieses Verhalten fest (Review 02 Nr. 8).
Ausgabe: eine Zeile @@VV@@<json>@@ENDE@@ auf stdout.
"""
import os
import sys

HASHSAAT = '0'
if __name__ == '__main__' and os.environ.get('PYTHONHASHSEED') != HASHSAAT:
    os.execve(sys.executable, [sys.executable, *sys.argv], {**os.environ, 'PYTHONHASHSEED': HASHSAAT})

import ast  # noqa: E402
import copy  # noqa: E402
import dataclasses  # noqa: E402
import enum  # noqa: E402
import functools  # noqa: E402
import glob  # noqa: E402
import hashlib  # noqa: E402
import importlib  # noqa: E402
import inspect  # noqa: E402
import itertools  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import re  # noqa: E402
import traceback  # noqa: E402
import types  # noqa: E402

REQ = {}
KAPPE, RAND_KAPPE, FORM_KAPPE, ITER_KAPPE = 8, 16, 16, 50
beob, argtext, zaehler, zaehler_rand, zaehler_form, beispiele = {}, {}, {}, {}, {}, {}
musterkarte, kopien, inhalt, unvergleichbar, instanzen = {}, {}, {}, {}, {}
aufrufe = []
AKTUELL = ['']
TIEFE = [0]
LAST = [False]          # True, solange die Referenzlast läuft: `erreicht` zählt dann jeden Aufruf, auch innere
erreicht = {}
WEISS = set('\t\n\r\x0b\x0c\u00a0\u2028\u2029\u3000\u2009')
_ADRESSE = re.compile(r' at 0x[0-9a-fA-F]+')


# ---------------------------------------------------------------- kanonische Form (Vergleich beider Stände)
def kan(x, anc=None, t=0):
    anc = set() if anc is None else anc
    if x is None or isinstance(x, (bool, str, int)):
        return x
    if isinstance(x, float):
        if math.isnan(x):
            return '__NaN'
        if math.isinf(x):
            return '__Inf' if x > 0 else '__-Inf'
        return '__-0' if x == 0 and math.copysign(1, x) < 0 else x
    if isinstance(x, (bytes, bytearray)):
        return {'__bytes': x.hex()[:400], 'typ': type(x).__name__}
    if isinstance(x, enum.Enum):
        return {'__enum': type(x).__qualname__ + '.' + x.name}
    if isinstance(x, Verfaelscht):
        return '__verfaelscht'
    if id(x) in anc:
        return '__zyklus'
    if t > 12:
        return '__tief'
    anc.add(id(x))
    try:
        if isinstance(x, list):
            return [kan(v, anc, t + 1) for v in x]
        if isinstance(x, tuple):
            r = {'__tupel': [kan(v, anc, t + 1) for v in x]}
            if type(x) is not tuple:
                r['typ'] = type(x).__qualname__
            return r
        if isinstance(x, dict):
            if all(isinstance(k, str) for k in x):
                return {'__dict': {k: kan(v, anc, t + 1) for k, v in x.items()}}
            paare = [[kan(k, anc, t + 1), kan(v, anc, t + 1)] for k, v in x.items()]
            return {'__dictk': sorted(paare, key=lambda p: json.dumps(p[0], sort_keys=True, default=str))}
        if isinstance(x, (set, frozenset)):
            return {'__set': sorted((kan(v, anc, t + 1) for v in x), key=lambda v: json.dumps(v, sort_keys=True, default=str))}
        if isinstance(x, BaseException):
            return {'__fehler': type(x).__name__, 'meldung': _ADRESSE.sub(' at 0x…', str(x))[:200]}
        if isinstance(x, (types.FunctionType, types.BuiltinFunctionType, types.MethodType, type, types.ModuleType)):
            return '__fn'
        if dataclasses.is_dataclass(x):
            return {'__klasse': type(x).__qualname__,
                    'felder': {f.name: kan(getattr(x, f.name, None), anc, t + 1) for f in dataclasses.fields(x)}}
        if hasattr(x, '__dict__'):
            return {'__klasse': type(x).__qualname__, 'felder': {k: kan(v, anc, t + 1) for k, v in sorted(vars(x).items())}}
        if hasattr(type(x), '__slots__'):
            return {'__klasse': type(x).__qualname__,
                    'felder': {s: kan(getattr(x, s, None), anc, t + 1) for s in getattr(type(x), '__slots__', ())}}
        return {'__objekt': type(x).__qualname__, 'repr': _ADRESSE.sub(' at 0x…', repr(x))[:200]}
    finally:
        anc.discard(id(x))


def text_von(x):
    return json.dumps(kan(x), sort_keys=True, ensure_ascii=False, default=str)


def knapp(t):
    if len(t) <= 200:
        return t
    return t[:120] + '…#' + hashlib.sha256(t.encode('utf-8', 'surrogatepass')).hexdigest()[:16]


def eingabe_text(args, kwargs):
    try:
        return knapp(text_von([list(args), kwargs]))
    except Exception:  # noqa: BLE001
        return '__unkanonisch'


class Verfaelscht:
    """Ergebnis einer verfälschten Funktion (Deckungsprobe): gleich nichts, auch sich selbst nicht."""
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True

    __hash__ = object.__hash__

    def __repr__(self):
        return '<verfälscht>'


# ---------------------------------------------------------------- Merkmalsklassen (Muster einer Eingabe)
def klassen_von(werte):
    """Merkmalsklassen der Werte — dieselben Namen wie die Formarten der Korpusaufrufe (Deckung je Muster).
    Leer heißt: gewöhnliche Eingabe."""
    out = set()

    def geh(x, t):
        if t > 6:
            return
        if x is None:
            out.add('null')
        elif isinstance(x, bool):
            return
        elif isinstance(x, (int, float)):
            if isinstance(x, float) and not math.isfinite(x):
                out.add('nichtendlich')
            elif x == 0:
                out.add('null_zahl')
            elif x < 0:
                out.add('negativ')
            if isinstance(x, float) and math.isfinite(x) and x.is_integer():
                out.add('zahltyp')
        elif isinstance(x, str):
            if x == '':
                out.add('leer')
                return
            if any(c in WEISS for c in x) or '  ' in x:
                out.add('weissraum')
            if x != x.strip():
                out.add('randweissraum')
            if any(c.isupper() for c in x):
                out.add('gross')
            if any(c.isalpha() for c in x) and x == x.lower() and x != x.upper():
                out.add('klein')
            if re.search(r'(?<![\d.])0\d|\d\.\d*0(?!\d)', x):
                out.add('zahlform')
            if len(x) >= 40:
                out.add('lang')
            if any(ord(c) > 127 and c not in WEISS for c in x):
                out.add('nichtascii')
        elif isinstance(x, (list, tuple, set, frozenset)):
            if isinstance(x, tuple):
                out.add('behaelter')
            if not x:
                out.add('leer')
            if len(x) >= 20:
                out.add('lang')
            for v in list(x)[:40]:
                geh(v, t + 1)
        elif isinstance(x, dict):
            if not x:
                out.add('leer')
            schl = list(x)
            if len(schl) > 1 and all(isinstance(k, str) for k in schl) and schl != sorted(schl):
                out.add('schluesselfolge')
            for v in list(x.values())[:40]:
                geh(v, t + 1)
        elif dataclasses.is_dataclass(x) and not isinstance(x, type):
            for f in dataclasses.fields(x):
                geh(getattr(x, f.name, None), t + 1)
        elif _instanz(x):
            for v in list(vars(x).values())[:40]:
                geh(v, t + 1)
    for w in werte:
        geh(w, 0)
    return out


def _gebunden(orig, args, kwargs, ohne_erstes):
    """Argumentwerte über die Signatur vereinheitlicht (Standardwerte eingesetzt; Review 02 Nr. 9a)."""
    try:
        ba = inspect.signature(orig).bind(*args, **kwargs)
        ba.apply_defaults()
        werte = []
        for name, v in ba.arguments.items():
            p = ba.signature.parameters[name]
            if p.kind == p.VAR_POSITIONAL:
                werte += list(v)
            elif p.kind == p.VAR_KEYWORD:
                werte += list(v.values())
            else:
                werte.append(v)
    except (TypeError, ValueError):
        werte = list(args) + list(kwargs.values())
    return werte[1:] if ohne_erstes and werte else werte


def _klassen_sicher(f):
    try:
        return sorted(f())
    except Exception:  # noqa: BLE001
        return ['__unbestimmt']


# ---------------------------------------------------------------- Ergebnis eines Aufrufs
def _iter_art(v):
    if inspect.iscoroutine(v) or inspect.isasyncgen(v) or inspect.isawaitable(v):
        return 'async'
    if isinstance(v, (str, bytes, bytearray, list, tuple, dict, set, frozenset, range)) or not hasattr(v, '__next__'):
        return None
    return 'iter'


def _weiter(elemente, quelle, fehler):
    yield from elemente
    if fehler is not None:
        raise fehler
    if quelle is not None:
        yield from quelle


def wert(f, name=None):
    """Ruft f(). Rückgabe {text, roh | fehler, inhaltlich}. Iteratoren werden begrenzt ausgelesen; `roh` ist dann ein
    Iterator über dieselben Elemente (der Aufrufer merkt nichts)."""
    try:
        v = f()
    except BaseException as e:  # noqa: B902 — jede Ausnahme ist ein beobachtetes Verhalten
        return {'text': 'Fehler:' + type(e).__name__, 'fehler': e, 'inhaltlich': False}
    art = _iter_art(v)
    if art == 'async':
        if name:
            unvergleichbar[name] = unvergleichbar.get(name, 0) + 1
        return {'text': '__async', 'roh': v, 'inhaltlich': False}
    if art == 'iter':
        elemente, fehler = [], None
        try:
            for x in itertools.islice(v, ITER_KAPPE + 1):
                elemente.append(x)
        except BaseException as e:  # noqa: B902
            fehler = e
        mehr = fehler is None and len(elemente) > ITER_KAPPE
        try:
            text = text_von({'__iter': elemente[:ITER_KAPPE], 'ende': ('Fehler:' + type(fehler).__name__) if fehler
                             else ('mehr' if mehr else 'ende')})
        except Exception as e:  # noqa: BLE001
            text = '__unkanonisch:' + type(e).__name__
        ok = not text.startswith('__unkanonisch')
        if name and ok:
            inhalt[name] = inhalt.get(name, 0) + 1
        return {'text': text, 'roh': _weiter(elemente, v if mehr else None, fehler), 'inhaltlich': ok}
    try:
        text = text_von(v)
    except Exception as e:  # noqa: BLE001
        return {'text': '__unkanonisch:' + type(e).__name__, 'roh': v, 'inhaltlich': False}
    if name:
        inhalt[name] = inhalt.get(name, 0) + 1
    return {'text': text, 'roh': v, 'inhaltlich': True}


# ---------------------------------------------------------------- Zustand der Eingaben
def _instanz(x):
    return hasattr(x, '__dict__') and not isinstance(
        x, (type, types.ModuleType, types.FunctionType, types.MethodType, types.BuiltinFunctionType, enum.Enum,
            functools.partial)) and not callable(getattr(x, '__wrapped__', None))


def _veraenderlich(v):
    return isinstance(v, (list, dict, set, bytearray)) or _instanz(v)


def _zahl(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and (not isinstance(v, float) or math.isfinite(v))


def schnappschuss(werte):
    log, seen = [], set()

    def geh(x, t):
        if t > 4 or id(x) in seen:
            return
        if isinstance(x, list):
            seen.add(id(x)); log.append((x, list(x), 'list'))
            for v in x:
                geh(v, t + 1)
        elif isinstance(x, dict):
            seen.add(id(x)); log.append((x, dict(x), 'dict'))
            for v in list(x.values()):
                geh(v, t + 1)
        elif isinstance(x, set):
            seen.add(id(x)); log.append((x, set(x), 'set'))
        elif isinstance(x, bytearray):
            seen.add(id(x)); log.append((x, bytearray(x), 'bytes'))
        elif isinstance(x, tuple):
            for v in x:
                geh(v, t + 1)
        elif _instanz(x):
            seen.add(id(x)); log.append((x, dict(vars(x)), 'obj'))
            for v in list(vars(x).values()):
                geh(v, t + 1)
    for a in werte:
        geh(a, 0)
    return log


def zuruecksetzen(log):
    for o, kopie, art in log:
        try:
            if art in ('list', 'bytes'):
                o[:] = kopie
            elif art in ('dict', 'set'):
                o.clear(); o.update(kopie)
            else:
                d = vars(o); d.clear(); d.update(kopie)
        except Exception:  # noqa: BLE001 — eingefroren oder schreibgeschützt: bleibt, wie es ist
            pass


def mutieren(werte):
    """Zahlenblätter an Ort und Stelle ändern — gleiche Referenzen, gleiche Längen. Rückgabe: Anzahl."""
    n, seen = 0, set()

    def geh(x, t):
        nonlocal n
        if t > 4 or id(x) in seen:
            return
        if isinstance(x, list):
            seen.add(id(x))
            for i, v in enumerate(x):
                if _zahl(v):
                    x[i] = v * 10 + 7; n += 1
                else:
                    geh(v, t + 1)
        elif isinstance(x, dict):
            seen.add(id(x))
            for k in list(x):
                v = x[k]
                if _zahl(v):
                    x[k] = v * 10 + 7; n += 1
                else:
                    geh(v, t + 1)
        elif isinstance(x, tuple):
            for v in x:
                geh(v, t + 1)
        elif _instanz(x):
            seen.add(id(x))
            for k, v in list(vars(x).items()):
                if _zahl(v):
                    try:
                        setattr(x, k, v * 10 + 7); n += 1
                    except Exception:  # noqa: BLE001
                        pass
                else:
                    geh(v, t + 1)
    for a in werte:
        geh(a, 0)
    return n


def _zustand_obs(schl, args, kwargs):
    """Zustand der veränderlichen Argumente NACH dem Aufruf als eigene Beobachtung (Review 02 Nr. 2)."""
    if any(_veraenderlich(v) for v in list(args) + list(kwargs.values())):
        try:
            beob[schl + '>args'] = knapp(text_von([list(args), kwargs]))
        except Exception:  # noqa: BLE001
            beob[schl + '>args'] = '__unkanonisch'


def _vorlage(args, kwargs):
    try:
        return copy.deepcopy((list(args), dict(kwargs)))
    except Exception:  # noqa: BLE001
        return None


def _kopie_vergleich(k, vorlage, call, ergebnis_text):
    """Dieselbe Eingabe als tiefe Kopie (Zustand VOR dem Aufruf): weicht das Ergebnis ab, hängt es an Referenz oder
    verborgenem Zustand statt am Inhalt — `kopien[k]`; solche Abweichungen deckt kein Test (verhaltensvergleich)."""
    if vorlage is None:
        kopien[k] = '__nicht_kopierbar'
        return
    ak, kk = vorlage
    t = knapp(wert(lambda: call(*ak, **kk))['text'])
    if t != ergebnis_text:
        kopien[k] = t


def muster(schl, args, kwargs, call, name=None, kl=()):
    """Ein Aufruf mit den vier Mustern. Rückgabe: das Ergebnis des echten Aufrufs ({roh} oder {fehler}).
    `kl`: das Muster der Eingabe (Merkmalsklassen des variierten Werts bzw. Formart; [] = gewöhnliche Eingabe).
    Nach jedem Aufruf: Zustand der veränderlichen Argumente (`>args`); zu jedem Aufruf die Kopienprobe."""
    TIEFE[0] += 1
    try:
        musterkarte[schl] = sorted(kl)
        argtext[schl] = eingabe_text(args, kwargs)
        vorlage = _vorlage(args, kwargs)
        erst = wert(lambda: call(*args, **kwargs), name)
        beob[schl] = knapp(erst['text'])
        _zustand_obs(schl, args, kwargs)
        werte = list(args) + list(kwargs.values())
        stand = schnappschuss(werte)
        _kopie_vergleich(schl, vorlage, call, beob[schl])
        zuruecksetzen(stand)

        def zusatz(k):
            argtext[k] = eingabe_text(args, kwargs)
            vorher = schnappschuss(werte)
            vl = _vorlage(args, kwargs)
            r = knapp(wert(lambda: call(*args, **kwargs), name)['text'])
            beob[k] = r
            _zustand_obs(k, args, kwargs)
            zuruecksetzen(vorher)
            _kopie_vergleich(k, vl, call, r)
            zuruecksetzen(vorher)
        zusatz(schl + '@alias')
        zuruecksetzen(stand)
        if mutieren(werte) > 0:
            zusatz(schl + '@mutation')
            zuruecksetzen(stand)
            zusatz(schl + '@nach_ruecksetzung')
            zuruecksetzen(stand)
        return erst
    finally:
        TIEFE[0] -= 1


# ---------------------------------------------------------------- Einwickeln
def _metadaten(w, orig):
    try:
        functools.update_wrapper(w, orig)
    except Exception:  # noqa: BLE001
        w.__wrapped__ = orig
    return w


def _methodenart(cls, n):
    """('inst'|'class'|'static'|'prop'|'cprop', Funktion) — None, wenn kein beobachtbares Mitglied."""
    roh = inspect.getattr_static(cls, n)
    if isinstance(roh, staticmethod):
        return 'static', roh.__func__
    if isinstance(roh, classmethod):
        return 'class', roh.__func__
    if isinstance(roh, property):
        return ('prop', roh.fget) if roh.fget is not None else None
    if isinstance(roh, functools.cached_property):
        return 'cprop', roh.func
    if inspect.isfunction(roh) or callable(getattr(roh, '__wrapped__', None)):
        return 'inst', roh
    return None


def wickeln(name, orig, art='fn'):
    ohne_erstes = art in ('inst', 'class', 'prop', 'cprop')

    def w(*args, **kwargs):
        if LAST[0]:
            erreicht[name] = erreicht.get(name, 0) + 1
        if TIEFE[0] > 0:
            return orig(*args, **kwargs)
        i = zaehler[name] = zaehler.get(name, -1) + 1
        if i == 0 and name not in beispiele:
            try:
                rest = args[1:] if ohne_erstes else args
                beispiele[name] = [[pack(a) for a in rest], {k: pack(v) for k, v in kwargs.items()}]
            except Exception:  # noqa: BLE001 — nicht packbar: ohne Beispiel
                beispiele[name] = None
        if art in ('inst', 'prop', 'cprop') and args:
            rezept_aus_zustand(args[0])
        if i >= KAPPE:
            return orig(*args, **kwargs)
        # Muster = Merkmalsklassen ALLER vereinheitlichten Argumente — dieselbe Rechnung wie im Aufzeichner der
        # deckenden Tests (deck_wickeln), damit „Test ruft dasselbe Muster“ auf beiden Seiten gleich gemessen ist.
        kl = _klassen_sicher(lambda: klassen_von(_gebunden(orig, args, kwargs, ohne_erstes)))
        erst = muster(f'{name}#{i}', args, kwargs, orig, name, kl=kl)
        if 'fehler' in erst:
            raise erst['fehler']
        return erst['roh']
    return _metadaten(w, orig)


_GESEHEN = set()
ZUSTAND = {}


def _stoeren(werte):
    for v in werte:
        try:
            if isinstance(v, list):
                v.append(Verfaelscht())
            elif isinstance(v, dict):
                v['__verfaelscht__'] = Verfaelscht()
            elif isinstance(v, set):
                v.add(Verfaelscht())
            elif isinstance(v, bytearray):
                v.append(0)
            elif _instanz(v):
                mutieren([v])
                setattr(v, '__verfaelscht__', Verfaelscht())
        except Exception:  # noqa: BLE001
            pass


def deck_wickeln(name, orig, art='fn'):
    """Aufzeichner der deckenden Tests: je Aufruf Test, Funktion und Merkmalsklassen der vereinheitlichten Argumente.
    Mit REQ['verfaelschen'] = {f: name, art: 'rueckgabe' | 'zustand'} wird genau diese Funktion verfälscht."""
    ohne_erstes = art in ('inst', 'class', 'prop', 'cprop', 'init')
    vf = REQ.get('verfaelschen') or {}

    def w(*args, **kwargs):
        if vf:
            if vf.get('f') != name:
                return orig(*args, **kwargs)
            if vf.get('art') == 'zustand':
                v = orig(*args, **kwargs)
                _stoeren(list(args) + list(kwargs.values()))
                return v
            try:
                orig(*args, **kwargs)
            except BaseException:  # noqa: B902 — das Ergebnis wird ersetzt, nicht der Aufruf unterdrückt
                pass
            return Verfaelscht()
        eintrag = {'test': AKTUELL[0], 'f': name,
                   'klassen': _klassen_sicher(lambda: klassen_von(_gebunden(orig, args, kwargs, ohne_erstes)))}
        s = json.dumps(eintrag, sort_keys=True)
        if s not in _GESEHEN:
            _GESEHEN.add(s)
            aufrufe.append(eintrag)
        return orig(*args, **kwargs)
    return _metadaten(w, orig)


def _einwickelbar(obj, mod):
    if inspect.isclass(obj):
        return False
    if inspect.isfunction(obj):
        return obj.__module__ == mod.__name__
    return callable(obj) and callable(getattr(obj, '__wrapped__', None)) and getattr(obj, '__module__', None) == mod.__name__


def _klasse_beobachtbar(obj, mod):
    return inspect.isclass(obj) and obj.__module__ == mod.__name__ and not issubclass(obj, (enum.Enum, BaseException))


def alle_wickeln(module, fabrik, init=False):
    """Funktionen, aufrufbare Objekte mit __wrapped__, Methoden und Eigenschaften der Klassen einwickeln.
    Rückgabe (eingewickelt, nicht_eingewickelt) — Letzteres mit Grund je Mitglied (gezählte Enthaltung)."""
    eingewickelt, nicht, ersatz = {}, {}, {}
    for m in module:
        mod = sys.modules[m]
        namen, fehlt = [], []
        for name, obj in list(vars(mod).items()):
            if name.startswith('_'):
                continue
            if _einwickelbar(obj, mod):
                w = fabrik(f'{m}:{name}', obj)
                setattr(mod, name, w)
                ersatz[id(obj)] = (obj, w)
                namen.append(name)
            elif _klasse_beobachtbar(obj, mod):
                mitglieder = sorted(n for n in vars(obj) if not n.startswith('_'))
                if init and '__init__' in vars(obj):
                    mitglieder.append('__init__')
                for n in mitglieder:
                    if n == '__init__':
                        w = fabrik(f'{m}:{name}.__init__', vars(obj)['__init__'], 'init')
                        obj.__init__ = w
                        continue
                    ma = _methodenart(obj, n)
                    if ma is None:
                        continue
                    art, fn = ma
                    w = fabrik(f'{m}:{name}.{n}', fn, art)
                    try:
                        if art == 'static':
                            setattr(obj, n, staticmethod(w))
                        elif art == 'class':
                            setattr(obj, n, classmethod(w))
                        elif art == 'prop':
                            alt = inspect.getattr_static(obj, n)
                            setattr(obj, n, property(w, alt.fset, alt.fdel, alt.__doc__))
                        elif art == 'cprop':
                            cp = functools.cached_property(w)
                            cp.__set_name__(obj, n)
                            setattr(obj, n, cp)
                        else:
                            setattr(obj, n, w)
                        namen.append(f'{name}.{n}')
                    except Exception as e:  # noqa: BLE001
                        fehlt.append(f'{name}.{n} ({type(e).__name__})')
            elif callable(obj) and not inspect.isclass(obj) and not inspect.ismodule(obj) \
                    and getattr(type(obj), '__module__', None) == mod.__name__:
                fehlt.append(f'{name} (aufrufbares Objekt ohne __wrapped__)')
        eingewickelt[m] = sorted(namen)
        if fehlt:
            nicht[m] = fehlt
    wurzeln = {m.split('.')[0] for m in module}
    for mn, mod in list(sys.modules.items()):
        if mod is None or mn.split('.')[0] not in wurzeln:
            continue
        for name, obj in list(vars(mod).items()):
            if id(obj) in ersatz and ersatz[id(obj)][0] is obj:
                try:
                    setattr(mod, name, ersatz[id(obj)][1])
                except Exception:  # noqa: BLE001
                    pass
    return eingewickelt, nicht


def signaturen_lesen(mod):
    """Öffentliche Funktionen, Methoden und Eigenschaften → Annotationen ihrer positionalen Parameter (ohne self/cls).
    Methoden heißen 'Klasse.name'."""
    out = {}
    try:
        baum = ast.parse(inspect.getsource(mod))
    except Exception:  # noqa: BLE001
        return out

    def params(fn, ohne_erstes):
        if any(d is None for d in fn.args.kw_defaults):
            return None           # Pflicht-Schlüsselwortparameter: keine positionalen Randfälle
        ps = list(fn.args.posonlyargs) + list(fn.args.args)
        ps = ps[1:] if ohne_erstes else ps
        return [ast.unparse(p.annotation) if p.annotation is not None else '' for p in ps]
    for k in baum.body:
        if isinstance(k, (ast.FunctionDef, ast.AsyncFunctionDef)) and not k.name.startswith('_'):
            p = params(k, False)
            if p is not None:
                out[k.name] = p
        elif isinstance(k, ast.ClassDef) and not k.name.startswith('_'):
            for f in k.body:
                if not isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef)) or f.name.startswith('_'):
                    continue
                deko = {ast.unparse(d) for d in f.decorator_list}
                if any(d.endswith(('.setter', '.deleter')) for d in deko):
                    continue
                if deko & {'property', 'functools.cached_property', 'cached_property'}:
                    out[f'{k.name}.{f.name}'] = []
                    continue
                p = params(f, 'staticmethod' not in deko)
                if p is not None:
                    out[f'{k.name}.{f.name}'] = p
    return out


# ---------------------------------------------------------------- Beispiele packen (reisen über den Wirt zur zweiten Kammer)
def pack(x, t=0):
    if t > 6:
        raise ValueError('zu tief')
    if x is None or isinstance(x, (bool, str, int)):
        return x
    if isinstance(x, float):
        return x if math.isfinite(x) else {'__num': repr(x)}
    if isinstance(x, list):
        return [pack(v, t + 1) for v in x[:20]]
    if isinstance(x, tuple) and type(x) is tuple:
        return {'__tupel': [pack(v, t + 1) for v in x[:20]]}
    if isinstance(x, (set, frozenset)):
        return {'__set': [pack(v, t + 1) for v in list(x)[:20]], 'fest': isinstance(x, frozenset)}
    if isinstance(x, dict):
        return {'__dict': [[pack(k, t + 1), pack(v, t + 1)] for k, v in list(x.items())[:20]]}
    if isinstance(x, enum.Enum):
        return {'__enum': f'{type(x).__module__}:{type(x).__qualname__}', 'n': x.name}
    if dataclasses.is_dataclass(x) and not isinstance(x, type) and all(f.init for f in dataclasses.fields(x)):
        return {'__dc': f'{type(x).__module__}:{type(x).__qualname__}',
                'f': {f.name: pack(getattr(x, f.name), t + 1) for f in dataclasses.fields(x)}}
    if _instanz(x) and not hasattr(type(x), '__slots__') and type(x).__module__ not in ('builtins',):
        return {'__obj': f'{type(x).__module__}:{type(x).__qualname__}',
                'z': {k: pack(v, t + 1) for k, v in vars(x).items()}}
    raise ValueError('nicht packbar: ' + type(x).__name__)


def _klasse(pfad):
    modul, _, qual = pfad.partition(':')
    obj = importlib.import_module(modul)
    for teil in qual.split('.'):
        obj = getattr(obj, teil)
    return obj


def unpack(x):
    if isinstance(x, list):
        return [unpack(v) for v in x]
    if not isinstance(x, dict):
        return x
    if '__tupel' in x:
        return tuple(unpack(v) for v in x['__tupel'])
    if '__set' in x:
        s = {unpack(v) for v in x['__set']}
        return frozenset(s) if x.get('fest') else s
    if '__dict' in x:
        return {unpack(k): unpack(v) for k, v in x['__dict']}
    if '__num' in x:
        return float(x['__num'])
    if '__enum' in x:
        return _klasse(x['__enum'])[x['n']]
    if '__dc' in x:
        return _klasse(x['__dc'])(**{k: unpack(v) for k, v in x['f'].items()})
    if '__obj' in x:
        cls = _klasse(x['__obj'])
        o = cls.__new__(cls)
        o.__dict__.update({k: unpack(v) for k, v in x['z'].items()})
        return o
    return x


# ---------------------------------------------------------------- Instanzen für Methoden (Entscheidung 3)
KONSTRUKTION = {}      # 'modul:Klasse' → {'art': 'aufruf'|'zustand', 'args', 'kwargs'|'z', 'herkunft'}
KLASSEN = {}           # 'modul:Klasse' → Klasse (öffentlich, im geänderten Modul definiert)


def _klassenname(obj):
    return f'{type(obj).__module__}:{type(obj).__qualname__}'


def rezept_aus_zustand(obj):
    n = _klassenname(obj)
    if n in KONSTRUKTION or n not in KLASSEN or REQ.get('konstruktion') is not None:
        return
    try:
        KONSTRUKTION[n] = {'art': 'zustand', 'z': {k: pack(v) for k, v in vars(obj).items()}, 'herkunft': 'last_zustand'}
    except Exception:  # noqa: BLE001
        pass


def klassen_sammeln(module):
    for m in module:
        mod = sys.modules[m]
        for name, obj in vars(mod).items():
            if not name.startswith('_') and _klasse_beobachtbar(obj, mod):
                KLASSEN[f'{m}:{obj.__qualname__}'] = obj


def konstruktion_aufzeichnen(herkunft):
    """__init__ jeder Klasse umhüllen: der erste packbare Konstruktoraufruf wird Rezept (nur an der Vorgeneration).
    Rückgabe: Aufräumer."""
    alt = {}
    if REQ.get('konstruktion') is not None:
        return lambda: None
    for n, cls in KLASSEN.items():
        orig = cls.__dict__.get('__init__')
        if orig is None:
            continue

        def huelle(self, *a, _n=n, _orig=orig, **k):
            if type(self) is KLASSEN[_n] and _n not in KONSTRUKTION:
                try:
                    KONSTRUKTION[_n] = {'art': 'aufruf', 'args': [pack(v) for v in a],
                                        'kwargs': {kk: pack(v) for kk, v in k.items()}, 'herkunft': herkunft}
                except Exception:  # noqa: BLE001
                    pass
            return _orig(self, *a, **k)
        alt[n] = orig
        cls.__init__ = functools.wraps(orig)(huelle)

    def aufraeumen():
        for n, orig in alt.items():
            KLASSEN[n].__init__ = orig
    return aufraeumen


def vertraege_ausfuehren():
    """Die Vertragstests des Werks (beide Stände, gleiche Stelle im Ablauf) — erste Quelle der Instanzrezepte."""
    dateien = sorted(glob.glob('tests/vertraege/test_*.py'))
    if not dateien:
        return {'dateien': 0, 'rc': None}
    import pytest
    rc = pytest.main(['-q', '-p', 'no:cacheprovider', '--tb=no', '-o', 'addopts=', *dateien])
    return {'dateien': len(dateien), 'rc': int(rc)}


def instanz(n):
    """Frische Instanz der Klasse n aus dem Rezept (Vorgeneration); ohne Rezept aus der Signatur von __init__."""
    cls = KLASSEN[n]
    r = (REQ.get('konstruktion') or KONSTRUKTION).get(n)
    if r and r.get('art') == 'aufruf':
        return cls(*[unpack(v) for v in r['args']], **{k: unpack(v) for k, v in r['kwargs'].items()})
    if r and r.get('art') == 'zustand':
        o = cls.__new__(cls)
        o.__dict__.update({k: unpack(v) for k, v in r['z'].items()})
        return o
    try:
        ps = [p for p in list(inspect.signature(cls).parameters.values())
              if p.default is inspect.Parameter.empty and p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)]
    except (TypeError, ValueError):
        ps = []
    typen = ['' if p.annotation is inspect.Parameter.empty else
             (p.annotation if isinstance(p.annotation, str) else getattr(p.annotation, '__name__', str(p.annotation)))
             for p in ps]
    grund = argumentlisten(typen, None)[0] if typen else []
    return cls(*[unpack(v) for v in grund])


# ---------------------------------------------------------------- Korpus: Randfälle und Formvarianten
def _blaetter(p, f):
    if isinstance(p, list):
        return [_blaetter(v, f) for v in p]
    if isinstance(p, dict):
        if '__tupel' in p:
            return {**p, '__tupel': [_blaetter(v, f) for v in p['__tupel']]}
        if '__set' in p:
            return {**p, '__set': [_blaetter(v, f) for v in p['__set']]}
        if '__dict' in p:
            return {'__dict': [[k, _blaetter(v, f)] for k, v in p['__dict']]}
        if '__dc' in p:
            return {'__dc': p['__dc'], 'f': {k: _blaetter(v, f) for k, v in p['f'].items()}}
        if '__obj' in p:
            return {'__obj': p['__obj'], 'z': {k: _blaetter(v, f) for k, v in p['z'].items()}}
        return p
    return f(p)


def schrumpfen(p):
    """leer, einzeln, doppelt, Grenzwerte — aus einem beobachteten (gepackten) Wert."""
    out = [p]
    if isinstance(p, list):
        out.append([])
        if p:
            out += [[p[0]], [p[0], p[0]], [_blaetter(p[0], lambda v: 0 if _zahl(v) else ('' if isinstance(v, str) else v))]]
    elif isinstance(p, dict) and ('__dc' in p or '__dict' in p or '__tupel' in p or '__obj' in p):
        out += [_blaetter(p, lambda v: (0.0 if isinstance(v, float) else 0) if _zahl(v) else v),
                _blaetter(p, lambda v: '' if isinstance(v, str) else v),
                _blaetter(p, lambda v: (-1.0 if isinstance(v, float) else -1) if _zahl(v) else v)]
    elif isinstance(p, bool):
        out.append(not p)
    elif isinstance(p, float):
        out += [0.0, -1.0, 1.0]
    elif isinstance(p, int):
        out += [0, -1, 1]
    elif isinstance(p, str):
        out += ['', ' ', 'a b'] if ERWEITERT[0] else ['', ' ']
    return out


def teilen(t, zeichen):
    teile, tiefe, start = [], 0, 0
    for i, c in enumerate(t):
        if c in '[(':
            tiefe += 1
        elif c in '])':
            tiefe -= 1
        elif c == zeichen and tiefe == 0:
            teile.append(t[start:i].strip()); start = i + 1
    teile.append(t[start:].strip())
    return [x for x in teile if x]


def _elemente(b):
    if isinstance(b, list):
        return b
    if isinstance(b, dict) and '__tupel' in b:
        return b['__tupel']
    if isinstance(b, dict) and '__set' in b:
        return b['__set']
    return None


UNTYPISIERT = ['a b', 1, 0, [], None]      # Parameter ohne Annotation und ohne Beispiel (Review 02 Nr. 3)
ERWEITERT = [True]      # False: Korpus wie an 330b4ec (nur Randfälle) — nur für die getrennte Messung K2868 (S-7)


def typ_kandidaten(t, b, stufe=0):
    t = (t or '').strip().strip('"\'')
    t = re.sub(r'^(?:typing|t|collections\.abc)\.', '', t)
    if not t or stufe > 3:
        if b is not None:
            return schrumpfen(b)
        return list(UNTYPISIERT) if stufe == 0 and ERWEITERT[0] else []
    m = re.fullmatch(r'Optional\[(.+)\]', t)
    teile = [m.group(1), 'None'] if m else teilen(t, '|')
    m = re.fullmatch(r'Union\[(.+)\]', t)
    if m:
        teile = teilen(m.group(1), ',')
    if len(teile) > 1:
        ohne = [s for s in teile if s not in ('None', 'NoneType')]
        rest = [v for s in ohne for v in typ_kandidaten(s, b, stufe + 1)][:6]
        return rest + ([None] if len(ohne) < len(teile) else [])
    m = re.fullmatch(r'Literal\[(.+)\]', t)
    if m:
        out = []
        for s in teilen(m.group(1), ','):
            try:
                out.append(ast.literal_eval(s))
            except Exception:  # noqa: BLE001
                pass
        return [v for v in out if v is None or isinstance(v, (str, int, float, bool))]
    if t == 'int':
        return [0, 1, -1, 2, 100]
    if t == 'float':
        return [0.0, 1.0, -1.0, 0.5, 100.0]
    if t == 'bool':
        return [False, True]
    if t == 'str':
        return ['', 'a', ' ', 'a b', 'Ä-1', 'x' * 40] if ERWEITERT[0] else ['', 'a', ' ', 'Ä-1', 'x' * 40]
    if t in ('None', 'NoneType'):
        return [None]
    m = re.fullmatch(r'(list|List|Sequence|MutableSequence|Iterable|Collection|set|Set|frozenset|FrozenSet|tuple|Tuple)\[(.+)\]', t)
    if m:
        art, innen = m.group(1).lower(), m.group(2)
        glieder = teilen(innen, ',')
        if art == 'tuple' and not (len(glieder) == 2 and glieder[1] == '...'):
            eb = _elemente(b) or []
            kand = [typ_kandidaten(g, eb[i] if i < len(eb) else None, stufe + 1) or [None] for i, g in enumerate(glieder)]
            grund = [k[0] for k in kand]
            return [{'__tupel': grund}] + [{'__tupel': grund[:i] + [v] + grund[i + 1:]} for i, k in enumerate(kand) for v in k[1:3]]
        if art == 'tuple':
            innen = glieder[0]
        elemente = _elemente(b)
        eb = elemente[0] if elemente else None
        e = typ_kandidaten(innen, eb, stufe + 1)
        if not e and eb is not None:
            e = schrumpfen(eb)
        listen = [[]]
        if e:
            listen += [[e[0]], [e[0], e[0]]] + [[v] for v in e[1:4]]
            if len(e) >= 3:
                listen.append([e[0], e[1], e[2]])
        if elemente:
            listen.append(elemente[:20])
        if art == 'tuple':
            return [{'__tupel': l} for l in listen]
        if art in ('set', 'frozenset'):
            return [{'__set': l, 'fest': art == 'frozenset'} for l in listen]
        return listen
    m = re.fullmatch(r'(dict|Dict|Mapping|MutableMapping)\[(.+)\]', t)
    if m:
        out = [{'__dict': []}]
        if isinstance(b, dict) and '__dict' in b:
            out += [b, {'__dict': b['__dict'][:1]}]
        return out
    return schrumpfen(b) if b is not None else []


def _json(x):
    return json.dumps(x, sort_keys=True, default=str)


def _eindeutig(listen, kappe):
    gesehen, out = set(), []
    for l in listen:
        s = _json(l)
        if s not in gesehen:
            gesehen.add(s); out.append(l)
    return out[:kappe]


def argumentlisten(typen, beispiel):
    if not typen:
        return [[]]
    k = []
    for j, typ in enumerate(typen):
        b = beispiel[j] if beispiel and j < len(beispiel) else None
        c = typ_kandidaten(typ, b)
        if b is not None:
            c = [b] + c
        if not c:
            c = [None, []]
        k.append(_eindeutig(c, 64))
    grund = [c[0] for c in k]
    listen = [grund] + [grund[:j] + [v] + grund[j + 1:] for j in range(len(k)) for v in k[j][1:]]
    return _eindeutig(listen, RAND_KAPPE)


def _text_formen(s):
    """[(wert, art)] — dieselbe Zeichenkette in anderer Form."""
    out = []
    if ' ' in s:
        out += [(s.replace(' ', r), 'weissraum') for r in ('\t', '\n', '  ', '\r\n', '\u00a0')]
    out += [(' ' + s, 'randweissraum'), (s + ' ', 'randweissraum'), ('\t' + s + '\n', 'randweissraum')]
    if s.upper() != s:
        out.append((s.upper(), 'gross'))
    if s.lower() != s:
        out.append((s.lower(), 'klein'))
    m = re.search(r'\d+(?:\.\d+)?', s)
    if m:
        z, a, e = m.group(0), s[:m.start()], s[m.end():]
        out += [(a + '0' + z + e, 'zahlform'), (a + z + ('0' if '.' in z else '.0') + e, 'zahlform')]
    return out


def form_werte(p):
    """[(wert, art)] — dieselbe Eingabe in anderer Form (Weißraum, Groß/Klein, Zahlform, Zahltyp, Behälter, Folge)."""
    out = []
    if isinstance(p, str) and p:
        out += _text_formen(p)
    elif isinstance(p, bool) or p is None:
        pass
    elif isinstance(p, int):
        out.append((float(p), 'zahltyp'))       # nur int → float: klassen_von erkennt den ganzzahligen float
    elif isinstance(p, list):
        out.append(({'__tupel': p}, 'behaelter'))
    elif isinstance(p, dict) and ('__dict' in p or '__dc' in p):
        if '__dict' in p and len(p['__dict']) > 1:
            out.append(({'__dict': list(reversed(p['__dict']))}, 'schluesselfolge'))
        felder = p['__dict'] if '__dict' in p else list(p['f'].items())
        n = 0
        for i, (k, v) in enumerate(felder):
            if isinstance(v, str) and v and n < 2:
                n += 1
                for w, art in _text_formen(v)[:6]:
                    if '__dict' in p:
                        d = [list(x) for x in p['__dict']]; d[i] = [k, w]; out.append(({'__dict': d}, art))
                    else:
                        out.append(({'__dc': p['__dc'], 'f': {**p['f'], k: w}}, art))
    s0 = _json(p)
    return [(v, a) for v, a in out if _json(v) != s0]


def _hat_leerzeichen(p):
    if isinstance(p, str):
        return ' ' in p.strip()
    if isinstance(p, list):
        return any(_hat_leerzeichen(v) for v in p)
    if isinstance(p, dict):
        teile = p.get('__tupel') or p.get('__set') or [x[1] for x in p.get('__dict') or []] or list((p.get('f') or {}).values())
        return any(_hat_leerzeichen(v) for v in teile)
    return False


def formvarianten(quellen):
    """Formvarianten aus der Grundliste und aus jeder Randliste mit Leerzeichen. Rückgabe [(liste, art)]."""
    listen = []
    for grund in quellen:
        for j, p in enumerate(grund):
            for v, art in form_werte(p):
                listen.append((grund[:j] + [v] + grund[j + 1:], art))
    gesehen, out = set(), []
    for l, art in listen:
        s = _json(l)
        if s not in gesehen:
            gesehen.add(s); out.append((l, art))
    return out[:FORM_KAPPE]


def _ziel(m, f):
    """(Aufrufbares, Art, Klassenname) eines Korpusziels; None, wenn der Stand es nicht (mehr) hat."""
    klasse, _, meth = f.rpartition('.')
    if not klasse:
        fn = getattr(sys.modules[m], f, None)
        return (fn, 'fn', None) if callable(fn) else None
    cls_n = f'{m}:{klasse}'
    cls = KLASSEN.get(cls_n)
    if cls is None or meth not in vars(cls):
        return None
    ma = _methodenart(cls, meth)
    if ma is None:
        return None
    art, fn = ma
    if art == 'cprop':
        fn = getattr(inspect.getattr_static(cls, meth), 'func', fn)
    return fn, art, cls_n


def korpus_randfaelle(module, signaturen):
    quelle = REQ.get('beispiele') if REQ.get('beispiele') is not None else beispiele
    erweitert = REQ.get('korpus_erweitert', True)
    for m in module:
        for f, typen in (signaturen.get(m) or {}).items():
            name = f'{m}:{f}'
            z = _ziel(m, f)
            if z is None:
                continue                      # vom Kandidaten entfernt: der Wirt weist das getrennt aus
            fn, art, cls_n = z
            bsp = (quelle or {}).get(name)
            listen = argumentlisten(typen or [], bsp[0] if isinstance(bsp, list) and bsp else None)
            grund = listen[0] if listen else []
            quellen = [grund] + [l for l in listen[1:] if _hat_leerzeichen(l)] if erweitert else []
            formen = formvarianten(quellen) if erweitert else []
            laeufe = [('rand', i, l, None) for i, l in enumerate(listen)] + [('form', j, l, a) for j, (l, a) in enumerate(formen)]
            for korpusart, i, liste, formart in laeufe:
                try:
                    args = [unpack(v) for v in liste]
                except Exception:  # noqa: BLE001 — Beispiel am Kandidaten nicht herstellbar
                    continue
                schl = f'{name}~{korpusart}#{i}'
                if art in ('fn', 'static'):
                    voll = args
                else:
                    try:
                        ziel = KLASSEN[cls_n] if art == 'class' else instanz(cls_n)
                    except BaseException as e:  # noqa: B902 — keine Instanz: als Aufbaufehler beobachtet, gezählt
                        beob[schl] = 'Instanzfehler:' + type(e).__name__
                        musterkarte[schl] = []
                        instanzen[cls_n] = 'fehlgeschlagen:' + type(e).__name__
                        continue
                    voll = [ziel] + args     # Zustand von self danach: `>args`; davor: `~instanz` je Klasse
                # Muster = Merkmalsklassen aller Argumente (wie im Aufzeichner), bei Formvarianten zusätzlich die Formart.
                kl = _klassen_sicher(lambda: klassen_von(_gebunden(fn, voll, {}, art not in ('fn', 'static'))))
                if korpusart == 'form':
                    kl = sorted(set(kl) | {formart})
                erst = muster(schl, voll, {}, fn, name, kl=kl)
                if 'fehler' not in erst:
                    zz = zaehler_rand if korpusart == 'rand' else zaehler_form
                    zz[name] = zz.get(name, 0) + 1


def main():
    global KAPPE, RAND_KAPPE, FORM_KAPPE
    REQ.clear()
    REQ.update(json.load(open(sys.argv[1], encoding='utf-8')))
    KAPPE, RAND_KAPPE, FORM_KAPPE = REQ.get('kappe') or 8, REQ.get('rand_kappe') or 16, REQ.get('form_kappe') or 16
    if '/werk' not in sys.path:
        sys.path.insert(0, '/werk')
    modus = REQ.get('modus', 'beobachten')
    ERWEITERT[0] = bool(REQ.get('korpus_erweitert', True))
    # Module einzeln laden (Review 02 Nr. 12: auch Wurzelmodule): ein nicht ladbares Modul ist ein eigener, gezählter
    # Befund (`nicht_ladbar`); nur wenn keines lädt, ist die ganze Sonde ohne Gegenstand.
    nicht_ladbar = {}
    for m in REQ.get('module') or []:
        try:
            importlib.import_module(m)
        except BaseException as e:  # noqa: B902
            nicht_ladbar[m] = ''.join(traceback.format_exception_only(type(e), e))[-600:]
    module = [m for m in REQ.get('module') or [] if m not in nicht_ladbar]
    if not module:
        return {'gueltig': False, 'art': 'inhalt', 'nicht_ladbar': nicht_ladbar,
                'grund': 'Modul lädt nicht: ' + ' | '.join(f'{m}: {g}' for m, g in nicht_ladbar.items())[-1500:]}
    klassen_sammeln(module)
    signaturen = REQ.get('signaturen') or {m: signaturen_lesen(sys.modules[m]) for m in module}
    if modus == 'deckung':
        eingewickelt, _ = alle_wickeln(module, deck_wickeln, init=True)
        import pytest

        class Plugin:
            def pytest_runtest_setup(self, item):
                datei, _, rest = item.nodeid.partition('::')
                AKTUELL[0] = os.path.basename(datei) + '::' + rest

            def pytest_runtest_logreport(self, report):
                datei, _, rest = report.nodeid.partition('::')
                tid = os.path.basename(datei) + '::' + rest
                if report.when == 'call' or report.outcome != 'passed':
                    ZUSTAND[tid] = 'pass' if report.outcome == 'passed' and ZUSTAND.get(tid, 'pass') == 'pass' else 'fail'
        rc = pytest.main(['-q', '-p', 'no:cacheprovider', '--tb=no', '-o', 'addopts=', *(REQ.get('testdateien') or [])],
                         plugins=[Plugin()])
        ueberlauf = len(aufrufe) > 20000        # laut statt abgeschnitten
        return {'gueltig': int(rc) in (0, 1) and not ueberlauf, 'rc': int(rc), 'aufrufe': [] if ueberlauf else aufrufe,
                'zustand': ZUSTAND, 'ueberlauf': ueberlauf, 'eingewickelt': eingewickelt, 'nicht_ladbar': nicht_ladbar,
                'verfaelscht': REQ.get('verfaelschen'), 'hashsaat': os.environ.get('PYTHONHASHSEED'),
                'grund': 'Aufzeichnung über 20000 eindeutige Aufrufe — verworfen, nicht abgeschnitten' if ueberlauf else ''}
    # Verträge laufen auf BEIDEN Seiten an derselben Stelle (gleicher Modulzustand vor der Last); Rezepte zeichnet nur
    # die Vorgeneration auf (am Kandidaten kommen sie aus REQ['konstruktion']).
    aufraeumen = konstruktion_aufzeichnen('vertrag')
    try:
        vertragslauf = vertraege_ausfuehren()
    finally:
        aufraeumen()
    aufraeumen = konstruktion_aufzeichnen('last')
    eingewickelt, nicht = alle_wickeln(module, wickeln)
    ns = {}
    try:
        with open('_messgeraet/referenzlast.py', encoding='utf-8') as f:
            exec(compile(f.read(), '_messgeraet/referenzlast.py', 'exec'), ns)
    except BaseException as e:  # noqa: B902
        return {'gueltig': False, 'art': 'infrastruktur', 'grund': 'Referenzlast nicht ladbar: ' + repr(e)[:500]}
    korpus = [k for k in ['beobachten'] + ['last_' + b for b in REQ.get('bereiche') or []] if callable(ns.get(k))]
    LAST[0] = True
    for k in korpus:
        try:
            ns[k]()
            beob['korpus:' + k] = 'ok'
        except BaseException as e:  # noqa: B902
            beob['korpus:' + k] = 'Fehler:' + type(e).__name__
    LAST[0] = False
    aufraeumen()
    if modus == 'erreichbarkeit':
        # Welche Funktionen erreicht die Referenzlast (jeder Aufruf, auch innere)? Für die Vertragsprobe (S-10).
        return {'gueltig': True, 'erreicht': erreicht, 'korpus': korpus, 'beobachtungen': {k: v for k, v in beob.items()
                                                                                         if k.startswith('korpus:')}}
    for n in sorted(KLASSEN):
        instanzen.setdefault(n, ((REQ.get('konstruktion') or KONSTRUKTION).get(n) or {}).get('herkunft') or 'signatur')
        # „Zustand von self VOR dem Aufruf“ (Entscheidung 3) für alle Korpusaufrufe: die frische Instanz aus dem Rezept.
        k = f'{n}.__init__~instanz#0'
        musterkarte[k] = []
        TIEFE[0] += 1
        try:
            beob[k] = knapp(text_von(instanz(n)))
            inhalt[f'{n}.__init__'] = 1
        except BaseException as e:  # noqa: B902
            beob[k] = 'Instanzfehler:' + type(e).__name__
        finally:
            TIEFE[0] -= 1
    korpus_randfaelle(module, signaturen)
    if module:
        korpus += ['randfaelle'] + (['formvarianten'] if ERWEITERT[0] else [])
    out = {'gueltig': True, 'beobachtungen': beob, 'argumente': argtext, 'korpus': korpus, 'aufgerufen': zaehler,
           'aufgerufen_rand': zaehler_rand, 'aufgerufen_form': zaehler_form, 'kappe': KAPPE, 'rand_kappe': RAND_KAPPE,
           'form_kappe': FORM_KAPPE, 'signaturen': signaturen, 'eingewickelt': eingewickelt, 'nicht_eingewickelt': nicht,
           'muster': musterkarte, 'kopien': kopien, 'inhalt': inhalt, 'unvergleichbar': unvergleichbar,
           'instanzen': {**{n: (r or {}).get('herkunft') for n, r in (REQ.get('konstruktion') or KONSTRUKTION).items()},
                         **instanzen},
           'vertragslauf': vertragslauf, 'hashsaat': os.environ.get('PYTHONHASHSEED'),
           'korpus_erweitert': ERWEITERT[0], 'nicht_ladbar': nicht_ladbar, 'erreicht': erreicht}
    if REQ.get('beispiele') is None:
        out['beispiele'] = beispiele
    if REQ.get('konstruktion') is None:
        out['konstruktion'] = KONSTRUKTION
    return out


if __name__ == '__main__':
    try:
        ergebnis = main()
    except BaseException as e:  # noqa: B902 — die Sonde selbst ist gescheitert: Messgerätausfall
        ergebnis = {'gueltig': False, 'art': 'infrastruktur', 'grund': 'Sondenfehler: ' + traceback.format_exc()[-1500:]}
    sys.stdout.write('\n@@VV@@' + json.dumps(ergebnis, ensure_ascii=False, default=str) + '@@ENDE@@\n')
