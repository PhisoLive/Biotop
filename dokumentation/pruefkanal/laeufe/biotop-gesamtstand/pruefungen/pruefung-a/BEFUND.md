# Biotop gegen Masterprompt Fassung 6 — nur lesende Codeprüfung A

**Ergebnis: 35 Befunde — 31 statisch belegt, 2 nur Risiken, 2 historisch behoben.** Keine Tor-Abnahme und kein neu ausgeführter Biotop-Lauf. Schwerpunkt sind Aufnahme, Landkarte, Maß/Messgerät, Kasse, Anbieterschicht, Generation 0, Kammer, Kernschutz und Lazarus.

## Stand, Maßstab und Grenzen

- Geprüfter HEAD: `b42dc941e7fcb66632ba6a0e13b8df106a270a31`; Git-Arbeitsbaum vor und nach der Prüfung sauber.
- Historischer F6-Ausgang: `7c73d403c18755dda26655c78ac7290c446d9f45`. Unter `biotop/` unterscheiden sich gegenüber diesem Stand nur `organe/aegis.py` und `organe/gedaechtnis.py`; Einzelursachen sind dadurch nicht automatisch datiert. Beleg: `historischer-vergleich.json` und `historie.diff`.
- Verbindlicher Maßstab: `/root/.hermes/cache/documents/doc_8d640daa6c3c_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6.md`, 470 Zeilen, SHA-256 `effefeec0fe2ea0621d4fdca0f27bdd3dae981fd289f1e0b5d56da5aca81aefd`. F6 hat Vorrang vor älteren Bauhinweisen, Kommentaren und späteren F7-Erweiterungen.[1]
- Gelesen: 35 Python-Dateien mit 6.370 physischen Textzeilen im Paket `biotop/` (einschließlich drei leerer `__init__.py`) sowie Dockerfile und zwei Vorspann-/Prüfskripte. Einzeldateien und Siegel stehen in `LESEABDECKUNG.json`. Lesen ist kein Nachweis vollständiger Fehlererkennung.
- **Gelesen, nicht ausgeführt:** keine Tests, keine Generation, keine Kammer, keine Biotop-CLI, keine Installation, keine Anbieter-/OpenRouter-Anfrage. Ausschließlich Git-Lesezugriffe, Textlektüre, Prüfsummen, lesende Zähler der bereitgestellten DB-Kopie und Schreiben dieser Prüfartefakte außerhalb des Repositories.
- **„Statisch belegt“** benennt einen konkreten Codepfad, eine fehlende Vorbedingung oder eine nachweislich abweichende Implementierung. Ein tatsächlicher Betriebsfehler, Verlust oder erfolgreicher Angriff wird damit nicht behauptet. **„Nur Risiko“** kennzeichnet Folgen, die zusätzlich eine konkrete Eingabe, Nebenläufigkeit oder Manipulation voraussetzen und hier nicht erprobt wurden. **„Historisch behoben“** bedeutet Quelltext-/Gitvergleich, nicht bestandener Lauf.
- Schweregrade sind die Priorisierung der Prüfinstanz, keine gemessenen Ausfallwahrscheinlichkeiten. Implementierte Fähigkeiten, historische Ausführungsbehauptungen und aktueller Betrieb werden nicht gleichgesetzt.

## Wichtigste Sperrgründe aus dieser Prüfung

- **Maß und Eichung nicht als Kernvorbedingungen durchgesetzt:** Start ohne belegte Generation −1/0, überschreibbares Einfrieren und nicht übernommene Rauschtoleranzen/Bereichssperren (A08–A10).
- **Prüfbelege können falsch positiv sein:** Normprobe liest das falsche Urteilsfeld; Mutantenfang zählt Prozessfehler; Testidentitäten/Scannerfehler gehen verloren (A11, A15–A18).
- **Kernschutz ist nicht die geforderte technische Grenze:** ungeprüfte Wirts-Pfade, gemeinsame Schreibrolle sowie innerhalb der Kammer beschreibbare Messmittel (A03–A04, A26–A27).
- **Abbruch und Rückholbarkeit haben konkrete Lücken:** HTTP-Abbruch ruft eine fehlende Methode auf; ein laufender Generationskörper liest den Abbruch nicht erneut; Archivschlüssel sind überschreibbar und Rückkehr prüft nicht fail-closed (A28–A31).
- **Späteres Bauteil getrennt bewertet:** Die F7-Aufnahmesperre kann die eigene zuvor gespeicherte Ansage als Altvorrat behandeln (A33). Medianaggregation und Ansageorgan existieren heute dagegen tatsächlich (A34–A35).

## Abschnitt 2a — Prüfung der sechs Grundsätze

Keine pauschale Abnahme. Die Tabelle nennt die unmittelbaren Querbezüge; allgemeine Verfassungssätze bleiben davon getrennt.

| Grundsatz / F6-Zeile | Ergebnis im gelesenen Code | Befunde |
|---|---|---|
| 1 · fallender Test beweist keine Richtung · Z. 103 | Fehlermeldung wird als Werkabsturz interpretiert; Mutantenfang kann Infrastrukturfehler zählen. | A14, A15 |
| 2 · benannter Befehl für jede Pflicht · Z. 104 | Vorspann nicht als verbindlicher Einstieg; Abbruchbefehl vorhanden, aber HTTP-Weg defekt und laufender Prozess nicht kooperativ angehalten; Wiederholungsablauf nach Rückkehr fehlt. | A08, A28, A29, A31 |
| 3 · Streuung zwischen Messungen · Z. 105 | Median und Zwischen-Messungsfunktion vorhanden; deren Ergebnis wird nicht verbindlich in alle Grenz-/Gewinnentscheidungen übernommen. | A10, A20, A34 |
| 4 · Prüfung verändert geprüften Bestand nicht · Z. 106 | Probensperren der drei Gedächtnisse vorhanden; reale Ansage-/Immunaufnahme hat diese Sperre und Rücknahme nicht. | A13 |
| 5 · dieselbe Ableitung bei Nachrechnung · Z. 107 | Importgraph vs. Text-Zyklen; isolierte Nachlast vs. Komplettlast; Fehlermeldungssuche statt Aegis-Ortsprüfung; Kurve nicht mit vollständigem Endtestbestand. | A05, A10, A14, A32 |
| 6 · Sache statt Erscheinung · Z. 108 | Unter anderem Textanker in Proben, formell vorhandener statt gültiger tragender Pfad, falsches Norm-Urteilsfeld, Testnamen statt stabiler Identitäten und eigene Ansage als Altbestand. | A05, A06, A11, A12, A13, A16, A17, A33 |

Normgrundlage der Tabelle: `/root/.hermes/cache/documents/doc_8d640daa6c3c_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6.md:99–110`.[1] Details und genaue Codezeilen folgen; die Tabelle erzeugt keine zusätzlichen Befunde.

## Einzelbefunde

### A01 · Aufnahme ist auf eine schmale Python-Paketform beschränkt; Abhängigkeiten und echter Bau fehlen

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Aufnahme, Landkarte

**Masterprompt F6:** Z. 69, 119–121.[1]

**Quellstellen:**
- `/root/biotop/biotop/organe/landkarte.py` — Z. 1–6, 33–39.[3]
- `/root/biotop/biotop/organe/aufnahme.py` — Z. 22–24, 83–87, 117–160.[2]
- `/root/biotop/kammer/Dockerfile` — Z. 1–4.[4]

**Mechanik:** Die Aufnahme erkennt Endungen, wählt aber die Sprache nach den meisten Zeilen einschließlich Markdown/JSON und führt Tests/Bau nur bei sprache == 'Python' aus. _paket nimmt das erste alphabetische Wurzelpaket mit __init__.py; Bereiche sind dessen unmittelbare Unterpakete. Bau bedeutet lediglich import <paket>. Weder Aufnahme noch das feste Kammer-Image lesen/installieren Werkabhängigkeiten oder wählen Bauwerkzeuge. src-Layouts, mehrere Dienste, namespace packages und andere Sprachen sind damit keine implementierten Aufnahmewege.

**Folge:** Der Anspruch beliebiger Quelltext sowie die Aufnahme- und Phase-4-Vorbedingung sind nicht allgemein erfüllt; selbst ein Python-Werk kann aufgrund umfangreicher Dokumentation den Testlauf überspringen.

**Beweisgrenze:** Kein echtes Werk neu aufgenommen; keine Abhängigkeit installiert. Dies ist eine belegte Implementierungsbegrenzung, kein gemessener Fehler eines bestimmten Werks.

**Hermes-Bezug:** Landkarte Z.3–4 verschiebt tree-sitter ausdrücklich als „Entscheidung Hermes“ nach hinten, weil Phase 1 nur Python-Werke hat. Das belegt eine frühere Scope-Entscheidung, keine heutige F6-Freigabe für die weiterhin schmale Aufnahme.

### A02 · Ethische Prüfung akzeptiert ungültige oder leere Antworten als UNBEDENKLICH

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Aufnahme

**Masterprompt F6:** Z. 90, 95, 119–121.[1]

**Quellstellen:**
- `/root/biotop/biotop/organe/aufnahme.py` — Z. 90–114, 151–175.[2]

**Mechanik:** Das Urteil ist nur dann BEDENKLICH, wenn die erste Antwortzeile BEDENKLICH und nicht UNBEDENKLICH enthält. Jede andere Antwort, auch leer, unbekannt oder ohne Begründung, landet im else UNBEDENKLICH. Die Modellgrundlage besteht aus werkseigenen Beschreibungsdateien, einer begrenzten Python-Dateiliste und Stichworttreffern; Funktionscode wird nicht unabhängig semantisch geprüft. Stichworttreffer allein sperren nicht.

**Folge:** Fehlende oder nicht interpretierbare Prüfung besteht statt anzuhalten. Werkseigene Beschreibungen dominieren die Zweckbeurteilung.

**Beweisgrenze:** Kein schädliches Werk und keine Täuschungsantwort erzeugt. Prompt-Manipulation bleibt Risiko; der permissive Antwortparser ist direkt belegt.

### A03 · Aufnahmeziel wird ungeprüft gelöscht; Wiederaufnahme desselben Namens verändert andere Läufe

**Status:** statisch belegt · **Priorität:** kritisch · **Organe:** Aufnahme, Kernschutz

**Masterprompt F6:** Z. 88–89, 106, 270–279.[1]

**Quellstellen:**
- `/root/biotop/biotop/__main__.py` — Z. 37–38.[5]
- `/root/biotop/biotop/organe/aufnahme.py` — Z. 35–59, 117–125, 163–169.[2]
- `/root/biotop/biotop/lauf.py` — Z. 54–67.[6]

**Mechanik:** Der frei übergebene name wird direkt an WERKE angehängt. Absolute Pfade bzw. .. werden nicht auf einen erlaubten Namensraum begrenzt; _holen löscht ein vorhandenes Ziel mit shutil.rmtree, noch bevor die Quelle validiert ist. Auch ein normaler wiederverwendeter Name ersetzt dieselbe Arbeitskopie und aktualisiert denselben werke-Datensatz per ON CONFLICT. Andere Läufe können auf diese werk_id und diesen Pfad zeigen.

**Folge:** Destruktiver Pfad außerhalb des vorgesehenen Werkverzeichnisses ist nicht mechanisch ausgeschlossen; Wiederaufnahme ist kein isolierter Lauf und kann einen laufenden Bestand austauschen.

**Beweisgrenze:** Kein problematischer Name übergeben, nichts gelöscht. Die konkrete Löschfolge und fehlende Pfad-/Laufsperre wurden nur gelesen.

### A04 · Kandidaten- und Kammerpfade besitzen keine kanonische Begrenzung zum Werk

**Status:** statisch belegt · **Priorität:** kritisch · **Organe:** Kernschutz, Kammer

**Masterprompt F6:** Z. 88, 121, 237–238, 270–279.[1]

**Quellstellen:**
- `/root/biotop/biotop/organe/genesis.py` — Z. 75–76, 129–136.[7]
- `/root/biotop/biotop/kern/diffwerk.py` — Z. 48–61.[8]
- `/root/biotop/biotop/organe/aegis.py` — Z. 53–71.[9]
- `/root/biotop/biotop/organe/kammer.py` — Z. 38–42, 54–61.[10]
- `/root/biotop/biotop/lauf.py` — Z. 316–323.[6]

**Mechanik:** Genesis prüft nur textuelle Präfixe der aus dem Diff herausgelesenen Namen. Ein Pfad mit erlaubtem Präfix und folgenden ..-Segmenten bleibt zulässig; die Regex deckt außerdem nicht dieselben Headerformen ab wie diffwerk.parsen. Aegis liest werk / d.pfad vor einer kanonischen Prüfung; Kammer schreibt arbeit / rel direkt auf dem Wirt, und die spätere Übernahme schreibt pfad / p. Aufnahmekopie/Kammer dereferenzieren Symlinks statt sie auf Werkgrenzen zu begrenzen.

**Folge:** Wirts-Lese-/Schreibpfade außerhalb der Werkgrenze sind im Kandidatenweg nicht ausgeschlossen. Die Aussage, aus Schwarm/Kammer gebe es keine Schreibpfade in den Kern, ist strukturell nicht durchgesetzt.

**Beweisgrenze:** Keine Exploit-Datei, kein Symlink und kein Ausbruch ausgeführt. Bestätigt ist die fehlende Pfadvalidierung an allen genannten Übergängen, nicht ein erfolgter Kernzugriff.

### A05 · Straßen sind nur Importkanten; Funktionsaufrufe werden nie ausgewertet

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Landkarte, Messgerät

**Masterprompt F6:** Z. 129–132, 189–193, 402.[1]
**Direkter Bezug 2a:** 5, 6.

**Quellstellen:**
- `/root/biotop/biotop/organe/landkarte.py` — Z. 57–95, 98–125.[3]
- `/root/biotop/biotop/kern/messgeraet.py` — Z. 168–191.[11]

**Mechanik:** strassen baut zwar fn_index auf, verwendet ihn danach aber nicht. Die einzigen Zweige behandeln ast.ImportFrom und ast.Import; keine ast.Call-Auswertung und keine Kante art='aufruf' existiert im Rückgabepfad. Bei from . import nachbar wird das importierte Alias-Ziel nicht aufgelöst. Das Grenzmaß Zyklen hat zudem eine zweite, textbasierte Ableitung über Zeilen-Substringsuche statt denselben AST-Graphen.

**Folge:** Aufrufgraph, Bereichsabhängigkeiten und Wirkungskreis können unvollständig sein; Kommentar-/Stringtreffer können gleichzeitig die Zyklenzahl verfälschen. Eine Anzahl gespeicherter Straßen beweist keine Vollständigkeit.

**Beweisgrenze:** Keine unabhängige Zählung eines Werkgraphen ausgeführt; keine tatsächliche Zahl fehlender Kanten behauptet.

### A06 · Vertragsableitung liefert keine Grenzzusicherungen und blendet eigene abgeleitete Verträge aus

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Landkarte

**Masterprompt F6:** Z. 128–132.[1]
**Direkter Bezug 2a:** 6.

**Quellstellen:**
- `/root/biotop/biotop/organe/landkarte.py` — Z. 42–54, 128–150, 230–255.[3]
- `/root/biotop/biotop/kern/datenbank.py` — Z. 50–52.[12]

**Mechanik:** Stufe 3 enthält nur kn.args.args; positional-only, keyword-only, Varargs, Defaultwerte und Annotationen fehlen. Zweck ist nur die erste Docstringzeile, sonst leer. vertraege_ableiten übernimmt vorhandene Docstring-Aufzählungen oder hängt Signatur/Zweck aneinander; ohne Docstring steht 'ohne Beschreibung'. Grenzpartner, Eingabe-/Ausgabe-/Nebenwirkungszusicherungen werden nicht abgeleitet. sicht liest ausdrücklich nur herkunft='docstring', obwohl sie abgeleitete Verträge ankündigt.

**Folge:** Wo ein Werk keine expliziten Verträge besitzt, erhält der Schwarm gerade keine belastbar abgeleiteten Grenzzusicherungen.

**Beweisgrenze:** Explizite Vertragstests existieren als separates Organ; dies widerlegt deren Existenz nicht, sondern betrifft den zugesagten Landkarten-Fallback.

### A07 · Landkarte wird nach Veränderungen nicht konsistent aktualisiert; alte Einträge bleiben sichtbar

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Landkarte, Lazarus

**Masterprompt F6:** Z. 131–132, 212.[1]

**Quellstellen:**
- `/root/biotop/biotop/organe/landkarte.py` — Z. 154–183, 192–255.[3]
- `/root/biotop/biotop/lauf.py` — Z. 70–77, 316–356.[6]
- `/root/biotop/biotop/organe/lazarus.py` — Z. 90–110.[13]
- `/root/biotop/biotop/organe/genesis.py` — Z. 93–114.[7]

**Mechanik:** bauen löscht Straßen/Verträge, aber entfernt keine Landkarten-Zeilen für weggefallene Dateien oder Bereiche; Einträge werden nur upserted. Die Generation schreibt neue Dateien und archiviert sie ohne Aufruf von landkarte.bauen. Rueckkehr markiert lediglich Stufe <=2 als veraltet; sicht prüft keine Prüfsumme und liest auch alte Stufe-3-Inhalte. Genesis mischt diese Daten mit frisch gelesenen Quelldateien. Der Landkartenpfad enthält auch keinen Chunking-/Embedding-/Suchindex des in F6 vorgesehenen Aktenschranks.

**Folge:** Der Schwarm kann alte Signaturen und Verträge neben neuer Implementierung sehen; die Kennzeichnung 'veraltet' bewirkt allein keine Aktualisierung.

**Beweisgrenze:** Ein externer Aufrufer kann neu kartieren; im gelesenen Generations-/Rückkehrpfad ist das nicht erzwungen. Kein globaler Nachweis, dass außerhalb der geprüften Module kein alter Aktenschrank existiert.

### A08 · Generation minus eins und Generation 0 sind keine erzwungenen Startvoraussetzungen

**Status:** statisch belegt · **Priorität:** kritisch · **Organe:** Maß, Generation 0, Eichung

**Masterprompt F6:** Z. 104, 159–173, 255–258.[1]
**Direkter Bezug 2a:** 2.

**Quellstellen:**
- `/root/biotop/biotop/lauf.py` — Z. 54–115, 133–166, 557–616.[6]
- `/root/biotop/biotop/__main__.py` — Z. 34–64.[5]
- `/root/biotop/pruefung/vorspann.py` — Z. 15–56.[14]

**Mechanik:** mass_einfrieren setzt den Lauf unmittelbar auf bereit und Generation 0 auf angenommen, ohne Mutantenquote oder Eichungsbeleg zu lesen. generation kontrolliert Status und Freigabe, nicht Eichung/Mutantenfang. Der separate Vorspann erwartet bereits ein eingefrorenes Maß, bewertet Funde vor den vier Proben und schreibt 'Lauf startet' nur als Berichtstext. Es fehlt ein benannter CLI-Vorspann-Befehl. Bei fehlenden Tests stoppt einlegen vor dem Setzen von werk_id; das vorgeschlagene gen0 dereferenziert aber genau diese werk_id.

**Folge:** Die Reihenfolge aus F6 ist umgehbar und beim testlosen Werk über den vorgeschlagenen Standardweg nicht ausführbar. Ein falsch/gar nicht geeichtes Messgerät kann für Generation 1 benutzt werden.

**Beweisgrenze:** Nicht behauptet wird, dass konkrete historische Läufe ihren externen Vorspann ausgelassen haben. Die fehlende Kernvorbedingung ist statisch belegt.

### A09 · Einfrieren ist überschreibbar; Bestätigung und Messgerätstand sind nicht versiegelt

**Status:** statisch belegt · **Priorität:** kritisch · **Organe:** Maß, Kernschutz

**Masterprompt F6:** Z. 86, 173, 270–279.[1]

**Quellstellen:**
- `/root/biotop/biotop/lauf.py` — Z. 80–115, 146–150, 401–406.[6]
- `/root/biotop/biotop/organe/verfassung.py` — Z. 24–40.[15]
- `/root/biotop/biotop/__main__.py` — Z. 40, 100–104.[5]

**Mechanik:** mass_einfrieren hat weder 'bereits eingefroren'- noch Laufstatus-/Autorisierungsprüfung. Es ersetzt mass und Generation-0-Datensatz desselben Laufs und ruft denselben Snapshot-Schlüssel auf. bestaetigt_von ist ein frei gelieferter String. Die Werkverfassung wird ebenfalls per INSERT OR REPLACE ohne Laufbindung/Änderungswache eingelegt. Das eingefrorene JSON enthält keine Prüfsummen von Messskript, Referenzlast, Ankläger oder Nischenregeln; generation liest die Referenzlast erneut aus dem aktuellen Kern. Auch die Freigabeidentität beruht auf startswith('philipp'), nicht einer festen Rolle.

**Folge:** Maß-/Messgerät-/Verfassungsänderungen erzwingen weder Abbruch noch einen neuen Lauf; die behauptete Unverhandelbarkeit ist keine technische Invariante.

**Beweisgrenze:** Kein eingefrorenes Maß geändert. Ein freier CLI-String ist bei vertrauenswürdigem Betreiber kein Beleg für tatsächlichen Missbrauch; der Schutzmechanismus selbst fehlt.

### A10 · Gemessene Rauschtoleranzen, Bereichssperren und Maschinenvorbehalt erreichen die Auswahl nicht

**Status:** statisch belegt · **Priorität:** kritisch · **Organe:** Eichung, Maß, Messgerät

**Masterprompt F6:** Z. 105, 153, 161–162.[1]
**Direkter Bezug 2a:** 3, 5.

**Quellstellen:**
- `/root/biotop/biotop/organe/eichung.py` — Z. 111–147, 150–217.[16]
- `/root/biotop/biotop/kern/messgeraet.py` — Z. 401–455, 143–166.[11]
- `/root/biotop/biotop/lauf.py` — Z. 193–224.[6]
- `/root/biotop/biotop/organe/landkarte.py` — Z. 33–35.[3]
- `/root/biotop/biotop/kern/referenzlast/logmuehle.py` — Z. 8–21, 24–53.[17]

**Mechanik:** rauschmessung extrahiert ausschließlich laufzeit_ms, nicht jedes Grenzmaß. Das Ergebnis wird gespeichert/zurückgegeben, aber der Generationsloop erzeugt für alle mass.bereiche Kandidaten. urteil_f2 ruft grenzen_f2 ohne dessen rauschtoleranz-Argument; damit bleibt der feste Fallback aktiv. Bauzeit erhält zusätzlich eine feste absolute Zugabe. Maschinenvorbehalte bleiben Rückgabedaten der Eichung, kein Feld der späteren Messungen. Aussetzer werden mit [b] statt der ursprünglichen Bereichsliste nachgemessen: bei logmuehle teilt _zeilen(n) einen Cache. In der alphabetisch sortierten Komplettmessung initialisiert last_ausgabe ihn zuerst per _zeilen(800); eine isolierte Nachmessung etwa von filtern verwendet dagegen _zeilen() mit Standardargument n=4000.

**Folge:** Das Eichorgan kann ein Messproblem ausweisen, ohne den betreffenden Produktionspfad zu sperren oder dessen Zahlen zu markieren; zudem kann die Nachmessung eine andere Last messen.

**Beweisgrenze:** Die Rauschformel selbst wurde nicht als fehlend bezeichnet; ihre Kernanbindung und der Geltungsbereich fehlen. Keine neue Rauschmessung ausgeführt.

### A11 · Eichproben bestehen teilweise aus falschen Gründen; die Normprobe liest das falsche Feld

**Status:** statisch belegt · **Priorität:** kritisch · **Organe:** Eichung, Messgerät

**Masterprompt F6:** Z. 103–108, 163–169, 356–359.[1]
**Direkter Bezug 2a:** 6.

**Quellstellen:**
- `/root/biotop/biotop/organe/eichproben.py` — Z. 50–106, 157–215.[18]
- `/root/biotop/biotop/organe/aegis.py` — Z. 474–492.[9]

**Mechanik:** Nebenwirkung legt nur A lahm: der angekündigte messbare Gewinn in B wird nicht gebaut und nicht geprüft; jeder Ablehnungsgrund mit dem Namen A reicht. Die Normprobe greift auf u.get('masse') zu, obwohl Aegis sein Urteil unter 'mass' hält; der Fallback macht daraus Zuwachs 0 und leeren Testbestand. Sie kann so ohne Normnachweis bestehen. Die Vertragsprobe akzeptiert beliebige Ablehnung. Ihr Eingriff benutzt weiterhin quelle.replace('def ...'), obwohl F6 Textanker ausschließt. Der Vollersetzungs-Diff wird bei großen Dateien schon von der Neuschreibungsregel abgefangen.

**Folge:** Ein grüner Vier-Proben-Bericht beweist die geforderten Wirkmechanismen nicht. Gerade die Normprobe ist durch ihre Defaultwerte entwertet.

**Beweisgrenze:** Kein Probe-Kandidat eingeschleust. Nicht alle Proben sind wirkungslos: die Regressionsprobe verlangt ausdrücklich 'Regression je Test' und einen Testnamen.

### A12 · Eichgegenstand kann trotz unbrauchbarer Pfadangabe auf einen Nebenvertrag ausweichen

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Eichung

**Masterprompt F6:** Z. 108, 167–169, 394–396.[1]
**Direkter Bezug 2a:** 6.

**Quellstellen:**
- `/root/biotop/biotop/organe/eichgegenstand.py` — Z. 34–80, 105–159, 160–199.[19]

**Mechanik:** Eine nichtleere tragender_pfad-Liste gilt sofort als ausdrückliche Angabe, auch wenn kein angegebenes Paar zu den vorhandenen Verträgen passt. Dann erhalten alle echten Paare Gewicht 0 und die Vertragsgröße entscheidet trotzdem. Ein vorhandenes Siegel wird allein am Fortbestehen und Hash der Vertragsdatei erkannt; Existenz der beiden Bereiche und Gültigkeit des tragenden Pfads werden vor dem Frühreturn nicht neu geprüft. Bei Hashwechsel wird der alte Hash nur verkürzt in Befund/Protokolltext getragen.

**Folge:** Bei Betriebszwecken kann eine formal vorhandene, aber sachlich wirkungslose Angabe das verlangte Warten umgehen; das Siegel bestätigt eine Datei, nicht den weiter bestehenden tragenden Pfad.

**Beweisgrenze:** Der Normalfall ganz fehlender Regeln wird korrekt mit wartet=True abgewiesen. Kein versiegelter Gegenstand in der Datenbank verändert.

### A13 · Eichproben hinterlassen lernwirksame Ansagen und Immunfunde im geprüften Bestand

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Eichung, Kernschutz

**Masterprompt F6:** Z. 106, 219.[1]
**Direkter Bezug 2a:** 4, 6.

**Quellstellen:**
- `/root/biotop/biotop/organe/eichproben.py` — Z. 128–138, 157–171, 217–224.[18]
- `/root/biotop/biotop/organe/aegis.py` — Z. 302–331, 394–407, 626–668.[9]
- `/root/biotop/biotop/organe/gedaechtnis.py` — Z. 123–166, 285–294, 427–437.[20]
- `/root/biotop/pruefung/vorspann.py` — Z. 28–56.[14]

**Mechanik:** Die Proben setzen ist_probe=1 und die drei Gedächtnis-Eintrittsstellen beachten das. Der unmittelbar benutzte Aegis-Pfad übernimmt dieses Merkmal aber nicht in seine Ansage-/Immunaufnahme. Ansagen und ggf. neue Fund-/Normzeilen werden unter echter lauf_id/werk_id geschrieben; bisherige_behauptungen liest sie später ohne Probenausschluss. Weder proben noch vorspann stellen diesen Bestand nach jeder Probe wieder her. Fund-Neubewertung erfolgt sogar vor den Proben.

**Folge:** Die Prüfung verändert den Vorrat, gegen den nächste Proben und spätere Angriffe entscheiden. Die enge Probensperre der drei Gedächtnisse behebt diese zusätzliche Kontamination nicht.

**Beweisgrenze:** Dass eine konkrete Probe tatsächlich einen neuen Immunfund erzeugte, wurde nicht nachgemessen. Der Ansageschreibpfad und fehlende Rücknahme sind belegt.

### A14 · Fund-Neubewertung verwechselt Fehlermeldungen mit Abstürzen im Werk und konserviert unbelegte Funde

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Fund-Neubewertung, Messgerät

**Masterprompt F6:** Z. 103, 107, 164, 197, 222.[1]
**Direkter Bezug 2a:** 1, 5.

**Quellstellen:**
- `/root/biotop/biotop/organe/fundpruefung.py` — Z. 26–43, 46–90.[21]
- `/root/biotop/biotop/organe/aegis.py` — Z. 75–106, 589–608.[9]

**Mechanik:** _ausfuehren beurteilt 'besteht' durch Textfragmente und 'absturz_im_werk' durch Error/Exception ohne AssertionError; Paketpfad, Traceback-Ort und Returncode gehen nicht in den Absturzbeleg ein. Ein Import- oder testinterner Fehler kann dadurch wie ein Werkabsturz wirken. Anders als der Aegis-JUnit-Pfad wird nicht dieselbe Ortsableitung verwendet. Ein fallender Altbestand mit status='offen', ohne Absturz und ohne Bezug bleibt im else erneut offen statt offen_norm. Das optionale bereiche-Argument begrenzt den Scan nicht.

**Folge:** Die Neubewertung kann gerade die Norm-/Infrastrukturfehler zu Funden machen oder als solche erhalten, die F6 mechanisch ausschließen wollte.

**Beweisgrenze:** Keine vorhandenen Funde ausgeführt oder umklassifiziert. Der gemeinsame Vertragsverweis-Helper ist korrekt wiederverwendet; die Absturzableitung dagegen nicht.

### A15 · Mutantenfang zählt jeden Prozessfehler und kann ohne gültigen Gegenstand bestehen

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Generation 0

**Masterprompt F6:** Z. 90, 103, 171–173.[1]
**Direkter Bezug 2a:** 1.

**Quellstellen:**
- `/root/biotop/biotop/organe/generation0.py` — Z. 108–113, 180–200, 243–256.[22]
- `/root/biotop/biotop/lauf.py` — Z. 557–616.[6]
- `/root/biotop/biotop/__main__.py` — Z. 53.[5]

**Mechanik:** _testlauf verwendet ausschließlich e.rc != 0 als gefangen; es unterscheidet weder echte mutantenspezifische Testabweichung, bereits roten Ausgang, keine Tests, Importfehler noch Docker-Fehler. Der Testbau verwendet für faengt denselben RC-Kurzschluss. generation0 erzwingt keinen vorher grünen unmutierten Bestand und keine positive Zahl nichtäquivalenter Mutanten. Bei leerer Mutantenliste wird das Anteilziel zu 0 und erreicht ist wahr. Das frei wählbare --ziel hat zudem keine Mindestgrenze aus F6.

**Folge:** Eine hohe Fangquote kann Infrastruktur- oder Basisfehler zählen; eine Prüfung ohne Mutanten kann als erreicht zurückgegeben werden.

**Beweisgrenze:** Keine Quote neu gemessen und keine leere Probe ausgeführt. Die beschriebenen Bedingungen folgen aus dem Kontrollfluss.

### A16 · Äquivalenz ist Rastergleichheit ohne Codebegründung; fehlende Beobachtung wird durch einen Regexfehler gleichgesetzt

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Generation 0

**Masterprompt F6:** Z. 90, 108, 172.[1]
**Direkter Bezug 2a:** 6.

**Quellstellen:**
- `/root/biotop/biotop/organe/generation0.py` — Z. 116–176.[22]

**Mechanik:** Das Beobachtungsskript meldet bei fehlendem beobachten() 'AEQ keine-beobachtung' und beendet sich erfolgreich. Der Regex AEQ (\w+) liest davon nur 'keine'; die spätere Gleichheitsprüfung auf 'keine-beobachtung' kann deshalb nie greifen. Ein vom Testlauf nicht gefangener Mutant kann dann aufgrund zweimal 'keine' als äquivalent aussortiert werden. Auch mit echter Beobachtung wird eine bloße Hashgleichheit auf dem Raster plus grünen Tests zur Äquivalenz erklärt; die 'Codebegründung' wiederholt nur Mutationsbeschreibung/Ort und untersucht keine Verhaltensäquivalenz.

**Folge:** Blinde Flecken können vor der Quote aus dem Nenner verschwinden, obwohl der geforderte Äquivalenzbeleg fehlt.

**Beweisgrenze:** Die beiden mitgelieferten Referenzlasten besitzen beobachten(); der Regexfehler betrifft den unterstützten Fallbackpfad und ist kein Nachweis, dass bestehende Mutanten dort falsch aussortiert wurden.

### A17 · Testmessung und Pareto verlieren Identitäten, Skips und Fehler hinter dem Abschneidelimit

**Status:** statisch belegt · **Priorität:** kritisch · **Organe:** Messgerät, Maß

**Masterprompt F6:** Z. 90, 108, 150–152.[1]
**Direkter Bezug 2a:** 6.

**Quellstellen:**
- `/root/biotop/biotop/kern/messgeraet.py` — Z. 66–95, 129–140, 196–216, 277–297.[11]

**Mechanik:** Testzuordnung erfolgt über Dateinamenskonventionen. Als Dateiname wird das letzte classname-Segment benutzt; bei Klassen-Tests ist das häufig der Klassenname statt der Testdatei. Nicht zugeordnete Ergebnisse landen unter None und werden keinem Bereich zugerechnet. <skipped> wird wie bestanden behandelt. pytest_rc und ein leerer Testbestand machen eine vorhandene Messausgabe nicht ungültig. tests_fehlgeschlagen_liste wird auf die ersten 100 Einträge gekürzt; Pareto je Test bildet danach nur die Differenz dieser gekürzten Listen.

**Folge:** Kernmaß und Regressionsentscheidung sind bei fremden Testlayouts bzw. großen roten Beständen nicht vollständig. Ein neuer Fehlschlag jenseits des gespeicherten Ausschnitts kann dem Einzeltest-Pareto fehlen.

**Beweisgrenze:** Keine konkrete Regression in einem angenommenen Lauf behauptet. Die F6-Regel 'je Test' ist vorhanden, aber ihr Eingang ist nicht verlustfrei.

### A18 · Fehlgeschlagene Sicherheits- und Totcodeanalyse kann als Nullbefund in gültige Messungen eingehen

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Messgerät

**Masterprompt F6:** Z. 90, 150–152, 157, 320.[1]

**Quellstellen:**
- `/root/biotop/biotop/kern/messgeraet.py` — Z. 97–140, 208–216, 265–289.[11]

**Mechanik:** Wenn Bandits Ausgabe nicht als JSON parsebar ist, liefert bandit() 0 Punkte, leere Befunde und einen Fehlertext. Rückgabecode und JSON-Fehlerliste bestimmen die Messgültigkeit nicht. vulture() ignoriert ebenfalls rc/stderr und zählt lediglich passende stdout-Zeilen. Der übergeordnete Pfad setzt gueltig=True, sobald ein Messmarker vorhanden ist; die Fehlerfelder werden von Kernmaß und Pareto nicht ausgewertet. Eine eigenständige Abhängigkeitsprüfung ist im Messskript nicht implementiert.

**Folge:** Werkzeugausfall kann wie das Verschwinden eines Befundes oder toten Codes aussehen und dadurch das harte Maß verbessern.

**Beweisgrenze:** Keine Scannerinstallation geändert und kein Ausfall erzeugt. Die Fehlerpfade selbst sind der Beleg.

### A19 · Speichergrenzmaß und konfigurierbares Klassenmaß fehlen im tatsächlichen Mess-/Auswahlpfad

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Maß, Messgerät

**Masterprompt F6:** Z. 153–156, 397–406.[1]

**Quellstellen:**
- `/root/biotop/biotop/kern/messgeraet.py` — Z. 39–44, 129–166, 265–274, 378–445.[11]
- `/root/biotop/biotop/lauf.py` — Z. 93–106.[6]
- `/root/biotop/biotop/organe/kammer.py` — Z. 23–25, 63–73.[10]

**Mechanik:** Die Messwertschema-/Bestwert-/Grenzlisten enthalten keinen Speicherverbrauch; Docker setzt nur ein absolutes Kammerlimit. kernmass_f2_bereich ist fest auf Fehlschläge, Sicherheit und Totcode verdrahtet. mass_einfrieren liest aus den Werkregeln nur Tauschparameter für seine Maßdefinition, keinen Klassenmaß-Adapter. Ein Ertrags-/Verlustmaß aus der Verfassung würde nicht an der Auswahl teilnehmen.

**Folge:** Speicherzunahmen unterhalb des Containerlimits bleiben ungemessen; die in F6 vorgesehene Werkklassen-Erweiterung und das Handels-Kernmaß sind im heutigen Kern nicht anschließbar.

**Beweisgrenze:** Keine Aussage, Phase 4 sei bereits freigegeben oder gestartet. Dies ist eine noch nicht gebaute F6-Fähigkeit, nicht der Nachweis eines misslungenen Handelslaufs.

### A20 · Unmessbare Laufzeit wird übersprungen; die Geschwindigkeitsannahme verwendet weiter eine feste Schwelle

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Messgerät, Maß

**Masterprompt F6:** Z. 90, 153–155, 161–162.[1]
**Direkter Bezug 2a:** 3.

**Quellstellen:**
- `/root/biotop/biotop/kern/messgeraet.py` — Z. 143–166, 208–216, 419–433, 464–478.[11]
- `/root/biotop/biotop/lauf.py` — Z. 298–303.[6]

**Mechanik:** Eine fehlende last_<bereich>-Funktion oder eine Ausnahme in der Last ergibt None, aber keine ungültige Gesamtmessung. grenzen_f2 prüft Laufzeit nur, wenn Ausgang und Kandidat beide truthy sind; None und 0 umgehen diesen Teil. Die schnelle Nische und die Generalprobe verlangen unabhängig von gemessener Bereichsstreuung den Faktor 0.85 für einen Gewinn. Damit kann eine defekte oder stark rauschende Laufzeit ihren Grenz-/Gewinnmaßcharakter verlieren.

**Folge:** Der vorhandene Referenzlast-Dateiname genügt, obwohl einzelne Bereichslasten fehlen/abstürzen können; messbare Verschlechterung und unmessbares Ergebnis werden nicht gleich streng behandelt.

**Beweisgrenze:** Kein neuer Lastlauf; vorhandene Funktion im Ausgang wird nicht als Gewähr für die Last am Kandidaten gewertet.

### A21 · Sicherheitsgewinn wird auch ohne verpflichtenden Umgehungs-Immuntest anerkannt

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Maß, Messgerät

**Masterprompt F6:** Z. 150–157, 192.[1]

**Quellstellen:**
- `/root/biotop/biotop/organe/aegis.py` — Z. 161–175, 678–699.[9]
- `/root/biotop/biotop/kern/befundklassen.py` — Z. 14–74.[23]
- `/root/biotop/biotop/kern/messgeraet.py` — Z. 265–289, 448–457.[11]

**Mechanik:** Befundklassen-Tests werden nur gebaut, wenn die Verfassung einen Einstieg kennt und der Katalog Code liefert. Bei fehlendem Einstieg oder unbekannter/umgehungsloser Klasse wird still continue/None verwendet. Die spätere Auswahl bewertet dennoch jede Verringerung von sicherheit_punkte als Kernmaßgewinn und Tauschberechtigung; es gibt keine Kopplung 'verschwundener Befund -> bestandener und aufgenommener Klassen-Immuntest'. Bekannte Klassen sind nur ein begrenzter Katalog.

**Folge:** Die harte Bedingung 'behoben heißt verschwunden UND Umgehung im Werk' ist nicht für alle Sicherheitsbefunde durchgesetzt.

**Beweisgrenze:** Bei konfigurierten Einstiegen kann der vorgesehene Schutz wirken. Ein bestimmter historisch angenommener Sicherheitsfix wurde hier nicht erneut ausgeführt.

### A22 · Budgetvorprüfung ist keine obere Kostengrenze und reserviert keine parallelen Aufrufe

**Status:** nur Risiko · **Priorität:** hoch · **Organe:** Kasse, Anbieterschicht

**Masterprompt F6:** Z. 92, 241–242.[1]

**Quellstellen:**
- `/root/biotop/biotop/anbieter/__init__.py` — Z. 48–49, 113–136.[24]
- `/root/biotop/biotop/kern/kasse.py` — Z. 88–136, 180–199.[25]

**Mechanik:** Eingabetoken werden aus len(system+nutzer)//3 geschätzt, ohne modellgenauen Tokenizer oder Protokolloverhead. Die Vorprüfung liest bereits gebuchte Kosten; vor dem Netzaufruf wird keine atomare Kostenreservierung geschrieben. Zwei unabhängige Prozesse könnten denselben Restbetrag sehen. Generation_vorpruefung benutzt nur die teuerste abgeschlossene Generation, bei fehlender Historie 0.

**Folge:** Ein realer Aufruf kann teurer sein als die Schätzung; gleichzeitige Aufrufe können zusammen den freigegebenen Rest überschreiten. Das harte 'nie danach' ist durch diese Schätzung nicht garantiert.

**Beweisgrenze:** Kein Tokenvergleich, kein Parallelversuch und keine Überschreitung gemessen. Daher ausdrücklich Risiko statt behaupteter tatsächlicher Budgetverletzung.

### A23 · Fehlende Nutzungsdaten werden als Nullkosten gebucht; fehlgeschlagene Aufrufe fehlen im Kassenzähler

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Kasse, Anbieterschicht

**Masterprompt F6:** Z. 90–92, 241–242.[1]

**Quellstellen:**
- `/root/biotop/biotop/anbieter/__init__.py` — Z. 87–98, 126–136.[24]
- `/root/biotop/biotop/kern/kasse.py` — Z. 69–85, 124–136.[25]

**Mechanik:** Fehlt usage oder ein Tokenfeld, setzt der Adapter prompt_tokens/completion_tokens auf 0. Diese Werte werden ohne Kennzeichnung als fehlende Daten regulär gebucht. Bei AnbieterFehler wird nur modell.fehler protokolliert und vor kasse.buchen abgebrochen; COUNT(*) aus kasse bedeutet daher erfolgreiche Buchungen, nicht alle versuchten Modellaufrufe. Es existiert kein eigener ungeklärter Abrechnungsposten für einen nach Versand abgebrochenen Aufruf.

**Folge:** Kostenstand und Aufrufzahl können unterzählen; '0' ist hier unter Umständen eine Defaultzahl statt gemessener Verbrauch.

**Beweisgrenze:** Keine reale Providerrechnung abgeglichen. Ob ein bestimmter fehlgeschlagener Aufruf kostenpflichtig war, bleibt offen.

### A24 · Anbieterschicht ist OpenRouter-only; eigene Kontingentgrenze und ausschließliche Server-Umgebung fehlen

**Status:** statisch belegt · **Priorität:** mittel · **Organe:** Anbieterschicht, Kasse

**Masterprompt F6:** Z. 242, 287–290, 312, 322.[1]

**Quellstellen:**
- `/root/biotop/biotop/anbieter/__init__.py` — Z. 36–45, 101–120.[24]
- `/root/biotop/biotop/kern/kasse.py` — Z. 33–35, 69–85, 88–135.[25]
- `/root/biotop/biotop/organe/mentor.py` — Z. 24.[26]
- `/root/biotop/biotop/organe/jury.py` — Z. 19.[27]

**Mechanik:** adapter() akzeptiert nur openrouter; eine zweite Adapterimplementierung oder ein Port für Aboanbieter existiert hier nicht. kontingent ist nur ein optionaler Buchungsmarker, aber kein in vorpruefung geprüftes eigenes Limit; aufrufen reicht den Marker nie weiter. Mentor benutzt ebenfalls tokenabgerechnetes OpenRouter, die Jury Schnellmodelle. _schluessel liest bei fehlender Umgebungsvariable ausdrücklich /root/.hermes/.env statt ausschließlich Servervariablen zu verlangen.

**Folge:** Mehrere Modellhersteller sind vorhanden, aber nicht die in F6 zugesagte austauschbare Mehradapter-/Kontingentarchitektur. Die Geheimnisquelle greift auf Hermes-Dateikonfiguration zurück.

**Beweisgrenze:** Keine .env-Datei gelesen, kein Schlüssel ausgegeben, kein Katalog abgefragt. Kasse Z.33–35 nennt selbst eine spätere/spezifische Philipp-Vorgabe zum Träger; deren tatsächliche Autorisierung wurde nicht unabhängig geprüft. Als F6-Abweichung, nicht als bewiesener Ungehorsam von Hermes, eingeordnet.

**Hermes-Bezug:** Direkter, belegter Kopplungspfad an Hermes: _schluessel mit Dateifallback. Keine Spekulation über aktive Hermes-Modelle oder aktuelle Anbieterpreise.

### A25 · Eichkosten: Kammerläufe werden konstant behauptet; dieselben Modellkosten bleiben in der Laufsumme

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Eichung, Kasse

**Masterprompt F6:** Z. 110, 165, 426.[1]

**Quellstellen:**
- `/root/biotop/biotop/organe/eichproben.py` — Z. 157–169.[18]
- `/root/biotop/biotop/organe/aegis.py` — Z. 531–533, 575–578, 672–678.[9]
- `/root/biotop/biotop/organe/eichung.py` — Z. 49–87, 90–108.[16]
- `/root/biotop/biotop/kern/kasse.py` — Z. 69–85, 139–158.[25]

**Mechanik:** lauf_probe setzt kammerlaeufe fest auf 1 und bucht genau 1, unabhängig davon, ob Aegis früh abbricht oder Basis/Kandidat und Zusatztests jeweils eigene Kammern aufruft. Modellkosten werden dagegen korrekt als Kassenstanddifferenz erfasst. kosten_buchen legt eine zweite eichkosten-Zeile an, entfernt/markiert aber die ursprüngliche kasse-Buchung nicht. stand und bericht_md summieren weiterhin alle kasse-Zeilen des Laufs, während kosten_text behauptet, Eichkosten seien nicht enthalten.

**Folge:** Die behauptete Zahl der Kammerläufe ist keine Messung; reine Laufsumme und Eichsumme sind ohne Abzug nicht getrennt. Ein Vergleich historischer Vorspannkosten darf diese Zahlen nicht ungeprüft übernehmen.

**Beweisgrenze:** Keine tatsächliche Zahl je historischem Probenlauf neu bestimmt. Die statische Konstante und widersprüchlichen Summenpfade sind nachgewiesen.

### A26 · Unantastbarer Kern und unveränderliches Protokoll sind nicht technisch getrennt

**Status:** statisch belegt · **Priorität:** kritisch · **Organe:** Kernschutz, Kasse, Lazarus

**Masterprompt F6:** Z. 270–279.[1]

**Quellstellen:**
- `/root/biotop/biotop/kern/datenbank.py` — Z. 1–5, 18–82.[12]
- `/root/biotop/biotop/kern/protokoll.py` — Z. 19–46.[28]
- `/root/biotop/biotop/lauf.py` — Z. 13–15.[6]
- `/root/biotop/biotop/organe/genesis.py` — Z. 137–141.[7]
- `/root/biotop/biotop/dienst.py` — Z. 233–237.[29]

**Mechanik:** Kern, Schwarm, Dienst und Organe verwenden dieselbe SQLite-Verbindung bzw. dieselbe Datei im selben Import-/Prozessmodell. Die Datenbankschicht besitzt keine exklusive Kernrolle und keine Append-only-Trigger für das Protokoll. Die Hashkette schützt nur gegen unbegleitete Einzeländerung; ein Besitzer des Schreibrechts kann Zeilen/Kette neu schreiben oder am Ende entfernen, ohne externen Anker. Die eigene Modulbeschreibung bezeichnet die Rollentrennung als offen. Zudem wird die später benötigte ist_probe-Spalte nur im CREATE definiert; die Migration ergänzt allein vertraege.

**Folge:** Das F6-Schutzmodell 'eigener Prozess, eigene Rolle, kein Schreibpfad' ist nicht implementiert. Die vorhandene Hashprüfung ist ein Nachweismechanismus, keine Unveränderlichkeit.

**Beweisgrenze:** Weder Datenbank noch Protokoll geändert, keine Dienstrechte live erhoben. Das Migrationsproblem betrifft ältere Schemas; die gesicherte aktuelle DB wurde nicht als spaltenlos behauptet.

### A27 · Fremdcode kann innerhalb der Kammer Messskripte/Belege beeinflussen; Messausgabe ist nicht vertrauensgetrennt

**Status:** nur Risiko · **Priorität:** kritisch · **Organe:** Kammer, Messgerät, Kernschutz

**Masterprompt F6:** Z. 85, 173, 237–238, 270–279.[1]

**Quellstellen:**
- `/root/biotop/biotop/organe/kammer.py` — Z. 54–80.[10]
- `/root/biotop/biotop/kern/messgeraet.py` — Z. 79–85, 143–166, 196–216.[11]
- `/root/biotop/biotop/organe/aegis.py` — Z. 79–102.[9]

**Mechanik:** Die kopierten _messgeraet-Dateien werden zusammen mit dem Werk an UID 10001 übereignet und als ein rw-Verzeichnis eingebunden. Werkcode läuft in pytest-Subprozessen und bei Referenzlasten im selben Python-Prozess wie die Auswertelogik; Ergebnisse kommen aus beschreibbarer JUnit-Datei bzw. stdout-Markern. messen akzeptiert einen Marker ohne verifizierten Erzeuger und prüft e.rc bei vorhandenem Marker nicht. Keine getrennte schreibgeschützte Messgerätablage und kein authentischer Ergebnisübergang schützen diese Grenze.

**Folge:** Ein bewusst manipulierender Kandidat könnte Prüfwerkzeuge oder Ergebnisartefakte statt seiner Qualität verändern. Containerisolation allein garantiert nicht, dass die Messung unabhängig vom zu prüfenden Werk ist.

**Beweisgrenze:** Keine Ergebnisfälschung ausgeführt; deshalb Risiko. Positiv: Netzwerk, Ressourcen, Benutzer, Root-Dateisystem und Capabilities sind im Dockeraufruf tatsächlich begrenzt.

### A28 · Abbruch markiert die Datenbank, hält einen bereits laufenden Generationsprozess aber nicht vor dem nächsten Aufruf an

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Kernschutz, Kasse

**Masterprompt F6:** Z. 86, 92, 104, 281.[1]
**Direkter Bezug 2a:** 2.

**Quellstellen:**
- `/root/biotop/biotop/lauf.py` — Z. 133–170, 175–181, 359–393.[6]
- `/root/biotop/biotop/anbieter/__init__.py` — Z. 113–131.[24]
- `/root/biotop/biotop/kern/kasse.py` — Z. 88–121.[25]

**Mechanik:** abbrechen ändert Lauf-/Generationsstatus und protokolliert, sendet jedoch kein Stoppsignal. generation prüft den Status nur am Einstieg; ihr laufender Körper und die Anbieter-Vorprüfung lesen später kein Abbruchmerkmal. Ein anderer Prozess kann weiter aufrufen und mit abschluss sogar erneut bereit setzen. Ein bereits beendeter Lauf kehrt in abbrechen vor protokoll.schreiben zurück, obwohl die Rückgabe 'trotzdem protokolliert' sagt; ein nach Budget beendeter Lauf lässt sich dort auch nicht nachträglich als Satz-2-verworfen markieren.

**Folge:** Der benannte Befehl ist vorhanden, die Pflicht zum wirksamen Stoppen vor weiteren Modellaufrufen ist im nebenläufigen Betrieb nicht durchgesetzt.

**Beweisgrenze:** Kein laufender Prozess gestoppt und keine Nebenläufigkeit erzeugt. Der fehlende erneute Zustandscheck ist belegt; ein konkreter Weiterlauf wurde nicht gemessen.

### A29 · HTTP-Abbruchroute ruft eine nicht existierende Methode auf

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Kernschutz

**Masterprompt F6:** Z. 104, 246, 281.[1]
**Direkter Bezug 2a:** 2.

**Quellstellen:**
- `/root/biotop/biotop/dienst.py` — Z. 81–112, 233–237.[29]
- `/root/biotop/biotop/oberflaeche.py` — Z. 11–31.[30]

**Mechanik:** do_POST liest den Body bereits mit _json_body. Im Abbruchzweig ruft es danach self._json() auf, obwohl Handler nur _json_body definiert und BaseHTTPRequestHandler diese Biotop-Methode nicht anbietet. Der Aufruf liegt vor dem try/except, daher wird L.abbrechen nicht erreicht. Ein Abbruch-Bedienelement ist auch nicht in ELEMENTE verdrahtet.

**Folge:** Die registrierte und beworbene HTTP-Abbruchroute ist im gelesenen Code defekt; der CLI-Befehl bleibt davon unberührt.

**Beweisgrenze:** Kein HTTP-Aufruf ausgeführt. Statischer Methoden-/Kontrollflussbeleg, keine erfundene HTTP-Statusausgabe.

### A30 · Lazarus überschreibt vorhandene Schnappschüsse; Annahme ist nicht ausfallsicher mit Archivierung gekoppelt

**Status:** statisch belegt · **Priorität:** kritisch · **Organe:** Lazarus, Kernschutz

**Masterprompt F6:** Z. 89, 207–213, 274–279.[1]

**Quellstellen:**
- `/root/biotop/biotop/organe/lazarus.py` — Z. 46–76.[13]
- `/root/biotop/biotop/lauf.py` — Z. 107–114, 316–356.[6]
- `/root/biotop/biotop/organe/gedaechtnis.py` — Z. 262–312.[20]

**Mechanik:** Snapshotnamen sind lauf_id/generation. Wiederholung benutzt git tag -f, öffnet dasselbe tar.gz mit w:gz und überschreibt die DB-Zeile per ON CONFLICT; das Archiv ist nicht append-only. Der Generationspfad schreibt zuvor Werkdateien, markiert Kandidaten angenommen und lässt art_merken einen kostenpflichtigen Musteraufruf machen, bevor Lazarus überhaupt sichert. Scheitert dieser Aufruf bzw. das Archivieren, gibt es keinen transaktionalen Rückbau des Werks. sicherstellen_repo überschreibt außerdem bei der Initialisierung die werkseigene .gitignore.

**Folge:** Ein Zustand kann verändert bzw. als angenommen markiert sein, ohne neuen rückholbaren Schnappschuss; vorhandene Historie kann unter demselben Schlüssel ersetzt werden.

**Beweisgrenze:** Kein Archiv überschrieben und kein Ausfall provoziert. Belegt sind Schreibreihenfolge und Überschreiboperationen, nicht ein eingetretener Datenverlust.

### A31 · Rückkehr restauriert nicht den vollständigen Laufzustand und scheitert bei Prüfsummenabweichung nicht laut

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Lazarus, Landkarte

**Masterprompt F6:** Z. 89–90, 212–213.[1]
**Direkter Bezug 2a:** 2.

**Quellstellen:**
- `/root/biotop/biotop/organe/lazarus.py` — Z. 28–35, 83–110.[13]
- `/root/biotop/biotop/lauf.py` — Z. 423–434.[6]
- `/root/biotop/biotop/__main__.py` — Z. 84–89.[5]

**Mechanik:** Produktivrückkehr stellt Dateien per Git her und markiert nur spätere angenommene Generationen; Landkarte <=2 erhält 'veraltet', aber Straßen, Verträge und Stufe 3 werden nicht aus dem Stand n wiederhergestellt; laufende/vorgelegte Generationen werden von der Statuskorrektur nicht erfasst. Die Messwerte werden nur zurückgegeben. Eine abweichende Werkprüfsumme setzt stimmt=False, wirft aber keinen Fehler; CLI und Freigabe-Ablehnung behandeln die Rückgabe normal. Ein benannter Ablauf 'fehlerhafte Generation finden -> n-1 -> Immuntest -> n..n+k wiederholen' fehlt in den gelesenen Eintrittsstellen. Der Werkhash deckt Inhalte/Pfade, nicht ausführbare Dateimodi oder Symlinktyp ab.

**Folge:** Dateirückkehr und Lauf-/Messgerätrückkehr sind nicht dasselbe; eine festgestellte unvollständige Rückholung kann ohne Stopp fortgesetzt werden.

**Beweisgrenze:** Keinen Schnappschuss zurückgeholt. Keine tatsächliche Prüfsummenabweichung behauptet; auch abgelehnte Linien werden nicht pauschal als gelöscht bezeichnet.

### A32 · Nachgerechnete Verlaufskurve verwendet nicht durchgängig den Endtestbestand oder nur angenommene Generationen

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Maß, Lazarus

**Masterprompt F6:** Z. 107, 150–154, 245–246.[1]
**Direkter Bezug 2a:** 5.

**Quellstellen:**
- `/root/biotop/biotop/lauf.py` — Z. 437–475.[6]
- `/root/biotop/biotop/kern/messgeraet.py` — Z. 208–223.[11]
- `/root/biotop/biotop/__main__.py` — Z. 71–79.[5]
- `/root/biotop/biotop/dienst.py` — Z. 199–207.[29]
- `/root/biotop/biotop/oberflaeche.py` — Z. 104–114.[30]

**Mechanik:** kurve_nachrechnen selektiert alle Lazarus-Einträge und den numerisch letzten Snapshot ohne Join auf angenommene/freigegebene Generationen. Der Endtestbestand wird nur mit tests.glob('test_*.py') ermittelt: Unterverzeichnisse/Verträge fehlen. Die Dateien werden über den alten Bestand gelegt, nicht als vollständiger Ersatz; weggefallene alte Tests verbleiben. Außerdem bleibt messung.kernmass die historische F1-Formel, und CLI sowie HTTP-Feld kernmass geben dieses Feld aus, während die Auswahl F2 verwendet. Die Web-Kurve berechnet F2 separat aus Bereichswerten.

**Folge:** Die Pflichtkurve kann eine andere Population/Testgrundlage messen; gleich benannte Kennzahlen in Ausgaben stehen für verschiedene Formeln.

**Beweisgrenze:** Keine Kurve nachgerechnet. Nicht behauptet wird, die Web-Kurve verwende F1; genau dort ist die lokale F2-Neuberechnung vorhanden.

### A33 · Späteres F7-Bauteil C kann einen neuen Fund wegen seiner eigenen vorherigen Ansage sperren

**Status:** statisch belegt · **Priorität:** hoch · **Organe:** Messgerät, Kernschutz

**Masterprompt F6:** Z. 91, 195–197, 217–221.[1]
**Direkter Bezug 2a:** 6.

**Quellstellen:**
- `/root/biotop/biotop/organe/aegis.py` — Z. 325–331, 394–407, 423–463, 619–625, 650–668.[9]

**Mechanik:** _angriff schreibt die aktuelle neue Behauptung schon vor dem Testschreiben als aegis.ansage. aufnahmesperre fragt später bisherige_behauptungen erneut ab; diese Funktion enthält ausdrücklich auch alle angesagten Behauptungen desselben Laufs/Bereichs. Es gibt keinen Ausschluss des aktuellen Angriffs. Bei leerem Altvorrat und einem Test, dessen abgeleiteter Schlüssel der eigenen Ansage entspricht, steht sein Schlüssel deshalb nun im Vorrat und wird als Wiederholung abgewiesen. Fund- und Normaufnahme benutzen beide diesen Pfad.

**Folge:** Die spätere Aufnahmehärtung kann einen erstmals bestätigten Fehler an der Aufnahme seines Tests hindern. Eine Zählung 'gesperrt' belegt dabei nicht automatisch eine echte Alt-Doppelung.

**Beweisgrenze:** Keine neue Probe und keine Quote aus Lauf 25 berechnet. Der bedingte Selbstblock folgt direkt aus der Reihenfolge der Schreib-/Lesepfade.

**Versionsbezug:** Spätere Abweichung: C wurde nach dem F6-Ausgang hinzugefügt und nennt sich im Quelltext Fassung 7. Kein fehlendes F6-Bauteil behauptet; heutiger Code wird gegen Immunisierungs-/Belegregeln aus F6 geprüft.

### A34 · Historisch behoben: Laufzeitaggregation benutzt heute Median statt Minimum

**Status:** historisch behoben · **Priorität:** info · **Organe:** Messgerät

**Masterprompt F6:** Z. 105, 153, 161.[1]
**Direkter Bezug 2a:** 3.

**Quellstellen:**
- `/root/biotop/biotop/kern/messgeraet.py` — Z. 151–164, 300–325, 352–375.[11]
**Historischer Gegenbeleg:**
- `/root/gesamtstand-01/pruefung-a/historie/a41838c-eltern-messgeraet.py:151–158`[31]

**Mechanik:** Der gelesene historische Elternstand 908c03d1ef7f4cd836921a2540b65e15de6da762 aktualisiert best mit min(best,d). Der heutige Code sammelt drei Laufzeiten, sortiert und nimmt das mittlere Element. streuung trennt die Ebene zwischen Messungen und verwirft ebene!='zwischen'; rauschtoleranz_aus_werten benutzt diese Funktion. Git führt die Umstellung unter a41838c8449ef8af471e8b1d89fdeed0633d3619.

**Folge:** Die pauschale alte Kritik 'Minimum statt Median' trifft den heutigen Ausführungspfad nicht mehr. Sie darf nicht aus veralteten Kopfkommentaren oder Skills erneut als aktueller Defekt übernommen werden.

**Beweisgrenze:** Nur Quelltext-/Gitvergleich, keine Rauschkampagne. Die fehlende Weitergabe der Toleranz und Sperren bleibt ein separater aktueller Befund A10.

**Hermes-Bezug:** Die geladenen Biotop-Bauhinweise enthalten alte Versions-/Toleranzangaben; F6 und heutiger Quelltext haben hier Vorrang.

### A35 · Historisch behoben: Das in F6 noch offene Ansage-Bauteil ist heute implementiert

**Status:** historisch behoben · **Priorität:** info · **Organe:** Messgerät

**Masterprompt F6:** Z. 195, 386, 393.[1]

**Quellstellen:**
- `/root/biotop/biotop/organe/aegis.py` — Z. 334–420.[9]
**Historischer Gegenbeleg:**
- `/root/gesamtstand-01/pruefung-a/historie/7c73d403c18755dda26655c78ac7290c446d9f45-aegis.py:302–355`[32]

**Mechanik:** Am F6-Ausgang 7c73d403c18755dda26655c78ac7290c446d9f45 wird die Liste bisheriger Behauptungen nur in den Angriffsprompt eingebettet. Heute gibt es einen eigenen _ansage-Aufruf und vor dem Testschreiben einen deterministischen ansage-in-schon-Zweig. Der heutige Gitstand enthält damit ein nach F6 gebautes Bauteil; die historische Notiz 'noch nicht gebaut' ist kein aktueller Befund mehr.

**Folge:** Versionen sind getrennt: Existenz des Ansageorgans ist heute statisch belegt. Daraus folgt weder die vollständige Wirksamkeit noch eine bestandene Doppelungsquote.

**Beweisgrenze:** Keine Ankläger-/OpenRouter-Aufrufe. Aktuelle Risiken durch begrenzten Vorrat, Prüfbestandskontamination und F7-Selbstblock werden nicht durch diese Existenzfeststellung entkräftet.

**Versionsbezug:** F6-Ausgang vs. HEAD: im Modulbaum biotop änderten sich nur aegis.py und gedaechtnis.py; der Vergleich ist als Artefakt beigefügt.

## Integrität, Kosten und offene Prüfgrenze

Vorher-/Nachher-Vergleich: 37 von 37 überwachten Dateien unverändert in Inhalt, Größe und mtime (35 Python-Dateien, Dockerfile, gesicherte DB-Kopie). HEAD unverändert und Git-Arbeitsbaum sauber. Die neun erfassten Tabellenzähler der Kopie sowie deren Kassensumme blieben unverändert. Einzelbelege stehen in den Zustands- und Zählerdateien; dies ist keine Behauptung über die Live-Produktionsdatenbank, die nicht geöffnet wurde.

Zusätzlich ausgelöste Biotop-/OpenRouter-Aufrufe: 0; Kammerläufe: 0; zusätzliche Providerkosten solcher Aktionen: 0 €. Die Kosten des Trägermodells dieser Unterhaltung wurden nicht gemessen. Es wurden keine Schlüsselwerte gelesen oder ausgegeben. Siehe `KASSE.md`.

Nicht geleistet: dynamische Reproduktion, erneute Kalibrierung, Tor-Abnahme, vollständige Prüfung aller historischen Abschlussordner/Archive oder aktueller Dienstrechte. Belegte Codeabweichungen entkräften die jeweilige Implementierungsbehauptung; sie beweisen nicht rückwirkend, dass jeder frühere Lauf denselben Schaden hatte.

## Artefakte

Verbindliche Lieferfassungen sind `BEFUND.md` und `BEFUND.json`. `befunde-roh.json` ist die interne Eingabefassung, kein zweiter Ergebnisstand. `BELEGE.json` enthält die referenzierten Zeilen wörtlich; historische Gegenstände sind als getrennte Dateien abgelegt.

/root/gesamtstand-01/pruefung-a/BEFUND.md

/root/gesamtstand-01/pruefung-a/BEFUND.json

/root/gesamtstand-01/pruefung-a/BELEGE.json

/root/gesamtstand-01/pruefung-a/LESEABDECKUNG.json

/root/gesamtstand-01/pruefung-a/historischer-vergleich.json

/root/gesamtstand-01/pruefung-a/historie.diff

/root/gesamtstand-01/pruefung-a/zustand-vorher.json

/root/gesamtstand-01/pruefung-a/zustand-nachher.json

/root/gesamtstand-01/pruefung-a/db-zaehler-vorher.json

/root/gesamtstand-01/pruefung-a/db-zaehler-nachher.json

/root/gesamtstand-01/pruefung-a/KASSE.md

/root/gesamtstand-01/pruefung-a/DATEIEN.txt

/root/gesamtstand-01/pruefung-a/PRUEFSUMMEN.sha256

/root/gesamtstand-01/pruefung-a/VERIFIKATION.json

## Sources

[1] file:///root/.hermes/cache/documents/doc_8d640daa6c3c_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6.md — Masterprompt Fassung 6 (lokales Übergabedokument)
[2] file:///root/biotop/biotop/organe/aufnahme.py — aufnahme.py
[3] file:///root/biotop/biotop/organe/landkarte.py — landkarte.py
[4] file:///root/biotop/kammer/Dockerfile — Dockerfile
[5] file:///root/biotop/biotop/__main__.py — __main__.py
[6] file:///root/biotop/biotop/lauf.py — lauf.py
[7] file:///root/biotop/biotop/organe/genesis.py — genesis.py
[8] file:///root/biotop/biotop/kern/diffwerk.py — diffwerk.py
[9] file:///root/biotop/biotop/organe/aegis.py — aegis.py
[10] file:///root/biotop/biotop/organe/kammer.py — kammer.py
[11] file:///root/biotop/biotop/kern/messgeraet.py — messgeraet.py
[12] file:///root/biotop/biotop/kern/datenbank.py — datenbank.py
[13] file:///root/biotop/biotop/organe/lazarus.py — lazarus.py
[14] file:///root/biotop/pruefung/vorspann.py — vorspann.py
[15] file:///root/biotop/biotop/organe/verfassung.py — verfassung.py
[16] file:///root/biotop/biotop/organe/eichung.py — eichung.py
[17] file:///root/biotop/biotop/kern/referenzlast/logmuehle.py — logmuehle.py
[18] file:///root/biotop/biotop/organe/eichproben.py — eichproben.py
[19] file:///root/biotop/biotop/organe/eichgegenstand.py — eichgegenstand.py
[20] file:///root/biotop/biotop/organe/gedaechtnis.py — gedaechtnis.py
[21] file:///root/biotop/biotop/organe/fundpruefung.py — fundpruefung.py
[22] file:///root/biotop/biotop/organe/generation0.py — generation0.py
[23] file:///root/biotop/biotop/kern/befundklassen.py — befundklassen.py
[24] file:///root/biotop/biotop/anbieter/__init__.py — __init__.py
[25] file:///root/biotop/biotop/kern/kasse.py — kasse.py
[26] file:///root/biotop/biotop/organe/mentor.py — mentor.py
[27] file:///root/biotop/biotop/organe/jury.py — jury.py
[28] file:///root/biotop/biotop/kern/protokoll.py — protokoll.py
[29] file:///root/biotop/biotop/dienst.py — dienst.py
[30] file:///root/biotop/biotop/oberflaeche.py — oberflaeche.py
[31] file:///root/gesamtstand-01/pruefung-a/historie/a41838c-eltern-messgeraet.py — a41838c-eltern-messgeraet.py
[32] file:///root/gesamtstand-01/pruefung-a/historie/7c73d403c18755dda26655c78ac7290c446d9f45-aegis.py — 7c73d403c18755dda26655c78ac7290c446d9f45-aegis.py
