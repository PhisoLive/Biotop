"""Integrierte Eigen-Suite mit tatsächlichem Kammerzähler, kein Modellnetz."""
from pathlib import Path
import os,sys,json,time,hashlib,subprocess,socket,contextlib,xml.etree.ElementTree as ET
R=Path('/root/biotop')
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
name=sys.argv[1];assert '/' not in name
for suffix in ('.txt','.json','.xml','-kammer.json'):assert not (O/(name+suffix)).exists()
os.environ.update(PYTHONPATH=str(R),PYTHONDONTWRITEBYTECODE='1',TMPDIR='/root/reparatur-01/eltern-temp',BIOTOP_DB='/root/reparatur-01/unbenutzt-suite.db',BIOTOP_EICHWERK='/root/reparatur-01/teil-eichung/werk-lauf25-kopie',BIOTOP_EICHDB='/root/reparatur-01/ausgang.db',BIOTOP_EICHWERK_ID='22',BIOTOP_EICHBELEG=str(O/(name+'-eichpaare.json')))
os.chdir(R);sys.path.insert(0,str(R));sys.dont_write_bytecode=True
import tempfile
tempfile.tempdir=os.environ['TMPDIR']
def verboten(*a,**kw):raise AssertionError('Reparatursuite: Netzwerk gesperrt')
socket.socket.connect=verboten;socket.create_connection=verboten
from biotop.organe import kammer
import pytest
quellen={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((R/'biotop').rglob('*.py'))}
argv=['-v','--tb=short','--junitxml='+str(O/(name+'.xml'))]
t0=time.monotonic()
with (O/(name+'.txt')).open('x') as out,contextlib.redirect_stdout(out),contextlib.redirect_stderr(out),kammer.zaehlung() as aufrufe:
    print('BEFEHL:',sys.executable,*sys.argv,'\nPYTEST-ARGUMENTE:',argv,'\nQUELLWURZEL:',R)
    rc=pytest.main(argv)
    print('RUECKGABEWERT:',rc)
(O/(name+'-kammer.json')).write_text(json.dumps(aufrufe,ensure_ascii=False,indent=2)+'\n')
suites=[x.attrib for x in ET.parse(O/(name+'.xml')).getroot().iter('testsuite')]
ergebnis={'rc':int(rc),'dauer_s':round(time.monotonic()-t0,3),'testsuites':suites,'kammerlaeufe':len(aufrufe),'verschiedene_container':len({x['container'] for x in aufrufe}),'quellen_sha256':quellen,'netzsperre':True,'art':'Eigen-Tests samt echten Eichfixtures; kein natürlicher Biotop-Lauf'}
assert ergebnis['kammerlaeufe']==ergebnis['verschiedene_container']
assert quellen=={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((R/'biotop').rglob('*.py'))}
(O/(name+'.json')).write_text(json.dumps(ergebnis,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in ergebnis.items() if k!='quellen_sha256'},ensure_ascii=False));sys.exit(rc)
