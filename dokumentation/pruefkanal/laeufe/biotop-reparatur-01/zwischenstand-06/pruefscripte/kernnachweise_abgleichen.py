"""Kernnachweise aus realer Suite/CLI prüfen und Zahlen abstimmen."""
from pathlib import Path
import json,hashlib,sys,xml.etree.ElementTree as ET
sys.dont_write_bytecode=True;sys.path.insert(0,'/root/biotop')
from biotop.organe import eichproben
R=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01')
O=R/'ausgaben';ziel=O/'51-kernabnahme-abgleich.json';assert not ziel.exists()
def lade(n):return json.loads((O/n).read_text())
suite=lade('48-gesamtsuite-kernabschluss.json');gate=lade('49-vorspann-kernabschluss.json');sperre=lade('50-vorspann-cli-sperre.json')
assert suite['rc']==gate['rc']==0 and gate['gen0_nachweis_verwendbar'] and all(gate['schutz'].values())
raw=json.loads(gate['nachweis']['ergebnis']);paare=raw['eichproben'];namen=set(eichproben.PROBEN)
assert set(paare['proben'])==set(paare['gegenproben'])==namen
assert paare['bestanden'] is True
zeilen=[]
for name in eichproben.PROBEN:
 for gruppe,soll in [('proben',True),('gegenproben',False)]:
  e=paare[gruppe][name];assert e['ausgefuehrt'] is True and e['pruefbar'] is True and e['bestanden'] is soll
  assert eichproben._bestanden(name,e['belege']) is soll
  assert e['kammerlaeufe']==len(e['kammer']) and e['modellaufrufe']==0 and e['kosten_eur']==0
  row={'probe':name,'gruppe':gruppe,'ausgefuehrt':e['ausgefuehrt'],'pruefbar':e['pruefbar'],'praedikat':e['bestanden'],'grund':e['grund'],'kammerlaeufe':e['kammerlaeufe']}
  b=e['belege']
  if name=='vertrag':
   z=f"{Path(b['vertragspfad']).parent.as_posix()}/{b['vertragstest']}";w=b['kandidat_tests'][z]
   assert eichproben._vertrag_pruefbar(b,gegenprobe=not soll)
   assert w['ok'] is (not soll)
   row.update(benannter_vertrag=z,vertragszeuge=w,verbraucher=b['verbrauchertest'],verbraucherzeuge=b['kandidat_tests'][b['verbrauchertest']])
  if name=='norm':
   assert b['urteil']['mass']['zuwachs']==0
   row.update(norm=b['urteil']['norm'],zuwachs=b['urteil']['mass']['zuwachs'],test_aufgenommen=b['werk_test_vorhanden'])
  zeilen.append(row)
cases=ET.parse(O/'48-gesamtsuite-kernabschluss.xml').getroot().findall('.//testcase')
assert len(cases)==sum(int(s['tests']) for s in suite['testsuites'])
assert not any(c.find('failure') is not None or c.find('error') is not None or c.find('skipped') is not None for c in cases)
prior=[i for i,c in enumerate(cases) if c.get('classname','').endswith('test_kernmass_pareto')];andere=[i for i,c in enumerate(cases) if not c.get('classname','').endswith('test_kernmass_pareto')]
assert prior and max(prior)<min(andere)
kammern=lade('49-vorspann-kernabschluss-kammer.json');teile={x['teil']:x['kammerlaeufe'] for x in gate['eichkosten']}
assert len(kammern)==gate['kammerlaeufe']==sum(teile.values())
assert sum(e['kammerlaeufe'] for e in zeilen)==paare['kosten']['kammerlaeufe']
assert all(e['rc']==1 and e['kammerlaeufe']==0 for e in sperre['faelle'])
quelle=Path('/root/biotop');hashes=json.loads(Path('/root/reparatur-01/review-02/QUELLHASHES.json').read_text())
assert all(hashlib.sha256((quelle/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
r={'scope':'Nur Kernauftrag nach Auftraggeber-Eingrenzung; vier weiter offene Phase4-Lücken nicht grün gewertet','suite':{'bestanden':len(cases),'von':len(cases),'kernmass_pareto_zuerst':len(prior),'reihenfolge':[c.get('classname','')+'::'+c.get('name','') for c in cases],'kammerlaeufe':suite['kammerlaeufe']},'paare':zeilen,'positive':sum(e['praedikat'] is True for e in zeilen if e['gruppe']=='proben'),'negative':sum(e['praedikat'] is False for e in zeilen if e['gruppe']=='gegenproben'),'erwartet_je':len(namen),'batterie_kammerlaeufe':paare['kosten']['kammerlaeufe'],'cli':{'rc':gate['rc'],'gen0_nachweis_verwendbar':gate['gen0_nachweis_verwendbar'],'kammerteile':teile,'kammergesamt':len(kammern),'schutz':gate['schutz'],'gesperrte_bereiche':raw['rauschen']['gesperrt'],'bereichszahl':len(raw['rauschen']['bereiche'])},'cli_sperre':{'gesperrt':sperre['gesperrt'],'von':sperre['von'],'kammern':sum(x['kammerlaeufe'] for x in sperre['faelle'])},'quelle_identisch_review02':len(hashes),'unabhaengiges_kernreview':'noch offen'}
ziel.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items() if k not in ('paare','suite')},ensure_ascii=False,indent=2));print(json.dumps({'suite':{k:v for k,v in r['suite'].items() if k!='reihenfolge'},'vertrag':[z for z in zeilen if z['probe']=='vertrag']},ensure_ascii=False,indent=2))
