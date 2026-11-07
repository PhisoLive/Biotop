"""Einen Eigen-Testlauf mit unveränderlicher Roh-Ausgabe und Rückgabewert sichern."""
from pathlib import Path
import subprocess,sys,json,time,xml.etree.ElementTree as ET,os
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
name=sys.argv[1]; assert '/' not in name
out=O/(name+'.txt'); assert not out.exists(), 'Ausgabe existiert bereits'
cmd=['/root/reparatur-01/venv/bin/python','-m','pytest',*sys.argv[2:],'--junitxml='+str(O/(name+'.xml'))]
t=time.monotonic(); env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
tmp=Path('/root/reparatur-01/eltern-temp');tmp.mkdir(exist_ok=True);env['TMPDIR']=str(tmp);env['PYTHONPATH']='/root/biotop'
r=subprocess.run(cmd,cwd='/root/biotop',capture_output=True,text=True,env=env)
out.write_text('BEFEHL: '+' '.join(cmd)+'\nARBEITSVERZEICHNIS: /root/biotop\n'+r.stdout+'\nSTDERR:\n'+r.stderr+'\nRUECKGABEWERT: '+str(r.returncode)+'\n')
result={'befehl':cmd,'rc':r.returncode,'dauer_s':round(time.monotonic()-t,3),'ausgabe':str(out)}
if (O/(name+'.xml')).exists():
    root=ET.parse(O/(name+'.xml')).getroot(); result['testsuites']=[x.attrib for x in root.iter('testsuite')]
(O/(name+'.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(r.stdout);print(r.stderr);print(json.dumps(result,ensure_ascii=False))
sys.exit(r.returncode)
