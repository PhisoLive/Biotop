"""Gegenproben des Zwischenbericht-Wächters. Die Wurzel ist ein Argument, der Prüfkanal eine Attrappe unter tmp_path.

Die Tests prüfen, dass der Wächter unter der Schwelle schweigt, ab der Schwelle genau einmal auslöst, bei 140 ein
zweites Mal auslöst und die Verdichtungsfortsetzung nicht als neuen Turn liest. Ein neuer Turn beginnt neu zu zählen,
Kindsitzungen zählen nicht, ein vorhandener Ordner wird nie überschrieben, Geheimnisse werden geschwärzt.
"""
import contextlib
import importlib.util
import io
import json
import sqlite3
import time
from pathlib import Path

import pytest

import os  # noqa: E402
SKRIPT = Path(os.environ.get('WAECHTER_SKRIPT', '/root/.hermes/scripts/zwischenbericht_waechter.py'))  # Gegenproben: Kopie mit Ausschalter
_spec = importlib.util.spec_from_file_location('zwischenbericht_waechter', SKRIPT)
W = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(W)


def _nachricht(con, sid, rolle, text='', werkzeug=False):
    con.execute("INSERT INTO messages(session_id, role, content, tool_calls, timestamp) VALUES (?,?,?,?,?)",
                (sid, rolle, text, '[{"id": "a"}]' if werkzeug else None, time.time()))


def _runden(con, sid, k):
    for _ in range(k):
        _nachricht(con, sid, 'assistant', 'arbeite weiter', werkzeug=True)
        _nachricht(con, sid, 'tool', 'ok')
    con.commit()


@pytest.fixture
def u(tmp_path):
    home = tmp_path / 'hermes'
    (home / 'zwischenbericht').mkdir(parents=True)
    (home / 'config.yaml').write_text('model:\n  default: x\nagent:\n  max_turns: 150\n  service_tier: ""\nterminal:\n  max_turns: 7\n')
    arbeit = tmp_path / 'arbeit'
    (arbeit / 'gesperrt').mkdir(parents=True)
    (arbeit / 'a.txt').write_text('a')
    (arbeit / 'gesperrt' / 'geheim.txt').write_text('nicht listen')
    ueb = tmp_path / 'UEBERGABE.md'
    ueb.write_text('# Übergabe\nStand X; Schlüssel sk-or-v1-' + 'b' * 40 + '\n')
    (home / 'zwischenbericht' / 'auftrag.json').write_text(json.dumps(
        {'auftrag': 'probe-auftrag', 'uebergabe': [str(ueb)], 'repos': [], 'arbeitsordner': [str(arbeit)],
         'ausschluss': [str(arbeit / 'gesperrt')]}))
    db = tmp_path / 'state.db'
    con = sqlite3.connect(db)
    con.executescript("CREATE TABLE sessions (id TEXT PRIMARY KEY, source TEXT, ended_at REAL, last_activity_at REAL);"
                      "CREATE TABLE messages (id INTEGER PRIMARY KEY AUTOINCREMENT, session_id TEXT, role TEXT, content TEXT,"
                      " tool_calls TEXT, timestamp REAL);")
    con.execute("INSERT INTO sessions VALUES ('haupt', 'telegram', NULL, ?)", (time.time(),))
    con.execute("INSERT INTO sessions VALUES ('kind', 'subagent', NULL, ?)", (time.time(),))
    con.commit()
    wurzel = tmp_path / 'akte'
    wurzel.mkdir()
    return {'home': home, 'db': db, 'con': con, 'wurzel': wurzel, 'arbeit': arbeit}


def _lauf(u, *extra, rc_erwartet=0):
    puffer = io.StringIO()
    with contextlib.redirect_stdout(puffer):
        rc = W.main(['--state-db', str(u['db']), '--hermes-home', str(u['home']), '--pruefkanal-wurzel', str(u['wurzel']),
                     '--url-basis', 'https://beispiel.invalid/_akte/k', '--ohne-https', '--kein-besitzer', *extra])
    assert rc == rc_erwartet, (rc, puffer.getvalue())
    return puffer.getvalue()


def _ordner(u):
    d = u['wurzel'] / 'laeufe' / 'probe-auftrag'
    return sorted(p for p in d.glob('zwischenbericht-*')) if d.exists() else []


def test_grenze_aus_dem_agent_block_und_schwellen():
    import tempfile
    with tempfile.TemporaryDirectory() as t:
        (Path(t) / 'config.yaml').write_text('terminal:\n  max_turns: 7\nagent:\n  max_turns: 150\n')
        assert W.grenze(Path(t)) == 150
        (Path(t) / 'config.yaml').write_text('agent:\n  service_tier: x\n')
        assert W.grenze(Path(t)) == 500
    assert W.schwellen(150) == [110, 140]


def test_unter_der_schwelle_still_ab_110_genau_einmal_bei_140_erneut(u):
    con = u['con']
    _nachricht(con, 'haupt', 'user', 'Auftrag: mach etwas Ordentliches')
    con.commit()
    time.sleep(0.01)
    (u['arbeit'] / 'b.txt').write_text('nach Turnbeginn geschrieben')
    (u['arbeit'] / 'gesperrt' / 'geheim2.txt').write_text('nach Turnbeginn, aber ausgeschlossen')
    _runden(con, 'haupt', 60)
    _nachricht(con, 'haupt', 'user', '[Your active task list was preserved across context compression]\n- [ ] x')
    _runden(con, 'haupt', 49)
    assert _lauf(u) == '' and _ordner(u) == []
    herz = json.loads((u['home'] / 'zwischenbericht' / 'herzschlag.json').read_text())
    assert [s['runden'] for s in herz['sitzungen'] if s['sitzung'] == 'haupt'] == [109]   # Fortsetzung zählt weiter
    _runden(con, 'haupt', 1)
    aus = _lauf(u)
    assert 'Zwischenbericht ausgelöst' in aus and 'Runde 110 von 150 (Schwelle 110)' in aus, aus
    ordner = _ordner(u)
    assert len(ordner) == 1 and ordner[0].name.endswith('-r110')
    namen = {p.name for p in ordner[0].iterdir()}
    assert {'ZWISCHENBERICHT.md', 'DATEIEN.txt', 'MANIFEST.sha256', 'PRUEFSUMME-ORDNER.txt', 'UEBERGABE-1-UEBERGABE.md'} <= namen
    text = (ordner[0] / 'ZWISCHENBERICHT.md').read_text()
    assert 'Auftrag: mach etwas Ordentliches' in text and '110 von 150' in text
    assert 'b.txt' in text and 'a.txt' not in text                                     # nur Dateien seit Turnbeginn
    assert 'geheim' not in text                                                        # Ausschluss greift
    assert 'sk-or-v1-' not in (ordner[0] / 'UEBERGABE-1-UEBERGABE.md').read_text()     # geschwärzt
    zeilen = (ordner[0] / 'DATEIEN.txt').read_text().splitlines()
    assert any(z.startswith('https://beispiel.invalid/_akte/k/laeufe/probe-auftrag/zwischenbericht-') and 'ZWISCHENBERICHT.md' in z for z in zeilen)
    assert _lauf(u) == '' and len(_ordner(u)) == 1                                     # nicht doppelt
    _runden(con, 'haupt', 30)
    assert 'Runde 140 von 150 (Schwelle 140)' in _lauf(u) and len(_ordner(u)) == 2


def test_neuer_turn_zaehlt_neu_und_kindsitzungen_zaehlen_nicht(u):
    con = u['con']
    _nachricht(con, 'haupt', 'user', 'alter Auftrag')
    _runden(con, 'haupt', 130)
    _nachricht(con, 'haupt', 'user', 'neuer Auftrag')
    _runden(con, 'haupt', 5)
    _nachricht(con, 'kind', 'user', 'Unterauftrag')
    _runden(con, 'kind', 130)
    assert _lauf(u) == '' and _ordner(u) == []
    herz = json.loads((u['home'] / 'zwischenbericht' / 'herzschlag.json').read_text())
    # geändert (Kontext-Auslöser): der Herzschlag führt je Sitzung zusätzlich 'kontext' und 'verdichtung_gescheitert'
    assert [{k: s[k] for k in ('sitzung', 'runden')} for s in herz['sitzungen']] == [{'sitzung': 'haupt', 'runden': 5}]


def test_sofort_loest_unabhaengig_von_der_schwelle_aus(u):
    _nachricht(u['con'], 'haupt', 'user', 'Auftrag')
    _runden(u['con'], 'haupt', 3)
    assert 'Runde 3 von 150 (Schwelle sofort)' in _lauf(u, '--sofort') and len(_ordner(u)) == 1


def test_vorhandener_ordner_wird_nie_ueberschrieben(u):
    _nachricht(u['con'], 'haupt', 'user', 'Auftrag')
    _runden(u['con'], 'haupt', 110)
    jetzt = time.time() + 5          # geändert (Kontext-Auslöser): --jetzt filtert jetzt auch Nachrichten
    vorhanden = u['wurzel'] / W.ordnername('probe-auftrag', jetzt, 110)
    vorhanden.mkdir(parents=True)
    (vorhanden / 'ZWISCHENBERICHT.md').write_text('alt')
    aus = _lauf(u, '--jetzt', str(jetzt), rc_erwartet=1)                             # Fehler wird gemeldet, nicht verschluckt
    assert 'gescheitert' in aus and 'FileExistsError' in aus, aus
    assert (vorhanden / 'ZWISCHENBERICHT.md').read_text() == 'alt'
    zustand = json.loads((u['home'] / 'zwischenbericht' / 'ausgeloest.json').read_text())
    assert zustand == {}                                                               # nicht als erledigt vermerkt


def test_geheimnisse_werden_geschwaerzt():
    assert 'sk-or-v1-' not in W.schwaerzen('x sk-or-v1-' + 'a' * 40 + ' y')
    assert 'hunter2' not in W.schwaerzen('password: hunter2')
    assert W.schwaerzen('Kernmaß −11 → 0') == 'Kernmaß −11 → 0'


# ================================================================ Zweiter Auslöser: Kontextfüllung und Verdichtung
from datetime import datetime  # noqa: E402


def _ts(t=None):
    t = time.time() if t is None else t
    return datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S') + f',{int(t * 1000) % 1000:03d}'


def _log(u, zeilen):
    (u['home'] / 'logs').mkdir(exist_ok=True)
    with open(u['home'] / 'logs' / 'agent.log', 'a') as f:
        for z in zeilen:
            f.write(z + '\n')


def _api(u, sid, tokens, t=None, modell='claude-opus-5-5', anbieter='anthropic'):
    _log(u, [f"{_ts(t)} INFO [{sid}] agent.conversation_loop: API call #7: model={modell} provider={anbieter} "
             f"in={tokens} out=10 total={tokens + 10} latency=1.0s"])


def _telemetrie(u, sid, gescheitert, t=None, meldung='Error code: 401 - OAuth access token has been revoked.'):
    zeilen = [f"{_ts(t)} WARNING agent.context_compressor: Failed to generate context summary: {meldung}"] if gescheitert else []
    daten = ('"commit_status":"aborted","failure_class":"summary_generation_aborted"' if gescheitert
             else '"commit_status":"committed"')
    zeilen.append(f'{_ts(t)} INFO agent.conversation_compression: context compression attempt telemetry: '
                  f'{{{daten},"event":"compression_attempt","session_id":"{sid}"}}')
    _log(u, zeilen)


@pytest.fixture
def uk(u):
    (u['home'] / 'models_dev_cache.json').write_text(json.dumps(
        {'anthropic': {'models': {'claude-opus-5-5': {'limit': {'context': 1000000}}}}}))
    _nachricht(u['con'], 'haupt', 'user', 'Auftrag mit großem Kontext')
    _runden(u['con'], 'haupt', 5)
    time.sleep(0.01)
    return u


def _herz(u):
    return {s['sitzung']: s for s in json.loads((u['home'] / 'zwischenbericht' / 'herzschlag.json').read_text())['sitzungen']}


def test_kontext_unter_80_still_ab_80_genau_einmal(uk):
    _api(uk, 'haupt', 799_999)
    _api(uk, 'haupt', 950_000, t=time.time() + 3600)           # nach `jetzt`: zählt nicht
    assert _lauf(uk) == '' and _ordner(uk) == []
    k = _herz(uk)['haupt']['kontext']
    assert (k['tokens'], k['grenze'], k['anteil']) == (799_999, 1_000_000, 0.8)   # Anzeige gerundet, Entscheidung nicht
    _api(uk, 'haupt', 800_000)
    aus = _lauf(uk, '--jetzt', str(time.time()))
    assert 'Kontextfüllung 80.0 % (800000 von 1000000 Token' in aus, aus
    ordner = _ordner(uk)
    assert len(ordner) == 1 and ordner[0].name.endswith('-r5-kontext80'), ordner
    assert 'Kontextfüllung 80.0 %' in (ordner[0] / 'ZWISCHENBERICHT.md').read_text()
    _api(uk, 'haupt', 900_000)
    assert _lauf(uk, '--jetzt', str(time.time())) == '' and len(_ordner(uk)) == 1     # je Turn genau einmal
    _nachricht(uk['con'], 'haupt', 'user', 'neuer Auftrag')
    uk['con'].commit()
    time.sleep(0.01)
    _api(uk, 'haupt', 910_000)
    assert 'Kontextfüllung 91.0 %' in _lauf(uk, '--jetzt', str(time.time())) and len(_ordner(uk)) == 2   # neuer Turn


def test_kontext_gegenprobe_fremde_sitzung_und_unbekannte_grenze(uk):
    _api(uk, 'haupt', 990_000, modell='unbekannt-9', anbieter='nirgendwo')
    _api(uk, 'andere', 950_000)                                 # letzte API-Zeile im Log, aber andere Sitzung
    assert _lauf(uk) == '' and _ordner(uk) == []
    k = _herz(uk)['haupt']['kontext']
    assert k['tokens'] == 990_000 and k['grenze'] is None and k['grenze_quelle'] == 'unbekannt', k


def test_erste_gescheiterte_verdichtung_genau_einmal(uk):
    _api(uk, 'haupt', 300_000)
    _telemetrie(uk, 'haupt', True, t=time.time() - 3600)        # vor Turnbeginn: zählt nicht
    _telemetrie(uk, 'haupt', False)                             # gelungene Verdichtung: kein Anlass
    _telemetrie(uk, 'andere', True, meldung='fremder Fehler')   # andere Sitzung: kein Anlass für 'haupt'
    assert _lauf(uk) == '' and _ordner(uk) == []
    assert _herz(uk)['haupt']['verdichtung_gescheitert'] is None
    time.sleep(0.01)
    _telemetrie(uk, 'haupt', True)
    aus = _lauf(uk, '--jetzt', str(time.time()))
    assert 'Verdichtung gescheitert' in aus and 'OAuth access token has been revoked' in aus and 'fremder' not in aus, aus
    ordner = _ordner(uk)
    assert len(ordner) == 1 and ordner[0].name.endswith('-r5-verdichtung'), ordner
    assert 'summary_generation_aborted' in (ordner[0] / 'ZWISCHENBERICHT.md').read_text()
    _telemetrie(uk, 'haupt', True, meldung='zweiter Fehler')
    assert _lauf(uk, '--jetzt', str(time.time())) == '' and len(_ordner(uk)) == 1     # nur die erste


def test_runden_verdichtung_und_kontext_zusammen_ein_ordner(uk):
    _runden(uk['con'], 'haupt', 105)
    _api(uk, 'haupt', 850_000)
    _telemetrie(uk, 'haupt', True)
    aus = _lauf(uk, '--jetzt', str(time.time()))
    assert 'Runde 110 von 150 (Schwelle 110)' in aus and 'Kontextfüllung 85.0 %' in aus and 'Verdichtung gescheitert' in aus
    assert [p.name.split('-r', 1)[1] for p in _ordner(uk)] == ['110-kontext80-verdichtung']


def test_nachspiel_sitzung_die_erst_nach_jetzt_endete_zaehlt(uk):
    """--jetzt: eine damals offene, inzwischen beendete Sitzung wird nachgespielt; eine vorher beendete nicht."""
    _telemetrie(uk, 'haupt', True)
    damals = time.time() + 1
    uk['con'].execute("UPDATE sessions SET ended_at=? WHERE id='haupt'", (damals + 60,))
    uk['con'].commit()
    assert 'Verdichtung gescheitert' in _lauf(uk, '--jetzt', str(damals))
    uk['con'].execute("UPDATE sessions SET ended_at=? WHERE id='haupt'", (damals - 0.5,))
    uk['con'].commit()
    (uk['home'] / 'zwischenbericht' / 'ausgeloest.json').unlink()
    assert _lauf(uk, '--jetzt', str(damals)) == ''                     # Gegenprobe: vorher beendet


def test_sperrkonflikt_ist_kein_scheitern(uk):
    """failure_class lock_contended: eine andere Verdichtung hält die Sperre — sie läuft, sie scheitert nicht."""
    _log(uk, [f'{_ts()} INFO agent.conversation_compression: context compression attempt telemetry: '
              '{"commit_status":"aborted","failure_class":"lock_contended","event":"compression_attempt","session_id":"haupt"}'])
    assert _lauf(uk) == '' and _ordner(uk) == []
    assert _herz(uk)['haupt']['verdichtung_gescheitert'] is None
