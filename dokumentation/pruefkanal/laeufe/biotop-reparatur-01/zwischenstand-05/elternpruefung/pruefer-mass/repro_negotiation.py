"""Replay the real negotiation path, with measurements/model output explicitly doubled."""
from repro_mass import *
from biotop.organe import vertraege, landkarte

def run(blocked):
    with tempfile.TemporaryDirectory(dir=TMP,prefix='negotiation-') as tmp:
        work=Path(tmp)/'werk'
        files={
            'paket/__init__.py':'',
            'paket/alpha/__init__.py':'from paket.beta import wert\ndef nutzt():\n    return wert()\n\ndef ungenutzt():\n    return 2\n',
            'paket/beta/__init__.py':'def wert():\n    return 1\n',
            'paket/gamma/__init__.py':'from paket.beta import wert\ndef nutzt():\n    return wert()\n',
        }
        for p,c in files.items():
            dest=work/p
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_text(c)
        new_alpha='from paket.beta import wert_neu\ndef nutzt():\n    return wert_neu()\n'
        new_beta='import time\ndef wert():\n    time.sleep(1)\n    return 1\n\ndef wert_neu():\n    return 1\n'
        def diff(p,c):
            return ''.join(unified_diff(files[p].splitlines(True),c.splitlines(True),fromfile='a/'+p,tofile='b/'+p))
        alpha_diff=diff('paket/alpha/__init__.py',new_alpha)
        beta_diff=diff('paket/beta/__init__.py',new_beta)
        db=memory_db()
        db.execute("INSERT INTO werke(id,name,pfad,bericht,status) VALUES(1,'unit',?,?,'kartiert')",(str(work),D.j({'paket':'paket'})))
        db.execute("INSERT INTO laeufe(id,werk_id,budget_eur,status) VALUES(1,1,0,'laeuft')")
        db.execute("INSERT INTO generationen(lauf_id,nummer,status) VALUES(1,1,'laeuft')")
        contract=vertraege.einlegen(db,1,work,{('alpha','beta'):'from paket.alpha import nutzt\ndef test_v():\n    assert nutzt()==1\n'},'isolated reviewer fixture')[0]
        areas=['alpha','beta','gamma']
        edges=[('alpha','beta'),('gamma','beta')]
        base=measurement()
        base['bereiche']['gamma']=deepcopy(base['bereiche']['beta'])
        broken=deepcopy(base)
        broken['bereiche']['alpha']['tote_funktionen']=0
        broken['bereiche']['beta']['tests_fehlgeschlagen']=1
        broken['werk']['tests_fehlgeschlagen_liste']=[Path(contract).name+'::test_v']
        paired=deepcopy(base)
        paired['bereiche']['alpha']['tote_funktionen']=0
        paired['bereiche']['gamma']['laufzeit_ms']=10000.0
        tausch={'_gesperrte_bereiche':blocked,'_rauschtoleranz':{b:1.15 for b in areas if b not in blocked}}
        calls=[]
        def measure(*a,**kw):
            code=kw.get('dateien') or {}
            m=paired if 'paket/beta/__init__.py' in code else broken if 'paket/alpha/__init__.py' in code else base
            calls.append({'dateien':deepcopy(code),'result':deepcopy(m)})
            return deepcopy(m)
        generated=[]
        def generate(con,lauf_id,werk_id,generation,pfad,paket,bereich,*a,**kw):
            assert bereich=='beta'
            cur=con.execute("INSERT INTO kandidaten(lauf_id,generation,bereich,nische,modell,diff,begruendung,status,grund,vertraege) VALUES(1,1,'beta','sicher','unit/no-paid-model',?,'unit adaptation','erzeugt','',?)",(beta_diff,contract))
            generated.append({'id':cur.lastrowid,'bereich':bereich,'diff':beta_diff})
            return [cur.lastrowid]
        with ExitStack() as stack:
            stack.enter_context(patch.object(M,'messen',measure))
            stack.enter_context(patch.object(aegis,'_angriff',lambda *a,**k:(None,'unit abstention',None)))
            stack.enter_context(patch.object(L.genesis,'erzeugen',generate))
            stack.enter_context(patch.object(L.lazarus,'schnappschuss',lambda *a,**k:{'tag':'unit-no-git','pruefsumme':'unit-not-a-hash'}))
            stack.enter_context(patch.object(L.entropie,'messen',lambda *a:{}))
            stack.enter_context(patch.object(L.entropie,'pruefen_und_beenden',lambda *a:None))
            r=L._generation_koerper(db,1,1,dict(db.execute('SELECT * FROM werke WHERE id=1').fetchone()),
                                     {'nischen':[]},'paket',areas,work,None,base,edges,base,tausch,
                                     einschleusen=[{'bereich':'alpha','diff':alpha_diff,'vertraege':contract,'probe':'own-area-only'}])
        rows=[dict(z) for z in db.execute('SELECT id,bereich,status,grund,wirkungskreis,masse FROM kandidaten')]
        for z in rows:
            z['wirkungskreis']=D.lj(z['wirkungskreis'])
            z['masse']=D.lj(z['masse'])
        result={'blocked':blocked,'bstrassen':edges,'input_candidate_area':'alpha','input_diff':alpha_diff,
                'generated_adaptations':generated,'actual_adaptation_scope':landkarte.wirkungskreis('beta',edges),
                'generation':r,'candidates':rows,'measurement_calls':calls,
                'beta_before':files['paket/beta/__init__.py'],'beta_after':(work/'paket/beta/__init__.py').read_text(),
                'protocol':[{'nr':z['nr'],'art':z['art'],'inhalt':D.lj(z['inhalt'])} for z in db.execute('SELECT * FROM protokoll')],
                'kasse_rows':db.execute('SELECT count(*) FROM kasse').fetchone()[0]}
        db.close()
        return result

if __name__ == '__main__':
    raw={'method':'Original _generation_koerper -> _verhandeln -> aegis.pruefen -> urteil_f2. Own-area-only diffs. Network/chamber prohibited; model and measurement seams explicitly doubled.',
         'cases':[run(['gamma']),run(['beta','gamma'])]}
    (OUT/'negotiation-raw.json').write_text(json.dumps(raw,ensure_ascii=False,indent=2))
    print(json.dumps([{'blocked':c['blocked'],'status':c['generation']['status'],
                      'stored_scope':c['candidates'][0]['wirkungskreis'],
                      'actual_adaptation_scope':c['actual_adaptation_scope'],
                      'beta_changed':c['beta_before']!=c['beta_after']} for c in raw['cases']],ensure_ascii=False,indent=2))
    assert raw['cases'][0]['generation']['status']=='vorgelegt'
    assert raw['cases'][0]['beta_before']!=raw['cases'][0]['beta_after']
    assert raw['cases'][1]['generation']['status']=='abgelehnt'
