"""Runde2-Belege versiegeln; gescheiterte Abnahme bleibt rot, keine Produktänderung."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal
from collections import Counter
import json,hashlib,shutil,sqlite3,datetime,os,sys,grp,urllib.request,urllib.parse,xml.etree.ElementTree as ET,ast,subprocess,tarfile
P=Path('/root/reparatur-01');Q=Path('/root/biotop');R=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01');A=R/'ausgaben'
name=sys.argv[1];assert name in ('zwischenstand-11','eskalation-runde-02');final=name=='eskalation-runde-02'
O=R/name;assert not (O/'MANIFEST.sha256').exists();O.mkdir(mode=0o700,exist_ok=True)
u='https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/';url=u+name+'/'
zeit=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def lade(p):return json.loads(p.read_text())
def aus(n,z):(O/n).parent.mkdir(parents=True,exist_ok=True);(O/n).write_text(json.dumps(z,ensure_ascii=False,indent=2)+'\n')
aliasse={}
def abholbar(b):
 return O/Path(*[('PUNKTDATEI-'+x[1:]) if x.startswith('.') else x for x in b.relative_to(O).parts])
def kopie(a,b):
 assert a.is_file() and a.suffix not in ('.db','.sqlite','.pyc') and not a.is_symlink(),a
 original=str(b.relative_to(O));ziel=abholbar(b)
 if ziel!=b:aliasse[original]={'original':original,'download':str(ziel.relative_to(O)),'sha256':sha(a)}
 ziel.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a,ziel);assert sha(a)==sha(ziel)
def manifest_kopieren(d,ziel,erwartet=None):
 m=d/'SHA256SUMS';assert erwartet is None or sha(m)==erwartet
 lines=m.read_text().splitlines();namen=[]
 for line in lines:
  h,f=line.split(None,1);f=f.strip().removeprefix('*');p=d/f;assert p.resolve().is_relative_to(d.resolve()) and sha(p)==h,f
  namen.append(f);kopie(p,O/ziel/f)
 assert len(namen)==len(set(namen));kopie(m,O/ziel/'SHA256SUMS')
 return {'paket':ziel,'manifest_sha256':sha(m),'gepruefte_eintraege':len(namen)}
pakete=[manifest_kopieren(P/'nachbesserung-02/lieferung','lieferungen/aegis','f1df8c2d4f341cfaf58150a943ce101d84e26f0a30df9519447c6b730917fe8d'),manifest_kopieren(P/'nachbesserung-02/messung/lieferung','lieferungen/messung','1316c2e9ea914fb490225d7028eb2e6782f77046511f405e1b121dc8a16bfd3b'),manifest_kopieren(P/'nachbesserung-02/verbraucher/lieferung','lieferungen/verbraucher','1aabd4f67c79861e9c0e3a9f8e9f307a9798eba32d0ee45ecd979d41e34af6c0'),manifest_kopieren(P/'nachweis-leserpruefung-02/audit','audit-original')]
for d,z in [(P/'audit-elternabgleich','audit-elternabgleich'),(P/'review-03/repo','produktstand'),(P/'review-03/einzeldiffs','diffs')]:
 for f in sorted(d.rglob('*')):
  if f.is_file():kopie(f,O/z/f.relative_to(d))
for n in ['AUSSERHALB-KERN-BESTAETIGT-OFFEN.md','AUSSERHALB-KERN-BESTAETIGT-OFFEN.json']:kopie(P/'audit-elternabgleich'/n,O/n)
for n in ['QUELLHASHES.json','STATIK.json','AENDERUNGEN.diff','PRUEFGEGENSTAND.md','KERNGRENZE.json','PHASE-4-LUECKEN.md']:kopie(P/'review-03'/n,O/n)
for n in ['FASSUNG-7-SATZ.md','FASSUNG-7-SATZ.json','AUFTRAGGEBER-WORTLAUT.txt']:kopie(R/'auftragseingrenzung-02'/n,O/n)
kopie(R/'zwischenstand-08/MELDEREGEL-AUFTRAGGEBER.txt',O/'MELDEREGEL-AUFTRAGGEBER.txt')
kopie(P/'INTEGRATIONSENTSCHEIDUNG-RUNDE2.md',O/'INTEGRATIONSENTSCHEIDUNG-RUNDE2.md')
for f in sorted(A.iterdir()):
 if f.is_file() and f.name[:2].isdigit() and 53<=int(f.name[:2])<=63:kopie(f,O/'ausgaben'/f.name)
for n in ['aegis2_integrieren.py','leser2_integrieren.py','fokus_messen.py','suite_messen.py','skip_repro_lauf.py','vorspann_runde2_pruefen.py','cli_gate_kind.py','audit_elternabgleich.py','runde2_fehler_einordnen.py','review03_vorbereiten.py','runde2_paket.py']:kopie(P/n,O/'pruefscripte'/n)
# Quellbindung: gesamter aktueller Reviewstand, nur neun autorisierte Pfade verändert/neu.
quellen=lade(P/'review-03/QUELLHASHES.json');basis=lade(P/'nachbesserung-02/ELTERN-AUSGANG.json')
assert len(quellen)==129 and len(basis)==126
for z in quellen:assert sha(Q/z['pfad'])==z['sha256']==sha(abholbar(O/'produktstand'/z['pfad']))
neu=[z['pfad'] for z in quellen if z['pfad'] not in basis];geaendert=[f for f,z in basis.items() if sha(Q/f)!=z['sha256']]
assert len(neu)==3 and len(geaendert)==6
vor=ast.parse((P/'nachbesserung-02/verbraucher/lieferung/ausgang/biotop/lauf.py').read_text());nach=ast.parse((Q/'biotop/lauf.py').read_text())
for b in [vor,nach]:b.body=[z for z in b.body if not isinstance(z,(ast.FunctionDef,ast.AsyncFunctionDef)) or z.name!='_verhandeln']
assert ast.dump(vor)==ast.dump(nach)
# Elternläufe: äußeres rc UND JUnit, alle Kammeraufrufe nach Kennung zählen.
eltern=[];gesamt_kammer=[];gruppen=[]
for xml in sorted((O/'ausgaben').glob('*.xml')):
 st=xml.stem;meta=lade(O/'ausgaben'/(st+'.json'));ks=lade(O/'ausgaben'/(st+'-kammer.json'));tcs=list(ET.parse(xml).getroot().iter('testcase'));assert len(ks)==meta['kammerlaeufe']==len({z['container'] for z in ks})
 n=len(tcs);f=sum(t.find('failure') is not None for t in tcs);e=sum(t.find('error') is not None for t in tcs);s=sum(t.find('skipped') is not None for t in tcs)
 assert n==sum(int(x.get('tests','0')) for x in meta['testsuites'])
 eltern.append({'lauf':st,'rc':meta['rc'],'gesamt':n,'bestanden':n-f-e-s,'fehlgeschlagen':f,'errors':e,'skips':s,'kammern':len(ks),'fehlerfaelle':[t.get('classname')+'::'+t.get('name') for t in tcs if t.find('failure') is not None],'kernmass_pareto_zuerst':len(tcs)>=15 and all(t.get('classname')=='tests.test_kernmass_pareto' for t in tcs[:15])})
 gesamt_kammer.extend(ks);gruppen.append({'gruppe':'Eltern '+st,'kammern':len(ks)})
rr=next(x for x in eltern if x['lauf']=='58-leser2-eltern-rot');gg=next(x for x in eltern if x['lauf']=='59-leser2-eltern-gruen')
assert rr['rc']==1 and rr['errors']==rr['skips']==0 and gg['rc']==0 and rr['gesamt']==gg['gesamt']==gg['bestanden']==103
cli=lade(O/'ausgaben/63-vorspann-zweite-runde.json');cli['status']=cli['nachweis']['status'];cli['stderr']=(O/'ausgaben/63-vorspann-zweite-runde.stderr.txt').read_text();ck=lade(O/'ausgaben/63-vorspann-zweite-runde-kammer.json');ce=json.loads(cli['nachweis']['ergebnis']);assert len(ck)==cli['kammerlaeufe']==cli['gebuchte_kammern'] and all(cli['schutz'].values()) and cli['rc']==1 and cli['status']=='gescheitert' and cli['gen0_nachweis_verwendbar'] is False
assert cli['neue_modellbuchungen']==[];gesamt_kammer.extend(ck);gruppen.append({'gruppe':'Eltern63 echte Pflichtvorspann-CLI','kammern':len(ck)})
# Originale Lieferzähler: weder verschachtelte noch wiederholte JSON-Kopien doppelt zählen.
for d in sorted((P/'nachbesserung-02/lieferung/laeufe').iterdir()):
 if d.is_dir():ks=lade(d/'kammer.json');gesamt_kammer.extend(ks);gruppen.append({'gruppe':'Aegis '+d.name,'kammern':len(ks)})
M=P/'nachbesserung-02/messung/lieferung';messsum=0
for v in lade(M/'VERSUCHE.json'):
 fs=sorted((M/v['zaehlungsquelle']).glob('*.json'));assert len(fs)==v['rohzaehler_dateien'];ks=[k for f in fs for k in lade(f)['kammer']];assert len(ks)==v['kammerlaeufe'],v['label']
 messsum+=len(ks);gesamt_kammer.extend(ks);gruppen.append({'gruppe':'Messgerät '+v['label'],'kammern':len(ks)})
assert messsum==lade(M/'KENNZAHLEN.json')['archivierte_echte_kammeraufrufe']
VK=lade(P/'nachbesserung-02/verbraucher/lieferung/KAMMERZAEHLUNG.json');ks=VK['eintraege'];assert len(ks)==VK['gesamt']==VK['kern']+VK['quarantaene_gen0'];gesamt_kammer.extend(ks);gruppen.append({'gruppe':'Verbraucher, einschließlich nicht integrierter Quarantäne','kammern':len(ks),'kern':VK['kern'],'quarantaene':VK['quarantaene_gen0']})
ids=[x['container'] for x in gesamt_kammer];assert len(ids)==len(set(ids))==sum(x['kammern'] for x in gruppen)
aus('KAMMERBILANZ.json',{'schnitt':'Archivierte zweite-Runde-Arbeit der drei Implementierer plus Eltern53–63; keine Gesamtsumme des ganzen Auftrags','gruppen':gruppen,'archivierte_kammern':len(ids),'verschiedene_container':len(set(ids)),'kennungen':ids,'weiterer_abgeleiteter_nicht_roharchivierter_lauf':lade(M/'KENNZAHLEN.json')['abgeleiteter_weiterer_lauf_ohne_vollstaendigen_rohzaehler'],'lokalrepro55':'4 lokale pytest-Aufrufe an markierter Kammer-I/O-Grenze, keine Docker-Kammer; separat, nicht addiert'})
# Letzter gültiger Stand wird NICHT aus älteren grünen Versuchen gewählt.
suite=next(x for x in eltern if x['lauf']=='62-gesamtsuite-zweite-runde');assert (suite['rc'],suite['gesamt'],suite['bestanden'],suite['fehlgeschlagen'],suite['errors'],suite['skips'])==(1,305,303,2,0,0) and suite['kernmass_pareto_zuerst']
paare=[]
for schnitt,b in [('Vollsuite62',lade(O/'ausgaben/62-gesamtsuite-zweite-runde-eichpaare.json')),('Pflichtvorspann63',ce['eichproben'])]:
 for g,soll in [('proben',True),('gegenproben',False)]:
  assert len(b[g])==4
  for art,z in b[g].items():paare.append({'schnitt':schnitt,'gruppe':g,'art':art,'ausgefuehrt':z['ausgefuehrt'],'pruefbar':z['pruefbar'],'praedikat':z['bestanden'],'soll':soll,'gueltiges_sollurteil':z['ausgefuehrt'] is True and z['pruefbar'] is True and z['bestanden'] is soll,'grund':z.get('grund')})
for schnitt in ['Vollsuite62','Pflichtvorspann63']:
 assert sum(x['gueltiges_sollurteil'] for x in paare if x['schnitt']==schnitt and x['gruppe']=='proben')==1
 assert sum(x['gueltiges_sollurteil'] for x in paare if x['schnitt']==schnitt and x['gruppe']=='gegenproben')==4
ab=lade(P/'nachweis-leserpruefung-02/audit/ABDECKUNG.json');aussen=lade(P/'audit-elternabgleich/AUSSERHALB-KERN-BESTAETIGT-OFFEN.json');assert len(aussen)==19
review=None
if final:
 pakete.append(manifest_kopieren(P/'review-03/pruefer','schlussreview'))
 review=lade(P/'review-03/pruefer/REVIEW.json');assert review['passed'] is False
 for z in quellen:assert sha(Q/z['pfad'])==z['sha256']==sha(P/'review-03/repo'/z['pfad'])
aus('ABNAHME.json',{'zeit':zeit,'runde':2,'letzte_automatische_runde':True,'bestanden':False,'elternlaeufe':eltern,'aktuelle_vollsuite':suite,'aktuelle_paare':paare,'cli':{k:cli[k] for k in ['rc','status','gen0_nachweis_verwendbar','kammerlaeufe','gebuchte_kammern','neue_modellbuchungen','schutz','stderr']},'unabhaengiger_schlussreview':review,'schritt':'Eskalation, Entscheidung Philipp' if final else 'Elternabnahme rot, nur unabhängiger lesender Schlussbefund ausstehend','suchvollstaendigkeit':False,'quellen':{'nenner_ausgang':len(basis),'unveraendert':len(basis)-len(geaendert),'geaendert':geaendert,'neu':neu,'aktuell':len(quellen),'lauf_ast_ausser_verhandeln_unveraendert':True}})
aus('LIEFERABGLEICH.json',pakete)
# Kasse aus den beiden Datenbanken; unbekannte Trägerkosten bleiben NULL.
with sqlite3.connect('file:/root/biotop/daten/biotop.db?mode=ro',uri=True) as c:
 c.row_factory=sqlite3.Row;buch=[dict(z) for z in c.execute('SELECT * FROM kasse WHERE id>4070 ORDER BY id')];dbhash=hashlib.sha256('\n'.join(c.iterdump()).encode()).hexdigest()
kost=sum((Decimal(str(z['kosten_eur'])) for z in buch),Decimal(0));assert kost<=Decimal('5')
with sqlite3.connect('file:/root/.hermes/state.db?mode=ro',uri=True) as c:
 c.row_factory=sqlite3.Row;abzeit=datetime.datetime.fromisoformat(lade(A/'01-ausgang.json')['zeit']).timestamp();hm=[dict(z) for z in c.execute('SELECT id,parent_session_id,started_at,ended_at,billing_provider,billing_mode,cost_status,cost_source,actual_cost_usd,estimated_cost_usd,api_call_count FROM sessions WHERE id=? OR (parent_session_id=? AND started_at>=?) ORDER BY id',('20260920_063003_896e94ff','20260920_063003_896e94ff',abzeit))]
aus('KASSE.json',{'zeit':zeit,'budget_eur':'5.00','gebuchte_biotop_modellkosten_eur':str(kost),'neue_biotop_buchungen_ab4070':buch,'produktive_db_logischer_sha256':dbhash,'hermes_sitzungen':hm,'archivierte_kammern_zweite_runde':len(ids),'weitere_abgeleitete_kammer_ohne_rohzaehler':1,'abgrenzung':'Kein Euro-Gesamtbetrag für Träger/CPU/Host erhoben. NULL ist nicht gemessene Null. Keine vollständige Auftrags-Kammergesamtsumme behauptet. Frühere Aufwände bleiben unverändert erhalten.'})
(O/'KASSE.md').write_text(f'# Kasse — {name}\n\nStand UTC: {zeit}\n\n{len(buch)} neue Biotop-Buchungen seit ID4070; **{kost} € von 5,00 €** gebuchte Biotop-Modellkosten. Quelle: KASSE.json, direkte SQL-Abfrage. {len(hm)} abgefragte Eltern-/Kindsitzungsdatensätze sind beigelegt; eine unbekannte Träger-/Host-/CPU-Rechnung wird nicht als Null ausgewiesen.\n\n**Zweite-Runde-Schnitt:** {len(ids)} von {len(ids)} archivierten Docker-Kammerdatensätzen anhand eindeutiger Containerkennungen gezählt, disjunkte Gruppen und vollständige Kennungen in KAMMERBILANZ.json. Darin {VK["quarantaene_gen0"]} nicht integrierte quarantänisierte Gen0-Versuche; sie werden nicht aus dem Aufwand entfernt. Ein zusätzlicher Kammerlauf ist im Messgerätversuch05 nur aus Ausgabe ableitbar, ohne vollständigen Rohzähler: nicht still zu den archivalisch belegten Kammern addiert. Der lokale Repro55 liegt an markierter I/O-Grenze und ist keine Docker-Kammer. Keine globale Vollständigkeit der Kammerzählung über den gesamten mehrstufigen Auftrag behauptet.\n\nAlle frühere Rotversuche, Wiederholungen und Kosten bleiben in ihren unveränderten Vorgängerordnern. Die aktuelle Suite62 umfasst {suite["kammern"]} Kammern. CLI63 umfasst {len(ck)} gezählte und {cli["gebuchte_kammern"]} privat gebuchte Kammern; ihre interne Batterie ist darin enthalten und nicht zusätzlich zu zählen.\n')
status='**Kernabnahme gescheitert. Zweite und letzte automatische Runde beendet; Entscheidung liegt bei Philipp.**' if final else '**Kernabnahme nach zweiter Runde gescheitert; Produktänderungen gestoppt. Nur der unabhängige lesende Schlussbefund steht noch aus.**'
(O/'ZWISCHENBERICHT.md').write_text(f'''# Biotop Reparatur01 — {'Eskalation nach zweiter und letzter Runde' if final else 'Zwischenstand11, Elternabnahme rot'}

{zeit}

{status}

Keine Abnahme erbeten, keine natürliche Messfreigabe, keine dritte automatische Reparaturrunde. Die Schwellen und geforderten Sollurteile bleiben unverändert.

## Gemessener aktueller Stand

- **Vollsuite62 fehlgeschlagen: 303 von 305 Fällen bestanden, 2 von 305 Assertionfehler, 0 von 305 Errors, 0 von 305 Skips; äußerer Exit1.** Die 15 Kernmaß-/Paretofälle wurden tatsächlich zuerst ausgeführt und sind bestanden. Rohtext, JUnit, Quellhashes und {suite['kammern']} Kammerdatensätze liegen unter `ausgaben/62-*`.
- Fehlgeschlagen: `test_eichproben::test_vier_paare_am_kopierten_pruefwerk` und `test_review_vertrag::test_benannter_vertrag_am_kopierten_pruefwerk`. Keine Herabsetzung der Erwartungen oder neuer Produktpatch nach dieser roten Abnahme.
- **Eichbatterie62: 1 von 4 positiven Fällen gültig mit Sollurteil True, 3 von 4 positiven Fällen unprüfbar; 4 von 4 Gegenfällen gültig mit Sollurteil False.** Nebenwirkung und Regression werden durch den neuen Vollständigkeitswächter abgebrochen. Beim positiven Vertrag fehlt der angeforderte Laufzeitnachweis `bericht`. Diese Gründe belegen die Sperre, noch keine vollständig isolierte Wurzelursache. Insbesondere ist ein falsches Prädikat eines unprüfbaren positiven Falls keine erfolgreiche Gegenprobe.
- **Echte Pflichtvorspann-CLI63 fehlgeschlagen: Exit1, privater Status `gescheitert`, Gen0-Eingangsnachweis nicht verwendbar.** Wieder 1 von 4 gültigen positiven und 4 von 4 gültigen falschen Gegenfällen. {len(ck)} von {len(ck)} tatsächlichen Kammern mit Privatbuchungen abgeglichen; keine Modellbuchung. Die Rauschkalibrierung sperrte 0 von 4 Bereichen — das heilt die unbrauchbare Batterie nicht. Rohdaten einschließlich stderr unter `ausgaben/63-*`.
- Die {rr['gesamt']} neuen Messgeräte-/Verbraucher-Eigenfälle waren in Eltern58 gegen den vorherigen Stand zu {rr['fehlgeschlagen']} von {rr['gesamt']} rot, in Eltern59 zu {gg['bestanden']} von {gg['gesamt']} grün. Das ist ein isolierter Integrationsnachweis, **kein Ersatz** für die fehlgeschlagene Gesamtprüfung. Exakte Einzelzählungen in `ABNAHME.json`.
- Die F7-Anpassung des alten Vertrags-Eigentests ist als eigene Parent-Entscheidung dokumentiert: `INTEGRATIONSENTSCHEIDUNG-RUNDE2.md`. In Eltern60 scheiterten die drei veralteten Messhüllen-Erwartungen; in61 sind 6 von 6 Fälle grün. Positive Bestandsproben wurden dadurch nicht umdefiniert.

## Lieferumfang und Grenze

Vier ursprüngliche Arbeitspakete sind mit ihren unveränderten Prüfsummen aufgenommen: Aegis-Zeugenfix, Messgerät, Kernverbraucher und lesendes Originalaudit. Integration ausschließlich der erlaubten Kernpfade: {len(geaendert)} geänderte von {len(basis)} Ausgangsdateien, {len(neu)} neue Eigentestdateien, {len(basis)-len(geaendert)} von {len(basis)} Ausgangsdateien bytegleich. Aktueller vollständiger Quellstand: {len(quellen)} Dateien. In `lauf.py` ist der AST außerhalb `_verhandeln` identisch. Gen0-/Aufnahme-/Legacy-Außenfixes nicht integriert; die quarantänisierte Arbeit bleibt sichtbar und im Aufwand.

Der grüne Aegis-Teilstand57 (202 von202, vier gültige Paare) bleibt historisch richtig, ist aber **nicht** der aktuelle Gesamtstand. Er gilt nicht als Freigabe nach Messgeräte-/Verbraucherintegration. Kein veröffentlichter Vorgänger wurde geändert.

Auslieferungskorrektur gegenüber Zwischenstand10: seine beiden `.gitignore`-Adressen lieferten404. Dieser neue Ordner hält die Originalbytes unter benannten Downloadaliasen und mit Originalpfaden in `PUNKTDATEIEN.tar.gz`; siehe `AUSLIEFERUNGSKORREKTUR.md`, `DOWNLOAD-ZUORDNUNG.json` und `PUNKTDATEIEN-WIEDERHERSTELLEN.md`. Der alte Fehlversuch bleibt benannt; keine Serverregel wurde gelockert.

## Suchabdeckung und offene Außenliste

Originalaudit: {ab['inventar_dateien']} von {ab['inventar_dateien']} inventarisierten Dateien als gelesen dokumentiert, {ab['semantische_lesebloecke']} Leserblöcke, {ab['deduplizierte_bestaetigte_mechanismen']} Mechanismusgruppen. Parent prüfte die Quellhashes aller Dateien und die exakten Quellzitate aller Leserblöcke sowie alle ID-Verweise und disjunkten Summen. Das beweist Integrität der Auditzuordnung, nicht lückenlose semantische Fehlerfreiheit.

**Suche weiterhin unvollständig:** acht semantische Kandidaten und45 breite Kandidatenzeilen ohne abgeschlossene Feinzuordnung bleiben offen. Diese beiden Populationen sind nicht zu einer Fehlerzahl zu addieren. Die661 ursprünglichen Suchzeilen sind keine661 Fehler. Keine Entwarnung aus Abwesenheit weiterer Funde.

`AUSSERHALB-KERN-BESTAETIGT-OFFEN.md/.json` enthält **19 bestätigte Leserorte**, ausdrücklich offen: die ursprünglichen11 Orte in11 nichtproduktiven Prüfskripten plus8 weitere Orte in3 Produktdateien, die nach der Nutzergrenze außerhalb dieser Reparatur bleiben. Statische Bestätigung wird nicht als ausgeführter Repro ausgegeben. Originalkategorien bleiben unverändert; die engere Parent-Arbeitszuordnung steht daneben in `audit-elternabgleich/`, inklusive Verbraucher-Aliassen statt Doppelzählung.

Die vier früheren Phase4-Lücken bleiben ausdrücklich ungelöst und sind separat in `PHASE-4-LUECKEN.md` erhalten. Keine Behauptung, sie seien widerlegt oder repariert.

## Unabhängige Nachprüfung und Entscheidung

{'Der separate Schlussbefund liegt unter schlussreview/; sein passed-Feld ist false. Er ist eine lesende Nachprüfung des aktuellen integrierten Stands, kein weiterer Fixzyklus. Seine Grenzen und nicht verifizierten Aspekte bleiben erhalten.' if final else 'Ein eigener unabhängiger Kontext prüft nur lesend den eingefrorenen aktuellen Diff und die vorhandenen Ausführungsbelege. Kein Fixauftrag und keine neuen Werk-/Modellläufe. Dieser Zwischenstand nimmt sein Urteil nicht vorweg.'}

**Eigene Empfehlung des Parents für die Entscheidung:** einen getrennten, eng begrenzten Folgeauftrag zur Ursachenisolierung und Reparatur der verbliebenen Kern-Inkompatibilität freigeben; erst danach dieselbe Bestandsbatterie und Pflichtvorspannroute erneut abnehmen. Kein Schwellenabbau, keine automatische Wahl eines bequemeren Prüfgegenstands und keine pauschale Ausweitung auf die Außenliste. Ohne Freigabe keine weitere automatische Produktänderung.

Kasse: {kost} € von5,00 € gebuchte Biotop-Modellkosten, {len(buch)} neue Buchungen. Sonstige Kosten nicht als Null behauptet; KASSE.md/.json und KAMMERBILANZ.json enthalten Schnitt und Lücken.

Dateien: {url}DATEIEN.txt
Bericht: {url}ZWISCHENBERICHT.md
Manifest: {url}MANIFEST.sha256
Prüfsumme: {url}PRUEFSUMME-ORDNER.txt
Kasse: {url}KASSE.md
''')
# Berichtszahlen werden gegen vollständige JUnit-Auswertung abgesichert.
assert (rr['gesamt'],rr['fehlgeschlagen'],gg['gesamt'],gg['bestanden'])==(103,82,103,103),(rr,gg)
(O/'OFFENE_PUNKTE.md').write_text('# Offen, nicht erledigt\n\n1. Aktueller Kern: zwei gescheiterte Bestands-Eigentests / drei unprüfbare positive Eichfälle; echte Pflichtvorspannroute gesperrt. Ursachen nicht durch bloßes Exit1 festgelegt; keine automatische Nachbesserung mehr.\n2. Entscheidung Philipp über gesonderten Kern-Folgeauftrag.\n3. Unabhängiges Schlussreview: '+('abgeschlossen negativ, siehe schlussreview/BERICHT.md.\n' if final else 'nur lesend beauftragt, noch nicht abgeschlossen.\n')+'4. Alle19 benannten Außenleserorte bleiben bestätigt offen; keine Außenreparatur übernommen.\n5. Vier Phase4-Mechanismen ungelöst (separate Liste).\n6. Acht semantische Kandidaten und45 nicht feinzugeordnete Quellzeilen des Inventaraudits bleiben ungeklärt; keine Vollständigkeitsentwarnung.\n7. Ein Messgeräte-Kammerlauf ohne vollständigen Rohzähler; kein auftragsgenauer Träger-/Host-Euro-Gesamtbetrag vorhanden.\n8. Keine neue natürliche Wirkungsmessung und keine Freigabe für Fortsetzung alter Läufe.\n')
(O/'VORGAENGER.json').write_text(json.dumps([{'ordner':n,'manifest':u+n+'/MANIFEST.sha256','sha256':sha(R/n/'MANIFEST.sha256')} for n in ['auftragseingrenzung-02','zwischenstand-08','zwischenstand-09','zwischenstand-10']],ensure_ascii=False,indent=2)+'\n')
assert len(aliasse)>=2
with tarfile.open(O/'PUNKTDATEIEN.tar.gz','w:gz') as tar:
 for original,z in sorted(aliasse.items()):tar.add(O/z['download'],arcname=original,recursive=False)
with tarfile.open(O/'PUNKTDATEIEN.tar.gz','r:gz') as tar:
 assert set(tar.getnames())==set(aliasse)
 for original,z in aliasse.items():assert hashlib.sha256(tar.extractfile(original).read()).hexdigest()==z['sha256']
aus('DOWNLOAD-ZUORDNUNG.json',list(aliasse.values()))
(O/'PUNKTDATEIEN-WIEDERHERSTELLEN.md').write_text('# Unveränderte Originalnamen wiederherstellen\n\nPunktdateien lieferten bei der HTTPS-Abholung404. Deshalb liegen ihre unveränderten Bytes unter expliziten PUNKTDATEI-Aliasnamen und zusätzlich mit den Originalnamen im PUNKTDATEIEN.tar.gz. DOWNLOAD-ZUORDNUNG.json bindet Originalpfad, abholbaren Alias und SHA256. Keine Quelldatei wurde inhaltlich verändert.\n\nFür einen lokalen Originalbaum: im heruntergeladenen Ordner `tar -xzf PUNKTDATEIEN.tar.gz` ausführen. Danach sind die Originalpfade wieder vorhanden; auch audit-original/SHA256SUMS kann dann unverändert geprüft werden. Das äußere Manifest bindet weiterhin die Aliasdateien und das Archiv.\n')
alt_https=lade(P/'zwischenstand-10-https.json');probleme=[z for z in alt_https if not z['bytegleich']]
assert len(probleme)==2
kopie(P/'zwischenstand-10-https.json',O/'VORHERIGE-HTTPS-PRUEFUNG.json')
(O/'AUSLIEFERUNGSKORREKTUR.md').write_text(f'# Auslieferungskorrektur gegenüber Zwischenstand10\n\nZwischenstand10 war nicht vollständig abholbar: {sum(z["bytegleich"] for z in alt_https)} von {len(alt_https)} HTTPS-Abrufen waren bytegleich; die beiden .gitignore-Adressen lieferten404. Seine bereits versiegelten Dateien bleiben unverändert.\n\nDieser neue Ordner erhält alle Originalbytes unter expliziten Downloadaliasen und in PUNKTDATEIEN.tar.gz mit den Originalpfaden; siehe DOWNLOAD-ZUORDNUNG.json. Keine Serverkonfiguration wurde geändert. Der Fehlversuch wird nicht als erfolgreiche Vollveröffentlichung gewertet.\n\nBei der Vorbereitung waren außerdem ein falscher Inventarpfad und die Verwechslung von Kurz-Ausgabe und Rohdaten-Schema (Status, Buchungsliste, stderr-Datei) zu korrigieren. Diese Paketbauer-Aufrufe scheiterten vor der Versiegelung; die fehlerhaften Stellen wurden nicht übergangen. Keine Produktdatei, keine Messausgabe und kein Test-Sollurteil wurde dafür verändert; keine zusätzliche Kammer gestartet.\n')
files=sorted([str(p.relative_to(O)) for p in O.rglob('*') if p.is_file()]+['DATEIEN.txt']);assert len(files)==len(set(files))
(O/'DATEIEN.txt').write_text(f'{name} — Kernabnahme fehlgeschlagen, kein grüner Abschluss.\n'+''.join(f+'\n' for f in files)+'MANIFEST.sha256\nPRUEFSUMME-ORDNER.txt\n')
(O/'MANIFEST.sha256').write_text(''.join(sha(O/f)+'  '+f+'\n' for f in files));digest=sha(O/'MANIFEST.sha256')
(O/'PRUEFSUMME-ORDNER.txt').write_text(f'SHA-256 von MANIFEST.sha256: {digest}\n{len(files)} Nutzdateien plus2 Prüfhüllen.\n')
gid=grp.getgrnam('caddy').gr_gid
for p in [O]+list(O.rglob('*')):os.chown(p,0,gid);os.chmod(p,0o750 if p.is_dir() else 0o640)
def abholen(f):
 for versuch in range(3):
  try:
   with urllib.request.urlopen(url+urllib.parse.quote(f,safe='/'),timeout=45) as r:b=r.read();status=r.status
   return {'datei':f,'http':status,'bytegleich':status==200 and hashlib.sha256(b).hexdigest()==sha(O/f)}
  except Exception as e:
   if versuch==2:return {'datei':f,'bytegleich':False,'fehler':str(e)}
with ThreadPoolExecutor(max_workers=12) as ex:checks=list(ex.map(abholen,files+['MANIFEST.sha256','PRUEFSUMME-ORDNER.txt']))
(P/(name+'-https.json')).write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');assert all(x['bytegleich'] for x in checks),[x for x in checks if not x['bytegleich']]
print(json.dumps({'ordner':str(O),'dateien':url+'DATEIEN.txt','manifest_sha256':digest,'nutzdateien':len(files),'https_geprueft':len(checks),'https_bytegleich':sum(x['bytegleich'] for x in checks),'kern_bestanden':False,'finale_eskalation':final,'archivierte_kammern_runde2':len(ids),'offene_aussenorte':len(aussen),'kosten_eur':str(kost)},ensure_ascii=False))
