# Abnahme: Biotop Phase 4, Vorbedingung 1

**Geprüft von:** Chat-Claude · **Abruf:** 20.09.2026, Adressen `-06`
**Wertung: ABGENOMMEN.** Alle Punkte des Freigabetors aus Prüfung 6 sind belegt.
**Geltungsbereich ist eng — Abschnitt 4 gehört zwingend zur Abnahme dazu.**

---

## 1. Bestätigt durch Ausführung

```
Je Zweck, vollständige Liste:   76 Zwecke, 183 Aufrufe    ✓ (gemeldet 76 / 183)
                                0,3895 € gegen 0,3899 €   — Rundung über 76 Zeilen, kein Befund
Je Modell:                      183 Aufrufe, 0,3899 €     ✓
Läufe 22–25:                    848 Aufrufe, 1,6970 €     ✓
Laufgrenze Lauf 25:             0,3899 / 0,80 = 48,7 %    ✓ gehalten
```

**Die Kassenlücke ist aufgelöst, und zwar zu Hermes' Gunsten:**

```
233 − 44      = 189 Aufrufe     ← genau der fehlende Block
0,5166 − 0,1190 = 0,3976 €      ← genau der fehlende Betrag
```

Mein `BERICHT.md`-Befund war berechtigt — aber der Fehler saß in der **Einzelzeile** für Lauf 22 (nur die Fortsetzung, 44 Aufrufe), nicht in der Summe. Die 189 Aufrufe gehören zu Lauf 22, nicht zu Lauf 25. Die Zeitfenster belegen es unabhängig: Lauf 22 endete 19.09. um 22:53, Lauf 25 begann 20.09. um 01:13. **Die befürchtete Grenzverletzung bei 98 % liegt nicht vor.**

**Unabhängige Gegenprobe aus dem Kassenblatt**, die Hermes selbst nicht zieht:

```
aegis.ansage.formeln 11 + preise 7 + lager 5   = 23   ✓ = die 23 Ansagen der Ursachenkette
aegis.angriff.lager 1 + formeln 1 + preise 1   =  3   ✓ = die 3 ausgeführten Angriffe
```

Die Ursachenkette aus `NACHGANG-05.md` stimmt mit der Kasse überein, obwohl beide aus verschiedenen Tabellen kommen. Das ist der beste Beleg dafür, dass die Zahlen nicht nacherzählt, sondern abgefragt sind.

---

## 2. Das Freigabetor, Punkt für Punkt

| Tor-Punkt | Stand | Beleg |
|---|---|---|
| N12 klärt den Kassenstand | **erfüllt** | 848 / 1,6970 € geht auf, Differenz als Lauf 22 identifiziert |
| Laufgrenze nachweislich gehalten | **erfüllt** | 48,7 %, Zeitfenster ohne Überschneidung |
| N13 benennt die Aufnahmestelle | **erfüllt** | beide `-05`-Belege trugen `sperrart="norm"` |
| Beide Aufnahmestellen belegt | **erfüllt** | `fund` #16026/#16027 (Zeile 621), `norm` #16010/#16014 (Zeile 654) |
| Mindestens zwei verschiedene Sperrfälle | **erfüllt** | `reserviert\|Eq:zahl` (lager) und `preis_fuer\|GtE:zahl` (preise) |

Der Maßstab stand vor der Messung und ist erfüllt. Ich verhandle ihn jetzt nicht nach — in keine Richtung.

### Eine Korrektur, die nichts am Ergebnis ändert

Der Bericht nennt **drei** verschiedene Sperrfälle. Zwei davon sind dieselbe Behauptung im selben Bereich (`preis_fuer|GtE:zahl` in `preise`), einmal an der Norm-Stelle, einmal an der Fund-Stelle. Nach Hermes' eigenem neuen Punkt 15 sind das **zwei verschiedene Behauptungen**, die drei Stellen-Durchläufe erzeugt haben.

Meine Grenze lautete „mindestens zwei verschiedene". Zwei liegen vor. **Das Tor ist erfüllt, die Zahl 3 ist zu hoch gegriffen.** Für Fassung 7 zählt: je Stelle ein Beleg, je Behauptung ein Fall — das sind zwei verschiedene Größen und gehören getrennt ausgewiesen.

---

## 3. Der stärkste Beleg ist der, den er beinahe nicht gemeldet hätte

Drei Fehlversuche auf dem Weg zur Fund-Stelle, alle offengelegt:

1. Kandidat starb am Grenzmaß
2. Test trug `Staffel|GtE:zahl` statt `preis_fuer|GtE:zahl`
3. Test wurde als Norm eingestuft, dann ein Vertragstest zitiert, den das Werk nicht hat — `_nennt_vertrag` gab korrekt `False`

Sein Schluss daraus ist richtig und nicht naheliegend: **Ein gestellter Gegenstand, der die Regeln des Kerns nicht erfüllt, kommt nicht durch.** Grenzmaß, Vertragsprüfung und Norm-Regel haben den Prüfkandidaten dreimal zurückgewiesen, bevor er die Fund-Stelle erreichte. Ein sauberer Treffer beim ersten Versuch wäre ein **schwächerer** Beleg für die Echtheit des Pfads gewesen als diese drei Fehlschläge.

---

## 4. Geltungsbereich der Abnahme — das gehört dazu

Abgenommen ist: **Die Bauteile sind gebaut, und ihre Mechanik ist im laufenden Kern nachgewiesen.**

Nicht abgenommen und ausdrücklich offen:

| Offener Punkt | Wo er gemessen wird |
|---|---|
| C hat im **natürlichen Betrieb** nie eine Doppelung abgefangen — alle Belege sind gestellte Gegenstände | Tor 4 am echten Werk |
| Tor 2 Zeile 8 ist **ungemessen** — Lauf 25 erzeugte 0 Funde | Tor 4, wo 135 Testfehlschläge den Nenner liefern |
| Abweichungsquote Ansage ↔ Ausführung: **0 Zeilen**, ungemessen | Tor 4 |
| Bauteil B zeigt **Streuung statt Wirkung** (75 % gegen 20 % bei gleichem Bestand) | bleibt so; die Zeile wird umbenannt, siehe Fassung 7 |
| Der Prüfkandidat kam erst nach einer Änderung an `katalog.py` am Grenzmaß vorbei | belegt den **Pfad**, nicht das Grenzmaß oder die Kandidatengüte |

Hermes hat jeden dieser Punkte von sich aus benannt. Keiner davon ist ein verstecktes Loch.

---

## 5. Kassenstand — meine Entscheidung, als eigene gekennzeichnet

Zwei Lesarten stehen im Raum. **V16: Ich führe Vorbedingung 1 mit Lesart A, 1,6970 € von 3 €, frei 1,3030 €.**

Grund: Die vorsichtige Lesart kann später nur Geld freigeben, nie welches kosten. Ob die erste Etappe von Lauf 22 schon im Phase-3-Nachlaufordner verbucht ist, kann ich von hier nicht prüfen — die Adresse liegt mir nicht vor. Auf die Liste für danach, nicht in diese Runde: In beiden Lesarten ist das Budget gehalten, der Unterschied beträgt 0,40 € bei über 1,30 € frei.

Der eigentliche Fehler dahinter gehört in Fassung 7: **Ein Aufruf trägt genau eine Lauf- und Abschnittszuordnung und wird nie zwei Abschnitten belastet.**

---

## 6. Was Vorbedingung 1 gekostet und erbracht hat

| | |
|---|---|
| Läufe | 22, 23, 24, 25 |
| Aufrufe | 848 |
| Kosten | 1,6970 € von 3 € (57 %) |
| Prüfrunden | 6 |
| Zählfehler, alle von Hermes selbst gefunden | 7 |

**Erbracht:** Bauteil A tut nicht, wofür es zuerst gutgeschrieben wurde — es spart Aufrufe und verhindert Zwangsbefunde, verhindert aber keine Doppelungen. Bauteil B streut. Und ein drittes Bauteil, das im ursprünglichen Plan gar nicht vorkam, musste gebaut werden, weil eine Sperre an der Ansage einem Sprachmodell auf sein Wort vertraut.

Genau dafür gibt es Vorbedingungen. Wären diese zwei Bauteile ungeprüft ins echte Werk gegangen — 237.000 Zeilen, 17 Dienste —, wäre Zeile 8 dort gegen ein Messgerät gemessen worden, das die gemessene Größe gar nicht erfasst.

---

## 7. Änderungsverzeichnis für Fassung 7

Mir liegt Fassung 6 im Wortlaut nicht vor, deshalb hier das vollständige Verzeichnis statt der ausgeschriebenen Fassung. **Gib mir Fassung 6, und ich schreibe Fassung 7 aus.**

### A — Messgerät (erzwingt neue Läufe)

1. **Zeile Bauteil B umbenennen** in „≥ 1 werkübergreifender Verweis bei gezeigtem Mindestanteil". Belegt ist allein die Vorlagenänderung 3 → 6 fremde Muster; das Zitierverhalten streut und wird nicht als Wirkung verbucht.
2. **A und C bekommen getrennte Zeilen.** A misst gesparte Aufrufe und den „KEIN ANGRIFF"-Anteil. C misst Doppelungen. Zeile 8 gehört zu C.
3. **Zeile 8 gilt als ungemessen unterhalb von 20 erzeugten Funden.**
4. **V9 ist ein Zähler** (`aegis.abweichung`), keine Sperre.
5. **Ein Sperrbauteil wird am Zustrom gemessen, nie am Rest.**
6. **Eine Sperre ohne Sperrung meldet „nicht gemessen", nicht „bestanden".**
7. **Jedes deterministische Tor braucht einen Pfadnachweis je Eintrittsstelle.**
8. **Filtergüte als stehendes Maß:** Fehlalarm 0 mit Einzelbeleg, Durchgerutscht 0.

### B — Bericht und Belege

9. Keine Zahl aus dem Gedächtnis — jede aus einer Protokollabfrage, die Abfrage beigelegt.
10. Jede Zahl nennt ihre Menge im Satz daneben.
11. Die Herkunft jeder Zahl steht dabei: laufender Lauf, gestellte Prüfung oder Rekonstruktion.
12. Eine berichtigte Zahl braucht eigene Eichfälle.
13. Ein gestellter Fall, zweimal durchlaufen, ist **ein** Fall. Stellen-Durchläufe und Behauptungsfälle werden getrennt ausgewiesen.
14. Jede Aufstellung nennt, ob sie vollständig ist oder ein Auszug.
15. Abbrüche und abgewiesene Aufrufe erscheinen im Bericht **und** im Kassenblatt.
16. `.err`-Dateien werden nach jedem Lauf durchgesehen, der Befund genannt — auch wenn sie leer sind.
17. Laut scheitern, nie still.

### C — Kasse

18. Der Gesamtstand wird bei jeder Meldung gegen die Summe der Einzelläufe geprüft; jede Abweichung wird benannt, bevor jemand anders sie findet.
19. **Ein Aufruf trägt genau eine Lauf- und Abschnittszuordnung** und wird nie zwei Abschnitten belastet.

### D — Ablieferung

20. Keine Datei wird überschrieben; nummerierte Namen.
21. Melden und Abliefern sind ein Vorgang; die gemeldete Prüfsumme ist die des ausgelieferten Ordners.
22. Jeder Abschlussbericht nennt Bericht, Dateiliste, Ordnerprüfsumme und Kassenblatt als ganze URL in eigener Zeile.

### E — Pflichten des Auftraggebers (betrifft mich, nicht Hermes)

23. **Verlangt ein Auftrag eine Größe, die es noch nicht gibt, ist er eine Messgerätänderung** — der Auftraggeber schreibt das hin, nicht der Ausführer.
24. **Ein Maßstab, der bei leerem Gegenstand wahr wird, ist kein Maßstab.** Jede Grenze wird gegen den leeren Fall geprüft, bevor sie gesetzt wird. „Geprüfte Aufnahmen = erzeugte Einträge" war bei 0 = 0 wahr und leer.

---

## 8. Nächster Schritt

Fassung 7 schreiben, dann **Vorbedingung 2: die Verfassung des Handelssystems.** Die schreibt Philipp; Hermes legt einen Entwurf vor, der den tragenden Pfad für den Eichgegenstand benennen muss. Ohne diesen Eintrag wartet das Organ und der Lauf beginnt nicht.

---

## 9. Kurzprompt für den Telegram-Chat mit Hermes

> **Vorbedingung 1 ist abgenommen.** Ich habe alles nachgerechnet: 76 Zwecke und 183 Aufrufe in der vollständigen Kassenliste, 848 Aufrufe und 1,6970 € über die Läufe 22–25, Laufgrenze 25 bei 48,7 % gehalten, und die Lücke löst sich exakt auf — 233 − 44 = 189 Aufrufe, 0,5166 − 0,1190 = 0,3976 €, der Fehler saß in deiner Einzelzeile für Lauf 22, nicht in der Summe, und die Zeitfenster belegen es unabhängig. Deine drei Fehlversuche auf dem Weg zur Fund-Stelle sind dabei der stärkste Beleg des ganzen Nachgangs: Grenzmaß, Vertragsprüfung und Norm-Regel haben den gestellten Kandidaten dreimal zurückgewiesen, und ein sauberer Treffer beim ersten Versuch wäre ein schwächerer Nachweis für die Echtheit des Pfads gewesen — eine Zahl korrigiere ich trotzdem: Es sind zwei verschiedene Sperrfälle an drei Stellen-Durchläufen, nicht drei Fälle, und mein Tor verlangte zwei. **Die Abnahme gilt eng:** gebaut und im laufenden Kern nachgewiesen, aber C hat im natürlichen Betrieb nie eine Doppelung abgefangen, Zeile 8 und die Abweichungsquote bleiben ungemessen und stehen für Tor 4 — das Änderungsverzeichnis für Fassung 7 mit 24 Punkten steht in `ABNAHME_Vorbedingung-1_2026-09-20.md`, danach kommt Vorbedingung 2, die Verfassung des Handelssystems.
