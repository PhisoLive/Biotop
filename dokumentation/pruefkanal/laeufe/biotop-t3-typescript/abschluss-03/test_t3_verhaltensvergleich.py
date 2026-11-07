"""Verhaltensvergleich alt gegen neu: „schneller, aber falsch" muss auffallen.

Befund aus Lauf 37: Kandidat K2934 baute einen WeakMap-Cache in `geordnet()` ein, der
an der Array-Referenz hängt und nur die Länge prüft. Gemessen am echten Werk:
`quantil` liefert nach Mutation desselben Arrays 3 statt 300, `spannweite` 8 statt 80.
Der Kandidat wurde angenommen — für 49 % Laufzeitgewinn, ohne dass ein Test das Verhalten
prüfte. Das Biotop optimierte die Messung statt den Code, und niemand sah es.

Die Abwehr: Vor der Annahme werden Vorgeneration und Kandidat mit denselben Eingaben
aufgerufen und ihre Ausgaben verglichen — ausdrücklich auch als FOLGE (aufrufen, Eingabe
an Ort und Stelle ändern, erneut aufrufen) und mit ALIASEN (dieselbe Referenz mehrfach).
Genau diese Muster fängt ein Einzelaufruf nicht.

Jede Abweichung muss durch einen Test gedeckt sein, den die Vorgeneration NICHT besteht
und der Kandidat besteht — sonst ist sie eine unbelegte Verhaltensänderung und der
Kandidat wird abgelehnt.
"""
import json
from pathlib import Path

import pytest

from biotop.organe import verhaltensvergleich as vv


def test_gleiche_ausgaben_sind_kein_befund():
    alt = {'quantil(x,1)': 3, 'spannweite(y)': 8}
    neu = {'quantil(x,1)': 3, 'spannweite(y)': 8}
    r = vv.vergleichen(alt, neu, gedeckt=set())
    assert r['abweichungen'] == []
    assert r['ungedeckt'] == []
    assert r['tragfaehig'] is True


def test_abweichung_ohne_deckung_ist_ablehnung():
    """Der K2934-Fall: Folge-Aufruf liefert anderes Ergebnis, kein Test deckt es."""
    alt = {'quantil(x,1)': 3, 'quantil(x,1)@nach_mutation': 300}
    neu = {'quantil(x,1)': 3, 'quantil(x,1)@nach_mutation': 3}
    r = vv.vergleichen(alt, neu, gedeckt=set())
    assert r['abweichungen'] == ['quantil(x,1)@nach_mutation']
    assert r['ungedeckt'] == ['quantil(x,1)@nach_mutation']
    assert r['tragfaehig'] is False
    assert 'ungedeckt' in r['grund']


def test_abweichung_mit_deckung_ist_zulaessig():
    """Der K2868-Fall: S1 behoben, ein Test deckt die Änderung."""
    alt = {'ausdruck("1+1")': 2, 'ausdruck("gewicht*2")': 'Fehler:ReferenceError'}
    neu = {'ausdruck("1+1")': 2, 'ausdruck("gewicht*2")': 'Fehler:SyntaxError'}
    r = vv.vergleichen(alt, neu, gedeckt={'ausdruck("gewicht*2")'})
    assert r['abweichungen'] == ['ausdruck("gewicht*2")']
    assert r['ungedeckt'] == []
    assert r['tragfaehig'] is True


def test_reine_beschleunigung_ohne_verhaltensaenderung_ist_zulaessig():
    """Der S2-Fall: O(n²) → O(n), alle Ausgaben identisch."""
    alt = {f'planen(n={n})': f'ergebnis{n}' for n in (40, 80, 160)}
    neu = dict(alt)
    r = vv.vergleichen(alt, neu, gedeckt=set())
    assert r['tragfaehig'] is True
    assert r['abweichungen'] == []


def test_teilweise_gedeckt_reicht_nicht():
    alt = {'a': 1, 'b': 2}
    neu = {'a': 9, 'b': 8}
    r = vv.vergleichen(alt, neu, gedeckt={'a'})
    assert r['abweichungen'] == ['a', 'b']
    assert r['ungedeckt'] == ['b']
    assert r['tragfaehig'] is False


def test_fehlende_beobachtung_ist_kein_stillschweigen():
    """Kann eine Seite nicht beobachtet werden, ist das ein Befund, keine Gleichheit."""
    alt = {'a': 1, 'b': 2}
    neu = {'a': 1}
    r = vv.vergleichen(alt, neu, gedeckt=set())
    assert 'b' in r['abweichungen']
    assert r['tragfaehig'] is False


# ---------------------------------------------------------------- Deckung und Module
def test_geaenderte_module_sind_die_quellmodule_des_kandidaten():
    code = {'src/zahlen/statistik.ts': 'x', 'src/tarife/ausdruck.ts': 'y', 'README.md': 'z',
            'src/typen.d.ts': 'q'}
    assert vv.geaenderte_module(code) == ['tarife/ausdruck', 'zahlen/statistik']


def test_funktion_wird_aus_der_beobachtung_gelesen():
    assert vv.funktion_von('zahlen/statistik:quantil#0@mutation') == 'quantil'
    assert vv.funktion_von('zahlen/statistik:quantil#7') == 'quantil'
    assert vv.funktion_von('korpus:beobachten') is None


def test_deckung_verlangt_aufruf_der_abweichenden_funktion():
    """Ein Test deckt nur, was er aufruft — ein Test auf median deckt quantil nicht."""
    abw = ['zahlen/statistik:quantil#0@mutation', 'zahlen/statistik:spannweite#1']
    tests = {'test_zahlen.test.ts::median neu': "expect(median([1,2,3])).toBe(2)",
             'test_zahlen.test.ts::spannweite frisch': "expect(spannweite(w)).toBe(80)"}
    d = vv.deckung(abw, tests)
    assert d == {'zahlen/statistik:spannweite#1': ['test_zahlen.test.ts::spannweite frisch']}


def test_gegenprobe_deckung_ohne_passenden_test_bleibt_leer():
    """Ohne diese Probe würde eine Deckung, die jede Abweichung als gedeckt meldet, ebenso bestehen."""
    d = vv.deckung(['zahlen/statistik:quantil#0@alias'], {'t::x': "expect(quantilen(w)).toBe(1)"})
    assert d == {}


@pytest.fixture
def ts_werk(tmp_path):
    """Ein TypeScript-Werk (package.json + src/*.ts). Die Sonde gibt es nur für TypeScript;
    an einem Pfad ohne TS-Werk enthält sich das Organ — korrigiert: die ersten Fassungen dieser
    Tests zeigten auf '/nicht/da' und prüften damit die Enthaltung statt des gemeinten Zweigs."""
    w = tmp_path / 'werk'
    (w / 'src' / 'm').mkdir(parents=True)
    (w / 'package.json').write_text('{"type":"module"}')
    (w / 'src' / 'm' / 'a.ts').write_text('export function f(x: number): number { return x; }\n')
    return w


def test_python_werk_enthaelt_sich_gezaehlt(tmp_path):
    """Gegenprobe zum TS-Zweig: ohne Sonde für die Sprache kein Urteil — aber eine benannte Enthaltung."""
    (tmp_path / 'paket').mkdir()
    r = vv.pruefen(tmp_path, {'paket/a.py': 'x'}, 'last', ['paket'], {})
    assert r['geurteilt'] is False and r['tragfaehig'] is True
    assert r['grund_art'] == 'sprache_ohne_sonde'


def test_ohne_quellaenderung_nichts_zu_vergleichen(ts_werk):
    r = vv.pruefen(ts_werk, {'tests/test_x.test.ts': 'x'}, 'last', ['zahlen'], {})
    assert r['tragfaehig'] is True and r['grund_art'] == 'keine_quellaenderung'
    assert r['geurteilt'] is True


def test_ohne_referenzlast_ist_gleichheit_unbelegt(ts_werk):
    r = vv.pruefen(ts_werk, {'src/zahlen/a.ts': 'x'}, None, ['zahlen'], {})
    assert r['ausgefuehrt'] is False and r['tragfaehig'] is False
    assert r['grund_art'] == 'ohne_referenzlast'


def test_unausfuehrbare_sonde_ist_kein_beleg_fuer_gleichheit(ts_werk, monkeypatch):
    seiten = iter([{'gueltig': True, 'beobachtungen': {'m:f#0': '1'}},
                   {'gueltig': False, 'art': 'inhalt', 'grund': 'Modul lädt nicht'}])
    monkeypatch.setattr(vv, 'beobachten', lambda *a, **k: next(seiten))
    r = vv.pruefen(ts_werk, {'src/m.ts': 'x'}, 'last', ['m'], {})
    assert r['ausgefuehrt'] is False and r['tragfaehig'] is False
    assert r['grund_art'] == 'sonde_kandidat_inhalt'


def test_abweichung_mit_deckendem_test_ist_tragfaehig(ts_werk, monkeypatch):
    alt = {'m/a:f#0': '1', 'm/a:f#0@alias': '1'}
    neu = {'m/a:f#0': '2', 'm/a:f#0@alias': '2'}
    seiten = iter([{'gueltig': True, 'beobachtungen': alt, 'eingewickelt': {'m/a': ['f']}, 'aufgerufen': {'m/a:f': 0}},
                   {'gueltig': True, 'beobachtungen': neu, 'eingewickelt': {'m/a': ['f']}, 'aufgerufen': {'m/a:f': 0}}])
    monkeypatch.setattr(vv, 'beobachten', lambda *a, **k: next(seiten))
    r = vv.pruefen(ts_werk, {'src/m/a.ts': 'x'}, 'last', ['m'], {'t.test.ts::f neu': 'expect(f(1)).toBe(2)'})
    assert r['tragfaehig'] is True and r['anzahl_abweichungen'] == 2 and r['ungedeckt'] == []


def test_abweichung_ohne_deckenden_test_ist_ablehnung(ts_werk, monkeypatch):
    alt = {'m/a:f#0@mutation': '300'}
    neu = {'m/a:f#0@mutation': '3'}
    seiten = iter([{'gueltig': True, 'beobachtungen': alt}, {'gueltig': True, 'beobachtungen': neu}])
    monkeypatch.setattr(vv, 'beobachten', lambda *a, **k: next(seiten))
    r = vv.pruefen(ts_werk, {'src/m/a.ts': 'x'}, 'last', ['m'], {})
    assert r['tragfaehig'] is False and r['ungedeckt'] == ['m/a:f#0@mutation']
    assert r['werte']['m/a:f#0@mutation'] == ['300', '3']
