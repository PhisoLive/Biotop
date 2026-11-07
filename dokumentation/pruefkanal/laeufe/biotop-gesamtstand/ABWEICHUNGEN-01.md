# Abweichungen vom Masterprompt Fassung 6 — konsolidierter Codebefund

**49 Befundgruppen** aus zwei überlappend geprüften Teilsichten und drei Ergänzungen des Hauptprüfers. Das ist eine redaktionelle Gruppierung, keine behauptete Naturkonstante der Fehlerzahl. Zwei frühere Abweichungen (A34, A35) sind heute aufgehoben und separat ausgewiesen. Alle Einzelbefunde bleiben in den Anlagen erhalten; kein ungünstiger Befund wurde gestrichen.

**Beweisgrenze:** Statische Codebelege sind gelesen, nicht vollständig dynamisch ausgeführt. Historische Protokollbelege sind historische Ausführung, kein frischer Abnahmelauf. A22 und A27 bleiben Risiken, nicht beobachtete Schadensfälle. Selbst eine zeilenweise Prüfung garantiert nicht, jeden denkbaren Fehler gefunden zu haben.

Quellen: unverändertes `biotop/QUELLSTAND-01.tar.gz`, vollständiger Solltext `quellen/MASTERPROMPT-FASSUNG-6.md`, Einzelprüfungen unter `pruefungen/`. Die Quellenbereiche und in A vorhandenen Quellhashes wurden am Original nochmals geprüft (`22-referenzpruefung.json`).

## Befunde

### A01 — Aufnahme ist auf eine schmale Python-Paketform beschränkt; Abhängigkeiten und echter Bau fehlen
Zugeordnete Einzelbefunde: A01.

**A01: Aufnahme ist auf eine schmale Python-Paketform beschränkt; Abhängigkeiten und echter Bau fehlen**
**Status:** statisch belegt.
**F6:** Z. 69–69, Z. 119–121.
**Code:** `biotop/organe/landkarte.py:1–6`; `biotop/organe/aufnahme.py:22–24`; `biotop/organe/aufnahme.py:83–87`; `biotop/organe/aufnahme.py:117–160`; `biotop/organe/landkarte.py:33–39`; `kammer/Dockerfile:1–4`.
Die Aufnahme erkennt Endungen, wählt aber die Sprache nach den meisten Zeilen einschließlich Markdown/JSON und führt Tests/Bau nur bei sprache == 'Python' aus. _paket nimmt das erste alphabetische Wurzelpaket mit __init__.py; Bereiche sind dessen unmittelbare Unterpakete. Bau bedeutet lediglich import <paket>. Weder Aufnahme noch das feste Kammer-Image lesen/installieren Werkabhängigkeiten oder wählen Bauwerkzeuge. src-Layouts, mehrere Dienste, namespace packages und andere Sprachen sind damit keine implementierten Aufnahmewege.
Der Anspruch beliebiger Quelltext sowie die Aufnahme- und Phase-4-Vorbedingung sind nicht allgemein erfüllt; selbst ein Python-Werk kann aufgrund umfangreicher Dokumentation den Testlauf überspringen.
**Grenze:** Kein echtes Werk neu aufgenommen; keine Abhängigkeit installiert. Dies ist eine belegte Implementierungsbegrenzung, kein gemessener Fehler eines bestimmten Werks.

**Eigenanteil Hermes:** Landkarte Z.3–4 verschiebt tree-sitter ausdrücklich als „Entscheidung Hermes“ nach hinten, weil Phase 1 nur Python-Werke hat. Das belegt eine frühere Scope-Entscheidung, keine heutige F6-Freigabe für die weiterhin schmale Aufnahme.

### A02 — Ethische Prüfung akzeptiert ungültige oder leere Antworten als UNBEDENKLICH
Zugeordnete Einzelbefunde: A02.

**A02: Ethische Prüfung akzeptiert ungültige oder leere Antworten als UNBEDENKLICH**
**Status:** statisch belegt.
**F6:** Z. 90–90, Z. 95–95, Z. 119–121.
**Code:** `biotop/organe/aufnahme.py:90–114`; `biotop/organe/aufnahme.py:151–175`.
Das Urteil ist nur dann BEDENKLICH, wenn die erste Antwortzeile BEDENKLICH und nicht UNBEDENKLICH enthält. Jede andere Antwort, auch leer, unbekannt oder ohne Begründung, landet im else UNBEDENKLICH. Die Modellgrundlage besteht aus werkseigenen Beschreibungsdateien, einer begrenzten Python-Dateiliste und Stichworttreffern; Funktionscode wird nicht unabhängig semantisch geprüft. Stichworttreffer allein sperren nicht.
Fehlende oder nicht interpretierbare Prüfung besteht statt anzuhalten. Werkseigene Beschreibungen dominieren die Zweckbeurteilung.
**Grenze:** Kein schädliches Werk und keine Täuschungsantwort erzeugt. Prompt-Manipulation bleibt Risiko; der permissive Antwortparser ist direkt belegt.

### A03 — Aufnahmeziel wird ungeprüft gelöscht; Wiederaufnahme desselben Namens verändert andere Läufe
Zugeordnete Einzelbefunde: A03.

**A03: Aufnahmeziel wird ungeprüft gelöscht; Wiederaufnahme desselben Namens verändert andere Läufe**
**Status:** statisch belegt.
**F6:** Z. 88–89, Z. 106–106, Z. 270–279.
**Code:** `biotop/__main__.py:37–38`; `biotop/organe/aufnahme.py:35–59`; `biotop/organe/aufnahme.py:117–125`; `biotop/organe/aufnahme.py:163–169`; `biotop/lauf.py:54–67`.
Der frei übergebene name wird direkt an WERKE angehängt. Absolute Pfade bzw. .. werden nicht auf einen erlaubten Namensraum begrenzt; _holen löscht ein vorhandenes Ziel mit shutil.rmtree, noch bevor die Quelle validiert ist. Auch ein normaler wiederverwendeter Name ersetzt dieselbe Arbeitskopie und aktualisiert denselben werke-Datensatz per ON CONFLICT. Andere Läufe können auf diese werk_id und diesen Pfad zeigen.
Destruktiver Pfad außerhalb des vorgesehenen Werkverzeichnisses ist nicht mechanisch ausgeschlossen; Wiederaufnahme ist kein isolierter Lauf und kann einen laufenden Bestand austauschen.
**Grenze:** Kein problematischer Name übergeben, nichts gelöscht. Die konkrete Löschfolge und fehlende Pfad-/Laufsperre wurden nur gelesen.

### A04 — Kandidaten- und Kammerpfade besitzen keine kanonische Begrenzung zum Werk
Zugeordnete Einzelbefunde: A04.

**A04: Kandidaten- und Kammerpfade besitzen keine kanonische Begrenzung zum Werk**
**Status:** statisch belegt.
**F6:** Z. 88–88, Z. 121–121, Z. 237–238, Z. 270–279.
**Code:** `biotop/organe/genesis.py:75–76`; `biotop/organe/genesis.py:129–136`; `biotop/kern/diffwerk.py:48–61`; `biotop/organe/aegis.py:53–71`; `biotop/organe/kammer.py:38–42`; `biotop/organe/kammer.py:54–61`; `biotop/lauf.py:316–323`.
Genesis prüft nur textuelle Präfixe der aus dem Diff herausgelesenen Namen. Ein Pfad mit erlaubtem Präfix und folgenden ..-Segmenten bleibt zulässig; die Regex deckt außerdem nicht dieselben Headerformen ab wie diffwerk.parsen. Aegis liest werk / d.pfad vor einer kanonischen Prüfung; Kammer schreibt arbeit / rel direkt auf dem Wirt, und die spätere Übernahme schreibt pfad / p. Aufnahmekopie/Kammer dereferenzieren Symlinks statt sie auf Werkgrenzen zu begrenzen.
Wirts-Lese-/Schreibpfade außerhalb der Werkgrenze sind im Kandidatenweg nicht ausgeschlossen. Die Aussage, aus Schwarm/Kammer gebe es keine Schreibpfade in den Kern, ist strukturell nicht durchgesetzt.
**Grenze:** Keine Exploit-Datei, kein Symlink und kein Ausbruch ausgeführt. Bestätigt ist die fehlende Pfadvalidierung an allen genannten Übergängen, nicht ein erfolgter Kernzugriff.

### A05 — Straßen sind nur Importkanten; Funktionsaufrufe werden nie ausgewertet
Zugeordnete Einzelbefunde: A05.

**A05: Straßen sind nur Importkanten; Funktionsaufrufe werden nie ausgewertet**
**Status:** statisch belegt.
**F6:** Z. 129–132, Z. 189–193, Z. 402–402.
**Code:** `biotop/organe/landkarte.py:57–95`; `biotop/organe/landkarte.py:98–125`; `biotop/kern/messgeraet.py:168–191`.
strassen baut zwar fn_index auf, verwendet ihn danach aber nicht. Die einzigen Zweige behandeln ast.ImportFrom und ast.Import; keine ast.Call-Auswertung und keine Kante art='aufruf' existiert im Rückgabepfad. Bei from . import nachbar wird das importierte Alias-Ziel nicht aufgelöst. Das Grenzmaß Zyklen hat zudem eine zweite, textbasierte Ableitung über Zeilen-Substringsuche statt denselben AST-Graphen.
Aufrufgraph, Bereichsabhängigkeiten und Wirkungskreis können unvollständig sein; Kommentar-/Stringtreffer können gleichzeitig die Zyklenzahl verfälschen. Eine Anzahl gespeicherter Straßen beweist keine Vollständigkeit.
**Grenze:** Keine unabhängige Zählung eines Werkgraphen ausgeführt; keine tatsächliche Zahl fehlender Kanten behauptet.

### A06 — Vertragsableitung liefert keine Grenzzusicherungen und blendet eigene abgeleitete Verträge aus
Zugeordnete Einzelbefunde: A06.

**A06: Vertragsableitung liefert keine Grenzzusicherungen und blendet eigene abgeleitete Verträge aus**
**Status:** statisch belegt.
**F6:** Z. 128–132.
**Code:** `biotop/organe/landkarte.py:42–54`; `biotop/organe/landkarte.py:128–150`; `biotop/organe/landkarte.py:230–255`; `biotop/kern/datenbank.py:50–52`.
Stufe 3 enthält nur kn.args.args; positional-only, keyword-only, Varargs, Defaultwerte und Annotationen fehlen. Zweck ist nur die erste Docstringzeile, sonst leer. vertraege_ableiten übernimmt vorhandene Docstring-Aufzählungen oder hängt Signatur/Zweck aneinander; ohne Docstring steht 'ohne Beschreibung'. Grenzpartner, Eingabe-/Ausgabe-/Nebenwirkungszusicherungen werden nicht abgeleitet. sicht liest ausdrücklich nur herkunft='docstring', obwohl sie abgeleitete Verträge ankündigt.
Wo ein Werk keine expliziten Verträge besitzt, erhält der Schwarm gerade keine belastbar abgeleiteten Grenzzusicherungen.
**Grenze:** Explizite Vertragstests existieren als separates Organ; dies widerlegt deren Existenz nicht, sondern betrifft den zugesagten Landkarten-Fallback.

### A07 — Landkarte wird nach Veränderungen nicht konsistent aktualisiert; alte Einträge bleiben sichtbar
Zugeordnete Einzelbefunde: A07.

**A07: Landkarte wird nach Veränderungen nicht konsistent aktualisiert; alte Einträge bleiben sichtbar**
**Status:** statisch belegt.
**F6:** Z. 131–132, Z. 212–212.
**Code:** `biotop/organe/landkarte.py:154–183`; `biotop/organe/landkarte.py:192–255`; `biotop/lauf.py:70–77`; `biotop/lauf.py:316–356`; `biotop/organe/lazarus.py:90–110`; `biotop/organe/genesis.py:93–114`.
bauen löscht Straßen/Verträge, aber entfernt keine Landkarten-Zeilen für weggefallene Dateien oder Bereiche; Einträge werden nur upserted. Die Generation schreibt neue Dateien und archiviert sie ohne Aufruf von landkarte.bauen. Rueckkehr markiert lediglich Stufe <=2 als veraltet; sicht prüft keine Prüfsumme und liest auch alte Stufe-3-Inhalte. Genesis mischt diese Daten mit frisch gelesenen Quelldateien. Der Landkartenpfad enthält auch keinen Chunking-/Embedding-/Suchindex des in F6 vorgesehenen Aktenschranks.
Der Schwarm kann alte Signaturen und Verträge neben neuer Implementierung sehen; die Kennzeichnung 'veraltet' bewirkt allein keine Aktualisierung.
**Grenze:** Ein externer Aufrufer kann neu kartieren; im gelesenen Generations-/Rückkehrpfad ist das nicht erzwungen. Kein globaler Nachweis, dass außerhalb der geprüften Module kein alter Aktenschrank existiert.

### A08 — Generation minus eins und Generation 0 sind keine erzwungenen Startvoraussetzungen
Zugeordnete Einzelbefunde: A08, B-02.

**A08: Generation minus eins und Generation 0 sind keine erzwungenen Startvoraussetzungen**
**Status:** statisch belegt.
**F6:** Z. 104–104, Z. 159–173, Z. 255–258.
**Code:** `biotop/lauf.py:54–115`; `biotop/lauf.py:133–166`; `biotop/lauf.py:557–616`; `biotop/__main__.py:34–64`; `pruefung/vorspann.py:15–56`.
mass_einfrieren setzt den Lauf unmittelbar auf bereit und Generation 0 auf angenommen, ohne Mutantenquote oder Eichungsbeleg zu lesen. generation kontrolliert Status und Freigabe, nicht Eichung/Mutantenfang. Der separate Vorspann erwartet bereits ein eingefrorenes Maß, bewertet Funde vor den vier Proben und schreibt 'Lauf startet' nur als Berichtstext. Es fehlt ein benannter CLI-Vorspann-Befehl. Bei fehlenden Tests stoppt einlegen vor dem Setzen von werk_id; das vorgeschlagene gen0 dereferenziert aber genau diese werk_id.
Die Reihenfolge aus F6 ist umgehbar und beim testlosen Werk über den vorgeschlagenen Standardweg nicht ausführbar. Ein falsch/gar nicht geeichtes Messgerät kann für Generation 1 benutzt werden.
**Grenze:** Nicht behauptet wird, dass konkrete historische Läufe ihren externen Vorspann ausgelassen haben. Die fehlende Kernvorbedingung ist statisch belegt.

**B-02: Generation minus eins ist gebaut, aber kein verpflichtender Laufpfad**
**Status:** aktuelle_Logik.
**F6:** Z. 159–169, Z. 104–104, Z. 222–222.
**Code:** `biotop/lauf.py:80–115`; `biotop/lauf.py:133–166`; `biotop/lauf.py:557–616`; `biotop/__main__.py:34–61`; `pruefung/vorspann.py:16–55`.
Die produktiven Befehle mass, gen0 und generation rufen weder eichung.rauschmessung noch eichproben.proben, eichgegenstand.sichern oder fundpruefung.bewerten auf und prüfen keinen Eichabschluss. mass setzt unmittelbar bereit und schreibt Generation 0. vorspann.py ist ein separat aufrufbares Prüfschema; es erwartet schon einen eingefrorenen Lauf, führt Fund-Neubewertung vor den vier Proben aus (umgekehrt zu F6) und druckt Lauf startet, ohne den Laufstatus zu sperren oder Eichwerte in laeufe.mass zu übernehmen. Ein benannter CLI-Befehl für den gesamten obligatorischen Vorspann fehlt.
Eine lauf_startet=False-Meldung bzw. eine bestandene Einzelprobe ist kein verbindliches Start-Gate. Proben und Neubewertung können ausgelassen werden; Generation 0 und normale Generationen bleiben erreichbar.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Eichung wurde historisch ausgeführt, aber über Prüfaufrufe: #12517 friert Lauf 22 ein, erst danach #12518 Rauschmessung, #12520 Neubewertung und #12544 Probenabschluss. Lauf 23 besitzt einen Freeze und Generationen, aber keinen ihm zugeordneten Eichprobenabschluss. Separate Organereignisse beweisen die Implementierung der Hauptpfadpflicht nicht.

### A09 — Einfrieren ist überschreibbar; Bestätigung und Messgerätstand sind nicht versiegelt
Zugeordnete Einzelbefunde: A09.

**A09: Einfrieren ist überschreibbar; Bestätigung und Messgerätstand sind nicht versiegelt**
**Status:** statisch belegt.
**F6:** Z. 86–86, Z. 173–173, Z. 270–279.
**Code:** `biotop/lauf.py:80–115`; `biotop/lauf.py:146–150`; `biotop/organe/verfassung.py:24–40`; `biotop/__main__.py:40–40`; `biotop/__main__.py:100–104`; `biotop/lauf.py:401–406`.
mass_einfrieren hat weder 'bereits eingefroren'- noch Laufstatus-/Autorisierungsprüfung. Es ersetzt mass und Generation-0-Datensatz desselben Laufs und ruft denselben Snapshot-Schlüssel auf. bestaetigt_von ist ein frei gelieferter String. Die Werkverfassung wird ebenfalls per INSERT OR REPLACE ohne Laufbindung/Änderungswache eingelegt. Das eingefrorene JSON enthält keine Prüfsummen von Messskript, Referenzlast, Ankläger oder Nischenregeln; generation liest die Referenzlast erneut aus dem aktuellen Kern. Auch die Freigabeidentität beruht auf startswith('philipp'), nicht einer festen Rolle.
Maß-/Messgerät-/Verfassungsänderungen erzwingen weder Abbruch noch einen neuen Lauf; die behauptete Unverhandelbarkeit ist keine technische Invariante.
**Grenze:** Kein eingefrorenes Maß geändert. Ein freier CLI-String ist bei vertrauenswürdigem Betreiber kein Beleg für tatsächlichen Missbrauch; der Schutzmechanismus selbst fehlt.

### A10 — Gemessene Rauschtoleranzen, Bereichssperren und Maschinenvorbehalt erreichen die Auswahl nicht
Zugeordnete Einzelbefunde: A10, B-03.

**A10: Gemessene Rauschtoleranzen, Bereichssperren und Maschinenvorbehalt erreichen die Auswahl nicht**
**Status:** statisch belegt.
**F6:** Z. 105–105, Z. 153–153, Z. 161–162.
**Code:** `biotop/organe/eichung.py:111–147`; `biotop/organe/eichung.py:150–217`; `biotop/kern/messgeraet.py:401–455`; `biotop/lauf.py:193–224`; `biotop/organe/landkarte.py:33–35`; `biotop/kern/messgeraet.py:143–166`; `biotop/kern/referenzlast/logmuehle.py:8–21`; `biotop/kern/referenzlast/logmuehle.py:24–53`.
rauschmessung extrahiert ausschließlich laufzeit_ms, nicht jedes Grenzmaß. Das Ergebnis wird gespeichert/zurückgegeben, aber der Generationsloop erzeugt für alle mass.bereiche Kandidaten. urteil_f2 ruft grenzen_f2 ohne dessen rauschtoleranz-Argument; damit bleibt der feste Fallback aktiv. Bauzeit erhält zusätzlich eine feste absolute Zugabe. Maschinenvorbehalte bleiben Rückgabedaten der Eichung, kein Feld der späteren Messungen. Aussetzer werden mit [b] statt der ursprünglichen Bereichsliste nachgemessen: bei logmuehle teilt _zeilen(n) einen Cache. In der alphabetisch sortierten Komplettmessung initialisiert last_ausgabe ihn zuerst per _zeilen(800); eine isolierte Nachmessung etwa von filtern verwendet dagegen _zeilen() mit Standardargument n=4000.
Das Eichorgan kann ein Messproblem ausweisen, ohne den betreffenden Produktionspfad zu sperren oder dessen Zahlen zu markieren; zudem kann die Nachmessung eine andere Last messen.
**Grenze:** Die Rauschformel selbst wurde nicht als fehlend bezeichnet; ihre Kernanbindung und der Geltungsbereich fehlen. Keine neue Rauschmessung ausgeführt.

**B-03: Bereichssperre und Maschinen-Vorbehalt erreichen die Generation nicht**
**Status:** aktuelle_Logik.
**F6:** Z. 162–162, Z. 104–104.
**Code:** `biotop/organe/eichung.py:153–217`; `biotop/lauf.py:147–166`; `biotop/lauf.py:203–212`.
eichung erzeugt toleranz, gesperrt und bei Maschinenserie vorbehalt_zeitraum. generation arbeitet jedoch alle mass.bereiche ab; _generation_koerper hat keinen Filter für gesperrte Bereiche. Die Kalibrierung wird weder geladen noch an aktuelle Messungen gekoppelt. Die detaillierte Deutung steht nur im Rückgabeobjekt; das Protokoll der Rauschmessung speichert aus dem Bereichsobjekt nur eine reduzierte Auswahl ohne serie_zeitraum/serie_deutung/vorbehalt_zeitraum.
Ein gesperrter Bereich kann weiterhin Kandidaten erhalten. Der geforderte eigene Vorbehalt an allen betroffenen Laufzeitmessungen ist nicht automatisch wirksam.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Organ-Meldungen und Sperren liegen in der DB vor; daraus folgt nicht, dass eine produktive Generation die Sperre respektiert hat. Kein solcher positiver Pfadnachweis festgestellt.

### A11 — Eichproben bestehen teilweise aus falschen Gründen; die Normprobe liest das falsche Feld
Zugeordnete Einzelbefunde: A11, B-04, B-05.

**A11: Eichproben bestehen teilweise aus falschen Gründen; die Normprobe liest das falsche Feld**
**Status:** statisch belegt.
**F6:** Z. 103–108, Z. 163–169, Z. 356–359.
**Code:** `biotop/organe/eichproben.py:50–106`; `biotop/organe/eichproben.py:157–215`; `biotop/organe/aegis.py:474–492`.
Nebenwirkung legt nur A lahm: der angekündigte messbare Gewinn in B wird nicht gebaut und nicht geprüft; jeder Ablehnungsgrund mit dem Namen A reicht. Die Normprobe greift auf u.get('masse') zu, obwohl Aegis sein Urteil unter 'mass' hält; der Fallback macht daraus Zuwachs 0 und leeren Testbestand. Sie kann so ohne Normnachweis bestehen. Die Vertragsprobe akzeptiert beliebige Ablehnung. Ihr Eingriff benutzt weiterhin quelle.replace('def ...'), obwohl F6 Textanker ausschließt. Der Vollersetzungs-Diff wird bei großen Dateien schon von der Neuschreibungsregel abgefangen.
Ein grüner Vier-Proben-Bericht beweist die geforderten Wirkmechanismen nicht. Gerade die Normprobe ist durch ihre Defaultwerte entwertet.
**Grenze:** Kein Probe-Kandidat eingeschleust. Nicht alle Proben sind wirkungslos: die Regressionsprobe verlangt ausdrücklich 'Regression je Test' und einen Testnamen.

**B-04: Norm-Eichprobe besteht wegen falschem Rückgabeschlüssel ohne Normnachweis**
**Status:** aktuelle_Logik.
**F6:** Z. 90–90, Z. 108–108, Z. 169–169, Z. 197–197.
**Code:** `biotop/organe/eichproben.py:115–124`; `biotop/organe/eichproben.py:157–169`; `biotop/organe/eichproben.py:185–191`; `biotop/organe/aegis.py:474–482`.
Die Prüflambda liest u[masse], Aegis liefert aber u[mass]. Damit werden Zuwachs und Testbestand durch leere Defaults ersetzt: int(... or 0)==0 und Datei nicht in [] sind unabhängig vom tatsächlichen Anklägerurteil wahr. Zusätzlich importiert die Probe ein erst im Kandidaten angelegtes Modul; sie erzeugt am Ausgang einen Import-/Sammlungsfehler und nicht sicher eine gerichtete Assertion. Der offene Normeintrag und der echte Werkbestand werden nicht geprüft.
Grün für Norm ist hier eine Scheinaussage; ein falscher oder gar nicht erreichter Normpfad kann die Vorbedingung passieren.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Historisch konkret: #12538 (Lauf 22, K2083, 2026-09-19T20:59:09.321Z) bestanden=true, norm=[], zuwachs=None; wirklicher Grund: Pareto verletzt: preise.tote_funktionen: 0 → 1. Gleichartig #12440/#12465. #12418 war sogar bereits an einer Verfassungsvorprüfung gescheitert und meldete dennoch bestanden=true.

**B-05: Weitere Eichproben prüfen Ersatzgegenstände oder falsche Ablehnungsgründe**
**Status:** aktuelle_Logik.
**F6:** Z. 108–108, Z. 169–169, Z. 203–203.
**Code:** `biotop/organe/eichproben.py:157–177`; `biotop/organe/eichproben.py:193–215`.
Nebenwirkung wird als B schneller/A kaputt kommentiert, aber tatsächlich wird nur A lahmgelegt; die Bedingung verlangt lediglich Ablehnung und A als Text im Grund. Vertrag wird direkt durch aegis.pruefen geprüft, nicht durch Nexus-Verhandlung; jedes Nicht-ueberlebt genügt. Die Konsumentenergänzung wird trotz AST-Auswahl per quelle.replace("def <name>",...) eingefügt und nur als zusätzliche Funktion definiert, ohne deren Benutzung sicherzustellen.
Diese Proben beweisen weder den Bereichstausch noch den vollständigen Vertrags-Nachbarpfad; syntaktische/anderweitige Ablehnungen können die Torzeile fälschlich grün machen.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Vier Eichprobenabschlüsse und Einzelurteile sind historisch vorhanden; eine solche Ausgabe ist kein Ersatz für die in F6 geforderten Gründe. Kein neuer Probelauf durchgeführt.

### A12 — Eichgegenstand kann trotz unbrauchbarer Pfadangabe auf einen Nebenvertrag ausweichen
Zugeordnete Einzelbefunde: A12, B-25.

**A12: Eichgegenstand kann trotz unbrauchbarer Pfadangabe auf einen Nebenvertrag ausweichen**
**Status:** statisch belegt.
**F6:** Z. 108–108, Z. 167–169, Z. 394–396.
**Code:** `biotop/organe/eichgegenstand.py:34–80`; `biotop/organe/eichgegenstand.py:105–159`; `biotop/organe/eichgegenstand.py:160–199`.
Eine nichtleere tragender_pfad-Liste gilt sofort als ausdrückliche Angabe, auch wenn kein angegebenes Paar zu den vorhandenen Verträgen passt. Dann erhalten alle echten Paare Gewicht 0 und die Vertragsgröße entscheidet trotzdem. Ein vorhandenes Siegel wird allein am Fortbestehen und Hash der Vertragsdatei erkannt; Existenz der beiden Bereiche und Gültigkeit des tragenden Pfads werden vor dem Frühreturn nicht neu geprüft. Bei Hashwechsel wird der alte Hash nur verkürzt in Befund/Protokolltext getragen.
Bei Betriebszwecken kann eine formal vorhandene, aber sachlich wirkungslose Angabe das verlangte Warten umgehen; das Siegel bestätigt eine Datei, nicht den weiter bestehenden tragenden Pfad.
**Grenze:** Der Normalfall ganz fehlender Regeln wird korrekt mit wartet=True abgewiesen. Kein versiegelter Gegenstand in der Datenbank verändert.

**B-25: Eichgegenstand prüft bei Wiederverwendung nur die Vertragsdatei**
**Status:** aktuelle_Logik.
**F6:** Z. 90–90, Z. 108–108, Z. 167–167.
**Code:** `biotop/organe/eichgegenstand.py:65–95`; `biotop/organe/eichgegenstand.py:111–125`; `biotop/organe/eichgegenstand.py:149–171`.
Bei vorhandenem Siegel reichen Existenz und unveränderte Prüfsumme der Vertragsdatei für geprueft=unveraendert. Ob die Bereiche noch existieren, das Paar noch zur DB-Vertragsmenge gehört oder der tragende Pfad der aktuellen Verfassung weiterhin passt, wird nicht geprüft. Beim ersten Siegel kann ein ausdrücklich gesetzter, aber in paare nicht vorhandener tragender Pfad außerdem auf Vertragsgröße zurückfallen. Bei vollständig fehlender Verfassung liefert _tragende_paare keinen FEHLT_AUSDRUECKLICH-Stop.
Die ausdrückliche tragender_pfad-Sperre für normale Werke ist vorhanden, ihre Umgehungsfälle lassen aber einen ungeeigneten/weggefallenen Gegenstand als versiegelt weiterleben. Ein unveränderter Datei-Hash ist nicht der ganze Gegenstand.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** 16 Versiegelungsereignisse, drei Wegfallereignisse und ein Wartesignal liegen historisch vor; die Tabelle enthält zwei aktive Siegel für reale Prüfwerke. Kein neuer Siegel-/Wegfallversuch vorgenommen.

### A13 — Eichproben hinterlassen lernwirksame Ansagen und Immunfunde im geprüften Bestand
Zugeordnete Einzelbefunde: A13, B-06.

**A13: Eichproben hinterlassen lernwirksame Ansagen und Immunfunde im geprüften Bestand**
**Status:** statisch belegt.
**F6:** Z. 106–106, Z. 219–219.
**Code:** `biotop/organe/eichproben.py:128–138`; `biotop/organe/eichproben.py:157–171`; `biotop/organe/eichproben.py:217–224`; `biotop/organe/aegis.py:302–331`; `biotop/organe/aegis.py:394–407`; `biotop/organe/aegis.py:626–668`; `biotop/organe/gedaechtnis.py:123–166`; `biotop/organe/gedaechtnis.py:285–294`; `biotop/organe/gedaechtnis.py:427–437`; `pruefung/vorspann.py:28–56`.
Die Proben setzen ist_probe=1 und die drei Gedächtnis-Eintrittsstellen beachten das. Der unmittelbar benutzte Aegis-Pfad übernimmt dieses Merkmal aber nicht in seine Ansage-/Immunaufnahme. Ansagen und ggf. neue Fund-/Normzeilen werden unter echter lauf_id/werk_id geschrieben; bisherige_behauptungen liest sie später ohne Probenausschluss. Weder proben noch vorspann stellen diesen Bestand nach jeder Probe wieder her. Fund-Neubewertung erfolgt sogar vor den Proben.
Die Prüfung verändert den Vorrat, gegen den nächste Proben und spätere Angriffe entscheiden. Die enge Probensperre der drei Gedächtnisse behebt diese zusätzliche Kontamination nicht.
**Grenze:** Dass eine konkrete Probe tatsächlich einen neuen Immunfund erzeugte, wurde nicht nachgemessen. Der Ansageschreibpfad und fehlende Rücknahme sind belegt.

**B-06: Proben werden aus drei Gedächtnissen gefiltert, nicht aus allen wirksamen Prüfbeständen**
**Status:** aktuelle_Logik.
**F6:** Z. 106–106, Z. 219–219.
**Code:** `biotop/organe/eichproben.py:128–138`; `biotop/organe/eichproben.py:157–223`; `biotop/organe/aegis.py:631–668`; `biotop/organe/aegis.py:302–331`; `pruefung/lauf25_pfadnachweis.py:79–102`; `pruefung/nachgang_n13_n14.py:103–121`.
Die Probenerzeuger setzen ist_probe, Aegis schreibt neue Fund-/Normtests und Ansagen aber ohne entsprechende Bereichsisolierung in den normalen Immunsystem-/Protokollvorrat. Die drei Gedächtnis-Eintrittsstellen schützen ihre Tabellen, nicht die Aegis-Aufnahmestellen. Eichproben räumen diese Nebenwirkungen nicht in finally zurück. Wiederaufnahmen aus anderen Werken kopieren solche Funde ebenfalls.
Prüfmaterial kann spätere Kandidaten messen, Angriffe sperren oder über Werk-Kopien weiterwandern, auch wenn die drei Gedächtnistabellen inzwischen sauber sind.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** DB-Join findet 21 noch vorhandene Immunsystem-Einträge mit direkt zuordenbarem ist_probe=1-Kandidaten. Für Lauf 22 stehen z.B. IDs 285–287 (norm_k2081_bericht, aegis_k2082_bericht, norm_k2082_bericht) weiterhin im Bestand. Die drei eigentlichen Gedächtnistabellen haben in der getrennten direkten Probe-Zuordnung keine Treffer. C-Pfadproben #16010–16030 sind ausdrücklich gestellte Fälle, nicht natürlicher Schwarmbetrieb.

### A14 — Fund-Neubewertung verwechselt Fehlermeldungen mit Abstürzen im Werk und konserviert unbelegte Funde
Zugeordnete Einzelbefunde: A14, B-07, B-08.

**A14: Fund-Neubewertung verwechselt Fehlermeldungen mit Abstürzen im Werk und konserviert unbelegte Funde**
**Status:** statisch belegt.
**F6:** Z. 103–103, Z. 107–107, Z. 164–164, Z. 197–197, Z. 222–222.
**Code:** `biotop/organe/fundpruefung.py:26–43`; `biotop/organe/fundpruefung.py:46–90`; `biotop/organe/aegis.py:75–106`; `biotop/organe/aegis.py:589–608`.
_ausfuehren beurteilt 'besteht' durch Textfragmente und 'absturz_im_werk' durch Error/Exception ohne AssertionError; Paketpfad, Traceback-Ort und Returncode gehen nicht in den Absturzbeleg ein. Ein Import- oder testinterner Fehler kann dadurch wie ein Werkabsturz wirken. Anders als der Aegis-JUnit-Pfad wird nicht dieselbe Ortsableitung verwendet. Ein fallender Altbestand mit status='offen', ohne Absturz und ohne Bezug bleibt im else erneut offen statt offen_norm. Das optionale bereiche-Argument begrenzt den Scan nicht.
Die Neubewertung kann gerade die Norm-/Infrastrukturfehler zu Funden machen oder als solche erhalten, die F6 mechanisch ausschließen wollte.
**Grenze:** Keine vorhandenen Funde ausgeführt oder umklassifiziert. Der gemeinsame Vertragsverweis-Helper ist korrekt wiederverwendet; die Absturzableitung dagegen nicht.

**B-07: Fund-Neubewertung konserviert unbegründete offene Funde**
**Status:** aktuelle_Logik.
**F6:** Z. 103–103, Z. 107–107, Z. 222–222.
**Code:** `biotop/organe/fundpruefung.py:55–77`.
Für einen am neuen Ausgang fallenden Test ohne Werkabsturz und ohne gültigen Verweis übernimmt Zeile 74 bei bisherigem status=offen wieder offen. F6 Zeile 222 verlangt in genau diesem Fall Norm. Das Vermeiden der früheren Norm→Fund-Beförderung ist eine sinnvolle Korrektur, die neue Logik korrigiert aber einen bereits falsch offenen Fund nicht.
Eine alte Fehlklassifikation wird trotz mechanischer Nachmessung in den neuen Testbestand übernommen und kann echte Behebungen blockieren.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Die historischen Neubewertungen sind belegt (#12472, #12473, #14477, #15273). Die #12472-Ausgabe mit Norm→offen ist ein früherer Stand, NICHT die heutige Zeile 74: der aktuelle Stand konserviert und befördert Normtests ohne Nachweis nicht. Aus dem reduzierten Protokoll ist die Zahl heutiger offener Fälle ohne Nachweis nicht sicher ableitbar.

**B-08: Neubewertung prüft Absturz und Erfolg anders als Aegis**
**Status:** aktuelle_Logik.
**F6:** Z. 103–103, Z. 107–107, Z. 108–108, Z. 222–222.
**Code:** `biotop/organe/fundpruefung.py:34–43`; `biotop/organe/fundpruefung.py:55–77`; `biotop/organe/aegis.py:75–107`; `biotop/organe/aegis.py:591–605`.
Das neue Organ teilt zwar _nennt_vertrag mit Aegis, bestimmt besteht/Absturz aber durch Substrings in stdout+stderr für die gesamte Testdatei. Es prüft weder Returncode noch JUnit-Fehlerort im Werk. Ein ImportError oder Test-eigener TypeError kann als Werkabsturz zählen; ein AssertionError irgendwo kann umgekehrt einen zusätzlichen Werkabsturz verdecken. Mehrere Tests pro Datei erhalten gemeinsam einen Status und any(Verweis) reicht für die ganze Datei.
Nachrechnung und geprüftes Organ besitzen weiterhin unterschiedliche Ableitungen; ein unbrauchbarer Test kann als Fund weitergeführt werden. Ein geteiltes Verweis-Prädikat allein erfüllt 2a5 nicht vollständig.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Gelesen, nicht ausgeführt; kein einzelner Fehlfall aus dem DB-Protokoll zugeordnet.

### A15 — Mutantenfang zählt jeden Prozessfehler und kann ohne gültigen Gegenstand bestehen
Zugeordnete Einzelbefunde: A15.

**A15: Mutantenfang zählt jeden Prozessfehler und kann ohne gültigen Gegenstand bestehen**
**Status:** statisch belegt.
**F6:** Z. 90–90, Z. 103–103, Z. 171–173.
**Code:** `biotop/organe/generation0.py:108–113`; `biotop/organe/generation0.py:180–200`; `biotop/organe/generation0.py:243–256`; `biotop/lauf.py:557–616`; `biotop/__main__.py:53–53`.
_testlauf verwendet ausschließlich e.rc != 0 als gefangen; es unterscheidet weder echte mutantenspezifische Testabweichung, bereits roten Ausgang, keine Tests, Importfehler noch Docker-Fehler. Der Testbau verwendet für faengt denselben RC-Kurzschluss. generation0 erzwingt keinen vorher grünen unmutierten Bestand und keine positive Zahl nichtäquivalenter Mutanten. Bei leerer Mutantenliste wird das Anteilziel zu 0 und erreicht ist wahr. Das frei wählbare --ziel hat zudem keine Mindestgrenze aus F6.
Eine hohe Fangquote kann Infrastruktur- oder Basisfehler zählen; eine Prüfung ohne Mutanten kann als erreicht zurückgegeben werden.
**Grenze:** Keine Quote neu gemessen und keine leere Probe ausgeführt. Die beschriebenen Bedingungen folgen aus dem Kontrollfluss.

### A16 — Äquivalenz ist Rastergleichheit ohne Codebegründung; fehlende Beobachtung wird durch einen Regexfehler gleichgesetzt
Zugeordnete Einzelbefunde: A16.

**A16: Äquivalenz ist Rastergleichheit ohne Codebegründung; fehlende Beobachtung wird durch einen Regexfehler gleichgesetzt**
**Status:** statisch belegt.
**F6:** Z. 90–90, Z. 108–108, Z. 172–172.
**Code:** `biotop/organe/generation0.py:116–176`.
Das Beobachtungsskript meldet bei fehlendem beobachten() 'AEQ keine-beobachtung' und beendet sich erfolgreich. Der Regex AEQ (\w+) liest davon nur 'keine'; die spätere Gleichheitsprüfung auf 'keine-beobachtung' kann deshalb nie greifen. Ein vom Testlauf nicht gefangener Mutant kann dann aufgrund zweimal 'keine' als äquivalent aussortiert werden. Auch mit echter Beobachtung wird eine bloße Hashgleichheit auf dem Raster plus grünen Tests zur Äquivalenz erklärt; die 'Codebegründung' wiederholt nur Mutationsbeschreibung/Ort und untersucht keine Verhaltensäquivalenz.
Blinde Flecken können vor der Quote aus dem Nenner verschwinden, obwohl der geforderte Äquivalenzbeleg fehlt.
**Grenze:** Die beiden mitgelieferten Referenzlasten besitzen beobachten(); der Regexfehler betrifft den unterstützten Fallbackpfad und ist kein Nachweis, dass bestehende Mutanten dort falsch aussortiert wurden.

### A17 — Testmessung und Pareto verlieren Identitäten, Skips und Fehler hinter dem Abschneidelimit
Zugeordnete Einzelbefunde: A17.

**A17: Testmessung und Pareto verlieren Identitäten, Skips und Fehler hinter dem Abschneidelimit**
**Status:** statisch belegt.
**F6:** Z. 90–90, Z. 108–108, Z. 150–152.
**Code:** `biotop/kern/messgeraet.py:66–95`; `biotop/kern/messgeraet.py:129–140`; `biotop/kern/messgeraet.py:196–216`; `biotop/kern/messgeraet.py:277–297`.
Testzuordnung erfolgt über Dateinamenskonventionen. Als Dateiname wird das letzte classname-Segment benutzt; bei Klassen-Tests ist das häufig der Klassenname statt der Testdatei. Nicht zugeordnete Ergebnisse landen unter None und werden keinem Bereich zugerechnet. <skipped> wird wie bestanden behandelt. pytest_rc und ein leerer Testbestand machen eine vorhandene Messausgabe nicht ungültig. tests_fehlgeschlagen_liste wird auf die ersten 100 Einträge gekürzt; Pareto je Test bildet danach nur die Differenz dieser gekürzten Listen.
Kernmaß und Regressionsentscheidung sind bei fremden Testlayouts bzw. großen roten Beständen nicht vollständig. Ein neuer Fehlschlag jenseits des gespeicherten Ausschnitts kann dem Einzeltest-Pareto fehlen.
**Grenze:** Keine konkrete Regression in einem angenommenen Lauf behauptet. Die F6-Regel 'je Test' ist vorhanden, aber ihr Eingang ist nicht verlustfrei.

### A18 — Fehlgeschlagene Sicherheits- und Totcodeanalyse kann als Nullbefund in gültige Messungen eingehen
Zugeordnete Einzelbefunde: A18.

**A18: Fehlgeschlagene Sicherheits- und Totcodeanalyse kann als Nullbefund in gültige Messungen eingehen**
**Status:** statisch belegt.
**F6:** Z. 90–90, Z. 150–152, Z. 157–157, Z. 320–320.
**Code:** `biotop/kern/messgeraet.py:97–140`; `biotop/kern/messgeraet.py:208–216`; `biotop/kern/messgeraet.py:265–289`.
Wenn Bandits Ausgabe nicht als JSON parsebar ist, liefert bandit() 0 Punkte, leere Befunde und einen Fehlertext. Rückgabecode und JSON-Fehlerliste bestimmen die Messgültigkeit nicht. vulture() ignoriert ebenfalls rc/stderr und zählt lediglich passende stdout-Zeilen. Der übergeordnete Pfad setzt gueltig=True, sobald ein Messmarker vorhanden ist; die Fehlerfelder werden von Kernmaß und Pareto nicht ausgewertet. Eine eigenständige Abhängigkeitsprüfung ist im Messskript nicht implementiert.
Werkzeugausfall kann wie das Verschwinden eines Befundes oder toten Codes aussehen und dadurch das harte Maß verbessern.
**Grenze:** Keine Scannerinstallation geändert und kein Ausfall erzeugt. Die Fehlerpfade selbst sind der Beleg.

### A19 — Speichergrenzmaß und konfigurierbares Klassenmaß fehlen im tatsächlichen Mess-/Auswahlpfad
Zugeordnete Einzelbefunde: A19.

**A19: Speichergrenzmaß und konfigurierbares Klassenmaß fehlen im tatsächlichen Mess-/Auswahlpfad**
**Status:** statisch belegt.
**F6:** Z. 153–156, Z. 397–406.
**Code:** `biotop/kern/messgeraet.py:39–44`; `biotop/kern/messgeraet.py:129–166`; `biotop/kern/messgeraet.py:265–274`; `biotop/kern/messgeraet.py:378–445`; `biotop/lauf.py:93–106`; `biotop/organe/kammer.py:23–25`; `biotop/organe/kammer.py:63–73`.
Die Messwertschema-/Bestwert-/Grenzlisten enthalten keinen Speicherverbrauch; Docker setzt nur ein absolutes Kammerlimit. kernmass_f2_bereich ist fest auf Fehlschläge, Sicherheit und Totcode verdrahtet. mass_einfrieren liest aus den Werkregeln nur Tauschparameter für seine Maßdefinition, keinen Klassenmaß-Adapter. Ein Ertrags-/Verlustmaß aus der Verfassung würde nicht an der Auswahl teilnehmen.
Speicherzunahmen unterhalb des Containerlimits bleiben ungemessen; die in F6 vorgesehene Werkklassen-Erweiterung und das Handels-Kernmaß sind im heutigen Kern nicht anschließbar.
**Grenze:** Keine Aussage, Phase 4 sei bereits freigegeben oder gestartet. Dies ist eine noch nicht gebaute F6-Fähigkeit, nicht der Nachweis eines misslungenen Handelslaufs.

### A20 — Unmessbare Laufzeit wird übersprungen; die Geschwindigkeitsannahme verwendet weiter eine feste Schwelle
Zugeordnete Einzelbefunde: A20.

**A20: Unmessbare Laufzeit wird übersprungen; die Geschwindigkeitsannahme verwendet weiter eine feste Schwelle**
**Status:** statisch belegt.
**F6:** Z. 90–90, Z. 153–155, Z. 161–162.
**Code:** `biotop/kern/messgeraet.py:143–166`; `biotop/kern/messgeraet.py:208–216`; `biotop/kern/messgeraet.py:419–433`; `biotop/kern/messgeraet.py:464–478`; `biotop/lauf.py:298–303`.
Eine fehlende last_<bereich>-Funktion oder eine Ausnahme in der Last ergibt None, aber keine ungültige Gesamtmessung. grenzen_f2 prüft Laufzeit nur, wenn Ausgang und Kandidat beide truthy sind; None und 0 umgehen diesen Teil. Die schnelle Nische und die Generalprobe verlangen unabhängig von gemessener Bereichsstreuung den Faktor 0.85 für einen Gewinn. Damit kann eine defekte oder stark rauschende Laufzeit ihren Grenz-/Gewinnmaßcharakter verlieren.
Der vorhandene Referenzlast-Dateiname genügt, obwohl einzelne Bereichslasten fehlen/abstürzen können; messbare Verschlechterung und unmessbares Ergebnis werden nicht gleich streng behandelt.
**Grenze:** Kein neuer Lastlauf; vorhandene Funktion im Ausgang wird nicht als Gewähr für die Last am Kandidaten gewertet.

### A21 — Sicherheitsgewinn wird auch ohne verpflichtenden Umgehungs-Immuntest anerkannt
Zugeordnete Einzelbefunde: A21.

**A21: Sicherheitsgewinn wird auch ohne verpflichtenden Umgehungs-Immuntest anerkannt**
**Status:** statisch belegt.
**F6:** Z. 150–157, Z. 192–192.
**Code:** `biotop/organe/aegis.py:161–175`; `biotop/kern/befundklassen.py:14–74`; `biotop/organe/aegis.py:678–699`; `biotop/kern/messgeraet.py:265–289`; `biotop/kern/messgeraet.py:448–457`.
Befundklassen-Tests werden nur gebaut, wenn die Verfassung einen Einstieg kennt und der Katalog Code liefert. Bei fehlendem Einstieg oder unbekannter/umgehungsloser Klasse wird still continue/None verwendet. Die spätere Auswahl bewertet dennoch jede Verringerung von sicherheit_punkte als Kernmaßgewinn und Tauschberechtigung; es gibt keine Kopplung 'verschwundener Befund -> bestandener und aufgenommener Klassen-Immuntest'. Bekannte Klassen sind nur ein begrenzter Katalog.
Die harte Bedingung 'behoben heißt verschwunden UND Umgehung im Werk' ist nicht für alle Sicherheitsbefunde durchgesetzt.
**Grenze:** Bei konfigurierten Einstiegen kann der vorgesehene Schutz wirken. Ein bestimmter historisch angenommener Sicherheitsfix wurde hier nicht erneut ausgeführt.

### A22 — Budgetvorprüfung ist keine obere Kostengrenze und reserviert keine parallelen Aufrufe
Zugeordnete Einzelbefunde: A22.

**A22: Budgetvorprüfung ist keine obere Kostengrenze und reserviert keine parallelen Aufrufe**
**Status:** nur Risiko.
**F6:** Z. 92–92, Z. 241–242.
**Code:** `biotop/anbieter/__init__.py:48–49`; `biotop/anbieter/__init__.py:113–136`; `biotop/kern/kasse.py:88–136`; `biotop/kern/kasse.py:180–199`.
Eingabetoken werden aus len(system+nutzer)//3 geschätzt, ohne modellgenauen Tokenizer oder Protokolloverhead. Die Vorprüfung liest bereits gebuchte Kosten; vor dem Netzaufruf wird keine atomare Kostenreservierung geschrieben. Zwei unabhängige Prozesse könnten denselben Restbetrag sehen. Generation_vorpruefung benutzt nur die teuerste abgeschlossene Generation, bei fehlender Historie 0.
Ein realer Aufruf kann teurer sein als die Schätzung; gleichzeitige Aufrufe können zusammen den freigegebenen Rest überschreiten. Das harte 'nie danach' ist durch diese Schätzung nicht garantiert.
**Grenze:** Kein Tokenvergleich, kein Parallelversuch und keine Überschreitung gemessen. Daher ausdrücklich Risiko statt behaupteter tatsächlicher Budgetverletzung.

### A23 — Fehlende Nutzungsdaten werden als Nullkosten gebucht; fehlgeschlagene Aufrufe fehlen im Kassenzähler
Zugeordnete Einzelbefunde: A23.

**A23: Fehlende Nutzungsdaten werden als Nullkosten gebucht; fehlgeschlagene Aufrufe fehlen im Kassenzähler**
**Status:** statisch belegt.
**F6:** Z. 90–92, Z. 241–242.
**Code:** `biotop/anbieter/__init__.py:87–98`; `biotop/anbieter/__init__.py:126–136`; `biotop/kern/kasse.py:69–85`; `biotop/kern/kasse.py:124–136`.
Fehlt usage oder ein Tokenfeld, setzt der Adapter prompt_tokens/completion_tokens auf 0. Diese Werte werden ohne Kennzeichnung als fehlende Daten regulär gebucht. Bei AnbieterFehler wird nur modell.fehler protokolliert und vor kasse.buchen abgebrochen; COUNT(*) aus kasse bedeutet daher erfolgreiche Buchungen, nicht alle versuchten Modellaufrufe. Es existiert kein eigener ungeklärter Abrechnungsposten für einen nach Versand abgebrochenen Aufruf.
Kostenstand und Aufrufzahl können unterzählen; '0' ist hier unter Umständen eine Defaultzahl statt gemessener Verbrauch.
**Grenze:** Keine reale Providerrechnung abgeglichen. Ob ein bestimmter fehlgeschlagener Aufruf kostenpflichtig war, bleibt offen.

### A24 — Anbieterschicht ist OpenRouter-only; eigene Kontingentgrenze und ausschließliche Server-Umgebung fehlen
Zugeordnete Einzelbefunde: A24.

**A24: Anbieterschicht ist OpenRouter-only; eigene Kontingentgrenze und ausschließliche Server-Umgebung fehlen**
**Status:** statisch belegt.
**F6:** Z. 242–242, Z. 287–290, Z. 312–312, Z. 322–322.
**Code:** `biotop/anbieter/__init__.py:36–45`; `biotop/anbieter/__init__.py:101–120`; `biotop/kern/kasse.py:33–35`; `biotop/kern/kasse.py:69–85`; `biotop/kern/kasse.py:88–135`; `biotop/organe/mentor.py:24–24`; `biotop/organe/jury.py:19–19`.
adapter() akzeptiert nur openrouter; eine zweite Adapterimplementierung oder ein Port für Aboanbieter existiert hier nicht. kontingent ist nur ein optionaler Buchungsmarker, aber kein in vorpruefung geprüftes eigenes Limit; aufrufen reicht den Marker nie weiter. Mentor benutzt ebenfalls tokenabgerechnetes OpenRouter, die Jury Schnellmodelle. _schluessel liest bei fehlender Umgebungsvariable ausdrücklich /root/.hermes/.env statt ausschließlich Servervariablen zu verlangen.
Mehrere Modellhersteller sind vorhanden, aber nicht die in F6 zugesagte austauschbare Mehradapter-/Kontingentarchitektur. Die Geheimnisquelle greift auf Hermes-Dateikonfiguration zurück.
**Grenze:** Keine .env-Datei gelesen, kein Schlüssel ausgegeben, kein Katalog abgefragt. Kasse Z.33–35 nennt selbst eine spätere/spezifische Philipp-Vorgabe zum Träger; deren tatsächliche Autorisierung wurde nicht unabhängig geprüft. Als F6-Abweichung, nicht als bewiesener Ungehorsam von Hermes, eingeordnet.

**Eigenanteil Hermes:** Direkter, belegter Kopplungspfad an Hermes: _schluessel mit Dateifallback. Keine Spekulation über aktive Hermes-Modelle oder aktuelle Anbieterpreise.

### A25 — Eichkosten: Kammerläufe werden konstant behauptet; dieselben Modellkosten bleiben in der Laufsumme
Zugeordnete Einzelbefunde: A25.

**A25: Eichkosten: Kammerläufe werden konstant behauptet; dieselben Modellkosten bleiben in der Laufsumme**
**Status:** statisch belegt.
**F6:** Z. 110–110, Z. 165–165, Z. 426–426.
**Code:** `biotop/organe/eichproben.py:157–169`; `biotop/organe/aegis.py:531–533`; `biotop/organe/aegis.py:575–578`; `biotop/organe/aegis.py:672–678`; `biotop/organe/eichung.py:49–87`; `biotop/organe/eichung.py:90–108`; `biotop/kern/kasse.py:69–85`; `biotop/kern/kasse.py:139–158`.
lauf_probe setzt kammerlaeufe fest auf 1 und bucht genau 1, unabhängig davon, ob Aegis früh abbricht oder Basis/Kandidat und Zusatztests jeweils eigene Kammern aufruft. Modellkosten werden dagegen korrekt als Kassenstanddifferenz erfasst. kosten_buchen legt eine zweite eichkosten-Zeile an, entfernt/markiert aber die ursprüngliche kasse-Buchung nicht. stand und bericht_md summieren weiterhin alle kasse-Zeilen des Laufs, während kosten_text behauptet, Eichkosten seien nicht enthalten.
Die behauptete Zahl der Kammerläufe ist keine Messung; reine Laufsumme und Eichsumme sind ohne Abzug nicht getrennt. Ein Vergleich historischer Vorspannkosten darf diese Zahlen nicht ungeprüft übernehmen.
**Grenze:** Keine tatsächliche Zahl je historischem Probenlauf neu bestimmt. Die statische Konstante und widersprüchlichen Summenpfade sind nachgewiesen.

### A26 — Unantastbarer Kern und unveränderliches Protokoll sind nicht technisch getrennt
Zugeordnete Einzelbefunde: A26.

**A26: Unantastbarer Kern und unveränderliches Protokoll sind nicht technisch getrennt**
**Status:** statisch belegt.
**F6:** Z. 270–279.
**Code:** `biotop/kern/datenbank.py:1–5`; `biotop/kern/datenbank.py:18–82`; `biotop/kern/protokoll.py:19–46`; `biotop/lauf.py:13–15`; `biotop/organe/genesis.py:137–141`; `biotop/dienst.py:233–237`.
Kern, Schwarm, Dienst und Organe verwenden dieselbe SQLite-Verbindung bzw. dieselbe Datei im selben Import-/Prozessmodell. Die Datenbankschicht besitzt keine exklusive Kernrolle und keine Append-only-Trigger für das Protokoll. Die Hashkette schützt nur gegen unbegleitete Einzeländerung; ein Besitzer des Schreibrechts kann Zeilen/Kette neu schreiben oder am Ende entfernen, ohne externen Anker. Die eigene Modulbeschreibung bezeichnet die Rollentrennung als offen. Zudem wird die später benötigte ist_probe-Spalte nur im CREATE definiert; die Migration ergänzt allein vertraege.
Das F6-Schutzmodell 'eigener Prozess, eigene Rolle, kein Schreibpfad' ist nicht implementiert. Die vorhandene Hashprüfung ist ein Nachweismechanismus, keine Unveränderlichkeit.
**Grenze:** Weder Datenbank noch Protokoll geändert, keine Dienstrechte live erhoben. Das Migrationsproblem betrifft ältere Schemas; die gesicherte aktuelle DB wurde nicht als spaltenlos behauptet.

### A27 — Fremdcode kann innerhalb der Kammer Messskripte/Belege beeinflussen; Messausgabe ist nicht vertrauensgetrennt
Zugeordnete Einzelbefunde: A27.

**A27: Fremdcode kann innerhalb der Kammer Messskripte/Belege beeinflussen; Messausgabe ist nicht vertrauensgetrennt**
**Status:** nur Risiko.
**F6:** Z. 85–85, Z. 173–173, Z. 237–238, Z. 270–279.
**Code:** `biotop/organe/kammer.py:54–80`; `biotop/kern/messgeraet.py:79–85`; `biotop/kern/messgeraet.py:143–166`; `biotop/kern/messgeraet.py:196–216`; `biotop/organe/aegis.py:79–102`.
Die kopierten _messgeraet-Dateien werden zusammen mit dem Werk an UID 10001 übereignet und als ein rw-Verzeichnis eingebunden. Werkcode läuft in pytest-Subprozessen und bei Referenzlasten im selben Python-Prozess wie die Auswertelogik; Ergebnisse kommen aus beschreibbarer JUnit-Datei bzw. stdout-Markern. messen akzeptiert einen Marker ohne verifizierten Erzeuger und prüft e.rc bei vorhandenem Marker nicht. Keine getrennte schreibgeschützte Messgerätablage und kein authentischer Ergebnisübergang schützen diese Grenze.
Ein bewusst manipulierender Kandidat könnte Prüfwerkzeuge oder Ergebnisartefakte statt seiner Qualität verändern. Containerisolation allein garantiert nicht, dass die Messung unabhängig vom zu prüfenden Werk ist.
**Grenze:** Keine Ergebnisfälschung ausgeführt; deshalb Risiko. Positiv: Netzwerk, Ressourcen, Benutzer, Root-Dateisystem und Capabilities sind im Dockeraufruf tatsächlich begrenzt.

### A28 — Abbruch markiert die Datenbank, hält einen bereits laufenden Generationsprozess aber nicht vor dem nächsten Aufruf an
Zugeordnete Einzelbefunde: A28.

**A28: Abbruch markiert die Datenbank, hält einen bereits laufenden Generationsprozess aber nicht vor dem nächsten Aufruf an**
**Status:** statisch belegt.
**F6:** Z. 86–86, Z. 92–92, Z. 104–104, Z. 281–281.
**Code:** `biotop/lauf.py:133–170`; `biotop/lauf.py:175–181`; `biotop/lauf.py:359–393`; `biotop/anbieter/__init__.py:113–131`; `biotop/kern/kasse.py:88–121`.
abbrechen ändert Lauf-/Generationsstatus und protokolliert, sendet jedoch kein Stoppsignal. generation prüft den Status nur am Einstieg; ihr laufender Körper und die Anbieter-Vorprüfung lesen später kein Abbruchmerkmal. Ein anderer Prozess kann weiter aufrufen und mit abschluss sogar erneut bereit setzen. Ein bereits beendeter Lauf kehrt in abbrechen vor protokoll.schreiben zurück, obwohl die Rückgabe 'trotzdem protokolliert' sagt; ein nach Budget beendeter Lauf lässt sich dort auch nicht nachträglich als Satz-2-verworfen markieren.
Der benannte Befehl ist vorhanden, die Pflicht zum wirksamen Stoppen vor weiteren Modellaufrufen ist im nebenläufigen Betrieb nicht durchgesetzt.
**Grenze:** Kein laufender Prozess gestoppt und keine Nebenläufigkeit erzeugt. Der fehlende erneute Zustandscheck ist belegt; ein konkreter Weiterlauf wurde nicht gemessen.

### A29 — HTTP-Abbruchroute ruft eine nicht existierende Methode auf
Zugeordnete Einzelbefunde: A29, B-21.

**A29: HTTP-Abbruchroute ruft eine nicht existierende Methode auf**
**Status:** statisch belegt.
**F6:** Z. 104–104, Z. 246–246, Z. 281–281.
**Code:** `biotop/dienst.py:81–112`; `biotop/dienst.py:233–237`; `biotop/oberflaeche.py:11–31`.
do_POST liest den Body bereits mit _json_body. Im Abbruchzweig ruft es danach self._json() auf, obwohl Handler nur _json_body definiert und BaseHTTPRequestHandler diese Biotop-Methode nicht anbietet. Der Aufruf liegt vor dem try/except, daher wird L.abbrechen nicht erreicht. Ein Abbruch-Bedienelement ist auch nicht in ELEMENTE verdrahtet.
Die registrierte und beworbene HTTP-Abbruchroute ist im gelesenen Code defekt; der CLI-Befehl bleibt davon unberührt.
**Grenze:** Kein HTTP-Aufruf ausgeführt. Statischer Methoden-/Kontrollflussbeleg, keine erfundene HTTP-Statusausgabe.

**B-21: Web-Abbruch ruft eine nicht existierende Methode auf**
**Status:** aktuelle_Logik.
**F6:** Z. 104–104, Z. 94–94, Z. 246–246.
**Code:** `biotop/dienst.py:81–112`; `biotop/__main__.py:42–43`; `biotop/__main__.py:80–81`.
POST /laeufe/<id>/abbrechen liest den JSON-Body bereits in Zeile 100, ruft dann vor dem try nochmals self._json() auf. Die Klasse definiert _json_body, aber keine _json. Der benannte Endpunkt scheitert deshalb vor L.abbrechen. Der CLI-Befehl abbrechen ist demgegenüber tatsächlich vorhanden und angebunden.
Eine Pflicht ist zwar über CLI erreichbar, ihr gebauter HTTP-Pfad ist aber nicht funktionsfähig. Eine reine Route-ohne-Token-Prüfung würde den Fehler nicht erreichen.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Statischer Befund; kein HTTP-Aufruf und kein laufender Dienst in dieser Prüfung. Vorhandene lauf.abgebrochen-Ereignisse beweisen nicht diesen HTTP-Pfad.

### A30 — Lazarus überschreibt vorhandene Schnappschüsse; Annahme ist nicht ausfallsicher mit Archivierung gekoppelt
Zugeordnete Einzelbefunde: A30.

**A30: Lazarus überschreibt vorhandene Schnappschüsse; Annahme ist nicht ausfallsicher mit Archivierung gekoppelt**
**Status:** statisch belegt.
**F6:** Z. 89–89, Z. 207–213, Z. 274–279.
**Code:** `biotop/organe/lazarus.py:46–76`; `biotop/lauf.py:107–114`; `biotop/lauf.py:316–356`; `biotop/organe/gedaechtnis.py:262–312`.
Snapshotnamen sind lauf_id/generation. Wiederholung benutzt git tag -f, öffnet dasselbe tar.gz mit w:gz und überschreibt die DB-Zeile per ON CONFLICT; das Archiv ist nicht append-only. Der Generationspfad schreibt zuvor Werkdateien, markiert Kandidaten angenommen und lässt art_merken einen kostenpflichtigen Musteraufruf machen, bevor Lazarus überhaupt sichert. Scheitert dieser Aufruf bzw. das Archivieren, gibt es keinen transaktionalen Rückbau des Werks. sicherstellen_repo überschreibt außerdem bei der Initialisierung die werkseigene .gitignore.
Ein Zustand kann verändert bzw. als angenommen markiert sein, ohne neuen rückholbaren Schnappschuss; vorhandene Historie kann unter demselben Schlüssel ersetzt werden.
**Grenze:** Kein Archiv überschrieben und kein Ausfall provoziert. Belegt sind Schreibreihenfolge und Überschreiboperationen, nicht ein eingetretener Datenverlust.

### A31 — Rückkehr restauriert nicht den vollständigen Laufzustand und scheitert bei Prüfsummenabweichung nicht laut
Zugeordnete Einzelbefunde: A31, B-20.

**A31: Rückkehr restauriert nicht den vollständigen Laufzustand und scheitert bei Prüfsummenabweichung nicht laut**
**Status:** statisch belegt.
**F6:** Z. 89–90, Z. 212–213.
**Code:** `biotop/organe/lazarus.py:28–35`; `biotop/organe/lazarus.py:83–110`; `biotop/lauf.py:423–434`; `biotop/__main__.py:84–89`.
Produktivrückkehr stellt Dateien per Git her und markiert nur spätere angenommene Generationen; Landkarte <=2 erhält 'veraltet', aber Straßen, Verträge und Stufe 3 werden nicht aus dem Stand n wiederhergestellt; laufende/vorgelegte Generationen werden von der Statuskorrektur nicht erfasst. Die Messwerte werden nur zurückgegeben. Eine abweichende Werkprüfsumme setzt stimmt=False, wirft aber keinen Fehler; CLI und Freigabe-Ablehnung behandeln die Rückgabe normal. Ein benannter Ablauf 'fehlerhafte Generation finden -> n-1 -> Immuntest -> n..n+k wiederholen' fehlt in den gelesenen Eintrittsstellen. Der Werkhash deckt Inhalte/Pfade, nicht ausführbare Dateimodi oder Symlinktyp ab.
Dateirückkehr und Lauf-/Messgerätrückkehr sind nicht dasselbe; eine festgestellte unvollständige Rückholung kann ohne Stopp fortgesetzt werden.
**Grenze:** Keinen Schnappschuss zurückgeholt. Keine tatsächliche Prüfsummenabweichung behauptet; auch abgelehnte Linien werden nicht pauschal als gelöscht bezeichnet.

**B-20: Ablehnung erzeugt keinen Fehlertest und hinterlässt inkonsistente Begleitstände**
**Status:** aktuelle_Logik.
**F6:** Z. 89–89, Z. 91–91, Z. 212–212, Z. 213–213, Z. 216–216, Z. 259–259.
**Code:** `biotop/lauf.py:324–350`; `biotop/lauf.py:423–434`; `biotop/organe/lazarus.py:83–110`.
Bei menschlicher Ablehnung werden Geschmack gespeichert, Git zurückgesetzt und Generations-/Kandidatenstatus geändert, aber kein Immuntest erzeugt und keine Wiederholungslinie geplant. Bereits vor Freigabe angelegte angenommene Artmuster und Immunsystem-im_werk/Archivstatus werden nicht zurückgesetzt. Lazarus markiert Landkarte nur veraltet statt sie wiederherzustellen; dessen stimmt=False ist ein Rückgabewert, kein Stop. Eine automatische Rückkehr n-1 mit erneutem Durchlaufen der betroffenen Generationen bei später entdecktem Fehler fehlt.
Der geforderte vollständige rückholbare Biotop-Zustand und die Immunisierung bei Ablehnung sind nicht durch den aktuellen Freigabepfad gedeckt.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** 48 freigabe.frei und fünf lazarus.rueckkehr-Ereignisse sind vorhanden; kein freigabe.abgelehnt-Ereignis. Damit ist dieser Ablehnungszweig hier gebaut/gelesen, nicht historisch ausgeführt belegt.

### A32 — Nachgerechnete Verlaufskurve verwendet nicht durchgängig den Endtestbestand oder nur angenommene Generationen
Zugeordnete Einzelbefunde: A32, C03.

**A32: Nachgerechnete Verlaufskurve verwendet nicht durchgängig den Endtestbestand oder nur angenommene Generationen**
**Status:** statisch belegt.
**F6:** Z. 107–107, Z. 150–154, Z. 245–246.
**Code:** `biotop/lauf.py:437–475`; `biotop/kern/messgeraet.py:208–223`; `biotop/__main__.py:71–79`; `biotop/dienst.py:199–207`; `biotop/oberflaeche.py:104–114`.
kurve_nachrechnen selektiert alle Lazarus-Einträge und den numerisch letzten Snapshot ohne Join auf angenommene/freigegebene Generationen. Der Endtestbestand wird nur mit tests.glob('test_*.py') ermittelt: Unterverzeichnisse/Verträge fehlen. Die Dateien werden über den alten Bestand gelegt, nicht als vollständiger Ersatz; weggefallene alte Tests verbleiben. Außerdem bleibt messung.kernmass die historische F1-Formel, und CLI sowie HTTP-Feld kernmass geben dieses Feld aus, während die Auswahl F2 verwendet. Die Web-Kurve berechnet F2 separat aus Bereichswerten.
Die Pflichtkurve kann eine andere Population/Testgrundlage messen; gleich benannte Kennzahlen in Ausgaben stehen für verschiedene Formeln.
**Grenze:** Keine Kurve nachgerechnet. Nicht behauptet wird, die Web-Kurve verwende F1; genau dort ist die lokale F2-Neuberechnung vorhanden.

**C03: Verlaufskurve übernimmt nicht den vollständigen Endtestbestand**
**Status:** statisch belegt.
**F6:** Z. 151–151, Z. 154–154.
**Code:** `biotop/lauf.py:448–470`.
kurve_nachrechnen übernimmt mit glob(test_*.py) nur unmittelbar unter tests liegende Endtests. Tests in Unterordnern, insbesondere tests/vertraege, werden nicht als Endbestand auf ältere Archive übertragen. Außerdem werden sämtliche Lazarus-Einträge statt ausdrücklich freigegebener/angenommener Generationen ausgewählt. Damit ist dieser Befehl für verschachtelte/veränderte Vertragsbestände nicht die verlangte Gleichheit des Endtestbestands über angenommene Generationen.

**Grenze:** Kein neuer Kurvenlauf. Keine Behauptung, eine bestimmte alte Zahl sei deswegen numerisch falsch; der allgemeine Rechenpfad ist eingeschränkt.

### A33 — Späteres F7-Bauteil C kann einen neuen Fund wegen seiner eigenen vorherigen Ansage sperren
Zugeordnete Einzelbefunde: A33, B-11.

**A33: Späteres F7-Bauteil C kann einen neuen Fund wegen seiner eigenen vorherigen Ansage sperren**
**Status:** statisch belegt.
**F6:** Z. 91–91, Z. 195–197, Z. 217–221.
**Code:** `biotop/organe/aegis.py:325–331`; `biotop/organe/aegis.py:394–407`; `biotop/organe/aegis.py:423–463`; `biotop/organe/aegis.py:619–625`; `biotop/organe/aegis.py:650–668`.
_angriff schreibt die aktuelle neue Behauptung schon vor dem Testschreiben als aegis.ansage. aufnahmesperre fragt später bisherige_behauptungen erneut ab; diese Funktion enthält ausdrücklich auch alle angesagten Behauptungen desselben Laufs/Bereichs. Es gibt keinen Ausschluss des aktuellen Angriffs. Bei leerem Altvorrat und einem Test, dessen abgeleiteter Schlüssel der eigenen Ansage entspricht, steht sein Schlüssel deshalb nun im Vorrat und wird als Wiederholung abgewiesen. Fund- und Normaufnahme benutzen beide diesen Pfad.
Die spätere Aufnahmehärtung kann einen erstmals bestätigten Fehler an der Aufnahme seines Tests hindern. Eine Zählung 'gesperrt' belegt dabei nicht automatisch eine echte Alt-Doppelung.
**Grenze:** Keine neue Probe und keine Quote aus Lauf 25 berechnet. Der bedingte Selbstblock folgt direkt aus der Reihenfolge der Schreib-/Lesepfade.

**B-11: Späteres C sperrt die eigene frische Ansage als vermeintliche Doppelung**
**Status:** spaetere_C_Erweiterung_aktuelle_Logik.
**F6:** Z. 91–91, Z. 194–194, Z. 195–195, Z. 221–221.
**Code:** `biotop/organe/aegis.py:325–331`; `biotop/organe/aegis.py:394–420`; `biotop/organe/aegis.py:442–462`; `biotop/organe/aegis.py:619–668`; `pruefung/lauf25_pfadnachweis.py:95–102`; `pruefung/nachgang_n13_n14.py:115–121`.
A schreibt die neue Ansage vor dem Angriff als ausgefuehrt=true ins Protokoll. C lädt danach genau diese Protokollansagen in seinen Vorrat und hat weder Kandidatenkennung noch Ausschluss der aktuellen Ansage. Wenn der erste gültige Test tatsächlich die angekündigte Behauptung prüft, liegt sein Schlüssel daher bereits im Vorrat und C weist ihn ab. Neu, aber anders als angesagt, kann dagegen passieren. Die gestellten Pfadproben ersetzen _angriff komplett und schreiben keine echte vorlaufende Ansage; sie prüfen diese Wechselwirkung nicht.
Das als F7 bezeichnete Zusatzteil kann neue bestätigte Fehler trotz Immunisierungspflicht verwerfen. Es darf nicht als bereits vollständig geprüfte Verbesserung des F6-Standes ausgegeben werden.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Nur statischer Integrationsbefund, keine neue Ausführung. Die DB enthält C-Prüfereignisse für Prüfwerk-IDs sowie K2680 in gestellten Pfaden; Lauf 25 selbst hatte vor den Pfadproben keinen normalen C-Aufruf. Die tatsächliche Fehlerrate dieser Selbstsperre ist daraus nicht messbar.

### B-01 — Satz 2: Anklägerablauf wurde unter weiterbenutzten Lauf-IDs geändert
Zugeordnete Einzelbefunde: B-01.

**B-01: Satz 2: Anklägerablauf wurde unter weiterbenutzten Lauf-IDs geändert**
**Status:** historische_Ausfuehrung_und_aktuelle_Schutzluecke.
**F6:** Z. 86–86, Z. 195–195.
**Code:** `biotop/lauf.py:133–166`; `biotop/organe/aegis.py:302–331`; `biotop/organe/aegis.py:392–420`.
Es gibt beim Start einer Generation keinen Abgleich einer eingefrorenen Messgeräte-/Anklägerrevision. Für Lauf 22 belegen die Ereignisse Generationen 1–4 ohne Ansagephase, danach Generation 5 mit Ansage unter derselben ID und demselben Ausgang 0. In Lauf 23 wurde die zunächst unvollständige Ansagesperre zwischen Generation 4 und 5 wirksam geändert: vorher wiederholte Ansagen trotz bisherige=0; danach Vorrat aus bisherigen Ansagen und echte Sperrung. Es geht um den Anklägerablauf, nicht um eine bloße Commit-Zeit.
Die Kurven und Ablehnungen dieser IDs sind kein Nachweis eines durchgehend unveränderten Messgeräts. A/B dürfen weder dem ursprünglichen v6-Commit noch den gesamten IDs 22/23 pauschal zugeschrieben werden.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Historisch belegt, nicht heute ausgeführt: Lauf 22 Gen 4 Ende #13232 2026-09-19T21:22:12.328Z; Gen 5 Start #14248 22:46:02.011Z; erste A-Ansage #14305 22:46:45.372Z. Nur ein mass.eingefroren (#12517). Lauf 23 #13398 und #13442 nennen extern_filtern|raises:ValueError zweimal ausgefuehrt=true, bisherige=0; #13773 wiederholt nach_zeit|raises:FilterFehler; #14086 nennt bisherige=3, #14160 sperrt nach_zeit|raises:FilterFehler mit bisherige=8. Gen 5 beginnt unter derselben ID #14066. B-spezifische Vorlage ist im Aufrufprotokoll nicht gespeichert: verbesserte Mentor-Verweise allein beweisen die genaue Vorlage nicht.

### B-09 — Altes funde_neubewerten.py bleibt eine abweichende historische Prüflogik
Zugeordnete Einzelbefunde: B-09.

**B-09: Altes funde_neubewerten.py bleibt eine abweichende historische Prüflogik**
**Status:** historisches_aufrufbares_Pruefscript.
**F6:** Z. 103–103, Z. 106–106, Z. 107–107, Z. 108–108, Z. 197–197, Z. 222–222.
**Code:** `pruefung/funde_neubewerten.py:17–43`; `biotop/organe/fundpruefung.py:55–74`; `biotop/organe/aegis.py:185–227`.
Das Altscript scannt nur status=offen, sucht Verweise mit einem eigenen Regex irgendwo im gesamten Code und löst keine Vertrags-/Satzkennung auf. Sein Regex akzeptiert z.B. bloßen Vertragstext außerhalb des Testnamens/Docstrings, kann nicht vorhandene Kennungen anerkennen und kennt nur eine enge Schreibweise für Verfassung. Erfolg/Absturz kommen aus Ausgabetext statt Fehlerort. Mit --schreiben ändert es normale Immunsystemzeilen dauerhaft; keine Bestandskopie oder Rücknahme. Es ist kein Aufrufziel von CLI mass/generation und nicht die heutige Fundpruefung.
Alte Ausgaben dieses Scripts dürfen nicht als Nachweis der aktuellen gemeinsamen Ableitung zitiert werden; erneutes Aufrufen mit --schreiben wäre eine Bestandsmigration, keine neutrale Prüfung.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** #11417 am 2026-09-19T15:39:16.728Z protokolliert sechs Änderungen mit dem exakt vom Altscript erzeugten Payloadschema anzahl/namen/regel. Das belegt den historischen Neubewertungsvorgang, nicht forensisch den Prozessnamen des Aufrufers. Spätere Organereignisse verwenden geprueft/kammerlaeufe/aenderungen. Script wurde in dieser Prüfung nur gelesen.

### B-10 — Expliziter Vertragsname wird mit inhaltlichem Recht gleichgesetzt
Zugeordnete Einzelbefunde: B-10.

**B-10: Expliziter Vertragsname wird mit inhaltlichem Recht gleichgesetzt**
**Status:** aktuelle_Logik.
**F6:** Z. 103–103, Z. 108–108, Z. 197–197.
**Code:** `biotop/organe/aegis.py:185–227`; `biotop/organe/aegis.py:591–607`; `pruefung/nachgang_n13_n14.py:70–93`.
_nennt_vertrag verifiziert nur, dass eine genannte Datei, ein Testname oder eine Satznummer existiert, und liefert True. Es prüft nicht, dass deren Zusicherung die Erwartung des neuen Tests trägt. Das N14-Script fordert unter vorhandenen Vertragskennungen preis_fuer(...) >= 999.0 bzw. anzahl() < -1, während der Kandidat nur einen Kommentar ergänzt. Ein existierender Name verwandelt dadurch eine frei erfundene Erwartung in einen Fund.
2a1 bleibt materiell offen: ausdrücklich benannt ist notwendig, aber nicht hinreichend für „Vertrag weist das Verhalten als falsch aus“. Dies ist kein natürlich gefundener Fehler.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Der gestellte N14-Pfad ist historisch belegt: #16025 noch Norm; #16026 bis #16030 anschließend Fundpfad mit Modellkennzeichnung hermes/gestellt-n14, immun.gefunden #16029. #16028 führt den tatsächlich berechneten grünen Schlüssel anzahl|Lt:name (nicht die Kommentarbehauptung Lt:zahl). Diese Prüfung hat den Pfad nicht erneut ausgeführt.

### B-12 — Archivierung liegt weiterhin hinter erfolgreicher Generalprobe
Zugeordnete Einzelbefunde: B-12.

**B-12: Archivierung liegt weiterhin hinter erfolgreicher Generalprobe**
**Status:** aktuelle_Logik.
**F6:** Z. 223–223.
**Code:** `biotop/lauf.py:175–190`; `biotop/lauf.py:274–275`; `biotop/lauf.py:309–350`; `biotop/organe/aegis.py:528–529`.
Der Zähler benutzt zwar alle Generationen, die Archivierungsschleife wird aber nur erreicht, nachdem ein Gesamtkandidat die Generalprobe bestanden hat und ins Werk geschrieben wurde. Frühere returns bei keinem Überlebenden oder Generalprobenfehler umgehen sie. Zusätzlich bleiben in solchen Generationen neu gefundene Tests status=gefunden, während die Archivierung nur offen/offen_norm auswählt.
Am gesättigten Werk ohne angenommene Generation archiviert das Organ weiterhin nicht nach fünf Generationen. Genau die in F6 beschriebene Fehlerklasse besteht als Aufrufstellenfehler fort.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Es gibt genau ein immun.archiviert-Ereignis (#13340), ausdrücklich mechanikpruefung=true, anschließend #13341 Rücknahme zweier mitgetroffener Normtests. In Lauf 22 bestehen noch Probe-Funde aus Gen 0 trotz fünf Folgegenerationen. Das beweist keinen natürlichen Archivierungserfolg.

### B-13 — Artgedächtnis und Geschmack werden nicht vor jeder Generation gelesen
Zugeordnete Einzelbefunde: B-13.

**B-13: Artgedächtnis und Geschmack werden nicht vor jeder Generation gelesen**
**Status:** aktuelle_Logik.
**F6:** Z. 231–234, Z. 183–183.
**Code:** `biotop/organe/genesis.py:87–120`; `biotop/organe/landkarte.py:230–255`; `biotop/organe/mentor.py:59–67`; `biotop/organe/jury.py:38–55`; `biotop/dienst.py:161–166`.
Der Schwarmauftrag liest Projektwege, Elite, Verfassung, offene Funde und Mentor-Richtung; er liest weder art_text noch Geschmack. landkarte.sicht ergänzt diese beiden ebenfalls nicht. art_text wird beim expliziten Mentoraufruf gelesen, die Geschmacksvorhersage in der Web-Vorlage/CLI, nicht durch die Jury und nicht im Generationsanfang. Die drei Gedächtnisse sind dauerhaft vorhanden, aber ihre geforderte Lesewirkung ist nicht vollständig verbunden.
Abstrahierte werkübergreifende Muster erreichen den Schwarm nicht als Vorlage; ein fehlender Musterverweis ist daher nicht nur Modellverhalten. Die Geschmacksvorhersage ergänzt die Jury nicht wie gefordert.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Mentor-/Geschmacks-/Juryereignisse sind belegt, aber das Aufrufprotokoll speichert keine vollständigen System-/Nutzerprompts. Der statische Callgraph zeigt die aktuelle Leselücke; es wird nicht behauptet, die Tabellen seien unbenutzt.

### B-14 — Bauteil B unterschreitet die Hälfte und begrenzt fremde Muster vor dem Filter
Zugeordnete Einzelbefunde: B-14.

**B-14: Bauteil B unterschreitet die Hälfte und begrenzt fremde Muster vor dem Filter**
**Status:** aktuelle_Logik.
**F6:** Z. 233–233.
**Code:** `biotop/organe/gedaechtnis.py:368–392`.
Bei GEZEIGT=25 nutzt fremd_min die Ganzzahldivision 25//2. Sind ausreichend eigene und fremde Einträge vorhanden, werden 13 eigene und 12 fremde gezeigt: 12/25=48 %, nicht mindestens die Hälfte. Ferner werden zunächst nur die letzten 200 angenommenen Einträge insgesamt gelesen und erst danach fremde Muster herausgefiltert; genügend vorhandene fremde Muster jenseits dieses Fensters können unsichtbar bleiben.
Die Mengenregel von F6 ist auch im später gebauten B nicht für jeden Bestand erfüllt. Die Mindest-vier/fünf-Verweisausgaben eines Mentors beweisen keine korrekte Mindestvorlage.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Deterministische Rechnung am gelesenen Ausdruck, keine Organ-Ausführung. Historisch #14246 enthält drei Richtungen mit werkübergreifendem Verweis; das belegt den Mentor-Ausgang, nicht die 50%-Invariante.

### B-15 — Geschmack mischt Simulation und Hermes-Freigaben in Philipps Modell
Zugeordnete Einzelbefunde: B-15.

**B-15: Geschmack mischt Simulation und Hermes-Freigaben in Philipps Modell**
**Status:** aktuelle_Logik.
**F6:** Z. 234–234, Z. 264–264.
**Code:** `biotop/organe/gedaechtnis.py:427–439`; `biotop/organe/gedaechtnis.py:490–511`; `biotop/lauf.py:416–424`; `pruefung/tor3_geschmack.py:1–20`; `biotop/dienst.py:164–166`.
geschmack_merken speichert jede gewählte Kandidaten-ID einer Freigabe als eigene Entscheidung. geschmack_modell ohne quelle filtert weder nach echter Person noch nach Simulationsherkunft; der Web-Aufruf lässt quelle weg. Die Schwelle len(rows)>=20 zählt Kandidatenzeilen, nicht unabhängige Freigabeentscheidungen. Simulation P1 und Hermes-Vollmacht können so Philipps angeblichen Geschmack trainieren.
Eine sichtbare Geschmacksvorhersage ist kein Nachweis eines aus mindestens zwanzig echten Philipp-Entscheidungen gelernten Modells.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** DB: 15 Zeilen quelle=freigabe von Hermes unter Vollmacht, 20 Zeilen quelle=regel_P1 von Simulation P1; keine als solche belegten echten Philipp-Freigaben in dieser Tabelle. Die P1-Prüfung ist als Mechanikversuch zu würdigen, nicht als persönliches Lernen.

### B-16 — Bandit belohnt Überleben statt Annahme und lernt nur pro Lauf
Zugeordnete Einzelbefunde: B-16.

**B-16: Bandit belohnt Überleben statt Annahme und lernt nur pro Lauf**
**Status:** aktuelle_Logik.
**F6:** Z. 183–183.
**Code:** `biotop/organe/nischen.py:60–89`; `biotop/lauf.py:235–246`; `biotop/organe/genesis.py:116–120`.
Der Schlüssel der Bandittabelle ist (lauf_id,nische,hersteller), nicht Werkklasse. Gebucht wird unmittelbar nach Aegis mit erfolg=(status==ueberlebt), bevor Bereichswahl, Generalprobe und Freigabe feststehen. Nicht gewählte oder später verworfene Kandidaten bleiben Erfolge; beim neuen Lauf beginnt ein neuer Gewichtsbestand. KEIN VORSCHLAG wird dagegen korrekt nicht gebucht.
Die Herstellergewichtung optimiert einen anderen Erfolg und überträgt keinen Erfahrungsvorteil zwischen gleichartigen Werken. Vier Nischen, verschiedene Hersteller und Eliten sind dennoch echte vorhandene Mechanik.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** bandit.wahl und bandit-/eliten-Tabellen belegen historischen Einsatz. Die Bewertung als angenommener Kandidat ist aus der Mechanik nicht ableitbar; es wird nicht behauptet, Bandit fehle.

### B-17 — Mentor-Richtung ist weder Startpflicht noch eigener unveränderter Lauf
Zugeordnete Einzelbefunde: B-17.

**B-17: Mentor-Richtung ist weder Startpflicht noch eigener unveränderter Lauf**
**Status:** aktuelle_Logik.
**F6:** Z. 142–142, Z. 143–143, Z. 144–144, Z. 202–202, Z. 257–257.
**Code:** `biotop/lauf.py:140–166`; `biotop/organe/mentor.py:80–104`; `biotop/organe/mentor.py:107–135`.
generation prüft bereit/laeuft und offene Freigabe, nicht eine gewählte Richtung. richtung_text liefert bei fehlender Wahl einen leeren String. waehlen überschreibt laeufe.richtung an derselben ID auch nach Generationen; es legt keinen neuen Lauf und kein neues Maß an. Der Mentor berechnet anzahl_ok, Pflichtfelder und erfundene Verweise, speichert/returniert aber auch negative Prüfergebnisse, ohne zu stoppen.
Arbeiten ohne Richtungswahl und Richtungswechsel im selben Lauf bleiben möglich. Der 3–5-Richtungen-Vertrag ist nur protokollierte Diagnose, kein Gate.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Kein ungültiges Mentor-Richtungsformat in den vorhandenen Protokollprüfungen gefunden. Historisch wurde Lauf 22 jedoch zweimal gewählt (#12548 und #14247) bei identischer Lauf-ID; das ist eine belegte Nachwahl, kein Beweis einer grundlegend anderen Zielrichtung.

### B-18 — Verhandlung kann leere Prüfwerte als bestanden werten und mehrere Nachbarn verlieren
Zugeordnete Einzelbefunde: B-18.

**B-18: Verhandlung kann leere Prüfwerte als bestanden werten und mehrere Nachbarn verlieren**
**Status:** aktuelle_Logik.
**F6:** Z. 90–90, Z. 203–203.
**Code:** `biotop/lauf.py:495–550`; `biotop/organe/aegis.py:474–519`.
paar_ok verlangt nur leere vertrag_verletzt/pareto_schlechter/grenzen_gerissen. Vorzeitige Aegis-Ablehnungen (z.B. Verfassung, Diff) haben dieselben leeren Defaultfelder und mass=None und können daher als bestandene Verhandlung protokolliert werden. Bei mehreren Nachbarn wird anp jeweils allein als extra_code geprüft; extra.update sammelt Anpassungen, das gesammelte extra wird aber nie erneut übergeben oder endgültig genutzt. Das letzte u2 und dessen _dateien können frühere Nachbaranpassungen ersetzen. Bei einseitig_ok gilt außerdem all(...) über leere ids als Bestätigung ohne tatsächliche Nachbarantwort.
Bestandene Verhandlung bedeutet nicht zwingend bestandene vollständige Anpassung aller Nachbarn; die spätere Gesamtauswahl kann eine nicht vollständig geprüfte Kombination erhalten.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Früherer Cachefehler ist historisch #6488 dokumentiert und in aktuellen Zeilen 529–531 korrigiert. Dieser Bericht gibt den alten Cachefehler nicht als weiterhin vorhandenen Hauptfehler aus. Die hier beschriebenen neuen Randfälle sind nur gelesen, nicht ausgeführt.

### B-19 — Nexus hat keinen vollständigen Kombinations-/Wiederholungspfad
Zugeordnete Einzelbefunde: B-19.

**B-19: Nexus hat keinen vollständigen Kombinations-/Wiederholungspfad**
**Status:** aktuelle_Logik.
**F6:** Z. 205–205, Z. 208–208, Z. 232–232.
**Code:** `biotop/lauf.py:277–313`; `biotop/lauf.py:248–252`; `biotop/lauf.py:133–162`; `biotop/organe/aegis.py:503–517`.
Das Zusammenführen setzt Dateien mit dateien[p]=inhalt zusammen (letzter Schreiber gewinnt); kollidierende Nachbar- oder Testdateien werden nicht als Konflikt gemeldet. Die Generalprobe misst zwar das ganze Werk und Verträge, ruft aber die Werkverfassung nicht für den finalen Verbund auf. extra_code des Nachbarn liegt in Aegis zudem nicht im an verfassung.mechanisch_pruefen übergebenen dateien-Dict. Bei Generalprobenablehnung werden Kandidaten erst nach den Gedächtnisaufrufen auf abgelehnt gesetzt; Kombination und Grund werden nicht ins Projektgedächtnis eingespeist. Es gibt keinen bis zu dreimaligen Wiederholungszähler für die Generation, sondern MAX(nummer)+1.
Das Ganze wird tatsächlich gemessen, aber nicht mit dem vollständigen geforderten Verfassungs-/Lern-/Retry-Protokoll. Nexus ist vorhanden in lauf.py, nicht fehlend wegen fehlender nexus.py-Datei.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** 116 generation.ergebnis-Ereignisse belegen den historischen Hauptpfad. Aus diesen Erfolgs-/Fehlerzeilen allein folgt keine Erfüllung der Kombinationspflicht.

### B-22 — Historisches Oberfläche-Prüfscript überschreibt ein echtes Konto ohne Wiederherstellung
Zugeordnete Einzelbefunde: B-22.

**B-22: Historisches Oberfläche-Prüfscript überschreibt ein echtes Konto ohne Wiederherstellung**
**Status:** historisches_aufrufbares_Pruefscript.
**F6:** Z. 106–106.
**Code:** `pruefung/tor3_oberflaeche.py:16–21`; `pruefung/tor3_oberflaeche.py:65–66`; `pruefung/tor3_oberflaeche.py:77–90`; `biotop/kern/anmeldung.py:21–41`.
Das Script verbindet sich ohne Prüf-DB-Override mit dem normalen Bestand und legt unter dem bestehenden Benutzer philipp ein zufälliges Prüfkennwort an. benutzer_anlegen benutzt INSERT OR REPLACE: Salz/Hash werden ersetzt. Anmeldung erzeugt zusätzlich einen gültigen Token-Datensatz. finally beendet nur den Prüfserver; Konto und Tokens werden nicht gesichert/zurückgestellt. Die Freigabeprobe ruft zudem ungeprüft die echte Freigaberoute auf und verlässt sich darauf, dass keine Generation vorliegt.
Ein erneuter Aufruf wäre keine bestandsneutrale Prüfung und könnte den Benutzerzugang überschreiben bzw. eine wartende Generation freigeben. Das ist ein historisch aufrufbares Prüfschema, KEIN heute laufender Angriff.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Gelesen, nicht ausgeführt. Anmeldeereignisse #7504–#7509 zeigen historisch Benutzeranlage und Tokens im einschlägigen Zeitraum; sie belegen allein weder die Hashwerte noch eindeutig den Scriptprozess. Keine Zugangsdaten oder Tokenwerte wurden aus der DB ausgelesen oder in den Bericht kopiert.

### B-23 — Web-Vorlage zeigt keinen vollständigen Anklägerbericht und nicht alle Maßkurven
Zugeordnete Einzelbefunde: B-23.

**B-23: Web-Vorlage zeigt keinen vollständigen Anklägerbericht und nicht alle Maßkurven**
**Status:** aktuelle_Logik.
**F6:** Z. 94–94, Z. 245–245, Z. 246–246.
**Code:** `biotop/dienst.py:153–168`; `biotop/organe/aegis.py:479–491`; `biotop/oberflaeche.py:104–124`; `biotop/oberflaeche.py:133–136`.
Dienst.vorlage sucht angriff, norm, tests_neu usw. im Kandidatenfeld masse. Aegis.fertig schreibt dort nur Messwerte plus _dateien/_basis_paar/_urteil_f2; die ausführliche Anklage steht im Protokoll, nicht in diesen masse-Feldern. Der ausgegebene anklaeger-Block bleibt so gewöhnlich leer. Die Kurve zeichnet nur Gesamtkernmaß und Bereichslaufzeit, nicht alle harten Maße; die Landkarte zeigt Stufe 0/1, für Stufe 2/3 nur eine Anzahl.
Die Elemente sind nicht bloß Namen: reale JSON-Routen und Darstellung sind vorhanden. Ihre Inhalte decken jedoch den F6-Vorlagen- und Kurvenumfang nicht ab. Oberfläche-Prüfungen auf HTTP 200 oder vorhandene Schlüssel genügen nicht.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** Historische Login-/Routentests belegen Teilfunktion, keinen visuellen Vollständigkeitsnachweis. Hier wurde weder Browser noch Dienst gestartet.

### B-24 — Entropie misst Mengen von Textzeilen und filtert Proben am Namen
Zugeordnete Einzelbefunde: B-24.

**B-24: Entropie misst Mengen von Textzeilen und filtert Proben am Namen**
**Status:** aktuelle_Logik.
**F6:** Z. 90–90, Z. 108–108, Z. 227–227.
**Code:** `biotop/organe/entropie.py:25–44`; `biotop/organe/entropie.py:77–102`.
Die Diversität bildet set(diff-Zeilen), verliert also Wiederholungszahl und Reihenfolge. Kandidaten mit unterschiedlichen Häufigkeiten derselben geänderten Zeile können als identisch erscheinen. Die SQL-Auswahl kennt nur nische!=probe, nicht ist_probe; markierte Jury-/Pfadproben mit anderer Nische können eingehen. Ein Fenster ohne Kandidaten mit Diff erhält anteil=0.0 statt einer expliziten Nicht-Bestimmbarkeit. Die Sättigungsmeldung selbst beendet den Lauf tatsächlich.
Der ausgewiesene Doppelgänger-Anteil ist eine Textmengenheuristik, kein vollständiger Nachweis der verlangten geänderten-Zeilen-Differenz. Probe-Markierungen werden an dieser Messstelle nicht beachtet.
**Grenze:** Kein neuer Lauf; statische/historische Einordnung nicht zur aktuellen Torabnahme aufwerten.

**Historischer Beleg:** 43 entropie.generation und sechs entropie.saettigung-Ereignisse sind vorhanden. Das belegt die Meldefunktion, nicht die Messgenauigkeit dieser Diversitätsheuristik.

### C01 — Vorgänger-Torwächter und zugesagte Entwicklungsabsicherung nicht übernommen
Zugeordnete Einzelbefunde: C01.

**C01: Vorgänger-Torwächter und zugesagte Entwicklungsabsicherung nicht übernommen**
**Status:** statisch belegt.
**F6:** Z. 308–312, Z. 322–322.
**Code:** `biotop/dienst.py:25–25`; `biotop/dienst.py:60–102`; `.gitignore:1–4`.
Der Dienst ist Python HTTPServer, nicht der übernommene Express-Torwächter. _json_body liest die angegebene Content-Length ohne Obergrenze; bei der Anmeldung fehlen im Dienst Rate-Limit, Request-ID, CORS-Liste und die genannte zentrale Fehler-/Redaction-Schicht. Im vollständigen Git-Dateiinventar fehlen CI, CodeQL, Dependabot, Vitest/Playwright sowie der gitleaks-Pflichtlauf. .gitignore ignoriert .env*, ist aber kein Archiv-/Secret-Scan. Datenbank und Token-Anmeldung existieren; das erfüllt nicht den gesamten Übernahmeauftrag.

**Grenze:** Gilt für den untersuchten Biotop-Quellstand; keine Aussage über beliebige vorgeschaltete Fremdserver. Kein Angriff und kein Login ausgeführt. Inventarbeleg 03-dateien.json.

### C02 — Verfassungsentwurf ist weiterhin manueller Import, kein Organentwurf
Zugeordnete Einzelbefunde: C02.

**C02: Verfassungsentwurf ist weiterhin manueller Import, kein Organentwurf**
**Status:** statisch belegt.
**F6:** Z. 135–137, Z. 254–254.
**Code:** `biotop/organe/verfassung.py:1–7`; `biotop/organe/verfassung.py:24–41`.
Das Verfassungsmodul legt mitgelieferten Text und Regeln ein. Es erzeugt aus Aufnahmebericht/Landkarte keinen Entwurf mit 5–15 Sätzen; das Modul nennt dies ausdrücklich als auf später verschobene Arbeit. Manuell von Hermes/Chat-Claude verfasste Übungswerkdokumente sind nicht die Implementierung dieses Entwurfsorgans.

**Grenze:** Das Vorliegen zweier bestätigter Werkverfassungen wird nicht bestritten; es fehlt der verlangte allgemeine Entwurfsweg.

## Historisch vorhanden, heute nicht mehr als aktueller Mangel zählen

### A34 — Historisch behoben: Laufzeitaggregation benutzt heute Median statt Minimum
Der gelesene historische Elternstand 908c03d1ef7f4cd836921a2540b65e15de6da762 aktualisiert best mit min(best,d). Der heutige Code sammelt drei Laufzeiten, sortiert und nimmt das mittlere Element. streuung trennt die Ebene zwischen Messungen und verwirft ebene!='zwischen'; rauschtoleranz_aus_werten benutzt diese Funktion. Git führt die Umstellung unter a41838c8449ef8af471e8b1d89fdeed0633d3619.
Nur Quelltext-/Gitvergleich, keine Rauschkampagne. Die fehlende Weitergabe der Toleranz und Sperren bleibt ein separater aktueller Befund A10.

### A35 — Historisch behoben: Das in F6 noch offene Ansage-Bauteil ist heute implementiert
Am F6-Ausgang 7c73d403c18755dda26655c78ac7290c446d9f45 wird die Liste bisheriger Behauptungen nur in den Angriffsprompt eingebettet. Heute gibt es einen eigenen _ansage-Aufruf und vor dem Testschreiben einen deterministischen ansage-in-schon-Zweig. Der heutige Gitstand enthält damit ein nach F6 gebautes Bauteil; die historische Notiz 'noch nicht gebaut' ist kein aktueller Befund mehr.
Keine Ankläger-/OpenRouter-Aufrufe. Aktuelle Risiken durch begrenzten Vorrat, Prüfbestandskontamination und F7-Selbstblock werden nicht durch diese Existenzfeststellung entkräftet.

## Eigene Aussagen zurückgenommen / eingeschränkt

- „Vier Eichproben bestanden“ war bei der Normprobe keine Aussage über die Normregel. `masse` statt `mass`, `norm=[]`, `zuwachs=None` und Ablehnung schon durch Pareto sind dokumentiert. Die frühere 4-von-4-Abnahme darf für den untersuchten Stand nicht als Nachweis der Normzeile fortgeschrieben werden (A11/B04/B05).
- Der Fortbau von A und die geänderte Ansagehistorie innerhalb der weiterverwendeten IDs 22/23 verletzen Satz 2. Mehr Aufrufe allein wären kein Beweis; die konkreten Ansage-Payloads vor/nach dem Übergang sind es (B01).
- „Mindestanteil gebaut“ beweist nicht „Mindestanteil stets erfüllt“: der Branch bei genügend eigenen und fremden Einträgen zeigt 12 fremde von 25, also weniger als die Hälfte (B14; statisch, kein natürlicher neuer Lauf).
- Die Aufnahme-/Kern-/Generationsmechanik existiert; „eigenständig betriebsbereit“ wäre trotzdem falsch: kein laufender Dienst, kein erzwungener Vorspann, keine pytest-Eigen-Testsuite.
- Auch die Zusatz-Reproduktionsprüfung dieser Bestandsaufnahme scheiterte: erster Versuch `21-gegenfaelle.json`, Exit 1 wegen fehlerhaftem Testgerüst; die Wiederholung wurde von der Tool-Freigabe blockiert und nicht umgangen. Daher **0 von 4 vorgesehenen neuen Gegenfällen als vollständig bestätigt gemeldet**. Keine synthetischen Erfolgsoutputs. Der Skriptfehler wurde nur im außerhalb liegenden Prüfskript berichtigt, nicht im Biotop.
