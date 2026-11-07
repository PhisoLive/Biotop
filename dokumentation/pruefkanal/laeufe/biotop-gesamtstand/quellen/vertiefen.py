"""Lesende Vertiefung; Ausgaben nur im Gesamtstandsordner, Docker ohne Netz."""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import json, collections, subprocess, re, datetime, ast
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand')
R=Path('/root/biotop'); A=O/'ausgaben'
def save(n,x): (A/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def run(args):
    p=subprocess.run(args,capture_output=True,text=True,timeout=180)
    return {'befehl':args,'rc':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
def eur(rows): return sum((Decimal(str(r['kosten_eur'])) for r in rows),Decimal(0))
K=json.loads((A/'06-kassenbuchungen.json').read_text())
counts={1:27,2:100,3:1,4:62,5:46,6:178,7:88,8:136,9:108,10:32,11:6,12:480,13:704,14:17,15:28,16:263,17:310,18:154,19:220,20:233,21:0,22:189,23:18}
phases=[('Phase 1',1,5,'0.4031','0.40'),('Nachlauf Phase 1',6,10,'1.7903','1.79'),('Phase 2',11,13,'1.9050','1.91'),('Phase 3',14,20,'2.8269','2.83'),('Nachlauf Phase 3',21,23,'0.4367','0.44')]
old=[]; extra=[]; rows=[]
for n in range(1,24):
    allrows=[k for k in K if k['lauf_id']==n]; early=allrows[:counts[n]]; late=allrows[counts[n]:]
    old+=early;extra+=late
    rows.append({'lauf':n,'historisch_aufrufe':len(early),'historisch_eur':str(eur(early)),'historisch_ids':[x['id'] for x in early], 'heute_aufrufe':len(allrows),'heute_eur':str(eur(allrows)), 'spaeter_aufrufe':len(late),'spaeter_eur':str(eur(late)),'spaeter_ids':[x['id'] for x in late]})
ps=[]
for label,a,b,bericht,gerundet in phases:
    oh=[r for r in old if a<=r['lauf_id']<=b]; nh=[r for r in K if a<=r['lauf_id']<=b]
    ps.append({'abschnitt':label,'laeufe':[a,b],'historisch_aufrufe':len(oh),'historisch_roh_eur':str(eur(oh)), 'bericht_eur':bericht,'zweistellig_eur':gerundet, 'passt_auf_vier_stellen':eur(oh).quantize(Decimal('0.0001'),rounding=ROUND_HALF_UP)==Decimal(bericht), 'heute_aufrufe':len(nh),'heute_eur':str(eur(nh)), 'spaeter_eur':str(eur(nh)-eur(oh))})
# Phase 2 besitzt Einzel-IDs, diese gegen die Rekonstruktion prüfen.
p2=(O.parent/'biotop-phase-2/KASSE.md').read_text()
p2ids=[int(m[1]) for m in re.finditer(r'^\| (\d+) \| (?:11|12|13) \| 2026-',p2,re.M)]
sel=[r for r in K if r['lauf_id']<=23]
data={'methode':'Historischer Berichtsschnitt: pro Lauf die im damaligen Kassenblatt genannte Anzahl frühester Buchungen nach ID. Bei Phase 2 zusätzlich vollständige Original-ID-Liste abgeglichen. Für Phase 3 und Nachlauf mangels Original-Einzelbuchungen Rekonstruktion, nicht exakte historische DB-Kopie. Preise werden NICHT neu erfunden, gespeichert kosten_eur wird mit Decimal addiert.', 'phase2_ids_abgleich':p2ids==[r['id'] for r in old if 11<=r['lauf_id']<=13], 'phase2_ids_anzahl':len(p2ids), 'laeufe':rows,'abschnitte':ps,'historisch_roh_eur':str(eur(old)), 'heute_1bis23_eur':str(eur(sel)),'spaeter_eur':str(eur(extra)), 'historisch_aufrufe':len(old),'heute_aufrufe':len(sel),'spaeter_aufrufe':len(extra),'nutzer_rechnung_eur':'7.37','differenz_heute_zu_7_37':str(eur(sel)-Decimal('7.37')), 'differenz_historisch_zu_7_37':str(eur(old)-Decimal('7.37')),'summe_fuenf_gerundete_abschnitte':str(sum((Decimal(p['zweistellig_eur']) for p in ps),Decimal(0)))}
save('12-kassenabgleich.json',data);save('13-spaetere-buchungen.json',extra)
# Dateipopulation vollständig ohne Abhängigkeiten: disjunkte Kategorien.
state=json.loads((A/'01-zustand-vorher.json').read_text()); tracked=json.loads((A/'03-dateien.json').read_text()); tracked_paths={x['pfad'] for x in tracked};groups=collections.defaultdict(lambda:{'dateien':0,'bytes':0})
for f,v in state['dateien'].items():
    p=Path(f)
    if f in tracked_paths: cat='Git-verfolgter Eigenbau'
    elif '.git' in p.parts: cat='Git-Interna (einschließlich Werk-Git)'
    elif '__pycache__' in p.parts or '.pytest_cache' in p.parts: cat='Python-/Pytest-Caches'
    elif f.startswith('daten/lazarus/'): cat='Lazarus-Archive'
    elif f.startswith('daten/werke/'): cat='Werkdateien (ohne Git/Caches)'
    elif f.startswith('daten/biotop.db'): cat='Biotop-Datenbank mit WAL/SHM'
    else: cat='Sonstige'
    groups[cat]['dateien']+=1;groups[cat]['bytes']+=v['bytes']
save('14-dateisystem-zerlegung.json',{'zeit':state['zeit'],'gruppen':dict(groups),'gesamt_dateien':sum(x['dateien'] for x in groups.values()),'gesamt_bytes':sum(x['bytes'] for x in groups.values()),'lesefehler':state['fehler'],'python':{'dateien':sum(x['pfad'].endswith('.py') for x in tracked),'physische_zeilen':sum(x['zeilen'] for x in tracked if x['pfad'].endswith('.py')),'codezeilen':sum(x.get('python_codezeilen',0) for x in tracked),'dokumentationszeilen':sum(x.get('python_dokumentationszeilen',0) for x in tracked)}})
# Namen von CLI-Befehlen/Symbolen und referenzierter Skripte statisch erheben.
refs=[]
for x in tracked:
    f=x['pfad']; txt=(R/f).read_text()
    for y in tracked:
        if y['gruppe']=='pruefung' and y['pfad']!=f and Path(y['pfad']).name in txt:
            refs.append({'quelle':f,'ziel':y['pfad']})
save('15-pruefskript-referenzen.json',refs)
cmd=['docker','run','--rm','--network','none','--read-only','--memory','128m','--cpus','1','--pids-limit','64','--cap-drop','ALL','--security-opt','no-new-privileges','--tmpfs','/tmp:rw,nosuid,size=32m','-e','PYTHONDONTWRITEBYTECODE=1','-e','PYTHONPATH=/root/biotop','-v',str(R/'biotop')+':/root/biotop/biotop:ro','-v',str(R/'pruefung')+':/root/biotop/pruefung:ro','-w','/tmp','biotop-kammer:1','python']
save('16-eigene-tests-sammlung.json',run(cmd+['-m','pytest','--collect-only','-q','-p','no:cacheprovider','/root/biotop/biotop','/root/biotop/pruefung']))
save('17-rauschbeispiele-ausfuehrung.json',run(cmd+['/root/biotop/pruefung/rauschregeln_pruefen.py']))
save('18-historischer-codevergleich.json',run(['git','-C',str(R),'diff','--stat','7c73d403c18755dda26655c78ac7290c446d9f45','HEAD']))
print(json.dumps({'abgleich':{k:v for k,v in data.items() if k not in ('laeufe',)},'dateisystem':dict(groups),'testsammlung':json.loads((A/'16-eigene-tests-sammlung.json').read_text()),'rauschbeispiele':json.loads((A/'17-rauschbeispiele-ausfuehrung.json').read_text())},ensure_ascii=False,indent=2))
