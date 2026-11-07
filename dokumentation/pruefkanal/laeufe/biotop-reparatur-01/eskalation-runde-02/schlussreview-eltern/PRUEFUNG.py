"""Nur lesende Belegauswertung und deklarierte synthetische Parser-Units.
Kein Projektimport, kein Werkcode, kein pytest-/Docker-/Netz-/DB-Start.
Alle geschriebenen Artefakte bleiben unter dem Prüferordner.
"""
import ast
import collections
import hashlib
import json
import os
from pathlib import Path
import re
from types import SimpleNamespace
import xml.etree.ElementTree as ET

ROOT = Path('/root/reparatur-01/review-03')
OUT = Path('/root/reparatur-01/schlussreview-eltern')
REP = ROOT / 'repo'
EV = ROOT / 'elternbelege'

def save(name, obj):
    (OUT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def load(path):
    return json.loads(path.read_text())

def snapshot():
    return [dict(pfad=x['pfad'], sha256=hashlib.sha256((REP/x['pfad']).read_bytes()).hexdigest(),
                 bytes=(REP/x['pfad']).stat().st_size, mtime_ns=(REP/x['pfad']).stat().st_mtime_ns)
            for x in load(ROOT/'QUELLHASHES.json')]

manifest = load(ROOT/'QUELLHASHES.json')
hashes = {x['pfad']:x['sha256'] for x in manifest}
before = load(OUT/'QUELLEN-VORHER.json')
parsed = []
for x in manifest:
    if x['pfad'].endswith('.py'):
        ast.parse((REP/x['pfad']).read_text(), filename=x['pfad'])
        parsed.append(x['pfad'])
diffs = re.findall(r'^\+\+\+ b/(.+)$', (ROOT/'AENDERUNGEN.diff').read_text(), re.M)
result = dict(art='Unabhängige Nachzählung vorhandener Elternbelege, keine neue Bestandsausführung',
              ast_dateien=parsed, diff_pfade=diffs, laeufe=[], batterien={}, eigene_kammerlaeufe=0,
              eigene_modell_api_aufrufe=0, eigene_bezahlte_tool_api_kosten_eur=0,
              traegerkosten='Nicht gemessen; nicht als null behauptet')
allcontainers=[]
names=['58-leser2-eltern-rot','59-leser2-eltern-gruen','60-vertragszeugen-integration',
       '61-vertragszeugen-integration-gruen','62-gesamtsuite-zweite-runde','63-vorspann-zweite-runde']
for name in names:
    d=load(EV/(name+'.json')); chambers=load(EV/(name+'-kammer.json'))
    containers=[x['container'] for x in chambers]; allcontainers += containers
    assert len(chambers)==d['kammerlaeufe']==len(set(containers))
    row=dict(id=name, rc=d['rc'], kammern=len(chambers), eindeutige_container=len(set(containers)),
             quellenbindung_anzahl=len(d['quellen_sha256']),
             quellenabweichungen=[p for p,h in d['quellen_sha256'].items() if hashes.get(p)!=h],
             kammer_rcs=dict(collections.Counter(x['rc'] for x in chambers)))
    xp=EV/(name+'.xml')
    if xp.exists():
        xml=ET.parse(xp).getroot(); tests=list(xml.iter('testcase'))
        row['junit']=dict(tests=len(tests),fehler=sum(t.find('error') is not None for t in tests),
                         fehlgeschlagen=sum(t.find('failure') is not None for t in tests),
                         uebersprungen=sum(t.find('skipped') is not None for t in tests))
        row['junit']['bestanden']=sum(all(t.find(k) is None for k in ['failure','error','skipped']) for t in tests)
        row['junit']['fehlschlaege']=[dict(test=t.attrib, text=t.find('failure').text) for t in tests if t.find('failure') is not None]
        row['junit']['je_datei']=dict(collections.Counter(t.get('classname') for t in tests))
        for key,attr in [('tests','tests'),('fehler','errors'),('fehlgeschlagen','failures'),('uebersprungen','skipped')]:
            assert row['junit'][key]==sum(int(s.get(attr,0)) for s in xml.iter('testsuite'))
    result['laeufe'].append(row)
result['kammern_in_58_bis_63']=len(allcontainers)
result['eindeutige_container_in_58_bis_63']=len(set(allcontainers))
assert len(set(allcontainers))==len(allcontainers)

for name in ['62-gesamtsuite-zweite-runde','63-vorspann-zweite-runde']:
    d=load(EV/(name+'.json'))
    er=load(EV/(name+'-eichpaare.json')) if name.startswith('62') else load(EV/(name+'.json'))
    if name.startswith('63'):
        er=json.loads(er['nachweis']['ergebnis'])['eichproben']
        result['cli']=dict(rc=d['rc'],status=d['nachweis']['status'],nachweis_sha256=d['nachweis']['nachweis_sha256'],
            gen0_nachweis_verwendbar=d['gen0_nachweis_verwendbar'],stdout=(EV/(name+'.stdout.txt')).read_text(),
            stderr=(EV/(name+'.stderr.txt')).read_text(), neue_modellbuchungen=len(d['neue_modellbuchungen']),
            gebuchte_kammern=sum(k['kammerlaeufe'] for k in d['eichkosten']), kosten_zeilen=d['eichkosten'])
        assert result['cli']['gebuchte_kammern']==d['kammerlaeufe']==d['gebuchte_kammern']
    summary=dict(bestanden=er['bestanden'],paare=[],positiv_gueltig_bestanden=0,negativ_gueltig_falsch=0)
    whole={x['container'] for x in load(EV/(name+'-kammer.json'))}
    paircontainers=[]
    for group in ['proben','gegenproben']:
        for n,p in sorted(er[group].items()):
            cs=p['kammer']; paircontainers += [x['container'] for x in cs]
            assert len(cs)==p['kammerlaeufe']
            row=dict(gruppe=group,name=n,**{k:p[k] for k in ['ausgefuehrt','pruefbar','bestanden','kammerlaeufe','grund']})
            be=p['belege']; m=be['messung']; u=be['urteil']
            row['mass']=u.get('mass'); row['vertrag_verletzt']=u.get('vertrag_verletzt'); row['norm']=u.get('norm')
            row['messung_gueltig']=m.get('gueltig'); row['basis_paar_gueltig']=(m.get('_basis_paar') or {}).get('gueltig')
            row['unbrauchbare_messungen']=[]
            for i,k in enumerate(cs):
                if '_messgeraet/messen.py' not in k['befehl']: continue
                mm=re.search(r'@@MESSUNG@@(.*)@@ENDE@@', k['stdout'],re.S)
                item=dict(index=i,container=k['container'],rc=k['rc'],zeitlimit=k['zeitlimit'],
                          stdout_bytes=len(k['stdout'].encode()),stderr_bytes=len(k['stderr'].encode()))
                if mm:
                    raw=json.loads(mm.group(1)); item['pytest_rc']=raw['werk'].get('pytest_rc')
                    item['laufzeit_fehler']={b:v for b,v in raw['bereiche'].items() if v.get('laufzeit_ms') is None}
                    item['einzeltest_fehlliste']=raw['werk'].get('tests_fehlgeschlagen_liste')
                    item['pytest_tail']=raw['werk'].get('pytest_tail')
                elif k['rc']:
                    item['stderr_anfang']=k['stderr'][:180]
                    lists={}
                    for key in ['aufrufe','beendet']:
                        match=re.search(r"'"+key+r"': (\[[^\]]*\])",k['stderr'])
                        if match: lists[key]=ast.literal_eval(match.group(1))
                    item['lesbare_begleitzaehler']={key:len(val) for key,val in lists.items()}
                    if set(lists)=={'aufrufe','beendet'}:
                        item['beendet_ohne_call']=sorted(set(lists['beendet'])-set(lists['aufrufe']))
                    item['einschraenkung']='stderr transportseitig als Ende erhalten; vollständige ursprüngliche Ausnahme und JUnit hier nicht behauptet'
                if k['rc'] or (mm and item['laufzeit_fehler']): row['unbrauchbare_messungen'].append(item)
            if n=='vertrag':
                target=be['vertragspfad']+'::'+be['vertragstest'].split('::')[-1]
                row['benannte_zeugen']={side:{key:be[side].get(key) for key in [be['verbrauchertest'],target]} for side in ['basis_tests','kandidat_tests']}
            ok=p['ausgefuehrt'] is True and p['pruefbar'] is True
            if group=='proben': summary['positiv_gueltig_bestanden'] += int(ok and p['bestanden'] is True)
            else: summary['negativ_gueltig_falsch'] += int(ok and p['bestanden'] is False)
            summary['paare'].append(row)
    assert set(paircontainers)<=whole
    assert len(paircontainers)==len(set(paircontainers))==er['kosten']['kammerlaeufe']
    summary['kammerlaeufe']=len(paircontainers)
    summary['modellaufrufe']=sum(p['modellaufrufe'] for g in ['proben','gegenproben'] for p in er[g].values())
    summary['kosten_eur']=sum(p['kosten_eur'] for g in ['proben','gegenproben'] for p in er[g].values())
    result['batterien'][name]=summary
save('BELEGABGLEICH.json',result)

# Synthetische Unit: exakter Parser-AST und reine Maßfunktionen, keine Projektimporte.
source=(REP/'biotop/kern/messgeraet.py').read_text(); tree=ast.parse(source)
raw=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='MESSSKRIPT' for t in n.targets)))
pt=ast.parse(raw)
parsernodes=[n for n in pt.body if (isinstance(n,ast.FunctionDef) and n.name=='zuordnung') or
             (isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=='tc')]
scoring_names={'kernmass_f2_bereich','kernmass_f2','pareto_f2','grenzen_f2','urteil_f2'}
selected=[n for n in tree.body if (isinstance(n,ast.FunctionDef) and n.name in scoring_names) or
          (isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in {'PARETO_F2','GRENZ_F2','RAUSCH_F4'} for t in n.targets))]
ns={}; exec(compile(ast.Module(body=selected,type_ignores=[]),'reine_kernfunktionen','exec'),ns)
def measurement(failing):
    root=ET.Element('testsuites'); suite=ET.SubElement(root,'testsuite')
    cases=[('TestA','test_wert'),('TestB','test_wert'),('TestC','test_alt')]
    for cl,n in cases:
        tc=ET.SubElement(suite,'testcase',file='tests/test_alpha.py',classname='tests.test_alpha.'+cl,name=n)
        if cl in failing: ET.SubElement(tc,'failure',message='AssertionError').text='assert False'
    env=dict(os=os,bereiche=['alpha'],testfaelle=list(root.iter('testcase')),je_datei={},fehler_liste=[])
    exec(compile(ast.Module(body=parsernodes,type_ignores=[]),'originaler_junit_parser_ast','exec'),env)
    passed,failed=env['je_datei']['alpha']
    m=dict(bereiche={'alpha':dict(tests_bestanden=passed,tests_fehlgeschlagen=failed,tests_gesamt=len(cases),
                sicherheit_punkte=0,tote_funktionen=0,groesste_funktion=2,laufzeit_ms=1)},
           werk=dict(baut=True,tests_fehlgeschlagen_liste=env['fehler_liste'],zyklen=0,bauzeit_ms=10))
    return m,ET.tostring(root,encoding='unicode')
basis,bxml=measurement({'TestA','TestC'}); kandidat,kxml=measurement({'TestB'})
verdict=ns['urteil_f2'](basis,kandidat,basis,['alpha'],['alpha'])
assert verdict['ok'] is True and verdict['zuwachs']==1 and verdict['pareto_schlechter']==[]
unit=dict(grenze='Synthetische Parser-/Entscheider-Unit, kein realer Werk-/Kammer-/JUnit-Lauf',
          parser_quelle='biotop/kern/messgeraet.py:123-134',entscheider_quelle='biotop/kern/messgeraet.py:344-368,523-562',
          basis_xml=bxml,kandidat_xml=kxml,basis=basis,kandidat=kandidat,tatsaechliches_urteil=verdict)
# Dieselben Messzahlen, eindeutige Testidentitäten: negativer Kontrollpfad.
b2=json.loads(json.dumps(basis)); k2=json.loads(json.dumps(kandidat))
b2['werk']['tests_fehlgeschlagen_liste']=['tests/test_alpha.py::TestA::test_wert','tests/test_alpha.py::TestC::test_alt']
k2['werk']['tests_fehlgeschlagen_liste']=['tests/test_alpha.py::TestB::test_wert']
unit['kontrolle_mit_eindeutigen_ids']=ns['urteil_f2'](b2,k2,b2,['alpha'],['alpha'])
assert unit['kontrolle_mit_eindeutigen_ids']['ok'] is False

# Synthetische Fund-Verbraucher-Unit: keinerlei Kammerprozess.
fsource=ast.parse((REP/'biotop/organe/fundpruefung.py').read_text())
fn=next(n for n in fsource.body if isinstance(n,ast.FunctionDef) and n.name=='_ausfuehren')
xml=ET.fromstring('<testcase name="test_eins" classname="tests.test_neubewertung_probe"><failure message="NameError: name fehlt">tests/test_neubewertung_probe.py:2: NameError: name fehlt</failure></testcase>')
fns=dict(Path=Path,_pytest_nachweis=lambda *args:(SimpleNamespace(rc=1,stdout='Deklariertes Unit-I/O',stderr=''),[xml]))
exec(compile(ast.Module(body=[fn],type_ignores=[]),'originaler_fund_verbraucher_ast','exec'),fns)
u=fns['_ausfuehren'](OUT,'probe','def test_eins():\n    unbekannter_name\n')
assert u[:2]==(False,True)
unit['fund_fehlattribution']=dict(grenze='Synthetischer Parser-Verbrauch mit gestelltem I/O',
    quelle='biotop/organe/fundpruefung.py:75-77,95-111',failure_xml=ET.tostring(xml,encoding='unicode'),
    besteht=u[0],absturz_im_werk=u[1],erwartet_absturz_im_werk=False)
save('UNIT-GRENZE.json',unit)
after=snapshot()
after_report=dict(anzahl=len(after),manifest_abweichungen=[x['pfad'] for x,y in zip(after,manifest) if x!=y],
    vorher_nachher_abweichungen=[x['pfad'] for x,y in zip(after,before['quellen']) if x!=y],quellen=after)
assert not after_report['manifest_abweichungen'] and not after_report['vorher_nachher_abweichungen']
save('QUELLEN-NACHHER.json',after_report)
print(json.dumps(dict(ast_dateien=len(parsed),diff_pfade=len(diffs),
    laeufe=[{k:v for k,v in r.items() if k!='junit'}|({'junit':{k:v for k,v in r['junit'].items() if k not in ['fehlschlaege','je_datei']}} if 'junit' in r else {}) for r in result['laeufe']],
    kammern_58_bis_63=result['kammern_in_58_bis_63'],
    batterien={k:{x:y for x,y in v.items() if x!='paare'} for k,v in result['batterien'].items()},
    nachweisfehler=[dict(lauf=k,name=p['name'],messungen=p['unbrauchbare_messungen']) for k,v in result['batterien'].items() for p in v['paare'] if p['unbrauchbare_messungen']],
    synthetisches_pareto=verdict,kontrolle=unit['kontrolle_mit_eindeutigen_ids'],fund_unit=unit['fund_fehlattribution'],
    hash_nachher_abweichungen=after_report['vorher_nachher_abweichungen']),ensure_ascii=False,indent=2))
