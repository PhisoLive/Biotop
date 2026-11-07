"""Originalaudit nachvollziehen und enge Reparaturzuordnung daneben führen, nichts wegkategorisieren."""
from pathlib import Path
from collections import Counter
import hashlib,json
P=Path('/root/reparatur-01');A=P/'nachweis-leserpruefung-02/audit';O=P/'audit-elternabgleich';O.mkdir(exist_ok=False)
def lade(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aus(f,d):(O/f).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
quellen={z['pfad']:z for z in lade(P/'nachweis-leserpruefung-02/QUELLEN.json')};dateien=lade(A/'DATEIPRUEFUNG.json');leser=lade(A/'LESESTELLEN.json');befunde=lade(A/'BEFUNDE.json');ab=lade(A/'ABDECKUNG.json');treffer=lade(A/'SUCHTREFFER-ZUORDNUNG.json')
assert len(quellen)==len(dateien)==ab['inventar_dateien'] and {z['pfad'] for z in dateien}==set(quellen)
assert len(leser)==len({z['id'] for z in leser})==ab['semantische_lesebloecke']
assert len(befunde)==len({z['id'] for z in befunde})==ab['deduplizierte_bestaetigte_mechanismen']
ld={z['id']:z for z in leser};bd={z['id']:z for z in befunde}
for z in dateien:
    assert z['sha256']==quellen[z['pfad']]['sha256']==sha(P/'review-02/repo'/z['pfad'])
    assert set(z['lesestellen'])<=set(ld) and set(z['befunde'])<=set(bd)
for z in leser:
    text=(P/'review-02/repo'/z['pfad']).read_text().splitlines();von,bis=z['zeile_von'],z['zeile_bis']
    assert 1<=von<=bis<=len(text),(z['id'],von,bis,len(text))
    assert z['quellen_sha256']==quellen[z['pfad']]['sha256']
    assert z['quellbeleg']=='\n'.join(f'{i}|{text[i-1]}' for i in range(von,bis+1)),z['id']
    assert set(z['befunde'])<=set(bd)
assert dict(Counter(z['gruppe'] for z in dateien))==ab['gruppen']
assert dict(Counter(z['kernpfadbezug']['klasse'] for z in leser))==ab['scope_lesebloecke']
assert sum(ab['kandidatenzeilen_status'].values())==ab['breite_kandidatenzeilen']
# Originalurteile bleiben vollständig bestehen. Nur Arbeitsauftrag daneben abgrenzen.
aussen_zusaetzlich={'O01','G01','G02','G03','G04','L06','L08','L09'}
kernbelege={'B01':['53-aegis2-eltern-rot','54-aegis2-eltern-gruen','55-skip-eltern-gruen','58-leser2-eltern-rot','59-leser2-eltern-gruen','61-vertragszeugen-integration-gruen'],
'B02':['53-aegis2-eltern-rot','54-aegis2-eltern-gruen'],
'B03':['58-leser2-eltern-rot','59-leser2-eltern-gruen'],
'B04':['58-leser2-eltern-rot','59-leser2-eltern-gruen'],
'B05':['58-leser2-eltern-rot','59-leser2-eltern-gruen'],
'B09':['58-leser2-eltern-rot','59-leser2-eltern-gruen'],
'B10':['53-aegis2-eltern-rot','54-aegis2-eltern-gruen','56-aegis2-kern-und-eichpaare']}
zuordnung=[];aussen=[]
for b in befunde:
    for ort in b['orte']:
        ident=ort['id'];auss=ld[ident]['kernpfadbezug']['klasse']=='ausserhalb_kern' or ident in aussen_zusaetzlich
        r={'id':b['id']+':'+ident,'audit_befund':b['id'],'audit_leser':ident,'titel':b['titel'],'pfad':ort['pfad'],'originalzeilen':[ort['zeile_von'],ort['zeile_bis']],'original_sha256':ort['sha256'],'original_audit_scope':ort['kernpfadbezug']['klasse'],'originalbeleg':{'datei':'audit/LESESTELLEN.json','id':ident,'quellbeleg':ld[ident]['quellbeleg']},'bestaetigungsart':'statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall','mechanismus':b['dedup_mechanismus'],'minimalbeleg':b['minimalbeleg']}
        if auss:
            r.update(reparaturzuordnung='ausserhalb_der_eingegrenzten_Runde',status='bestaetigt_offen',repariert=False,ziel='Eigener Folgeauftrag nach Kernabschluss/Entscheidung',grund='Historischer Parallelprüfer ohne Rückfluss in aktuellen Pflichtvorspann' if ident not in aussen_zusaetzlich else 'Versiegelte Kerneingrenzung02: Aufnahme/Gen0-Produzenten und leere Herstellerantwort nicht integrieren; kein Durchgriff auf P4-Freeze-Erfolgsbindung.')
            if ident in {'G01','G03'}:
                r['zusaetzlicher_ausfuehrungsbeleg']='verbraucher/belege/03-gen0-fang-rot/junit.xml; vor Scope-Reduktion ausgeführt, Teilfix quarantänisiert und nicht als erledigt übernommen'
            aussen.append(r)
        else:
            assert b['id'] in kernbelege,(b['id'],ident)
            r.update(reparaturzuordnung='eingegrenzter_Kern_oder_sein_Eigennachweis',status='Kernschutz_integriert_Elterneigensuite_belegt_Schlussreview_offen',elternbelege=kernbelege[b['id']],beleggrenze='Produzentenschutz oder gezielter Verbraucherfall; keine Behauptung, jeder Ort sei separat end-to-end ausgeführt.')
        zuordnung.append(r)
assert len({z['id'] for z in zuordnung})==len(zuordnung)
assert len({z['audit_leser'] for z in aussen})==len(aussen)
verbraucher=lade(P/'nachbesserung-02/verbraucher/lieferung/BEFUNDE.json')['lesestellen']
alias={'AUSSEN-VERHANDLUNG-LEERE-ANTWORT':['B08:L06'],'AUSSEN-GEN0-FANG':['B06:G01','B06:G03'],'AUSSEN-GEN0-AEQUIVALENZ':['B07:G02'],'AUSSEN-GEN0-TESTBAU':['B06:G04'],'AUSSEN-AUFNAHME-TESTLAUF':['B05:O01'],'AUSSEN-LEGACY-FUND':['B05:P11'],'AUSSEN-LEGACY-VERHANDLUNG':['B09:P41'],'AUSSEN-LEGACY-TOR2':['B09:P46']}
for z in verbraucher:
    if z['id'].startswith('AUSSEN-') and 'bestätigt offen' in z['urteil']:
        assert z['id'] in alias,z['id']
        for ziel in alias[z['id']]:
            r=next(a for a in aussen if a['id']==ziel);r.setdefault('verbraucher_alias',[]).append(z)
aus('BEFUNDZUORDNUNG.json',zuordnung);aus('AUSSERHALB-KERN-BESTAETIGT-OFFEN.json',aussen)
aus('VERBRAUCHER-ALIASSE.json',alias)
aus('ZUSAETZLICHE-OFFENE-HINWEISE.json',[z for z in verbraucher if z['id']=='AUSSEN-AUFNAHME-BAU'])
s={'original_abdeckung_unveraendert':ab,'eltern_quellhashes_geprueft':len(dateien),'eltern_quellbereiche_bytegleich_geprueft':len(leser),'befundorte_zugeordnet':len(zuordnung),'befundort_status':dict(Counter(z['reparaturzuordnung'] for z in zuordnung)),'aussen_orte':len(aussen),'aussen_dateien':len({z['pfad'] for z in aussen}),'aussen_historische_pruefdateien':len({z['pfad'] for z in aussen if z['pfad'].startswith('pruefung/')}),'aussen_produkt_orte':sum(not z['pfad'].startswith('pruefung/') for z in aussen),'suche_semantisch_vollstaendig':False,'wichtig':'Die originale breite Audit-Scopezählung wird nicht still ersetzt. Die zweite Spalte benennt ausschließlich den engeren Reparaturauftrag; bestätigt offen bedeutet nicht repariert. Statischer Befund ist keine Behauptung seines Auftretens in einer aktuellen DB.'}
aus('ABGLEICH.json',s)
(O/'AUSSERHALB-KERN-BESTAETIGT-OFFEN.md').write_text('# Außerhalb Kern — bestätigt offen\n\n'+f'{len(aussen)} benannte Leserorte in {len({z["pfad"] for z in aussen})} Dateien; davon {s["aussen_historische_pruefdateien"]} historische Prüfdateien und {s["aussen_produkt_orte"]} weitere Produktleserorte. Keine Fehleranzahl des gesamten Biotops. Alle Einträge sind offen für einen eigenen Folgeauftrag; kein Quarantäne-Teilfix gilt als Erledigung. Bestätigungsart und Originalquelltext stehen pro Eintrag in JSON.\n\n'+''.join(f'## {z["id"]} — {z["titel"]}\n\n`{z["pfad"]}:{z["originalzeilen"][0]}–{z["originalzeilen"][1]}` (Originalstand)\n\n- Status: **bestätigt offen**, nicht repariert.\n- Bestätigung: {z["bestaetigungsart"]}\n- Mechanismus: {z["mechanismus"]}\n- Grenze: {z["grund"]}\n- Originalbeleg: audit/LESESTELLEN.json, {z["audit_leser"]}; SHA {z["original_sha256"]}.\n\n' for z in aussen)+'Die vier bestehenden P4-Mechanismen bleiben eine separate offene Liste. Acht semantische Originalkandidaten und45 breite Quellzeilen sind weiterhin ungeklärt; außerdem steht der Aufnahmestart-Hinweis des Verbraucherteils getrennt, nicht als bestätigter Fehler. Keine Vollständigkeitsentwarnung.\n')
(O/'BERICHT.md').write_text('# Elternabgleich des Originalaudits\n\n'+json.dumps(s,ensure_ascii=False,indent=2)+'\n\nDie Originaldateilesung ist die dokumentierte Leistung des Auditagenten. Parent hat hier Hashes, Originalquellbereiche, Mengen und Referenzen nachgerechnet, nicht eine zusätzliche vollständige semantische Prüfung behauptet. Die breite Auditklassifikation umfasst auch Vorstufen und Anzeigen. BEFUNDZUORDNUNG.json erhält jede Originalzuordnung und stellt den engeren Reparaturauftrag ausdrücklich daneben.\n')
print(json.dumps(s,ensure_ascii=False))
