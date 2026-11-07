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
import asyncio  # noqa: E402
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
# Behebungsrunde 5: ITER_KAPPE 50 → 1000 (der eigene Randfall-Korpus erzeugte mit der Zahl 100 an linearen Generatoren
# 100 Elemente — eine Enthaltung durch die Sonde selbst; gemessen in TEILLAUF-1)
KAPPE, RAND_KAPPE, FORM_KAPPE, ITER_KAPPE = 8, 16, 16, 1000
beob, argtext, zaehler, zaehler_rand, zaehler_form, beispiele = {}, {}, {}, {}, {}, {}
musterkarte, kopien, inhalt, unvergleichbar, instanzen = {}, {}, {}, {}, {}
teilweise = {}          # Behebungsrunde 4: je Funktion gezählte Teil-Enthaltungen (Iterator-Kappe, Iterator-Objekt)
unvollstaendig = {}     # Behebungsrunde 5 (Entscheidung 1): je Funktion unvollständige Erfassungen (Grund → Anzahl)
sonde_ausfall = {}      # Behebungsrunde 5 (Entscheidung 3): Funktion → Grund (ihre Einwicklung ließ eine Bereichslast abbrechen)
TRANSPARENT = set()     # Behebungsrunde 5: durchlässige Funktionen (keine Beobachtung, kein Eingriff)
NUR = [None]            # Behebungsrunde 5: Eingrenzung — nur diese Funktionen greifen ein (Menge)
IM_LAST = [None]        # Behebungsrunde 5: Funktionen, in die die Sonde während der laufenden Bereichslast eingriff
LAST_AUFRUFE = {}       # Behebungsrunde 5: Bereichslast → Funktionen, in die die Sonde eingriff
LAST_OHNE_SONDE = {}    # Behebungsrunde 5: Bereichslast → Abbruch, der auch ohne jeden Eingriff der Sonde auftritt (Werk)
aufrufe = []
AKTUELL = ['']
TIEFE = [0]
LAST = [False]          # True, solange die Referenzlast läuft: `erreicht` zählt dann jeden Aufruf, auch innere
erreicht = {}
WEISS = set('\t\n\r\x0b\x0c\u00a0\u2028\u2029\u3000\u2009')
_ADRESSE = re.compile(r' at 0x[0-9a-fA-F]+')


# ---------------------------------------------------------------- kanonische Form (Vergleich beider Stände)
_HEAPTYPE = 1 << 9          # Py_TPFLAGS_HEAPTYPE: in Python definierte Klasse (nicht C)


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
        if type(x) is object:
            return '__objekt_leer'                     # reiner Platzhalter ohne Daten
        if type(x).__name__ == 'deque' and type(x).__module__ == 'collections':
            return {'__deque': [kan(v, anc, t + 1, fehlend) for v in x], 'maxlen': x.maxlen}
        roh = repr(x)
        if fehlend is not None:
            if hasattr(x, '__next__'):
                fehlend.append(f'{type(x).__qualname__}: Iterator in der Beobachtung, Elemente nicht erfasst')
            elif type(x).__repr__ is object.__repr__:
                fehlend.append(f'{type(x).__qualname__}: Objekt ohne erfassbare Daten (nur Standarddarstellung)')
        # ungekürzt (Behebungsrunde 5): knapp() kürzt den ganzen Text mit Prüfsumme, nichts fällt still weg
        return {'__objekt': type(x).__qualname__, 'repr': _ADRESSE.sub(' at 0x…', roh)}
    finally:
        anc.discard(id(x))


def text_von(x, fehlend=None):
    return json.dumps(kan(x, None, 0, fehlend), sort_keys=True, ensure_ascii=False, default=str)


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
WEISS_SONST = set('\x0b\x0c\u2028\u2029\u3000\u2009')


def _text_merkmale(x):
    """Merkmale einer Zeichenkette — je Formvariante der Sonde ein eigenes Merkmal (Entscheidung Chat-Claude 2,
    Behebungsrunde 4; Review 03 Nr. 1: ein gemeinsames `weissraum` ließ einen Test mit doppeltem Leerzeichen einen
    Tab-/Zeilenumbruch-Rückschritt decken). Dieselben Namen in kern/ts/kanon.mjs."""
    m = set()
    ohne_crlf = x.replace('\r\n', '')
    if '\r\n' in x:
        m.add('crlf')
    if '\r' in ohne_crlf:
        m.add('cr')
    if '\n' in ohne_crlf:
        m.add('zeilenumbruch')
    if '\t' in x:
        m.add('tab')
    if '\u00a0' in x:
        m.add('nbsp')
    if any(c in WEISS_SONST for c in x):
        m.add('weissraum_sonst')
    if '  ' in x:
        m.add('doppelleer')
    if x != x.lstrip():
        m.add('rand_vorn')
    if x != x.rstrip():
        m.add('rand_hinten')
    if any(c.isupper() for c in x):
        m.add('gross')
    if any(c.isalpha() for c in x) and x == x.lower() and x != x.upper():
        m.add('klein')
    if re.search(r'(?<![\d.])0\d', x):
        m.add('zahlform_null_vorn')
    if re.search(r'\d\.\d*0(?!\d)', x):
        m.add('zahlform_null_hinten')
    if len(x) >= 40:
        m.add('lang')
    if any(ord(c) > 127 and c not in WEISS for c in x):
        m.add('nichtascii')
    return m


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
            out.update(_text_merkmale(x))
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
            for v in list(_felder(x).values())[:40]:
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
    # Behebungsrunde 4 (Review 03 Nr. 3): nur Generatoren und Iteratoren der Standardbibliothek auslesen und ersetzen.
    # Ein Iterator-Objekt des Werks (eigene Klasse, eigene Attribute) bleibt unverändert — der Aufrufer liest womöglich
    # Attribute (gemessen: die Last brach sonst still ab, eine spätere Änderung blieb unsichtbar).
    # Behebungsrunde 5 (Entscheidung 3, Review 04 Nr. 4): ersetzt werden nur echte Iteratoren — Generatoren und
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


def _teil(name, art):
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


def _koroutine_ausfuehren(v):
    """Koroutine in einer eigenen Ereignisschleife ausführen, wenn keine läuft (Review 03 Nr. 7). Rückgabe
    (ergebnis, fehler) oder None, wenn eine Schleife läuft (dann bleibt es bei „unvergleichbar“)."""
    try:
        asyncio.get_running_loop()
        return None
    except RuntimeError:
        pass
    schleife = asyncio.new_event_loop()
    try:
        try:
            return schleife.run_until_complete(v), None
        except BaseException as e:  # noqa: B902 — ein Fehler der Koroutine ist beobachtetes Verhalten
            return None, e
    finally:
        schleife.close()


async def _fertig(ergebnis, fehler):
    if fehler is not None:
        raise fehler
    return ergebnis


def _weiter(elemente, quelle, fehler):
    yield from elemente
    if fehler is not None:
        raise fehler
    if quelle is not None:
        yield from quelle


def wert(f, name=None):
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


# ---------------------------------------------------------------- Zustand der Eingaben
def _slotnamen(x):
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


def _felder(x):
    """Zustand eines Objekts: __dict__ UND __slots__ (Review 03 Nr. 4: Slot-Klassen und dataclass(slots=True) hatten
    keinen Zustandsvergleich — 0 statt 28 Abweichungen)."""
    d = dict(vars(x)) if hasattr(x, '__dict__') else {}
    for n in _slotnamen(x):
        if n not in d and hasattr(x, n):
            d[n] = getattr(x, n)
    return d


def _felder_setzen(x, d):
    slots = _slotnamen(x)
    if hasattr(x, '__dict__'):
        vars(x).clear()
    for n in slots:
        if n not in d and hasattr(x, n):
            try:
                object.__delattr__(x, n)
            except Exception:  # noqa: BLE001
                pass
    for k, v in d.items():
        try:
            if k in slots or not hasattr(x, '__dict__'):
                object.__setattr__(x, k, v)
            else:
                vars(x)[k] = v
        except Exception:  # noqa: BLE001 — eingefroren oder schreibgeschützt: bleibt, wie es ist
            pass


def _instanz(x):
    return (hasattr(x, '__dict__') or bool(_slotnamen(x))) and not isinstance(
        x, (type, types.ModuleType, types.FunctionType, types.MethodType, types.BuiltinFunctionType, enum.Enum,
            functools.partial)) and not callable(getattr(x, '__wrapped__', None)) and not isinstance(x, os.PathLike)


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
            seen.add(id(x)); log.append((x, _felder(x), 'obj'))
            for v in list(_felder(x).values()):
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
                _felder_setzen(o, kopie)
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
            for k, v in list(_felder(x).items()):
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


def _zustand_obs(schl, args, kwargs, name=None):
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
        _zustand_obs(schl, args, kwargs, name)
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
            _zustand_obs(k, args, kwargs, name)
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
    if inspect.iscoroutinefunction(orig):
        inspect.markcoroutinefunction(w)
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
        if name in TRANSPARENT or (NUR[0] is not None and name not in NUR[0]):
            return orig(*args, **kwargs)        # Behebungsrunde 5 (Entscheidung 3): durchlässig bzw. Eingrenzung
        if TIEFE[0] > 0:
            return orig(*args, **kwargs)
        if IM_LAST[0] is not None:
            IM_LAST[0].add(name)
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
        # Behebungsrunde 5 (Entscheidung 7, Review 04 Nr. 9): der Lastaufruf trägt die Formmerkmale seiner Eingabe —
        # sonst deckt ein Test mit gewöhnlicher Eingabe eine Regression, die nur Tab/Zeilenumbruch der Last zeigt.
        kl = [m for m in _klassen_sicher(lambda: klassen_von(_gebunden(orig, args, kwargs, ohne_erstes)))
              if m in FORM_MERKMALE or m == '__unbestimmt']
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
            # Behebungsrunde 4 (Review 03 Nr. 2): nur Aufrufe verfälschen, deren Eingabe das Merkmal des Musters trägt —
            # sonst „hält“ ein Test fest, der das Merkmal nur nebenbei ruft und etwas anderes zusichert.
            m = vf.get('merkmal') or ''
            if m and m not in _klassen_sicher(lambda: klassen_von(_gebunden(orig, args, kwargs, ohne_erstes))):
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
    if _instanz(x) and type(x).__module__ not in ('builtins',):
        # Behebungsrunde 5 (Entscheidung 1): alle Datenattribute, auch Slots der ganzen Hierarchie
        return {'__obj': f'{type(x).__module__}:{type(x).__qualname__}',
                'z': {k: pack(v, t + 1) for k, v in _felder(x).items()}}
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
        _felder_setzen(o, {k: unpack(v) for k, v in x['z'].items()})
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
        KONSTRUKTION[n] = {'art': 'zustand', 'z': {k: pack(v) for k, v in _felder(obj).items()}, 'herkunft': 'last_zustand'}
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
        _felder_setzen(o, {k: unpack(v) for k, v in r['z'].items()})
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
        out += [(s.replace(' ', r), a) for r, a in (('\t', 'tab'), ('\n', 'zeilenumbruch'), ('  ', 'doppelleer'),
                                                     ('\r\n', 'crlf'), ('\u00a0', 'nbsp'))]
    out += [(' ' + s, 'rand_vorn'), (s + ' ', 'rand_hinten'), ('\t' + s + '\n', 'rand_tab_zeilenumbruch')]
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


FORM_MERKMALE = frozenset({'tab', 'zeilenumbruch', 'crlf', 'cr', 'nbsp', 'weissraum_sonst', 'doppelleer', 'rand_vorn',
                           'rand_hinten', 'gross', 'klein', 'zahlform_null_vorn', 'zahlform_null_hinten', 'zahltyp',
                           'behaelter', 'schluesselfolge'})


def _muster_von(liste, bezug, korpusart):
    """Muster eines Korpusaufrufs (Entscheidungen Chat-Claude 2 und 3, Behebungsrunde 4): die Formvarianten-Merkmale,
    die die Veränderung der Sonde an einem Argument einführt — Merkmale danach minus davor, nur an den veränderten
    Argumenten, nur Merkmale aus FORM_MERKMALE (Randwerte wie leer, None, lang, nicht-ASCII sind keine Formvarianten).
    Keine Veränderung (Grundliste) oder nichts eingeführt: gewöhnlich, []. `korpusart` nur zur Beschriftung."""
    var = [j for j in range(len(liste)) if j >= len(bezug) or _json(liste[j]) != _json(bezug[j])]
    if not var:
        return []
    try:
        neu = klassen_von([unpack(liste[j]) for j in var]) - klassen_von([unpack(bezug[j]) for j in var if j < len(bezug)])
        return sorted(neu & FORM_MERKMALE)
    except Exception:  # noqa: BLE001
        return ['__unbestimmt']


def formvarianten(quellen):
    """Formvarianten aus der Grundliste und aus jeder Randliste mit Leerzeichen. Rückgabe [(liste, art)]."""
    listen = []
    for grund in quellen:
        for j, p in enumerate(grund):
            for v, art in form_werte(p):
                listen.append((grund[:j] + [v] + grund[j + 1:], art, grund))
    gesehen, out = set(), []
    for l, art, q in listen:
        s = _json(l)
        if s not in gesehen:
            gesehen.add(s); out.append((l, art, q))
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


def instanz_erproben(n, signaturen):
    """Behebungsrunde 4 (Review 03 Nr. 6): ohne Rezept aus Vertrag oder Last baute die Sonde die Instanz nur mit der
    ersten Argumentliste der Signatur von __init__ (ohne Annotation: 'a b') — jede Methode warf, eine geänderte Methode
    blieb still. Jetzt die Argumentlisten der Reihe nach, bis eine Instanz entsteht, an der mindestens eine öffentliche
    Methode oder Eigenschaft mit ihrer Grundliste fehlerfrei antwortet; diese Liste wird Rezept (Herkunft
    'signatur_erprobt', gilt für beide Stände). Keine solche Liste: 'signatur_ohne_inhalt' (gezählter Enthaltungsgrund)."""
    cls = KLASSEN[n]
    modul, _, klasse = n.partition(':')
    try:
        ps = [p for p in list(inspect.signature(cls).parameters.values())
              if p.default is inspect.Parameter.empty and p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)]
    except (TypeError, ValueError):
        ps = []
    typen = ['' if p.annotation is inspect.Parameter.empty else
             (p.annotation if isinstance(p.annotation, str) else getattr(p.annotation, '__name__', str(p.annotation)))
             for p in ps]
    listen = argumentlisten(typen, None)[:12] if typen else [[]]
    mitglieder = [(f, t) for f, t in (signaturen.get(modul) or {}).items() if f.startswith(klasse + '.')]
    TIEFE[0] += 1
    try:
        for liste in listen:
            try:
                o = cls(*[unpack(v) for v in liste])
            except BaseException:  # noqa: B902
                continue
            for f, t in mitglieder:
                z = _ziel(modul, f)
                if z is None or z[1] not in ('inst', 'prop', 'cprop'):
                    continue
                grund = (argumentlisten(t or [], None) or [[]])[0]
                try:
                    wert_ = z[0](o, *[unpack(v) for v in grund])
                    if inspect.iscoroutine(wert_):
                        wert_.close()
                        continue
                    text_von(wert_)
                except BaseException:  # noqa: B902
                    continue
                KONSTRUKTION[n] = {'art': 'aufruf', 'args': [pack(v) for v in liste], 'kwargs': {},
                                   'herkunft': 'signatur_erprobt'}
                return True
    finally:
        TIEFE[0] -= 1
    instanzen[n] = 'signatur_ohne_inhalt'
    return False


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
            laeufe = ([('rand', i, l, None, grund) for i, l in enumerate(listen)]
                      + [('form', j, l, a, q) for j, (l, a, q) in enumerate(formen)])
            for korpusart, i, liste, formart, bezug in laeufe:
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
                erst = muster(schl, voll, {}, fn, name, kl=_muster_von(liste, bezug, korpusart))
                if 'fehler' not in erst:
                    zz = zaehler_rand if korpusart == 'rand' else zaehler_form
                    zz[name] = zz.get(name, 0) + 1


def _zusicherung_faellt(report, datei):
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


def _korpus_einmal(ns, k):
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


def _last_versuch(ns, k, modus, menge=None):
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
    for f in schuldig:
        sonde_ausfall[f] = grund
    TRANSPARENT.update(schuldig)


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
                # Behebungsrunde 4 (Review 03 Nr. 2): ein Fehler in Aufbau/Abbau (Fixture) oder ein Skip ist 'fehler'.
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
    TRANSPARENT.update(REQ.get('transparent') or [])
    LAST[0] = True
    for k in korpus:
        # Behebungsrunde 5 (Entscheidung 3): eingegrenzt wird nur beim ersten Blick auf die Vorgeneration (ohne Vorgabe
        # `transparent`); danach bekommen beide Stände dieselben durchlässigen Funktionen.
        _korpus_lauf(ns, k, eingrenzen=REQ.get('transparent') is None)
    LAST[0] = False
    aufraeumen()
    if modus == 'erreichbarkeit':
        # Welche Funktionen erreicht die Referenzlast (jeder Aufruf, auch innere)? Für die Vertragsprobe (S-10).
        return {'gueltig': True, 'erreicht': erreicht, 'korpus': korpus, 'beobachtungen': {k: v for k, v in beob.items()
                                                                                         if k.startswith('korpus:')}}
    if REQ.get('konstruktion') is None:
        for n in sorted(KLASSEN):
            if n not in KONSTRUKTION:
                instanz_erproben(n, signaturen)
    for n in sorted(KLASSEN):
        instanzen.setdefault(n, ((REQ.get('konstruktion') or KONSTRUKTION).get(n) or {}).get('herkunft') or 'signatur')
        # „Zustand von self VOR dem Aufruf“ (Entscheidung 3) für alle Korpusaufrufe: die frische Instanz aus dem Rezept.
        k = f'{n}.__init__~instanz#0'
        musterkarte[k] = []
        TIEFE[0] += 1
        try:
            fehl = []
            beob[k] = knapp(text_von(instanz(n), fehl))
            if fehl:
                _unvoll(f'{n}.__init__', fehl)
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
           'korpus_erweitert': ERWEITERT[0], 'nicht_ladbar': nicht_ladbar, 'erreicht': erreicht, 'teilweise': teilweise,
           'unvollstaendig': unvollstaendig, 'sonde_ausfall': sonde_ausfall, 'transparent': sorted(TRANSPARENT),
           'last_aufrufe': LAST_AUFRUFE, 'last_ohne_sonde': LAST_OHNE_SONDE}
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
