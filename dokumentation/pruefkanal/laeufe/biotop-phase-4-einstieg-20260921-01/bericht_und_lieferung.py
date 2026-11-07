"""Nur den gemessenen Lesestand dokumentieren und in neuem Ordner liefern."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from decimal import Decimal
import hashlib,json,os,grp,re,urllib.request

P=Path(__file__).resolve().parent
PUB=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe')
BASE='https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/'
REL='biotop-phase-4-einstieg-20260921-01/'
Q=PUB/REL
assert not Q.exists(), 'Kein Überschreiben einer Lieferung'
def lesen(n):return json.loads((P/n).read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def geld(s):return str(Decimal(s).quantize(Decimal('0.000001'))).replace('.',',')
b=lesen('BESTAND-AKTUELL.json'); k=lesen('KASSE-AKTUELL.json'); q=lesen('QUELLEN-UND-ABNAHME.json'); t=lesen('TRAEGER-AKTUELL.json'); l=lesen('LESEGRENZE.json'); betrieb=lesen('BETRIEB-AKTUELL.json')
zeit=datetime.fromisoformat(b['zeit_utc']).astimezone(ZoneInfo('Europe/Berlin')).isoformat()
master_rel='biotop-wiedereinstieg-2026-09-20-01/INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6-01.md'
master=(PUB/master_rel).read_text()
soll_organe=len(re.findall(r'^### 3\.\d+ ',master,re.M))
review=json.loads((PUB/'biotop-phase-4-vorbedingung-1/nach-reparatur-02/abschluss-02/REVIEW.json').read_text())
assert review['passed'] is True and review['abgeschlossen'] is True
review_anzahl=len(review['pruefpunkte'])
sha_unveraendert=sum(l['vorher'][n].get('sha256')==l['nachher'][n].get('sha256') and l['vorher'][n]['vorhanden']==l['nachher'][n]['vorhanden'] for n in l['vorher'])
assert sha_unveraendert==l['erfasste_pfade']

# Beobachtung aus dem tatsächlich zugestellten Referenzkontext dieses Antwortzuges.
# Kein Ersatz für einen HTTP-Mitschnitt; Referenztexte bleiben privat.
mitglieder=['[GESCHWÄRZT]:gpt-6-astra-900k[reasoning=max]','anthropic:claude-opus-5[reasoning=max]']
beobachtung={'quelle':'Im aktuellen Dialogzug zugestellter Mixture-of-Agents-Referenzkontext',
    'preset':'astra-opus-max','aggregator':'[GESCHWÄRZT]:gpt-6-astra-900k[reasoning=max]',
    'referenzlabels':mitglieder,'vorgesehene_referenzen':len(mitglieder),'vorliegende_nichtleere_textbeitraege':len(mitglieder),
    'grenze':'Beitragseingang im Dialog beobachtet. Keine neue externe Inferenzprobe und kein neuer HTTP-Wire-Mitschnitt; Modelllabels/Stufe nicht als unabhängig erneut auf dem Draht gemessen ausgeben. Inhalt der Hinweise muss gegen Quellen geprüft werden.'}
(P/'MOA-BEITRAGSEINGANG.json').write_text(json.dumps(beobachtung,ensure_ascii=False,indent=2)+'\n')

kopf=f'''# Phase 4 — lesender Einstieg, kein fachlicher Start

Messstand: {zeit}. Dieser Auftrag bestätigt Quellen und Bestand; er startet keine Phase, keinen Lauf, keinen Review, keine Modellprobe und keinen Verfassungsentwurf. Freigaben am echten Werk ausschließlich durch Philipp.

## Vollständig gelesen und gebunden
Die ausdrücklich genannte Abnahmeübergabe, die ausführliche Übergabe a–f aus abschluss-01, die Ergänzung aus abschluss-02 und der Masterprompt Fassung 6 wurden vollständig gelesen. Die überholten roten Abnahmesätze der alten Übergaben bleiben historische Wertungen und überschreiben die jüngste ausdrückliche Abnahme nicht.

Der alte lokale Cachepfad zum Masterprompt war nicht vorhanden. Verwendet wurde die in der vollständigen Übergabe selbst angegebene Prüfkanalkopie, vollständig bis Zeile {len(master.splitlines())}. Fassung 6 ist maßgeblich; abweichende ältere Skillangaben sind nicht maßgeblich.

'''
for src in q['https_quellen']:
    if src['pfad'].endswith('UEBERGABE-PHASE-4.md') or src['pfad']==master_rel:
        kopf+=f"- {src['url']}\n  {src['zeilen']} physische Zeilen, {src['bytes']} Bytes; SHA-256 `{src['sha256']}`; HTTPS/lokal bytegleich.\n"
kopf+=f'''
Insgesamt {sum(r['https_lokal_bytegleich'] for r in q['https_quellen'])} von {len(q['https_quellen'])} hier gebundenen HTTPS-Quellen bytegleich. Das ist keine Neuprüfung aller historischen Torläufe.

## 1. Biotop-Bestand, aktuell nachgezählt
- {b['eigene_dateien']} von {b['erfasste_pfade']} eigenen Quelldateien lesbar, {b['physische_zeilen']} physische Zeilen; davon {b['git_erfasst']} Git-erfasst und {b['eigene_dateien']-b['git_erfasst']} nicht ignorierte unversionierte Dateien.
- Python-Abgrenzung wie in der Übergabe: {b['python_dateien']} Dateien unter biotop/, tests/ und pruefung/, {b['python_physische_zeilen']} physische Zeilen. Keine neue SLOC-Zählmethode und keine Testausführung.
- {b['vergleich_gesamt_zur_uebergabe']['sha256_gleich']} von {b['vergleich_gesamt_zur_uebergabe']['alt']} Quellen SHA-identisch zur Übergabe; darin {b['vergleich_python_zur_uebergabe']['sha256_gleich']} von {b['vergleich_python_zur_uebergabe']['alt']} Pythonquellen. Keine zusätzlichen, fehlenden oder geänderten Dateien gegenüber dieser gebundenen Population.
- HEAD `{b['git_head']['stdout'].strip()}`. Der Arbeitsbaum ist nicht sauber; der vorhandene uncommittete Stand bleibt erhalten. `git status` zeigt 11 geänderte erfasste Dateien und fünf unversionierte Pfade, darunter das Verzeichnis tests/; Pfadzeilen und einzelne Dateien sind verschiedene Nenner. Vollständiger Status in BESTAND-AKTUELL.json.
- {soll_organe} fachliche Sollorgane nach Fassung 6, {len(b['organmodule_ohne_init'])} physische Organmodule ohne __init__.py. Existenz ist nicht aktueller Betrieb. Historische Organaufrufe stehen in der gebundenen ausführlichen Übergabe, sie wurden nicht wiederholt.
- Betriebssnapshot: {len(betrieb['biotop_marker_treffer'])} passende Biotop-Prozesse bei {betrieb['ps_zeilen']} erfassten ps-Zeilen; eigene Prozessahnen wurden ausdrücklich aus der Markersuche ausgeschlossen. Alte Mess-PID 1921606 nicht vorhanden, Dienst biotop.service not-found/inactive, docker ps leer. Keine neue HTTP-/Anmeldeprüfung.

## 2. Letzte Abnahme
**Vorbedingung 1 ist durch Philipp abgenommen; Tor 2 Zeile 8 erfüllt.** Abnahmevermerk: uebergabe-abnahme-01; Belegrevision: abschluss-02. Quote 1 von 11 = 9,09 %, bei denselben elf Testidentitäten. K2689: nur der Importname korrigiert, Testkörper/Assertions unverändert, 2 von 2 positive Ausführungen und 2 von 2 gültig an Assertions scheiternde Gegenproben historisch belegt. Vollständiger Nachtragsreview: passed=true, abgeschlossen=true, {review_anzahl} Prüfpunkte. Der frühere 180-Sekunden-Abbruch bleibt ein historischer Abbruch ohne Urteil.

Diese Ausführungen sind **aus den gebundenen Belegen nachgelesen, nicht in diesem Einstieg wiederholt**. Reparatur-02 bleibt abgenommen (305 von 305, 4 positive und 4 gültige Gegenfälle). Keine Gesamtfreigabe des Biotops, keine Freigabe für einen Handelslauf.

Manifest abschluss-02: `{q['manifeste'][0]['manifest_sha256']}`, {q['manifeste'][0]['gleich']} von {q['manifeste'][0]['geprueft']} manifestgebundenen Dateien lokal geprüft. Manifest der Abnahmeergänzung: `{q['manifeste'][1]['manifest_sha256']}`, {q['manifeste'][1]['gleich']} von {q['manifeste'][1]['geprueft']} gebundenen Dateien lokal geprüft. Die Manifeste selbst wurden zusätzlich über HTTPS abgeglichen.

## 3. Offene Befunde — nicht neu untersucht oder erledigt
- 19 bestätigte Außenleserorte: 11 in 11 Prüfskripten und 8 in 3 Produktdateien.
- Vier Phase-4-Lücken: Wirkungskreis einschließlich transitiver/kumulativ verhandelter Änderungen; Vertrags-/Verfassungsidentität Vorspann→Freeze; bereichsweises NaN/Null/Rauschen; tatsächlicher Gen0-Erfolg als Freeze-Bedingung.
- Suche unvollständig: 8 semantische Kandidaten sowie 45 breite ungeklärte Kandidatenzeilen. Keine zusätzlichen 53 bestätigten Fehler und keine Entwarnung.
- 9 von 11 Ansage-/Sache-Abweichungen bleiben eigener Auftrag erst **nach Vorbedingung 2**. Nicht mit der Doppelungsquote vermischen.
- Natürlicher Lauf ohne neuen bestätigten Behebungs-/Immunisierungsgegenstand. K2689-Nachholung ist keine rückwirkend neue natürliche Immunisierung.

Quelle: OFFEN.md aus abschluss-02 und die vollständige Liste der historischen Übergabe. Kein neuer Außenscan, keine Reparatur.

## 4. Kassenstand direkt aus SQLite, mode=ro
- Produktiv: {k['produktiv']['buchungen']} Buchungen, letzte ID {k['produktiv']['letzte_id']}, {geld(k['produktiv']['summe_eur_decimal'])} EUR.
- Privatbestand: {k['privat_lauf26']['buchungen']} Buchungen, letzte ID {k['privat_lauf26']['letzte_id']}, {geld(k['privat_lauf26']['summe_eur_decimal'])} EUR. Darin sind die {k['abgleich']['gemeinsame_identische_zeilen']} produktiven Buchungen identisch enthalten — Gesamtbeträge nicht addieren.
- Zusätzlicher natürlicher Lauf 26: {k['abgleich']['zusaetzliche_private_zeilen']} von {k['abgleich']['zusaetzliche_private_zeilen']} Buchungen (IDs 4071–4316), {geld(k['abgleich']['kosten_neu_eur_decimal'])} EUR von damals 3,00 EUR. Status {k['privat_lauf26']['lauf26']['status']}, beendet nach Generation 5.
- Nachtrag laut gebundener Kasse: keine neuen Biotop-Modellbuchungen, 0,00 EUR von damals 2,00 EUR. Die aktuell gelesenen Zähler entsprechen diesem Schlussstand.
- Produktive Läufe 24/25 stehen noch auf „bereit“; das ist kein laufender Prozess und kein Fortsetzungsauftrag.
- Keine neue Budgetfreigabe. Träger-, Review-, Host- und Abonnementkosten dieses Einstiegs monetär nicht ermittelt; nicht als null ausgewiesen.

## 5. Trägt astra-opus-max diese Unterhaltung?
**Ja als aktuelle Sitzungsbindung und als Verbund in diesem Antwortzug; keine pauschale Langcode-Garantie.** Nicht nur die globale Konfiguration, sondern der eigene Datensatz in state.db und der Routing-Eintrag der konkreten Telegram-Unterhaltung nennen `astra-opus-max` / `moa`. Die Modellbindung zeigt `moa://local`. Der laufende Dialog hat Textbeiträge beider benannter Referenzen geliefert ({len(mitglieder)} von {len(mitglieder)}); die Hinweise wurden gegen die Messquellen geprüft, nicht als Urteil übernommen.

Konfiguriert sind Astra-900k und Opus 5 als Referenzen, beide max; Astra-900k als Aggregator max; `fanout=user_turn`, `degraded_reference_policy=loud`. Diese Werte wurden frisch gelesen. **Kein neuer HTTP-Wire-Beleg für max, keine neue 900k-Anfrage und kein neuer Status-Kommando-/Lasttest** wurden für diesen Leseauftrag erzeugt. Für diese Sitzungs-ID liegt keine gespeicherte MoA-Trace-Datei vor. Ein gesetztes loud-Feld allein beweist keine robuste Ausfallbehandlung.

Gateway: {t['gateway']['stdout'].strip().replace(chr(10), '; ')}. Damit ist der frühere Gateway-Neustart inzwischen tatsächlich erfolgt; der alte offene Neustartstatus wird nicht fortgeschrieben.

**Aber technisch keine frische Sitzung:** Aktuelle ID `{t['aktuelle_sitzung']['id']}`, Routing `is_fresh_reset={str(t['routing'].get('is_fresh_reset')).lower()}`, `was_auto_reset={str(t['routing'].get('was_auto_reset')).lower()}`. Das ist weiterhin die alte Unterhaltung, kein neuer Kontextreset. `/restart` erneuert den Gateway, nicht die Unterhaltung. Für den verlangten frischen Phase-4-Kontext ist `/new` beziehungsweise `/reset` nötig; es wurde nicht eigenmächtig ausgelöst. Kein fachlicher Start unter der alten Kennung.

**Bekannte Betriebsgrenze:** Opus kann im Verbund bei großen Code-Eingaben mit cyber-Ablehnung ausfallen. Der konkret vorliegende frühere Großbeleg war synthetisches Füllmaterial, keine neu geprüfte Handelscode-Eingabe. Eine Ablehnung, ein leerer Beitrag oder ein Infrastrukturfehler zählt niemals als Beitrag — auch bei HTTP 200, message_stop oder erfolgreichem Aggregator. Der Verbund muss den Ausfall offen führen; dieser Einstieg implementiert keine neue Ausfallbehandlung und beansprucht dafür keine Abnahme.

## 6. Lesebereich und Halt
SHA/Vorhandensein blieben bei {sha_unveraendert} von {l['erfasste_pfade']} erfassten Pfadzuständen unverändert. Alle Metadaten blieben bei {l['unveraendert']} von {l['erfasste_pfade']} Zuständen gleich. Im SQLite-Lesefenster änderten sich ausschließlich die mtime-Werte der beiden -shm-Dateien; ihre Bytes/SHA blieben gleich. Diese Nebenwirkung wird nicht als völlig unverändertes Dateisystem ausgegeben. Keine Datenbankzeile, Produktquelle oder Trägerkonfiguration wurde durch diesen Auftrag geändert. LESEGRENZE.json enthält Vorher/Nachher.

**Nächster fachlicher Schritt bleibt ausschließlich Vorbedingung 2. Philipp schreibt und entscheidet die Verfassung des Handelssystems einschließlich des tragenden Orderpfads, der Risikomodule und der Verlustgrenze für den Eichgegenstand.** Fassung 6, Zeile 394: „ohne diesen Eintrag wartet das Organ und der Lauf beginnt nicht“. Kein spontaner Entwurf, keine Aufnahme/Landkarte, keine Eichung, keine Generation.

Es gelten weiterhin Abschnitt 2a, die F7-Sätze („Ein Nachweis zählt nur, wenn er ausgeführt wurde“; „Jede Probe braucht eine Gegenprobe, die fehlschlagen muss“), ein Reviewdurchgang je fachlichem Auftrag ohne Kaskade, Abschlussordner mit den Torbelegen statt allen Zwischenstufen und Freigaben am echten Werk ausschließlich durch Philipp. Die Übungswerk-Vollmacht wird nicht übertragen.

## Abholung dieses Lesestands
{BASE}{REL}DATEIEN.txt
'''
(P/'ZWISCHENBERICHT.md').write_text(kopf)
(P/'KASSE.md').write_text(f'''# Kasse — lesender Einstieg

Direkte SQLite-RO-Abfrage, Stand {zeit}. Vollständige Summen/Zeilenbindung in KASSE-AKTUELL.json; neue historische Lauf-26-Zeilen in LAUF26-BUCHUNGEN.json.

- Produktiv: {k['produktiv']['buchungen']} Buchungen; {geld(k['produktiv']['summe_eur_decimal'])} EUR.
- Privat: {k['privat_lauf26']['buchungen']} Buchungen; {geld(k['privat_lauf26']['summe_eur_decimal'])} EUR.
- Überlappung: {k['abgleich']['gemeinsame_identische_zeilen']} von {k['produktiv']['buchungen']} Produktivzeilen im Privatbestand identisch. Nicht addieren.
- Zusatz im Privatbestand: {k['abgleich']['zusaetzliche_private_zeilen']} Buchungen, {geld(k['abgleich']['kosten_neu_eur_decimal'])} EUR (Lauf 26; damaliges Budget 3 EUR).
- Nachtrag historisch: 0 neue Biotop-Modellbuchungen, 0 EUR (damaliges Budget 2 EUR).
- Dieser Einstieg: keine Biotop-Modell-/Kammer-/Generationsaufrufe; DB-Inhalte im gemessenen Vorher/Nachher-Fenster unverändert. Kein neues Budget freigegeben.

Die ausführende Hermes-/MoA-Unterhaltung verbraucht Trägerkontingent. Dessen monetäre Kosten sowie Host-/Reviewkosten wurden nicht bestimmt. Keine Nullkostenbehauptung über den Gesamtauftrag. Decimal-Summen dienen der reproduzierbaren Rechnung auf gespeicherten Werten; kein Rechnungsbeleg des Anbieters.
''')

namen=['ZWISCHENBERICHT.md','KASSE.md','BESTAND-AKTUELL.json','KASSE-AKTUELL.json','LAUF26-BUCHUNGEN.json','QUELLEN-UND-ABNAHME.json','TRAEGER-AKTUELL.json','MOA-BEITRAGSEINGANG.json','BETRIEB-AKTUELL.json','LESEGRENZE.json','MESSAUSGABE.json','stand_lesen.py','bericht_und_lieferung.py','DATEIEN.txt','MANIFEST.sha256','PRUEFSUMME-ORDNER.txt']
(P/'DATEIEN.txt').write_text('Lesender Einstieg Phase 4 — keine Freigabe und kein fachlicher Start\n\n'+'\n'.join(BASE+REL+n for n in namen)+'\n')
payload=[n for n in namen if n not in ('MANIFEST.sha256','PRUEFSUMME-ORDNER.txt')]
manifest=''.join(sha((P/n).read_bytes())+'  '+n+'\n' for n in payload)
(P/'MANIFEST.sha256').write_text(manifest)
manifest_sha=sha(manifest.encode())
(P/'PRUEFSUMME-ORDNER.txt').write_text(manifest_sha+'  MANIFEST.sha256\n')
gid=grp.getgrnam('caddy').gr_gid
Q.mkdir(mode=0o750);os.chown(Q,-1,gid)
for n in namen:
    target=Q/n
    with target.open('xb') as f:f.write((P/n).read_bytes())
    os.chmod(target,0o640);os.chown(target,-1,gid)
checks=[]
for n in namen:
    with urllib.request.urlopen(BASE+REL+n,timeout=30) as r:data=r.read();status=r.status
    gleich=status==200 and data==(P/n).read_bytes()
    checks.append({'datei':n,'status':status,'bytegleich':gleich,'sha256':sha(data)})
    assert gleich,n
out={'bericht':BASE+REL+'ZWISCHENBERICHT.md','dateiliste':BASE+REL+'DATEIEN.txt','manifest_sha256':manifest_sha,'http_bytegleich':sum(r['bytegleich'] for r in checks),'http_dateien':len(checks),'pruefungen':checks,'phase4_fachlich_gestartet':False}
(P/'LIEFERUNG.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
