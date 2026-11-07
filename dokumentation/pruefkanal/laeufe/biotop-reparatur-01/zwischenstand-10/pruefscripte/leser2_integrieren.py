"""Restliche Kernleser der zweiten/letzten Runde hashgebunden integrieren, keine Außenfixes."""
from pathlib import Path
import hashlib,json,sys,subprocess,datetime,ast
P=Path('/root/reparatur-01');Q=Path('/root/biotop');O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
phase=sys.argv[1];assert phase in ('tests','produkt')
ziel=O/('58-leser2-tests-integriert.json' if phase=='tests' else '59-leser2-produkt-integriert.json');assert not ziel.exists()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def lade(p):return json.loads(p.read_text())
base=lade(P/'nachbesserung-02/ELTERN-AUSGANG.json')
ag={x['path']:x['sha256'] for x in lade(P/'nachbesserung-02/lieferung/DATEIMANIFEST.json')}
pakete=[('messung','AENDERUNGEN.diff','1316c2e9ea914fb490225d7028eb2e6782f77046511f405e1b121dc8a16bfd3b',{'biotop/kern/messgeraet.py','tests/test_messnachweise.py'}),('verbraucher','KERN.diff','1aabd4f67c79861e9c0e3a9f8e9f307a9798eba32d0ee45ecd979d41e34af6c0',{'biotop/lauf.py','biotop/organe/fundpruefung.py','tests/test_nachweis_verbraucher.py'})]
er=[];allow=set(ag)
for name,patch,checksum,pfade in pakete:
    D=P/'nachbesserung-02'/name/'lieferung'
    assert sha(D/'SHA256SUMS')==checksum
    ls=(D/'SHA256SUMS').read_text().splitlines()
    for line in ls:
        h,f=line.split(None,1);f=f.strip().removeprefix('*');p=D/f
        assert p.resolve().is_relative_to(D.resolve()) and sha(p)==h,f
    assert {str(p.relative_to(D/'dateien')) for p in (D/'dateien').rglob('*') if p.is_file()}==pfade
    allow|=pfade
    for f in pfade:
        alt=sha(Q/f) if (Q/f).exists() else None
        erwartet=sha(D/'dateien'/f) if phase=='produkt' and f.startswith('tests/') else (base[f]['sha256'] if f in base else None)
        assert alt==erwartet,(f,alt,erwartet)
    sel=sorted(f for f in pfade if f.startswith('tests/')==(phase=='tests'))
    cmd=['git','-C',str(Q),'apply',*[f'--include={f}' for f in sel],str(D/patch)]
    subprocess.run(cmd[:4]+['--check']+cmd[4:],check=True);subprocess.run(cmd,check=True)
    for f in sel:assert sha(Q/f)==sha(D/'dateien'/f)
    er.append({'paket':name,'manifest':checksum,'dateien_geprueft':len(ls),'integriert':sel,'hashes':{f:sha(Q/f) for f in sel}})
assert all(sha(Q/f)==h for f,h in ag.items())
abweichungen=[f for f,z in base.items() if f not in allow and sha(Q/f)!=z['sha256']];assert not abweichungen,abweichungen
if phase=='produkt':
    vorher=ast.parse((P/'nachbesserung-02/verbraucher/lieferung/ausgang/biotop/lauf.py').read_text());nachher=ast.parse((Q/'biotop/lauf.py').read_text())
    for baum in (vorher,nachher):baum.body=[x for x in baum.body if not isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef)) or x.name!='_verhandeln']
    assert ast.dump(vorher)==ast.dump(nachher)
subprocess.run(['git','-C',str(Q),'diff','--check'],check=True)
r={'zeit':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':phase,'lieferungen':er,'bisher_erlaubte_dateien':sorted(allow),'uebrige_ausgangsdateien_bytegleich':sum(f not in allow for f in base),'abweichungen':abweichungen,'aussenfix_integriert':False,'runde':2,'letzte_automatische_runde':True}
ziel.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False))
