"""Verhaltenssonde für Python-Werke (T4, Grundsatz 11). Läuft in der netzlosen Kammer (cwd /werk):
    python _messgeraet/verhalten.py _messgeraet/anfrage.json
Gegenstück zu kern/ts/verhalten.mjs + verhalten-runner.mjs, im selben Umfang:
- Jede öffentliche Funktion (Modulebene, Name ohne '_') der geänderten Module wird eingewickelt, auch dort, wo andere
  Module des Pakets sie schon gebunden haben (Re-Export, `from … import`). Dann läuft die Referenzlast
  (`beobachten()`, `last_<bereich>()`). Je Funktion werden die ersten KAPPE äußeren Aufrufe beobachtet (Folge #0…#7),
  jeder in vier Mustern: der Aufruf selbst; @alias (dieselben Referenzen sofort noch einmal); @mutation (Zahlenblätter
  der Eingaben an Ort und Stelle geändert — gleiche Referenzen, gleiche Längen); @nach_ruecksetzung (zurückgesetzt,
  erneut). Vor jedem Zusatzaufruf wird der Zustand der Eingaben festgehalten und danach wiederhergestellt.
- Randfall-Korpus (~rand#i) aus der deklarierten Signatur (Typannotationen) der Vorgeneration und beobachteten
  Beispielen; Formvarianten (~form#j) derselben Eingaben (Weißraum, Groß/Klein, Zahlform, Zahltyp, Behälter,
  Schlüsselfolge) — die Weißraumlücke aus T3 (K2868) zeigt, dass Randwerte allein nicht reichen.
- Modus 'deckung': führt Tests (pytest) mit Aufzeichnern aus und hält je Test jeden Aufruf fest (Funktion, kanonische
  Argumente, Identität und Inhalt veränderlicher Argumente) — Grundlage der Deckung je Abweichung.
Ausgabe: eine Zeile @@VV@@<json>@@ENDE@@ auf stdout."""
import ast
import dataclasses
import enum
import hashlib
import importlib
import inspect
import json
import math
import os
import re
import sys
import traceback
import types

REQ = {}
KAPPE, RAND_KAPPE, FORM_KAPPE = 8, 16, 16
beob, argtext, zaehler, zaehler_rand, zaehler_form, beispiele = {}, {}, {}, {}, {}, {}
aufrufe = []
AKTUELL = ['']
TIEFE = [0]
_FEHLT = object()


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
            return {'__fehler': type(x).__name__, 'meldung': str(x)[:200]}
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
        return {'__objekt': type(x).__qualname__, 'repr': repr(x)[:200]}
    finally:
        anc.discard(id(x))


def text_von(x):
    return json.dumps(kan(x), sort_keys=True, ensure_ascii=False, default=str)


def eingabe_text(args, kwargs):
    try:
        return knapp(text_von([list(args), kwargs]))
    except Exception:  # noqa: BLE001
        return '__unkanonisch'


def knapp(t):
    if len(t) <= 200:
        return t
    return t[:120] + '…#' + hashlib.sha256(t.encode('utf-8', 'surrogatepass')).hexdigest()[:16]


def wert(f):
    try:
        v = f()
    except BaseException as e:  # noqa: B902 — jede Ausnahme ist ein beobachtetes Verhalten
        return {'text': 'Fehler:' + type(e).__name__, 'fehler': e}
    if inspect.isgenerator(v) or inspect.iscoroutine(v) or inspect.isasyncgen(v) or (
            hasattr(v, '__next__') and not isinstance(v, (str, bytes, list, tuple, dict, set))):
        return {'text': '__iterator', 'roh': v}
    try:
        return {'text': text_von(v), 'roh': v}
    except Exception as e:  # noqa: BLE001
        return {'text': '__unkanonisch:' + type(e).__name__, 'roh': v}


# ---------------------------------------------------------------- Zustand der Eingaben
def _instanz(x):
    return hasattr(x, '__dict__') and not isinstance(
        x, (type, types.ModuleType, types.FunctionType, types.MethodType, types.BuiltinFunctionType, enum.Enum))


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
            if art == 'list':
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


def muster(schl, args, kwargs, call):
    """Ein Aufruf mit den vier Mustern. Rückgabe: das Ergebnis des echten Aufrufs ({roh} oder {fehler})."""
    TIEFE[0] += 1
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
        return erst
    finally:
        TIEFE[0] -= 1


# ---------------------------------------------------------------- Einwickeln
def _metadaten(w, orig):
    for a in ('__name__', '__qualname__', '__doc__', '__module__'):
        try:
            setattr(w, a, getattr(orig, a))
        except Exception:  # noqa: BLE001
            pass
    w.__wrapped__ = orig
    return w


def wickeln(name, orig):
    def w(*args, **kwargs):
        if TIEFE[0] > 0:
            return orig(*args, **kwargs)
        i = zaehler[name] = zaehler.get(name, -1) + 1
        if i == 0 and name not in beispiele:
            try:
                beispiele[name] = [[pack(a) for a in args], {k: pack(v) for k, v in kwargs.items()}]
            except Exception:  # noqa: BLE001 — nicht packbar: ohne Beispiel
                beispiele[name] = None
        if i >= KAPPE:
            return orig(*args, **kwargs)
        erst = muster(f'{name}#{i}', args, kwargs, orig)
        if 'fehler' in erst:
            raise erst['fehler']
        return erst['roh']
    return _metadaten(w, orig)


_GESEHEN = set()
ZUSTAND = {}


def deck_wickeln(name, orig):
    """Aufzeichner der deckenden Tests: je Aufruf Test, Funktion, Eingabe (vor dem Aufruf) und Ergebnis — genau so
    geschrieben, wie die Sonde Beobachtungen schreibt (wert/knapp). Ausnahmen gehen unverändert an den Test."""
    def w(*args, **kwargs):
        eintrag = {'test': AKTUELL[0], 'f': name, 'args': eingabe_text(args, kwargs), 'erg': None}

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
        return v
    return _metadaten(w, orig)


def alle_wickeln(module, fabrik):
    eingewickelt, nicht, ersatz = {}, {}, {}
    for m in module:
        mod = sys.modules[m]
        namen = []
        for name, obj in list(vars(mod).items()):
            if name.startswith('_') or not inspect.isfunction(obj) or obj.__module__ != mod.__name__:
                continue
            w = fabrik(f'{m}:{name}', obj)
            setattr(mod, name, w)
            ersatz[id(obj)] = (obj, w)
            namen.append(name)
        eingewickelt[m] = sorted(namen)
        andere = sorted(n for n, o in vars(mod).items() if not n.startswith('_') and inspect.isclass(o)
                        and o.__module__ == mod.__name__)
        if andere:
            nicht[m] = ['class ' + n for n in andere]
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
    """Öffentliche Funktionen der Modulebene → Liste der Annotationen ihrer positionalen Parameter (Quelltext)."""
    out = {}
    try:
        baum = ast.parse(inspect.getsource(mod))
    except Exception:  # noqa: BLE001
        return out
    for k in baum.body:
        if isinstance(k, (ast.FunctionDef, ast.AsyncFunctionDef)) and not k.name.startswith('_'):
            if any(d is None for d in k.args.kw_defaults):
                continue            # Pflicht-Schlüsselwortparameter: keine positionalen Randfälle
            params = list(k.args.posonlyargs) + list(k.args.args)
            out[k.name] = [ast.unparse(p.annotation) if p.annotation is not None else '' for p in params]
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
    return x


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
        return p
    return f(p)


def schrumpfen(p):
    """leer, einzeln, doppelt, Grenzwerte — aus einem beobachteten (gepackten) Wert."""
    out = [p]
    if isinstance(p, list):
        out.append([])
        if p:
            out += [[p[0]], [p[0], p[0]], [_blaetter(p[0], lambda v: 0 if _zahl(v) else ('' if isinstance(v, str) else v))]]
    elif isinstance(p, dict) and ('__dc' in p or '__dict' in p or '__tupel' in p):
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
        out += ['', ' ']
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


def typ_kandidaten(t, b, stufe=0):
    t = (t or '').strip().strip('"\'')
    t = re.sub(r'^(?:typing|t|collections\.abc)\.', '', t)
    if not t or stufe > 3:
        return schrumpfen(b) if b is not None else []
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
        return ['', 'a', ' ', 'Ä-1', 'x' * 40]
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


def _eindeutig(listen, kappe):
    gesehen, out = set(), []
    for l in listen:
        s = json.dumps(l, sort_keys=True, default=str)
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
    out = []
    if ' ' in s:
        out += [s.replace(' ', r) for r in ('\t', '\n', '  ', '\r\n', '\u00a0')]
    out += [' ' + s, s + ' ', '\t' + s + '\n']
    if s.upper() != s:
        out.append(s.upper())
    if s.lower() != s:
        out.append(s.lower())
    m = re.search(r'\d+(?:\.\d+)?', s)
    if m:
        z, a, e = m.group(0), s[:m.start()], s[m.end():]
        out += [a + '0' + z + e, a + z + ('0' if '.' in z else '.0') + e]
    return out


def form_werte(p):
    """Dieselbe Eingabe in anderer Form (Weißraum, Groß/Klein, Zahlform im Text, Zahltyp, Behälter, Schlüsselfolge)."""
    out = []
    if isinstance(p, str) and p:
        out += _text_formen(p)
    elif isinstance(p, bool) or p is None:
        pass
    elif isinstance(p, int):
        out.append(float(p))
    elif isinstance(p, float) and p.is_integer() and abs(p) < 2 ** 53:
        out.append(int(p))
    elif isinstance(p, list):
        out.append({'__tupel': p})
    elif isinstance(p, dict) and ('__dict' in p or '__dc' in p):
        if '__dict' in p and len(p['__dict']) > 1:
            out.append({'__dict': list(reversed(p['__dict']))})
        felder = p['__dict'] if '__dict' in p else list(p['f'].items())
        n = 0
        for i, (k, v) in enumerate(felder):
            if isinstance(v, str) and v and n < 2:
                n += 1
                for w in _text_formen(v)[:6]:
                    if '__dict' in p:
                        d = [list(x) for x in p['__dict']]; d[i] = [k, w]; out.append({'__dict': d})
                    else:
                        out.append({'__dc': p['__dc'], 'f': {**p['f'], k: w}})
    return [v for v in out if json.dumps(v, sort_keys=True, default=str) != json.dumps(p, sort_keys=True, default=str)]


def formvarianten(grund):
    listen = []
    for j, p in enumerate(grund):
        for v in form_werte(p):
            listen.append(grund[:j] + [v] + grund[j + 1:])
    return _eindeutig(listen, FORM_KAPPE)


# ---------------------------------------------------------------- Ablauf
def korpus_randfaelle(module, signaturen):
    quelle = REQ.get('beispiele') if REQ.get('beispiele') is not None else beispiele
    for m in module:
        mod = sys.modules[m]
        for f, typen in (signaturen.get(m) or {}).items():
            fn = getattr(mod, f, None)
            if not callable(fn):
                continue                      # vom Kandidaten entfernt: Python weist das getrennt aus
            name = f'{m}:{f}'
            bsp = (quelle or {}).get(name)
            listen = argumentlisten(typen or [], bsp[0] if isinstance(bsp, list) and bsp else None)
            for art, ls, zz in (('rand', listen, zaehler_rand), ('form', formvarianten(listen[0] if listen else []), zaehler_form)):
                for i, liste in enumerate(ls):
                    try:
                        args = [unpack(v) for v in liste]
                    except Exception:  # noqa: BLE001 — Beispiel am Kandidaten nicht herstellbar
                        continue
                    erst = muster(f'{name}~{art}#{i}', args, {}, fn)
                    if 'fehler' not in erst:
                        zz[name] = zz.get(name, 0) + 1


def main():
    global KAPPE, RAND_KAPPE, FORM_KAPPE
    REQ.clear()
    REQ.update(json.load(open(sys.argv[1], encoding='utf-8')))
    KAPPE, RAND_KAPPE, FORM_KAPPE = REQ.get('kappe') or 8, REQ.get('rand_kappe') or 16, REQ.get('form_kappe') or 16
    if '/werk' not in sys.path:
        sys.path.insert(0, '/werk')
    modus = REQ.get('modus', 'beobachten')
    module = REQ.get('module') or []
    try:
        for m in module:
            importlib.import_module(m)
    except BaseException as e:  # noqa: B902
        return {'gueltig': False, 'art': 'inhalt',
                'grund': 'Modul lädt nicht: ' + ''.join(traceback.format_exception_only(type(e), e))[-1500:]}
    signaturen = REQ.get('signaturen') or {m: signaturen_lesen(sys.modules[m]) for m in module}
    if modus == 'deckung':
        eingewickelt, _ = alle_wickeln(module, deck_wickeln)
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
        rc = pytest.main(['-q', '-p', 'no:cacheprovider', '--tb=no', *(REQ.get('testdateien') or [])], plugins=[Plugin()])
        ueberlauf = len(aufrufe) > 20000        # laut statt abgeschnitten
        return {'gueltig': int(rc) in (0, 1) and not ueberlauf, 'rc': int(rc), 'aufrufe': [] if ueberlauf else aufrufe,
                'zustand': ZUSTAND, 'ueberlauf': ueberlauf, 'eingewickelt': eingewickelt,
                'grund': 'Aufzeichnung über 20000 eindeutige Aufrufe — verworfen, nicht abgeschnitten' if ueberlauf else ''}
    eingewickelt, nicht = alle_wickeln(module, wickeln)
    ns = {}
    try:
        with open('_messgeraet/referenzlast.py', encoding='utf-8') as f:
            exec(compile(f.read(), '_messgeraet/referenzlast.py', 'exec'), ns)
    except BaseException as e:  # noqa: B902
        return {'gueltig': False, 'art': 'infrastruktur', 'grund': 'Referenzlast nicht ladbar: ' + repr(e)[:500]}
    korpus = [k for k in ['beobachten'] + ['last_' + b for b in REQ.get('bereiche') or []] if callable(ns.get(k))]
    for k in korpus:
        try:
            ns[k]()
            beob['korpus:' + k] = 'ok'
        except BaseException as e:  # noqa: B902
            beob['korpus:' + k] = 'Fehler:' + type(e).__name__
    korpus_randfaelle(module, signaturen)
    if module:
        korpus += ['randfaelle', 'formvarianten']
    out = {'gueltig': True, 'beobachtungen': beob, 'argumente': argtext, 'korpus': korpus, 'aufgerufen': zaehler,
           'aufgerufen_rand': zaehler_rand, 'aufgerufen_form': zaehler_form, 'kappe': KAPPE, 'rand_kappe': RAND_KAPPE,
           'form_kappe': FORM_KAPPE, 'signaturen': signaturen, 'eingewickelt': eingewickelt, 'nicht_eingewickelt': nicht}
    if REQ.get('beispiele') is None:
        out['beispiele'] = beispiele
    return out


if __name__ == '__main__':
    try:
        ergebnis = main()
    except BaseException as e:  # noqa: B902 — die Sonde selbst ist gescheitert: Messgerätausfall
        ergebnis = {'gueltig': False, 'art': 'infrastruktur', 'grund': 'Sondenfehler: ' + traceback.format_exc()[-1500:]}
    sys.stdout.write('\n@@VV@@' + json.dumps(ergebnis, ensure_ascii=False, default=str) + '@@ENDE@@\n')
