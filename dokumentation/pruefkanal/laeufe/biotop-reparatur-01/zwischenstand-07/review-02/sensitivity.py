"""Controlled in-memory mutations: prove existing core tests go red."""
import sys
from pathlib import Path
import pytest
from biotop.kern import messgeraet as M
ROOT=Path(__file__).resolve().parent
assert Path(M.__file__).resolve().is_relative_to(ROOT/'arbeitskopie')
mode=sys.argv[1]
if mode=='kern-belohnt-gruen':
    original=M.kernmass_f2_bereich
    M.kernmass_f2_bereich=lambda b: original(b)+b['tests_bestanden']
elif mode=='pareto-ohne-einzeltest':
    original=M.pareto_f2
    def ohne(*args,**kw):
        bad,good=original(*args,**kw)
        return [x for x in bad if not x.startswith('Regression je Test')],good
    M.pareto_f2=ohne
else:
    raise ValueError(mode)
print('REVIEWER MUTATION: '+mode+'; process-local only, source unchanged')
raise SystemExit(pytest.main(['-q','-p','no:cacheprovider','--tb=short',
 f'--basetemp={ROOT}/tmp/{mode}',f'--junitxml={ROOT}/sensitivity-{mode}.xml',
 'tests/test_kernmass_pareto.py']))
