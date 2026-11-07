-- Reproduktion auf /root/reparatur-01/ausgang.db ausschließlich mode=ro.
-- Nicht als Skript gegen eine produktive Verbindung/CLI ausführen.
-- 1. DB-Status und Datumsgrenzen (Status ist kein laufender Prozess).
SELECT id,werk_id,status,begonnen_am,beendet_am,budget_eur FROM laeufe WHERE id IN (22,23,24,25) ORDER BY id;

-- 2. Jede Generation, Generation 0 ausdrücklich separat.
SELECT id,lauf_id,nummer,status,erstellt_am,freigabe_am,tag,pruefsumme,grund FROM generationen WHERE lauf_id IN (24,25) ORDER BY lauf_id,nummer;

-- 3. Kandidatenbestände sind nicht automatisch die Zahl regulärer Generationsteilnehmer.
SELECT lauf_id,generation,ist_probe,status,COUNT(*) AS anzahl FROM kandidaten WHERE lauf_id IN (24,25) GROUP BY lauf_id,generation,ist_probe,status ORDER BY lauf_id,generation,ist_probe,status;

-- 4. Echtes Ereignisleben einer Lauf-ID; frühe wiederverwendete ID 22 nicht mitmischen.
SELECT p.nr,p.zeit,p.art,p.inhalt FROM protokoll AS p JOIN laeufe AS l ON json_extract(p.inhalt,'$.lauf_id')=l.id WHERE l.id IN (22,23,24,25) AND p.zeit>=l.begonnen_am AND p.art IN ('lauf.angelegt','mass.eingefroren','generation.begonnen','generation.ergebnis','freigabe.frei','lauf.abgebrochen','entropie.gesaettigt') ORDER BY p.nr;

-- 5. Ansageentscheidungen: ausgeführt / bekannte Behauptung gesperrt / keine Behauptung.
SELECT json_extract(inhalt,'$.lauf_id') AS lauf,COUNT(*) AS gesamt,SUM(CASE WHEN json_extract(inhalt,'$.ausgefuehrt')=1 THEN 1 ELSE 0 END) AS ausgefuehrt,SUM(CASE WHEN json_extract(inhalt,'$.ausgefuehrt')=0 AND json_extract(inhalt,'$.behauptung') IS NOT NULL THEN 1 ELSE 0 END) AS bekannte_gesperrt,SUM(CASE WHEN json_extract(inhalt,'$.behauptung') IS NULL THEN 1 ELSE 0 END) AS keine_behauptung FROM protokoll WHERE art='aegis.ansage' AND json_extract(inhalt,'$.lauf_id') IN (24,25) GROUP BY lauf;

-- 6. Natürlicher C-Zustrom vs. belegte spätere Pfadproben. Schnitt nicht aus Name geraten:
-- #16010 beginnt die nachträglichen K2680-Mechanikproben laut Originalscripts/-akten.
SELECT json_extract(inhalt,'$.lauf_id') AS lauf,CASE WHEN nr>=16010 THEN 'gestellt_K2680' ELSE 'vor_Pfadproben' END AS population,art,json_extract(inhalt,'$.sperrart') AS stelle,COUNT(*) AS ereignisse FROM protokoll WHERE art IN ('immun.aufnahme_geprueft','immun.aufnahme_gesperrt','aegis.abweichung') AND json_extract(inhalt,'$.lauf_id') IN (24,25) GROUP BY lauf,population,art,stelle;

-- 7. Distinkte rote Behauptungen ohne falsche Gleichsetzung von Stelle und Fall.
SELECT DISTINCT json_extract(inhalt,'$.bereich') AS bereich,json_extract(inhalt,'$.behauptung') AS behauptung FROM protokoll WHERE art='immun.aufnahme_gesperrt' AND json_extract(inhalt,'$.lauf_id')=25 ORDER BY bereich,behauptung;

-- 8. Übernommenen Immunbestand und neue natürliche Einträge trennen.
SELECT id,lauf_id,werk_id,generation,bereich,name,status,erstellt_am,ursprung FROM immunsystem WHERE werk_id IN (21,22) ORDER BY werk_id,generation,id;

-- 9. Vorbehaltsschlüssel: mass Fassung ist keine eingefrorene Quellrevision.
SELECT id,json_extract(mass,'$.fassung') AS mass_fassung,json_extract(mass,'$.eingefroren_am') AS freeze,json_extract(mass,'$.grenzen') AS grenzen,mass FROM laeufe WHERE id IN (24,25) ORDER BY id;
SELECT * FROM eichung WHERE lauf_id IN (24,25);
SELECT * FROM eichkosten WHERE lauf_id IN (24,25);

-- 10. Kasse: Einzelzeilen statt gerundeter Berichtssummen; exakte Summation in Python Decimal(str()).
SELECT id,lauf_id,zeit,zweck,kosten_eur FROM kasse WHERE lauf_id IN (22,23,24,25) ORDER BY id;

-- 11. Antworten durch echte Aufruf-Referenz verbinden, nicht nach Ereignisreihenfolge.
SELECT a.nr AS aufruf_nr,a.zeit AS aufruf_zeit,json_extract(a.inhalt,'$.lauf_id') AS lauf,json_extract(a.inhalt,'$.zweck') AS zweck,b.nr AS antwort_nr,b.zeit AS antwort_zeit FROM protokoll AS a LEFT JOIN protokoll AS b ON b.art='modell.antwort' AND json_extract(b.inhalt,'$.aufruf_nr')=a.nr WHERE a.art='modell.aufruf' AND json_extract(a.inhalt,'$.lauf_id') IN (24,25) ORDER BY a.nr;

-- 12. Die zurückgenommenen Normprüfungen mit tatsächlichem Befund und Grund.
SELECT nr,zeit,inhalt FROM protokoll WHERE art='eichprobe.ergebnis' AND json_extract(inhalt,'$.probe')='norm' ORDER BY nr;

-- 13. Historische Tor-Aussage 54,5% ist keine neu zu definierende Kennzahl.
-- Historische Quelle: .../biotop-phase-4-vorbedingung-1/ausgaben/03-vorbedingung1-messung.txt Z.18.
-- Nutzerentscheidung separat aus state.db: SELECT id,session_id,role,timestamp,content FROM messages WHERE id=4317 AND role='user';
-- Ausgabe im Lieferpaket nutzerentscheidungen.json; keine anderen Chats/Konten exportieren.
