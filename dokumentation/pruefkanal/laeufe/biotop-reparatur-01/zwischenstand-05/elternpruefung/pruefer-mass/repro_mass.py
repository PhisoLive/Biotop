"""Isolated reviewer repros. Boundary measurements are explicit doubles, not timing claims."""
from pathlib import Path
from copy import deepcopy
from contextlib import ExitStack
from difflib import unified_diff
from unittest.mock import patch
import json
import os
import socket
import sqlite3
import sys
import tempfile

ROOT = Path('/root/reparatur-01/eltern-reviewpruefung')
OUT = ROOT / 'pruefer-mass'
TMP = OUT / 'tmp-repro'
TMP.mkdir(exist_ok=True)
os.environ['TMPDIR'] = str(TMP)
os.environ['BIOTOP_DB'] = str(TMP / 'unused.db')
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'repo'))

def forbidden(*a, **k):
    raise AssertionError('Reviewer guard: chamber/model/network/subprocess forbidden')

def audit(event, args):
    if event in ('subprocess.Popen', 'socket.connect'):
        forbidden()
sys.addaudithook(audit)
socket.socket.connect = forbidden
socket.create_connection = forbidden
from biotop.kern import datenbank as D, messgeraet as M
from biotop.organe import aegis, eichung, kammer, vorspann as V
from biotop import lauf as L, anbieter
kammer.ausfuehren = forbidden
kammer._ausfuehren = forbidden
anbieter.aufrufen = forbidden
aegis.aufrufen = forbidden

def memory_db():
    db = sqlite3.connect(':memory:', isolation_level=None)
    db.row_factory = sqlite3.Row
    db.executescript(D.SCHEMA)
    db.execute('ALTER TABLE kandidaten ADD COLUMN vertraege TEXT')
    return db

def measurement():
    row = dict(tests_bestanden=2, tests_fehlgeschlagen=0, sicherheit_punkte=0,
               tote_funktionen=0, laufzeit_ms=100.0, groesste_funktion=3)
    m = dict(gueltig=True, kernmass=3, bereiche={b:deepcopy(row) for b in ['alpha','beta']},
             werk=dict(baut=True, zyklen=0, bauzeit_ms=100, tests_fehlgeschlagen_liste=[]))
    m['bereiche']['alpha']['tote_funktionen'] = 1
    return m

def noise_record(values):
    e = M.rauschtoleranz_aus_werten(values)
    e['gesperrt'] = bool(e.get('meldung'))
    return e

def blocked_scope_case(label, foreign_change, edges):
    with tempfile.TemporaryDirectory(dir=TMP, prefix='scope-') as tmp:
        work = Path(tmp) / 'werk'
        files = {
            'paket/__init__.py':'',
            'paket/alpha/__init__.py':'def nutzt():\n    return 1\n\ndef ungenutzt():\n    return 2\n',
            'paket/beta/__init__.py':'def wert():\n    return 1\n',
        }
        for name, code in files.items():
            p = work / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(code)
        changes = {'paket/alpha/__init__.py':'def nutzt():\n    return 1\n'}
        if foreign_change:
            changes['paket/beta/__init__.py'] = 'import time\ndef wert():\n    time.sleep(1)\n    return 1\n'
        diff = ''.join(''.join(unified_diff(files[p].splitlines(True), c.splitlines(True),
                                         fromfile='a/'+p,tofile='b/'+p)) for p,c in changes.items())
        db = memory_db()
        db.execute("INSERT INTO werke(id,name,pfad,bericht,status) VALUES(1,'unit',?,?,'kartiert')",
                   (str(work),D.j({'paket':'paket'})))
        db.execute("INSERT INTO laeufe(id,werk_id,budget_eur,status) VALUES(1,1,0,'laeuft')")
        db.execute("INSERT INTO generationen(lauf_id,nummer,status) VALUES(1,1,'laeuft')")
        base = measurement()
        cand = deepcopy(base)
        cand['bereiche']['alpha']['tote_funktionen'] = 0
        cand['bereiche']['beta']['laufzeit_ms'] = 10000.0
        n = {b:noise_record(v) for b,v in {'alpha':[100.0]*5,'beta':[100.,100.,120.,150.,150.]}.items()}
        rausch = {'toleranz':{'alpha':n['alpha']['toleranz']},'gesperrt':['beta'],
                  'bereiche':n,'lauf_startet':True}
        tausch = V._rauschwerte(rausch,['alpha','beta'])
        calls = []
        def measure(*args, **kw):
            code = kw.get('dateien') or {}
            result = cand if 'paket/alpha/__init__.py' in code else base
            calls.append({'dateien':deepcopy(code),'rueckgabe':deepcopy(result)})
            return deepcopy(result)
        original_check = aegis.pruefen
        def mechanical_check(*args, **kw):
            return original_check(*args, **kw, probe_ohne_modell=True)
        with ExitStack() as stack:
            stack.enter_context(patch.object(M,'messen',measure))
            stack.enter_context(patch.object(aegis,'pruefen',mechanical_check))
            stack.enter_context(patch.object(L.lazarus,'schnappschuss',lambda *a,**k:{'tag':'isolated-no-git','pruefsumme':'unit-not-a-hash'}))
            stack.enter_context(patch.object(L.entropie,'messen',lambda *a:{}))
            stack.enter_context(patch.object(L.entropie,'pruefen_und_beenden',lambda *a:None))
            r = L._generation_koerper(db,1,1,dict(db.execute('SELECT * FROM werke WHERE id=1').fetchone()),
                                      {'nischen':[]},'paket',['alpha','beta'],work,None,base,edges,base,tausch,
                                      einschleusen=[{'bereich':'alpha','diff':diff,'probe':'scope-review'}])
        row = dict(db.execute('SELECT id,status,grund,wirkungskreis,masse FROM kandidaten').fetchone())
        row['wirkungskreis'] = D.lj(row['wirkungskreis'])
        row['masse'] = D.lj(row['masse'])
        result = {'label':label, 'foreign_change':foreign_change, 'edges':edges,
                  'diff':diff, 'rauschen':rausch,'tausch':tausch,
                  'baseline':base, 'candidate_measurement_double':cand,
                  'measurement_calls':calls, 'generation':r, 'candidate_row':row,
                  'beta_before':files['paket/beta/__init__.py'],
                  'beta_after':(work/'paket/beta/__init__.py').read_text(),
                  'kasse_rows':db.execute('SELECT count(*) FROM kasse').fetchone()[0]}
        db.close()
        return result

def invalid_area(value):
    db=memory_db()
    calls=[]
    def measured(*a,**kw):
        calls.append({'alpha':value, 'beta':100.0})
        return calls[-1]
    r={'input_samples':[{'alpha':repr(value),'beta':100.0} for _ in range(5)]}
    with patch.object(eichung,'_messen_einmal',measured):
        try:
            r['result']=eichung.rauschmessung(db,1,1,Path('.'),['alpha','beta'],'paket','# unit')
        except Exception as e:
            r['exception']={'type':type(e).__name__,'message':str(e)}
    r['eichung_rows']=[dict(z) for z in db.execute('SELECT * FROM eichung')]
    r['eichkosten_rows']=[dict(z) for z in db.execute('SELECT * FROM eichkosten')]
    r['calls']=len(calls)
    db.close()
    return r

if __name__ == '__main__':
    raw = {
        'method':'Real calibration/decision/generation functions; explicit boundary doubles, synthetic in-memory DB and private fixture. No real timings/chambers/models/network.',
        'scope_cases':[
            blocked_scope_case('changed_blocked_beta_omitted_from_declared_scope',True,[]),
            blocked_scope_case('control_same_diff_beta_declared_dependent',True,[('beta','alpha')]),
            blocked_scope_case('control_unrelated_blocked_beta_not_changed',False,[]),
        ],
        'invalid_area_cases':{repr(v):invalid_area(v) for v in [0.0,float('nan'),True,None]},
    }
    (OUT/'repro-raw.json').write_text(json.dumps(raw,ensure_ascii=False,indent=2,allow_nan=False))
    print(json.dumps({'scope_cases':[{'label':r['label'],'status':r['generation']['status'],
                                    'candidate_scope':r['candidate_row']['wirkungskreis'],
                                    'beta_changed':r['beta_before']!=r['beta_after']} for r in raw['scope_cases']],
                      'invalid_area_cases':{k:{'exception':v.get('exception'),'result':v.get('result'),'calls':v['calls']} for k,v in raw['invalid_area_cases'].items()}},
                     ensure_ascii=False,indent=2))
    assert raw['scope_cases'][0]['generation']['status']=='vorgelegt', 'Observed issue no longer reproduces'
    assert raw['scope_cases'][0]['beta_after'] != raw['scope_cases'][0]['beta_before']
    assert raw['scope_cases'][1]['generation']['status']=='abgelehnt'
    assert raw['scope_cases'][2]['generation']['status']=='vorgelegt'
