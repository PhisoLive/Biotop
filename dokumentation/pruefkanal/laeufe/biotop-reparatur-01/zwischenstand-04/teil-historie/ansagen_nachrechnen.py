#!/usr/bin/env python3
"""Bestehende Ansageentscheidungen zeitlich nachrechnen, keine Proben erzeugen."""
import ast,json,pathlib,sqlite3,subprocess
O=pathlib.Path(__file__).resolve().parent
head='b42dc941e7fcb66632ba6a0e13b8df106a270a31'
src=subprocess.run(['git','--no-optional-locks','-C','/root/biotop','show',head+':biotop/organe/aegis.py'],capture_output=True,text=True,check=True).stdout
node=next(n for n in ast.parse(src).body if isinstance(n,ast.FunctionDef) and n.name=='bisherige_behauptungen')
g={'lj':lambda s:json.loads(s) if s else None}
exec(compile(ast.Module(body=[node],type_ignores=[]),'<Originalfunktion bisherige_behauptungen>','exec'),g)
c=sqlite3.connect('file:/root/reparatur-01/ausgang.db?mode=ro',uri=True);c.row_factory=sqlite3.Row
c.execute('PRAGMA query_only=ON')
class Stichtag:
    def __init__(self,nr,zeit): self.nr,self.zeit=nr,zeit
    def execute(self,sql,params=()):
        if sql.startswith('SELECT ursprung FROM immunsystem WHERE werk_id=? AND bereich=?'):
            return c.execute(sql.replace(' ORDER BY',' AND erstellt_am<? ORDER BY'),(*params,self.zeit))
        if sql=="SELECT inhalt FROM protokoll WHERE art='aegis.ansage' ORDER BY nr DESC LIMIT 400":
            return c.execute(sql.replace(' ORDER BY',' AND nr<? ORDER BY'),(self.nr,))
        raise RuntimeError('Nicht vorgesehene Abfrage')
results=[]
for r in c.execute("SELECT nr,zeit,inhalt FROM protokoll WHERE art='aegis.ansage' AND json_extract(inhalt,'$.lauf_id') IN (24,25) ORDER BY nr"):
    d=json.loads(r['inhalt']); w={24:21,25:22}[d['lauf_id']]
    v=g['bisherige_behauptungen'](Stichtag(r['nr'],r['zeit']),w,d['bereich'],d['lauf_id'])
    results.append({'nr':r['nr'],'zeit':r['zeit'],**d,'rekonstruiert_vorrat':v,'rekonstruiert_bekannt':bool(d.get('behauptung') and d['behauptung'] in v),'rekonstruiert_vorratszahl_passt':d.get('bisherige') is None or len(v)==d['bisherige']})
out={'methode':'Originalfunktion am fixierten HEAD, nur SELECT-Population auf zeitlich fruehere Datensaetze begrenzt. Immu-Urspruenge aus Endbestand; nachtraeglich geloeschte oder inhaltlich ueberschriebene Datensaetze nicht rekonstruierbar. Keine Aussage ueber ausbleibende Angriffe oder semantische Richtigkeit eines Behauptungsschluessels.','pro_lauf':{},'entscheidungen':results}
for l in (24,25):
    rr=[r for r in results if r['lauf_id']==l];blocked=[r for r in rr if r.get('behauptung') and not r['ausgefuehrt']]
    out['pro_lauf'][l]={'gesamt':len(rr),'sperrungen':len(blocked),'sperrungen_ohne_rekonstruiertes_gegenstueck':[r['nr'] for r in blocked if not r['rekonstruiert_bekannt']],'ausgefuehrt_trotz_rekonstruiertem_gegenstueck':[r['nr'] for r in rr if r['ausgefuehrt'] and r['rekonstruiert_bekannt']],'abweichende_vorratszahlen':[r['nr'] for r in rr if not r['rekonstruiert_vorratszahl_passt']]}
(O/'A-rekonstruktion.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out['pro_lauf'],ensure_ascii=False,indent=2))
