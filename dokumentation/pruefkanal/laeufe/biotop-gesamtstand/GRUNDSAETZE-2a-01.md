# Die sechs Grundsätze gegen meinen eigenen Code

Maßstab ist der unveränderte Wortlaut von Fassung 6, Zeilen 103–108. **Keine Gesamtquote „sechs bestanden“ oder „sechs verletzt“:** Der aktuelle Code enthält zu fünf Grundsätzen konkrete Abweichungen beziehungsweise fortbestehende historische Nebenpfade; beim dritten ist die zentrale Trennung heute gebaut, ihre vollständige Anwendung jedoch nicht. Statische Befunde sind gelesen, nicht neu ausgeführt. Die Anhänge unterscheiden davon historische Protokollbelege.

## 1. Ein fallender Test beweist eine Abweichung, nie ihre Richtung

**Nicht durchgängig eingehalten.**

- Die aktuelle Aegis-Normklassifikation ist real vorhanden: Absturz im Werk oder expliziter Vertrags-/Verfassungsverweis werden geprüft. Den früheren Fehler „jeder rote Test ist ein Fund“ pauschal dem heutigen Ankläger zuzuschreiben wäre falsch.
- **A14/B-08 und B-10:** Die Fund-Neubewertung kann testinterne Ausnahmen dem Werk zurechnen; die Verweisprüfung kann eine passende Verfassungsnummer als Autorität akzeptieren, ohne die semantische Bindung der Behauptung an diesen Satz zu prüfen. Eine Kennung ist notwendig, aber kein Beweis, dass die gewählte Sollrichtung gilt.
- **B-09:** `pruefung/funde_neubewerten.py` leitet Vertragshinweise/Fehler anders ab als das heutige Fundprüfungsorgan. Es kann Normfälle anders einordnen und schreibt Status; es ist fachlich abgelöst, aber nicht ungefährlich „tot“.
- **A11/B-04/B-05:** Meine Norm-Eichprobe beweist nicht einmal, dass sie diese Regel erreicht. Sie liest `masse` statt `mass`; historische grüne Ergebnisse nennen `norm=[]` und `zuwachs=None`, während die Ablehnung aus Pareto beziehungsweise Verfassung stammt. Beispiel #12538 ist im Protokollanhang enthalten. Die Behauptung „Normprobe bestanden“ war damit nicht gerechtfertigt.

**Eigenanteil:** Die Grünmeldung habe ich gebaut beziehungsweise übernommen; ich darf sie nicht als unabhängigen Beleg gegen den eigenen Parser verwenden.

## 2. Für jede Pflicht muss es einen benannten Befehl geben

**Teilweise gebaut, nicht durchgehend wirksam.**

- Ein benannter CLI-Abbruch existiert heute. Frühere Kritik „kein Abbruchbefehl“ ist in dieser Form überholt.
- **A28/A29/B-21:** Der HTTP-Abbruch ruft `self._json()` auf, aber die Methode heißt `_json_body()`. Auch ein CLI-Abbruch stoppt einen schon arbeitenden Generationsprozess nicht verlässlich; spätere Zustandsupdates können den Abbruch überschreiben. Ein Befehl ohne durchgesetzte Wirkung erfüllt die Pflicht nicht.
- **A08/B-02:** `eichen`, `eichproben`, `funde-neubewerten` und `pruefung/vorspann.py` existieren. `mass`, `gen0` und `generation` verlangen ihren gültigen Abschluss jedoch nicht. Der Pflichtvorspann ist optionaler Bedienablauf statt Sperre.
- **A31/B-19:** Nach Fehlerfund fehlen der vollständige Lazarus-Wiederholungsablauf und die begrenzte automatische Wiederholung abgelehnter Generationen. Ein vorhandenes `rueckkehr` ist nur ein Teil dieser Pflicht.

**Eigenanteil:** Ich habe Befehlsnamen und Einzelorgan-Proben zu weitgehend mit einem erzwungenen Ablauf gleichgesetzt.

## 3. Streuung immer zwischen Messungen, nie innerhalb einer

**Die zentrale Ebenentrennung ist heute vorhanden. Kein erneuter Beleg des alten Fehlers.**

- `kern/messgeraet.py` aggregiert Laufzeiten aus drei Durchläufen; `organe/eichung.py` bildet die Streuung aus wiederholten Messungen. A34 grenzt den früheren Zustand ausdrücklich als historisch behoben ab.
- Das vorhandene Rauschbeispielskript wurde in dieser Bestandsaufnahme im schreibgeschützten Container ausgeführt: `17-rauschbeispiele-ausfuehrung-02.json`, Exit 0 mit Ausgabe. Es druckt Ergebnisse und Erwartungen; das ist **keine eigenständige assert-basierte Testsuite** und kein neuer Eichlauf am Werk.
- **A10/B-03:** Die richtige statistische Hilfsfunktion wird nicht über alle verlangten Grenzmaße und nicht verbindlich in jeder Auswahl verwendet. Gemessene Bereichssperren und Toleranzen erreichen normale Läufe nicht zwingend. Nullwerte/fehlende Werte, Ausreißerbehandlung und Zeitraumvorbehalt haben weitere Lücken. Das verletzt den vollständigen Eichauftrag, ist aber nicht identisch mit „Streuung wieder innerhalb eines Medians gebildet“.

**Eigenanteil:** Einen richtig gerechneten Helfer als vollständig wirksame Rauschkontrolle auszugeben wäre meine Übertreibung. Diese Bestandsaufnahme tut es nicht.

## 4. Eine Prüfung darf den geprüften Bestand nicht verändern

**Konkrete Verstöße in eigenen Prüfscripten und Zustandswegen.**

- **B-22:** `pruefung/tor3_oberflaeche.py:16–19` überschreibt das reale Konto `philipp` mit einem Prüfkennwort. `finally` beendet den Server, stellt Konto und Tokenbestand nicht wieder her. Das Script wurde hier ausschließlich gelesen, nicht ausgeführt.
- **B-15:** Die Geschmacksmechanik verwendet produktive Tabellen; der Vorhersagepfad trennt synthetische Entscheidungen und Hermes-Entscheidungen nicht sicher von Philipps echten Entscheidungen.
- **A13/B-06:** Die Eichproben setzen zwar `ist_probe`, hinterlassen aber lernwirksame Ansagen und gegebenenfalls Immunfunde unter echten Lauf-/Werk-IDs. Die spätere Behauptungssperre kann sie ohne Probenausschluss lesen. Weder `proben` noch `vorspann` nehmen diesen Bestand vollständig zurück.
- **Positiv abzugrenzen:** `ist_probe` an Gedächtniseintrittsstellen ist heute vorhanden. Es macht andere Nebenwirkungen nicht rückwirkend unschädlich.

**Diese Bestandsaufnahme:** Quellcode und produktive Datenbank wurden nicht repariert oder fortgeschrieben. Auswertungen verwenden eine private SQLite-Sicherung und schreibgeschützte Verbindungen; eigene Skripte liegen außerhalb des Biotops. Anfangs-/Endvergleich und Hashprüfung sind beigefügt. Die optionale neue Gegenfallprüfung scheiterte im eigenen Gerüst und wurde nach blockierter Freigabe nicht wiederholt; kein Erfolg erfunden.

## 5. Nachrechnung mit derselben Ableitung wie das geprüfte Organ

**Nicht bei allen vorhandenen Nachrechenwegen eingehalten.**

- **B-09:** Das alte `funde_neubewerten.py` hat eigene Fund-/Vertragsableitungen statt denselben Aegis-/Fundprüfungshelfern. Das Ergebnis ist deshalb nicht ohne Weiteres die Nachrechnung des aktuellen Organs.
- **A11/B-04:** Die Eichprobe liest einen anderen Ergebnis-Schlüssel als das Organ liefert. Das ist ein besonders einfacher Fall einer scheinbar passenden Nachrechnung, die tatsächlich etwas anderes prüft.
- **A32/C03:** Die Kurvennachrechnung überträgt nur unmittelbar unter `tests/` liegende `test_*.py`. Verschachtelte Endtests/Verträge bleiben generationsspezifisch. Dann werden nicht alle Generationen mit demselben vollständigen Endtestbestand betrachtet.
- **Positiv:** Die spätere Projektgedächtnis-Differenzprüfung benutzt die Zielableitung und den Filter für verworfene Läufe; die früheren drei strittigen Fälle werden hier nicht wieder zu echten Wiederholungen umgedeutet. Auch die Hashkettenprüfung dieser Bestandsaufnahme rief die originale `protokoll.pruefen`-Funktion auf.

**Eigenanteil:** Unabhängigkeit des Prüfers bedeutet nicht Freiheit, die Bezugsgröße oder Klassifikation still zu wechseln.

## 6. Sache statt Erscheinung

**Gebaut, aber weiterhin an mehreren Stellen verletzt.**

- **B-10:** Die explizite Vertrags-/Verfassungskennung ersetzt nicht die inhaltliche Bindung der Behauptung an diesen Vertrag. Der Code prüft den Verweis, nicht vollständig dessen inhaltliches Recht.
- **A33/B-11:** Die zusätzliche Aufnahmesperre C kann die gerade von A protokollierte eigene neue Ansage als bereits vorhandene Behauptung behandeln. Eine Sperrmeldung ist nicht der Beweis, dass eine echte Doppelung verhindert wurde; sie kann den ersten neuen Fall verhindern. Gestellte Pfadproben ohne die eigene Ansage umgehen die kritische Wechselwirkung.
- **B-14:** Der Mindestanteil fremder Artmuster ist nicht durch den Namen des Blocks erfüllt: Bei genügend eigenen/fremden Einträgen enthält der 25er-Branch 12 fremde Einträge, also weniger als die Hälfte. Eine erzwungene Referenz im Modellergebnis wäre kein zulässiger Ersatz.
- **B-24:** Entropie vergleicht Mengen geänderter Textzeilen, verliert damit Häufigkeit und Reihenfolge und filtert nur `nische!=probe`, nicht `ist_probe`. Die Bezugsgröße des ausgegebenen Anteils ist dagegen tatsächlich die Zahl betroffener Kandidaten, nicht die Zahl der Paare.
- **A09:** Ein Entscheidertext, der mit `philipp` beginnt, ist keine verifizierte Identität. Der CLI-/Kernpfad darf eine Benennung nicht mit Philipps tatsächlicher Freigabe verwechseln.
- **Positiv:** Der heutige Eichgegenstand verlangt beim Betriebswerk einen expliziten tragenden Pfad. Die heutige Probensperre kennt `ist_probe`. Diese Fortschritte werden nicht unterschlagen.

## Konsequenz vor einem weiteren Bau-/Hebungslauf

Die Grenzwerte bleiben unverändert. Zuerst müssen Messgerät-/Prüfpfade repariert und in einem isolierten Prüfbestand mit echten Gegenfällen nachgewiesen werden. Danach neuer Lauf vom festgehaltenen Ausgang, nicht Fortsetzung von 22/23/25. Diese Reihenfolge ist eine Folgerung aus den gefundenen Verstößen, **keine in dieser Bestandsaufnahme ausgeführte Reparatur oder Freigabe**.
