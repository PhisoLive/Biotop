"""Nachspiel des erweiterten Wächters an den ECHTEN Daten der am Kontext gestorbenen Sitzung 20260921_015554_e79a4a0f.

Minütlich wie der Zeitplan, von Turnbeginn (15:53:55, Nachricht 14000) bis zum Tod der Sitzung (19:35:07), mit --jetzt.
Echt: state.db (nur gelesen, mode=ro), agent.log/agent.log.1, models_dev_cache.json, config.yaml (als Kopien/Links in
einem Wegwerf-Home, damit der echte Wächterzustand ausgeloest.json/herzschlag.json unberührt bleibt). Prüfkanal: eine
Attrappe unter /tmp, ohne HTTPS, ohne Besitzerwechsel. Frage: WANN hätte der neue Auslöser gefeuert, und hätte der alte
(Runden) überhaupt gefeuert?"""
import contextlib
import importlib.util
import io
import json
import shutil
import time
from datetime import datetime
from pathlib import Path

SKRIPT = Path('/root/.hermes/scripts/zwischenbericht_waechter.py')
spec = importlib.util.spec_from_file_location('w', SKRIPT)
W = importlib.util.module_from_spec(spec)
spec.loader.exec_module(W)

H = Path('/tmp/waechter-nachspiel/home')
shutil.rmtree('/tmp/waechter-nachspiel', ignore_errors=True)
(H / 'zwischenbericht').mkdir(parents=True)
(H / 'logs').mkdir()
for n in ('agent.log', 'agent.log.1'):
    (H / 'logs' / n).symlink_to(f'/root/.hermes/logs/{n}')
for n in ('models_dev_cache.json', 'context_length_cache.yaml', 'config.yaml'):
    shutil.copy2(f'/root/.hermes/{n}', H / n)
shutil.copy2('/root/.hermes/zwischenbericht/auftrag.json', H / 'zwischenbericht' / 'auftrag.json')
WURZEL = Path('/tmp/waechter-nachspiel/akte')
WURZEL.mkdir()
echt_zustand = Path('/root/.hermes/zwischenbericht/ausgeloest.json').read_bytes()

SID = '20260921_015554_e79a4a0f'
start = datetime(2026, 9, 23, 15, 54, 0).timestamp()
ende = datetime(2026, 9, 23, 19, 35, 7).timestamp()
ausloesungen, verlauf = [], []
t = start
while t <= ende + 60:
    puffer = io.StringIO()
    with contextlib.redirect_stdout(puffer):
        rc = W.main(['--state-db', '/root/.hermes/state.db', '--hermes-home', str(H), '--pruefkanal-wurzel', str(WURZEL),
                     '--url-basis', 'https://beispiel.invalid/_akte/k', '--ohne-https', '--kein-besitzer', '--jetzt', str(t)])
    herz = json.loads((H / 'zwischenbericht' / 'herzschlag.json').read_text())
    s = next((x for x in herz['sitzungen'] if x['sitzung'] == SID), None)
    if s:
        verlauf.append({'zeit': W.iso(t), 'runden': s['runden'], 'kontext': (s.get('kontext') or {}).get('anteil'),
                        'verdichtung': bool(s.get('verdichtung_gescheitert'))})
    for z in puffer.getvalue().splitlines():
        if SID in z or 'ausgelöst' in z:
            ausloesungen.append({'zeit': W.iso(t), 'rc': rc, 'zeile': z})
    t += 60
ordner = sorted(p.name for p in (WURZEL / 'laeufe').rglob('zwischenbericht-*'))
erster = {}
for v in verlauf:
    if v['kontext'] is not None and v['kontext'] >= 0.8 and 'kontext80' not in erster:
        erster['kontext80'] = v
    if v['verdichtung'] and 'verdichtung' not in erster:
        erster['verdichtung'] = v
    if v['runden'] >= 110 and 'runden110' not in erster:
        erster['runden110'] = v
ergebnis = {'sitzung': SID, 'minuten': len(verlauf), 'ausloesungen': ausloesungen, 'ordner': ordner, 'erste': erster,
            'hoechste_runde': max((v['runden'] for v in verlauf), default=None),
            'echter_zustand_unberuehrt': Path('/root/.hermes/zwischenbericht/ausgeloest.json').read_bytes() == echt_zustand,
            'verlauf_auszug': verlauf[::15]}
Path('/root/biotop-vor-t4/waechter/NACHSPIEL-ECHTE-SITZUNG.json').write_text(json.dumps(ergebnis, ensure_ascii=False, indent=1))
print(json.dumps({k: v for k, v in ergebnis.items() if k != 'verlauf_auszug'}, ensure_ascii=False, indent=1)[:5000])
