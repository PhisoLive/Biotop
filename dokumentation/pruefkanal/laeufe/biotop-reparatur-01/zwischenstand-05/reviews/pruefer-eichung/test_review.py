"""Independent UNIT review repros. No Docker, no paid calls, synthetic works only.

Gate tests substitute calibration/I/O at explicit boundaries. They exercise the
shipped guard, CLI, chain, mass binding and state transitions, NOT calibration.
The contract test executes only this file's small trusted fixture using pytest;
it does not claim a Docker/Kammer run or static/performance measurement.
"""
from contextlib import redirect_stdout, redirect_stderr
from copy import deepcopy
from io import StringIO
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

import pytest
from biotop import lauf as L, __main__ as CLI
from biotop.kern import datenbank, messgeraet as M, protokoll
from biotop.organe import (aegis, eichgegenstand, eichproben as E, eichung,
                           fundpruefung, generation0 as G0, kammer,
                           verfassung, vertraege, vorspann as V)

OUT = Path(__file__).resolve().parent


def measurement():
    return {'gueltig': True, 'kernmass': 6,
            'bereiche': {b: {'tests_bestanden': 3, 'tests_fehlgeschlagen': 0,
                             'sicherheit_punkte': 0, 'sicherheit_befunde': [],
                             'tote_funktionen': 0, 'laufzeit_ms': 100.,
                             'groesste_funktion': 10} for b in ['alpha', 'beta']},
            'werk': {'baut': True, 'zyklen': 0, 'bauzeit_ms': 100.,
                     'tests_fehlgeschlagen_liste': []}}


def emit(label, value):
    print(label + ' ' + json.dumps(value, ensure_ascii=False, sort_keys=True, default=str))


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    work = tmp_path / 'fixture'
    for name in ['alpha', 'beta']:
        path = work / 'paket' / name / '__init__.py'
        path.parent.mkdir(parents=True)
        path.write_text('def value():\n    return 1\n')
    (work / 'paket/__init__.py').write_text('')
    db = datenbank.verbinden(tmp_path / 'isolated.db')
    db.execute("INSERT INTO werke(id,name,pfad,bericht,status) VALUES(1,'review-unit',?,?,'aufgenommen')",
               (str(work), datenbank.j({'paket': 'paket'})))
    db.execute("INSERT INTO laeufe(id,werk_id,budget_eur,status) VALUES(1,1,0,'kartiert')")
    verfassung.einlegen(db, 1, 'alpha nutzt beta; Satz 2: Messgerät bleibt fest.',
                       {'uebungswerk': True, 'tragender_pfad': [['alpha', 'beta']]},
                       'Review-Unit', 'Review-Unit')
    vertraege.einlegen(db, 1, work, {('alpha', 'beta'): 'def test_vertrag():\n    assert True\n'}, 'Review-Unit')
    db.execute("INSERT INTO landkarte(werk_id,stufe,schluessel,inhalt) VALUES(1,1,'review','{}')")
    # Explicit UNIT boundary values, not measured or paid outputs.
    monkeypatch.setattr(V, '_infrastruktur', lambda: {'image': 'UNIT-NOT-DOCKER', 'image_id': 'sha256:' + 'f'*64})
    monkeypatch.setattr(L, '_referenzlast', lambda *args: '# UNIT load, not executed')
    monkeypatch.setattr(M, 'messen', lambda *args, **kwargs: measurement())
    noise = {'gesperrt': [], 'toleranz': {'alpha': 1.15, 'beta': 1.15}, 'lauf_startet': True,
             'bereiche': {b: {'gesperrt': False, 'toleranz': 1.15, 'werte': [100.]*5,
                              'nachmessen': False, 'meldung': None} for b in ['alpha', 'beta']}}
    monkeypatch.setattr(eichung, 'rauschmessung', lambda *args: deepcopy(noise))
    monkeypatch.setattr(fundpruefung, 'bewerten', lambda *args: {
        'kammerlaeufe': 0, 'geprueft': 0, 'ergebnisse': [], 'bezugsgroesse': 'UNIT no funds'})
    def unit_probes(*args, **kwargs):
        # Deliberately synthetic proof object at the calibration boundary.
        return {'bestanden': True, 'gegenstand': eichgegenstand.lesen(db, 1),
                **{group: {name: {'ausgefuehrt': True, 'pruefbar': True, 'bestanden': verdict,
                                   'kammerlaeufe': 0, 'modellaufrufe': 0, 'kosten_eur': 0., 'dauer_s': 0.}
                           for name in E.PROBEN}
                   for group, verdict in [('proben', True), ('gegenproben', False)]}}
    monkeypatch.setattr(E, 'proben', unit_probes)
    monkeypatch.setattr(G0, 'erzeugen', lambda *args: [
        {'datei': 'paket/alpha/__init__.py', 'zeile': 2, 'art': 'unit',
         'beschreibung': 'UNIT mutant', 'code': 'def value():\n    return 2\n'}])
    monkeypatch.setattr(G0, 'aequivalenz_pruefen', lambda *args: None)
    monkeypatch.setattr(G0, 'messen', lambda *args: {'nicht_aequivalent': 1, 'gefangen': 1, 'blind': []})
    monkeypatch.setattr(L.lazarus, 'schnappschuss', lambda *args: {'tag': 'UNIT', 'pruefsumme': '0'*64})
    monkeypatch.setattr(CLI, 'verbinden', lambda: db)
    yield db, work, noise
    db.close()


def test_valid_route_reaches_generation_and_rejects_missing_order(isolated, monkeypatch):
    db, work, noise = isolated
    with pytest.raises(L.LaufFehler, match='Vorspann'):
        L.generation0(db, 1, None, .8)
    r = V.ausfuehren(db, 1)
    with pytest.raises(L.LaufFehler, match='Generation 0'):
        L.mass_einfrieren(db, 1, 'Review-Unit')
    g0 = L.generation0(db, 1, None, .8)
    m = L.mass_einfrieren(db, 1, 'Review-Unit')
    entered = []
    monkeypatch.setattr(L, '_generation_koerper', lambda *args: entered.append(args[12]) or {'unit_entered': True})
    generation = L.generation(db, 1)
    assert generation['unit_entered'] is True and len(entered) == 1
    assert entered[0]['_rauschtoleranz'] == noise['toleranz']
    assert protokoll.pruefen(db)[0] is True
    emit('VALID_ROUTE_UNIT', {'gen0_erreicht': g0['erreicht'], 'generation': generation,
                             'toleranz_consumer': entered[0]['_rauschtoleranz'],
                             'mass_bound': m['mass']['vorspann_sha256'] == r['nachweis_sha256']})


def test_failed_gen0_must_block_mass_and_cli(isolated, monkeypatch):
    db, work, noise = isolated
    V.ausfuehren(db, 1)
    mutant = G0.erzeugen(work, 'paket', ['alpha', 'beta'])[0]
    # Real generation0 control flow, failed result supplied at measurement boundary.
    monkeypatch.setattr(G0, 'erzeugen', lambda *args: [mutant])
    monkeypatch.setattr(G0, 'messen', lambda *args: {'nicht_aequivalent': 1, 'gefangen': 0, 'blind': [mutant]})
    monkeypatch.setattr(G0, 'tests_evolutionieren', lambda *args: {'neue_tests': {}})
    stdout, stderr = StringIO(), StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        gen0_rc = CLI.main(['gen0', '1'])
        mass_rc = CLI.main(['mass', '1', '--bestaetigt-von', 'Review-Unit'])
    row = db.execute("SELECT inhalt FROM protokoll WHERE art='generation0.ergebnis'").fetchone()
    result = datenbank.lj(row[0])
    emit('FAILED_GEN0_BYPASS', {'gen0': result, 'gen0_rc': gen0_rc, 'mass_rc': mass_rc,
                              'status': L._lauf(db, 1)['status'],
                              'mass_bound': bool(db.execute('SELECT mass_sha256 FROM vorspann_nachweise').fetchone()[0]),
                              'stdout': stdout.getvalue(), 'stderr': stderr.getvalue()})
    assert result['erreicht'] is False
    assert mass_rc != 0, 'Failed generation0 result was accepted as completed prerequisite'


def test_sealed_contract_replacement_after_vorspann_must_invalidate(isolated):
    db, work, noise = isolated
    proof = V.ausfuehren(db, 1)
    sealed = proof['gegenstand']['gegenstand']
    # Use the shipped public insertion API, not an UPDATE of proof or hash chain.
    vertraege.einlegen(db, 1, work, {('alpha', 'beta'): 'def test_vertrag():\n    assert 2 == 2\n'}, 'replacement after calibration')
    before = sealed['vertrag_pruefsumme']
    after = hashlib.sha256((work / sealed['vertrag_pfad']).read_bytes()).hexdigest()
    assert before != after
    error = None
    try:
        V.verlangen(db, 1, 'gen0')
        L.generation0(db, 1, None, .8)
        L.mass_einfrieren(db, 1, 'Review-Unit')
        V.verlangen(db, 1, 'generation')
    except V.VorspannFehler as e:
        error = str(e)
    emit('CONTRACT_REPLACEMENT_BYPASS', {'seal': before, 'actual': after,
                                       'hash_chain_valid': protokoll.pruefen(db)[0], 'error': error,
                                       'proof_status': db.execute('SELECT status FROM vorspann_nachweise').fetchone()[0],
                                       'run_status': L._lauf(db, 1)['status']})
    assert error is not None, 'Changed calibration contract remains certified through gen0, mass and generation gate'


def test_blocked_area_must_include_actual_diff_targets(isolated, monkeypatch):
    db, work, noise = isolated
    noise['gesperrt'] = ['beta']
    noise['toleranz'].pop('beta')
    noise['bereiche']['beta'].update(gesperrt=True, toleranz=1.7, meldung='UNIT noisy beta')
    V.ausfuehren(db, 1)
    L.generation0(db, 1, None, .8)
    baseline = measurement()
    baseline['bereiche']['alpha']['tote_funktionen'] = 1
    monkeypatch.setattr(M, 'messen', lambda *args, **kwargs: deepcopy(baseline))
    L.mass_einfrieren(db, 1, 'Review-Unit')
    candidate = deepcopy(baseline)
    candidate['bereiche']['alpha']['tote_funktionen'] = 0
    candidate['bereiche']['beta']['laufzeit_ms'] = 10000.
    calls = []
    def measured(*args, **kwargs):
        calls.append(sorted((kwargs.get('dateien') or {}).keys()))
        return deepcopy(candidate if len(calls) % 2 == 0 else baseline)
    monkeypatch.setattr(M, 'messen', measured)
    monkeypatch.setattr(aegis, '_angriff', lambda *args, **kwargs: (None, 'UNIT-NO-MODEL', None))
    monkeypatch.setattr(L.entropie, 'messen', lambda *args: {})
    monkeypatch.setattr(L.entropie, 'pruefen_und_beenden', lambda *args: None)
    diff = ''.join(E._diff(f'paket/{name}/__init__.py', (work / f'paket/{name}/__init__.py').read_text(),
                           'def value():\n    return 2\n') for name in ['alpha', 'beta'])
    result = L.generation(db, 1, einschleusen=[{'bereich': 'alpha', 'diff': diff}])
    k = db.execute('SELECT status,wirkungskreis,masse FROM kandidaten').fetchone()
    old_gate = M.urteil_f2(baseline, candidate, baseline, ['alpha', 'beta'], ['alpha'], {})
    emit('BLOCKED_DIFF_BYPASS', {'generation_status': result['status'], 'reason': result['grund'],
                               'declared_area': 'alpha', 'blocked_areas': ['beta'],
                               'wirkungskreis': datenbank.lj(k['wirkungskreis']),
                               'actual_diff_files': sorted(datenbank.lj(k['masse'])['_dateien']),
                               'beta_file_after': (work / 'paket/beta/__init__.py').read_text(),
                               'beta_time_fixture': [100., 10000.], 'measure_calls': calls,
                               'without_new_skip': old_gate})
    assert old_gate['ok'] is False and any('beta.laufzeit_ms' in s for s in old_gate['grenzen_gerissen'])
    assert result['status'] == 'abgelehnt', 'Declared alpha bypassed beta lock; generation wrote beta'


@pytest.fixture
def trusted_contract_fixture(tmp_path):
    work = tmp_path / 'trusted-work'
    files = {
        'beispiel/__init__.py': '',
        'beispiel/abnehmer/__init__.py': 'from .quelle import bericht\n',
        'beispiel/abnehmer/quelle.py': 'def bericht(zahl: float):\n    ergebnis = zahl + 1\n    return ergebnis\n',
        'beispiel/lieferant/__init__.py': 'from .quelle import wert\n',
        'beispiel/lieferant/quelle.py': 'def wert(zahl: float):\n    ergebnis = zahl * 2\n    return ergebnis\n',
        'tests/test_abnehmer.py': 'from beispiel.abnehmer import bericht\nEINGABE = 2\ndef test_bericht():\n    assert bericht(EINGABE) == 3\n',
        'tests/test_lieferant.py': 'from beispiel.lieferant import wert\ndef test_wert():\n    assert wert(2) == 4\n',
        'tests/vertraege/test_vertrag_abnehmer_lieferant.py': 'from beispiel.lieferant import wert\ndef test_alt():\n    assert wert(2) == 4\n',
    }
    for rel, text in files.items():
        f = work / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text)
    return work


@pytest.fixture
def local_junit_adapter(monkeypatch):
    raw_runs = []
    def run_local(werk, befehl, zeitlimit_s=None, dateien=None):
        # Trusted tiny review fixture ONLY. No arbitrary works or measurement script.
        assert 'trusted-work' in str(werk) or 'contract-fixture-private' in str(werk)
        assert befehl[1] == '_messgeraet/lauf.py', befehl
        with tempfile.TemporaryDirectory(prefix='local-pytest-', dir=OUT / 'tmp') as d:
            dest = Path(d) / 'fixture'
            shutil.copytree(werk, dest)
            for rel, text in dateien.items():
                target = dest / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                if rel == '_messgeraet/lauf.py':
                    text = text.replace('/tmp/j.xml', str(Path(d) / 'j.xml'))
                target.write_text(text)
            env = dict(os.environ, PYTHONPATH=os.pathsep.join([str(dest), str(OUT / 'guard')]))
            command = [sys.executable, *befehl[1:]]
            p = subprocess.run(command, cwd=dest, env=env, capture_output=True, text=True, timeout=30)
            raw = {'evidence': 'local trusted pytest, NOT Docker', 'cmd': command,
                   'cwd': str(dest), 'rc': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}
            raw_runs.append(raw)
            return kammer.Ergebnis(p.returncode, p.stdout, p.stderr, 0., False, 'UNIT-LOCAL-NOT-DOCKER')
    monkeypatch.setattr(kammer, '_ausfuehren', run_local)
    yield raw_runs
    (OUT / 'contract-local-pytest-raw.json').write_text(json.dumps(raw_runs, ensure_ascii=False, indent=2))


def test_contract_countercase_is_not_allowed_to_fail_inside_cloned_test(trusted_contract_fixture, local_junit_adapter):
    work = trusted_contract_fixture
    contract = 'tests/vertraege/test_vertrag_abnehmer_lieferant.py'
    rows = []
    for counter in [False, True]:
        diff, description, witnesses, attack = E._vertrag_vorbereiten(work, 'beispiel', 'abnehmer', 'lieferant', contract, counter)
        files = aegis.kandidat_dateien(work, diff)
        contract_result = aegis.junit_lauf(work, 'beispiel', files, [contract])
        name = contract + '::test_eichprobe_vertrag_neue_zusicherung'
        # Original predicate receives real executed consumer witnesses. Only the
        # measure envelope/verdict is a declared UNIT input to isolate validation.
        mass = {'ok': False, 'zuwachs': -1}
        reason = 'Vertrag verletzt (Schritt 2): ' + witnesses['vertragstest']
        belege = dict(witnesses, urteil={'mass': mass, 'status': 'abgelehnt', 'grund': reason,
                                       'vertrag_verletzt': [witnesses['vertragstest']]},
                      messung={'gueltig': True, '_basis_paar': {'gueltig': True}})
        rows.append({'gegenprobe': counter, 'predicate': E._bestanden('vertrag', belege),
                     'consumer': witnesses['kandidat_tests'], 'contract': contract_result,
                     'generated_contract': files[contract]})
    emit('CONTRACT_COUNTERCASE_FALSE_GREEN', rows)
    assert rows[0]['predicate'] is True and rows[1]['predicate'] is False
    neg = rows[1]['contract'][name]
    assert neg['ok'] is True, 'Countercase still fails named contract: cloned function lost EINGABE global'


def test_private_db_and_work_changes_do_not_escape(isolated):
    db, work, noise = isolated
    before_db = list(db.iterdump())
    before_files = {p.relative_to(work).as_posix(): p.read_bytes() for p in work.rglob('*') if p.is_file()}
    with E._privat(db, work) as (private_db, private_work):
        assert private_work != work
        assert private_db.execute('SELECT pfad FROM werke WHERE id=1').fetchone()[0] == str(private_work)
        private_db.execute("UPDATE werke SET name='private-only' WHERE id=1")
        (private_work / 'paket/alpha/__init__.py').write_text('private-only')
    assert list(db.iterdump()) == before_db
    assert {p.relative_to(work).as_posix(): p.read_bytes() for p in work.rglob('*') if p.is_file()} == before_files
    emit('PRIVATE_ISOLATION_UNIT', {'db_unchanged': True, 'work_unchanged': True})


@pytest.mark.parametrize('name', E.PROBEN)
def test_nonexecution_is_not_a_countercase(name):
    positive = {n: {'ausgefuehrt': True, 'pruefbar': True, 'bestanden': True} for n in E.PROBEN}
    negative = {n: {'ausgefuehrt': True, 'pruefbar': True, 'bestanden': False} for n in E.PROBEN}
    negative[name]['ausgefuehrt'] = False
    assert E._vollstaendig(positive, negative) is False
    negative[name]['ausgefuehrt'] = True
    negative[name]['pruefbar'] = False
    assert E._vollstaendig(positive, negative) is False
    assert E._bestanden(name, {'urteil': {'mass': None}, 'messung': {}}) is False


def test_proof_quality_needs_mechanism_not_boolean_envelope():
    payload = {'bestanden': True,
               **{group: {name: {'ausgefuehrt': True, 'pruefbar': True, 'bestanden': result}
                          for name in E.PROBEN}
                  for group, result in [('proben', True), ('gegenproben', False)]}}
    # Characterization, suggestion: flags alone are currently trusted here.
    result = V._qualitaet(payload)
    emit('QUALITY_FLAGS_ONLY_UNIT', {'input': payload, 'accepted': result})
    assert result == {'positive': 4, 'negative': 4, 'erwartet_je': 4}
