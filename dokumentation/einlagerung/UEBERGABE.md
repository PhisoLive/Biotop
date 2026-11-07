# UEBERGABE BIOTOP-EINLAGERUNG-01 (für jeden folgenden Turn und jeden Nachfolger)

- **Auftrag:** `/root/biotop-einlagerung/auftrag/BIOTOP-EINLAGERUNG-01-Auftrag.md` (Kopie des eingelegten Dokuments
  `/root/.hermes/cache/documents/doc_1414008da41a_BIOTOP-EINLAGERUNG-01-Auftrag.md`), Philipp 25.09.2026 ~23:08 CEST.
- **Arbeitsordner:** `/root/biotop-einlagerung/` (nicht öffentlich). Abschlussordner: `laeufe/biotop-einlagerung-01/`.
- **Rohbelege:** EB1, EB2 … in `rohbelege/EB0001.txt` …; jeder Befehl über
  `python3 /root/biotop-einlagerung/arbeit/eb.py "<Titel>" "<Befehl>" [<Anzeige>]`.

## Harte Regeln (Kurzfassung, Auftrag Abschnitt 2)
- Am Biotop nichts bauen/reparieren. Erlaubt: Sicherungscommit auf eigenem Zweig, Stillstandsvermerke, alles unter
  `/root/biotop-einlagerung/`, Abschlussordner, Gedächtnisdateien, P2.
- Nichts löschen/überschreiben außer P2-Verschiebung und eigenen Probe-Kopien/Containern (am Ende entfernen, belegen).
- Keine Biotop-Läufe, keine bezahlten Modellaufrufe. Regression der Probe ruft kein Modell.
- Kein Geheimnis in Prüfkanal/Meldung; Archive nie im Prüfkanal; Geheimnisdateien nicht in Archive.
- `git` nur mit `--no-optional-locks` für lesende Befehle (sonst schreibt `git status` den Index).
- Datenbanken nur lesend mit immutable (leere -wal) oder über Kopie; state.db mit mode=ro.
- Wortlaut-Dateien nie auf der Befehlszeile nennen (SPERRE-01 aus BIOTOP-LAGE-01).
- **Keine Subagenten, keine Wecker mit Biotop-Bezug** (Stillstandsvermerk; Auftrag Ziel 1).

## Stand (25.09.2026, CEST; neueste zuletzt)
- 23:19 Orientierung EB1: HEAD `0c2f058` auf `main`, 25 Einträge in `git status`, keine Markierungen, 4 Docker-Abbilder.
- 23:24 Stillstand am Anfang EB2: 0 Prozesse, 0 Container, 0 Subagenten, Kammer-Sperre fehlt; aktiv mit Biotop-Bezug
  nur der Wächter-Cron 26fbb1513a1a (über auftrag.json → biotop-vor-t4-06). EB5/EB6: Zeitgeber ohne Biotop-Bezug.
- 23:31 OpenRouter vorher EB3: usage 21,067113777 USD. Sicherungskopien EB4 (MEMORY.md, auftrag.json).
- 23:40 Stillstandsvermerk in MEMORY.md (EB7). P2 gelesen (EB8): Kennung in Z. 12 (chat_id, user_id).
- 23:47 Trockenlauf Wächter mit neuem Auftrag: 0 Treffer (EB9). Wächter umgestellt (EB10, auftrag.json → biotop-einlagerung-01,
  repos leer). START-01 veröffentlicht (EB11, 7aebba41…). **Meldung 1 gesendet** (EB12/EB13, message_id 8322) — NICHT erneut senden
  (Merkdatei `meldungen/meldung1.txt.gesendet`).
- NÄCHSTES: Schritt 2 (Git). Fundstellenliste aus BIOTOP-LAGE-01 lesen (AUFBAU FK38, INVENTAR I4/I5) → weitere Repos.
- 00:03 **Schritt 2 fertig.** EB14/EB15: 53 Repos außerhalb der LAGE-01-Probekopien, 6 mit nicht Eingechecktem. Selbsttest
  s2_git.py EB16 (sauber/Geheimnis/falsche Anzahl). /root/biotop: VORHER EB17 = R156 (EB18, 3.153, e67011b9…), Commit EB19
  `e8401afda590…` auf `einlagerung/runde-6-stand` (25 Einträge, Status sauber, main unverändert 0c2f058), runde-5 → 0c2f058,
  eingelagert-20260925 → e8401af; NACHHER EB20/EB21 = VORHER, Gegenprobe angeschlagen. Weitere 5 Repos EB23 (je Zweig
  `einlagerung/arbeitsstand-20260925` + Markierung, alle rc 0, Baum gleich): biotop-t3/repo-sicherung-vor-commits 2e71c554 (84),
  reparatur-01/teil-eichung/repo 6d60a5d9 (4), /tmp/r6-s2/baum b8c2f825 (2), baum2 5d6c4ee9 (2), baum3 a00e075f (2).
  Vorschau EB22: Tests nennen absolute Pfade (/root/biotop/daten, /root/reparatur-01, /root/biotop-t3/…, /root/biotop-vor-t4*,
  /root/versandwerk-t3-02, /root/.hermes/.env) → Probe braucht Bindungen über die Originalpfade.
- **Entscheidungen Hermes (für den Bericht):** (E1) Wächter-„repos“ leer (git status ohne --no-optional-locks schriebe den
  Index). (E2) Weitere Repos auch unter /tmp festgeschrieben (Auftrag: „weitere Repositorys“). (E3) WIEDEREINSTIEG/INHALT:
  Fassung 01 geht in KOMPLETT (vor der Probe), Fassung 02 mit Probe-Ergebnissen in DOKUMENTATION + Abschlussordner;
  DOKUMENTATION wird NACH der Probe gepackt (Abschnitt 5 Punkt 7 verlangt Rohbelege aus Schritt 6). (E4) Aus
  /root/sicherung/biotop-lage-01 zusätzlich ausgelassen: Reproduktionskopien sicherung/{stufe,probe,gegenprobe},
  testlauf/baum, tmp/db-*, tmp/inventar-db-*, tmp/node-compile-cache (Nachweis: Vergleich MANIFEST-PACKEN gegen neues Manifest).
- NÄCHSTES: Schritt 3 (Vergängliches), dann Schritt 4.
- 00:26 **Schritt 3 fertig:** /tmp → tmp-belege EB25 (233 Einträge, 24.869 von 24.869 Dateien gleich, 678.681.304 B, 0 Geheimnis;
  23 Werkzeug-/Systemeinträge ausgelassen); Zwischenspeicher EB26 (30 Delegationen + 3 Dokumente, alle mit Biotop-Bezug, alle
  gleich); RUNDE6-DOKUMENTE-01 EB28 (17 Quellen → 19 Dateien + VERZEICHNIS, 0 geschwärzt) veröffentlicht EB29 (20 von 20).
  Vorschau EB27 (Prüfkanal 21 Biotop-Ordner, Adresse 212.227.7.117, SSH nur Schlüssel). Geheimnis-Arten EB24.
- 00:27 **P2 umgesetzt (E5: vorgezogen vor das Packen)** EB30: Kopie ZWISCHENBERICHT-GESCHWAERZT-01.md (2 Stellen, 0 Treffer),
  Original nach entfernt-aus-pruefkanal/… verschoben (SHA gleich c96667d2…), alte Adresse 404, Kopie 200. In Schritt 8 Abrufprobe
  wiederholen.
- NÄCHSTES: Schritt 4 Dokumentation (d_pruefkanal.py, d_quellen.py, Verlauf, Umgebung, Gedächtnis, WIEDEREINSTIEG-01, INHALT-01),
  dann Schritt 5 (Paket, Hintergrund).
- 01:26 **Schritt 4 teilweise:** Prüfkanal-Kopien EB31 (21 Ordner, Schwärzung in Kopien: 30 Dateien, davon 24 nur
  „auth.active_provider“ = öffentlicher Anbietername, EB33; 2+2 Muster in native-mcp.md = Platzhalter aus dem Hermes-Paket,
  EB34), Masterprompt v1–v8/Aufträge/Verfassungen EB32 (46 von 46 bytegleich), Verlauf EB37 (1016 Nachrichten in 54 Teilen,
  27 Stellen in 14 Nachrichten geschwärzt), Umgebung EB38. Vorschau EB35/EB36 (Umfang, venvs, Testmarker).
  Selbsttest s5_paket.py EB40 (Skriptfehler in Protokollausgabe, rc 1) → korrigiert → EB41 grün (Auslassungen, WAL-Backup,
  Originale unverändert, Geheimnissuche-Gegenprobe angeschlagen, Probe leer, Gegenprobe genau 1 Datei).
- 01:27 **Kette A läuft im Hintergrund** (proc_3cbf595272a9, Protokoll protokolle/kette-a.log): dbliste + stufe 1–5
  (Teil 5 = /usr/local/lib/hermes-agent ohne venv; Entscheidung E6: Hermes-Agent-Quelle mitsichern, LU93).
  Entscheidung E7: aus /root/.hermes ausgelassen: node/, lsp/, bin/ (Laufzeitinstallationen), cache/ + *_cache.json
  (Zwischenspeicher; Biotop-Teil liegt in hermes-zwischenspeicher/), .env*, auth.json.
- NÄCHSTES (während Kette A): REGELN-02, STAND-03 (Entwurf), WIEDEREINSTIEG-01, INHALT; danach Kette B: stufe 6-einlagerung,
  kammer (docker save), integritaet, geheimsuche, packen, probe, gegenprobe, altabdeckung; dann Schritt 6 (Regression).
- 01:29 Kette A fertig (EB42–EB47): 3.028 Datenbanken im Umfang; stufe 1 (3.958 Dateien + 1 DB), 2 (30.898 + 2.171 DB,
  1.479 Verweise), 3 (1.362 + 24 DB; altes Archiv + Reproduktionen ausgelassen), 4 (971 + 5 DB), 5 (12.953). 0 verschwunden.
  Kassenstand VORHER EB48 (Kopien in tmp/kasse-vorher). Adresse/SSH EB50 (212.227.7.117, root nur Schlüssel).
- 02:00 REGELN-02/STAND-03 gebaut (EB49, paket/dokumentation/gedaechtnis/), WIEDEREINSTIEG Fassung 01 (EB51 Abbruch Wortlaut-
  Abgleich, EB52 gebaut, 3 Teile). Werkzeuge: d_bauen.py (Vorlagen mit Wortlaut-Platzhaltern), d_inhalt.py, s5_inhalt01.py,
  wa_vergleich.py (Wiederaufnahme-Vergleich). Geheimnissuche dokumentation EB53: 0 Befunde, Gegenprobe angeschlagen.
  Entscheidung E8: Datum 20260925 für Archivnamen (= Markierung eingelagert-20260925, Stillstandsvermerk 25.09.).
- 02:03 **Kette B läuft** (protokolle/kette-b.log): stufe 6, kammer, INHALT-01, integritaet, geheimsuche. Danach Hermes liest
  die Geheimnissuche → ggf. Aussonderung → Kette C: packen, probe, gegenprobe, altabdeckung.
- 02:05 Kette B fertig: stufe 6 EB54, docker save EB55 (124.908.915 B < 3 GB → in KOMPLETT), INHALT-01 EB56, integrity 3.028 von
  3.028 ok EB57, Geheimnissuche Zwischenstand EB58 (192 Dateien mit Befund; Einordnung EB60: 89 Hermes-Agent-Testdaten/Beispiele,
  ~100 Dateien mit Philipps Telegram-Kennung in privaten Protokollen (KOMPLETT ist privat, Auftrag Schritt 7.6), 1 erfundener
  Gegenproben-Schlüssel aus LAGE-01, Platzhalter in native-mcp.md; 1 ZUGANG: request_dump …055836… mit auth.json account_id
  → E9 ausgesondert (Kette C Schritt 1). Vorschau 5 EB59 (uv-Zwischenspeicher hat die 5 Pakete; 0 Container; unshare ok).
- 02:10 **Kette C läuft** (protokolle/kette-c.log): aussondern → packen → ORIGINAL VORHER-PROBE → probe → gegenprobe →
  integritaet (entpackt) → s6_git.sh → altabdeckung. Danach: s6_einrichten.sh (venv offline, docker load), Probe-Isolation
  prüfen (s6_probe.sh pruefen), Regression (Kette D, s6_probe.sh test … tests/ -m "not integration"), rote Tests an zweiter
  Kopie aus /root/biotop, ORIGINAL NACHHER-PROBE + vergleich, Aufräumen (probe/entpackt, gegenprobe, zweitkopie, tmp-*).
  Werkzeuge Probe: s6_original.py, s6_innen.sh, s6_probe.sh, probe-bin/docker (Wächter: -v nur unter probe/), s6_einrichten.sh.
- 02:13 Kette C fertig: E9 ausgesondert EB61; KOMPLETT 1. Versuch EB62 (998.459.631 B, SHA 11ed18d4…, 124.222 Einträge);
  ORIGINAL VORHER-PROBE EB63 (46.605 Einträge, Liste pruefsummen/ORIGINAL-VORHER-PROBE.txt); Probe EB64 (Unterschied leer,
  124.221 = 124.221); Gegenprobe EB65 (genau README.md gemeldet); integrity EB66 (3.028 von 3.028 ok); Git EB67 (wie verlangt,
  Refs gleich, fsck rc 0); Altabdeckung EB68 (72.223 von 75.214 per SHA; 2.991 nicht: Abhängigkeiten/Cache/neuerer Stand/…
  und var/pruefkanal/oeffentlich 14 Dateien = geschwärzte Prüfkanal-Dateien).
- 02:16 **Entscheidung Hermes E10:** Die 26 in dokumentation/pruefkanal geschwärzten Prüfkanal-Dateien (EB31) kommen zusätzlich
  unverändert unter ihrem Originalpfad in KOMPLETT (Teil 7; sonst fehlte ihr Wortlaut im Paket; KOMPLETT ist privat).
  Erster Packversuch beiseite (verschoben nach verworfen/komplett-01, paket/verworfen-01, probe-verworfen-01 — nicht gelöscht;
  probe-verworfen-01 ist Probe-Kopie → am Ende entfernen). **Kette C2 läuft** (protokolle/kette-c2.log): beiseite, stufe 7,
  geheimsuche, packen, probe, gegenprobe, integritaet, git, altabdeckung, fundstellen. Danach Kette D (arbeit/s6_kette_d.sh).
- 02:21 **Kette C2 fertig:** beiseite EB69; stufe 7 EB70 (26 Originale); Geheimnissuche EB71 (0 Geheimnisdateien, 0 ZUGANG-Befunde,
  193 Dateien mit Befund: MUSTER 96, KENNUNG 97, SONST 17; Gegenprobe angeschlagen); **KOMPLETT EB72: 998.531.281 B, SHA-256
  343b2d6aeac67d187ff007849a47220e90b112ade1442956627295d8494a9a78, 124.282 Einträge (87.317 Dateien, 34.533 Ordner, 2.432 Verweise),
  tar -t 124.283 (+ Manifest)**; Probe EB73 leer; Gegenprobe EB74 genau README.md; integrity EB75 3.028 von 3.028 ok; Git EB76 wie
  verlangt; Altabdeckung EB77 (72.237 von 75.214); **Fundstellen EB78: 186 von 186 (184 im Paket, 1 ausgelassen mit Grund, 1 nicht
  gefunden /tmp/werk-ohne-tests-xf0aaqmv/w), 0 fehlend** (Liste paket/FUNDSTELLEN-ABGLEICH.tsv).
- 02:27 PRUEFUNG-02 (Sicherheitsscan, freigegeben, keine Sperre): sperren/PRUEFUNG-02-freigegeben.txt. Ab jetzt Schleifen nur als
  Skriptdatei. **Kette D läuft** (proc_e482e491f1bb, protokolle/kette-d.log): einrichten, pruefen, Regression (Runde 5: 598 passed,
  2 skipped, 93 deselected in 2457.93s → erwartet ≥ 41 min), Auswertung (s6_auswerten.py → probe-belege/lauf-entpackt/).
- Kosten: OpenRouter vorher EB3 usage 21,067113777 USD. Nachher mit arbeit/kosten.py <marke>.
- 03:11 **Kette D fertig:** EB79 einrichten (venv offline 5 Pakete, docker load Kennungen gleich), EB80 Abschottung (28 Einhängungen,
  kein Netz, .env/auth.json verdeckt), EB81 Regression im entpackten Stand: **12 failed, 939 passed, 2 skipped, 93 deselected in
  2457.86s** (docker 1.418 Aufrufe, 0 verweigert), EB83 Auswertung: rot 10 test_w_g_* + 2 test_t3_bindung (VorspannFehler) →
  Maßstab „rot nur test_w_g_*“ NEIN. **Kette E** EB84–EB92: zweite Arbeitskopie aus /root/biotop, beide übrigen auch dort rot (EB86)
  → Befund des Stands; EB87 Regression schreibt .git/index (entpackt); EB88 Weg A wa_vergleich Original leer; EB89/EB90 Kasse
  36 von 36 gleich; EB91/EB92 Originale VORHER = NACHHER (46.605, leer).
- **Berichtigung:** docker save = 124.908.544 B (EB55), nicht 124.908.915 B (Zwischenstand-Meldung 02:25 falsch).
- 03:20 **Ketten F+G laufen** (arbeit/s78_ketten.sh; protokolle/kette-f.log, kette-g.log): E12 Belege → WIEDEREINSTIEG 02 → INHALT-02 →
  Geheimnissuche dok. → DOKUMENTATION packen/prüfen → SHA256SUMS+ABHOLANLEITUNG → Befundvergleich → Probe aufräumen → OpenRouter
  nachher → altes Archiv → Gedächtnis 03 → Wächter gelöst → Stillstand Ende. Danach: eb_buendeln.py, Bericht, START-02, pk.py,
  ab_abschluss.py dateien/abruf, Meldung 2 (hermes send, letzte Teilmeldung mit MEDIA-Anhängen).
