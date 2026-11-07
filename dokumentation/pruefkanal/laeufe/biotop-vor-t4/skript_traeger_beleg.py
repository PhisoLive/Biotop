"""Beleg Träger: Grundwert Modell + Denkstufe, von der Datei bis zum Anfragekörper, dazu die Verdichtungsroute.

Stufen (measurement-harness-discipline, runtime-configuration-verification):
  1 Datei (config.yaml, gelesen über Hermes' eigenen Lader)
  5 Auflöser im Prozess (hermes_constants.resolve_reasoning_config — laut Quelltext die eine Stelle für CLI, Gateway, Cron)
    + Klemmprüfung an der Transportgrenze (anthropic_adapter._thinking_kwargs für genau dieses Modell)
  6 Anfragekörper einer echten Anfrage: frischer Prozess `hermes chat -q … --oneshot` mit HERMES_DUMP_REQUESTS=1
    (Dump 'preflight' vor dem Senden, Geheimnisse geschwärzt). Kein Modell/keine Denkstufe auf der Befehlszeile —
    geprüft wird der Grundwert.
  Verdichtung: dieselbe Hilfsroute wie der Verdichter (auxiliary_client.call_llm, task='compression'), echte Anfrage.
Kosten: 2 Anfragen über die Anthropic-Anmeldung des Trägers (Abo), kein Biotop-Geld.
Aufruf: /usr/local/lib/hermes-agent/venv/bin/python traeger_beleg.py
"""
import glob
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, '/usr/local/lib/hermes-agent')
AUS = Path('/root/biotop-vor-t4/traeger')
beleg = {'zeit': time.strftime('%Y-%m-%d %H:%M:%S %z')}

from hermes_cli.config import load_config_readonly  # noqa: E402
from hermes_constants import resolve_reasoning_config  # noqa: E402
from agent.anthropic_adapter import _thinking_kwargs  # noqa: E402

cfg = load_config_readonly()
modell = (cfg.get('model') or {}).get('default')
beleg['stufe1_datei'] = {'model.default': modell, 'model.provider': (cfg.get('model') or {}).get('provider'),
                         'agent.reasoning_effort': (cfg.get('agent') or {}).get('reasoning_effort'),
                         'config_sha256': hashlib.sha256(Path('/root/.hermes/config.yaml').read_bytes()).hexdigest()}
rc = resolve_reasoning_config(cfg, modell)
beleg['stufe5_aufloeser'] = {'resolve_reasoning_config': rc,
                             'klemme_thinking_kwargs': _thinking_kwargs(rc or {}, modell, 128000)}
try:
    from gateway.run import _resolve_gateway_model, _load_gateway_config  # noqa: E402
    gcfg = _load_gateway_config()
    beleg['stufe5_gateway'] = {'_resolve_gateway_model': _resolve_gateway_model(gcfg),
                               'reasoning_fuer_dieses_modell': resolve_reasoning_config(gcfg, _resolve_gateway_model(gcfg))}
except Exception as e:  # Befund, kein stilles Weiter
    beleg['stufe5_gateway'] = {'fehler': f'{type(e).__name__}: {e}'}

# ---- Stufe 6: echte Anfrage, Körper aus dem Dump
start = time.time()
vorher = set(glob.glob('/root/.hermes/sessions/request_dump_*.json'))
env = dict(os.environ, HERMES_DUMP_REQUESTS='1')
for k in ('HERMES_SESSION_KEY', 'HERMES_SESSION_ID', 'HERMES_UI_SESSION_ID', 'HERMES_SESSION_PLATFORM', 'HERMES_CRON_SESSION'):
    env.pop(k, None)
p = subprocess.run(['/usr/local/lib/hermes-agent/venv/bin/hermes', 'chat', '-q', 'Antworte nur mit dem Wort: BELEG',
                    '--oneshot', '-Q', '-t', 'todo'], capture_output=True, text=True, timeout=600, env=env, cwd='/root')
neu = sorted(set(glob.glob('/root/.hermes/sessions/request_dump_*.json')) - vorher, key=os.path.getmtime)
beleg['stufe6_cli'] = {'rc': p.returncode, 'stdout_ende': p.stdout.strip()[-300:], 'stderr_ende': p.stderr.strip()[-600:],
                       'dauer_s': round(time.time() - start, 1), 'dumps': neu}
if neu:
    d = json.loads(Path(neu[0]).read_text())
    body = d['request']['body']
    beleg['stufe6_anfragekoerper'] = {
        'dump_datei': neu[0], 'dump_sha256': hashlib.sha256(Path(neu[0]).read_bytes()).hexdigest(),
        'reason': d.get('reason'), 'url': d['request']['url'], 'session_id': d.get('session_id'),
        'felder': sorted(body.keys()),
        **{k: body.get(k) for k in ('model', 'thinking', 'output_config', 'max_tokens', 'temperature')},
        'nachrichten': len(body.get('messages') or [])}

# ---- Verdichtungsroute (task='compression'), echte Hilfsanfrage
from agent.auxiliary_client import call_llm  # noqa: E402
route = {}
t0 = time.time()
try:
    r = call_llm(task='compression', messages=[{'role': 'user', 'content':
                 'Fasse in genau einem Satz zusammen: Der Wächter prüft jede Minute die Sitzungen und legt bei Gefahr einen Zwischenbericht ab.'}],
                 route_info=route)
    text = r.choices[0].message.content if hasattr(r, 'choices') else str(r)
    beleg['verdichtung_route'] = {'ergebnis': 'ok', 'route': route, 'antwort': (text or '')[:300], 'dauer_s': round(time.time() - t0, 1)}
except Exception as e:
    beleg['verdichtung_route'] = {'ergebnis': 'gescheitert', 'route': route, 'meldung_wörtlich': f'{type(e).__name__}: {e}'[:1500]}

(AUS / 'TRAEGER-BELEG.json').write_text(json.dumps(beleg, ensure_ascii=False, indent=1, default=str))
print(json.dumps(beleg, ensure_ascii=False, indent=1, default=str)[:6000])
