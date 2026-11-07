"""Vorprobe Runde 5 (lokal, ohne Kammer): (1) object.__getstate__ / Member-Deskriptoren als unabhängige Aufzählung der
Datenattribute; (2) Auswertung STUFE2-EICHUNG.jsonl je Variante (Sperren, Toleranzen, längster Kammerlauf)."""
import collections
import csv
import dataclasses
import io
import json
import pathlib
import types


class A:
    def __init__(self):
        self.x = 1


class S:
    __slots__ = ('stand',)

    def __init__(self):
        self.stand = 1


class M:
    __slots__ = ('__stand',)

    def __init__(self):
        self.__stand = 1


class B:
    __slots__ = ('stand',)

    def __init__(self):
        self.stand = 1


class K(B):
    __slots__ = ('name',)

    def __init__(self):
        super().__init__()
        self.name = 'k'


class KD(B):
    def __init__(self):
        super().__init__()
        self.extra = 2


@dataclasses.dataclass(slots=True)
class DS:
    stand: int


@dataclasses.dataclass
class DX:
    a: int

    def __post_init__(self):
        self.b = 2


class L(list):
    def __init__(self):
        super().__init__([1])
        self.meta = 'm'


class U(S):
    __slots__ = ()


def member(x):
    out = []
    for k in type(x).__mro__:
        for n, d in vars(k).items():
            if isinstance(d, types.MemberDescriptorType):
                try:
                    d.__get__(x, type(x))
                    out.append(n)
                except AttributeError:
                    pass
    return out


proben = {'A': A(), 'S': S(), 'M': M(), 'K': K(), 'KD': KD(), 'DS': DS(1), 'DX': DX(1), 'L': L(), 'U': U(),
          'Path': pathlib.Path('a/b'), 'StringIO': io.StringIO('x'), 'csv.reader': csv.reader(io.StringIO('a')),
          'DictReader': csv.DictReader(io.StringIO('a\n1')), 'deque': collections.deque([1]), 'slice': slice(1, 2)}
for n, x in proben.items():
    try:
        s = object.__getstate__(x)
        st = (type(s).__name__, s if not isinstance(s, (list,)) else '…')
    except Exception as e:  # noqa: BLE001
        st = ('FEHLER', f'{type(e).__name__}: {e}')
    print(f'{n:11} member={member(x)} getstate={st}')

print('\n== Eichung Stufe 2 (eingang-Wiederholungen)')
z = [json.loads(l) for l in open('/root/biotop-vor-t4-05/proben/STUFE2-EICHUNG.jsonl')]
je = collections.defaultdict(list)
for r in z:
    je[r['variante']].append(r)
for v, rs in je.items():
    gesperrt = sum(1 for r in rs if r['gesperrt'])
    tol = collections.defaultdict(list)
    for r in rs:
        for b, t in (r['toleranz'] or {}).items():
            tol[b].append(t)
        if 'eingang' in r['gesperrt']:
            tol['eingang'].append(r['eingang']['toleranz'])
    lang = max(max(r['kammerlauf_s'] or [0]) for r in rs)
    print(f"{v:8} n={len(rs)} mit_sperre={gesperrt} gesperrt_je={collections.Counter(b for r in rs for b in r['gesperrt'])} "
          f"längster_kammerlauf={lang}s max_toleranz={ {b: max(t) for b, t in sorted(tol.items())} }")
