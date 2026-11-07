"""A/C+B nach vollständiger Integration erneut am gleichen Snapshot vergleichen."""
from pathlib import Path
import subprocess,os,json,hashlib
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
name='42-acb-gesamtintegration';assert not (O/(name+'.json')).exists()
cmd=['/root/reparatur-01/venv/bin/python','/root/reparatur-01/eltern-acb/bestandspruefung.py',str(O/(name+'.json'))]
r=subprocess.run(cmd,cwd='/root/reparatur-01/eltern-acb',env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH='/root/biotop',TMPDIR='/root/reparatur-01/eltern-temp'),capture_output=True,text=True)
(O/(name+'.txt')).write_text('BEFEHL: '+' '.join(cmd)+'\n'+r.stdout+'\nSTDERR:\n'+r.stderr+'\nRC: '+str(r.returncode)+'\n')
assert r.returncode==0
neu=(O/(name+'.json')).read_bytes();alt=(O/'34-acb-bestandspruefung-integriert.json').read_bytes()
b={'rc':r.returncode,'bytegleich_mit_34':neu==alt,'sha256':hashlib.sha256(neu).hexdigest(),'summary':json.loads(neu)['summary']}
(O/(name+'-vergleich.json')).write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(b,ensure_ascii=False,indent=2));assert neu==alt
