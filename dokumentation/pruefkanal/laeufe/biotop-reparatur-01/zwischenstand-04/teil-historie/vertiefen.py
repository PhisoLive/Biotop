#!/usr/bin/env python3
"""Lesende Nachrechnung vorhandener Datensätze; keine neuen Tests/Proben.
AST-Isolation führt nur gelesene reine Ableitungen aus, nie Biotop-Module.
"""
import ast
import collections
import datetime
import hashlib
import json
import pathlib
import sqlite3
import subprocess
from decimal import Decimal

O = pathlib.Path(__file__).resolve().parent
R = pathlib.Path('/root/biotop')
HEAD = 'b42dc941e7fcb66632ba6a0e13b8df106a270a31'
AKTE = pathlib.Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe')
def load(f): return json.loads((O/f).read_text())
def save(f,d): (O/f).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def git(*args): return subprocess.run(['git','--no-optional-locks','-C',str(R),*args],check=True,capture_output=True,text=True).stdout
def total(rs): return str(sum((Decimal(str(r['kosten_eur'])) for r in rs),Decimal('0')))
e=load('protokoll_sicher.json')
byid={r['nr']:r for r in e}
runs=load('laeufe.json'); candidates=load('kandidaten.json'); generations=load('generationen.json'); kasse=load('kasse.json')

# Genau die aktuellen verbindlichen Nutzerentscheidungen; keine anderen Chats exportieren.
s=sqlite3.connect('file:/root/.hermes/state.db?mode=ro',uri=True); s.row_factory=sqlite3.Row
msg=dict(s.execute("SELECT id,session_id,role,timestamp,content FROM messages WHERE id=4317 AND role='user'").fetchone())
msg['zeit_utc']=datetime.datetime.fromtimestamp(msg['timestamp'],datetime.UTC).isoformat()
alt=dict(s.execute("SELECT id,session_id,role,timestamp FROM messages WHERE id=3102 AND role='user'").fetchone())
alt['zeit_utc']=datetime.datetime.fromtimestamp(alt['timestamp'],datetime.UTC).isoformat()
alt['dokument']='/root/.hermes/cache/documents/doc_f18e4c5d9f14_ABNAHME_Vorbedingung-1_2026-09-20.md'
save('nutzerentscheidungen.json',{'verbindliche_juengste_entscheidung':msg,'fruehere_enge_abnahme':alt})

# Direkte Prüfung des ursprünglichen Schlüssels, nicht selbst erfundene Ersatzableitung.
source=git('show',HEAD+':biotop/organe/aegis.py')
node=next(n for n in ast.parse(source).body if isinstance(n,ast.FunctionDef) and n.name=='behauptung')
original=ast.get_source_segment(source,node)
globals_={'ast':ast}
exec(compile(ast.Module(body=[node],type_ignores=[]),'<gelesene Originalfunktion aegis.behauptung>','exec'),globals_)
keyfunc=globals_['behauptung']
c=sqlite3.connect('file:/root/reparatur-01/ausgang.db?mode=ro',uri=True); c.row_factory=sqlite3.Row
c.execute('PRAGMA query_only=ON')
immun=[dict(r) for r in c.execute('SELECT * FROM immunsystem WHERE werk_id IN (21,22) ORDER BY id')]
for r in immun:
    names=[n.name for n in ast.walk(ast.parse(r['code'])) if isinstance(n,ast.FunctionDef) and n.name.startswith('test_')]
    r['testschluessel_originalfunktion']={n:keyfunc(r['code'],n,'lagerhaus') for n in names}
    r['code_sha256']=hashlib.sha256(r.pop('code').encode()).hexdigest()
    r['quellfunktion']=f'{HEAD}:biotop/organe/aegis.py:230-278'
for r in immun:
    if r['werk_id']==21 and r['generation']>0:
        r['gegenstuecke_uebernahme']={key:[{'id':q['id'],'name':q['name'],'status':q['status'],'erstellt_am':q['erstellt_am'],'ursprung':q['ursprung']} for q in immun if q['werk_id']==21 and q['generation']==0 and q['bereich']==r['bereich'] and key in (q['ursprung'].split('behauptung=',1)[1].split() if 'behauptung=' in q['ursprung'] else [])] for key in r['testschluessel_originalfunktion'].values()}
save('immun-schluessel.json',immun)

# Historische Dateistände, nicht als laufbezogene Messgeräteversiegelung ausgeben.
versions=[]
refs=['7c73d403c18755dda26655c78ac7290c446d9f45','7bc112beac11110e22047ccaeaf7c4981efdaafe','293b1c16c53ca76fb737587b1c09b04bd21fcdba','19498ad5808c5b63c534a8bac844a6824fe306a2','71fb51cce7666eb74591ec3e64f69e5bd8ba54ce',HEAD]
files=['biotop/organe/aegis.py','biotop/organe/gedaechtnis.py','biotop/kern/messgeraet.py','biotop/organe/eichproben.py','biotop/lauf.py']
for ref in refs:
    blobs={f:git('show',ref+':'+f) for f in files}
    versions.append({'commit':ref,'git_metadaten':git('show','-s','--format=%H %aI %cI %s',ref).strip(),'sha256':{f:hashlib.sha256(v.encode()).hexdigest() for f,v in blobs.items()},'bauteile':{'A': 'def _ansage(' in blobs[files[0]],'B':'fremd_min' in blobs[files[1]],'C':'def aufnahmesperre(' in blobs[files[0]],'C_aufrufzaehler':'"immun.aufnahme_geprueft"' in blobs[files[0]]}})
save('quellstaende.json',{'versions':versions,'diff_produktiv_lauf24_vorbereitung_bis_bericht':git('diff','--stat',refs[2],'d4aa7a1108591a45836e89d3c2f821998e56ef22','--','biotop'),'diff_produktiv_lauf25_vorbereitung_bis_HEAD':git('diff','--stat',refs[4],HEAD,'--','biotop'),'grenze':'Git-Blobs und Berichtschronologie, kein technischer Hash im Lauf-Freeze; keine Ausführungszeit aus Commitzeit abgeleitet.'})

# Derselbe reine Werkhash wie im Original-Lazarus (keine Rueckkehr / kein schnappschuss).
laz=git('show',HEAD+':biotop/organe/lazarus.py')
ln=next(n for n in ast.parse(laz).body if isinstance(n,ast.FunctionDef) and n.name=='pruefsumme_werk')
exclude=ast.literal_eval(next(n.value for n in ast.parse(laz).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUSSCHLUSS' for t in n.targets)))
lg={'Path':pathlib.Path,'hashlib':hashlib,'AUSSCHLUSS':exclude}
exec(compile(ast.Module(body=[ln],type_ignores=[]),'<gelesene Originalfunktion lazarus.pruefsumme_werk>','exec'),lg)
works=[]
for w in load('werke.json'):
    if w['id'] not in (21,22): continue
    p=pathlib.Path(w['pfad'])
    h,n=lg['pruefsumme_werk'](p)
    works.append({'werk_id':w['id'],'pfad':str(p),'sha256_originaldefinition':h,'dateien':n,'git_head':subprocess.run(['git','--no-optional-locks','-C',str(p),'rev-parse','HEAD'],check=True,capture_output=True,text=True).stdout.strip(),'git_status':subprocess.run(['git','--no-optional-locks','-C',str(p),'status','--porcelain=v1'],check=True,capture_output=True,text=True).stdout,'passende_schnappschuesse':[q['tag'] for q in load('lazarus.json') if q['pruefsumme']==h]})
save('werkstaende.json',works)

results={}
for run in runs:
    lid=run['id']; begin=run['begonnen_am']
    re=[r for r in e if r['inhalt'].get('lauf_id')==lid and r['zeit']>=begin]
    before=[r for r in e if r['inhalt'].get('lauf_id')==lid and r['zeit']<begin]
    a=[r for r in re if r['art']=='aegis.ansage']
    ar=[r for r in a if r['inhalt'].get('behauptung') and not r['inhalt'].get('ausgefuehrt')]
    an=[r for r in a if not r['inhalt'].get('behauptung')]
    ka=[r for r in kasse if r['lauf_id']==lid]
    marked_probe_ids={r['id'] for r in candidates if r['lauf_id']==lid and r['ist_probe']}
    def is_fixture(r):
        return r['inhalt'].get('kandidat') in marked_probe_ids or (lid==25 and r['nr']>=16010)
    natural=[r for r in re if not is_fixture(r)]
    fixture=[r for r in re if is_fixture(r)]
    immune=[r for r in immun if r['lauf_id']==lid]
    ue=[r for r in natural if r['art']=='aegis.urteil' and r['inhalt'].get('angriff')]
    cc=[r for r in candidates if r['lauf_id']==lid]
    by_purpose=[]
    for purpose in sorted(set(r['zweck'] for r in ka)):
        rr=[r for r in ka if r['zweck']==purpose]
        by_purpose.append({'zweck':purpose,'anzahl':len(rr),'summe_eur':total(rr),'kassen_ids':[r['id'] for r in rr]})
    results[str(lid)]={
      'db_status':run['status'],'begonnen_am':begin,'beendet_am':run['beendet_am'],
      'vor_dieser_laufanlage_wiederverwendete_ids':before,
      'ansagen':{'gesamt':len(a),'ausgefuehrt':sum(bool(r['inhalt'].get('ausgefuehrt')) for r in a),'gesperrt':len(ar),'ohne_behauptung':len(an),'ids_gesperrt':[r['nr'] for r in ar],'ids_ohne_behauptung':[r['nr'] for r in an]},
      'kandidaten':{'gesamt':len(cc),'ist_probe':[r['id'] for r in cc if r['ist_probe']],'je_generation':dict(collections.Counter(r['generation'] for r in cc)), 'je_status':dict(collections.Counter(r['status'] for r in cc))},
      'natuerliche_urteile_mit_angriff':[{'nr':r['nr'],'zeit':r['zeit'],'kandidat':r['inhalt'].get('kandidat'),'angriff':r['inhalt']['angriff'],'immun':r['inhalt'].get('immun'),'norm':r['inhalt'].get('norm')} for r in ue],
      'natuerliche_C_pruefungen':[r for r in natural if r['art']=='immun.aufnahme_geprueft'],
      'gestellte_C_pruefungen':[r for r in fixture if r['art']=='immun.aufnahme_geprueft'],
      'gestellte_C_sperrungen':[r for r in fixture if r['art']=='immun.aufnahme_gesperrt'],
      'eichproben_in_lebenszeit':[r for r in re if r['art'].startswith(('eichprobe.','eichung.'))],
      'immunsystem':{'bestand':len(immune),'status':dict(collections.Counter(r['status'] for r in immune)),'neu_gen_gt_0':[r['id'] for r in immune if r['generation']>0]},
      'kasse':{'anzahl':len(ka),'summe_eur':total(ka),'budget_eur':str(run['budget_eur']),'budget_prozent':str(Decimal(total(ka))/Decimal(str(run['budget_eur']))*100),'zwecke':by_purpose},
      'modell_versuche': {'aufrufe':[r['nr'] for r in re if r['art']=='modell.aufruf'],'antworten':[r['nr'] for r in re if r['art']=='modell.antwort'],'fehler':[r for r in re if r['art']=='modell.fehler']}
    }
save('nachrechnung.json',results)
# Kassenmengen exakt per ID, abschnittsuebergreifende Entscheidungen nicht neu treffen.
sections={
  'lauf24_25':[r for r in kasse if r['lauf_id'] in (24,25)],
  'lauf22_25_vollstaendig':kasse,
  'lauf22_erster_block':[r for r in kasse if r['lauf_id']==22 and r['id']<=3411],
  'lauf22_spaeterer_block':[r for r in kasse if r['lauf_id']==22 and r['id']>=3651],
  'nur_fortsetzung22_und23_25':[r for r in kasse if r['lauf_id']!=22 or r['id']>=3651],
}
save('kosten-abgrenzung.json',{k:{'anzahl':len(v),'eur':total(v),'ids':[r['id'] for r in v]} for k,v in sections.items()})
# Ereignisse, die die Zeit- und Pfadbehauptungen tragen; Originalpayloads ohne Konten.
ids={12418,12440,12465,12517,12538,12544,13232,13398,13442,13773,14066,14086,14160,14246,14248,14305,14435,14475,14476,14477,14480,14533,14557,14677,14678,14772,14775,14776,15002,15003,15004,15005,15006,15027,15030,15143,15146,15147,15225,15227,15230,15231,15271,15272,15273,15276,15661,15662,16008,16009}|set(range(16010,16031))
save('ereignisse-belegauswahl.json',[r for r in e if r['nr'] in ids])
print(json.dumps({'werkstaende':works,'kosten':{k:{'anzahl':len(v),'eur':total(v)} for k,v in sections.items()},'neue_immun24':[{k:v for k,v in r.items() if k!='ursprung'} for r in immun if r['werk_id']==21 and r['generation']>0],'proben_kandidaten_24_25':{l:results[l]['kandidaten'] for l in ('24','25')},'angriff_urteile_25':results['25']['natuerliche_urteile_mit_angriff']},ensure_ascii=False,indent=2))
