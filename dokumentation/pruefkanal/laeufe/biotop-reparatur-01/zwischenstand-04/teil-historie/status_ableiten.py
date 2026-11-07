#!/usr/bin/env python3
"""Nur lokale Datenauswertung + SELECT; keine Biotop-Imports/Tests/Netzaufrufe.
Erzeugt den maschinenlesbaren Status der HISTORISCHEN Läufe, keine Statusänderung.
"""
import collections, datetime, hashlib, json, pathlib, sqlite3
from decimal import Decimal
O=pathlib.Path(__file__).resolve().parent
D=pathlib.Path('/root/reparatur-01/ausgang.db')
HEAD='b42dc941e7fcb66632ba6a0e13b8df106a270a31'
def load(f): return json.loads((O/f).read_text())
def save(f,v): (O/f).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def total(rs): return str(sum((Decimal(str(r['kosten_eur'])) for r in rs),Decimal(0)))
a=load('auswertung.json'); n=load('nachrechnung.json'); g=load('generationen.json'); k=load('kandidaten.json'); e=load('protokoll_sicher.json'); cash=load('kasse.json')
by_nr={r['nr']:r for r in e}
con=sqlite3.connect(D.as_uri()+'?mode=ro',uri=True);con.row_factory=sqlite3.Row;con.execute('PRAGMA query_only=ON')
status={
 'erstellt_am_utc':datetime.datetime.now(datetime.UTC).isoformat(),
 'umfang':{'laeufe':[24,25],'bauteile':['A','B','C'],'kontextlaeufe':[22,23],'snapshot':str(D),'snapshot_sha256':hashlib.sha256(D.read_bytes()).hexdigest(),'quellstand':HEAD,'lesemodus':'SQLite mode=ro + PRAGMA query_only=ON','produktive_ausfuehrung':False,'neue_tests':False,'neue_modellaufrufe':0,'db_statusaenderungen':0,'beweisgrenze':'Historischer Snapshot; keine heutige Lauf-Freigabe, keine Liveness-Behauptung. Gitzeiten sind Versionsmetadaten, keine Ereigniszeiten.'},
 'nutzerentscheidungen':load('nutzerentscheidungen.json'),
 'verbindliche_wertungen':{
  'normzeile':'zurueckgenommen; kein bestandener Normnachweis',
  'nachlauf_vier_von_vier':'zurueckgenommen; leere Normprüfung norm=[], zuwachs=None',
  'laeufe22_23_einschliesslich_54_5_prozent':'unter Vorbehalt wegen Satz-2-Verstoss; keine Rehabilitierung und kein Austausch des historischen Werts durch andere Nenner',
  'abnahme_frueher':'Historische enge Mechanikabnahme bleibt als Ereignis erhalten; keine natürliche C- oder vollständige Integrationsabnahme. Jüngster Reparaturauftrag vor weiterer Messung ist verbindlich.',
  'daten_aendern':'Keine Löschung oder Statusänderung beauftragt/ausgeführt. Allenfalls Empfehlung: Vergleichsfreigabe aussetzen und nach Messgerätänderungen neue Lauf-IDs verwenden.'},
 'laeufe':[], 'bauteile':{}, 'berichtskorrekturen':[],
 'werkstaende':load('werkstaende.json'),'quellstaende':load('quellstaende.json')
}
chron_ids=set(r['nr'] for r in load('ereignisse-belegauswahl.json'))
for lid in (24,25):
 s=a[str(lid)]; run=s['lauf']; begin=run['begonnen_am']
 re=[r for r in e if r['inhalt'].get('lauf_id')==lid and r['zeit']>=begin]
 candidates=[r for r in k if r['lauf_id']==lid]; gens=[r for r in g if r['lauf_id']==lid]
 regular_ids=sorted({q['kandidat'] for gr in gens for key,vl in (gr.get('kandidaten') or {}).items() if not key.startswith('_') for q in vl})
 extra=[r for r in candidates if r['id'] not in regular_ids]
 generation_rows=[]
 for gr in gens:
  rr={key:gr.get(key) for key in ('id','lauf_id','nummer','status','erstellt_am','freigabe_am','grund','tag','pruefsumme')}
  rr['auswahl']=(gr.get('kandidaten') or {}).get('_gewaehlt')
  rr['ereignisse']=[r for r in re if r['art'] in ('generation.begonnen','generation.ergebnis','freigabe.frei') and r['inhalt'].get('nummer')==gr['nummer']]
  chron_ids.update(r['nr'] for r in rr['ereignisse'])
  generation_rows.append(rr)
 calls={r['nr'] for r in re if r['art']=='modell.aufruf'}
 answers=[r for r in re if r['art']=='modell.antwort']; answer_refs={r['inhalt']['aufruf_nr'] for r in answers}
 ansage_cash=[r for r in cash if r['lauf_id']==lid and r['zweck'].startswith('aegis.ansage.')]
 attack_cash=[r for r in cash if r['lauf_id']==lid and r['zweck'].startswith('aegis.angriff.')]
 pairs=[{'antwort_nr':r['nr'],'aufruf_nr':r['inhalt']['aufruf_nr'],'zeit':r['zeit']} for r in answers]
 natural_urteile=[r for r in re if r['art']=='aegis.urteil' and r['nr']<16010 and (r['inhalt'].get('angriff') or {}).get('modell')]
 cprobes=[r for r in re if r['nr']>=16010 and r['art']=='immun.aufnahme_geprueft']
 cblocked=[r for r in re if r['nr']>=16010 and r['art']=='immun.aufnahme_gesperrt']
 fixture_verdicts=[r for r in re if r['nr']>=16010 and r['art']=='aegis.urteil']
 cr={'lauf_id':lid,'werk_id':run['werk_id'],'db_status':run['status'],'beendet_am':run['beendet_am'],'begonnen_am':begin,
     'bewertung':'Historischer Versuch und Einzelergebnisse belegt; keine pauschale Verwerfung, keine aktuelle Gesamt-/Vergleichsfreigabe',
     'evolutionaere_generationen':len([r for r in gens if r['nummer']>0]),'generation0_getrennt':1,'generationen':generation_rows,
     'kandidaten':{'tabellenzahl':len(candidates),'regulaere_generationsteilnehmer':len(regular_ids),'regulaere_ids':regular_ids,'zusaetzliche_kandidaten':extra,'aktuell_markierte_proben':[r['id'] for r in candidates if r['ist_probe']]},
     'mass':run['mass'],'eichung_tabellenzahl':sum(r['lauf_id']==lid for r in load('eichung.json')),'eichkosten_tabellenzahl':sum(r['lauf_id']==lid for r in load('eichkosten.json')),'eichereignisse':[r for r in re if r['art'].startswith(('eichprobe.','eichung.'))],
     'kosten':s['kasse']|{'budget_eur':str(run['budget_eur']),'anteil_prozent':str(Decimal(s['kasse']['summe_eur_decimal'])/Decimal(str(run['budget_eur']))*100)},
     'modellaufrufe':{'versuche':len(calls),'antworten':len(answers),'antworten_mit_echter_aufruf_id':len(calls&answer_refs),'fehler':[r for r in re if r['art']=='modell.fehler'],'unbeantwortet':sorted(calls-answer_refs),'fremde_antwortreferenzen':sorted(answer_refs-calls),'zuordnung':pairs},
     'A':n[str(lid)]['ansagen']|{'entscheidungsrekonstruktion':load('A-rekonstruktion.json')['pro_lauf'][str(lid)],'ansagekosten_eur':total(ansage_cash),'angriffskosten_eur':total(attack_cash),'ansage_kassen_ids':[r['id'] for r in ansage_cash],'angriff_kassen_ids':[r['id'] for r in attack_cash],'kostenersparnis_nachgewiesen':False},
     'natuerliche_angriffsbelege':{'urteile':natural_urteile,'urteile_mit_angriffsmodell':len(natural_urteile),'summe_feld_angriff_gesamt':sum(r['inhalt']['angriff'].get('gesamt',0) for r in natural_urteile),'neue_immunsystemeintraege':n[str(lid)]['immunsystem']['neu_gen_gt_0'],'definition':'Feldsumme gesamt zählt in diesen Urteilen erfasste Angriffstest-Ausführungen; weder neue Fundzeilen noch normativer Tor-2-Nenner.'},
     'natuerliche_C_aufrufe':len(n[str(lid)]['natuerliche_C_pruefungen']),
     'gestellte_C_proben':{'verdict_ereignisse':fixture_verdicts,'anzahl_verdict_durchlaeufe':len(fixture_verdicts),'kandidatenids_im_protokoll':sorted({r['inhalt']['kandidat'] for r in fixture_verdicts}),'id_ist_keine_anzahl_distinkter_gegenstaende':True,'C_aufrufe':cprobes,'C_sperrungen':cblocked,'C_pruefungen_anzahl':len(cprobes),'C_testdurchlaeufe':sum(r['inhalt']['anzahl'] for r in cprobes),'C_sperrungen_anzahl':len(cblocked),'verschiedene_schluesselfaelle':sorted({(r['inhalt']['bereich'],r['inhalt']['behauptung']) for r in cblocked}),'verschiedene_stelle_schluessel_kombinationen':sorted({(r['inhalt']['sperrart'],r['inhalt']['bereich'],r['inhalt']['behauptung']) for r in cblocked}),'V9_ereignisse':[r for r in re if r['art']=='aegis.abweichung']}}
 assert cr['evolutionaere_generationen']==4 and len(regular_ids)==128
 assert calls==answer_refs and len(answers)==len(calls)==s['kasse']['anzahl']
 assert cr['eichung_tabellenzahl']==cr['eichkosten_tabellenzahl']==0
 status['laeufe'].append(cr)
 chron_ids.update(r['nr'] for r in re if r['art'] in ('lauf.angelegt','mass.eingefroren','immun.uebernommen','immun.neubewertet','mentor.richtungen','aegis.abweichung'))
status['bauteile']={
 'A':{'gebaut':True,'historisch_natuerlich_benutzt':True,'gilt':'Exakte Ansagesperre + Verzichtsentscheidungen; alle 50 Entscheidungen mit Originalfunktion auf Entscheidungszeit rekonstruiert. Keine Fehl-/Durchlassentscheidung gegen den so rekonstruierten Ansagevorrat.','gilt_nicht':'Doppelungsverhinderung bei tatsächlicher Aufnahme; Rückgang alter Doppelungsquote A allein zurechnen; sichere Nettokostenersparnis.','aufnahmen_lauf24':{'neue_eintraege':3,'fund_eintraege':2,'norm_eintraege':1,'vorrat_doppelnde_eintraege':[337,338],'nicht_vorrat_doppelnd':[339],'beleg':'immun-schluessel.json; Originalableitung behauptung, Vergleich gegen vor Beginn übernommene Schlüssel, nicht gegen Endbestand.'},'grenze':'Ansagevorrat-Rekonstruktion nutzt Endbestand-Ursprünge mit Zeitfilter; überschriebene/gelöschte frühere Inhalte nicht rekonstruierbar. Schlüsselidentität ist kein neuer fachlicher Testnachweis.'},
 'B':{'gebaut':True,'gilt':'Vorlagenmechanik vorhanden; historischer Vorlagenbefund 3 -> 6 fremde Muster. Natürliche Mentor-Ausgaben #14246 (3/4), #14480 (1/5), #15276 (1/5) belegt.','gilt_nicht':'Stabile Mentorwirkung oder allgemeine Halbanteilsgarantie.','vorbehalt':'Vorlage nicht vollständig im Modellprotokoll gespeichert; historischer Vorlagenbefund aus Akten, nicht Request-Payload. B-14: Ganzzahldivision ergibt bei ausreichend großem Bestand 12/25=48%; Fremdmuster erst nach globalem LIMIT 200 gefiltert. Statischer Befund, kein hier ausgeführter Gegenfall. 22/23 bleiben auch für B unter Satz-2-Vorbehalt.','fremd_12_von_25_prozent':str(Decimal(12)/Decimal(25)*100)},
 'C':{'gebaut':True,'historisch_natuerliche_aufnahmen_lauf25':0,'historisch_gestellter_kernpfad':True,'gilt':'Norm- und Fund-Eintrittsstellen erreichbar, zwei verschiedene rote Behauptungen an drei Stelle/Schlüssel-Kombinationen historisch belegt.','gilt_nicht':'Natürliche Doppelungsabwehr oder bestandene A->C-Integration.','vorbehalt':'A33/B-11: C liest die eigene frische Ansage erneut als Altvorrat; bedingter Selbstblock folgt aus Code, natürlicher Schaden in Lauf25 mangels Zustrom nicht festgestellt. Proben monkeypatchen _angriff und umgehen gerade die natürliche A-Ansage.','V9':'Nur Diagnostik, kein Killkriterium; 0 natürliche Zeilen, 1 gestellte Zeile #16028 am 2026-09-20T02:04:52.314+00:00.'}}
status['berichtskorrekturen']=[
 {'aussage':'14 zu Norm umgestuft','korrekt':'Je 40 Übernahmen: 13 Statuswechsel, 14 Normeinträge danach (1 schon vorab Norm).','ereignisse':[14476,14477,15272,15273]},
 {'aussage':'Drei verschiedene C-Sperrfälle','korrekt':'2 verschiedene (Bereich, Schlüssel), 3 (Stelle, Bereich, Schlüssel); 5 C-Durchläufe, nicht fünf Fälle.','ereignisse':[16010,16014,16019,16022,16026]},
 {'aussage':'K2500-Doppelung stamme von Ansage #15027','korrekt':'Unmöglich: Eintrag 338 entstand 23:16:20.547 UTC, #15027 erst 23:16:38.204 UTC. Keine harte Nachzuordnung behauptet, weil Ansage-/Aufrufpayloads keine Kandidaten-ID enthalten.','ereignisse':[15002,15005,15006,15027,15030]},
 {'aussage':'11 Angriffe zu 9 Urteilen wegen 3 Angriffen in Sammelurteil #14707','korrekt':'Nicht belegt und durch unterschiedliche Kandidaten/Generationen widerlegt: #14664/K2439, #14693/K2442 sind eigene Null-Angriffs-Urteile; K2444 wurde erst #14698 nach den früheren Antworten erzeugt. #14663 und #14692 verknüpfen je 12 Zeichen Antworten mit #14662 und #14691; deren Rohtexte fehlen.','ereignisse':[14661,14662,14663,14664,14690,14691,14692,14693,14698,14704,14705,14706,14707]},
 {'aussage':'0 erzeugte Tests in Lauf25','korrekt':'0 neue natürliche Immunsystem-Einträge/Funde. Feld gesamt in #15340 und #15402 enthält 1+2=3 erfasste Angriffstests, keine bestätigten Funde. Kein nachträglicher Wechsel des Tor-Nenners.','ereignisse':[15340,15402]},
 {'aussage':'Aegis-Abweichung Lauf25 insgesamt 0 Zeilen','korrekt':'0 natürliche, aber 1 gestellte Zeile #16028 im abschließenden Snapshot.','ereignisse':[16028]}
]
for b in status['berichtskorrekturen']: chron_ids.update(b['ereignisse'])
# Alle tatsächlichen Norm-Ergebnisereignisse, nicht nur historische Berichtszahlen.
norm=[]
for r in con.execute("SELECT nr,zeit,art,inhalt FROM protokoll WHERE art='eichprobe.ergebnis' AND json_extract(inhalt,'$.probe')='norm' ORDER BY nr"):
 r=dict(r);r['inhalt']=json.loads(r['inhalt']);norm.append(r)
status['norm_ruecknahme_belege']=norm
status['kosten_gesamt']={name:{key:value for key,value in row.items() if key!='ids'} for name,row in load('kosten-abgrenzung.json').items()}
status['sekundaerquellen_gesamtstand']={'pruefung_A':'35 Befunde inkl. 2 historisch behobenen, keine Komponentenanzahl','pruefung_B':'25 Befunde, keine Torwertung','einbezug':['A10 fehlende Toleranzweitergabe','A33 C-Selbstblock','A34 Medianfehler historisch behoben, nicht neu behaupten','A35 Ansage heute gebaut, nicht als fehlend führen','B-01 Satz2','B-02/B-03 Vorspann nicht erzwungen','B-04 Norm-Eichung','B-06 Proben/Prüfbestände','B-11 A/C','B-14 Mindestanteil']}
status['fehlende_beweise']=['Laufbezogener Quellhash des tatsächlich ausgeführten Messgeräts','Vollständige natürliche A->C-Population','Neue Norm-Eichung/Gegenproben im hier untersuchten Stand','Vollständige historische System-/Nutzerprompts zur B-Vorlage','Providerrechnung und allgemeine Laufzeit-/Nettoersparnis von A']
save('STATUS-24-25.json',status)
chron=[by_nr[x] for x in sorted(chron_ids) if x in by_nr]
save('chronologie.json',chron)
print(json.dumps({'status_laeufe':len(status['laeufe']),'bauteile':list(status['bauteile']),'chronologie_ereignisse':len(chron),'kosten':status['kosten_gesamt'],'probe25':{k:v for k,v in status['laeufe'][1]['gestellte_C_proben'].items() if k in ('C_pruefungen_anzahl','C_testdurchlaeufe','C_sperrungen_anzahl','anzahl_verdict_durchlaeufe','verschiedene_schluesselfaelle','verschiedene_stelle_schluessel_kombinationen')}},ensure_ascii=False,indent=2))
