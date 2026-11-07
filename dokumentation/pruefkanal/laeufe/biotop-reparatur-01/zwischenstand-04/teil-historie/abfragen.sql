-- Ausschließlich SELECT auf eingefrorener SQLite, zu öffnen mit mode=ro.

-- laeufe
SELECT * FROM laeufe WHERE id IN (22,23,24,25) ORDER BY id;

-- werke
SELECT id,name,pfad,quelle,aufgenommen_am,sprache,status FROM werke WHERE id IN (11,19,20,21,22) ORDER BY id;

-- generationen
SELECT * FROM generationen WHERE lauf_id IN (22,23,24,25) ORDER BY lauf_id,nummer;

-- kandidaten
SELECT id,lauf_id,generation,bereich,nische,anbieter,modell,status,grund,erstellt_am,ist_probe FROM kandidaten WHERE lauf_id IN (22,23,24,25) ORDER BY id;

-- kasse
SELECT * FROM kasse WHERE lauf_id IN (22,23,24,25) ORDER BY id;

-- immunsystem
SELECT id,werk_id,lauf_id,bereich,name,ursprung,status,erstellt_am,generation FROM immunsystem WHERE werk_id IN (11,19,20,21,22) ORDER BY id;

-- lazarus
SELECT id,lauf_id,generation,tag,archiv,pruefsumme,erstellt_am FROM lazarus WHERE lauf_id IN (22,23,24,25) ORDER BY id;

-- eichung
SELECT * FROM eichung WHERE lauf_id IN (22,23,24,25) ORDER BY id;

-- eichkosten
SELECT * FROM eichkosten WHERE lauf_id IN (22,23,24,25) ORDER BY id;

-- mentor
SELECT * FROM mentor WHERE lauf_id IN (22,23,24,25) ORDER BY id;

-- protokoll_sicher
SELECT nr,zeit,art,inhalt FROM protokoll WHERE nr>=12400 AND art NOT LIKE 'anmeldung.%' AND art NOT LIKE 'benutzer.%' AND art NOT LIKE 'token.%' ORDER BY nr;
