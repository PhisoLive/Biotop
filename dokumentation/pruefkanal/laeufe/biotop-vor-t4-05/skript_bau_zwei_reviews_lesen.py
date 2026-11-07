"""Nur lesend: Wie entstanden zwei Reviews der Runde 5? Protokolle, Sitzungen (state.db mode=ro), Delegationslog.
Ausgabe nach /root/biotop-vor-t4-05/bau/ZWEI-REVIEWS-ROH.txt (wird vom Aufrufer umgeleitet)."""
import json
import re
import sqlite3
from pathlib import Path

H = Path('/root/.hermes')


def zeilen(datei, von, bis, muster=None, n=120):
    aus = []
    for z in Path(datei).read_text(errors='replace').splitlines():
        m = re.match(r'(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d)', z)
        if not m or not (von <= m.group(1) <= bis):
            continue
        if muster and not re.search(muster, z):
            continue
        aus.append(z[:320])
    return aus[:n]


print('== gateway.log 20:25–22:20 (Sitzung/Delegation/Telegram/Neustart)')
for z in zeilen(H / 'logs/gateway.log', '2026-09-24 20:25:00', '2026-09-24 22:20:00',
                r'(?i)session|delegat|subagent|telegram|restart|start|stop|resum|interrupt|compress|drop|adopt|attach|takeover|orphan'):
    print(z)
print('\n== agent.log 20:25–22:20 (Sitzung/Delegation/Unterbrechung/Kompression)')
for z in zeilen(H / 'logs/agent.log', '2026-09-24 20:25:00', '2026-09-24 22:20:00',
                r'(?i)delegat|subagent|resum|interrupt|compress|new session|session_id|rotat|handoff|takeover|orphan|telegram|gone',
                n=80):
    print(z)
print('\n== Delegationslog task-0.log')
t = (H / 'cache/delegation/live/deleg_b1c00361/task-0.log').read_text(errors='replace').splitlines()
print('zeilen', len(t))
for z in t[:6] + ['…'] + t[-25:]:
    print('  ', z[:300])
print('\n== process-results proc_0423d3933e03.json')
print((H / 'logs/process-results/proc_0423d3933e03.json').read_text()[:1500])
print('\n== state.db (mode=ro): Sitzungen seit 2026-09-24 15:00')
con = sqlite3.connect(f'file:{H}/state.db?mode=ro', uri=True)
con.row_factory = sqlite3.Row
tabellen = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")]
print('tabellen', tabellen)
spalten = [r[1] for r in con.execute('PRAGMA table_info(sessions)')]
print('sessions-spalten', spalten)
zeit = 'started_at' if 'started_at' in spalten else spalten[0]
for r in con.execute(f"SELECT * FROM sessions ORDER BY {zeit} DESC LIMIT 40"):
    d = dict(r)
    kurz = {k: (str(v)[:80] if v is not None else None) for k, v in d.items()
            if k in ('id', 'source', 'platform', 'parent_session_id', 'started_at', 'ended_at', 'end_reason', 'title',
                     'message_count', 'tool_call_count', 'model', 'user_id', 'chat_id')}
    print(json.dumps(kurz, ensure_ascii=False))
mspalten = [r[1] for r in con.execute('PRAGMA table_info(messages)')]
print('messages-spalten', mspalten)
