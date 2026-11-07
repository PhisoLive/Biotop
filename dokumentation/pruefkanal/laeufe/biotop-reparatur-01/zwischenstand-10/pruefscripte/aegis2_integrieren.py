"""Aegis-/Zeugenanteil der zweiten Runde selektiv und hashgebunden integrieren."""
from pathlib import Path
import hashlib,json,sys,subprocess,datetime
P=Path('/root/reparatur-01');R=Path('/root/biotop');D=P/'nachbesserung-02/lieferung'
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
phase=sys.argv[1];assert phase in ('tests','produkt')
name='53-aegis2-tests-integriert.json' if phase=='tests' else '54-aegis2-produkt-integriert.json'
ziel=O/name;assert not ziel.exists()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
lines=(D/'SHA256SUMS').read_text().splitlines()
assert sha(D/'SHA256SUMS')=='f1df8c2d4f341cfaf58150a943ce101d84e26f0a30df9519447c6b730917fe8d'
for h,f in [line.split('  ',1) for line in lines]:
    p=D/f;assert p.resolve().is_relative_to(D.resolve()) and sha(p)==h,f
manifest=json.loads((D/'DATEIMANIFEST.json').read_text())
allow={'biotop/organe/aegis.py','biotop/organe/eichproben.py','tests/test_junit_zeugen.py','tests/test_review_vertrag.py'}
assert {x['path'] for x in manifest}==allow
before={f:sha(R/f) if (R/f).exists() else None for f in allow}
for x in manifest:
    f=x['path'];assert sha(D/'dateien'/f)==x['sha256']
    expected=x['sha256'] if phase=='produkt' and f.startswith('tests/') else x['before_sha256']
    assert before[f]==expected,(f,before[f],expected)
selected=sorted(f for f in allow if f.startswith('tests/')==(phase=='tests'))
cmd=['git','-C',str(R),'apply',*[f'--include={f}' for f in selected],str(D/'AENDERUNGEN.diff')]
subprocess.run(cmd[:4]+['--check']+cmd[4:],check=True)
subprocess.run(cmd,check=True)
for f in selected:assert sha(R/f)==sha(D/'dateien'/f)
subprocess.run(['git','-C',str(R),'diff','--check'],check=True)
base=json.loads((P/'nachbesserung-02/ELTERN-AUSGANG.json').read_text())
abweichungen=[f for f,x in base.items() if f not in allow and sha(R/f)!=x['sha256']]
assert not abweichungen,abweichungen
r={'zeit':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':phase,'auswahl':selected,'vorher':before,'nachher':{f:sha(R/f) if (R/f).exists() else None for f in allow},'lieferdateien_geprueft':len(lines),'uebrige_ausgangsdateien_geprueft':sum(f not in allow for f in base),'uebrige_abweichungen':abweichungen,'gesamtintegration':False,'grenze':'Nur Aegis/Zeugenanteil, keine Messgeräte-/Verbraucher- oder Außenänderung übernommen.'}
ziel.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False))
