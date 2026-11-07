# Status der Läufe 24/25 und Bauteile A/B/C

**Historische, ausschließlich lesende Prüfung für Reparaturauftrag 01, Teilauftrag 6.** Maßgeblich sind die eingefrorene SQLite `/root/reparatur-01/ausgang.db` und der Quellstand `b42dc941e7fcb66632ba6a0e13b8df106a270a31`, nicht zwischenzeitliche Reparaturen im Arbeitsbaum.[21][34]
Alle Ereigniszeiten unten sind **UTC**.[21][34]
Datensatzstatus, fachliche Gültigkeit, frühere Abnahme und heutige Reparaturfreigabe werden getrennt.[21][34]

## 1. Entscheidung in Kürze

- **Lauf 24 und Lauf 25 sind im Snapshot beide `bereit`, nicht `verworfen`, nicht beendet.** Jeweils Generation 0 und vier evolutionäre Generationen sind belegt.[2][3]
  Das ist weder eine Aussage über einen laufenden Prozess noch eine Freigabe zur Fortsetzung.[2][3]
- **Nicht pauschal verwerfen:** Laufhistorie, gebuchte Kosten, gespeicherte Annahmen, Werkstände, A-Entscheidungen und gestellte C-Pfade bleiben als genau abgegrenzte Beobachtungen gültig.[14][15][34]
  Die Fehler im Vorspann und in A/C begründen dagegen **keine Gesamt-/Vergleichsfreigabe** dieser Läufe als sauber geeichte Wirksamkeitskampagne.[14][15][34]
- **A:** Ansagesperre tatsächlich benutzt; Sparmechanik gegenüber dem angekündigten Angriff belegt, aber keine allgemeine Doppelungsverhinderung und keine nachgewiesene Netto-Geldersparnis.[29][30][31]
  **B:** Vorlagenmechanik vorhanden, keine stabile Mentorwirkung und keine allgemeingültige Halbanteilsgarantie.[29][30][31]
  **C:** zwei Aufnahmestellen mit gestellten Gegenständen erreicht; natürliche Doppelungsabwehr und A→C-Integration nicht nachgewiesen.[29][30][31]
- **Verbindliche Nutzerentscheidung:** Die Normzeile und „4 von 4 bestanden“ sind zurückgenommen.[1]
  Die Zahlen der Läufe 22/23, **ausdrücklich einschließlich 54,5 %**, stehen wegen Satz 2 unter Vorbehalt.[1]
  Diese Entscheidung wird weder durch spätere Kostenabgleiche noch durch neue Nenner oder die frühere enge Mechanikabnahme aufgehoben.[1]
- **Empfehlung, keine Datenänderung:** 24/25 als historische Belege aufbewahren, nicht als neue Vergleichsbasis freigeben; nach einer Messgerätänderung neue Lauf-IDs und einen nachgewiesenen Vorspann verwenden. Dieser Bericht setzt keinen DB-Status um und löscht keine Zeile.

## 2. Verbindliche Entscheidungen und Rücknahmen

Die jüngste maßgebliche Nachricht ist **Nutzernachricht 4317**, Session `20260920_063003_896e94ff`, **2026-09-20T13:28:25Z**: „Wertungen, die ich zurücknehme: die Norm-Zeile aus Tor 2 und ‚4 von 4 bestanden‘ aus dem Nachlauf waren ein leerer Durchlauf (masse statt mass, norm=[]); die Zahlen aus den Läufen 22 und 23 stehen wegen des Satz-2-Verstoßes unter Vorbehalt, darunter die 54,5 %.“ Danach folgt ausdrücklich der Reparaturauftrag vor jeder weiteren Messung.[1]

Die frühere übermittelte enge Abnahme, Nutzernachricht **3102 vom 2026-09-20T02:50:16Z** mit Abnahmedokument, bezog sich auf **gebaut und im Kernpfad gezeigt**.[1][10]
Sie ließ C im natürlichen Betrieb, Zeile 8 und die natürliche Abweichungsquote ausdrücklich offen.[1][10]
Sie bleibt ein historischer Entscheid, ist aber kein Beleg für die später gefundenen Integrations- und Eichfehler.[1][10]
Insbesondere wird „Norm-Stelle von C erreicht“ nicht in „Norm-Eichprobe bestanden“ umgedeutet.[1][10]

### Norm: Rücknahme ist sachlich belegt, nicht nur redaktionell

| Ereignis | Zeit UTC | Kandidat / Lauf | Tatsächlicher Befund hinter dem grünen Prüfstatus |
|---|---|---|---|
| #12418 | 2026-09-19T20:09:59.169Z | K2071 / 20 | `norm=[]`, `zuwachs=None`; Ablehnung wegen Änderung einer vorhandenen Testdatei |
| #12440 | 2026-09-19T20:11:53.152Z | K2075 / 20 | `norm=[]`, `zuwachs=None`; Pareto-Verletzung durch zusätzliche tote Funktion |
| #12465 | 2026-09-19T20:13:10.918Z | K2079 / 20 | dieselbe leere Normprüfung / Pareto-Grund |
| #12538 | 2026-09-19T20:59:09.321Z | K2083 / 22 | dieselbe leere Normprüfung / Pareto-Grund |

Das sind vier **historisch grün protokollierte** Normprüfungen, nicht vier gültige Normnachweise.[32][34][35]
Der Abschluss #12544 vom **2026-09-19T20:59:15.462Z** meldete dennoch alle vier Prüfarten bestanden.[32][34][35]
Die falsche Rückgabeschlüssel-Auswertung (`masse` statt `mass`) und der leere Normgegenstand tragen die Rücknahme; andere einzelne Prüfarten werden dadurch nicht ohne eigenen Gegenbefund pauschal gelöscht oder umgewertet.[32][34][35]

### 22/23: Vorbehalt nicht nachträglich verkleinern

| Lauf | Frühere reale Ereignisse | Spätere reale Ereignisse unter derselben Lauf-ID | Folge |
|---|---|---|---|
| 22 | Freeze #12517, 2026-09-19T20:58:03.553Z; Gen-4-Ergebnis #13232, 21:22:12.328Z; bis dahin keine Ansagephase | Gen 5 #14248, 22:46:02.011Z; Ansage #14305, 22:46:45.372Z, ausgeführt | geänderter Anklägerablauf ohne neuen Lauf-/Maß-Freeze |
| 23 | #13398, 2026-09-19T22:22:14.925Z und #13442, 22:23:21.047Z: `extern_filtern\|raises:ValueError` jeweils ausgeführt, Vorrat 0 | Gen 5 #14066, 22:37:19.798Z; #14086, 22:37:40.225Z mit Vorrat 3; #14160, 22:39:02.179Z sperrt `nach_zeit\|raises:FilterFehler`, Vorrat 8 | geänderte Ansagehistorie/Sperrwirkung zwischen Generationen |

Diese Übergänge sind der Satz-2-Beleg; Commitzeiten allein wären es nicht.[12][15][35]
Die historische Ausgabe `03-vorbedingung1-messung.txt`, Zeile 18, nennt **6 Doppelungen aus 11 Tests = 54,5 %** für Lauf 22.[12][15][35]
Hier wird diese Aussage **als historische, nun unter Vorbehalt stehende Zahl erhalten**, nicht durch spätere Varianten ersetzt oder als neue valide Messung ausgegeben.[12][15][35]

Der Snapshot führt 22/23 jeweils als `gesaettigt`.[2][5][22]
Das frühere Ereignis **#12474 (2026-09-19T20:34:33.836Z)** mit `lauf_id=22`, `status=verworfen` liegt **vor** der Anlage der heute gespeicherten Laufzeile 22 um **20:57:41.378Z**.[2][5][22]
Es darf nicht als Abbruch dieses späteren Laufs ausgegeben werden: hier wurden IDs wiederverwendet.[2][5][22]
Die beigelegten Lebenszeitabfragen schneiden deshalb bei `laeufe.begonnen_am`.[2][5][22]

## 3. Tatsächliche Lauf- und Werkstände

| Merkmal | Lauf 24 | Lauf 25 |
|---|---|---|
| Werk | ID 21, `lagerhaus-zeile8-24` | ID 22, `lagerhaus-c-25` |
| Anlage laut DB | 2026-09-19T22:57:49.320Z | 2026-09-20T01:13:30.138Z |
| Anlageereignis | #14435, 22:57:49.321Z | #15231, 01:13:30.140Z |
| Maß-Freeze-Ereignis | #14475, 2026-09-19T22:59:05.087Z | #15271, 2026-09-20T01:13:51.986Z |
| DB-Status / Ende | `bereit` / NULL | `bereit` / NULL |
| Generation 0 | ID 136, angenommen | ID 141, angenommen |
| Reguläre Generationsteilnehmer | 128, je 32 in Gen 1–4 | 128, je 32 in Gen 1–4 |
| Kandidatentabelle insgesamt | 136: zusätzlich 8 außerhalb der regulären Generationslisten | 138: zusätzlich 10 außerhalb der regulären Generationslisten |
| Im Snapshot als Probe markierte Kandidaten | 0 | 0 — **kein Beleg, dass nie Proben liefen** |
| Letztes reguläres Generationsergebnis | #15225, 2026-09-19T23:25:25.570Z | #16008, 2026-09-20T01:43:39.269Z |
| Letzter angenommener Werkstand | Gen 1, K2419 | Gen 2, K2590 |

Die Zusatzkandidaten werden einzeln in `STATUS-24-25.json` geführt; sie sind nicht als `ist_probe` markiert und werden nicht mit den später gelöschten C-Pfadge­genständen verwechselt.[34][35]
Die echten Kandidaten-, Generations- und Probenmengen sind unterschiedliche Populationen.[34][35]

### Jede tatsächlich vorhandene Generation

| Lauf / Gen / DB-ID | Start-Ereignis, Zeit UTC | Abschluss-Ereignis, Zeit UTC | Gespeicherter Stand |
|---|---|---|---|
| 24 / 1 / 137 | #14482, 2026-09-19T23:01:00.435Z | #14677, 23:06:06.871Z; Freigabe #14678, 23:06:07.222Z | angenommen, Auswahl K2419 (`formeln`) |
| 24 / 2 / 138 | #14680, 23:06:07.382Z | #14853, 23:12:03.458Z | abgelehnt |
| 24 / 3 / 139 | #14855, 23:12:03.782Z | #15040, 23:16:49.115Z | abgelehnt |
| 24 / 4 / 140 | #15042, 23:16:49.427Z | #15225, 23:25:25.570Z | abgelehnt |
| 25 / 1 / 142 | #15278, 2026-09-20T01:15:15.888Z | #15450, 01:24:40.042Z | abgelehnt |
| 25 / 2 / 143 | #15452, 01:24:40.372Z | #15661, 01:35:49.757Z; Freigabe #15662, 01:35:50.117Z | angenommen, Auswahl K2590 (`formeln`) |
| 25 / 3 / 144 | #15664, 01:35:50.275Z | #15829, 01:38:59.987Z | abgelehnt |
| 25 / 4 / 145 | #15831, 01:39:00.352Z | #16008, 01:43:39.269Z | Generalprobe am Laufzeit-Grenzmaß abgelehnt |

Die Annahmen sind **historisch gespeicherte Hermes-Freigaben unter Übungswerk-Vollmacht**, keine neue fachliche Bestätigung dieses Teilauftrags.[3][35]
Lauf 24 Gen 1 begründete die Annahme mit Laufzeitgewinn bei unverändertem Kernmaß; Lauf 25 Gen 2 mit `formeln.tests_fehlgeschlagen: 1 → 0`.[3][35]
Gerade Lauf 25 Gen 4 nennt ausdrücklich den Rückfallfaktor **1,15 ohne Rauschmessung**.[3][35]
Eine neue geeichte Geschwindigkeits-/Qualitätsbehauptung wird daraus nicht abgeleitet.[3][35]

### Werkidentität und Messgerätidentität sind nicht dasselbe

Beide Generation-0-Werke tragen denselben Lazarus-Werkhash:

`0992e6981d4eec322297ea68a01876fcf4a6876172e19f96b2d3d6692dd6f22f`.[3]

Der aktuelle Inhalt der beiden abgefragten Werkverzeichnisse wurde mit der **unveränderten Originalfunktion `lazarus.pruefsumme_werk`**, ohne Snapshot-/Rückkehrfunktion, nachgerechnet.[6][28]
Werk 21 entspricht `lauf24-gen1`, Werk 22 `lauf25-gen2`; beide eigenen Werk-Gits waren bei dieser Lesung sauber.[6][28]

| Werk | Werkhash der Originalableitung | Werk-Git-HEAD |
|---|---|---|
| 21 | `03245fbcda1c4af5dbb5ac307ef515e62e9e182461c2f39ea75fdbe436a096f1` | `3052db093ef1099a0ff8def1c3625f5d358d7aea` |
| 22 | `c132565933dca99d07bbc417eae93755674a51a9514ad9899bf9128df1d9b630` | `fb07f3636df38f25e5cec4cbda9d100b24e26283` |

Der technische Maßdatensatz heißt bei beiden **Fassung 2**, mit Fachverweisen F3/F4 und einer Bestätigungsprosa zu v6 bzw.[2][7][34]
Lauf 25.
Das ist **keine gespeicherte Messgeräte-Commit-ID**.[2][7][34]
Eine Quellversiegelung des tatsächlich ausgeführten Messgeräts fehlt; die Versionszuordnung wird deshalb nicht als stärkerer Lauf-Freeze ausgegeben.[2][7][34]

| Quellstand / Geltungsgrenze | A | B | C |
|---|---|---|---|
| Historischer v6-Ausgang `7c73d403c18755dda26655c78ac7290c446d9f45` | nicht vorhanden | `fremd_min` nicht vorhanden | nicht vorhanden |
| Lauf-24-Vorbereitungsstand `293b1c16c53ca76fb737587b1c09b04bd21fcdba` | vorhanden | vorhanden | nicht vorhanden |
| Lauf-25-Vorbereitung `71fb51cce7666eb74591ec3e64f69e5bd8ba54ce` | vorhanden | vorhanden | vorhanden, einschließlich Aufrufzähler |
| untersuchter HEAD `b42dc941e7fcb66632ba6a0e13b8df106a270a31` | vorhanden | vorhanden | vorhanden |

Der produktive Git-Diff vom Lauf-24-Vorbereitungsstand zum zugehörigen Bericht sowie von der Lauf-25-Vorbereitung zum untersuchten HEAD ist jeweils leer.[7][35]
**Wichtig:** Der Lauf-24-Vorbereitungscommit trägt 23:00:53Z, sein Maß-Freeze liegt davor, Gen 1 danach.[7][35]
Das ist eine Provenienzlücke, aber kein selbständiger Beweis, dass zwischen zwei tatsächlich ausgeführten Generationen von 24 das Messgerät wechselte.[7][35]
Für 22/23 existieren dagegen die oben genannten realen Übergänge.[7][35]
Commitzeit wird hier weder als Laufzeit noch als alleiniger Verwerfungsgrund benutzt.[7][35]

Für **24 und 25** finden sich jeweils **0 Zeilen in `eichung`, 0 in `eichkosten` und 0 zugehörige Eichproben-/Eichungsereignisse** innerhalb der Lauflebenszeit.[14][15][34]
Die vorhandenen Übernahme-/Neubewertungsereignisse ersetzen keinen vollständigen Vorspann.[14][15][34]
Die Gesamtstandsprüfungen A/B (35 bzw.[14][15][34]
25 Befunde, nicht Bauteilzahlen) belegen die fehlende Verbindlichkeit des Vorspanns und die Integrationsfehler; ihre Befunde werden nicht pauschal in „alles wertlos“ übersetzt.[14][15][34]

## 4. Bauteil A — was seine natürliche Evidenz tatsächlich trägt

| Lauf | Ansagen | Angriff freigegeben | Bekannte Ansage gesperrt | Keine Behauptung | Ansagekosten | Angriffskosten |
|---|---:|---:|---:|---:|---:|---:|
| 24 | 27 | 11 | 10 | 6 | 0,019462963 € | 0,014954074 € |
| 25 | 23 | 3 | 16 | 4 | 0,019703796 € | 0,003535648 € |

Die Aufrechnungen schließen.
`A-rekonstruktion.json` prüft **alle 50 Entscheidungen** mit der Originalfunktion gegen den zeitlich vorausliegenden Vorrat.[29][34]
Bei sämtlichen 26 gesperrten Ansagen ist ein rekonstruiertes Gegenstück vorhanden; kein ausgeführter Schlüssel war im so rekonstruierten Vorrat enthalten, und alle protokollierten Vorratszahlen stimmen.[29][34]
Das gilt **für Schlüssel und Ansageentscheidungen**, nicht für semantische Fehlerfreiheit oder die spätere Aufnahme.[29][34]
Nicht mehr vorhandene bzw.[29][34]
nachträglich überschriebene historische Ursprünge sind aus dem Endsnapshot nicht wiederherstellbar.[29][34]

Ein echter Vorher-/Nachher-Fall innerhalb desselben Laufs ist **#14533 (2026-09-19T23:01:36.109Z)**: `auswerten|Eq:` ausgeführt bei Vorrat 1; anschließend **#14557 (23:02:12.056Z)**: derselbe Schlüssel gesperrt bei Vorrat 2.[35]
Die Modell-Ankündigung und der tatsächliche Testschlüssel werden dennoch nicht gleichgesetzt.[35]

### Die drei neuen Immunzeilen aus Lauf 24

| DB-ID / Name | Erzeugt UTC / Ereignis | Status im Snapshot | Schlüssel und Altgegenstück |
|---|---|---|---|
| 337 / `norm_k2458_lager` | 2026-09-19T23:09:00.573Z / #14775 | `offen_norm` | `reservierung_einloesen\|raises:NichtGenugBestand`; schon in Übernahmen 315 und 331 |
| 338 / `aegis_k2500_preise` | 2026-09-19T23:16:20.547Z / #15005 | `gefunden` | `preis_fuer\|GtE:zahl`; schon in Übernahme 336 |
| 339 / `aegis_k2526_lager` | 2026-09-19T23:20:47.268Z / #15146 | `gefunden` | `gesamtmenge\|Eq:zahl`; kein Gegenstück im übernommenen Vorrat |

Damit sind **zwei vorratsdoppelnde Einträge unter drei neuen Immunzeilen** belegt; davon eine Normzeile und eine Fundzeile.[8][7]
Vergleichsmenge ist der vorab übernommene Bereichsvorrat, die Schlüsselableitung ist die Originalfunktion — nicht der Endbestand einschließlich des eigenen neuen Eintrags.[8][7]
Das bestätigt den Aufnahmebefund, ohne die Norm nachträglich zum gültigen Fund zu machen.[8][7]
In Lauf 24 war C noch nicht eingebaut; das ist daher kein historischer C-Fehler.[8][7]

Der frühere N10-Bericht ordnet K2500 der Ansage **#15027** zu.[11][35]
Das ist **zeitlich unmöglich**: #15027 entstand erst um **23:16:38.204Z**, nach Immunzeile 338.[11][35]
#15002 um **23:16:17.635Z** ist die zeitlich benachbarte `rabatt_anwenden|GtE:zahl`-Ansage; mangels Kandidaten-ID im Ansagepayload wird hier keine harte Ersatzzuordnung behauptet.[11][35]
Die belegte Doppelung braucht diese unsichere Zuordnung nicht.[11][35]

**Gültig:** A unterdrückt nachweislich spätere Angriffsschritte bei bekannten Ansagen bzw.[30][34]
fehlender Behauptung.
**Nicht gültig:** „A verhindert tatsächliche Doppelungen“, die alten Rückgänge A allein zuzuschreiben oder vermiedene Kosten/Kammerläufe als gemessene Gegenwelt auszugeben.[30][34]
Ansagen kosten selbst Geld; die ohne A erzeugten Antworten und deren Kammeraufwand wurden nicht beobachtet.[30][34]
Die bloße Abweichung einer Ansage vom Test bleibt diagnostisch, kein neues Killkriterium.[30][34]

## 5. Bauteil B — Vorlage, Bestand und Mentor getrennt

Die historische Bestandsausgabe nennt für Werk 19 **19 eigene Instanzen und 6 fremde Muster**, für Werk 20 **14 eigene und 11 fremde**; der Bericht beschreibt die Vorlagenänderung **3 → 6 fremde Muster** für `lagerhaus`.[12][11][15]
Diese Werte sind ein archivierter Vorlagen-/Bestandsbefund, **keine rückwirkend aus vollständigen Request-Payloads bewiesenen Eingabetexte**.[12][11][15]

| Historischer Mentor-Ausgang | UTC | Richtungen mit fremdem Verweis | Geltungsgrenze |
|---|---|---:|---|
| #14246 / Lauf 22 | 2026-09-19T22:45:33.318Z | 3 von 4 | Ausgang belegt; Lauf bleibt unter Satz-2-Vorbehalt |
| #14480 / Lauf 24 | 2026-09-19T23:00:43.371Z | 1 von 5 | Verweise A597, A569 in einer Richtung |
| #15276 / Lauf 25 | 2026-09-20T01:15:08.017Z | 1 von 5 | Verweise A597, A569 in einer Richtung |

Das belegt Vorhandensein von werkübergreifenden Bezügen in konkreten Ausgaben, nicht eine isolierte kausale Mentorwirkung.[10][35]
Die frühere enge Abnahme bezeichnet bereits **Streuung statt Wirkung**.[10][35]

Der aktuelle historische Code verspricht mindestens die Hälfte, rechnet aber mit `GEZEIGT // 2`: bei ausreichend großen Beständen **12 fremde von 25 = 48 %**.[15][31][34]
Zudem wird das globale Fenster der letzten 200 angenommenen Einträge vor dem Fremdmusterfilter begrenzt.[15][31][34]
Das sind die statischen Befunde **B-14** des Gesamtstands; hier wurde kein neuer Gegenfall ausgeführt.[15][31][34]
Die spätere Bauarbeit kann diese Mängel beheben, aber nicht rückwirkend die alte Vorlagenbehauptung für jeden Bestand wahr machen.[15][31][34]

## 6. Bauteil C — natürliche Nullpopulation und gestellte Pfade

### Natürlicher Lauf 25

**Kein natürlicher Wirkungsnachweis:** 23 Ansagen → 3 freigegebene Angriffe, 16 Sperren durch A, 4 ohne Behauptung.[34][35]
Zwei Urteile enthalten einen Angriffsmodellabschnitt: **#15340, 2026-09-20T01:19:15.582Z** und **#15402, 01:23:33.233Z**.[34][35]
Darin stehen insgesamt **1 + 2 = 3 erfasste Angriffstests**, aber keine bestätigten Funde, keine Normaufnahme und kein natürlicher C-Aufruf.[34][35]
„0 Funde/Immunzeilen“ bedeutet also nicht „kein Angriffstesttext existierte“.[34][35]

**Kein neuer Tor-Nenner:** Der Feldzähler `angriff.gesamt`, die Anzahl neuer Fundzeilen und die Anzahl neuer Normzeilen werden nur auseinandergehalten.[10][34]
Zeile 8 bleibt ungemessen; die bisherige Definition wird hier nicht nachträglich durch eine bequemere Population ersetzt.[10][34]
Auch Lauf 24 mit zwei neuen Fundzeilen begründet keine Freigabe dieser Torlinie.[10][34]

### Historische gestellte Nachprüfungen nach dem normalen Lauf

| C-Aufruf / Zeit UTC | Stelle | Sperrereignis / roter Schlüssel | Einordnung |
|---|---|---|---|
| #16010 / 2026-09-20T01:51:51.236Z | norm | #16011 / `reserviert\|Eq:zahl` | erster Lager-Durchlauf |
| #16014 / 01:52:33.862Z | norm | #16015 / `reserviert\|Eq:zahl` | Wiederholung desselben Schlüsselfalls |
| #16019 / 02:03:33.208Z | norm | #16020 / `preis_fuer\|GtE:zahl` | Preis-Durchlauf noch an Norm-Stelle |
| #16022 / 02:04:02.763Z | norm | #16023 / `preis_fuer\|GtE:zahl` | weitere Norm-Wiederholung |
| #16026 / 02:04:52.311Z | fund | #16027 / `preis_fuer\|GtE:zahl` | Fund-Stelle tatsächlich erreicht |

**Bilanz:** fünf C-Aufrufe mit neun Testdurchläufen und fünf Sperrungen; **zwei verschiedene (Bereich, Schlüssel)-Fälle**, **drei (Stelle, Bereich, Schlüssel)-Kombinationen**.[10][34][35]
Die frühere Zahl „drei verschiedene Sperrfälle“ ist zu stark; dies war bereits in der engen Abnahme korrigiert.[10][34][35]

Es liegen insgesamt **sechs** `aegis.urteil`-Durchläufe mit der wiederverwendeten Kandidaten-ID **K2680** vor (#16013, #16017, #16018, #16021, #16025, #16030); einer davon, **#16018 um 02:02:57.077Z**, scheiterte vor C am Grenzmaß.[34][35]
Alle sechs Gesamturteile sind `abgelehnt`.[34][35]
Ein „grüner“ Aufnahmegegenstand bedeutet deshalb nicht, dass der ganze Prüfkandidat angenommen wurde.[34][35]
Die Kandidaten-/Immunzeilen dieser Proben sind im Endsnapshot entfernt, die Protokollereignisse bestehen fort.[34][35]

Die grünen Aufnahmeereignisse sind u.a.[35]
**#16012/#16016** (`inventur|Eq:text`, Norm) und **#16029** (Fund).[35]
**#16028 um 02:04:52.314Z** protokolliert die gestellte Abweichung zum tatsächlich abgeleiteten Schlüssel `anzahl|Lt:name`; nicht zum Kommentarwert `Lt:zahl`.[35]
Daher gilt: **0 natürliche V9-Zeilen, 1 gestellte V9-Zeile**, nicht im Gesamtsnapshot „0 Zeilen“.[35]

### Warum diese Belege erhalten bleiben, die Integration aber offen ist

Beide Probescripte ersetzten `_angriff` durch eine gestellte Rückgabe.[18][19]
Die folgenden Kernschritte einschließlich C liefen historisch wirklich; die natürliche A-Ansage samt Protokollierung lief in diesen Proben gerade **nicht**.[18][19]
Der Nachweis „C sitzt an Norm- und Fund-Aufnahme“ bleibt bestehen.[18][19]
Die Ableitung „A und C funktionieren zusammen korrekt“ folgt daraus nicht.[18][19]

Im fixierten Code protokolliert A die neue Ansage **vor** dem Schreiben des Tests; C liest später `bisherige_behauptungen` einschließlich dieser frischen Ansage.[14][15][30]
Passt der bestätigte neue Test zu seiner eigenen Ansage, kann er deshalb als bereits vorhandene Doppelung gesperrt werden.[14][15][30]
Das ist der statisch belegte **A33/B-11-Selbstblock**, keine in Lauf 25 gemessene natürliche Fehlalarmquote: dort erreichte kein natürlicher Gegenstand C.[14][15][30]

**C-Schlüsselabweichung ist weiterhin Diagnostik, kein Kill.** #16028 sagt ausdrücklich „V9 zählt nur“.[30][35]
Eine echte neue Behauptung soll nicht deshalb sterben, weil das Modell etwas anderes angekündigt hat.[30][35]
Die notwendige Reparatur betrifft die Herkunft und den Zeitpunkt des Vergleichsvorrats, nicht ein pauschales Verbot von Abweichungen.[30][35]

## 7. Kasse und weitere Berichtsgrenzen

| Lauf / Menge | Buchungen | Gespeicherte Rohsumme, € | Laufbudget, € | Anteil |
|---|---:|---:|---:|---:|
| 22 vollständig, unter fachlichem Vorbehalt | 233 | 0,51660830555555551616 | — | — |
| 23 vollständig, unter fachlichem Vorbehalt | 239 | 0,39361428703703700225 | — | — |
| 24 | 193 | 0,39687799999999996263 | 1,50 | 26,5 % |
| 25 | 183 | 0,38992867592592589323 | 0,80 | 48,7 % |
| **24 + 25** | **376** | **0,78680667592592585586** | getrennte Laufgrenzen | — |
| **22–25** | **848** | **1,69702926851851837427** | frühere Abschnittsentscheidung 3,00 | — |

Die Summen sind mit `Decimal(str(gespeicherter_Wert))` aus Einzelbuchungen nachgerechnet, nicht aus auf Cent gerundeten Berichtszeilen.[23][34]
Für 24 sind es Kassen-IDs **3695–3887**, Zeitfenster **2026-09-19T22:57:52.151Z bis 23:25:25.546Z**; für 25 **3888–4070**, **2026-09-20T01:13:33.011Z bis 01:43:33.219Z**.[23][34]
Die 193 bzw.
183 protokollierten Modellversuche lassen sich über echte `aufruf_nr`-Referenzen jeweils vollständig mit Antworten verbinden; kein `modell.fehler` oder unbeantworteter Versuch dieser Mengen.[23][34]
Das ist ein Kassen-/Protokollabgleich, keine Providerrechnungsprüfung.[23][34]

Die erste Etappe von 22 umfasst **189 Buchungen / 0,39776329629629626276 €**, die spätere **44 / 0,1188450092592592534 €**.[9][10]
Diese fehlende erste Etappe darf nicht Lauf 25 zugerechnet werden.[9][10]
Die vorsichtige historische Abschnittsentscheidung V16 blieb **1,6970 €**; der reine alternative Mengenschnitt „nur Fortsetzung 22 plus 23–25“ beträgt rechnerisch **659 / 1,29926597222222211151 €**, wird hier aber **nicht** zur neuen autorisierten Abschnittszuordnung erklärt.[9][10]

Die Nachprüfung fand **15** archivierte `.err`-Dateien, davon **eine** nicht leer: `04g6-gen6.err` meldet „Lauf 23 ist im Zustand gesaettigt, nicht bereit“.[20][11]
Generation 6 begann dort nicht.[20][11]
Die vorhandenen Fehlermeldungen werden nicht durch bloßes Lesen der Ergebnisdatenbank übergangen; zugleich ist das kein behaupteter Abbruch von 24/25.[20][11]

### Nicht ungeprüft aus Nachgängen übernehmen

Die N8-Erklärung, drei Angriffe seien im Sammelurteil #14707 zusammengefasst, stimmt nicht mit den Datensätzen überein: **#14664 (23:05:13.691Z) gehört K2439**, **#14693 (23:06:29.188Z) K2442**, beide mit `angriff=null`.[11][33][35]
K2444 wurde erst **#14698 um 23:07:18.682Z** erzeugt, sein Urteil ist #14707.[11][33][35]
Die Antworten #14663 und #14692 referenzieren die Aufrufe #14662/#14691 und haben jeweils zwölf Zeichen; ihr Rohtext ist nicht gespeichert.[11][33][35]
Deshalb werden weder der genaue Antwortinhalt noch eine Ersatz-Sammelzuordnung erfunden.[11][33][35]
Belastbar bleiben **11 gebuchte Angriffsaufrufe / 9 Urteile mit Angriffsmodell** für 24 als getrennte Mengen.[11][33][35]

Auch „14 zu Norm umgestuft“ wird präzisiert: **40 Einträge übernommen, 13 Statuswechsel**, danach 14 Normeinträge einschließlich einer bereits übernommenen Norm.[8][35]
Das belegen #14477 bzw.[8][35]
#15273 unmittelbar.
Kein früherer Eintrag wird dafür gelöscht oder umklassifiziert.[8][35]

## 8. Lesedisziplin, Integrität und Lieferung

Keine Produktiv-CLI, kein Biotop-Import, kein Modell-/Kammeraufruf, keine neue Probe und kein Produkttest wurde in diesem Teilauftrag ausgeführt.[22][28][34]
Die wenigen Originalableitungen wurden aus dem fixierten Git-Quelltext isoliert und nur auf bestehende Datensätze angewendet.[22][28][34]
Neue Dateien liegen ausschließlich im Lieferordner.[22][28][34]
Die lokalen Konsistenz-/SQL-Prüfungen sind keine reparierte Biotop-Testsuite.[22][28][34]

**Die Quellumgebung blieb nicht pauschal unverändert:** Der initial saubere Arbeitsbaum zeigte während der Untersuchung Änderungen und neue Dateien.[36]
Dieser Teilauftrag hat sie weder ausgeführt noch zurückgesetzt.[36]
Die Bewertung bleibt am fixierten HEAD; dessen relevante Originalquellen sind im Unterordner `quellen/` mitgeliefert.[36]
`zustand-nachher.json` und `VERIFIKATION.json` weisen den tatsächlichen Vorher-/Nachher-Unterschied aus.[36]
Über fremde Teilaufträge oder die Live-Kasse wird damit nichts behauptet.[36]

**Lieferprüfung ausgeführt:** 14 SELECT-Abfragen und 27 lokale Integritäts-/Konsistenzprüfungen erfolgreich; sechs Quellkopien bytegleich mit ihren Git-Blobs.[36][37]
Der eingefrorene DB-Snapshot ist in Inhalt, Größe und mtime unverändert, SHA-256 `711b2bbdca478f7f0de941a88cc51e72c46c9c7a20a3a908065f42861520fe14`.[36][37]
Keine neuen Biotop-Modellbuchungen durch diesen Teilauftrag; die Kosten des Trägermodells wurden nicht gemessen.[36][37]

Der erste Quellkopie-Export verlor im Terminal-Texttransport jeweils den letzten Zeilenumbruch.[36]
Die daraufhin fehlgeschlagene Byteprüfung ist in `VERIFIKATION-ERSTVERSUCH.json` erhalten; der korrigierte direkte Byteexport wurde erfolgreich erneut geprüft.[36]
Das betraf ausschließlich Lieferkopien, nicht den Quellbaum oder Messergebnisse.[36]

**Beweisgrenzen:** Keine nachträgliche Wiederholung der alten Werkmessungen, keine neue Normfreigabe, keine natürliche C-Wirksamkeitsmessung, keine vollständigen historischen Modellprompts, kein ausgeführter B-Gegenfall.[34]
Der Bericht unterscheidet ausdrücklich `gilt`, `gilt nicht` und `unter Vorbehalt`; eine vorgeschlagene Fortsetzungssperre ist keine vollzogene Datenänderung.[34]

Vollständige lokale Lieferadressen:

- Bericht: `/root/reparatur-01/teil-historie/STATUS-24-25.md`
- Strukturierter Status: `/root/reparatur-01/teil-historie/STATUS-24-25.json`
- Ereignisregister mit Originalzeiten: `/root/reparatur-01/teil-historie/chronologie.json`
- Reproduzierbare Abfragen: `/root/reparatur-01/teil-historie/status-abfragen.sql` und `/root/reparatur-01/teil-historie/abfragen.sql`
- Einzelkosten: `/root/reparatur-01/teil-historie/kasse.json`; Mengenschnitte: `/root/reparatur-01/teil-historie/kosten-abgrenzung.json`
- Lieferprüfung: `/root/reparatur-01/teil-historie/VERIFIKATION.json`
- Dateiliste: `/root/reparatur-01/teil-historie/DATEIEN.txt`
- Dateihashes: `/root/reparatur-01/teil-historie/PRUEFSUMMEN.sha256`
- Manifestprüfsumme: `/root/reparatur-01/teil-historie/PRUEFSUMME-ORDNER.txt`

Die öffentliche Veröffentlichung ist Aufgabe der übergeordneten Reparaturlieferung; dieses Teilpaket behauptet keinen erfolgten HTTPS-Abruf.

## Sources

[1] file:///root/reparatur-01/teil-historie/nutzerentscheidungen.json — nutzerentscheidungen.json
[2] file:///root/reparatur-01/teil-historie/laeufe.json — laeufe.json
[3] file:///root/reparatur-01/teil-historie/generationen.json — generationen.json
[5] file:///root/reparatur-01/teil-historie/nachrechnung.json — nachrechnung.json
[6] file:///root/reparatur-01/teil-historie/werkstaende.json — werkstaende.json
[7] file:///root/reparatur-01/teil-historie/quellstaende.json — quellstaende.json
[8] file:///root/reparatur-01/teil-historie/immun-schluessel.json — immun-schluessel.json
[9] file:///root/reparatur-01/teil-historie/kosten-abgrenzung.json — kosten-abgrenzung.json
[10] file:///root/.hermes/cache/documents/doc_f18e4c5d9f14_ABNAHME_Vorbedingung-1_2026-09-20.md — doc_f18e4c5d9f14_ABNAHME_Vorbedingung-1_2026-09-20.md
[11] file:///var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/NACHGANG-03.md — NACHGANG-03.md
[12] file:///var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/ausgaben/03-vorbedingung1-messung.txt — 03-vorbedingung1-messung.txt
[14] file:///var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/pruefungen/pruefung-a/BEFUND.md — BEFUND.md
[15] file:///var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/pruefungen/pruefung-b/BEFUND.md — BEFUND.md
[18] file:///root/biotop/pruefung/lauf25_pfadnachweis.py — lauf25_pfadnachweis.py
[19] file:///root/biotop/pruefung/nachgang_n13_n14.py — nachgang_n13_n14.py
[20] file:///root/reparatur-01/teil-historie/runner-stderr.json — runner-stderr.json
[21] file:///root/reparatur-01/teil-historie/zustand-vorher.json — zustand-vorher.json
[22] file:///root/reparatur-01/teil-historie/abfragen.sql — abfragen.sql
[23] file:///root/reparatur-01/teil-historie/kasse.json — kasse.json
[28] file:///root/reparatur-01/teil-historie/vertiefen.py — vertiefen.py
[29] file:///root/reparatur-01/teil-historie/A-rekonstruktion.json — A: Rekonstruktion aller historischen Entscheidungen
[30] file:///root/reparatur-01/teil-historie/quellen/b42dc941e7fcb66632ba6a0e13b8df106a270a31/biotop/organe/aegis.py
[31] file:///root/reparatur-01/teil-historie/quellen/b42dc941e7fcb66632ba6a0e13b8df106a270a31/biotop/organe/gedaechtnis.py
[32] file:///root/reparatur-01/teil-historie/quellen/b42dc941e7fcb66632ba6a0e13b8df106a270a31/biotop/organe/eichproben.py
[33] file:///root/reparatur-01/teil-historie/quellen/293b1c16c53ca76fb737587b1c09b04bd21fcdba/biotop/organe/aegis.py
[34] file:///root/reparatur-01/teil-historie/STATUS-24-25.json
[35] file:///root/reparatur-01/teil-historie/chronologie.json
[36] file:///root/reparatur-01/teil-historie/VERIFIKATION.json
[37] file:///root/reparatur-01/teil-historie/status-abfragen.sql
