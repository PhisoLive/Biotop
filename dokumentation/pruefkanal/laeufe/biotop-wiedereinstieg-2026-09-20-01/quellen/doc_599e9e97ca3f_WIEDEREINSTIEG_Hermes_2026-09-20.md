# Wiedereinstieg — neue Hermes-Sitzung nach dem Speicherüberlauf

**Anlass:** Sitzung von Hermes bei 571.459 Token übergelaufen, nicht mehr komprimierbar, automatisch zurückgesetzt. Davor: widerrufenes OAuth-Token.
**Verfasst von:** Chat-Claude · **Stand:** 20.09.2026 · **Entscheider:** Philipp Zöllisch

---

## 0. Zuerst die Entwarnung

**Es ist nichts verloren.** Die Sitzung war nie der Datenträger. Der Datenträger ist der Abschlussordner, und der steht:

```
PRUEFSUMME-ORDNER-06.txt abgerufen: 87 Dateien, 89a68d30e3539866f7fe1df0575bcb03974f8b5061cb6b6b9362f2359629a239
= exakt der gemeldete Wert. Der Ordner hat den Absturz überlebt.
```

Genau dafür gibt es die Regel, dass jeder Auftrag mit einem von außen abrufbaren Abschlussordner endet. Sie hat heute das erste Mal ihren Preis eingespielt.

Was verloren ist: Hermes' Erinnerung an den Gesprächsverlauf. Das ist ersetzbar — dieser Brief ersetzt es.

---

## 1. Neue stehende Regel — meine Entscheidung, als eigene gekennzeichnet

**V17: Eine Sitzung, ein Auftrag.** Hermes beginnt jeden Auftrag in einer frischen Sitzung, liefert den Abschlussordner ab, und setzt danach **bewusst** zurück — statt zu warten, bis der Speicher überläuft.

Begründung, mit Zahl: Zwei Sitzungsausfälle in zwei Meldungen — erst ein widerrufenes OAuth-Token, dann 571.459 Token ohne Komprimierungsmöglichkeit. Ein Überlauf mitten in der Arbeit ist der gefährlichste Zeitpunkt, weil dann womöglich abgeliefert, aber nicht gemeldet wurde.

**V18: Das Gedächtnis liegt im Tresor und im Abschlussordner, nicht in der Sitzung.** Was Hermes über mehrere Aufträge hinweg braucht, gehört in den Obsidian-Tresor geschrieben, bevor die Sitzung endet — nicht im Verlauf mitgeschleppt.

---

## 2. Wo der Stand liegt

Alles zu Vorbedingung 1, versiegelt und nachrechenbar:

Bericht:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/NACHGANG-06.md

Dateiliste:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/DATEIEN-06.txt

Ordnerprüfsumme:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/PRUEFSUMME-ORDNER-06.txt

Kassenblatt:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/KASSE-06.md

---

## 3. Der Stand in zehn Zeilen

- **Vorbedingung 1 ist abgenommen** (20.09.2026, sechs Prüfrunden, Läufe 22–25, 848 Aufrufe, 1,6970 € von 3 €).
- **Bauteil A** (Ankläger sagt die Behauptung vorab an) spart Aufrufe und verhindert Zwangsbefunde — es verhindert **keine** Doppelungen. Es sperrt, was angesagt wird, nicht was geschrieben wird.
- **Bauteil B** (Mindestanteil werkübergreifender Block) zeigt **Streuung statt Wirkung**: 75 % gegen 20 % bei gleichem Bestand. Belegt ist nur die Vorlagenänderung, 3 → 6 fremde Muster.
- **Aufnahmesperre C** wurde deshalb neu gebaut, war im Plan nicht vorgesehen: deterministisch, im Kern, an beiden Aufnahmestellen (`aegis.py` Zeile 621 `fund`, Zeile 654 `norm`).
- **Die Abnahme gilt eng.** C hat im natürlichen Betrieb **nie** eine Doppelung abgefangen. Alle Belege stammen aus gestellten Gegenständen, die durch den laufenden Kern gingen.
- **Tor 2 Zeile 8 ist ungemessen** und steht für Tor 4 am echten Werk (135 Testfehlschläge liefern dort den Nenner).
- **Abweichungsquote Ansage ↔ Ausführung: 0 Zeilen**, ungemessen.
- **Ablieferungsweg:** Dateien werden **nie überschrieben**. Nummerierte Namen, jede Adresse einmal. Überschriebene Dateien kommen im Chat nur im alten Stand an.
- **Kassenstand Vorbedingung 1:** 1,6970 € von 3 €, frei 1,3030 € (Lesart A, vorsichtig geführt).
- **Nächste Schritte:** Fassung 7 schreiben, dann Vorbedingung 2 — die Verfassung des Handelssystems.

---

## 4. Erster Auftrag der neuen Sitzung — bewusst klein

Ein frischer Wiedereinstieg beginnt nicht mit einem Lauf. Er beginnt mit etwas, das den Stand wieder greifbar macht und nichts kostet:

**W1 — Fassung 6 abrufbar machen.** Den Masterprompt `INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6.md` an eine nummerierte, von außen abrufbare Adresse legen und melden. Chat-Claude braucht ihn im Wortlaut, um **Fassung 7** auszuschreiben — das Änderungsverzeichnis mit 24 Punkten liegt fertig vor.

**W2 — eine offene Kassenfrage, falls billig.** Im Abschlussordner des Phase-3-Nachlaufs nachsehen, ob die erste Etappe von Lauf 22 (189 Aufrufe, 0,3976 €) dort bereits abgerechnet ist. Ist sie es, fällt Vorbedingung 1 auf 1,2994 €. Ändert nichts an der Abnahme, bereinigt nur die Bücher. Falls die Abfrage mehr als ein paar Minuten kostet: liegen lassen und melden.

**W3 — Tresoreintrag.** Bevor die Sitzung endet: Stand aus Abschnitt 3 in den Obsidian-Tresor schreiben, damit der nächste Wiedereinstieg keinen Brief mehr braucht.

Kosten W1 bis W3: **0 Modellaufrufe** erwartet.

---

## 5. Die tragenden Arbeitsregeln, weil das Gedächtnis weg ist

Kurzfassung. Die vollständige Sammlung steht im Änderungsverzeichnis Fassung 7.

**Belege**
- Keine Zahl aus dem Gedächtnis. Jede Zahl aus einer Protokollabfrage, die Abfrage beigelegt.
- Jede Zahl nennt ihre Menge im Satz daneben — was genau gezählt wurde, mit Nenner.
- Die Herkunft steht dabei: laufender Lauf, gestellte Prüfung oder Rekonstruktion.
- „Bestätigt durch Ausführung" nur mit beigefügter Ausgabe, sonst „gelesen, nicht ausgeführt".
- Eine berichtigte Zahl braucht ihre eigenen Eichfälle.
- Jede Aufstellung nennt, ob sie vollständig ist oder ein Auszug.

**Maßstäbe**
- Ein Maßstab wird vor der Messung gesetzt und danach nicht verhandelt. Eine Grenze wird nie verschoben, damit etwas durchgeht.
- Laut scheitern, nie still. Eine Prüfung ohne Gegenstand meldet das, statt zu bestehen.
- Eine Sperre ohne Sperrung meldet „nicht gemessen", nicht „bestanden".
- Ein Sperrbauteil wird am Zustrom gemessen, nie am Rest.
- Je Tor ein roter und ein grüner Eichfall.

**Läufe und Kasse**
- Jede Messgerätänderung erzwingt einen neuen Lauf. Während eines Laufs wird nichts am Messgerät geändert.
- Abbrüche und abgewiesene Aufrufe erscheinen im Bericht **und** im Kassenblatt. Ein folgenloser Abbruch ist erlaubt, ein verschwiegener nicht.
- `.err`-Dateien nach jedem Lauf durchsehen, den Befund nennen — auch wenn sie leer sind.
- Der Gesamtstand wird gegen die Summe der Einzelläufe geprüft, jede Abweichung benannt.
- Ein Aufruf trägt genau eine Lauf- und Abschnittszuordnung.

**Ablieferung**
- Keine Datei überschreiben. Nummerierte Namen, jede Adresse einmal.
- Melden und Abliefern sind ein Vorgang: erst hochladen, dann Dateiliste und Prüfsumme neu schreiben, dann melden.
- Jeder Bericht nennt Bericht, Dateiliste, Ordnerprüfsumme und Kassenblatt als ganze URL in eigener Zeile.
- Abgeliefert wird **auch bei Abbruch**. Ein Abschlussordner ohne Ergebnis ist ein Ergebnis; eine Meldung ohne Ordner ist keines.

**Rollen**
- Hermes führt aus. Chat-Claude ist Auftraggeber, Prüfer und Korrektiv. **Philipp entscheidet und gibt ab Phase 4 allein frei.**

---

## 6. Kurzprompt für den Telegram-Chat mit Hermes

> Deine Sitzung ist bei 571.459 Token übergelaufen und zurückgesetzt worden — **es ist nichts verloren**, ich habe `PRUEFSUMME-ORDNER-06.txt` abgerufen und der Ordner steht mit 87 Dateien und `89a68d30…`, genau wie gemeldet; Vorbedingung 1 ist abgenommen, der ganze Stand liegt in `WIEDEREINSTIEG_Hermes_2026-09-20.md`, und ab sofort gilt: **eine Sitzung, ein Auftrag**, am Ende Abschlussordner und dann bewusst zurücksetzen, statt zu warten, bis der Speicher überläuft. Dein erster Auftrag ist bewusst klein und kostet keinen Modellaufruf: Leg `INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6.md` an eine nummerierte, abrufbare Adresse und melde sie, damit ich Fassung 7 ausschreiben kann — das Änderungsverzeichnis mit 24 Punkten liegt fertig. Danach zwei Kleinigkeiten: im Phase-3-Nachlaufordner nachsehen, ob die erste Etappe von Lauf 22 (189 Aufrufe, 0,3976 €) dort schon abgerechnet ist, und den Stand in den Obsidian-Tresor schreiben, bevor die Sitzung endet.
