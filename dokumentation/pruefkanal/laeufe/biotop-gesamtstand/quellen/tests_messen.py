"""Wiederholung der lesenden Sammlung: Mount unter /quelle statt /root (Kammernutzer)."""
from pathlib import Path
import subprocess,json
A=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/ausgaben')
cmd=['docker','run','--rm','--network','none','--read-only','--memory','128m','--cpus','1','--pids-limit','64','--cap-drop','ALL','--security-opt','no-new-privileges','--tmpfs','/tmp:rw,nosuid,size=32m','-e','PYTHONDONTWRITEBYTECODE=1','-e','PYTHONPATH=/quelle','-v','/root/biotop/biotop:/quelle/biotop:ro','-v','/root/biotop/pruefung:/quelle/pruefung:ro','-w','/tmp','biotop-kammer:1','python']
for name,args in [('16-eigene-tests-sammlung-02.json',['-m','pytest','--collect-only','-q','-p','no:cacheprovider','/quelle/biotop','/quelle/pruefung']),('17-rauschbeispiele-ausfuehrung-02.json',['/quelle/pruefung/rauschregeln_pruefen.py'])]:
    p=subprocess.run(cmd+args,capture_output=True,text=True,timeout=60)
    r={'befehl':cmd+args,'rc':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    (A/name).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n'); print(name,json.dumps(r,ensure_ascii=False))
