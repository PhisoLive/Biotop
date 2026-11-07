"""Reviewer-Repros gegen den aktuellen Elterncode, nur private Fixtures."""
from pathlib import Path
import subprocess,os,json,shutil,hashlib,xml.etree.ElementTree as ET
P=Path('/root/reparatur-01');W=P/'eltern-reviewpruefung';W.mkdir(exist_ok=False)
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
(W/'repo').symlink_to('/root/biotop',target_is_directory=True)
for teil,quelle,namen in [('pruefer-eichung',P/'review-01/pruefer-eichung',['test_review.py','guard/sitecustomize.py']),('pruefer-mass',P/'review-01/pruefer-mass',['test_review_contracts.py','repro_mass.py','repro_negotiation.py'])]:
    for name in namen:
        a=quelle/name;b=W/teil/name;b.parent.mkdir(parents=True,exist_ok=True)
        text=a.read_text().replace("/root/reparatur-01/review-01",str(W))
        b.write_text(text)
    (W/teil/'tmp').mkdir(exist_ok=True)
results=[]
for name,teil,test in [('43-review-eichung-eltern-rot','pruefer-eichung','test_review.py'),('44-review-mass-eltern-rot','pruefer-mass','test_review_contracts.py')]:
    env=dict(os.environ,PYTHONPATH=os.pathsep.join([str(W/teil/'guard'),'/root/biotop',str(W/teil)]),PYTHONDONTWRITEBYTECODE='1',PYTEST_DISABLE_PLUGIN_AUTOLOAD='1',TMPDIR=str(W/teil/'tmp'),BIOTOP_DB=str(W/teil/'tmp/unbenutzt.db'))
    cmd=['/root/reparatur-01/venv/bin/python','-B','-m','pytest','-q','-s',str(W/teil/test),'--basetemp='+str(W/teil/'tmp/pytest'),'-c','/root/biotop/pytest.ini','--junitxml='+str(O/(name+'.xml'))]
    r=subprocess.run(cmd,cwd=W/teil,env=env,capture_output=True,text=True,timeout=60)
    (O/(name+'.txt')).write_text('BEFEHL: '+' '.join(cmd)+'\n'+r.stdout+'\nSTDERR:\n'+r.stderr+'\nRC: '+str(r.returncode)+'\n')
    suites=[s.attrib for s in ET.parse(O/(name+'.xml')).getroot().iter('testsuite')]
    d={'rc':r.returncode,'testsuites':suites,'befehl':cmd,'art':'Reviewer-Unit-Reproduktion am Elterncode, Mess-/Modellgrenzen ersetzt, kein Docker und keine Modelle'}
    (O/(name+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');results.append(d)
print(json.dumps(results,ensure_ascii=False,indent=2))
assert all(r['rc']==1 for r in results)
