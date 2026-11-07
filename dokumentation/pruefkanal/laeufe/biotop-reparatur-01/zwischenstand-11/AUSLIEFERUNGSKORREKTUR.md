# Auslieferungskorrektur gegenüber Zwischenstand10

Zwischenstand10 war nicht vollständig abholbar: 2420 von 2422 HTTPS-Abrufen waren bytegleich; die beiden .gitignore-Adressen lieferten404. Seine bereits versiegelten Dateien bleiben unverändert.

Dieser neue Ordner erhält alle Originalbytes unter expliziten Downloadaliasen und in PUNKTDATEIEN.tar.gz mit den Originalpfaden; siehe DOWNLOAD-ZUORDNUNG.json. Keine Serverkonfiguration wurde geändert. Der Fehlversuch wird nicht als erfolgreiche Vollveröffentlichung gewertet.

Bei der Vorbereitung waren außerdem ein falscher Inventarpfad und die Verwechslung von Kurz-Ausgabe und Rohdaten-Schema (Status, Buchungsliste, stderr-Datei) zu korrigieren. Diese Paketbauer-Aufrufe scheiterten vor der Versiegelung; die fehlerhaften Stellen wurden nicht übergangen. Keine Produktdatei, keine Messausgabe und kein Test-Sollurteil wurde dafür verändert; keine zusätzliche Kammer gestartet.
