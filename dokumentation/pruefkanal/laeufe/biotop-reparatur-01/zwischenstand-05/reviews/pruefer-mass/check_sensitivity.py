"""Intentional in-memory mutations to test sensitivity. Never writes product source."""
import inspect
import sys
import run_unit_checks as guard
from biotop.kern import messgeraet as M
from biotop.kern.datenbank import lj
from biotop.organe import aegis as A, gedaechtnis as G
import pytest

mode = sys.argv[1]
selected = []
if mode == 'kernmass_rewards_passes':
    original = M.kernmass_f2_bereich
    M.kernmass_f2_bereich = lambda b: original(b) + b['tests_bestanden']
    selected = ['tests/test_kernmass_pareto.py']
elif mode == 'pareto_aggregate_only':
    original = M.pareto_f2
    def aggregate_only(*a, **kw):
        bad, good = original(*a, **kw)
        return [s for s in bad if not s.startswith('Regression je Test')], good
    M.pareto_f2 = aggregate_only
    selected = ['tests/test_kernmass_pareto.py']
elif mode == 'ignore_measured_tolerance':
    original = M.urteil_f2
    def fallback(basis, kandidat, ausgang, bereiche, wirkungskreis, tausch=None, nische=None):
        t = dict(tausch or {})
        t.pop('_rauschtoleranz',None)
        return original(basis,kandidat,ausgang,bereiche,wirkungskreis,t,nische)
    M.urteil_f2 = fallback
    selected = ['tests/test_rauschmessung.py::test_urteil_verwendet_gemessene_statt_fester_rauschtoleranz']
elif mode == 'rounded_outlier_identity':
    original = M.rauschtoleranz_aus_werten
    def rounded(*a, **kw):
        r=original(*a, **kw)
        r['aussetzer']=[round(v,2) for v in r['aussetzer']]
        return r
    M.rauschtoleranz_aus_werten=rounded
    selected=['tests/test_rauschmessung.py::test_aussetzer_wird_ungekuerzt_entfernt_und_einmal_ersetzt',
              'tests/test_rauschmessung.py::test_gescheitertes_nachmessen_sperrt_den_bereich']
elif mode == 'self_announcement_not_exempt':
    original = A.aufnahmesperre
    def no_exemption(*a, **kw):
        kw.pop('eigene_ansage_nr',None)
        return original(*a, **kw)
    A.aufnahmesperre=no_exemption
    selected=['tests/test_ansage_aufnahme.py::test_erster_neuer_test_wird_nicht_von_eigener_ansage_gesperrt']
elif mode == 'erase_history_by_key':
    original=A.bisherige_behauptungen
    def erase(con,werk_id,bereich,lauf_id=None,limit=25,*,ohne_ansage_nr=None):
        r=original(con,werk_id,bereich,lauf_id,limit,ohne_ansage_nr=ohne_ansage_nr)
        if ohne_ansage_nr is not None:
            row=con.execute('SELECT inhalt FROM protokoll WHERE nr=?',(ohne_ansage_nr,)).fetchone()
            key=lj(row[0]).get('behauptung')
            r=[k for k in r if k!=key]
        return r
    A.bisherige_behauptungen=erase
    selected=['tests/test_ansage_aufnahme.py::test_nur_die_aktuelle_ansagezeile_ist_ausgenommen']
elif mode in ('foreign_quota_floor','foreign_global_window'):
    source=inspect.getsource(G.art_text)
    old,new=(('(GEZEIGT + 1) // 2','GEZEIGT // 2') if mode=='foreign_quota_floor' else
             ('art_lesen(con, None, None, nur_angenommen=True, fremd_zu=eigen_werk)',
              'art_lesen(con, None, 200, nur_angenommen=True)'))
    assert source.count(old)==1
    namespace=dict(G.__dict__)
    exec(compile(source.replace(old,new),f'<review-mutation:{mode}>','exec'),namespace)
    G.art_text=namespace['art_text']
    selected=['tests/test_artvorlage.py']
else:
    raise ValueError(mode)

print('INTENTIONAL_RUNTIME_MUTATION',mode)
raise SystemExit(pytest.main(['-q','-p','no:cacheprovider','--basetemp',str(guard.TMP/mode),
                            '--junitxml',str(guard.OUT/(mode+'.xml')),*selected]))
