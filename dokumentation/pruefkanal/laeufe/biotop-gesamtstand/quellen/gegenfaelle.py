"""Vier ausdrücklich gestellte Reproduktionen am unveränderten Code.
Nur Container/In-Memory-DB; keine produktive DB, keine Modellaufrufe.
Diese Fälle sind NEUE Bestandsaufnahme-Proben, keine vorher vorhandene Testsuite.
"""
import ast,json,sqlite3,re
from pathlib import Path
from unittest.mock import patch
from types import SimpleNamespace
from biotop.organe import aegis,gedaechtnis as G,generation0 as G0
from biotop.kern import protokoll
out=[]
# P1: Original-Prüflambda, ohne Neuimplementierung; gestellter Gegenfall.
src=Path('/quelle/biotop/organe/eichproben.py').read_text(); tree=ast.parse(src)
node=next(n for n in ast.walk(tree) if isinstance(n,ast.Lambda) and n.lineno==188)
fn=eval(compile(ast.Expression(node),'<Original Normlambda Z188>','eval'),{'rel_test':'tests/test_norm_eichung.py'})
u={'status':'abgelehnt','grund':'Messung hat gar nicht stattgefunden','mass':None,'norm':[]}
r=fn(u)
out.append({'id':'P1','art':'gestelltes ungemessenes Urteil an Original-Lambda','soll':'nicht bestanden','ist':r,'abweichung_bestaetigt':r[0] is True})
# P2: Original C/Schlüssel/Vorrats-/Protokollfunktionen, nur frische SQLite im Speicher.
c=sqlite3.connect(':memory:',isolation_level=None);c.row_factory=sqlite3.Row
c.executescript('CREATE TABLE immunsystem(id INTEGER PRIMARY KEY,werk_id INTEGER,bereich TEXT,ursprung TEXT); CREATE TABLE protokoll(nr INTEGER PRIMARY KEY,zeit TEXT,art TEXT,inhalt TEXT,hash_vor TEXT,hash TEXT);')
code='from werk.bereich import ziel\ndef test_neu():\n    assert ziel() == 1\n'
key=aegis.behauptung(code,'test_neu','werk')
vor=aegis.aufnahmesperre(c,1,1,'bereich',code,['test_neu'],'werk',1,'fund')
protokoll.schreiben(c,'aegis.ansage',lauf_id=1,bereich='bereich',behauptung=key,ausgefuehrt=True,bisherige=0)
nach=aegis.aufnahmesperre(c,1,1,'bereich',code,['test_neu'],'werk',1,'fund')
out.append({'id':'P2','art':'gestellte Ansage, kein Modellaufruf, leerer Immunbestand','schluessel':key,'ohne_eigene_ansage':vor,'mit_eigener_frischer_ansage':nach,'soll':'erster neuer Test in beiden Fällen aufnehmen','abweichung_bestaetigt':len(vor[0])==1 and len(nach[1])==1,'immunzeilen':c.execute('SELECT count(*) FROM immunsystem').fetchone()[0]})
# P3: Nur Speicherzugriff ersetzt; tatsächliche art_text-Auswahl unverändert ausgeführt.
def row(i,werk):
 return {'id':i,'werk':werk,'lauf_id':1,'generation':1,'bereich':'bereich','nische':'sicher','kategorie':'korrektheit','ergebnis':'angenommen','zuwachs':1,'laufzeit_prozent':0,'beschreibung':'Prüfbestand','muster':f'Verschiedenes geprüftes Muster {i}','werkklasse':'probe'}
eigen=[row(i,'eigen') for i in range(1,26)]; fremd=[row(i,'fremd') for i in range(101,126)]
def lesen(con,klasse,limit,werk=None,nur_angenommen=False): return (eigen if werk=='eigen' else eigen+fremd)[:limit]
with patch.object(G,'werkklasse',return_value='probe'),patch.object(G,'werkname',return_value='eigen'),patch.object(G,'art_lesen',side_effect=lesen):
 text=G.art_text(None,1)
a,b=text.split('ANDERE WERKE',1); ne=len(re.findall(r'^\[A\d+\]',a,re.M)); nf=len(re.findall(r'^\[A\d+\]',b,re.M))
out.append({'id':'P3','art':'gestellter Bestand 25 eigene+25 fremde Einträge, Original art_text','eigene_gezeigt':ne,'fremde_gezeigt':nf,'gesamt_gezeigt':ne+nf,'anteil_fremd':nf/(ne+nf),'soll':'mindestens 0.5 bei genügend Bestand','abweichung_bestaetigt':nf/(ne+nf)<0.5,'vorlage':text})
# P4: Ausschließlich Ergebnisform des fehlenden Beobachters als Test-Doppel.
# Keine echte Modell-/APIantwort, kein Ersatz für einen fehlgeschlagenen Netzaufruf.
mut=[{'datei':'werk/bereich/a.py','code':'x=2\n','beschreibung':'gestellter Mutant','zeile':1}]
with patch.object(G0.kammer,'ausfuehren',return_value=SimpleNamespace(rc=0,stdout='AEQ keine-beobachtung\n',stderr='')),patch.object(G0,'_testlauf',return_value=(False,'')):
 result=G0.aequivalenz_pruefen(c,1,Path('/nicht-benoetigt'),'# kein Beobachter',mut)
out.append({'id':'P4','art':'gestellter Kammer-Test-Doppel ohne Beobachtungsfunktion, Original aequivalenz_pruefen','soll':'nicht äquivalent / unprüfbar','ist':result,'abweichung_bestaetigt':result[0]['aequivalent'] is True})
print(json.dumps({'hinweis':'Vier gestellte lokale Gegenfälle, keine neue Hebung, kein Nachweis einer natürlichen Fehlerrate','faelle':out,'bestaetigte_codeabweichungen':sum(x['abweichung_bestaetigt'] for x in out),'gepruefte_faelle':len(out)},ensure_ascii=False,indent=2))
assert all(x['abweichung_bestaetigt'] for x in out), 'Mindestens eine erwartete Codeabweichung wurde NICHT reproduziert'
