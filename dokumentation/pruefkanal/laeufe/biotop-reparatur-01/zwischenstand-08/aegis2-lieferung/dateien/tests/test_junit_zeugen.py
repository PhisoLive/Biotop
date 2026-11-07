"""JUnit-Pflichtzeugen: echte Kammerdaten, kein Host-exec von Werkcode."""
import re
import xml.etree.ElementTree as ET

import pytest

from biotop.organe import aegis, kammer

TESTDATEI = 'tests/test_zeuge.py'
TESTNAME = TESTDATEI + '::test_ausgefuehrt'


@pytest.fixture
def zeugenwerk(tmp_path):
    werk = tmp_path / 'werk'
    (werk / 'tests').mkdir(parents=True)
    (werk / TESTDATEI).write_text('def test_ausgefuehrt():\n    assert 2 + 1 == 3\n')
    return werk


@pytest.mark.parametrize('ende', ['sauber', 'abbruch', 'zeitlimit', 'pytest_abbruch'])
def test_rest_junit_nur_aus_abgeschlossener_kammer_ist_erfolgszeuge(zeugenwerk, monkeypatch, ende):
    """Reales JUnit zuerst, danach echter Exitfehler bzw. echter Docker-Timeout.

    Nur der Test-Treiber erhält einen Nachspann; Ergebnis/rc/XML werden nicht gestellt.
    """
    original = kammer._ausfuehren

    def ausfuehren(werk, befehl, zeitlimit_s=None, dateien=None):
        dateien = dict(dateien)
        if ende == 'abbruch':
            dateien['_messgeraet/lauf.py'] = (
                'import atexit,os,sys;atexit.register(lambda:(sys.stdout.flush(),os._exit(7)));'
                + dateien['_messgeraet/lauf.py'])
        elif ende == 'zeitlimit':
            dateien['_messgeraet/lauf.py'] = (
                'import atexit,time,sys;atexit.register(lambda:(sys.stdout.flush(),time.sleep(30)));'
                + dateien['_messgeraet/lauf.py'])
            zeitlimit_s = 1
        elif ende == 'pytest_abbruch':
            dateien['tests/conftest.py'] = (
                'import os, pytest\n'
                '@pytest.hookimpl(trylast=True)\n'
                'def pytest_sessionfinish(session, exitstatus):\n'
                "    os.write(1, b'@@PYTEST_ABBRUCH_7@@')\n"
                '    os._exit(7)\n')
        return original(werk, befehl, zeitlimit_s, dateien)

    monkeypatch.setattr(kammer, '_ausfuehren', ausfuehren)
    with kammer.zaehlung() as aufrufe:
        zeugen = aegis.junit_lauf(zeugenwerk, 'beispiel', {}, [TESTDATEI])
    assert len(aufrufe) == 1
    lauf = aufrufe[0]
    xml = ET.fromstring(re.search(r'@@J@@(.*)@@E@@', lauf['stdout'], re.S).group(1))
    tc, = xml.iter('testcase')
    assert tc.get('name') == 'test_ausgefuehrt'
    assert all(tc.find(art) is None for art in ('skipped', 'failure', 'error'))
    assert lauf['zeitlimit'] is (ende == 'zeitlimit')
    if ende == 'pytest_abbruch':
        assert '@@PYTEST_ABBRUCH_7@@' in lauf['stdout']
    else:
        assert lauf['rc'] == {'sauber': 0, 'abbruch': 7, 'zeitlimit': 124}[ende]
    if ende == 'sauber':
        assert zeugen[TESTNAME]['ok'] is True
        assert aegis._namen(zeugen, TESTDATEI, ok=True) == {'test_ausgefuehrt'}
    else:
        assert zeugen and not any(x['ok'] for x in zeugen.values()), \
            'Abgebrochene Kammer wird durch grünes Rest-JUnit zum Erfolgszeugen'
        assert all(x['bestaetigt'] is False for x in zeugen.values())
        assert aegis._namen(zeugen, TESTDATEI, ok=True) == set()


@pytest.mark.parametrize('art', ['leer', 'testdatei_fehlt', 'junit_fehlt', 'keine_anforderung'])
def test_leeres_oder_fehlendes_junit_liefert_keinen_erfolgszeugen(zeugenwerk, monkeypatch, art):
    testdateien = [TESTDATEI]
    if art == 'leer':
        (zeugenwerk / TESTDATEI).write_text('# Absichtlich keine Testfunktion.\n')
    elif art == 'testdatei_fehlt':
        (zeugenwerk / TESTDATEI).unlink()
    elif art == 'keine_anforderung':
        testdateien = []
    else:
        original = kammer._ausfuehren

        def ohne_junit(werk, befehl, zeitlimit_s=None, dateien=None):
            # Echter Kammerprozess ohne pytest/JUnit, keine erfundene Antwort.
            return original(werk, ['python', '-c', 'pass'], zeitlimit_s, {})

        monkeypatch.setattr(kammer, '_ausfuehren', ohne_junit)
    with kammer.zaehlung() as aufrufe:
        zeugen = aegis.junit_lauf(zeugenwerk, 'beispiel', {}, testdateien)
    assert len(aufrufe) == (0 if art == 'keine_anforderung' else 1)
    assert aegis._namen(zeugen, TESTDATEI, ok=True) == set()
    assert not any(x['ok'] or x['bestaetigt'] for x in zeugen.values())
    if testdateien:
        assert zeugen, 'Angeforderte, aber fehlende Zeugen müssen einen Fehlerbeleg liefern'
