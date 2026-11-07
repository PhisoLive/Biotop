"""Read-only discovery; never reads credential tables or writes the source DB."""
import ast
import collections
import json
import re
import sqlite3
from pathlib import Path

root = Path(__file__).resolve().parent
con = sqlite3.connect('file:/root/reparatur-01/ausgang.db?mode=ro&immutable=1', uri=True)
con.row_factory = sqlite3.Row
ks = {r['id']: dict(r) for r in con.execute('SELECT id,lauf_id,generation,bereich,nische,anbieter,modell,ist_probe,status,erstellt_am FROM kandidaten')}
ims = [dict(r) for r in con.execute('SELECT * FROM immunsystem ORDER BY id')]
print('Candidate models', collections.Counter((k['anbieter'],k['modell']) for k in ks.values()))
print('Probe candidates', [k for k in ks.values() if k['ist_probe'] or 'hermes' in ((k['anbieter'] or '')+' '+(k['modell'] or '')).lower() or 'eich' in (k['modell'] or '').lower()])
print('Immunity binding counts', collections.Counter(bool(re.search(r'Kandidat (\d+)',r['ursprung'] or '')) for r in ims))
print('No candidate origin', [{k:r[k] for k in ['id','name','werk_id','lauf_id','generation','ursprung']} for r in ims if not re.search(r'Kandidat (\d+)',r['ursprung'] or '')])
print('Immune rows 280+', [{k:r[k] for k in ['id','name','werk_id','lauf_id','generation','erstellt_am']} for r in ims if r['id']>=280])
print('Art accepted pools', list(map(tuple,con.execute("SELECT werk,ergebnis,count(*),sum(trim(coalesce(muster,''))!='') FROM artgedaechtnis GROUP BY werk,ergebnis"))))
print('Admission events', [dict(r) for r in con.execute("SELECT nr,zeit,art,inhalt FROM protokoll WHERE art IN ('immun.aufnahme_geprueft','immun.aufnahme_gesperrt','aegis.abweichung')")])
print('Immunity lineage events', [dict(r) for r in con.execute("SELECT nr,zeit,art,inhalt FROM protokoll WHERE art IN ('immun.behauptung_nachgetragen','immun.uebernommen','immun.neubewertet','immun.verworfen')")])
