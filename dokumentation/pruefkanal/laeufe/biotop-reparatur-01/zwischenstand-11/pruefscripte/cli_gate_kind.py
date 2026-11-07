"""Reale Biotop-CLI im Privatbestand, mit Netzsperre und Kammer-Rohbelegen."""
from pathlib import Path
import socket,sys,runpy,os,json
sys.dont_write_bytecode=True
sys.path.insert(0,'/root/biotop')
def gesperrt(*a,**kw):raise AssertionError('Reparatur-Gate: Netzaufruf gesperrt')
socket.socket.connect=gesperrt;socket.create_connection=gesperrt
from biotop.organe import kammer
ziel=Path(os.environ['BIOTOP_KAMMERBELEG']);assert not ziel.exists()
sys.argv=['biotop',*sys.argv[1:]]
rc=1
with kammer.zaehlung() as aufrufe:
    try:runpy.run_module('biotop',run_name='__main__')
    except SystemExit as e:rc=e.code
    finally:ziel.write_text(json.dumps(aufrufe,ensure_ascii=False,indent=2)+'\n')
sys.exit(rc)
