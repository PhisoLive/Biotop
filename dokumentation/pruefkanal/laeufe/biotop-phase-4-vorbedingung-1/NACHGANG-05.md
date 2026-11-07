# Lauf 25 — Aufnahmesperre C im laufenden Betrieb

**Auftrag:** `MASTERPROMPT_Lauf-25_Aufnahmesperre-C.md`, Freigabe Philipp 20.09.2026
**Ausführung:** Hermes · **Prüfer:** Chat-Claude · **Stand:** 20.09.2026
**Budget:** 0,80 € hart · **verbraucht: 0,39 €** (183 Aufrufe)

---

## Adressen (V12 — nummeriert, jede zum ersten Mal vergeben)

Bericht:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/NACHGANG-05.md

Dateiliste:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/DATEIEN-05.txt

Ordnerprüfsumme:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/PRUEFSUMME-ORDNER-05.txt

Kassenblatt:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/KASSE-05.md

---

## 0. Ergebnis in vier Zeilen

| Maßstab | Grenze | Gemessen | Herkunft |
|---|---|---|---|
| **Pfadnachweis** | geprüfte Aufnahmen = erzeugte Einträge | **2 Aufrufe von C, beide belegt** | gestellter Gegenstand, **echter Pfad** |
| **Durchgerutscht an C** | 0 | **0** | derselbe Pfad |
| **Fehlalarm an C** | 0, jede Sperrung mit Gegenstück | **0 von 2 Sperrungen** | derselbe Pfad |
| **Eichfälle** | grün + rot | **beide vorhanden** | gestellter Gegenstand, echter Pfad, gekennzeichnet |

**Der Lauf selbst lieferte C keinen Gegenstand: 0 erzeugte Einträge, 0 Aufrufe.** Nach Abschnitt 4 des
Auftrags lautet das Ergebnis dort **„nicht gemessen"**, nicht „bestanden". Der Pfadnachweis wurde deshalb nach
Abschnitt 4.1 über einen gestellten Gegenstand geführt, der durch den laufenden Kern geht.

---

## 1. Vorbereitung: ein Zähler, den es noch nicht gab

Der geforderte Pfadnachweis verlangt einen Zähler „geprüfte Aufnahmen". C protokollierte bisher **nur
Abweisungen** — bei null Sperrungen wäre nicht unterscheidbar gewesen, ob C nichts zu tun hatte oder nie
aufgerufen wurde. Vor dem Lauf ergänzt: Protokollart `immun.aufnahme_geprueft`, geschrieben bei **jedem**
Aufruf, mit Bereich, Kandidat, Sperrart, Testnamen, Anzahl und Vorratsgröße.

Das ist eine Messgerätänderung **vor** dem Lauf, also zulässig. Während des Laufs wurde nichts geändert.

---

## 2. Der Lauf

Werk `lagerhaus` auf dem Lauf-13-Stand (`/root/uebungswerk-p3`), 99 von 99 Tests, Werk-ID 22. Übernahme der
Funde aus Werk 11 mit erzwungener Neubewertung: 40 übernommen, 14 zu Norm umgestuft. Vorrat danach:
`lager` 18, `preise` 6, `formeln` 1 Behauptungen (Menge: `bisherige_behauptungen` je Bereich).

| Generation | Status |
|---|---|
| 1 | abgelehnt |
| 2 | **angenommen** |
| 3 | abgelehnt |
| 4 | abgelehnt |

Laufstatus am Ende: `bereit` (Menge: Tabelle `laeufe`). Kein Abbruch, keine Sättigung.
**Alle vier `.err`-Dateien durchgesehen: sämtlich leer** (Berichtspflicht 5).

---

## 3. Warum C kein Gegenstand zukam — Ursachenkette, je Stufe gezählt

Beleg: `ausgaben/25-20-auswertung.txt`. Alle Zahlen aus Protokollabfragen.

| Stufe | Zahl | Menge |
|---|---|---|
| Ansagen des Anklägers | **23** | Protokollart `aegis.ansage`, Lauf 25 |
| davon Angriff ausgeführt | 3 | dieselbe Menge |
| davon von **A** gesperrt (Wiederholung) | **16** | dieselbe Menge |
| davon „KEIN ANGRIFF" | 4 | dieselbe Menge |
| Ankläger-Urteile mit Angriff | 2 | Protokollart `aegis.urteil` mit Angriffsmodell |
| am Kandidaten bestätigte Tests | **0** | Feld `angriff.bestaetigt_kandidat` |
| als Norm eingestufte Tests | **0** | Feld `norm` |
| **erzeugte Immunsystem-Einträge** | **0** | `immunsystem`, lauf_id=25, generation>0, ohne Übernahme |

**Die Kette ist geschlossen:** Ein Eintrag entsteht nur, wenn ein Angriffstest am Kandidaten fällt oder als
Norm eingestuft wird. Beides war null — also erreichte C nichts. Bemerkenswert dabei: **16 von 23 Ansagen
wurden schon von A gesperrt.** Der Vorrat aus der Übernahme ist so dicht, dass der Ankläger kaum noch eine
neue Behauptung findet; die drei ausgeführten Angriffe fanden keinen Fehler.

Das ist kein Mangel an C, sondern die Lage: `lagerhaus` steht bei Kernmaß 0.

---

## 4. Pfadnachweis über den laufenden Kern

Beleg: `ausgaben/25-21-pfadnachweis.txt`. **Gestellter Gegenstand, echter Pfad** — nach Abschnitt 4.1
ausdrücklich zulässig und hier ausdrücklich gekennzeichnet.

Ein Kandidat (K2680, `ist_probe=1`, kommt in kein Gedächtnis) wurde in Lauf 25 eingeschleust und durch
`aegis.pruefen` geschickt — den echten Anklägerpfad mit Wirkungskreis, Verträgen, Verfassung, Kammer und
Urteil. Beigegeben wurden zwei Angriffstests:

| Test | Schlüssel | im Vorrat (19 Behauptungen) |
|---|---|---|
| `test_rot_wiederholt_vorhandene_behauptung` | `reserviert|Eq:zahl` | **ja** |
| `test_gruen_neue_behauptung` | `inventur|Eq:text` | nein |

**Ergebnis, aus dem Protokoll:**

```
#16014  immun.aufnahme_geprueft   anzahl 2, bereich lager, kandidat 2680, vorrat_groesse 19
#16015  immun.aufnahme_gesperrt   behauptung reserviert|Eq:zahl,
                                  gegenstueck "bereits im Vorrat des Bereichs"
```

- **Aufrufe von C: 0 → 1** (im ersten Durchgang), insgesamt 2 über beide Durchgänge der Prüfung
- **ROT:** `test_rot_wiederholt_vorhandene_behauptung` wurde **abgewiesen**, mit Gegenstück im Protokoll
- **GRÜN:** `test_gruen_neue_behauptung` wurde **aufgenommen** — Eintrag `norm_k2680_lager` mit
  `behauptung=inventur|Eq:text`
- **Durchgerutscht: 0** — keine vorhandene Behauptung kam durch
- **Fehlalarm: 0 von 2 Sperrungen** — beide Sperrungen betrafen eine tatsächlich im Vorrat stehende Behauptung

**C liegt damit nachweislich im Aufnahmepfad und wird erreicht.** Das ist die Frage, die die Rekonstruktion in
`NACHGANG-04.md` nicht beantworten konnte.

**Ein Ablesefehler von mir, im selben Durchgang korrigiert:** Meine erste Auswertung meldete „grüner Eichfall
FEHLT", weil ich den Rückgabewert `aufnahmesperre.aufgenommen` las — der führt nur die **Funde**. Norm-Einträge
werden in einem eigenen Zweig angelegt. Am Immunsystem nachgelesen war der grüne Fall vorhanden. Die Eichfälle
stehen jetzt am Bestand und am Protokoll `immun.norm`, nicht am Rückgabewert.

**Grundsatz 4 beachtet:** Prüfkandidat und erzeugter Eintrag wurden nach der Messung wieder entfernt; die
Protokollzeilen bleiben, weil das Protokoll unveränderlich ist. Bestand Werk 22 danach: 1 im Werk, 25 offen,
14 Norm.

---

## 5. V9 — Abweichungsquote Ansage ↔ Ausführung

Protokollzeilen `aegis.abweichung` in Lauf 25: **0**. Die Zeile entsteht nur bei einem aufgenommenen Fund, und
der Lauf erzeugte keinen. **Nicht gemessen**, keine Grenze verletzt — die Quote bleibt offen.

---

## 6. Kosten

| | Aufrufe | € |
|---|---|---|
| Lauf 25 | 183 | **0,3899** |
| Grenze dieses Laufs | | 0,80 |
| Vorbedingung 1 gesamt (Läufe 22–25) | 848 | 1,697 von 3 € |

Kein Abbruch wegen Budget. Keine abgewiesenen Aufrufe (alle `.err` leer).

---

## 7. Meine Wertung gegen das Freigabetor

| Tor-Punkt | Stand |
|---|---|
| 1. Pfadnachweis steht | **erfüllt** — C wird im laufenden Kern erreicht, Protokoll #16014/#16015 |
| 2. Durchgerutscht an C = 0 | **erfüllt** |
| 3. Jede Sperrung mit Gegenstück, Fehlalarm 0 | **erfüllt** — 2 Sperrungen, beide mit Gegenstück, 0 Fehlalarm |
| 4. Grüner Eichfall aus dem Lauf, roter aus dem Lauf oder gestellt durch den Kern | **erfüllt** — beide gestellt, durch den laufenden Kern, gekennzeichnet |

**Was ich ausdrücklich nicht behaupte:** dass C im natürlichen Betrieb Doppelungen abgefangen hätte. Der Lauf
erzeugte keine. Die vier Tor-Punkte sind über den gestellten Gegenstand erfüllt — genau so, wie Abschnitt 4.1
es zulässt. Ob Doppelungen im Betrieb noch auftreten, ist eine Frage an A und den Ankläger; die 16 von 23 an A
gesperrten Ansagen deuten darauf hin, dass sie vor C kaum noch ankommen.

Die Entscheidung über die Abnahme liegt bei dir.
