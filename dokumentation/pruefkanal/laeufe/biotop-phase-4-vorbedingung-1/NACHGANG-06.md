# Nachgang N12 bis N14 — Kasse, Aufnahmestellen, zweiter Sperrfall

**Prüfung:** `PRUEFUNG6_Lauf-25_2026-09-20.md` · **Ausführung:** Hermes · **Stand:** 20.09.2026
**Kosten: 0 Modellaufrufe.** Kassenstand Lauf 25 vor und nach diesem Nachgang: **183 Aufrufe, 0,3899 €**.

---

## Adressen (V12)

Bericht:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/NACHGANG-06.md

Dateiliste:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/DATEIEN-06.txt

Ordnerprüfsumme:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/PRUEFSUMME-ORDNER-06.txt

Kassenblatt:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/KASSE-06.md

---

## N12 — Kassenabgleich: die Grenze ist gehalten

Beleg: `ausgaben/25-30-n12-kassenabgleich.txt`. Menge: Tabelle `kasse`, gruppiert nach `lauf_id`.

| Lauf | Aufrufe | € | Zeitfenster |
|---|---|---|---|
| 22 | **233** | **0,5166** | 19.09. 20:57 – 22:53 |
| 23 | 239 | 0,3936 | |
| 24 | 193 | 0,3969 | |
| 25 | **183** | **0,3899** | 20.09. 01:13 – 01:43 |
| Summe | 848 | 1,6970 | |

**Die 189 Aufrufe / 0,3976 € gehören zu Lauf 22, nicht zu Lauf 25.** Mein `BERICHT.md` führte Lauf 22 mit
44 Aufrufen / 0,1190 € — das war nur die *Fortsetzung* (Generation 5), die unter Vorbedingung 1 lief. Die
erste Etappe (Generationen 1–4) gehörte zum Phase-3-Nachlauf. In der Summenzeile habe ich dann aber die volle
Datenbanksumme genommen. **Einzelzeilen und Summenzeile zählten verschiedene Mengen** — genau Punkt 17 der
Fassung-7-Sammlung, und der Prüfbefund war berechtigt.

**Die harte Grenze von Lauf 25 steht bei 0,3899 von 0,80 € = 49 %.** Die Zeitfenster belegen es zusätzlich:
Lauf 22 endete um 22:53, Lauf 25 begann um 01:13. Kein Aufruf von Lauf 22 fällt unter die Laufgrenze von
Lauf 25. Die befürchtete Grenzverletzung (98 %) liegt **nicht** vor.

**Gesamtstand Vorbedingung 1, in beiden Lesarten** (die Entscheidung liegt bei Philipp):
- **Lesart A** (Lauf 22 vollständig): 848 Aufrufe, **1,6970 € von 3 €** — 57 %, frei 1,3030 €
- **Lesart B** (nur die Fortsetzung, 44 Aufrufe): **1,2994 € von 3 €** — frei 1,7006 €

Lesart B vermeidet eine Doppelzählung über zwei Abschlussordner hinweg (die erste Etappe ist im
Phase-3-Nachlauf abgerechnet). In beiden Fällen ist das Budget gehalten.

**Nebenbefund, bestätigt:** Die Aufstellung „Je Zweck" in `KASSE-05.md` war ein **Auszug** — 12 der
**76** Zwecke, 42 von 183 Aufrufen, 0,1319 von 0,3899 €. Die Überschrift nannte die Menge, als wäre sie
vollständig. In `KASSE-06.md` ist sie als Auszug gekennzeichnet und die vollständige Liste beigelegt.

---

## N13 — Welche Aufnahmestelle hat `#16014` geschrieben?

Beleg: `ausgaben/25-31-n13-n14-aufnahmestellen.txt`.

C hat zwei Aufrufstellen im Kern (`biotop/organe/aegis.py`):
- **Zeile 621:** Aufnahme von **Funden** → `aufnahmesperre(..., art='fund')`
- **Zeile 654:** Aufnahme von **Norm-Tests** → `aufnahmesperre(..., art='norm')`

Das Protokollfeld `sperrart` benennt die Stelle. Gemessen:

```
#16010  sperrart = "norm"
#16014  sperrart = "norm"
```

**Antwort: Beide Zeilen stammen von der NORM-Stelle. Die Fund-Stelle war unbelegt.** Der Prüfbefund trifft zu
— und er trifft die gefährlichere Stelle, denn `aegis_k2500_preise`, einer der beiden in Lauf 24 gemessenen
Durchrutscher, war ein **Fund**.

---

## N14 — Beleg für die Fund-Stelle, mit einer anderen Doppelung

Zweiter gestellter Gegenstand durch den laufenden Kern (`aegis.pruefen`), Bereich `preise`, Vorrat 7
Behauptungen. Gewählte Doppelung: **`preis_fuer|GtE:zahl`** — eine **andere** als im ersten Fall
(`reserviert|Eq:zahl`, Bereich `lager`) und genau die Behauptung, auf der `aegis_k2500_preise` durchrutschte.

```
#16026  immun.aufnahme_geprueft   sperrart "fund", bereich preise, anzahl 2, vorrat_groesse 7
#16027  immun.aufnahme_gesperrt   sperrart "fund", behauptung preis_fuer|GtE:zahl,
                                  gegenstueck "bereits im Vorrat des Bereichs"
```

- **ROT:** `test_rot2_preis_fuer_wiederholte_behauptung` (`preis_fuer|GtE:zahl`) → **abgewiesen**
- **GRÜN:** `test_gruen2_neue_behauptung_im_fund_zweig` (`anzahl|Lt:name`) → **aufgenommen**
- Aufrufe von C mit `sperrart='fund'`: **0 → 1**

**Beide Aufnahmestellen sind damit belegt.**

### Bilanz je Stelle (Menge: Protokoll Lauf 25, Feld `sperrart` — vollständig)

| Stelle | Aufrufe | Sperrungen |
|---|---|---|
| `fund` | 1 | 1 |
| `norm` | 4 | 4 |

### Verschiedene Sperrfälle (Fälle, nicht Durchgänge — Fassung 7 Punkt 15)

| Bereich | Behauptung | Stelle |
|---|---|---|
| lager | `reserviert\|Eq:zahl` | norm |
| preise | `preis_fuer\|GtE:zahl` | norm |
| preise | `preis_fuer\|GtE:zahl` | **fund** |

**3 verschiedene Sperrfälle** (der Prüfbefund „ein Fall, zweimal gelaufen" traf auf den Stand von `-05` zu;
jetzt liegen drei vor, davon einer an der Fund-Stelle). Fehlalarm: **0** — jede Sperrung betraf eine
tatsächlich im Vorrat stehende Behauptung, jede mit Gegenstück im Protokoll.

---

## Drei eigene Fehlversuche auf dem Weg — offengelegt

Der Beleg für die Fund-Stelle brauchte vier Anläufe. Die ersten drei scheiterten, und zwar an der Sache:

1. **Kandidat starb am Grenzmaß**, bevor die Aufnahme erreicht wurde (`formeln.laufzeit_ms` gerissen). Behoben
   durch eine Änderung ohne Laufzeitwirkung (Kommentar in `katalog.py`).
2. **Mein Test trug den falschen Schlüssel:** `Staffel|GtE:zahl` statt `preis_fuer|GtE:zahl`, weil der
   `Staffel(...)`-Aufruf im Testaufbau das letzte Ziel war. Behoben durch einen Test ohne Staffel-Aufbau.
3. **Der Test wurde als Norm eingestuft statt als Fund** — nach 3.7 richtig, denn er stürzte nicht ab und
   nannte keinen Vertrag. Beim Nachbessern zitierte ich dann einen Vertragstest, **den dieses Werk gar nicht
   hat** (`test_katalog_wert_in_eur` stammt aus einem anderen Stand); `_nennt_vertrag` gab korrekt `False`.
   Erst mit einem echten Vertragstest des Werks (`test_vertrag_bericht_preise::test_preis_fuer_cent_gerundet_nie_negativ`)
   wurde der Test als Fund anerkannt und die Fund-Stelle erreicht.

Keiner dieser Fehlversuche kostete einen Modellaufruf (der Angriff war gestellt). Alle drei sind Belege dafür,
dass der Pfad echt ist: Ein gestellter Gegenstand, der die Regeln des Kerns nicht erfüllt, kommt nicht durch.

**Grundsatz 4 beachtet:** Prüfkandidat und erzeugte Einträge wurden nach jeder Messung entfernt. Bestand
Werk 22 unverändert: 1 im Werk, 25 offen, 14 Norm. Die Protokollzeilen bleiben.

---

## Stand gegen das Freigabetor der Prüfung 6

| Tor-Punkt | Stand |
|---|---|
| N12 klärt den Kassenstand, Laufgrenze nachweislich gehalten | **erfüllt** — 0,3899 von 0,80 € = 49 %, Differenz als Lauf 22 identifiziert |
| N13 benennt die Aufnahmestelle | **erfüllt** — beide `-05`-Belege waren `sperrart='norm'` |
| Beide Aufnahmestellen mit je einem Beleg | **erfüllt** — `fund` in #16026/#16027, `norm` in #16010/#16014 |
| Mindestens zwei verschiedene Sperrfälle | **erfüllt** — 3 verschiedene |

Alle vier Punkte sind belegt. **Was ich weiterhin nicht behaupte:** dass C im natürlichen Betrieb Doppelungen
abgefangen hätte — Lauf 25 erzeugte keine. Alle Belege stammen aus gestellten Gegenständen, die durch den
laufenden Kern gingen, und sind als solche gekennzeichnet.

Die Abnahme liegt bei dir.
