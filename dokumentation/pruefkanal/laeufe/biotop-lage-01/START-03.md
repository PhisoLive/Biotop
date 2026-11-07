# BIOTOP-LAGE-01 · Fassung 2 · START-03

- **Kennung:** BIOTOP-LAGE-01
- **Fassung:** 2
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST, das Ende des Baus S1c
- **Uhrzeit dieser Datei:** 25.09.2026 21:09:29 CEST
- **Status: TEILWEISE.**
  - Nicht erfüllt ist Punkt 7 von Abschnitt 10: Im Ordner liegt, gesperrt, eine Datei mit Philipps Telegram-Kennung.
  - Nur teilweise erfüllt sind die Punkte 1, 3 und 11 (Abschnitt 3 unten).
- **START-03 ersetzt START-02 als Einstieg.** START-02 gilt weiter für seine Abschnitte A–G: Nachsteuerung, Berichtigungen, Nachrichtenzählung, Abweichungen A1–A8, Kosten, `/root/versehentlich`, `stufe2.py`.

## 1. Lage in fünf Sätzen

1. Es gilt Masterprompt Fassung 8 vom 23.09.2026. Das Biotop steht in Phase 4, dem Breitentest: T3 lief in den Läufen 26–38 und ist nicht abgenommen; T4 bis T6 sind nicht begonnen (LAGE-TEIL3-01.md, FK23 und FK25).
2. Vom 23. bis 25.09. liefen sechs Behebungsrunden vor T4, ohne Lauf und ohne Modellgeld. Keine ist abgenommen; der letzte Commit ist `0c2f058` aus Runde 5 (TORE-TEIL3-01.md §3).
3. Zum Stichzeitpunkt endete der Bau S1c der Runde 6 an seiner Iterationsgrenze. A–F sind gebaut; der neue stille Durchlass „Befund G“ steht nur als rote Spezifikation da. Nach der Startregel ist T4 deshalb nicht frei, und Runde 6 ruht, bis Philipp entscheidet (LAGE-TEIL1-01.md).
4. Die Kasse führt 6.919 Buchungen für 18,814735 €, davon 9,728638 € für T3. Seit dem 22.09. um 21:26:08 gab es keine Biotop-Buchung (CHRONIK-TEIL3-01.md; R218).
5. Die Sicherung ist gepackt, wiederhergestellt und verglichen: Unterschied leer, Gegenprobe angeschlagen. `/root/biotop` ist vorher und nachher gleich. Das Archiv liegt aber nur auf diesem Server (SICHERUNG-TEIL1-01.md).

## 2. Zählung der Antworttafel

- **Beantwortet 69 von 69:** 50 Fragen und 19 Punkte des Wissensstands.
- **UNBEKANNT als ganze Antwort:** 0.
- **Lückenliste:** 92 Nummern. 86 sind offen und haben eine Zuständigkeit (Hermes 44, Philipp 21, Chat-Claude 21), 6 haben keine.
- **Offene Punkte nach FK39:** 36.
- **Tafel:** VOLLSTAENDIGKEIT-TEIL1-01.md. **Lücken:** VOLLSTAENDIGKEIT-TEIL2-01.md.

## 3. Abschnitt 10: Stand je Punkt

| Punkt | Stand | Beleg |
|---|---|---|
| 1 Jede Datei aus Meldung 2 abrufbar | **teilweise**: Jede Datei steht mit Adresse in Meldung 2 und in DATEIEN-TEIL1-03 und DATEIEN-TEIL2-03. Eine Datei liefert absichtlich HTTP 403 (A4) | ABRUFPROBE-03 |
| 2 Antworttafel vollständig | erfüllt: 69 von 69; jedes UNBEKANNT hat Grund und Weg | VOLLSTAENDIGKEIT-TEIL1 §1 |
| 3 Abgleich ohne unerklärte Abweichung | **teilweise**. Erfüllt: Laufnummern, Fassungen, 75 von 75 Commits, 202 von 202 Dateien, Gegenprobe angeschlagen. Offen: Die Differenz Kasse gegen OpenRouter ist nur nach möglichen Ursachen erklärt (LU85); 11 Laufnummern in Ordnertexten sind ungeklärt (LU82) | INVENTAR-TEIL2 Abgleiche 1–9 |
| 4 Tagesbilanz vollständig | erfüllt: jeder Tag mit Zahl oder `NICHT ABGEDECKT`; die Spanne steht in LU86 | INVENTAR-TEIL2 Abgleich 7 |
| 5 Register trennt die Urheber | erfüllt; unbestätigte Vorentscheidungen stehen gesondert | ENTSCHEIDUNGEN-TEIL2 FK17 |
| 6 Wiederherstellungsprobe | erfüllt: 111.440 = 111.440 Einträge, Unterschied leer, Gegenprobe angeschlagen, `integrity_check` 3.004 von 3.004 ok. Tests im entpackten Stand nur ohne Kammer (LU89) | SICHERUNG-TEIL1; R187, R189, R190, R192, R196 |
| 7 Kein Geheimnis im Ordner | **nicht erfüllt**: 1 Treffer bei der Suche über 261 Dateien, `zwischenbericht-20260925-163807-r114/ZWISCHENBERICHT.md` Z. 12 (Philipps Telegram-Kennung). Der Abruf ist gesperrt (403). Löschen oder freigeben entscheidet Philipp (P2). Die Gegenprobe hat angeschlagen | R223 |
| 8 `/root/biotop` vorher = nachher | erfüllt: 3.153 = 3.153 Dateien, Unterschied leer, zweimal geprüft | R156, R205, R224 |
| 9 Wortlaut Masterprompt und Verfassungen | erfüllt: v8 mit 94.877 B, SHA-256 gleich. Verfassungen: 13 von 13 Wortlautblöcken gleich; Stichprobe der Fundorte 33 von 33 gleich | MASTERPROMPT-GUELTIG; VERFASSUNGEN-TEIL4 §12; R95, R137, R218 |
| 10 Glossar | erfüllt nach Prüfliste: 71 von 71. Die Prüfliste ist eine Näherung (LU97) | VOLLSTAENDIGKEIT-TEIL1 §3 |
| 11 Bezugsgröße je Zahl, Rohbeleg je „ausgeführt“ | **teilweise**: Seit Auftragsbeginn liefen bis zur Zählung R214 226 von 540 Terminalbefehlen ohne Rohbeleg (LU87). Die Rohbelege der Abschlussschritte ab R227 (Größenvorschau, Bündeln, Veröffentlichen, diese Datei, DATEIEN-TEIL1/2-03, Abrufprobe) entstehen erst nach dem Bündeln und liegen nur auf dem Server. Die Ausgabe der Abrufprobe steht in ABRUFPROBE-03 | VOLLSTAENDIGKEIT-TEIL2 |

## 4. Lesereihenfolge für Chat-Claude

1. Diese Datei.
2. LAGE-TEIL1-01.md: Kurzlage FK01–FK07, Endstand der Runde 6, FK41 dieses Auftrags, FK46–FK49 mit den Fragen P1–P20 und C1–C11. Danach LAGE-TEIL2 bis LAGE-TEIL6.
3. VOLLSTAENDIGKEIT-TEIL1 und VOLLSTAENDIGKEIT-TEIL2.
4. SICHERUNG-TEIL1.
5. CHRONIK, TORE, ENTSCHEIDUNGEN, SOLL-IST, VERFASSUNGEN, AUFBAU, GLOSSAR.
6. INVENTAR, KASSE, LISTEN.
7. VERLAUF, MASTERPROMPT-GUELTIG mit den drei Wortlaut-Teilen, AUFTRAG-V2-WORTLAUT.
8. START-02, Abschnitte A–G.
9. Rohbelege über ROHBELEGE-VERZEICHNIS-03.txt.

## 5. Kosten

- **OpenRouter:** 20,536052277 USD um 14:54 (R5), 21,020250027 USD um 20:28 (R213). Die Differenz von 0,484197750 USD entfällt auf Verdichtungen dieses Auftrags.
- **Biotop-Buchungen:** 0.
- **Soll:** 0,00 €. Ob das Budget auch Verdichtungen umfasst, ist offen (P1).
- Den Stand zum Zeitpunkt von Meldung 2 nennt Meldung 2.

## 6. Dateien des Ordners

- **Einzeln aufgeführt:** jede Datei außer den Rohbelegen ab Stand 02, mit vollständiger Adresse, Bytes und SHA-256 (Liste unten).
- **Rohbelege:** Sie sind zusammengefasst, weil diese Datei mit allen Adressen größer als 40 KB würde. Jede ihrer Adressen steht in DATEIEN-TEIL1-03.txt und DATEIEN-TEIL2-03.txt; welcher Rohbeleg in welcher Datei steht, zeigt ROHBELEGE-VERZEICHNIS-03.txt.
- **Nach dieser Datei entstehen:**
  - DATEIEN-TEIL1-03.txt, DATEIEN-TEIL2-03.txt und PRUEFSUMME-ORDNER-03.txt. Sie enthalten Bytes und SHA-256 jeder Datei, auch dieser. DATEIEN ist geteilt, weil eine Datei rund 43.500 B hätte (Vorschau R227, Grenze 40.000 B). PRUEFSUMME-ORDNER-03 steht im Format von `sha256sum`, mit Namen relativ zum Ordner.
  - Zuletzt ABRUFPROBE-03.txt.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/START-03.md
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/DATEIEN-TEIL1-03.txt
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/DATEIEN-TEIL2-03.txt
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/PRUEFSUMME-ORDNER-03.txt
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ABRUFPROBE-03.txt

- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/AUFBAU-TEIL1-01.md · 30131 B · SHA-256 `6bc02089eb00ec4592b1a9b816f3a7347ceb34dc83d77daecb3dc7268a3a3a25`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/AUFBAU-TEIL2-01.md · 22674 B · SHA-256 `284957d188866666181a00901f9b42d2019c876fd4da841e00a99684c95fe5ce`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/AUFBAU-TEIL3-01.md · 28223 B · SHA-256 `637e663091e5a7ff4cd0aadfe21b19611a5123bae9971466c7e10b70affdb4d6`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/AUFTRAG-V2-WORTLAUT-TEIL1-01.txt · 37946 B · SHA-256 `f98b92fa5264b0bd212c5d0b36abb8cf5c94fb2cc511483826f69677dea1e1eb`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/AUFTRAG-V2-WORTLAUT-TEIL2-01.txt · 3293 B · SHA-256 `3c0eff896969fa86d2794dc3575e08b44dca04ca064f9aa69df95a6f86e68d70`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/CHRONIK-TEIL1-01.md · 29163 B · SHA-256 `6a60a43e2a4cc998ee1933747864ecd88c91def340c8a3356dd71a4da7eb2791`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/CHRONIK-TEIL2-01.md · 26798 B · SHA-256 `90698f5dbfead2978ca1035403ee1afb84b016700c8ab617f2a096979237ba66`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/CHRONIK-TEIL3-01.md · 18463 B · SHA-256 `77d4a79365ad2a40af6d29bc0681114139623427b1c46cf56376b32c0dcbf7e0`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/DATEIEN-02.txt · 22958 B · SHA-256 `7cfe9221a235c978d0bd01c85e7c8bf37e3bb026ca1f7b028ab4a2ad50513e23`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ENTSCHEIDUNGEN-TEIL1-01.md · 29785 B · SHA-256 `198dfc5ac7ddb463305c43d52a5ca8b95ca3510c58d331db9f99f56f0bdaf354`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ENTSCHEIDUNGEN-TEIL2-01.md · 28615 B · SHA-256 `2877b9ce536e8c250645c1562c7fb3297744cffa0a8808e970066adb865360e5`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ENTSCHEIDUNGEN-TEIL3-01.md · 23385 B · SHA-256 `73c74ceb38b0863134cba056fcc119a5837e128fefa634ccba03862d3d557027`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ENTSCHEIDUNGEN-TEIL4-01.md · 21108 B · SHA-256 `6cdb138312dd053db31edf07604dbbb71f5e61d729a98e7b0fd86aea508c5e33`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/GLOSSAR-TEIL1-01.md · 29488 B · SHA-256 `67a733a62c4e0d7dfe5c697cf5b12d6907f71f02c6f201077188e5704714c615`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/GLOSSAR-TEIL2-01.md · 7216 B · SHA-256 `7b37fd06d85d359d19c039ad02f0359b7aed663a542cf19c3313f7257d050a4c`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/INVENTAR-TEIL1-01.md · 28804 B · SHA-256 `baf81caca056b2c7de172aa92d4d51cbce85ab59c38d3e52a26ed36efd2dea32`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/INVENTAR-TEIL2-01.md · 37625 B · SHA-256 `f27f101d023890fc908a23073e3fcfcef2380f2cf10944b79a7f6568de45089b`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/INVENTAR-TEIL3-01.md · 3919 B · SHA-256 `08709dabe56d41749e171437e9b4d91f2044169f28956269796026e700b3dbd3`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL1-01.csv · 6650 B · SHA-256 `eb7b1ff4071eff9ba9f19a62b41a20e4b4e678c3cb6758d0f14218841a161a5c`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL2-01.csv · 37902 B · SHA-256 `1d25fe4b5fb5de6aa0a30cf0ec49775121ec7af471a4596c85fbb123315bd411`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL3-01.csv · 37960 B · SHA-256 `dddd7b248a9ef0c0e0e734b1e1eb68ece9e5ce57ebe4f7ab617dae19592dd3ff`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL4-01.csv · 37862 B · SHA-256 `a3f437725b892843a5c43d268788ac65e96a43c61ca4fb0377746e32f7c2cfcc`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL5-01.csv · 37885 B · SHA-256 `92bf6c66c15b2d345a93952add516080f4fa5f79eaf432a89e1aa54228566248`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL6-01.csv · 37997 B · SHA-256 `d0a98e95d38ac3b7703c33bdf729146bb3072c94244efd95e38c972cb7a61c0e`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL7-01.csv · 37971 B · SHA-256 `41a9a996cb9e01aaf18596c876a8710274f5b5082c2a52b658aaab5f917b9e8e`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL8-01.csv · 37885 B · SHA-256 `2024c1e0d40bc80c5bacd093dc56dd6d4fa8e66d1f4e7536f24c6fc17edb16e7`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL9-01.csv · 37881 B · SHA-256 `285fe035150f607137c162a7121519a4e6e9b89094f0cbc0f285a6c3db7f8643`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL10-01.csv · 37878 B · SHA-256 `e9a248b58cec15cabef88a6e5dcfb749348313e84c09ac75917c0faccf157958`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL11-01.csv · 37849 B · SHA-256 `9fa526375ecaa89bce061e85e4163528ba083266e9ede75088ebe89cb7732cad`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL12-01.csv · 37882 B · SHA-256 `0ed268295ef524e10215f6e8723b604870ba727e7b2ab488521eab52f97f9972`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL13-01.csv · 37936 B · SHA-256 `797967b0d52868e51df2ce882a1c95bb07fe5bd1045780fe1cb45c3e92d2db4e`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL14-01.csv · 37932 B · SHA-256 `e8117b99321939fcd918d9eb20a6e4159316ad6e6411b5650c2c7737982605a9`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL15-01.csv · 37869 B · SHA-256 `bead2e6fa678cd85496ac5acf1364f4c17f377dc06b3b80cb532ea30d5cbff82`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL16-01.csv · 37864 B · SHA-256 `854649fd5433ce523c87a69fb4be8bc9ee3db4d837abc8fc5807a3a8ed238008`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL17-01.csv · 37876 B · SHA-256 `f45fae82749ad90d0be6bffe63d636aba8aec2530f4a9bf9088dbebb53e6aa35`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL18-01.csv · 37923 B · SHA-256 `c4ca4fed7b7f236bd8b5a1d4c8eae02b18cb8d18e736af96f2d9d723d6e70800`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL19-01.csv · 37993 B · SHA-256 `d7a7b53001f87e9704bd33a899f72252d581aa23acd7cbce97625413e658fd73`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL20-01.csv · 37999 B · SHA-256 `752b42a52f1ff55ee184d6397532165bbf5b08f3be8d3f7d93d8c9d5a5bc9967`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL21-01.csv · 37872 B · SHA-256 `331e14012a582e0cff30b692246f43d18ca8b90e2b32a0b48c37d8206f5cc548`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL22-01.csv · 37880 B · SHA-256 `22bdbf69b4b07f365195344ddc841f4f9ad24c13ee786099ba7ae1ca1d900f76`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL23-01.csv · 37999 B · SHA-256 `b51f4b3cd8c4e0e2fbde8edd28a01b2a48d726c83081fa2822a2555a3809f2c6`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL24-01.csv · 37975 B · SHA-256 `d2ee7c12b53b2b538104c5af18c4d897606cf428dbf0902b6f856878a0b7cd8f`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL25-01.csv · 37882 B · SHA-256 `47da48c32bacc437140e0e5d3ee6f46fddf327a3d5c9a959b98e5910f74537c5`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL26-01.csv · 37933 B · SHA-256 `e2ff772034d151b8b7c3320cdb7c444e3402a2017070b1395a4e41c35e44629b`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL27-01.csv · 36373 B · SHA-256 `4b1a653ccb4138e426a9ddc4e6b1f72f484eb983b9a1db0967935c3f6bc88f74`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/KASSE-TEIL28-01.csv · 10514 B · SHA-256 `51b95d28f7b031df948005fb6c98c6dacb2fc73e91558cf74316f69d007fa815`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LAGE-TEIL1-01.md · 24741 B · SHA-256 `dba299785760acb5e1cdfb91e121b2e40f46e41b4b3524f991b57898759f3c7d`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LAGE-TEIL2-01.md · 30675 B · SHA-256 `da9d759bffc2005cbdab40d24abd921d2c53d1d6a5e686a74901e8881bb8e7a8`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LAGE-TEIL3-01.md · 36852 B · SHA-256 `b4c51553b313a23a662b95a252805b163adaa5ec84ebfea4516e1808d0f28247`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LAGE-TEIL4-01.md · 32405 B · SHA-256 `d3970a34e5fc64fee58f5fccb413994e46098c41710ec34e2b67493f5b0cd472`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LAGE-TEIL5-01.md · 17306 B · SHA-256 `67bec1bf1a451861d599d03b62918261729878db42e6001d29d05329ea9fb6dd`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LAGE-TEIL6-01.md · 22233 B · SHA-256 `84a32ee321d8de5c15c5fed5d880c053c4d996cf5eab65fc91824143539800ed`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LISTEN-TEIL1-01.txt · 39520 B · SHA-256 `5e9b4c90e69cefe885217e961db78cf88b1d9e36355c11c10bc92cce6964e0a2`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LISTEN-TEIL2-01.txt · 37896 B · SHA-256 `83bd6c65303a2c16c1131c26e9ead4516999a341020fef267e254ea554fd6f29`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LISTEN-TEIL3-01.txt · 37916 B · SHA-256 `df446cb336a2c69fb717486771d130d6ef93476505532925a178225af945d3b7`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LISTEN-TEIL4-01.txt · 37922 B · SHA-256 `90c0daab4a1fb72afe66d486788103632cfc000b191a6c7deedcace8f22ea80c`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LISTEN-TEIL5-01.txt · 37970 B · SHA-256 `5e6cfffad7a3b8ae3c223a2002504c37a7ad0326bf2116acc132f7288dac0fde`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LISTEN-TEIL6-01.txt · 37824 B · SHA-256 `931c2e820717251558cd9c10e7b5d4c4444c7c76486b4c4523b8e36311f7af06`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LISTEN-TEIL7-01.txt · 5964 B · SHA-256 `ac4507d93bf14f11f70479d7cb71c8bfec7ee9a42d45ddf625c7d00662d95e5d`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/MASTERPROMPT-GUELTIG-TEIL1-01.md · 3819 B · SHA-256 `e1ef1326c0dadb8009c45d8df16449e221a2125f92fdcef93f3e65c44af55b85`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/MASTERPROMPT-V8-WORTLAUT-TEIL1-01.txt · 37726 B · SHA-256 `2aee31d8246d4d0234a5191b6b7dd98e6aacd9603e394234530cfbe295d1a137`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/MASTERPROMPT-V8-WORTLAUT-TEIL2-01.txt · 37981 B · SHA-256 `7d2284a75396620c5f445efefb7407bac9ecbc18bb0e020f197a1134d160f48f`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/MASTERPROMPT-V8-WORTLAUT-TEIL3-01.txt · 19170 B · SHA-256 `3e551cfbbed5e15e4dd8b58b5fd8648f8a93aa194e72bccbfac5a19376700d89`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/PRUEFSUMME-ORDNER-02.txt · 33251 B · SHA-256 `6e7acb737fc5aec13ac4768bce96e2cff951f51dfaf09a0ebc0b4b3d5fe5b774`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ROHBELEGE-TEIL1-01.txt · 25432 B · SHA-256 `5367071fec2fbee84851d5242bc35a3427ec3d032cd20c2de9543be02171687b`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ROHBELEGE-TEIL2-01.txt · 27478 B · SHA-256 `595dc921544719c4edaf9f8ffb3a7dbdea786c14044a22656214dba1d8ddde12`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ROHBELEGE-TEIL3-01.txt · 26515 B · SHA-256 `4de5790a957b4ab39f4dd3dce54044c03ce3733f68e8047db70b3d3126a0160d`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ROHBELEGE-VERZEICHNIS-03.txt · 8665 B · SHA-256 `62990f2734c532f12662a6c9fb133c523e2fe870d6f7c6b54ca68207ddc3a0db`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/SICHERUNG-TEIL1-01.md · 11969 B · SHA-256 `7493abee8aa4eb798b2eb516d88aa38d71a64a077c9479890cff84679ea49391`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/SOLL-IST-TEIL1-01.md · 30644 B · SHA-256 `08b45a92991dae953c8e743526554c298e5d23a680961eff0716c25b2a1625f8`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/SOLL-IST-TEIL2-01.md · 32242 B · SHA-256 `e71a32f8de915ca85fd2ba6d99d2e3d055eceebd4a041b428ab73e67e09e47c4`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/SOLL-IST-TEIL3-01.md · 22261 B · SHA-256 `d1859da18ce6063befb006008cd35cfeb10e83455bb50f09802e57964d0486e0`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/SOLL-IST-TEIL4-01.md · 10843 B · SHA-256 `bffbd205dd4e4e47b3df2e0dceeefc7c0c9ee2a763354200fe89ece8c6f9e6f4`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/START-01.md · 7308 B · SHA-256 `e31c4f5d01f688baba16d4436b738c0223983fcedeeb40a8dda5176326d3158c`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/START-02.md · 25674 B · SHA-256 `9a27f6a1743fff8486839d9426f82be722b4e2d01d2c22168b57f6e020c5a957`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/TORE-TEIL1-01.md · 19692 B · SHA-256 `37af75d4afd47d264ca28e9d54d457dfb1e99c9a6e5012a742ff9091907b737b`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/TORE-TEIL2-01.md · 22564 B · SHA-256 `3a180cb85d6f3b090fb21199f23888ee74bfb55161d2d1c4889c98da50b5bb05`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/TORE-TEIL3-01.md · 24152 B · SHA-256 `9564dafb1fc788d4acb08ae89bd5e99bc435430a4b225a421096663bde80c249`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/TORE-TEIL4-01.md · 19951 B · SHA-256 `ae6f2e11103a09b1421517d3066c8efbade17591981375bb9226516eaaa74214`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERFASSUNGEN-TEIL1-01.md · 30717 B · SHA-256 `d415d5a53eb849d7d9bfdfb8b5a3054d557bbee129f81b9d12650810de3cdfff`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERFASSUNGEN-TEIL2-01.md · 30603 B · SHA-256 `109b852d3f5b986fe79b71e10850bc0420e9e06750e82fc62c5b30d46ea41174`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERFASSUNGEN-TEIL3-01.md · 9704 B · SHA-256 `430d9d8fe5dd72b1c8722009936e77c5960a5a138d59636b1d410a9e85d4af2b`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERFASSUNGEN-TEIL4-01.md · 34325 B · SHA-256 `e0573e05a58408147560efdc1446263b8a991f2306f703dedfde2b435f3ab149`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERLAUF-TEIL1-01.md · 33934 B · SHA-256 `d23aa6638486a9959295ecb563c996e50cb705eb7ce47d59b9bfb6ea8371e2ab`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERLAUF-TEIL2-01.md · 36422 B · SHA-256 `48e0b5efbea0fde9367fcd7080c814e777d18014e42767c7887754c8626d587d`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERLAUF-TEIL3-01.md · 36523 B · SHA-256 `fe78b82b6ffe95828dac00d8afb28e17cb567be2f0246c8338a03593fa11e410`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERLAUF-TEIL4-01.md · 34955 B · SHA-256 `0900302420fd86700e4a2fa814dd19fb015ec97228a67eb516b16a181f165e92`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERLAUF-TEIL5-01.md · 34271 B · SHA-256 `e854819e6c74794434adc5245812682e99811e078688676c05efbd2f2011e9f9`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERLAUF-TEIL6-01.md · 31950 B · SHA-256 `058a44d6b3b081160fcfca366b40d86485427b391eff8d380cd5f3e3ca06fbd0`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERLAUF-TEIL7-01.md · 35542 B · SHA-256 `7f99d236d21763686207adff9822476434809faf3ee1e5bcd7845d6dbdb6c2bf`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERLAUF-TEIL8-01.md · 36508 B · SHA-256 `d3d2c9d8ccbb3ce174436c0ba5fb72becdcb4d814a2946d23b7f05beee83c14d`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERLAUF-TEIL9-01.md · 35522 B · SHA-256 `b0208ac475857a3fa7577990268307cafb04df79452555b74762e7c94d29c253`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERLAUF-TEIL10-01.md · 23212 B · SHA-256 `e61e3434e0552f95a37fdb48432fae1127038ca6ad30f5cef910193e83e82da4`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md · 9284 B · SHA-256 `2304b6edceb268e17d638f722d5b7957df846f74f487f07797a3ff2400ac4bcd`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL2-01.md · 16889 B · SHA-256 `99162ae033c9fa567e0f18f78326ed424509c8c0bfdd8211e45f59a5ea15e302`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/zwischenbericht-20260925-163807-r114/DATEIEN.txt · 543 B · SHA-256 `1f00ee85f4f732a72e3799f2773a770663ecb330bb5b4752f035e68a810fcfac`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/zwischenbericht-20260925-163807-r114/MANIFEST.sha256 · 254 B · SHA-256 `c6ac5b538264405cdd43c10fac7344bdd0d7d7b98c16743fb1cabdd8370641bf`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/zwischenbericht-20260925-163807-r114/PRUEFSUMME-ORDNER.txt · 65 B · SHA-256 `6e126595a0b93f0677cc10a6c1fd47181d3465cfe29e044be4b881565fc9b6ae`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/zwischenbericht-20260925-163807-r114/UEBERGABE-1-UEBERGABE.md · 5754 B · SHA-256 `ce7f985bbe7139bc2a1a52848b1ba81e7adeed61701772c0390d7370f15bbb6e`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/zwischenbericht-20260925-163807-r114/ZWISCHENBERICHT.md · 11021 B · SHA-256 `c96667d256604f8ec0c72a16141f048e66f4b915aa64db49fa7470d015f23df0` · **Abruf gesperrt (HTTP 403), siehe A4**
- Rohbelege Stand 02 und 03: 236 Dateien, `ROHBELEGE-TEIL4-02.txt` bis `ROHBELEGE-TEIL239-03.txt` mit R7–R226; jede mit vollständiger Adresse, Bytes und SHA-256 in DATEIEN-TEIL1-03.txt und DATEIEN-TEIL2-03.txt sowie PRUEFSUMME-ORDNER-03.txt; Rohbeleg → Datei in ROHBELEGE-VERZEICHNIS-03.txt

## 7. Gedächtnis: neueste Dateien in `laeufe/gedaechtnis/`

- **Neu aus diesem Auftrag:** STAND-02 und die Manifeste 02. Diese decken REGELN-01, STAND-01, STAND-02 und UNTERBAU-01 ab.
  https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/STAND-02.md
  https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/DATEIEN-02.txt
  https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/PRUEFSUMME-ORDNER-02.txt
- **Unverändert:**
  https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/REGELN-01.md
  https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/UNTERBAU-01.md
  https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/STAND-01.md
  https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/DATEIEN-01.txt
  https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/PRUEFSUMME-ORDNER-01.txt
