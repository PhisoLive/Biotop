"""Run bounded offline review tests and retain all output."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

out = Path(__file__).resolve().parent
repo = out / 'arbeitskopie'
python = '/root/reparatur-01/venv/bin/python'
env = dict(os.environ,
           PYTHONPATH=os.pathsep.join([str(out/'guard'), str(repo), str(repo/'tests')]),
           PYTHONDONTWRITEBYTECODE='1', TMPDIR=str(out/'tmp'),
           BIOTOP_DB=str(out/'tmp'/'unused-default.db'),
           PYTEST_DISABLE_PLUGIN_AUTOLOAD='1')
for key in list(env):
    if key in ('BIOTOP_EICHWERK', 'BIOTOP_EICHDB', 'BIOTOP_EICHBELEG') or key.endswith(('_API_KEY', '_TOKEN')):
        env.pop(key)
commands = [
    ('provided-unit', [python, '-m', 'pytest', '-vv', '-s',
                      'tests/test_vorspann.py', 'tests/test_vorspann_cli.py',
                      'tests/test_kernmass_pareto.py', 'tests/test_rauschmessung.py',
                      '--basetemp='+str(out/'tmp'/'provided-unit'),
                      '--junitxml='+str(out/'provided-unit.xml')]),
    ('independent-review', [python, '-m', 'pytest', '-vv', '-s', '-c', str(repo/'pytest.ini'),
                            str(out/'test_review.py'), '--basetemp='+str(out/'tmp'/'independent-review'),
                            '--junitxml='+str(out/'independent-review.xml')]),
]
records = []
for name, cmd in commands:
    t0 = time.monotonic()
    p = subprocess.run(cmd, cwd=repo, env=env, text=True, capture_output=True, timeout=180)
    (out/(name+'.stdout.txt')).write_text(p.stdout)
    (out/(name+'.stderr.txt')).write_text(p.stderr)
    r = {'name':name, 'cmd':cmd, 'cwd':str(repo), 'exit_code':p.returncode,
         'duration_s':time.monotonic()-t0, 'stdout':str(out/(name+'.stdout.txt')),
         'stderr':str(out/(name+'.stderr.txt')), 'docker_runs':0, 'paid_calls':0,
         'evidence':'UNIT. See test docstrings for explicit doubles.'}
    records.append(r)
    print(json.dumps(r), flush=True)
(out/'executions.json').write_text(json.dumps(records, ensure_ascii=False, indent=2))
