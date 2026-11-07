from pathlib import Path
import subprocess, json, sqlite3, hashlib, shutil, os
from datetime import datetime, timezone
from decimal import Decimal

W = Path('/root/wiedereinstieg-01')
B = W / 'belege'
B.mkdir(exist_ok=True)
P = Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe')

def neu(p, data):
    with p.open('xb') as f:
        f.write(data if isinstance(data, bytes) else data.encode())

def cmd(name, args):
    r = subprocess.run(args, text=True, capture_output=True)
    neu(B/name, '$ '+ ' '.join(args)+'\nExit: '+str(r.returncode)+'\nSTDOUT:\n'+r.stdout+'\nSTDERR:\n'+r.stderr)

for name, args in [
 ('KONFIGURATION-01.txt', ['hermes','config','get','model']),
 ('KONFIGPFAD-01.txt', ['hermes','config','path']),
 ('ANMELDUNGEN-01.txt', ['hermes','auth','list']),
 ('VERSION-01.txt', ['hermes','--version']),
 ('GATEWAY-01.txt', ['systemctl','--user','show','hermes-gateway.service','--property=ActiveState,SubState,FragmentPath,ExecStart']),
 ('ALTER-DIENST-01.txt', ['systemctl','show','hermes.service','--property=LoadState,ActiveState']),
 ('CLI-HILFE-01.txt',['hermes','--help'])]:
    cmd(name,args)

pfade = ['/root/.local/bin/hermes','/usr/local/lib/hermes-agent','/root/.hermes/config.yaml','/root/.hermes/state.db','/root/biotop','/root/biotop/daten/biotop.db','/opt/hermes','/root/Documents/Obsidian Vault']
neu(B/'PFADE-01.json',json.dumps({'zeit':datetime.now(timezone.utc).isoformat(),'abfrage':'Path.exists(), Path.resolve(), shutil.which(), os.environ (nur freigegebene Pfad-/Modellschluessel)', 'hermes_im_pfad':shutil.which('hermes'), 'pfade':[{'pfad':s,'existiert':Path(s).exists(),'aufgeloest':str(Path(s).resolve())} for s in pfade], 'umgebung':{k:os.environ.get(k) for k in ['HERMES_HOME','HERMES_PROFILE','HERMES_INFERENCE_MODEL','HERMES_INFERENCE_PROVIDER','OBSIDIAN_VAULT_PATH']}},indent=2))

c=sqlite3.connect('file:/root/biotop/daten/biotop.db?mode=ro',uri=True)
c.row_factory=sqlite3.Row
abfragen={
 'vorher_gesamt':'SELECT COUNT(*) AS anzahl, MAX(id) AS letzte_id, SUM(kosten_eur) AS kosten_eur FROM kasse',
 'laeufe':'SELECT lauf_id,COUNT(*) AS anzahl,SUM(kosten_eur) AS kosten_eur FROM kasse WHERE lauf_id BETWEEN 22 AND 25 GROUP BY lauf_id',
 'etappen22':"SELECT CASE WHEN id<=3411 THEN 'erste_etappe' ELSE 'fortsetzung' END AS abschnitt,COUNT(*) AS anzahl,SUM(kosten_eur) AS kosten_eur,MIN(id) AS erste_id,MAX(id) AS letzte_id,MIN(zeit) AS beginn,MAX(zeit) AS ende FROM kasse WHERE lauf_id=22 GROUP BY 1",
 'grenzzeilen':'SELECT id,lauf_id,zeit,zweck,kosten_eur FROM kasse WHERE lauf_id=22 AND (id>=3388 AND id<=3652)',
 'rohbestand':'SELECT id,lauf_id,zeit,zweck,kosten_eur FROM kasse WHERE lauf_id BETWEEN 22 AND 25 ORDER BY id'
}
ergebnis={k:{'sql':sql,'zeilen':[dict(x) for x in c.execute(sql)]} for k,sql in abfragen.items()}
neu(B/'KASSENABFRAGEN-01.json',json.dumps(ergebnis,indent=2,ensure_ascii=False))
# Decimal aus den aus SQLite gelesenen Einzelkosten, keine Differenz gerundeter Berichtszeilen.
roh=ergebnis['rohbestand']['zeilen']
gesamt=sum((Decimal(str(x['kosten_eur'])) for x in roh),Decimal(0))
erste=sum((Decimal(str(x['kosten_eur'])) for x in roh if x['lauf_id']==22 and x['id']<=3411),Decimal(0))
netto=gesamt-erste
neu(B/'KASSENRECHNUNG-01.json',json.dumps({'herkunft':'Rekonstruktion aus Kassenzeilen; Etappengrenze anhand Zweck und Zeitfenster, kein neuer Lauf', 'gesamt_22_bis_25':str(gesamt),'erste_etappe_22':str(erste),'netto_ohne_erste_etappe22':str(netto),'frei':str(Decimal(3)-netto),'anzahl_gesamt':len(roh),'anzahl_abzug':sum(x['lauf_id']==22 and x['id']<=3411 for x in roh),'anzahl_netto':sum(not(x['lauf_id']==22 and x['id']<=3411) for x in roh),'rundung_eichung':{'gruen':str(Decimal('0.5166083055555555').quantize(Decimal('.0001'))),'rot_angebliche_fortsetzung':str(Decimal('0.11884500925925925').quantize(Decimal('.0001'))),'behauptete_fortsetzung':'0.1190','maximaler_fehler_differenz_zweier_kaufmaennisch_auf_4_stellen_gerundeter_werte':'0.0001','gegenprobe_0.51665_rundet_auf_4_stellen':str(Decimal('0.51665').quantize(Decimal('.0001'),rounding='ROUND_HALF_UP'))}},indent=2))
for src,name in [(P/'biotop-phase-3-nachlauf/KASSE.md','QUELLE-KASSE-PHASE3-01.md'),(P/'biotop-phase-4-vorbedingung-1/NACHGANG-06.md','QUELLE-NACHGANG06-01.md')]:
    neu(B/name,src.read_bytes())
print((B/'KASSENRECHNUNG-01.json').read_text())
print('Vorbereitung ohne Modellaufruf abgeschlossen.')
