"""Fehlgeschlagene aktuelle Integration aus vollständigen Rohbelegen bilanzieren, nicht reparieren."""
from pathlib import Path
from collections import Counter
import json,ast,xml.etree.ElementTree as E
R=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben');P=Path('/root/reparatur-01')
def lade(f):return json.loads((R/f).read_text())
suite=lade('62-gesamtsuite-zweite-runde.json');b=lade('62-gesamtsuite-zweite-runde-eichpaare.json');faelle=list(E.parse(R/'62-gesamtsuite-zweite-runde.xml').getroot().iter('testcase'))
rows=[]
for gruppe,soll in [('proben',True),('gegenproben',False)]:
    for art,z in b[gruppe].items():
        kam=[]
        for k in z['kammer']:
            if k['rc']==0:continue
            txt=k['stderr'];marker='ValueError: pytest-Nachweis unvollständig/abgebrochen: '
            nd=None
            if marker in txt:
                d=ast.literal_eval(txt.split(marker,1)[1].strip())
                nd={'zahlen':{x:len(v) for x,v in d.items()},'gesammelt_ohne_call':sorted(set(d['gesammelt'])-set(d['aufrufe'])),'call_ohne_gesammelt':sorted(set(d['aufrufe'])-set(d['gesammelt'])),'gesammelt_ohne_teardown':sorted(set(d['gesammelt'])-set(d['beendet'])),'sammlungsfehler':d['sammlungsfehler'],'abgewaehlt':d['abgewaehlt'],'gleiche_callmultimenge':Counter(d['gesammelt'])==Counter(d['aufrufe']),'gleiche_teardownmultimenge':Counter(d['gesammelt'])==Counter(d['beendet'])}
            kam.append({'container':k['container'],'rc':k['rc'],'zeitlimit':k['zeitlimit'],'stderr_anfang':txt[:500],'vollstaendigkeitsdaten':nd})
        rows.append({'gruppe':gruppe,'probe':art,'ausgefuehrt':z['ausgefuehrt'],'pruefbar':z['pruefbar'],'praedikat':z['bestanden'],'sollpraedikat':soll,'gueltiger_erwarteter_fall':z['ausgefuehrt'] is True and z['pruefbar'] is True and z['bestanden'] is soll,'grund':z['grund'],'kammern':z['kammerlaeufe'],'fehlerkammern':kam})
r={'suite_rc':suite['rc'],'tests':len(faelle),'fehlgeschlagen':[{'fall':t.get('classname')+'::'+t.get('name'),'fehler':t.find('failure').text} for t in faelle if t.find('failure') is not None],'fehler':sum(t.find('error') is not None for t in faelle),'skips':sum(t.find('skipped') is not None for t in faelle),'bestanden':sum(all(t.find(x) is None for x in ['failure','error','skipped']) for t in faelle),'kammern':suite['kammerlaeufe'],'batterie_bestanden':b['bestanden'],'eichfaelle':rows,'gueltige_positive':sum(z['gueltiger_erwarteter_fall'] for z in rows if z['gruppe']=='proben'),'gueltige_gegenproben':sum(z['gueltiger_erwarteter_fall'] for z in rows if z['gruppe']=='gegenproben'),'probe_gesamt':len(b['proben']),'gegenprobe_gesamt':len(b['gegenproben']),'grenze':'Keine erneute Produktänderung; zweite Runde hat die aktuelle Bestandsabnahme nicht bestanden. Ursache aus Rohdaten noch nicht vollständig zugeordnet; kein Schluss aus bloßem rc1.'}
assert r['tests']==r['bestanden']+len(r['fehlgeschlagen'])+r['fehler']+r['skips']
(P/'RUNDE2-INTEGRATIONSFEHLER.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False,indent=2))
