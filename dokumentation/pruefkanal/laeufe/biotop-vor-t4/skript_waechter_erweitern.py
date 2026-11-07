"""Wächter um zwei Auslöser erweitern: Kontextfüllung ≥ 80 % und erste gescheiterte Verdichtung (je Sitzung und Turn
genau einmal). Ersetzt nur benannte Anker, jeder muss genau einmal vorkommen; Sicherung der alten Fassung vorher.
Zusätzlich: --jetzt wirkt auch auf Nachrichten und Logzeilen (echtes Nachspiel eines früheren Zeitpunkts)."""
import shutil
import time
from pathlib import Path

S = Path('/root/.hermes/scripts/zwischenbericht_waechter.py')
T = Path('/root/.hermes/zwischenbericht/test_waechter.py')
stempel = time.strftime('%Y%m%d-%H%M%S')
for p in (S, T):
    shutil.copy2(p, p.with_name(p.name + f'.vor-kontext-{stempel}'))
s = S.read_text()


def ersetze(alt, neu):
    global s
    assert s.count(alt) == 1, (s.count(alt), alt[:80])
    s = s.replace(alt, neu)


ersetze('''Was ausgelöst wird. Ein NEUER Ordner''', '''Zweiter Auslöser (Philipp, 23.09.2026, nach dem Tod einer Sitzung am Kontext statt am Rundenlimit): Kontextfüllung
≥ 80 % und die erste gescheiterte Verdichtung, je Sitzung und Turn genau einmal. Kontextfüllung = Eingabetoken der
letzten Modellanfrage der Sitzung (agent.log, Zeile „API call #n: model=… provider=… in=…“) geteilt durch das
Kontextfenster des Modells (models.dev-Zwischenspeicher, sonst context_length_cache.yaml, sonst die zuletzt vom
Verdichter gemeldete Grenze; unbekannt → kein Auslöser, im Herzschlag sichtbar). Entschieden wird am ungerundeten
Anteil. Gescheiterte Verdichtung = Telemetriezeile des Verdichters dieser Sitzung mit failure_class bzw.
commit_status „aborted“, oder „Context compression failed“, oder die in state.db vermerkte Verdichtungssperre — jeweils
seit Turnbeginn. Gemessen am 23.09.2026: Sitzung 20260921_015554_e79a4a0f scheiterte ab 18:27:39 an der Verdichtung
(401, widerrufene Anmeldung) und starb um 19:35 mit 1.001.191 von 1.000.000 Token — das Rundenlimit griff nie.
--jetzt wirkt auch auf Nachrichten und Logzeilen: ein früherer Zeitpunkt lässt sich so aus den echten Daten nachspielen.

Was ausgelöst wird. Ein NEUER Ordner''')
ersetze('''    <Prüfkanal>/laeufe/<auftrag>/zwischenbericht-<JJJJMMTT-HHMMSS>-r<runden>/''',
        '''    <Prüfkanal>/laeufe/<auftrag>/zwischenbericht-<JJJJMMTT-HHMMSS>-r<runden>[-kontext80][-verdichtung]/''')
ersetze('''HASH_GRENZE = 20 * 1024 * 1024
''', '''HASH_GRENZE = 20 * 1024 * 1024
KONTEXT_ANTEIL = 0.80
LOG_DATEIEN = ('agent.log.1', 'agent.log')          # chronologisch: rotierte Datei zuerst
LOG_REST = 6 * 1024 * 1024                            # je Datei nur das Ende lesen
ZEIT_RE = re.compile(r'^(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}),(\\d{3}) ')
API_RE = re.compile(r'\\] agent\\.conversation_loop: API call #\\d+: model=(\\S+) provider=(\\S+) in=(\\d+)')
''')
ersetze('''def turn_beginn(con, sid: str):
    for r in con.execute("SELECT id, content, timestamp FROM messages WHERE session_id=? AND role='user' ORDER BY id DESC", (sid,)):''',
        '''def turn_beginn(con, sid: str, jetzt: float | None = None):
    for r in con.execute("SELECT id, content, timestamp FROM messages WHERE session_id=? AND role='user' "
                         "AND COALESCE(timestamp, 0) <= ? ORDER BY id DESC", (sid, jetzt if jetzt is not None else 9e18)):''')
ersetze('''def runden(con, sid: str, ab_id: int) -> int:
    return con.execute(
        "SELECT COUNT(*) FROM messages WHERE session_id=? AND id>? AND role='assistant' AND tool_calls IS NOT NULL "
        "AND tool_calls NOT IN ('', '[]', 'null')", (sid, ab_id)).fetchone()[0]''',
        '''def runden(con, sid: str, ab_id: int, jetzt: float | None = None) -> int:
    return con.execute(
        "SELECT COUNT(*) FROM messages WHERE session_id=? AND id>? AND role='assistant' AND tool_calls IS NOT NULL "
        "AND tool_calls NOT IN ('', '[]', 'null') AND COALESCE(timestamp, 0) <= ?",
        (sid, ab_id, jetzt if jetzt is not None else 9e18)).fetchone()[0]


def log_zeilen(home: Path, jetzt: float) -> list:
    """(Zeit, Zeile) aus dem Ende von agent.log.1 und agent.log, nur Zeilen mit Zeitstempel bis `jetzt`."""
    out = []
    for name in LOG_DATEIEN:
        try:
            with open(home / 'logs' / name, 'rb') as f:
                f.seek(0, 2)
                f.seek(max(0, f.tell() - LOG_REST))
                daten = f.read().decode('utf-8', errors='replace')
        except OSError:
            continue
        for z in daten.splitlines():
            m = ZEIT_RE.match(z)
            if not m:
                continue
            try:
                t = datetime.strptime(m.group(1), '%Y-%m-%d %H:%M:%S').timestamp() + int(m.group(2)) / 1000
            except ValueError:
                continue
            if t <= jetzt:
                out.append((t, z))
    out.sort(key=lambda x: x[0])
    return out


def kontextgrenze(home: Path, modell: str, anbieter: str, zeilen: list, sid: str):
    try:
        d = json.loads((home / 'models_dev_cache.json').read_text())
        g = ((((d.get(anbieter) or {}).get('models') or {}).get(modell) or {}).get('limit') or {}).get('context')
        if g:
            return int(g), f'models.dev {anbieter}/{modell}'
    except (OSError, ValueError, AttributeError, TypeError):
        pass
    try:
        for zeile in (home / 'context_length_cache.yaml').read_text().splitlines():
            m = re.match(r'\\s+(\\S+?)@\\S+:\\s*(\\d+)\\s*$', zeile)
            if m and m.group(1) == modell:
                return int(m.group(2)), 'context_length_cache.yaml'
    except OSError:
        pass
    for _t, z in reversed(zeilen):
        if 'compression attempt telemetry' in z and f'"session_id":"{sid}"' in z and '"main_context_limit":' in z:
            return int(re.search(r'"main_context_limit":(\\d+)', z).group(1)), 'Verdichter-Telemetrie'
    return None, 'unbekannt'


def kontextstand(home: Path, zeilen: list, sid: str):
    """Eingabetoken der letzten Modellanfrage dieser Sitzung gegen das Kontextfenster ihres Modells."""
    for t, z in reversed(zeilen):
        if f'[{sid}]' in z and (m := API_RE.search(z)):
            modell, anbieter, tokens = m.group(1), m.group(2), int(m.group(3))
            g, quelle = kontextgrenze(home, modell, anbieter, zeilen, sid)
            return {'tokens': tokens, 'grenze': g, 'grenze_quelle': quelle, 'modell': f'{anbieter}/{modell}',
                    'anteil_roh': tokens / g if g else None, 'anteil': round(tokens / g, 4) if g else None, 'zeit': iso(t)}
    return None


def verdichtung_fehlschlag(con, zeilen: list, sid: str, ab: float, jetzt: float):
    """Erste gescheiterte Verdichtung dieser Sitzung seit `ab` (Turnbeginn), sonst None."""
    meldung = ''
    for t, z in zeilen:
        if 'Failed to generate context summary:' in z:
            meldung = z.split('Failed to generate context summary:', 1)[1].strip()
        if t < ab:
            continue
        if 'compression attempt telemetry' in z and f'"session_id":"{sid}"' in z:
            m = re.search(r'"failure_class":"([^"]+)"', z)
            if m or '"commit_status":"aborted"' in z:
                return {'zeit': iso(t), 'quelle': 'agent.log (Verdichter-Telemetrie)', 'art': m.group(1) if m else 'aborted',
                        'meldung': meldung[:600]}
        if f'[{sid}]' in z and 'Context compression failed' in z:
            return {'zeit': iso(t), 'quelle': 'agent.log', 'art': 'compression_failed',
                    'meldung': z.split('agent.conversation_loop:', 1)[-1].strip()[:600]}
    try:
        r = con.execute('SELECT compression_failure_cooldown_until, compression_failure_error FROM sessions WHERE id=?',
                        (sid,)).fetchone()
    except sqlite3.Error:                     # Schema ohne diese Spalten (ältere state.db, Test-Attrappe)
        r = None
    if r and r[1] and r[0] and ab <= float(r[0]) <= jetzt + 600:
        return {'zeit': iso(float(r[0])) + ' (Sperre bis)', 'quelle': 'state.db sessions.compression_failure_error',
                'art': 'sperre', 'meldung': str(r[1])[:600]}
    return None''')
ersetze('''def ordnername(auftrag: str, jetzt: float, n: int) -> str:
    name = re.sub(r'[^A-Za-z0-9._-]', '-', auftrag or 'zwischenberichte')
    return f"laeufe/{name}/zwischenbericht-{datetime.fromtimestamp(jetzt).strftime('%Y%m%d-%H%M%S')}-r{n}"''',
        '''def ordnername(auftrag: str, jetzt: float, n: int, zusatz: str = '') -> str:
    name = re.sub(r'[^A-Za-z0-9._-]', '-', auftrag or 'zwischenberichte')
    return f"laeufe/{name}/zwischenbericht-{datetime.fromtimestamp(jetzt).strftime('%Y%m%d-%H%M%S')}-r{n}{zusatz}"''')
ersetze('''def bericht(con, sid: str, turn_id: int, turn: dict, n: int, g: int, schwelle, auftrag: dict, jetzt: float) -> str:''',
        '''def bericht(con, sid: str, turn_id: int, turn: dict, n: int, g: int, schwelle, auftrag: dict, jetzt: float,
            anlass: str = '') -> str:''')
ersetze('''         f"Werkzeugrunde **{n} von {g}** (Schwelle {schwelle}).",''',
        '''         f"Werkzeugrunde **{n} von {g}** (Schwelle {schwelle}).", f"Anlass: {anlass or 'Rundenschwelle'}.",''')
ersetze('''def veroeffentlichen(*, con, sid, turn_id, turn, n, g, schwelle, home, wurzel, url_basis, jetzt, https, besitzer) -> str:
    auftrag = lade(home / 'zwischenbericht' / 'auftrag.json')
    rel = ordnername(auftrag.get('auftrag') or 'zwischenberichte', jetzt, n)''',
        '''def veroeffentlichen(*, con, sid, turn_id, turn, n, g, schwelle, home, wurzel, url_basis, jetzt, https, besitzer,
                     anlass: str = '', zusatz: str = '') -> str:
    auftrag = lade(home / 'zwischenbericht' / 'auftrag.json')
    rel = ordnername(auftrag.get('auftrag') or 'zwischenberichte', jetzt, n, zusatz)''')
ersetze('''    inhalte = {'ZWISCHENBERICHT.md': bericht(con, sid, turn_id, turn, n, g, schwelle, auftrag, jetzt).encode()}''',
        '''    inhalte = {'ZWISCHENBERICHT.md': bericht(con, sid, turn_id, turn, n, g, schwelle, auftrag, jetzt, anlass).encode()}''')
ersetze('''    return (f'Zwischenbericht ausgelöst: {url}/DATEIEN.txt | Runde {n} von {g} (Schwelle {schwelle}) | {pruefung} | '
            f'Ordnerprüfsumme {ordner}')''',
        '''    return (f'Zwischenbericht ausgelöst: {url}/DATEIEN.txt | Runde {n} von {g} (Schwelle {schwelle}) | '
            f'Anlass: {anlass or "Rundenschwelle"} | {pruefung} | Ordnerprüfsumme {ordner}')''')
ersetze('''    ausgaben = []
    for i, s in enumerate(sitzungen(con, jetzt)):
        tb = turn_beginn(con, s['id'])
        if not tb:
            continue
        turn_id, turn = tb
        n = runden(con, s['id'], turn_id)
        herz['sitzungen'].append({'sitzung': s['id'], 'turn_ab': turn_id, 'runden': n})
        faellig = [x for x in sw if n >= x and f"{s['id']}:{turn_id}:{x}" not in zustand]
        schwelle = max(faellig) if faellig else None
        if a.sofort and i == 0:
            schwelle, faellig = 'sofort', [f'sofort-{int(jetzt)}']
        if schwelle is None:
            continue
        try:
            zeile = veroeffentlichen(con=con, sid=s['id'], turn_id=turn_id, turn=turn, n=n, g=g, schwelle=schwelle,
                                     home=home, wurzel=a.pruefkanal_wurzel, url_basis=a.url_basis, jetzt=jetzt,
                                     https=not a.ohne_https, besitzer=not a.kein_besitzer)''',
        '''    ausgaben = []
    zeilen = log_zeilen(home, jetzt)
    for i, s in enumerate(sitzungen(con, jetzt)):
        tb = turn_beginn(con, s['id'], jetzt)
        if not tb:
            continue
        turn_id, turn = tb
        n = runden(con, s['id'], turn_id, jetzt)
        ks = kontextstand(home, zeilen, s['id'])
        vf = verdichtung_fehlschlag(con, zeilen, s['id'], float(turn['zeit'] or 0), jetzt)
        herz['sitzungen'].append({'sitzung': s['id'], 'turn_ab': turn_id, 'runden': n,
                                  'kontext': {k: v for k, v in (ks or {}).items() if k != 'anteil_roh'} or None,
                                  'verdichtung_gescheitert': vf})
        faellig = [x for x in sw if n >= x and f"{s['id']}:{turn_id}:{x}" not in zustand]
        schwelle = max(faellig) if faellig else '–'
        anlass, zusatz = ([f'Werkzeugrunde {n} von {g}'] if faellig else []), ''
        if ks and ks['anteil_roh'] is not None and ks['anteil_roh'] >= KONTEXT_ANTEIL \\
                and f"{s['id']}:{turn_id}:kontext80" not in zustand:
            faellig.append('kontext80')
            zusatz += '-kontext80'
            anlass.append(f"Kontextfüllung {ks['anteil_roh'] * 100:.1f} % ({ks['tokens']} von {ks['grenze']} Token, "
                          f"{ks['modell']}, Stand {ks['zeit']}; Schwelle 80 %)")
        if vf and f"{s['id']}:{turn_id}:verdichtung" not in zustand:
            faellig.append('verdichtung')
            zusatz += '-verdichtung'
            anlass.append(f"Verdichtung gescheitert {vf['zeit']} ({vf['art']}, {vf['quelle']}): {vf['meldung'][:400]}")
        if a.sofort and i == 0:
            schwelle, faellig, anlass, zusatz = 'sofort', [f'sofort-{int(jetzt)}'], ['sofort (von Hand ausgelöst)'], ''
        if not faellig:
            continue
        try:
            zeile = veroeffentlichen(con=con, sid=s['id'], turn_id=turn_id, turn=turn, n=n, g=g, schwelle=schwelle,
                                     home=home, wurzel=a.pruefkanal_wurzel, url_basis=a.url_basis, jetzt=jetzt,
                                     https=not a.ohne_https, besitzer=not a.kein_besitzer, anlass='; '.join(anlass),
                                     zusatz=zusatz)''')
S.write_text(s)

t = T.read_text()
alt = "    jetzt = 1790000000.0\n"
assert t.count(alt) == 1
# --jetzt wirkt jetzt auch auf Nachrichten (Nachspiel): der Zeitpunkt muss nach den eben geschriebenen Nachrichten liegen
t = t.replace(alt, "    jetzt = time.time() + 5          # geändert (Kontext-Auslöser): --jetzt filtert jetzt auch Nachrichten\n")
t += '''

# ================================================================ Zweiter Auslöser: Kontextfüllung und Verdichtung
from datetime import datetime  # noqa: E402


def _ts(t=None):
    t = time.time() if t is None else t
    return datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S') + f',{int(t * 1000) % 1000:03d}'


def _log(u, zeilen):
    (u['home'] / 'logs').mkdir(exist_ok=True)
    with open(u['home'] / 'logs' / 'agent.log', 'a') as f:
        for z in zeilen:
            f.write(z + '\\n')


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
'''
T.write_text(t)
print('ok', stempel)
'''
'''
