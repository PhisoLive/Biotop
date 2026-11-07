"""EICH-4: reale JUnit-/Kammerzeugen, niemals defekte negative Kontrollen."""
from pathlib import Path
from copy import deepcopy
import hashlib
import json
import os
import re
import sqlite3
import xml.etree.ElementTree as ET

import pytest

from biotop.kern import datenbank, messgeraet
from biotop.organe import aegis, eichgegenstand, eichproben, kammer, verfassung, vertraege, vorspann

VERTRAG = 'tests/vertraege/test_vertrag_abnehmer_lieferant.py'
VERTRAGSTEST = VERTRAG + '::test_eichprobe_vertrag_neue_zusicherung'


@pytest.fixture
def vertragswerk(tmp_path):
    """Minimales eigenes Reviewwerk, keine produktiven Pfade/DBs."""
    werk = tmp_path / 'werk'
    dateien = {
        'beispiel/__init__.py': '',
        'beispiel/abnehmer/__init__.py': 'from .quelle import bericht\n',
        'beispiel/abnehmer/quelle.py': 'def bericht(zahl: float):\n    ergebnis = zahl + 1\n    return ergebnis\n',
        'beispiel/lieferant/__init__.py': 'from .quelle import wert\n',
        'beispiel/lieferant/quelle.py': 'def wert(zahl: float):\n    ergebnis = zahl * 2\n    return ergebnis\n',
        'tests/test_abnehmer.py': ('from beispiel.abnehmer import bericht\nEINGABE = 2\n'
                                  'def test_bericht():\n    assert bericht(EINGABE) == 3\n'),
        'tests/test_lieferant.py': 'from beispiel.lieferant import wert\ndef test_wert():\n    assert wert(2) == 4\n',
        VERTRAG: 'from beispiel.lieferant import wert\ndef test_alt():\n    assert wert(2) == 4\n',
    }
    for rel, code in dateien.items():
        p = werk / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(code)
    return werk


def test_contract_countercase_is_not_allowed_to_fail_inside_cloned_test(vertragswerk):
    """Review-Repro: EINGABE darf nicht verschwinden; konkreter Vertrag entscheidet."""
    rows = []
    for gegenprobe in (False, True):
        diff, _, belege, _ = eichproben._vertrag_vorbereiten(
            vertragswerk, 'beispiel', 'abnehmer', 'lieferant', VERTRAG, gegenprobe)
        dateien = aegis.kandidat_dateien(vertragswerk, diff)
        zeugen = aegis.junit_lauf(vertragswerk, 'beispiel', dateien, [VERTRAG])
        rows.append(zeugen[VERTRAGSTEST])
        print('KONKRETER VERTRAG', gegenprobe, zeugen)
    assert rows[1]['ok'] is True, 'Gegenprobe stirbt im geklonten Test statt den benannten Vertrag zu bestehen'
    assert rows[0]['ok'] is False and rows[0]['bestaetigt'] is True
    assert rows[0]['ort'] == 'beispiel/abnehmer/quelle.py'
    assert 'eichprobe_zusicherung' in rows[0]['meldung']


def _belegen(name, row):
    if os.environ.get('BIOTOP_VERTRAGSBELEGE'):
        ziel = Path(os.environ['BIOTOP_VERTRAGSBELEGE']) / f'{name}-{row["gegenprobe"]}.json'
        ziel.parent.mkdir(parents=True, exist_ok=True)
        ziel.write_text(json.dumps(row, ensure_ascii=False, indent=2))
    print(name, {k: row[k] for k in ('gegenprobe', 'pruefbar', 'bestanden', 'grund', 'kammerlaeufe')})


@pytest.fixture
def vertragspruefung(vertragswerk, tmp_path, request):
    db = datenbank.verbinden(tmp_path / 'vertrag.db')
    db.executescript(verfassung.SCHEMA)
    db.execute("INSERT INTO laeufe(id,werk_id,budget_eur,status,mass) VALUES(1,1,0,'angelegt',NULL)")
    vertraege.einlegen(db, 1, vertragswerk, {('abnehmer', 'lieferant'): (vertragswerk / VERTRAG).read_text()},
                      'isoliertes EICH-4-Reviewwerk')
    bereiche = ['abnehmer', 'lieferant']
    basis = messgeraet.messen(vertragswerk, bereiche, 'beispiel', None)
    assert basis['gueltig']
    g = dict(von_bereich='abnehmer', nach_bereich='lieferant', vertrag_pfad=VERTRAG)

    def pruefen(gegenprobe, name='vertrag'):
        row = eichproben._einzelprobe(db, 1, 1, vertragswerk, 'beispiel', bereiche, [],
                                     basis, basis, None, {}, 0, g, name, gegenprobe)
        _belegen(request.node.name, row)
        return row

    yield pruefen
    db.close()


@pytest.mark.parametrize('art', ['skip', 'xfail', 'fehlend', 'pass'])
def test_normgegenprobe_braucht_ausgefuehrtes_zeugenpaar(vertragswerk, vertragspruefung, art):
    """Die negative Normprobe misst ohne Normtest: JUnit davor bleibt Pflicht."""
    if art in ('skip', 'xfail'):
        code = ('import pytest\ndef pytest_runtest_setup(item):\n'
                "    if item.name == 'test_lieferant_eichprobe_norm':\n"
                f"        pytest.{art}('Normzeuge nicht ausgeführt')\n")
    elif art == 'fehlend':
        code = ('def pytest_collection_modifyitems(items):\n'
                "    items[:] = [i for i in items if i.name != 'test_lieferant_eichprobe_norm']\n")
    else:
        code = ''
    (vertragswerk / 'tests/conftest.py').write_text(code)
    row = vertragspruefung(True, 'norm')
    assert row['ausgefuehrt'] is True
    assert row['belege']['messung']['gueltig'] is True
    assert row['bestanden'] is False
    assert row['pruefbar'] is (art == 'pass'), \
        'Spätere Messung ersetzt kein ausgeführtes Norm-Zeugenpaar'
    batterie = _batterie_unit(row, 'norm')
    assert eichproben._vollstaendig(batterie['proben'], batterie['gegenproben']) is (art == 'pass')
    if art == 'pass':
        assert vorspann._qualitaet(batterie) == dict(positive=4, negative=4, erwartet_je=4)
    else:
        with pytest.raises(ValueError, match='gegenproben'):
            vorspann._qualitaet(batterie)


def _batterie_unit(gegenprobe, name='vertrag'):
    """Nur Verbraucher-Unit-Grenze: sieben gestellte Flags + eine echte Zeile.

    Kein Nachweis einer frisch ausgeführten Gesamtbatterie.
    """
    return {'bestanden': True,
            'proben': {n: dict(ausgefuehrt=True, pruefbar=True, bestanden=True) for n in eichproben.PROBEN},
            'gegenproben': {n: gegenprobe if n == name else
                           dict(ausgefuehrt=True, pruefbar=True, bestanden=False) for n in eichproben.PROBEN}}


@pytest.mark.parametrize('art', ['setup', 'aufruf', 'sammlung', 'fehlend', 'skip', 'xfail'])
def test_test_eigener_fehler_ist_keine_pruefbare_vertragsgegenprobe(vertragswerk, vertragspruefung, art):
    """Echte Fixturedefekte, keine erwarteten False-Kontrollen; setup war TDD-Rot."""
    if art in ('sammlung', 'fehlend'):
        code = ('def pytest_collection_modifyitems(items):\n'
                "    if any(i.name == 'test_eichprobe_vertrag_neue_zusicherung' for i in items):\n")
        code += ("        raise RuntimeError('Vertrags-Sammelfehler')\n" if art == 'sammlung' else
                 "        items[:] = [i for i in items if i.name != 'test_eichprobe_vertrag_neue_zusicherung']\n")
    elif art in ('skip', 'xfail'):
        code = ('import pytest\n'
                'def pytest_runtest_setup(item):\n'
                "    if item.name == 'test_eichprobe_vertrag_neue_zusicherung':\n"
                f"        pytest.{art}('Pflichtzeuge nicht ausgeführt')\n")
    else:
        hook = 'setup' if art == 'setup' else 'call'
        code = (f'def pytest_runtest_{hook}(item):\n'
                "    if item.name == 'test_eichprobe_vertrag_neue_zusicherung':\n"
                "        raise NameError('EINGABE fehlt im Vertragsfixture')\n")
    (vertragswerk / 'tests/conftest.py').write_text(code)
    rows = [vertragspruefung(g) for g in (False, True)]
    if art in ('skip', 'xfail'):
        # Echtes Docker-JUnit: kein gebautes XML und kein Host-runpy.
        junit = [ET.fromstring(m.group(1)) for k in rows[1]['kammer']
                 if (m := re.search(r'@@J@@(.*)@@E@@', k['stdout'], re.S))]
        zeugen = [tc for xml in junit for tc in xml.iter('testcase')
                  if tc.get('name') == VERTRAGSTEST.split('::')[1]]
        assert zeugen and all(tc.find('skipped') is not None for tc in zeugen)
        assert eichproben._vertrag_pruefbar(rows[1]['belege'], True) is False, \
            'Übersprungener benannter Vertragszeuge wird als ausgeführte Gegenkontrolle akzeptiert'
        for row in rows:
            zeuge = row['belege']['kandidat_tests'][VERTRAGSTEST]
            assert zeuge['ok'] is False and zeuge['bestaetigt'] is False
            assert zeuge['uebersprungen'] is True
            assert 'Pflichtzeuge nicht ausgeführt' in zeuge['meldung']
    for row in rows:
        # F7: Setup-/Skip-/Sammelabbruch macht auch die Messhülle ungültig.
        # Ein ausgeführter Call-Fehler bleibt Inhalt. Der entfernte benannte
        # Vertrag wird zusätzlich vom Zeugenprüfer erkannt, nicht erfunden.
        messung_gueltig = art in ('aufruf', 'fehlend')
        assert row['belege']['messung']['gueltig'] is messung_gueltig
        if not messung_gueltig:
            assert 'kernmass' not in row['belege']['messung']
        assert row['ausgefuehrt'] is True
        assert row['pruefbar'] is False, 'Defekter benannter Vertrag darf keine gültige Gegenprobe sein'
        assert row['bestanden'] is False
    batterie = _batterie_unit(rows[1])
    assert eichproben._vollstaendig(batterie['proben'], batterie['gegenproben']) is False
    with pytest.raises(ValueError, match='gegenproben'):
        vorspann._qualitaet(batterie)


def test_modulhelfer_und_konstanten_bleiben_im_eigenen_namensraum(vertragswerk, vertragspruefung):
    """Charakterisierung des vollständigen Modulkontexts samt echter Aegis-Wertung."""
    (vertragswerk / 'tests/test_abnehmer.py').write_text(
        'from __future__ import annotations\n'
        'from beispiel.abnehmer import bericht\n'
        'EINGABE = 2\n'
        'def eingabe():\n    return EINGABE\n'
        'def test_bericht():\n    assert bericht(eingabe()) == 3\n')
    alt = (vertragswerk / VERTRAG).read_text()
    (vertragswerk / VERTRAG).write_text(alt + '\nEINGABE = 99\n'
        'def test_eigener_namensraum():\n    assert EINGABE == 99\n')
    rows = [vertragspruefung(g) for g in (False, True)]
    for g, row in zip((False, True), rows):
        assert row['pruefbar'] is True
        assert row['bestanden'] is (not g)
        b = row['belege']
        assert eichproben._vertrag_pruefbar(b, g) is True
        assert b['kandidat_tests'][VERTRAGSTEST]['ok'] is g
        assert b['kandidat_tests'][VERTRAG + '::test_eigener_namensraum']['ok'] is True
        assert eichproben._bestanden('vertrag', b) is (not g)
        # Unit-Sensitivität an echten Belegen: jede fehlende Pflichtspalte sperrt.
        for gruppe, name in [('basis_tests', b['verbrauchertest']), ('kandidat_tests', VERTRAGSTEST),
                             ('kandidat_tests', b['verbrauchertest'])]:
            for feld in ('ok', 'bestaetigt', 'meldung'):
                falsch = deepcopy(b)
                falsch[gruppe][name].pop(feld)
                assert eichproben._vertrag_pruefbar(falsch, g) is False
                assert eichproben._bestanden('vertrag', falsch) is False
        for feld in ('vertragspfad', 'vertragstest', 'verbrauchertest', 'verbraucherdatei'):
            falsch = deepcopy(b)
            falsch.pop(feld)
            assert eichproben._vertrag_pruefbar(falsch, g) is False
        falsch = deepcopy(b)
        falsch['kandidat_tests'][VERTRAGSTEST] = dict(ok=False, bestaetigt=True,
            meldung='AssertionError: eichprobe_zusicherung fehlt', ort=VERTRAG)
        assert eichproben._vertrag_pruefbar(falsch, g) is False
        assert eichproben._bestanden('vertrag', falsch) is False

    batterie = _batterie_unit(rows[1])
    assert eichproben._vollstaendig(batterie['proben'], batterie['gegenproben']) is True
    assert vorspann._qualitaet(batterie) == dict(positive=4, negative=4, erwartet_je=4)


def test_syntaxfehler_im_verbrauchertest_wird_als_unbaubar_gemeldet(vertragswerk):
    (vertragswerk / 'tests/test_abnehmer.py').write_text('def test_bericht(:\n')
    # proben() fängt RuntimeError und liefert pruefbar=False; SyntaxError würde
    # dagegen die ganze Batterie verlassen, statt eine ungültige Zeile zu liefern.
    with pytest.raises(RuntimeError, match='Verbrauchertest.*Syntax'):
        eichproben._vertrag_vorbereiten(vertragswerk, 'beispiel', 'abnehmer', 'lieferant', VERTRAG, True)


@pytest.mark.skipif(not os.environ.get('BIOTOP_EICHWERK'), reason='Private Werk-/DB-Kopie nicht angegeben')
def test_benannter_vertrag_am_kopierten_pruefwerk(tmp_path):
    """Nur Vertragspaar am Bestand, keine vier-Paare- oder CLI-Abnahme."""
    quelle = Path(os.environ['BIOTOP_EICHWERK'])
    dbquelle = Path(os.environ['BIOTOP_EICHDB'])
    assert str(quelle.resolve()).startswith('/root/reparatur-01/')
    assert str(dbquelle.resolve()).startswith('/root/reparatur-01/')
    quellhash = hashlib.sha256(dbquelle.read_bytes()).hexdigest()
    werk = tmp_path / 'werk'
    kammer._kopie(quelle, werk)
    db = sqlite3.connect(tmp_path / 'bestand.db', isolation_level=None)
    db.row_factory = sqlite3.Row
    with sqlite3.connect(f'file:{dbquelle}?mode=ro', uri=True) as original:
        original.backup(db)
    try:
        werk_id = int(os.environ.get('BIOTOP_EICHWERK_ID', '22'))
        db.execute('UPDATE werke SET pfad=? WHERE id=?', (str(werk), werk_id))
        lauf_id = db.execute('SELECT COALESCE(MAX(id),0)+1 FROM laeufe').fetchone()[0]
        db.execute("INSERT INTO laeufe(id,werk_id,status,budget_eur,mass) VALUES(?,?,'angelegt',0,NULL)",
                   (lauf_id, werk_id))
        g = eichgegenstand.sichern(db, werk_id, lauf_id, werk)['gegenstand']
        assert g is not None
        bereiche = sorted(p.name for p in (werk / 'lagerhaus').iterdir()
                          if p.is_dir() and (p / '__init__.py').exists())
        ref = (Path(__file__).parents[1] / 'biotop/kern/referenzlast/lagerhaus.py').read_text()
        regeln = verfassung.lesen(db, werk_id)['regeln']
        basis = messgeraet.messen(werk, bereiche, 'lagerhaus', ref)
        assert basis['gueltig']
        vor_db = list(db.iterdump())
        vor_werk = {str(p.relative_to(werk)): p.read_bytes() for p in werk.rglob('*') if p.is_file()}
        rows = []
        with kammer.zaehlung() as zaehler:
            for gegenprobe in (False, True):
                e = eichproben._einzelprobe(db, lauf_id, werk_id, werk, 'lagerhaus', bereiche,
                    [('bericht', 'preise'), ('bericht', 'lager'), ('preise', 'formeln')],
                    basis, basis, ref, regeln.get('tausch', {}), 0, g, 'vertrag', gegenprobe)
                e['gegenstand'] = g
                _belegen('bestand-vertrag', e)
                rows.append(e)
        assert sum(e['kammerlaeufe'] for e in rows) == len(zaehler)
        for gegenprobe, e in zip((False, True), rows):
            assert e['ausgefuehrt'] is True and e['pruefbar'] is True
            assert e['bestanden'] is (not gegenprobe)
            b = e['belege']
            ziel = f"{Path(b['vertragspfad']).parent.as_posix()}/{b['vertragstest']}"
            assert b['kandidat_tests'][ziel]['ok'] is gegenprobe
            assert (b['vertragstest'] in b['urteil']['vertrag_verletzt']) is (not gegenprobe)
            if not gegenprobe:
                assert b['kandidat_tests'][ziel]['bestaetigt'] is True
                assert b['kandidat_tests'][ziel]['ort'] == b['verbraucherdatei']
                assert 'eichprobe_zusicherung' in b['kandidat_tests'][ziel]['meldung']
            assert e['modellaufrufe'] == 0 and e['kosten_eur'] == 0
        assert list(db.iterdump()) == vor_db
        assert {str(p.relative_to(werk)): p.read_bytes() for p in werk.rglob('*') if p.is_file()} == vor_werk
        assert hashlib.sha256(dbquelle.read_bytes()).hexdigest() == quellhash
    finally:
        db.close()
