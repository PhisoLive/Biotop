"""Führt geprüfte Befunde zusammen; schreibt ausschließlich Abschlussartefakte."""
from pathlib import Path
from collections import Counter
import json,csv,hashlib,shutil,sqlite3
P=Path('/root/gesamtstand-01');R=Path('/root/biotop')
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand');A=O/'ausgaben'
def J(p): return json.loads(Path(p).read_text())
def W(n,x): (O/n).write_text(x)
def S(n,x): W(n,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
a=J(P/'pruefung-a/BEFUND.json'); b=J(P/'pruefung-b/befund.json')
for folder in ['pruefung-a','pruefung-b']:
 shutil.copytree(P/folder,O/'pruefungen'/folder,dirs_exist_ok=True)
for p in P.glob('*.py'): shutil.copy2(p,O/'quellen'/p.name)
# Explizite fachliche Gruppierung, nicht Summe unabhängiger Prüferbefunde.
zu={'B-02':'A08','B-03':'A10','B-04':'A11','B-05':'A11','B-06':'A13','B-07':'A14','B-08':'A14','B-11':'A33','B-20':'A31','B-21':'A29','B-25':'A12'}
raw={x['id']:x for x in a['befunde']+b['befunde']}; groups={x['id']:[x['id']] for x in a['befunde'] if x['id'] not in ['A34','A35']}
for x in b['befunde']:groups.setdefault(zu.get(x['id'],x['id']),[]).append(x['id'])
# Zusätzliche vom Hauptprüfer am Originalcode überprüfte Abweichungen.
c=[
 {'id':'C01','titel':'Vorgänger-Torwächter und zugesagte Entwicklungsabsicherung nicht übernommen','status':'statisch belegt','masterprompt':[{'von':308,'bis':312},{'von':322,'bis':322}], 'quellen':[{'datei':str(R/'biotop/dienst.py'),'von':25,'bis':25},{'datei':str(R/'biotop/dienst.py'),'von':60,'bis':102},{'datei':str(R/'.gitignore'),'von':1,'bis':4}], 'mechanik':'Der Dienst ist Python HTTPServer, nicht der übernommene Express-Torwächter. _json_body liest die angegebene Content-Length ohne Obergrenze; bei der Anmeldung fehlen im Dienst Rate-Limit, Request-ID, CORS-Liste und die genannte zentrale Fehler-/Redaction-Schicht. Im vollständigen Git-Dateiinventar fehlen CI, CodeQL, Dependabot, Vitest/Playwright sowie der gitleaks-Pflichtlauf. .gitignore ignoriert .env*, ist aber kein Archiv-/Secret-Scan. Datenbank und Token-Anmeldung existieren; das erfüllt nicht den gesamten Übernahmeauftrag.', 'abgrenzung':'Gilt für den untersuchten Biotop-Quellstand; keine Aussage über beliebige vorgeschaltete Fremdserver. Kein Angriff und kein Login ausgeführt. Inventarbeleg 03-dateien.json.'},
 {'id':'C02','titel':'Verfassungsentwurf ist weiterhin manueller Import, kein Organentwurf','status':'statisch belegt','masterprompt':[{'von':135,'bis':137},{'von':254,'bis':254}], 'quellen':[{'datei':str(R/'biotop/organe/verfassung.py'),'von':1,'bis':7},{'datei':str(R/'biotop/organe/verfassung.py'),'von':24,'bis':41}], 'mechanik':'Das Verfassungsmodul legt mitgelieferten Text und Regeln ein. Es erzeugt aus Aufnahmebericht/Landkarte keinen Entwurf mit 5–15 Sätzen; das Modul nennt dies ausdrücklich als auf später verschobene Arbeit. Manuell von Hermes/Chat-Claude verfasste Übungswerkdokumente sind nicht die Implementierung dieses Entwurfsorgans.', 'abgrenzung':'Das Vorliegen zweier bestätigter Werkverfassungen wird nicht bestritten; es fehlt der verlangte allgemeine Entwurfsweg.'},
 {'id':'C03','titel':'Verlaufskurve übernimmt nicht den vollständigen Endtestbestand','status':'statisch belegt','masterprompt':[{'von':151,'bis':151},{'von':154,'bis':154}], 'quellen':[{'datei':str(R/'biotop/lauf.py'),'von':448,'bis':470}], 'mechanik':'kurve_nachrechnen übernimmt mit glob(test_*.py) nur unmittelbar unter tests liegende Endtests. Tests in Unterordnern, insbesondere tests/vertraege, werden nicht als Endbestand auf ältere Archive übertragen. Außerdem werden sämtliche Lazarus-Einträge statt ausdrücklich freigegebener/angenommener Generationen ausgewählt. Damit ist dieser Befehl für verschachtelte/veränderte Vertragsbestände nicht die verlangte Gleichheit des Endtestbestands über angenommene Generationen.', 'abgrenzung':'Kein neuer Kurvenlauf. Keine Behauptung, eine bestimmte alte Zahl sei deswegen numerisch falsch; der allgemeine Rechenpfad ist eingeschränkt.'}
]
for x in c:raw[x['id']]=x;groups.setdefault('A32' if x['id']=='C03' else x['id'],[]).append(x['id'])
def refs(x):
 out=[]
 for q in x.get('masterprompt',[]):
  lo,hi=q.get('zeilen',[q.get('von'),q.get('bis')]);out.append((lo,hi))
 return out
def qrefs(x):
 out=[]
 for q in x.get('quellen',[]):
  lo,hi=q.get('zeilen',[q.get('von'),q.get('bis')]);out.append((q['datei'],lo,hi))
 return out
# Referenzen am tatsächlichen Quellstand nachprüfen, nicht Prüfer-Selbstberichte übernehmen.
valid=[];errors=[]
for bid,x in raw.items():
 for p,lo,hi in qrefs(x):
  data=Path(p).read_bytes();length=len(data.decode().splitlines());ok=isinstance(lo,int) and 1<=lo<=hi<=length
  expected=next((q.get('sha256') for q in x['quellen'] if q['datei']==p and q.get('sha256')),None)
  actual=hashlib.sha256(data).hexdigest();ok=ok and (not expected or expected==actual)
  entry={'befund':bid,'datei':p,'von':lo,'bis':hi,'dateizeilen':length,'sha256':actual,'referenz_gueltig':ok};valid.append(entry)
  if not ok:errors.append(entry)
assert not errors,errors
S('ausgaben/22-referenzpruefung.json',{'referenzen':valid,'geprueft':len(valid),'gueltig':len(valid)-len(errors),'fehler':errors,'grenze':'Gültige Zeilenbereiche/Hashes; keine dynamische Bestätigung sämtlicher Semantik.'})
S('ausgaben/23-befundregister.json',{'gruppen':groups,'gruppenzahl':len(groups),'einzelbefunde':raw,'historisch_aufgehoben':['A34','A35'],'hinweis':'Gruppen können mehrere Teilabweichungen enthalten. Keine Anzahl unabhängiger Fehler aus Addition der beiden Prüfberichte ableiten.'})
md=['# Abweichungen vom Masterprompt Fassung 6 — konsolidierter Codebefund','',f'**{len(groups)} Befundgruppen** aus zwei überlappend geprüften Teilsichten und drei Ergänzungen des Hauptprüfers. Das ist eine redaktionelle Gruppierung, keine behauptete Naturkonstante der Fehlerzahl. Zwei frühere Abweichungen (A34, A35) sind heute aufgehoben und separat ausgewiesen. Alle Einzelbefunde bleiben in den Anlagen erhalten; kein ungünstiger Befund wurde gestrichen.','', '**Beweisgrenze:** Statische Codebelege sind gelesen, nicht vollständig dynamisch ausgeführt. Historische Protokollbelege sind historische Ausführung, kein frischer Abnahmelauf. A22 und A27 bleiben Risiken, nicht beobachtete Schadensfälle. Selbst eine zeilenweise Prüfung garantiert nicht, jeden denkbaren Fehler gefunden zu haben.','', 'Quellen: unverändertes `biotop/QUELLSTAND-01.tar.gz`, vollständiger Solltext `quellen/MASTERPROMPT-FASSUNG-6.md`, Einzelprüfungen unter `pruefungen/`. Die Quellenbereiche und in A vorhandenen Quellhashes wurden am Original nochmals geprüft (`22-referenzpruefung.json`).','', '## Befunde','']
for key,ids in groups.items():
 md += [f'### {key} — {raw[key]["titel"]}', 'Zugeordnete Einzelbefunde: '+', '.join(ids)+'.','']
 for bid in ids:
  x=raw[bid];md += [f'**{bid}: {x["titel"]}**', '**Status:** '+x.get('status',x.get('stand','gelesen'))+'.', '**F6:** '+', '.join(f'Z. {lo}–{hi}' for lo,hi in refs(x))+'.', '**Code:** '+ '; '.join(f'`{p.removeprefix(str(R)+"/")}:{lo}–{hi}`' for p,lo,hi in qrefs(x))+'.', x['mechanik'], x.get('wirkung',x.get('folge','')), '**Grenze:** '+x.get('abgrenzung','Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.'),'']
  if x.get('historisch'):md+=['**Historischer Beleg:** '+x['historisch'].get('bewertung',str(x['historisch'])),'']
  if x.get('hermes_bezug'):md+=['**Eigenanteil Hermes:** '+x['hermes_bezug'],'']
md+=['## Historisch vorhanden, heute nicht mehr als aktueller Mangel zählen','']
for bid in ['A34','A35']:
 x=raw[bid];md += [f'### {bid} — {x["titel"]}',x['mechanik'],x.get('abgrenzung',''),'']
md+=['## Eigene Aussagen zurückgenommen / eingeschränkt','', '- „Vier Eichproben bestanden“ war bei der Normprobe keine Aussage über die Normregel. `masse` statt `mass`, `norm=[]`, `zuwachs=None` und Ablehnung schon durch Pareto sind dokumentiert. Die frühere 4-von-4-Abnahme darf für den untersuchten Stand nicht als Nachweis der Normzeile fortgeschrieben werden (A11/B04/B05).', '- Der Fortbau von A und die geänderte Ansagehistorie innerhalb der weiterverwendeten IDs 22/23 verletzen Satz 2. Mehr Aufrufe allein wären kein Beweis; die konkreten Ansage-Payloads vor/nach dem Übergang sind es (B01).', '- „Mindestanteil gebaut“ beweist nicht „Mindestanteil stets erfüllt“: der Branch bei genügend eigenen und fremden Einträgen zeigt 12 fremde von 25, also weniger als die Hälfte (B14; statisch, kein natürlicher neuer Lauf).', '- Die Aufnahme-/Kern-/Generationsmechanik existiert; „eigenständig betriebsbereit“ wäre trotzdem falsch: kein laufender Dienst, kein erzwungener Vorspann, keine pytest-Eigen-Testsuite.', '- Auch die Zusatz-Reproduktionsprüfung dieser Bestandsaufnahme scheiterte: erster Versuch `21-gegenfaelle.json`, Exit 1 wegen fehlerhaftem Testgerüst; die Wiederholung wurde von der Tool-Freigabe blockiert und nicht umgangen. Daher **0 von 4 vorgesehenen neuen Gegenfällen als vollständig bestätigt gemeldet**. Keine synthetischen Erfolgsoutputs. Der Skriptfehler wurde nur im außerhalb liegenden Prüfskript berichtigt, nicht im Biotop.','']
W('ABWEICHUNGEN-01.md','\n'.join(md))
# Für JEDE physische F6-Zeile ein Eintrag, inklusive nichtnormativer Zeilen.
mp=(O/'quellen/MASTERPROMPT-FASSUNG-6.md').read_text().splitlines();line_refs={i:[] for i in range(1,len(mp)+1)}
for key,ids in groups.items():
 for bid in ids:
  for lo,hi in refs(raw[bid]):
   for i in range(lo,hi+1):
    if i in line_refs and key not in line_refs[i]:line_refs[i].append(key)
# Sachbezogene Ergänzungen zu Zeilen, die die Teilsichten nicht separat zitieren.
manual={69:['A01','A04'],75:['A31','B-13'],77:['C01','B-23'],95:['A02'],116:['A26'],135:['C02'],137:['A09'],144:['B-17'],154:['A32'],156:['A19'],173:['A09'],202:['B-19'],208:['B-19'],211:['A30'],217:['A31'],231:['B-13'],237:['A04','A27'],238:['A27'],254:['C02'],255:['A08','A15','A16'],259:['A31'],263:['A09'],264:['A09'],276:['A26'],279:['A26'],281:['A28','A29'],289:['A24'],290:['A24'],308:['C01'],309:['A07'],310:['C01'],311:['C01'],312:['A24'],322:['C01'],335:['A21'],336:['A17'],338:['A30','A31'],339:['A22','A28'],340:['A08'],342:['C01'],354:['A15','A16'],356:['A11'],357:['A11'],358:['A11'],359:['B-18','A11'],360:['A33'],361:['B-18'],362:['A32'],364:['A11'],375:['B-14'],376:['B-17'],377:['B-24'],379:['B-15'],380:['B-12'],381:['A29','B-23'],384:['A11'],386:['A08','A10','A11'],393:['A33','B-14'],395:['A01','A05'],396:['A08','A11'],397:['A15','A16'],402:['A05','A06','A07'],403:['A10','A11','A12'],404:['A15','A16'],408:['B-18'],411:['A09'],412:['A28'],421:['A30'],426:['A23','A25'],435:['A09'],441:['A09'],457:['A09']}
for i,ids in manual.items():
 for key in ids:
  assert key in groups,key
  if key not in line_refs[i]:line_refs[i].append(key)
rows=[];section='Kopf / Änderungshistorie'
for i,text in enumerate(mp,1):
 if text.startswith('##'):section=text.lstrip('# ')
 ids=line_refs[i]
 if not text.strip():status='Leerzeile';note='Keine selbstständige Anforderung.'
 elif text=='---':status='Trennzeile';note='Keine selbstständige Anforderung.'
 elif text.startswith('#'):status='Überschrift';note='Die zugehörigen Anforderungen stehen in den folgenden Einzelzeilen.'
 elif ids:status='Abweichung / Einschränkung belegt';note='Konkrete Mechanik, Codezeilen, Version und Beweisgrenze in den genannten Gruppen; damit nicht notwendig jeder Teilsatz dieser Zeile verletzt.'
 elif i==28:status='Eigener Zwischenlieferfehler';note='Bei der Zwischenmeldung fehlte DATEIEN.txt, obwohl ZWISCHENBERICHT.md lag; in der Abschlusslieferung behoben, nicht rückwirkend als erfüllt ausgegeben.'
 elif i<65 or i in [344,346,350,351,364,366,370,371,384,386,389,390,457,466,470]:status='Historie / Standangabe / Kontext';note='Nicht als heute neu abgenommene Torzeile behandelt; heutiger Stand gegenüber historischem Schnitt getrennt (LAEUFE-01, ORGANBETRIEB-01).'
 elif 292<=i<=301:status='Kosten / Schätzung';note='Historische Beträge: LAEUFE-01.md und DB-Buchungen; Zukunftsschätzungen nicht gemessen und nicht als Kostenstand ausgegeben.'
 elif 392<=i<=412:status='Phase 4: heute nicht abgenommen';note='Kein echtes Werk in dieser Bestandsaufnahme bearbeitet; kein Tor-4-Nachweis erfunden.'
 elif 418<=i<=425:status='Lieferpflicht dieses Auftrags';note='BERICHT, Rohdaten, Quellarchiv, KASSE, DATEIEN und Manifest; kein neues gehobenes Werk (werk/HINWEIS-01.md).'
 elif i in [103,104,105,106,107,108,110]:status='Grundsatz / Belegregel';note='Einzelprüfung in GRUNDSAETZE-2a-01.md; kein pauschales Bestanden.'
 elif 330<=i<=383:status='Historische Torforderung, nicht neu ausgeführt';note='Ein erneuter kompletter Torlauf war nicht Gegenstand dieses lesenden Auftrags. Keine historische Grünmeldung ersetzt heutigen Befund.'
 elif 443<=i<=464:status='Werkverfassung / fachliches Soll';note='Allgemeine Durchsetzung siehe A16/A19/A20/A31; die Fachlogik der Übungswerke wurde nicht erneut in Hebungsläufen abgenommen.'
 elif i in [315,316]:status='Implementiert, begrenzter Nachweis';note='SQLite mit Transaktionen und drei persistente Gedächtnistabellen vorhanden; daraus folgt weder Prozess-/Rollentrennung noch korrekte Nutzung.'
 elif i in [318,319,320,321]:status='Altprojekt-Abgrenzung';note='Genannte Altprojekt-Komponenten im vollständigen aktuellen Git-Inventar nicht enthalten; historische Löschung im Vorgänger wurde nicht separat bewiesen.'
 else:status='Kein zusätzlicher Einzelbefund im Prüfschnitt';note='Gelesen; keine zusätzliche Abweichung für diese einzelne Textzeile belegt. Das ist ausdrücklich keine dynamische Abnahme oder Vollständigkeitsgarantie.'
 rows.append({'zeile':i,'abschnitt':section,'wortlaut':text,'bewertung':status,'befundgruppen':','.join(ids),'einordnung':note})
with (O/'MASTERPROMPT-ZEILEN-01.csv').open('w',newline='') as fp:
 wr=csv.DictWriter(fp,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
S('ausgaben/24-zeilenabdeckung.json',{'masterprompt_zeilen':len(mp),'eintraege':len(rows),'eindeutige_zeilen':len({r['zeile'] for r in rows}),'fehlende':sorted(set(range(1,len(mp)+1))-{r['zeile'] for r in rows}),'bewertungen':dict(Counter(r['bewertung'] for r in rows)),'hinweis':'Vollständige Zeilenadressierung ist nicht gleich Vollständigkeitsbeweis aller möglichen Fehler.'})
W('MASTERPROMPT-ABGLEICH-01.md',f'''# Zeilenweiser F6-Abgleich

`MASTERPROMPT-ZEILEN-01.csv` enthält **{len(rows)} von {len(mp)} physischen Originalzeilen**, jeweils ungekürzt mit Bewertung und Befundzuordnung. Leerzeilen, Überschriften, Änderungshistorie, Schätzungen und zukünftige Torforderungen sind ausdrücklich von laufzeitfähigen Codeanforderungen getrennt. `24-zeilenabdeckung.json` prüft eindeutige Zeilen und fehlende Nummern.

Die Codeabweichungen stehen nicht nur in einem Matrixhäkchen: `ABWEICHUNGEN-01.md` nennt für jede Gruppe den Mechanismus und die Originalcodezeilen. Der unveränderte Quellstand ist beigelegt. Die zwei Einzelprüfungen bleiben vollständig einsehbar, einschließlich aufgehobener Kritik und Risiken. Keine additive „60 Fehler“-Schlagzeile aus überlappenden Befunden.

## Versionsgrenze

Untersucht ist der heutige Quellstand `b42dc941e7fcb66632ba6a0e13b8df106a270a31`. Gegen den archivierten F6-Ausgangspunkt `7c73d403c18755dda26655c78ac7290c446d9f45` sind 17 Dateien verändert (1815 eingefügte, 23 entfernte Zeilen laut Git; nicht gleich physischer Größenunterschied). Nur zwei davon sind produktive Organmodule: `aegis.py` und `gedaechtnis.py`. Die anderen sind Prüfscripte. Quelle: `18-historischer-codevergleich.json`, vollständiger Diff im Prüfungsanhang A.

Deshalb gilt F6 als verlangter Solltext, aber nicht als Beschreibung des heutigen Ist-Stands: Ansage und Mindestanteil wurden später gebaut, ebenso eine zusätzliche Aufnahmesperre C. Aktuelle C-Lücken werden als spätere Lücken ausgewiesen, nicht dem früheren F6-Code untergeschoben. Die historischen Läufe 1–23 werden separat gerechnet, Lauf 24/25 nicht hineingemischt.

## Grenze des Versprechens „jede Abweichung“

Der Solltext wurde vollständig zeilenweise abgeglichen, der produktive Python-Quellstand vollständig in den kombinierten Leseabdeckungen erfasst. Alle gefundenen Abweichungen sind aufgeführt. Eine endliche Codeprüfung kann nicht beweisen, dass kein weiterer Fehler existiert. Statische Risiken sind keine ausgeführten Gegenfälle; heutige Abnahmegrenzen wurden nicht herabgesetzt.
''')
print(json.dumps({'gruppen':len(groups),'rohe_befunde':len(raw),'aufgehoben':2,'gueltige_quellreferenzen':len(valid),'sollzeilen':len(rows)},ensure_ascii=False))
