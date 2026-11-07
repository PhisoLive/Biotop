# BIOTOP-LAGE-01 · Fassung 2 · `VOLLSTAENDIGKEIT-TEIL2-01.md` (Abschnitt 7.4, Lückenliste)

- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST. Verfasser: Hermes.
- **Quellen:**
  - die Lücken der Entwürfe: A = ENTSCHEIDUNGEN, B = VERFASSUNGEN, C = TORE, D = AUFBAU, E = SOLL-IST, F = CHRONIK, G = LAGE-TEIL2/3, H = LAGE-TEIL4–6, I = INVENTAR;
  - dazu die Lücken von Hermes.
  - Gleiche Lücken aus mehreren Teilen sind zusammengelegt.
- **Wer schließt:** H = Hermes, P = Philipp, C = Chat-Claude.
- **Spalten:** Lücke · warum · was sie schließt · wer schließt. Nummern mit „–“ in der letzten Spalte sind nicht schließbar oder schon geschlossen; der Grund steht in derselben Zeile.
- **Nicht vergeben:** LU17, LU51, LU67, LU68, LU76, LU78, LU81 und LU100. Diese Lücken sind in eine andere Nummer eingegangen oder geschlossen; der Verweis steht unten.
- **Zählung (R220):** 92 vergebene Nummern.
  - 86 haben eine Zuständigkeit (je Zeile die erstgenannte Stelle): Hermes 44, Philipp 21, Chat-Claude 21.
  - 6 haben keine („–“), der Grund steht je Zeile:
    - nicht mehr schließbar: LU18, LU27, LU70, LU95;
    - mittelbar geprüft bzw. Zahlen liegen vor: LU19, LU88.

| LU | Lücke | warum | schließt | wer |
|---|---|---|---|---|
| LU01 | Plattenkopien v1–v5 außerhalb des Prüfkanals nicht gesucht (A L-2) | nicht gesucht | Suche über `/root` und `/tmp` | H |
| LU02 | REGELN-02 fehlt, obwohl V19 eine neue REGELN-Datei je Fassung verlangt (A L-3) | nicht geschrieben | REGELN-02 zu v7, v8 und der Arbeitsregel vom 23.09. | H |
| LU03 | STAND im Gedächtnis seit 20.09. nicht fortgeschrieben (A L-4, G) | nicht geschrieben | teilweise geschlossen durch `gedaechtnis/STAND-02.md` dieses Auftrags; REGELN siehe LU02 | H |
| LU04 | 9 von 24 Punkten der Sammlung für Fassung 7 stehen nirgends als Regel (A L-5) | nicht übernommen | Aufnahme in Fassung 9 | C |
| LU05 | Keine Bestätigung Philipps für das Maß der Läufe 2, 4 und 5 und für VB1 Lauf 26; 7 Freigaben vor der Vollmacht (A L-6, E L-E10) | nie eingeholt | Bestätigung oder Entscheidung (P12) | P |
| LU06 | T3 lief ohne Mentor und ohne Richtungswahl, 0 `mentor.gewaehlt` (A L-7, E L-E13) | nicht verlangt oder nicht gebaut | Entscheidung, ob v8 Z. 167/281 für Testwerke gilt (P9) | P |
| LU07 | Die Delegation der Verfassung für Übungswerke ist nur in den Fassungen belegt, keine Nachricht Philipps (A L-8, B L1) | nicht gefunden | Nachricht nennen (P14) | P |
| LU08 | Philipps Richtungsentscheidung vom 21.09. ist nur als Wiedergabe Chat-Claudes belegt (A L-9) | nur Wiedergabe | Bestätigung | P |
| LU09 | Das Register der Entscheidungen Hermes ist ein Auszug; es fehlen Phase 3, der Nachlauf und T3 abschluss-01/-02 (A L-10) | Zeit | Auswertung der übrigen 38 Dateien (R61) | H |
| LU10 | Die Nachricht „Vollmacht deckt die Richtungswahl“ (19.09.) ist nicht gesucht (A L-11, P-2) | nicht gesucht | Suche in `arbeit/verlauf/v3/wortlaut.jsonl` | H |
| LU11 | Ob V-2 (OpenRouter-Katalog prüfen) umgesetzt ist (A L-12) | nicht geprüft | Code und Berichte lesen | H |
| LU12 | Nachgänge außerhalb von VB1 nicht nach Regeln durchsucht (A L-13) | nicht gesucht | Suche | H |
| LU13 | Bestätigung der Vertragstests aus Phase 2 nicht gefunden (A L-14) | nicht gefunden | gezielte Suche; sonst Philipp | H |
| LU14 | Quelle des Satzes „Philipp hat am 21.09. entschieden: Chat-Claude bestätigt die Verfassung …“ (B L2) | 0 Treffer | Suche in der Sitzungsdatenbank; sonst Philipp (P15) | H |
| LU15 | Die Regeldateien von lagerhaus, logmuehle und T3 haben keine eigene Bestätigung und enthalten Werte, die im Text fehlen (B L3) | nie verlangt | Entscheidung (C3) | C |
| LU16 | Die T3-Regeldatei liegt nicht im Siegelordner `verfassung-02`, sie ist nach der Versiegelung geändert (B L4) | Ablauf | Entscheidung | C |
| LU18 | Frühere Einlegungen der Verfassungen sind nicht byteweise belegt, weil `INSERT OR REPLACE` überschreibt (B L6) | Bauart der Kasse | nicht mehr schließbar | – |
| LU19 | `b7_vorlagen_pflegen.py` (Teil B) lief ohne Rohbeleg (B) | eigener Ablauf des Subagenten | mittelbar geprüft durch R136/R137; gezählt in LU87 | – |
| LU20 | Nachmessung von VB1 Lauf 26 nach T3-Methode fehlt; davon hängt die Abnahme von Tor 2 Zeile 8 ab (C L1) | nicht beauftragt oder nicht gefunden | Messung ohne Modellaufruf oder Entscheidung (C11) | C |
| LU21 | Die Messgrenze „ungemessen unter 20 Tests“ steht nicht in v7/v8 (C L2) | nicht übernommen | Fassung 9 (C11) | C |
| LU22 | T3: Aufnahmezeile, Lauf 38 „Kein Rückschritt“ und Endgrund von Lauf 38 nicht belegt (C L3) | nicht gelesen | `biotop-t3-typescript/lauf38*` und abschluss-02 lesen | H |
| LU23 | 5 Messgerätfehler der v8-Liste ohne Einzelstand (Referenzlast, Aufwärmung, Median aus drei, Ausfall-Blockade, Budgetgrenze) (C L4) | nicht gelesen | `uebernahme-01/ZWISCHENBERICHT.md` und Laufberichte 27–36 lesen | H |
| LU24 | Einzelstand der Befundgruppen A01–A33, B-01–B-24, C01, C02 und von R5-1 … R5-14 (C L5) | nicht erhoben | Abschlussordner Reparatur 01/02 und Tafel der Runde 5 | H |
| LU25 | Mehrfach vergebene Kennungen: Lauf 26 (drei Zweige), Werk-id 23 (VB1 und T3), Kandidat 2680 (C L6, G) | Zweige zählen je für sich | Die Tafel in INVENTAR Abgleich 8 deckt nur Lauf 26 ab; Werk-id 23 und Kandidat 2680 ergänzen | H |
| LU26 | Eigener Auftrag zur Ansageabweichung 9 von 11 nicht gefunden (C L7, G) | nicht erteilt oder nicht gefunden | Entscheidung | P |
| LU27 | Erfundene Mentor-Verweise werden nicht gespeichert (C L8) | Bauart | nur durch Codeänderung; nicht Gegenstand | – |
| LU28 | Die 11. Zeile von Tor 2 und Tor 3 steht nicht im Tor-Block von v8 (C L9) | nicht übernommen | Fassung 9 | C |
| LU29 | Runde 6 ohne Commit, volle Regression mit Kammer, Review und Bericht; Befund G offen (C L10, F) | S1c endete an der Grenze; Runde 6 ruht seit dem Stich | Weiterlauf nach Entscheidung (P3) | P |
| LU30 | Versionen in den Kammer-Abbildern: Python 3.12.14 (R194); Node/TypeScript in `biotop-kammer:ts1` nicht belegt (D L-D2) | Befehl im Container nicht erlaubt | `package-lock.json` der Kammer auswerten (im Archiv) | H |
| LU31 | Umfang des nicht eingecheckten Stands in Zeilen nicht gezählt; 25 Einträge sind gelistet (D L-D3) | nicht gezählt | Zählung an der Liste `tmp/git-status-stich.txt` | H |
| LU32 | Kein Lauf aller Tests am Commit; die Regression wählte 93 Integrationsfälle ab (D L-D4) | Laufzeit, Kammer | volle Regression nach Runde 6 | H |
| LU33 | Welchen Wert `von` die Freigabe über den Dienst bekommt (D L-D5) | nicht gelesen | `dienst.py` lesen | H |
| LU34 | T3-Läufe 26–30 und 33–35 ohne Lazarus-Archiv und ohne Tabellenzeile (D L-D6) | nicht geprüft | Laufenden je Lauf prüfen | H |
| LU35 | Ob die 115 Buchungen ohne `kontingent` dieselben sind wie die 115 mit `ausfall.hoechstfall` (D L-D7) | nicht geprüft | Abfrage an einer Kopie von `t3.db` | H |
| LU36 | 11 von 44 Modulen ohne direkte Testdatei; keine Messung der Testabdeckung (D L-D8) | nicht gemessen | Abdeckungslauf | H |
| LU37 | Die Zwischenbericht-Pflicht steht nur im Änderungsverzeichnis, nicht in Abschnitt 9 (E L-E1) | Aufbau von v8 | Fassung 9 | C |
| LU38 | Für T3 ist keine Verlaufskurve auffindbar (E L-E2) | nicht erzeugt oder nicht abgelegt | `kurve` an einer Kopie von `t3.db`, ohne Modellaufruf | H |
| LU39 | Die technische Trennung des Kerns (v8 Z. 303) steht seit Phase 1 auf der Liste (E L-E3) | keiner Phase zugeordnet | Entscheidung | P |
| LU40 | Keine Kontingentgrenze und kein Adapter für die schweren Team-Modelle (E L-E4) | Aufrufe über OpenRouter | Entscheidung (P10) | P |
| LU41 | Die Landkarte hat keinen Aktenschrank (Stichwort- und Bedeutungssuche) (E L-E5) | nicht gebaut | Entscheidung (C8) | C |
| LU42 | Kein CI, kein gitleaks, keine Abhängigkeitsprüfung (E L-E6) | nicht gebaut | Entscheidung (C8) | C |
| LU43 | Die Organe sind nicht gegen die Grundsätze 7–14 geprüft (E L-E7) | nur 1–6 geprüft | Prüfung | H |
| LU44 | Keine Verteilung des Typsiebs, wenn der Kern Mutanten erzeugt; Tor-4-Zeile 3 hängt davon ab (E L-E8, C) | nicht gebaut | Bau vor T4 | H |
| LU45 | Für „Grenzanzeige ohne irreführende Rundung“ (v8 Z. 464) gibt es keinen Beleg (E L-E9) | nicht belegt | Probe | H |
| LU46 | Der Ablehnungsweg der Freigabe lief nie; die Übergabe an die Immunisierung ist nicht gefunden (E L-E11) | kein Anlass | Probe | H |
| LU47 | Bei der Rückkehr stellt Lazarus die Landkarte nicht zurück (E L-E12) | Bauart | Entscheidung | C |
| LU48 | `/root/biotop-vor-t4-06/UEBERGABE.md` liegt nicht im Prüfkanal (E L-E14) | Runde 6 nicht abgeschlossen | Veröffentlichung mit Runde 6; die Datei ist im Archiv gesichert | H |
| LU49 | Die Kasse führt den Laufstatus nicht nach: T3/31, /32, /36 „laeuft“, T3/38, STAMM 24 und 25 „bereit“, jeweils ohne Ende (F, H, I) | Status wird bei Abbruch nicht geschrieben | Datenpflege, braucht einen Auftrag (ändert das Biotop) | P |
| LU50 | 29 späte Buchungen (0,016949 €) auf alten Lauf-ids nach deren Endmeldungen (F) | Ursache nicht untersucht | Buchungen gegen das Protokoll legen | H |
| LU52 | Welche Review-Fassung der Runde 4 gilt: `REVIEW.md` oder `/tmp/review-vor-t4-04/REVIEW-B.md` (F, H) | nicht entschieden | Entscheidung (C1); beide sind im Archiv gesichert | C |
| LU53 | Wer schrieb den Auftragstext in id 1959 (19.09. 16:39) (F) | Quelle trennt die Teile nicht | Gateway-Protokoll dieser Minute; sonst P18 | H |
| LU54 | „Prüfung 5 vom 20.09.“ nicht gefunden. `GEDAECHTNIS_Hermes_2026-09-20.md` ist gefunden (VOLLSTAENDIGKEIT-TEIL1 §4) (F) | nicht gefunden | Philipp (P16) | P |
| LU55 | Kosten des Trägernachweises W4 (20.09.) unbekannt (F) | nicht gebucht | Anbieterabrechnung | P |
| LU56 | W6 vom 20.09.: 35 gegen 40 Dateien (F) | keine Antwort gefunden | Chat-Claude (C9) | C |
| LU57 | Die Startregel für T4 (id 16901) steht nur in einer Nachricht, nicht im Masterprompt (G) | nach v8 gesetzt | Fassung 9 (C10) | C |
| LU58 | v8 sieht eine Behebungsrunde vor T4 vor; es sind sechs, keine abgenommen (G) | Befunde je Runde | Fassung 9 oder Entscheidung (C10) | C |
| LU59 | Die Werkzeile von `versandwerk-t3-02` trägt `aufgenommen_am` 22.09. 15:43, nach dem Beginn der Läufe (G) | nicht geklärt | Protokoll lesen | H |
| LU60 | Phase 2 und Phase 3 haben kein Abnahmewort, nur „abgeschlossen und gewertet“ (G) | nie ausgesprochen | Wertung | C |
| LU61 | Die Rolle von `/root/versandwerk-t3` neben `versandwerk-t3-02`; kein Kasseneintrag (G, I LV-I-02) | nicht gelesen | T3-Berichte und uebernahme-01 lesen | H |
| LU62 | Wie geht es nach Phase 5 weiter? Wer setzt Tor 5, wer erklärt den Breitentest für abgeschlossen, wer wählt das Modell für T4? (G) | v8 schweigt | Entscheidung (P13) | P |
| LU63 | Zählen die Funde der Behebungsrunden zur Sättigungszählung von T3? (G) | keine Quelle | Entscheidung | C |
| LU64 | Umfang der erzeugten Prüfwerke nicht gezählt (G) | nur durch Ausführen von Biotop-Code | Zählung im abgeschotteten Stand | H |
| LU65 | Welchen Läufen die 18 T3-Freigaben unter Vollmacht je gehören (G) | nicht erhoben | Abfrage je `lauf_id` an einer Kopie | H |
| LU66 | Vier Phase-4-Lücken, 19 Außenorte und 9 von 11 Ansageabweichungen ohne neue Entscheidung, nachdem ihr Anlass entfallen ist (H) | Handelssystem gestrichen | Entscheidung | P |
| LU69 | Den Wortlaut „blockiert nicht“ gibt es in den Biotop-Quellen nur einmal; die Zählung in FK39 beruht auf gleichwertigen Vermerken (H) | Wortwahl der Berichte | ausgelegt (LAGE-TEIL5); Prüfung | C |
| LU70 | `hermes-an-philipp.md` enthält Wiederholungen und eine Verdichtung; „216 Meldungen“ ist unsicher (H) | Quelle | ersetzt durch die Zählung in VERLAUF (Hermes 119, Zwischentexte 263 ab 21.09.); die Zahl 216 selbst bleibt unbelegt | – |
| LU71 | Masterprompt v8 nicht nachgeführt: Lauf 38 „4 von 5“, Tor 2 Zeile 8 ohne „enger Nachtrag“, zwei Gründe für die Abbruchregel (H) | keine Fassung 9 | Fassung 9 (C10) | C |
| LU72 | Was der Reset am 19.09. um 15:10:15 (`67457ac`) verworfen hat (H) | das Reflog zeigt keinen Inhalt | `wortlaut.jsonl` 15:00–15:15 lesen | H |
| LU73 | Sind die Probeneinträge (`e77cead`) gelöscht oder gesperrt, und lassen sie sich wiederherstellen? (H) | nicht geprüft | `git show e77cead` und eine Abfrage an einer Kopie | H |
| LU74 | Wer hat den Beleg zu `_Konto.buchen` am 25.09. um 07:42 überschrieben? (H) | nicht geklärt | `bau/S1-PLAN.md` und den Verlauf von S1 lesen | H |
| LU75 | Wer hat sich am 18.09. achtmal als root am Terminal angemeldet? (H) | außerhalb von Hermes | Philipp (P17) | P |
| LU77 | Keine Entscheidung gefunden zu R5-14, R4-19, K2868 „007“, Gateway-Dump und „Bauzeit gepaart“ (H) | nicht entschieden | Entscheidung | C |
| LU79 | Ist die Arbeit außerhalb dieses Servers gesichert? (H) | Ablage 2 fehlt, siehe LU90 | Philipp (P4) | P |
| LU80 | Die Datei aus A4 mit Philipps Telegram-Kennung liegt im Ordner. Punkt 7 von Abschnitt 10 ist damit nicht erfüllt | Löschen ist nach Regel 2.2 nicht erlaubt | Löschen oder Freigeben (P2) | P |
| LU82 | 11 Laufnummern in Ordnertexten ohne Lauf: 0, 52, 53, 59, 60, 62, 66, 84, 128, 848, 991 (I LV-I-04) | Das Suchmuster trifft wohl auch Zahlen anderer Bedeutung | Fundstellen lesen | H |
| LU83 | 54 von 114 Aufträgen und Anweisungen Philipps ohne Status in der Zuordnung (I, Abgleich 4) | Die Zuordnung geht nur über id oder ±10 min | Status aus CHRONIK je Nachricht übertragen | H |
| LU84 | 7 Aufträge Hermes → Subagent ohne Schlussbericht in ihrer Sitzung, 5 davon vor diesem Auftrag (ids 16285, 16712, 17153, 17290, 17293) (I LV-I-06) | abgebrochen oder anders geliefert | Sitzungen lesen | H |
| LU85 | Die Differenz OpenRouter − Kasse (+0,2161 USD bis 14:54) ist nicht einzeln erklärt (I LV-I-07) | Die Anzeige hat keine Einzelposten | Aktivitätsexport von OpenRouter | P |
| LU86 | Tagesbilanz: Spalte OpenRouter für 18.–24.09. NICHT ABGEDECKT (I) | nur eine Abfrage vom 25.09. | Aktivitätsexport von OpenRouter | P |
| LU87 | Befehle ohne Rohbeleg: seit 14:44:20 liefen 226 von 540 Terminalbefehlen ohne `rb.py` (Hauptsitzung 100, Subagenten 126). Lese-, Such- und Schreibwerkzeuge haben keinen Rohbeleg (R214) | Abkürzungen | nicht nachholbar; der Wortlaut steht in der Sitzungsdatenbank, die gesichert ist | H |
| LU88 | SPERRE-01 (16:27): eine lesende Zählung gesperrt, nicht nachgeholt | harte Linie | Die Zahlen liegen in R19, R22 und R23 vor | – |
| LU89 | Tests im gesicherten Stand nur ohne Kammer: 203 von 953 nicht bestanden; bei 83 ist die Ursache nicht belegt (R203, R204) | Ein Kammerlauf legt Container an, also Änderungen außerhalb der erlaubten Ablagen | Lauf mit Kammer nach Entscheidung | P |
| LU90 | Ablage 2 fehlt; die Sicherung liegt nur auf diesem Server | Es ist keine Ablage eingerichtet (R36) | Philipp (P4) | P |
| LU91 | 2 `VorspannFehler` „Kernstand seit der Eichphase der Stufe 2 verändert“ in `tests/test_t3_bindung.py` (R203) | nicht untersucht | Test im Stand mit Kammer lesen und ausführen | H |
| LU92 | Eine Datei Unterschied: Umfang 79.597 (R177) gegen 75.214 + 4.382 = 79.596 (R181–R186) | nicht aufgeklärt | Listen von R177 und Manifest vergleichen | H |
| LU93 | `/usr/local/lib/hermes-agent` und die Serverkonfiguration (`/etc/pruefkanal`, Caddy) sind nicht gesichert | nicht im Umfang von Abschnitt 4 | Umfang erweitern | P |
| LU94 | Ob die Zwischentexte bei Philipp ankamen, ist nicht belegt (R188) | Das Gateway-Protokoll hat dazu keine Zeile | Zustellbuch prüfen | H |
| LU95 | OpenRouter +0,090302250 USD zwischen 18:04 und 20:28 nicht einzeln zugeordnet (R152, R213) | Verdichtungen nicht einzeln gezählt | Verdichtungszeilen in `agent.log` zählen; Einzelposten nicht abrufbar | – |
| LU96 | A7: Änderung von 4 Skills um 17:01, Ursache UNBEKANNT | nicht geklärt | Protokolle der Skillpflege lesen | H |
| LU97 | Die Glossarprüfung ist eine Näherung: Prüfliste 71 von 71 (R216) | Auswahl Hermes | Prüfung beim Lesen | C |
| LU98 | Die Entwürfe A–I sind nur mechanisch und in Stichproben geprüft (VOLLSTAENDIGKEIT-TEIL1 §4) | Umfang | Prüfung beim Lesen | C |
| LU99 | Zeitgeber und Prozesse nur zu Beginn erhoben (R2), nicht zum Stich | Ablauf | Die Übergabe S1c und R175 zeigen keine Hintergrundprozesse | H |

**Geschlossen oder zusammengelegt:**
- LU17: drahtwerk-Varianten und weitere Belege liegen nur in `/tmp`. Geschlossen, weil `/tmp` als Teil 2b gesichert ist (R183).
- LU51 ist in LU29 eingegangen, LU67 in LU49, LU81 in LU61.
- LU68: Belege nur in `/tmp`. Wie LU17 geschlossen; das Risiko steht in FK43.
- LU76: Wer hat `biotop.db-shm` um 15:55 geändert? Geschlossen: Hermes, A6, R31 (START-02 D).
- LU78: Vorschlag einer dauerhaften Freigabe. Steht als P20 in LAGE-TEIL1.
- LU100: Weicht der Arbeitsbaum von `0c2f058` ab? Geschlossen: 25 Einträge, R156 und R191.
