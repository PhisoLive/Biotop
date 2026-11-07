"""Abschluss eines Leseauftrags. Kein Biotop-Lauf und keine Reparatur."""
from pathlib import Path
from decimal import Decimal
from collections import Counter
import json,sqlite3,hashlib,datetime,subprocess,shutil,re,csv,tarfile
P=Path('/root/gesamtstand-01');R=Path('/root/biotop');O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand');A=O/'ausgaben'
def J(n):return json.loads((A/n).read_text())
def S(n,x):(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def W(n,x):(O/n).write_text(x)
def cmd(args):
 r=subprocess.run(args,capture_output=True,text=True);return {'befehl':args,'rc':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
# Nicht nur Git: gesamter zuvor gemessener Bestand als Mengen-/Hashvergleich.
before=J('01-zustand-vorher.json')['dateien'];after={};readerr=[]
for p in R.rglob('*'):
 if p.is_file() and not p.is_symlink():
  try:
   bs=p.read_bytes();after[str(p.relative_to(R))]={'bytes':len(bs),'sha256':hashlib.sha256(bs).hexdigest()}
  except OSError as e:readerr.append({'pfad':str(p),'fehler':str(e)})
changed=[p for p in sorted(before.keys()&after.keys()) if before[p]['sha256']!=after[p]['sha256']]
added=sorted(after.keys()-before.keys());removed=sorted(before.keys()-after.keys())
c=sqlite3.connect('file:/root/biotop/daten/biotop.db?mode=ro',uri=True);c.row_factory=sqlite3.Row
stand={'zeit':now,'dateien_vorher':len(before),'dateien_nachher':len(after),'inhalt_geaendert':changed,'hinzugefuegt':added,'entfernt':removed,'lesefehler':readerr,'git':cmd(['git','-C',str(R),'status','--porcelain=v1']),'head':cmd(['git','-C',str(R),'rev-parse','HEAD']), 'datenbank':{'laeufe':c.execute('SELECT count(*) FROM laeufe').fetchone()[0],'max_lauf':c.execute('SELECT max(id) FROM laeufe').fetchone()[0],'kassenbuchungen':c.execute('SELECT count(*) FROM kasse').fetchone()[0],'kosten_eur':str(sum((Decimal(str(x[0])) for x in c.execute('SELECT kosten_eur FROM kasse')),Decimal(0))),'protokollzeilen':c.execute('SELECT count(*) FROM protokoll').fetchone()[0]}}
S('ausgaben/26-bestand-unveraendert.json',stand)
assert not(changed or added or removed or readerr),stand
assert not stand['git']['stdout'] and stand['head']['stdout'].strip()=='b42dc941e7fcb66632ba6a0e13b8df106a270a31'
assert stand['datenbank']['kassenbuchungen']==J('02-datenbank.json')['kasse']['anzahl']
# Nur abrechnungsrelevante, nicht private Sitzungsmetadaten veröffentlichen.
h=sqlite3.connect('file:/root/.hermes/state.db?mode=ro',uri=True);h.row_factory=sqlite3.Row
fields='id,parent_session_id,model,billing_provider,billing_mode,cost_status,actual_cost_usd,estimated_cost_usd,api_call_count,input_tokens,output_tokens,cache_read_tokens,cache_write_tokens'
usage=[dict(x) for x in h.execute(f'SELECT {fields} FROM sessions WHERE id=? OR parent_session_id=?',('20260920_063003_896e94ff','20260920_063003_896e94ff'))]
S('ausgaben/27-auftragskosten.json',{'zeit':now,'biotop_kassenstand_vorher':J('02-datenbank.json')['kasse'],'biotop_kassenstand_nachher':stand['datenbank'],'neue_biotop_buchungen':stand['datenbank']['kassenbuchungen']-J('02-datenbank.json')['kasse']['anzahl'],'hermes_sitzungen':usage,'hinweis':'Snapshot des Rechnungsstands, laufende Hauptsitzung noch nicht beendet. actual_cost_usd NULL heißt unbekannter Einzelpreis; billing_mode subscription_included/cost_status included ist keine gemessene Token-Einzelrechnung. Frühere Sitzungen gehören nicht zu dieser Bestandsaufnahme.'})
assert len(usage)==3 and all(x['billing_mode']=='subscription_included' for x in usage)
S('ausgaben/21-gegenfaelle-FREIGABE.json',{'quelle':'Tatsächliches terminal-Toolergebnis des Wiederholungsversuchs','output':'','exit_code':-1,'status':'blocked','error':'BLOCKED: Command timed out without user response. The user has NOT consented to this action. Do NOT retry this command, do NOT rephrase it, and do NOT attempt the same outcome via a different command. Stop the current workflow and wait for the user to respond before taking any further destructive or irreversible action. Silence is not consent.','reaktion':'Keine Wiederholung und keine Umgehung. Keine 4-von-4-Behauptung. Nur Abschluss der lesenden Bestandsaufnahme.'})
# Die Quelle mit den nicht erneut ausgeführten Hilfsscripten bleibt reproduzierbar.
for p in P.glob('*.py'):shutil.copy2(p,O/'quellen'/p.name)
reg=J('23-befundregister.json');k=J('12-kassenabgleich.json');u=J('05-umfang.json');db=J('02-datenbank.json');cov=J('25-code-leseabdeckung.json')
assert len(k['laeufe'])==23 and {r['lauf'] for r in k['laeufe']}==set(range(1,24))
assert cov['produktiv_gesamt'] if 'produktiv_gesamt' in cov else cov['produktive_dateien']==35
# Bereinigung der B-Kürzel in redaktionellen Texten, keine Inhaltsänderung.
for name in ['ORGANBETRIEB-01.md','GRUNDSAETZE-2a-01.md']:
 p=O/name;text=p.read_text();p.write_text(re.sub(r'\bB(\d{2})\b',r'B-\1',text))
W('KASSE.md',f'''# Kasse dieses Auftrags — kein Lauf

Budget: **1,00 €**. Stand aus Datenbanken: **{now}**.

- **0 neue Biotop-Kassenbuchungen**, Stand vorher/nachher **{db['kasse']['anzahl']} / {stand['datenbank']['kassenbuchungen']}**; gespeicherte Summe unverändert **{db['kasse']['summe_eur']} €**. Damit **0,00 € neue tokenabgerechnete Biotop-Aufrufe von 1,00 € Budget**. Kein Lauf angelegt; **{stand['datenbank']['laeufe']} vorbestehende Lauf-IDs**, höchstens ID {stand['datenbank']['max_lauf']}.
- Hermes-Hauptprüfung und zwei delegierte Leseprüfungen: **{len(usage)} von {len(usage)} Sitzungen** sind in `state.db` als `subscription_included` / `included` geführt. Im Abfrageschnitt zusammen **{sum(x['api_call_count'] or 0 for x in usage)} gespeicherte API-Aufrufe**. Das sind keine Biotop-OpenRouter-Aufrufe. Einzelpreis `actual_cost_usd` ist NULL, nicht als gemessene Nullrechnung umgedeutet; geschätzte Einzelkosten sind in allen drei Zeilen 0. Ein noch ausstehendes Hauptsitzungsende ist nicht im Snapshot enthalten.
- Kein zusätzliches Anbieter-Abokontingent gekauft. Verbrauch des Hermes-Trägerabos wurde nicht gegen eine hier unbekannte Wochenquote bewertet.
- Prüfungen: keine Installation, kein produktiver Biotop-Lauf, keine kostenpflichtige neue Eichung. Vorhandene Kurzprüfcontainer und lokale Datei-/SQL-Prüfungen hatten keine Modellaufrufe. Der optionale Gegenfall-Wiederholungsversuch wurde vom Tool blockiert, nicht ausgeführt.

Die **historischen** Kosten der Läufe 1–23 stehen ausschließlich in `LAEUFE-01.md`; sie werden diesem 1-Euro-Auftrag nicht erneut belastet. Rohbeleg: `ausgaben/27-auftragskosten.json`, historische Rohbuchungen: `06-kassenbuchungen.json`.
''')
W('werk/HINWEIS-01.md','''# Kein neu gehobenes Werk

Dieser Auftrag ist ausdrücklich eine Bestandsaufnahme, kein Hebungslauf. Es wurde kein Werk eingelegt, geändert, angenommen oder rückgeholt. Daher gibt es hier kein als neu gehoben ausgegebenes Werkarchiv. Die geprüften Bestandszahlen, Metadaten und der Biotop-Quellstand liegen im Ordner. Historische Werkarchive verbleiben in den ursprünglichen Abschlussordnern; sie werden nicht ohne Auftrag dupliziert.

Die vollständige SQLite-Kopie wird wegen der enthaltenen Anmelde-/Tokendaten nicht öffentlich ausgeliefert. Fachliche Rohbuchungen und bereinigte Protokoll-/Zustandsdaten sind beigelegt. Ihre Bereinigung wird nicht als unveränderte Hashkette ausgegeben.
''')
W('OFFENE-PUNKTE-01.md','''# Entscheidung vor Vorbedingung 1

## Dieser Auftrag

Die fünf verlangten Teile liegen vor: Umfang, Organbetrieb/Altbestand, zeilenweiser F6-Abgleich, Läufe 1–23/Kosten, sechs Grundsätze. Kein neuer Lauf. Die optionale dynamische Gegenfallprüfung ist nicht bestanden; ihr Fehler und die blockierte Wiederholung bleiben sichtbar. Die Vollständigkeit der erfassten Mengen und die Veröffentlichung werden separat geprüft.

## Nicht als erledigt ausgegeben

- Keine Reparatur der gefundenen Codeabweichungen im Biotop. Die Bestandsaufnahme sollte den tatsächlichen Stand festhalten; Reparaturen würden ihren Gegenstand verändern. Das ist keine still verschobene Fehlerkorrektur, sondern eine ausdrücklich getrennte Änderung des Auftragsumfangs.
- Keine komplette neue Tor-Abnahme, kein neues Norm-Gegenfallpaar, kein allgemeiner Kammer-/Angriffs-Sicherheitsnachweis und keine neue Leistungsmessung am Handelswerk.
- Keine geschätzten Kosten für zwei historische Modellanfragen ohne Antwort-/Fehlerabschluss; tatsächliche Belastung dort unbekannt.
- Kein Anspruch, alle denkbaren Fehler gefunden zu haben; 470-zeilige Sollabdeckung ist kein mathematischer Vollständigkeitsbeweis.

## Vorbedingung 1 kann nicht als bloße Fortsetzung behandelt werden

A/B und später C wurden bereits vor dieser Bestandsaufnahme gebaut und Läufe 24/25 existieren. Ein erneutes „danach Vorbedingung 1“ darf diese Vergangenheit nicht als frischen Beginn verschleiern und darf keine alten IDs weiterführen.

Vor einem neuen Messlauf müssen mindestens die falsch grüne Norm-Eichprobe, verbindlicher Vorspann/Rauschanbindung, Fundklassifikation sowie A/C-Wechselwirkung und B-Mindestanteil geklärt/repariert werden. Kernschutz-/Aufnahmepfad-Lücken sind vor einem echten Betriebswerk zusätzlich zu schließen. Welche der übrigen Befundgruppen zuerst bearbeitet wird, darf nicht durch Absenkung von Torgrenzen entschieden werden.

**Entscheidung erforderlich:** eigener Reparaturauftrag mit klarer Eingrenzung und Budget; anschließend neuer Lauf vom dokumentierten Ausgang und unverändertem Messgerät. Die vorhandene Tool-Sperre für die Gegenfall-Wiederholung wird nicht umgangen. Diese Bestandsaufnahme erteilt selbst keine neue Freigabe.
''')
W('BERICHT.md',f'''# Biotop-Gesamtstand — unabhängig gemessene Bestandsaufnahme

**Kein Lauf, keine Code-/Datenreparatur.** Quellstand `b42dc941e7fcb66632ba6a0e13b8df106a270a31`. Bestandsstichtag {J('01-zustand-vorher.json')['zeit']}; Schlussprüfung {now}. Auftrag: vor Vorbedingung 1 den tatsächlichen Bauzustand offenlegen, nicht alte Abschlussberichte wiederholen.

## Ergebnis zu den fünf verlangten Teilen

1. **Umfang:** **{u['gesamt']['dateien']} eigene versionierte Dateien / {u['gesamt']['zeilen']} physische Zeilen**; davon **35 produktive Python-Dateien / 6370 Zeilen**, **18 physische Organmodule** für die **15 Sollorganabschnitte**. Hauptdatenbank **{db['live_dateien']['biotop.db']['bytes']} Bytes**, **{len(db['tabellen'])} Tabellen**. Eigene pytest-Sammlung: **0 Testfälle**, Exit 5, kein grüner Lauf. Prüfscripte und Werk-Vertragstests sind getrennt gezählt. → `UMFANG-01.md`.
2. **Betrieb:** Zum ausgewiesenen Prozessstichtag **0 Biotop-Treffer bei 148 von 148 gelesenen PID-Verzeichnissen**, kein vorhandener Biotop-System-/Benutzerdienst, keine laufenden Container. Viele Organe wurden historisch tatsächlich benutzt; das ist kein heutiger Dauerbetrieb. Optionale Pflichtorgane, fehlende Pfade und gefährliche Altscripte sind getrennt. → `ORGANBETRIEB-01.md`.
3. **F6-Abgleich:** **470 von 470 Solltextzeilen** einzeln adressiert; **35 von 35 produktiven Python-Dateien / 6370 von 6370 Zeilen** in den kombinierten Leseabdeckungen. **{reg['gruppenzahl']} redaktionelle Befundgruppen**, keine doppelte Fehlerzahl aus überlappenden Prüferlisten; zwei überholte historische Kritiken separat. Jede Gruppe mit konkreten Quell-/Sollzeilen und Beweisgrenze. → `MASTERPROMPT-ZEILEN-01.csv`, `ABWEICHUNGEN-01.md`, Prüfungsanhänge.
4. **Läufe/Kosten:** **23 von 23 Läufen** mit DB-Status, Werk, historischen und heutigen Buchungen tabelliert. **7,37 € stimmt als Summe der fünf auf Cent gerundeten Abschnittsbeträge.** Die rekonstruierte Rohsumme ist `{k['historisch_roh_eur']}` €; heutige Buchungen derselben IDs ergeben `{k['heute_1bis23_eur']}` €. Spätere Buchungen auf alten IDs und Rundung sind getrennt erklärt, nicht still verrechnet. → `LAEUFE-01.md`.
5. **Sechs Grundsätze:** Konkrete Eigenverstöße bei Norm-/Fundbeweisen, Befehlswirkung, Prüfnebenwirkungen, Nachrechnungsableitungen und Ersatzmerkmalen. Die Median-/Streuungsebenen sind heute grundsätzlich getrennt; ich behaupte dort nicht erneut den alten Fehler. → `GRUNDSAETZE-2a-01.md`.

## Die entscheidenden Gegenbefunde zu meiner bisherigen Arbeit

- Die Norm-Eichprobe konnte ohne Normprüfung grün werden (`masse` statt `mass`; historische Ergebnisse mit `norm=[]`, `zuwachs=None`). Ein früheres „vier bestanden“ beweist diese Torzeile nicht.
- Unter den IDs 22 und 23 wurde der Anklägerablauf geändert und weitergearbeitet. Reale Protokollübergänge belegen den Satz-2-Verstoß; Gitdatum oder Kostenanstieg allein wären kein Beweis.
- Das spätere C kann die eigene gerade protokollierte Ansage als Doppelung sperren. Die gestellten Pfadproben beweisen nicht die korrekte A→C-Integration.
- Der gebaute B-Mindestanteil hat einen Branch mit 12 fremden von 25 Einträgen. „Bauteil vorhanden“ ist nicht „Regel für jeden Bestand erfüllt“.
- Keine isolierte, automatisch auffindbare pytest-Eigen-Testsuite; kein erzwungener vollständiger Vorspann; keine technische Kern-Schreibrolle. Das ist kein für ein beliebiges echtes Werk betriebsfertiges System.

## Ausführung und Grenzen

Messungen stammen aus Dateien/AST, Git und read-only SQLite. Hashkette mit der Originalfunktion geprüft: **16030 von 16030 Protokollzeilen**. Dateiinhalte am Ende **{len(after)} von {len(before)} unverändert**, keine Datei hinzugefügt/entfernt, Git sauber (`26-bestand-unveraendert.json`). Die öffentliche Protokollkopie entfernt Anmeldeinhalte und ist deshalb nicht selbst die unveränderte Gesamthashkette.

Neu ausgeführt: Inventar-/SQL-/Rechenprüfungen, pytest-Sammlung (kein Fall), vorhandene Rauschbeispiele. **Zusatz-Gegenfallprüfung fehlgeschlagen**, Exit 1 im eigenen Testgerüst; Wiederholung vom Tool blockiert und nicht umgangen. **0 von 4 vorgesehenen neuen Gegenfällen vollständig bestätigt gemeldet.** Statische und historische Befunde stehen unabhängig davon mit ihrer tatsächlichen Beweisgrenze im Bericht. Keine erfundenen Ausführungsausgaben.

**Kosten:** 0 neue Biotop-Kassenbuchungen / 0,00 € zusätzliche Biotop-Modellkosten von 1,00 € Budget. Drei Hermes-Prüfsitzungen laut `state.db` im Abo enthalten, keine bekannte Einzelrechnung; Details und Abfrageschnitt in `KASSE.md`.

**Eigener Lieferfehler:** Bei der Zwischenmeldung vor Rückkehr der delegierten Prüfungen lag zwar `ZWISCHENBERICHT.md`, aber noch kein `DATEIEN.txt` im Ordner. Damit war die Zwischenlieferpflicht nicht vollständig erfüllt. Die Abschlusslieferung behebt das; der Zwischenstand wird nicht rückwirkend als vollständig bezeichnet.

## Versions- und Fortsetzungsgrenze

Der tatsächliche Ist-Stand liegt bereits nach früheren Arbeiten an Vorbedingung 1: Lauf 24/25 und A/B/C existieren. Diese Bestandsaufnahme setzt sie weder zurück noch erklärt sie rückwirkend als ungearbeitet. Kein neuer Lauf wurde gestartet. **Ein neuer Reparaturauftrag ist vor dem gewünschten erneuten Vorbedingungs-Lauf erforderlich**, weil die gefundenen Messgerätfehler sonst die nächste Messung entwerten. Offene Punkte und Entscheidung: `OFFENE-PUNKTE-01.md`.

## Abholung / Prüfbarkeit

`DATEIEN.txt` listet den gesamten Ordner. `PRUEFSUMME-ORDNER.txt` nennt die SHA-256 des sortierten `PRUEFSUMMEN.sha256`-Manifests; dessen Einträge versiegeln die Nutzdateien einschließlich dieses Berichts, Rohdaten, Quellen und Einzelprüfungen. Das abschließende Abrufprotokoll liegt außerhalb dieses Manifests, um keine Selbstreferenz zu erzeugen. Eine gültige Lieferung wird erst nach bytegleichem HTTPS-Abruf aller Manifestdateien gemeldet.
''')
W('ZWISCHENBERICHT.md',f'''# Schlussstand der Bestandsaufnahme

Stand {now}. Die fünf Auftragsteile liegen in `BERICHT.md` und seinen Fachdateien vor. Kein Biotop-Lauf, keine Reparatur. Datenbank: {stand['datenbank']['kassenbuchungen']} von {db['kasse']['anzahl']} vorherigen Buchungen unverändert, 0 neue Buchungen, keine neuen Biotop-Modellkosten von 1,00 € Budget. Hermes-Trägerkosten/Abokennzeichnung aus state.db: `KASSE.md` und `27-auftragskosten.json`.

Offen: keine erfolgreiche neue Gegenfall-Reproduktion (eigener Gerüstfehler; Wiederholungsfreigabe blockiert); keine Behebung der Codeabweichungen, kein neuer Vorbedingungs-Lauf. `OFFENE-PUNKTE-01.md` trennt notwendige Reparaturentscheidung und nächste Messung. Keine Schwelle wurde abgesenkt.

Für die Abnahme sind `DATEIEN.txt`, Manifest und vollständiges externes Abrufprotokoll maßgeblich. Kein historischer Abschlussbericht wird als frischer Lauf ausgegeben.
''')
# Basale Inventar-/Zählvalidierung vor dem Versiegeln.
rows=list(csv.DictReader((O/'MASTERPROMPT-ZEILEN-01.csv').open()));assert len(rows)==470 and {int(x['zeile']) for x in rows}==set(range(1,471))
with tarfile.open(O/'biotop/QUELLSTAND-01.tar.gz') as tar:
 members=[m for m in tar.getmembers() if m.isfile()]
 assert len(members)==u['gesamt']['dateien']
 for m in members:
  rel=m.name.removeprefix('biotop/');assert hashlib.sha256(tar.extractfile(m).read()).hexdigest()==next(x['sha256'] for x in J('03-dateien.json') if x['pfad']==rel)
S('ausgaben/28-abschlusskontrollen.json',{'zeit':now,'laufzeilen':23,'lauf_ids_vollstaendig':True,'masterpromptzeilen':len(rows),'masterprompt_luecken':0,'quellarchiv_dateien':len(members),'quellarchiv_bytegleich':len(members),'befundgruppen':reg['gruppenzahl'],'produktive_quellabdeckung':cov,'gegenfall_wiederholung':'blockiert, nicht wiederholt','quellen_pruefung':J('22-referenzpruefung.json')['gueltig']})
print(json.dumps({'bestand':stand,'hermes_abo_sitzungen':len(usage),'hermes_aufrufe_snapshot':sum(x['api_call_count'] or 0 for x in usage),'befundgruppen':reg['gruppenzahl'],'schlussbericht':str(O/'BERICHT.md')},ensure_ascii=False,indent=2))
