"""Lesende Elternprüfung der historischen SQL-Abfragen; keine Neuvermessung."""
from pathlib import Path
from decimal import Decimal
import sqlite3,json,hashlib
Q=Path('/root/reparatur-01/teil-historie');D=Path('/root/reparatur-01/ausgang.db')
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
c=sqlite3.connect(f'file:{D}?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
vorher=hashlib.sha256(D.read_bytes()).hexdigest();buf='';abfragen=[]
for line in (Q/'status-abfragen.sql').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('--'):continue
    buf+=line+'\n'
    if sqlite3.complete_statement(buf):
        assert buf.lstrip().upper().startswith('SELECT ')
        rows=[dict(r) for r in c.execute(buf)]
        abfragen.append({'sql':buf.strip(),'zeilen':len(rows),'ergebnis':rows});buf=''
assert not buf.strip()
vergleich=json.loads((Q/'VERIFIKATION.json').read_text())
assert len(abfragen)==vergleich['sql_abfragen']
assert [a['zeilen'] for a in abfragen]==vergleich['sql_zeilen']
laeufe=[]
for lid in (24,25):
    lauf=dict(c.execute('SELECT id,werk_id,status,beendet_am,budget_eur FROM laeufe WHERE id=?',(lid,)).fetchone())
    gens=[dict(r) for r in c.execute('SELECT nummer,status FROM generationen WHERE lauf_id=? ORDER BY nummer',(lid,))]
    geld=[dict(r) for r in c.execute('SELECT id,kosten_eur FROM kasse WHERE lauf_id=? ORDER BY id',(lid,))]
    summe=sum((Decimal(str(r['kosten_eur'])) for r in geld),Decimal(0))
    laeufe.append({**lauf,'generationen':gens,'buchungen':len(geld),'erste_id':geld[0]['id'],'letzte_id':geld[-1]['id'],
                    'kosten_eur_roh':str(summe),'kosten_eur_6_nachkommastellen':str(summe.quantize(Decimal('0.000001'))),
                    'eichung_zeilen':c.execute('SELECT count(*) FROM eichung WHERE lauf_id=?',(lid,)).fetchone()[0],
                    'eichkosten_zeilen':c.execute('SELECT count(*) FROM eichkosten WHERE lauf_id=?',(lid,)).fetchone()[0]})
nachher=hashlib.sha256(D.read_bytes()).hexdigest();assert vorher==nachher
r={'art':'historische Datenbank-Nachprüfung, keine heutige Messung, kein Lauf-/Freigabestatus verändert','db_sha256':vorher,
    'unveraendert':vorher==nachher,'sql_abfragen':len(abfragen),'abfragen':abfragen,'laeufe':laeufe}
(O/'35-historie-elternpruefung.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'unveraendert':r['unveraendert'],'sql_abfragen':len(abfragen),'zeilen':[a['zeilen'] for a in abfragen],'laeufe':laeufe},ensure_ascii=False,indent=2))
