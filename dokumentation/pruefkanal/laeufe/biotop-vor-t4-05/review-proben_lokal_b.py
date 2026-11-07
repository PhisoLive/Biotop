"""Review vor T4-05 — lokale Rechenproben ohne Kammer (Prüfpunkt b): kan() der Sonde am Stand HEAD (verhalten_head.py,
aus `git show HEAD:biotop/kern/py/verhalten.py`). Je Paar (alt, neu) mit verschiedenem Zustand: gleiche kanonische Form
UND keine Meldung der Vollständigkeitsprüfung = BLIND (wieder „0 Abweichungen, tragfähig“ möglich). Danach gewöhnliche
Werte: löst die Vollständigkeitsprüfung eine Enthaltung aus (Fehlalarm-Risiko)? Kein Modell, kein Netz."""
import array
import collections
import datetime
import decimal
import functools
import importlib.util
import io
import logging
import os
import sys
import threading
import weakref

sys.dont_write_bytecode = True
os.environ['TMPDIR'] = '/tmp/review-vor-t4-05'
spec = importlib.util.spec_from_file_location('vh', '/tmp/review-vor-t4-05/verhalten_head.py')
vh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vh)
print('ITER_KAPPE', vh.ITER_KAPPE)


def erfasse(x):
    fehl = []
    try:
        t = vh.text_von(x, fehl)
    except Exception as e:  # noqa: BLE001
        t = '__unkanonisch:' + type(e).__name__
    return t, fehl


def paar(name, alt, neu):
    ta, fa = erfasse(alt)
    tn, fn = erfasse(neu)
    blind = ta == tn and not fa and not fn
    print(f'B {name}: gleich={ta == tn} fehlend={fa or fn} -> {"BLIND" if blind else "gesehen/enthalten"} | {ta[:110]}')


def einzeln(name, x):
    t, f = erfasse(x)
    print(f'F {name}: fehlend={f[:2]} -> {"ENTHALTUNG" if f else "ok"} | {t[:90]}')


# ---- b) Blinde Stellen der unabhängigen Aufzählung (object.__getstate__)
class Feld:                       # Deskriptor, Zustand außerhalb der Instanz
    def __init__(self):
        self.werte = weakref.WeakKeyDictionary()

    def __get__(self, obj, typ=None):
        return self if obj is None else self.werte.get(obj, 0)

    def __set__(self, obj, v):
        self.werte[obj] = v


class KontoD:
    stand = Feld()

    def __init__(self, s):
        self.stand = s


def konto_closure(s):
    zustand = {'s': s}

    class K:
        @property
        def stand(self):
            return zustand['s']
    return K()


class Betrag(decimal.Decimal):
    pass


class Tag(datetime.date):
    pass


class Puffer(collections.deque):
    pass


class Text(io.StringIO):
    pass


class Zahlen(array.array):
    pass


class Eigen:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __getstate__(self):
        return {'a': self.a}


class SlotDict:
    __slots__ = ('a', '__dict__')

    def __init__(self, a, b):
        self.a = a
        self.b = b


def f(x, y):
    return x + y


class Ziel:
    pass


z1, z2 = Ziel(), Ziel()
e1, e2 = ValueError('ungültig'), ValueError('ungültig')
e1.feld, e2.feld = 'plz', 'ort'
lang1, lang2 = ValueError('x' * 250 + 'A'), ValueError('x' * 250 + 'B')

paar('deskriptor_extern', KontoD(3), KontoD(6))
paar('property_closure', konto_closure(3), konto_closure(6))
paar('decimal_unterklasse', Betrag('1.5'), Betrag('3.0'))
paar('date_unterklasse', Tag(2026, 1, 1), Tag(2026, 1, 2))
paar('deque_unterklasse', Puffer([1, 2]), Puffer([1, 3]))
paar('stringio_unterklasse', Text('a'), Text('b'))
paar('array_unterklasse', Zahlen('i', [1, 2]), Zahlen('i', [1, 3]))
paar('memoryview', memoryview(b'ab'), memoryview(b'ac'))
paar('defaultdict_fabrik', collections.defaultdict(int), collections.defaultdict(list))
paar('weakref_ziel', weakref.ref(z1), weakref.ref(z2))
paar('partial_argumente', functools.partial(f, 1), functools.partial(f, 2))
paar('ausnahme_attribut', e1, e2)
paar('ausnahme_meldung_ab_200', lang1, lang2)
paar('eigenes_getstate(kontrolle)', Eigen(1, 2), Eigen(1, 3))
paar('slots_mit_dict(kontrolle)', SlotDict(1, 2), SlotDict(1, 3))
paar('array(kontrolle)', array.array('i', [1, 2]), array.array('i', [1, 3]))
paar('decimal(kontrolle)', decimal.Decimal('1.5'), decimal.Decimal('3.0'))


def wirft(m):
    def g():
        raise ValueError(m)
    return g


print('W geworfene Ausnahme, Meldung verschieden:', vh.wert(wirft('PLZ ungültig'))['text'], '|', vh.wert(wirft('Ort ungültig'))['text'])


# ---- b) Umgekehrt: gewöhnliche Werte, die jetzt eine Enthaltung auslösen
class Tokenizer:
    def __init__(self, t):
        self._it = iter(t.split())


class Knoten:
    def __init__(self, wert, weiter=None):
        self.wert, self.weiter = wert, weiter


def kette(n):
    k = None
    for i in range(n):
        k = Knoten(i, k)
    return k


class Dienst:
    def __init__(self):
        self.log = logging.getLogger('review.dienst')
        self.sperre = threading.Lock()
        self.zaehler = collections.Counter('abca')


class MitDatei:
    def __init__(self):
        self.puffer = io.StringIO('x')


einzeln('objekt_mit_listeniterator', Tokenizer('a b'))
einzeln('dict_mit_map', {'z': map(str, [1, 2])})
einzeln('tupel_mit_generator', (1, (x for x in [1])))
einzeln('verkettete_liste_12', kette(12))
einzeln('verkettete_liste_14', kette(14))
einzeln('verschachtelte_liste_14', functools.reduce(lambda a, _: [a], range(14), 0))
einzeln('dienst_logger_lock_counter', Dienst())
einzeln('objekt_mit_stringio', MitDatei())
einzeln('datetime', datetime.datetime(2026, 9, 24, 12, 0))
einzeln('counter', collections.Counter('abca'))
einzeln('ordereddict', collections.OrderedDict(a=1))
einzeln('object()', object())
gen = (x for x in [1, 2])
print('V _veraenderlich(generator) =', vh._veraenderlich(gen), '| _veraenderlich(list) =', vh._veraenderlich([1]))
print('V Argumentzustand [liste, generator] fehlend:', erfasse([[[1], gen], {}])[1][:1])
