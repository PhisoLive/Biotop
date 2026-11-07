"""Gestellte Gegenmutanten: nachweisen, dass eigene Tests tatsächlich rot werden."""
from pathlib import Path
import shutil,subprocess,json,os,hashlib,xml.etree.ElementTree as ET
R=Path('/root/biotop'); W=Path('/root/reparatur-01/gegenmutanten')
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
original=R/'biotop/kern/messgeraet.py'; inhalt=original.read_text(); vorher=hashlib.sha256(original.read_bytes()).hexdigest()
mutanten=[('kernmass-bestehende-tests', 'return -b["tests_fehlgeschlagen"] - b["sicherheit_punkte"] - b["tote_funktionen"]', 'return b["tests_bestanden"] - b["tests_fehlgeschlagen"] - b["sicherheit_punkte"] - b["tote_funktionen"]', 'tests/test_kernmass_pareto.py', 'kernmass_belohnt'),
('pareto-einzelregression','regress = sorted(fehl_kand - fehl_basis)','regress = []', 'tests/test_kernmass_pareto.py', 'erkennt_einzelregression'),
('streuung-falsche-ebene','if ebene != "zwischen":','if False:', 'tests/test_rauschmessung.py', 'verbietet_innerhalb')]
ergebnisse=[]
for name,alt,neu,test,auswahl in mutanten:
    ziel=W/name; assert not ziel.exists(); ziel.mkdir(parents=True)
    shutil.copytree(R/'biotop',ziel/'biotop',ignore=shutil.ignore_patterns('__pycache__'))
    shutil.copytree(R/'tests',ziel/'tests',ignore=shutil.ignore_patterns('__pycache__'))
    shutil.copyfile(R/'pytest.ini',ziel/'pytest.ini')
    assert inhalt.count(alt)==1
    (ziel/'biotop/kern/messgeraet.py').write_text(inhalt.replace(alt,neu))
    xml=O/('27-mutant-'+name+'.xml')
    cmd=['/root/reparatur-01/venv/bin/python','-m','pytest',test,'-k',auswahl,'-q','--junitxml='+str(xml)]
    env=os.environ.copy();env.update(PYTHONPATH=str(ziel),PYTHONDONTWRITEBYTECODE='1',TMPDIR='/root/reparatur-01/eltern-temp')
    r=subprocess.run(cmd,cwd=ziel,text=True,capture_output=True,env=env)
    out=O/('27-mutant-'+name+'.txt');out.write_text('GESTELLTER GEGENMUTANT, NICHT PRODUKTIVCODE\nBEFEHL: '+' '.join(cmd)+'\n'+r.stdout+'\nSTDERR:\n'+r.stderr+'\nRC: '+str(r.returncode)+'\n')
    s=[x.attrib for x in ET.parse(xml).getroot().iter('testsuite')]
    korrekt=(r.returncode==1 and sum(int(x['failures']) for x in s)>0 and sum(int(x['errors']) for x in s)==0)
    ergebnisse.append({'name':name,'absichtlicher_fehler':{'alt':alt,'mutant':neu},'rc':r.returncode,'testsuites':s,'wie_erwartet_rot':korrekt,'ausgabe':out.name})
    assert korrekt, name
nachher=hashlib.sha256(original.read_bytes()).hexdigest();assert vorher==nachher
(O/'27-gegenmutanten.json').write_text(json.dumps({'herkunft':'drei ausdrücklich gestellte Gegenmutanten in isolierten Codekopien; kein Biotop-Lauf','original_vorher':vorher,'original_nachher':nachher,'ergebnisse':ergebnisse},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'wie_erwartet_rot':sum(e['wie_erwartet_rot'] for e in ergebnisse),'von':len(ergebnisse),'produktiver_kern_unveraendert':vorher==nachher},ensure_ascii=False))
