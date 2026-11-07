"""Bestands-Replay mit integrierten Modulen wiederholen, keine Produktivänderung."""
from pathlib import Path
import shutil,subprocess,os,json,hashlib
W=Path('/root/reparatur-01/eltern-acb');assert not W.exists();W.mkdir()
Q=Path('/root/reparatur-01/teil-acb')
shutil.copyfile(Q/'bestandspruefung.py',W/'bestandspruefung.py')
shutil.copytree(Q/'baseline',W/'baseline')
(W/'repo').symlink_to('/root/biotop',target_is_directory=True)
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',PYTHONPATH='/root/biotop',TMPDIR='/root/reparatur-01/eltern-temp')
cmd=['/root/reparatur-01/venv/bin/python',str(W/'bestandspruefung.py'),str(O/'34-acb-bestandspruefung-integriert.json')]
r=subprocess.run(cmd,cwd=W,env=env,text=True,capture_output=True)
(O/'34-acb-bestandspruefung-integriert.txt').write_text('BEFEHL: '+' '.join(cmd)+'\n'+r.stdout+'\nSTDERR:\n'+r.stderr+'\nRC: '+str(r.returncode)+'\n')
assert r.returncode==0,r.stderr
neu=(O/'34-acb-bestandspruefung-integriert.json').read_bytes();alt=(Q/'bestandspruefung-03.json').read_bytes()
beleg={'rc':r.returncode,'bytegleich_mit_teilpruefung_03':neu==alt,'sha256_integrierter_replay':hashlib.sha256(neu).hexdigest(),'zusammenfassung':json.loads(neu)['summary']}
(O/'34-acb-integrationsvergleich.json').write_text(json.dumps(beleg,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(beleg,ensure_ascii=False,indent=2))
assert neu==alt
