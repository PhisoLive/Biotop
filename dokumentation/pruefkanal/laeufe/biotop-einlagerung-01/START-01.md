# BIOTOP-EINLAGERUNG-01 · START-01

- **Kennung:** BIOTOP-EINLAGERUNG-01 (Auftrag von Chat-Claude im Auftrag von Philipp, 25.09.2026)
- **Beginn:** 25.09.2026 23:08:25 CEST, Eingang des Auftrags (state.db, Nachricht 27087; EB9)
- **Uhrzeit dieser Datei:** 25.09.2026 23:47 CEST
- **Status: IN ARBEIT**
- **Stillstand: ja.** Stillstandsprüfung 25.09.2026 23:24:14 CEST (EB2):
  - 0 Prozesse, 0 Container (laufend und gestoppt), 0 Subagenten, 0 Hintergrundprozesse von Hermes, keine Kammer-Sperre;
  - keine Crontab von root, keine systemd-Einheit und kein systemd-Zeitgeber mit Biotop-Bezug (EB2, EB5);
  - ein aktiver Hermes-Cron-Job mit Biotop-Bezug: der Zwischenbericht-Wächter 26fbb1513a1a. Er baut nichts; er legt nur Zwischenberichte ab. Sein Ziel war `laeufe/biotop-vor-t4-06/`. Er ist jetzt für die Dauer dieses Auftrags auf diesen Ordner umgestellt (EB10) und wird in Schritt 8 vom Biotop gelöst.
- **Stillstandsvermerk** in `/root/.hermes/memories/MEMORY.md` eingetragen (EB7); in `laeufe/gedaechtnis/STAND-03.md` folgt er in Schritt 8.

## Plan in fünf Zeilen

1. Stillstand prüfen und halten, Vermerk, Wächter auf diesen Auftrag (Schritt 1, erledigt bis auf die Endprüfung).
2. Git: `runde-5` auf `0c2f058`, Zweig `einlagerung/runde-6-stand` mit genau den 25 Einträgen, Markierung `eingelagert-20260925`; Vergängliches aus `/tmp` und Hermes-Zwischenspeichern kopieren und vergleichen (Schritte 2–3).
3. Dokumentation zusammenstellen: WIEDEREINSTIEG, INHALT, Masterprompt v1–v8, Verfassungen, Prüfkanal-Kopien, Verlauf, Umgebung, Gedächtnis (Schritt 4).
4. Packen (KOMPLETT, DOKUMENTATION, SHA256SUMS), wiederherstellen, Regression mit Kammer im entpackten Stand (Schritte 5–6).
5. Abholanleitung, P2, Wächter lösen, letzte Stillstandsprüfung, Abschlussordner, Meldung 2 (Schritte 7–8).

## Rohbelege

EB1–EB10 liegen bis zur nächsten Einstiegsdatei nur auf dem Server (`/root/biotop-einlagerung/rohbelege/`). Sie kommen gebündelt und geschwärzt mit der nächsten Einstiegsdatei in diesen Ordner.
