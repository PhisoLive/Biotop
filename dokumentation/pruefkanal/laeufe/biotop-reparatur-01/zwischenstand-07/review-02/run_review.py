"""Bounded reviewer jobs; command, streams, rc retained separately."""
from pathlib import Path
import json, os, subprocess, sys, time
ROOT=Path(__file__).resolve().parent
PY='/root/reparatur-01/venv/bin/python'
env=dict(os.environ, PYTHONPATH=os.pathsep.join([str(ROOT/'guard'),str(ROOT/'arbeitskopie'),str(ROOT/'arbeitskopie'/'tests')]),
         TMPDIR=str(ROOT/'tmp'), PYTHONDONTWRITEBYTECODE='1',
         PYTEST_DISABLE_PLUGIN_AUTOLOAD='1', BIOTOP_DB=str(ROOT/'tmp'/'unused.db'))
for k in ('BIOTOP_EICHWERK','BIOTOP_EICHDB','BIOTOP_EICHBELEG','BIOTOP_VERTRAGSBELEGE'):
    env.pop(k,None)
jobs={
 'cli-evidence': [PY,str(ROOT/'check_cli_evidence.py')],
 'evidence': [PY,str(ROOT/'check_evidence.py')],
 'sensitivity-kern': [PY,str(ROOT/'sensitivity.py'),'kern-belohnt-gruen'],
 'sensitivity-pareto': [PY,str(ROOT/'sensitivity.py'),'pareto-ohne-einzeltest'],
 'gen0-route': [PY,'-m','pytest','-q','-s','-p','no:cacheprovider',f'--basetemp={ROOT}/tmp/gen0-route',f'--junitxml={ROOT}/gen0-route.xml',str(ROOT/'test_independent_gen0.py')],
 'skip-repro-expanded': [PY,str(ROOT/'repro_skip_vertragszeuge.py')],
 'skip-repro': [PY,str(ROOT/'repro_skip_vertragszeuge.py')],
 'core-unit': [PY,'-m','pytest','-q','-v','--tb=short',f'--basetemp={ROOT}/tmp/core-unit',f'--junitxml={ROOT}/core-unit.xml',
   'tests/test_kernmass_pareto.py','tests/test_testreihenfolge.py',
   'tests/test_vorspann.py::test_unit_erfolgreicher_vorspann_vor_gen0_und_mass',
   'tests/test_vorspann.py::test_unit_unvollstaendige_eichung_liefert_keinen_nachweis_oder_retry',
   'tests/test_vorspann.py::test_unit_voraussetzungen_vor_erster_messung',
   'tests/test_vorspann.py::test_vorstufen_ohne_vorspann_starten_nicht',
   'tests/test_vorspann_cli.py'],
}
for name in sys.argv[1:] or jobs:
    command=jobs[name]; start=time.monotonic()
    result=subprocess.run(command,cwd=ROOT/'arbeitskopie',env=env,capture_output=True,text=True,timeout=150)
    (ROOT/f'{name}.stdout.txt').write_text(result.stdout)
    (ROOT/f'{name}.stderr.txt').write_text(result.stderr)
    meta=dict(command=command,cwd=str(ROOT/'arbeitskopie'),env={k:env[k] for k in ('PYTHONPATH','TMPDIR','PYTHONDONTWRITEBYTECODE','PYTEST_DISABLE_PLUGIN_AUTOLOAD','BIOTOP_DB')},rc=result.returncode,duration_s=time.monotonic()-start)
    (ROOT/f'{name}.execution.json').write_text(json.dumps(meta,indent=2)+'\n')
    print(json.dumps(meta))
    print(result.stdout[-4500:]); print(result.stderr)
