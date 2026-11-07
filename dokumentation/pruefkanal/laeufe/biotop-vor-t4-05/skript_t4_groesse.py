"""Entscheidung 4 (Behebungsrunde 5): Kappe der Verfälschungsläufe an einem Kandidaten in T4-Größe messen.

Aufbau (gestellt, dokumentiert): ein Python-Prüfwerk mit N Modulen × F Funktionen (Text-, Zahlen- und Listenfunktionen),
wie ein T4-Werk ohne Testsammlung plus die Soll-Tests, die ein Schwarmkandidat mitbringen oder das Werk nach
Generation 0 haben könnte. Der Kandidat ändert G Funktionen in einem Zug (eine breite Behebung, wie sie im T4-Maßstab zu
erwarten ist). Gemessen durch `aegis.pruefen` in der echten Kammer, gestellt nur Modell und Laufzeit:
  - Bedarf an Verfälschungsläufen (|bedarf|), Kappe, ausgelassen; Kammerläufe gesamt; Dauer;
  - Urteil mit Kappe 24 (Vorgabe) und — zum Vergleich — ohne Kappe (Kappe = Bedarf).
Kein Modellaufruf. Aufruf: python t4_groesse.py <baumkopie> > T4-GROESSE.txt"""
import json
import sqlite3
import sys
import tempfile
import time
from pathlib import Path
from types import SimpleNamespace

BAUM = Path(sys.argv[1])
sys.path.insert(0, str(BAUM))
from biotop.kern import datenbank, messgeraet  # noqa: E402
from biotop.organe import aegis, kammer  # noqa: E402
from biotop.organe import verhaltensvergleich as vv  # noqa: E402

kammer.IMAGE = 'biotop-kammer:1'
N_MODULE, F_JE_MODUL, G_GEAENDERT = 6, 5, 8
PAKET = 'grosswerk'


def modul_quelle(m: int, geaendert: set[str]) -> str:
    z = [f'"""Modul m{m} des Prüfwerks in T4-Größe."""\n']
    for f in range(F_JE_MODUL):
        n = f'm{m}_f{f}'
        art = f % 3
        if art == 0:          # Text: Weißraum normieren (Formvarianten)
            koerper = '"_".join(text.split())' if n in geaendert else '" ".join(text.split())'
            z.append(f'\n\ndef {n}(text: str) -> str:\n    return {koerper}\n')
        elif art == 1:        # Zahl
            koerper = 'x * 2 + 1' if n in geaendert else 'x * 2'
            z.append(f'\n\ndef {n}(x: int) -> int:\n    return {koerper}\n')
        else:                 # Liste
            koerper = 'sorted(xs, reverse=True)' if n in geaendert else 'sorted(xs)'
            z.append(f'\n\ndef {n}(xs: list[int]) -> list[int]:\n    return {koerper}\n')
    return ''.join(z)


def soll_tests(m: int, geaendert: set[str]) -> dict[str, str]:
    """Je geänderter Funktion ein Test je Formvariante des neuen Verhaltens — an der Vorgeneration rot, am Kandidaten
    grün (die Tests liegen im Werk, wie Gruppe B in test_vor_t4_03)."""
    out = {}
    for f in range(F_JE_MODUL):
        n = f'm{m}_f{f}'
        if n not in geaendert:
            continue
        art = f % 3
        if art == 0:
            faelle = {'gew': ('a b', 'a_b'), 'tab': ('a\tb', 'a_b'), 'lf': ('a\nb', 'a_b'), 'crlf': ('a\r\nb', 'a_b'),
                      'nbsp': ('a\u00a0b', 'a_b'), 'doppelt': ('a  b', 'a_b'), 'rand': (' a b ', 'a_b'),
                      'gross': ('A B', 'A_B')}
        elif art == 1:
            faelle = {'eins': (1, 3), 'null': (0, 1), 'neg': (-1, -1)}
        else:
            faelle = {'drei': ([1, 3, 2], [3, 2, 1]), 'leer': ([], [])}
        for k, (e, x) in faelle.items():
            out[f'tests/test_werk_{n}_{k}.py'] = (f'from {PAKET}.werk.m{m} import {n}\n\n\ndef test_{n}_{k}():\n'
                                             f'    assert {n}({e!r}) == {x!r}\n')
    return out


def anlegen(w: Path, geaendert: set[str]) -> dict[str, str]:
    (w / PAKET / 'werk').mkdir(parents=True)
    (w / 'tests').mkdir()
    (w / PAKET / '__init__.py').write_text('')
    (w / PAKET / 'werk' / '__init__.py').write_text('')
    (w / 'pyproject.toml').write_text(f'[project]\nname = "{PAKET}"\nversion = "0.1.0"\n')
    (w / 'tests' / 'test_werk_grund.py').write_text('def test_werk_grund():\n    assert True\n')
    code, tests = {}, {}
    for m in range(N_MODULE):
        (w / PAKET / 'werk' / f'm{m}.py').write_text(modul_quelle(m, set()))
        code[f'{PAKET}/werk/m{m}.py'] = modul_quelle(m, geaendert)
        tests.update(soll_tests(m, geaendert))
    for p, t in tests.items():
        (w / p).write_text(t)
    return code


REF = ('import sys\nsys.path.insert(0, "/werk")\n\n\ndef last_werk():\n'
       + ''.join(f'    from {PAKET}.werk.m{m} import ' + ', '.join(f'm{m}_f{f}' for f in range(F_JE_MODUL)) + '\n'
                 for m in range(N_MODULE))
       + '    for i in range(20):\n'
       + ''.join(f'        m{m}_f{f}(' + ('"wort wort"' if f % 3 == 0 else 'i' if f % 3 == 1 else '[i, 3, 1]') + ')\n'
                 for m in range(N_MODULE) for f in range(F_JE_MODUL)))


def diff(w: Path, code: dict[str, str]) -> str:
    import difflib
    d = ''
    for p, neu in sorted(code.items()):
        alt = (w / p).read_text()
        if alt != neu:
            d += ''.join(difflib.unified_diff(alt.splitlines(True), neu.splitlines(True), f'a/{p}', f'b/{p}'))
    return d


def lauf(kappe: int | None, geaendert: set[str]) -> dict:
    with tempfile.TemporaryDirectory(dir='/tmp') as d:
        w = Path(d) / 'werk'
        code = anlegen(w, geaendert)
        con = sqlite3.connect(':memory:', isolation_level=None)
        con.row_factory = sqlite3.Row
        con.executescript(datenbank.SCHEMA)
        con.execute("INSERT INTO kandidaten(id,lauf_id,generation,bereich,nische,status,diff) VALUES(7,1,1,'werk','sicher','erzeugt',?)",
                    (diff(w, code),))
        aegis.aufrufen = lambda *a, **k: SimpleNamespace(text='KEIN ANGRIFF')
        basis = messgeraet.messen(w, ['werk'], PAKET, REF)
        if not basis.get('gueltig'):
            return {'fehler': 'Basis ungültig: ' + str(basis.get('grund'))[:300]}
        messgeraet.laufzeit_messen = lambda werk, bereiche, paket, ref, dateien=None, zeitlimit_s=150: \
            {'gueltig': True, 'grund': '', 'bereiche': {b: {'laufzeit_ms': 5.0} for b in bereiche}}
        bedarf_gesehen = {}
        alt_bedarf = vv.verfaelschungsbedarf

        def bedarf(*a, **k):
            b = alt_bedarf(*a, **k)
            bedarf_gesehen['n'] = len(b)
            return b
        vv.verfaelschungsbedarf = bedarf
        vv.VERFAELSCHUNG_KAPPE = kappe if kappe is not None else 10 ** 6
        t0 = time.monotonic()
        with kammer.zaehlung() as kl:
            u = aegis.pruefen(con, 1, 1, 7, w, PAKET, ['werk'], [], basis, basis, REF, {'_rauschtoleranz': {'werk': 1.2}},
                              referenzlast_laufzeit=REF)
        vv.verfaelschungsbedarf = alt_bedarf
        z = con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil' ORDER BY nr DESC LIMIT 1").fetchone()
        v = json.loads(z[0]).get('verhalten') or {}
        dz = v.get('deckung_zaehlung') or {}
        return {'kappe': kappe, 'status': u['status'], 'grund': str(u['grund'])[:300], 'bedarf': bedarf_gesehen.get('n'),
                'verfaelschungen': dz.get('verfaelschungen'), 'ausgelassen': dz.get('ausgelassen'),
                'abweichungen': v.get('anzahl_abweichungen'), 'ungedeckt': len(v.get('ungedeckt') or []),
                'beobachtet': v.get('beobachtete_funktionen'), 'kammerlaeufe': len(kl),
                'dauer_s': round(time.monotonic() - t0, 1)}


if __name__ == '__main__':
    geaendert = {f'm{m}_f{f}' for m in range(N_MODULE) for f in range(F_JE_MODUL)}
    geaendert = set(sorted(geaendert)[:G_GEAENDERT * 2:2])        # jede zweite Funktion, G Stück
    print(json.dumps({'module': N_MODULE, 'funktionen': N_MODULE * F_JE_MODUL, 'geaendert': sorted(geaendert),
                      'zeilen_werk': sum(modul_quelle(m, set()).count('\n') for m in range(N_MODULE))}, ensure_ascii=False))
    for kappe in (24, None):
        print(json.dumps(lauf(kappe, geaendert), ensure_ascii=False), flush=True)
