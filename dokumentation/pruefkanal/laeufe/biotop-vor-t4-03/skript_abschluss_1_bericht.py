"""Abschluss des Berichts der Behebungsrunde 3 vor T4 — Schritt 1 von 3 (nur BERICHT.md).

Freigabe Philipp für genau diesen Fall (nicht als Dauerregel), nach zwei Sicherheitssperren: die gebündelten Schritte
getrennt; der Wortlaut der Sperren wird hier aus den gespeicherten Belegen unter sperre/ gelesen und nicht im Befehl
zitiert; das Auszählen des Protokolls der Ausführungsschicht entfällt. Inhalt wie die gesperrte Abschrift
bau/bericht_abschluss_gesperrt.py (Teil BERICHT.md), angepasst an den Stand nach der Freigabe: Gutachterproben kopiert,
Wächter nachgesehen. Keine Codeänderung an Biotop. Schritt 2 (SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md) und Schritt 3
(Quellenliste des Veröffentlichungsskripts) sind eigene Schritte.
"""
import re
from pathlib import Path

A = Path('/root/biotop-vor-t4-03')
B = A / 'BERICHT.md'
b = B.read_text()


def beleg(datei: str) -> tuple[str, str]:
    """(Befehl, Meldung) wörtlich aus einem Sperrbeleg; Befehl leer, wenn der Beleg ihn nur beschreibt."""
    t = (A / 'sperre' / datei).read_text()
    m = re.search(r'Meldung \(wörtlich\):\n-+\n(.*?)\n\n', t, re.S)
    assert m and m.group(1).startswith('Blocked:'), datei
    c = re.search(r'Befehl \(wörtlich\):\n-+\n(.*?)\n\nMeldung \(wörtlich\):', t, re.S)
    return (c.group(1).strip() if c else ''), m.group(1).strip()


befehl_1, meldung_1 = beleg('SPERRE-KOPIE-GUTACHTERPROBEN.txt')
_, meldung_2 = beleg('SPERRE-2-BERICHT-ABSCHLUSS.txt')
assert befehl_1.startswith('mkdir -p /root/biotop-vor-t4-03/review-proben')

ops = []


def R(a, n):
    ops.append((a, n))


R('# Behebungsrunde 3 vor T4: nicht abgenommen — die fünf Lücken der Python-Sonde sind geschlossen (vorher/nachher gemessen), aber K2904/K3091 wieder nur 2 von 3 (Vergleichslast), Methoden nur in Python, zwei Spezifikationen nur am Organ',
  '# Behebungsrunde 3 vor T4: nicht abgenommen — K2904/K3091 wieder nur 2 von 3 (Vergleichslast); die fünf Lücken der Python-Sonde sind für ihre Probenfälle geschlossen, aber das Review hat vier neue gemessen (Deckung: grobes Weißraum-Merkmal, Verfälschung je Funktion; Sonde: Iterator-Objekte, `__slots__`)')
R('- **Die fünf Lücken der Python-Sonde sind geschlossen, je mit einem Fall',
  '- **Die fünf Lücken der Python-Sonde sind für ihre Probenfälle geschlossen, je mit einem Fall')
R('  „nicht eingewickelt (Klasse)“ (§2). T4 ist ein Python-Werk.',
  '  „nicht eingewickelt (Klasse)“ (§2). T4 ist ein Python-Werk. Das Review fand auch in Python eine Lücke: Bei Klassen\n'
  '  mit `__slots__` (auch `@dataclass(slots=True)`) wird der Zustand von `self` nicht verglichen (§10 Nr. 4).')
R('  Test je Muster kommt am Prüfwerk durch (§3). **Grenze:**',
  '  Test je Muster kommt am Prüfwerk durch (§3). **Das Review hat zwei Lücken der Regel gemessen:** Ein Test mit doppeltem\n'
  '  Leerzeichen deckt einen Rückschritt bei Tab und Zeilenumbruch — die K2868-Lage, der Kandidat überlebt —, und ein Test\n'
  '  deckt mit einem Aufruf, den er nicht zusichert (§10 Nr. 1, 2). **Weitere Grenze:**')
R('- **Verdichtung** läuft seit dem Gateway-Neustart (§0).',
  '- **Verdichtung** läuft seit dem Gateway-Neustart (§0).\n'
  '- **Review (ein Durchgang): 18 Befunde, 4 hoch, 5 mittel, 9 niedrig** (§10). Bestätigt: alle nachgerechneten Zahlen des\n'
  '  Berichts; die alten Proben des Gutachtens 02 verhalten sich an HEAD in 14 von 14 Fallläufen wie spezifiziert. Die vier\n'
  '  hohen Befunde sind in der Kammer gemessen; Code baue ich nach dem Review nicht mehr, sie stehen als Spezifikationen in\n'
  '  `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`.\n'
  '- **Zwei Sicherheitssperren bei mir** (§11, Wortlaut aus den gespeicherten Belegen): beide Male angehalten, nichts\n'
  '  umgangen. Philipp gab für genau diesen Fall frei (nicht als Dauerregel); danach in einzelnen Schritten ausgeführt.\n'
  '- **Zwischenbericht-Wächter:** zwei Zwischenberichte in dieser Runde (Werkzeugrunde 113 und 141 von 150), beide HTTPS\n'
  '  bytegleich 5 von 5; kein Auslöser an Kontextfüllung oder Verdichtung (§11).')
R('Gesamtzahl war dieselbe wie im verhaltensgleichen Fall).',
  'Gesamtzahl war dieselbe wie im verhaltensgleichen Fall). Iteratoren werden bis zum 50. Element verglichen (Kappe N = 50);\n'
  'darüber hinaus ist eine Änderung unsichtbar (Review Nr. 16).')
R('''Enthaltung; (5) aufrufbare Objekte mit `__wrapped__` werden eingewickelt (die Hülle ruft das dekorierte Objekt, der
Zwischenspeicher bleibt wirksam).''',
  '''Enthaltung; (5) aufrufbare Objekte mit `__wrapped__` werden eingewickelt (die Hülle ruft das dekorierte Objekt, der
Zwischenspeicher bleibt wirksam).

**Grenzen nach dem Review** (gemessen vom Prüfer an HEAD, `REVIEW.md`; seine Proben und Ausgaben liegen im Ordner als
`review_*`):
- Nr. 3: Die Behebung von Lücke 1 ersetzt **jedes** zurückgegebene Iterator-Objekt durch einen Generator. Greift die Last
  auf ein Attribut des echten Objekts zu, bricht sie unter der Sonde auf beiden Seiten still ab; eine spätere Änderung
  bleibt unsichtbar (0 Abweichungen statt 6, tragfähig). Eine neue stille Stelle.
- Nr. 4: Bei `__slots__`-Klassen fehlt der Vergleich des Zustands nach dem Aufruf (0 statt 28 Abweichungen) — Lücke 2 ist
  für diese Klassen offen.
- Nr. 7: Koroutinen bleiben Enthaltung „unvergleichbar (asynchron)“, das Urteil trotzdem tragfähig.
Die Aussage „die fünf Lücken sind geschlossen“ gilt deshalb nur für ihre Probenfälle, nicht für die Lückenklassen.''')
R('''  Keine Instanz herstellbar → Enthaltung „keine Instanz (…)“, gezählt.''',
  '''  Keine Instanz herstellbar → Enthaltung „keine Instanz (…)“, gezählt.
- **Grenzen nach dem Review:** `__slots__`-Klassen ohne Zustandsvergleich (Nr. 4); eine Klasse ohne Vertrag mit
  unannotiertem Konstruktor bekommt aus der Signatur eine unbrauchbare Instanz — jede Methode wirft, die Enthaltung heißt
  „nur Fehler“, eine geänderte Methode bleibt still (Nr. 6: 0 statt 4 Abweichungen). Das ist keine „wirklich
  unbeobachtbare“ Stelle im Sinn der Entscheidung.''')
R('''| S-10 | Vertragsprobe mit Last, die A ruft | gebaut; `REF_PAAR`-Umgehung zurückgenommen | Last erreicht alle Funktionen → benannter Prüffehler | Laufweg (`_einzelprobe`), Gegenprobe am Organ |''',
  '''| S-10 | Vertragsprobe mit Last, die A ruft | gebaut; `REF_PAAR`-Umgehung zurückgenommen | Last erreicht alle Funktionen → benannter Prüffehler | Organ mit echter Kammer (`eichproben._einzelprobe`), nicht Laufweg (berichtigt nach Review Nr. 10); Gegenprobe am Organ |''')
R('- Grenze: ein grober Riss (× 9.000).',
  '- Grenze: ein grober Riss (Faktor ≈ 8.200 in der ersten, ≈ 9.100 in der Nachmessung).')
R('''- **Prüfwerk ohne Bereichsordner:** 15 von 30 neuen Tests brachen im ersten Teillauf bei der Basismessung ab''',
  '''- **`TEILLAUF-1.txt` ist unvollständig:** mit doppeltem `-q` ohne Kopf, Befehl und Zusammenfassung; belegt sind nur 103
  Fortschrittspunkte und rc 0 (Review Nr. 18).
- **Prüfwerk ohne Bereichsordner:** 15 von 30 neuen Tests brachen im zweiten Teillauf (`TEILLAUF-2.txt`) bei der Basismessung ab''')

REVIEW_TEXT = '''Ein Durchgang (`REVIEW.md`, Auftrag `REVIEW-AUFTRAG.md`), 07:39–08:36, Kammerproben erst nach dem Ende des
Nachtrag-Jobs (ab 08:11). Ergebnis: **18 Befunde, 4 hoch, 5 mittel, 9 niedrig**; keine Sperre beim Prüfer; Schreibort nur
`REVIEW.md` und `/tmp/review-vor-t4-03/`; `git status` vorher und nachher leer.
- Bestätigt: alle nachgerechneten Zahlen (Regressionen an `d54bf2f` und `0aac612`, Vorher/Nachher 17 Fälle, K2868 2×2,
  Gewinn-Tabelle und K3091-Statistik, Rissprobe, Gegenzeugen, Kasse); „2 von 3“ richtig gemeldet; keine verdeckte
  Regression in den geänderten älteren Tests; die Proben des Gutachtens 02 an HEAD: 14 von 14 wie spezifiziert.
- Bei jedem hohen Befund habe ich in den Ausgaben des Prüfers Urteil und Abweichungszahl von Probe und Kontrolle
  nachgesehen, bevor ich ihn übernahm: x1 überlebt / x1k abgelehnt, x2 überlebt / x2k abgelehnt (`DECKPROBE.json`);
  p18 tragfähig mit 0 / p18b 6 Abweichungen (`SONDENPROBE-3.json`); p19 und p20 tragfähig mit 0 / p19b 28
  (`SONDENPROBE-4.json`). Feinere Zahlen (etwa „14 von 14 gedeckt“) sind die des Prüfers.
- Seine Proben und Ausgaben liegen im Ordner als `review_*` (17 von 17 Dateien kopiert, alle bytegleich mit den
  Originalen unter `/tmp/review-vor-t4-03/`; nicht kopiert: `diffs/` und die Probenwerke `werke*/`, die die Skripte selbst
  erzeugen).
- Nach „ein Review, keine Fix-Kaskade“ baue ich keinen Code mehr: Code-Befunde → `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`
  (R4-1 … R4-14); Aussagen-Befunde → hier berichtigt.

| Nr | Schwere | Befund (kurz) | Umgang |
|---|---|---|---|
| 1 | hoch | Ein Merkmal `weissraum` für Tab, Zeilenumbruch, doppeltes Leerzeichen: ein Test mit doppeltem Leerzeichen deckt eine Tab-/LF-Regression, der Kandidat überlebt (Kontrolle ohne den Test: abgelehnt) | übernommen (x1/x1k); Ergebnis und §3 ergänzt; R4-1 |
| 2 | hoch | Verfälschung je Funktion statt je Aufruf: ein nicht zugesicherter Tab-Aufruf neben einem zugesicherten `normieren("a b")` deckt 6 von 6 | übernommen (x2/x2k); R4-2 |
| 3 | hoch | Iterator-Objekte werden durch Generatoren ersetzt: Last bricht still ab, Änderung unsichtbar | übernommen (p18/p18b); §1; R4-3 |
| 4 | hoch | `__slots__` / `dataclass(slots=True)`: Zustand von `self` nicht verglichen (0 statt 28) | übernommen (p19/p20); §1, §2; R4-4 |
| 5 | mittel | „die fünf Lücken sind geschlossen“ stärker als der Beleg | berichtigt: Titel, Ergebnis, §1 („für ihre Probenfälle“) |
| 6 | mittel | Klasse ohne Vertrag, unannotierter Konstruktor: unbrauchbare Instanz, geänderte Methode still | übernommen (p16/p16b); §2; R4-5 |
| 7 | mittel | Koroutinen: Enthaltung, Urteil trotzdem tragfähig | übernommen (p13); §1; R4-6 |
| 8 | mittel | K2868: woran die Deckung scheiterte (Weißraum oder `null_zahl`), ist nicht belegt | übernommen; §3 nennt die Grenze bereits; R4-7 |
| 9 | mittel | Lücken gegen den Auftrag: TS-Methoden, Doppelprüfung nicht erzwungen, Gewinn-Nachmessung der Generalprobe nie ausgeführt, 2 von 3 | bestätigt, offen (§14) |
| 10 | niedrig | S-10 ist Organ-, nicht Laufweg-Nachweis | §6 berichtigt |
| 11 | niedrig | Annahmegrund nennt einen Gewinn, den die Nachmessung nicht bestätigt (K2904 D1 `bericht`) | übernommen; R4-8 |
| 12 | niedrig | Zweig „Gewinn-Nachmessung ungültig“ ungetestet | übernommen; R4-9 |
| 13 | niedrig | veraltete Kommentare in `aegis.py` (Gewinn uneinig; Deckung „dieselbe Eingabe“) | übernommen; R4-10 |
| 14 | niedrig | Verdrahtungszusicherung prüft nur, dass die Schlüssel da sind | übernommen; R4-11 |
| 15 | niedrig | Verfälschungsproben ohne Obergrenze und ohne Zählung im Urteil | übernommen; R4-12 |
| 16 | niedrig | Iterator-Kappe 50 nicht genannt, Rest unsichtbar | §1 nennt N = 50; R4-13 |
| 17 | niedrig | Formart nur in der Sonde, nicht im Aufzeichner; instabile Funktionen zählen als beobachtet | übernommen (gelesen, nicht gemessen); R4-14 |
| 18 | niedrig | `TEILLAUF-1.txt` unvollständig; §13 nannte den falschen Teillauf | §13 berichtigt |

**Vom Prüfer nicht geprüft, von mir gelesen (nicht gemessen):** Vom Kandidaten mitgebrachte Tests gehen in den
Testbestand (`aegis.py:873`), die Basismessung läuft mit ihm (`:985`), und `behoben` (`:1059`) enthält damit auch diese
Tests — sie können decken. Ein Kandidat kann Nr. 1 und 2 also selbst ausnutzen, indem er einen passenden Test mitbringt.'''

SPERR_TEXT = f'''Zwei Sicherheitssperren bei mir, beide beim Abschluss nach dem Review. Wortlaut aus den gespeicherten Belegen
(`SPERRE-KOPIE-GUTACHTERPROBEN.txt`, `SPERRE-2-BERICHT-ABSCHLUSS.txt`), nicht aus einem neuen Befehl.

**Sperre 1** — Werkzeug `terminal`, gegen 08:40. Zweck: die Proben des Prüfers in den Abschlussordner kopieren, jede
Kopie prüfen und das Protokoll der Ausführungsschicht auszählen. Befehl:
```bash
{befehl_1}
```
Meldung:
> {meldung_1}

**Sperre 2** — Werkzeug `execute_code`, kurz nach 08:44. Zweck: diesen Bericht abschließen (§10, §11, Berichtigungen
nach dem Review), die Spezifikationen anlegen und die Quellenliste des Veröffentlichungsskripts ergänzen. Der Befehl
war das Skript; seine unveränderte Abschrift ist `skript_bericht_abschluss_gesperrt.py` (nicht ausgeführt). Meldung:
> {meldung_2}

**Einordnung:** beide Male Sicherheitsfilter, harte Linie 3. Keiner der Befehle ruft den Dienstprozess auf. Vermuteter
Auslöser von Sperre 2 (nicht geprüft): Das Skript zitierte die Meldung von Sperre 1. Den Auslöser von Sperre 1 kenne
ich nicht. Nicht umgangen: kein Umformulieren, kein Teilbefehl, kein anderes Werkzeug. Nachgesehen um 08:44:08 bzw.
danach: nichts kopiert, nichts geschrieben. Mein Fehler: zweimal unabhängige Handlungen in einem Befehl gebündelt.

**Freigabe Philipp** (für genau diesen Fall, nicht als Dauerregel): die Schritte getrennt, den Wortlaut der Sperren aus
den gespeicherten Dateien übernehmen, das Auszählen des Protokolls der Ausführungsschicht weglassen; sperrt ein
einzelner Schritt, anhalten. Danach als einzelne Schritte, bis zu diesem Bericht ohne weitere Sperre:
1. `mkdir -p` des Ordners für die Proben;
2. `cp -p` der 17 Dateien (Proben, Ausgaben, Skript `lauf_proben.sh`);
3. Prüfung der Kopien mit `cmp`: 17 von 17 bytegleich;
4. Wächter nachgesehen (unten), nur gelesen;
5. dieser Bericht (`skript_abschluss_1_bericht.py`; Wortlaut der Sperren aus den Belegen gelesen);
6. `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md` (Datei geschrieben);
7. Quellenliste des Veröffentlichungsskripts ergänzt (Datei bearbeitet);
8. Veröffentlichung. Ihr Ergebnis (HTTPS bytegleich, Ordnerprüfsumme) steht in `PRUEFSUMME-ORDNER.txt` und in der
   Endmeldung, nicht hier.
Das Protokoll der Ausführungsschicht ist nicht ausgezählt.

**Beim Prüfer:** keine Sperre (`REVIEW.md` → „Sperren: keine“). Er meldet eine Änderung am Protokoll der
Ausführungsschicht, nicht von ihm geschrieben.

**Freigabeabfragen** in dieser Runde: keine außer der Freigabe oben.

**Zwischenbericht-Wächter in dieser Runde** (`~/.hermes/zwischenbericht/ausgeloest.json`: 2 von 8 Einträgen fallen in
diese Runde; die Ordner im Prüfkanal nachgesehen):
- 05:11:04, Werkzeugrunde 113 von 150 (Schwelle 110): `laeufe/biotop-vor-t4-03/zwischenbericht-20260924-051104-r113/`,
  5 Dateien, HTTPS bytegleich 5 von 5, Ordnerprüfsumme `084e8a7e5b6d8b63976e86edb87ace79c31d644c1f825f9e27895a7e64bca8f7`.
- 05:19:06, Werkzeugrunde 141 von 150 (Schwelle 140): `laeufe/biotop-vor-t4-03/zwischenbericht-20260924-051906-r141/`,
  5 Dateien, HTTPS bytegleich 5 von 5, Ordnerprüfsumme `e083ddbd17bde85f4e449eb619fa634cae5a06d098b463ac55512556667a52c1`.
- Beide im ersten Turn dieser Runde, der danach an der Iterationsgrenze (150) endete. Beide tragen eine Übergabe von
  3.647 Byte — so groß war `UEBERGABE.md` im Stand 03:40; sie war zu diesem Zeitpunkt anderthalb Stunden alt (§13).
- Kein Auslöser „Kontextfüllung ≥ 80 %“ und keiner „Verdichtung gescheitert“: Die Verdichtungen um 02:14 und 05:08
  gelangen (§0); vor der um 05:08 stand die Sitzung bei ≈ 505.000 von 1.000.000 Token (`logs/agent.log`).
- Die Abholadressen der beiden `DATEIEN.txt` stehen als ganze Zeilen in `DATEIEN.txt` dieses Ordners.'''

R('‹REVIEW›', REVIEW_TEXT)
R('‹SPERREN›', SPERR_TEXT)
R('''7. **Vorher/Nachher an denselben Testfunktionen:** Die Fälle der Lücken wurden am alten Code aus `git archive 6243377`
   ausgeführt, statt eigene Altfälle zu bauen — dieselben Diffs, dieselbe Last, derselbe Ablauf.''',
  '''7. **Vorher/Nachher an denselben Testfunktionen:** Die Fälle der Lücken wurden am alten Code aus `git archive 6243377`
   ausgeführt, statt eigene Altfälle zu bauen — dieselben Diffs, dieselbe Last, derselbe Ablauf.
8. **Zwischenberichte des Wächters in `DATEIEN.txt`:** Sie liegen im selben Ordner, sind aber eigene Lieferungen mit
   eigener Prüfsumme; `DATEIEN.txt` nennt ihre Abholadressen, das Manifest dieses Ordners umfasst sie nicht.
9. **Nachtrag-Commit `0aac612`** statt Änderung von `d54bf2f`, und die Regression danach noch einmal voll: Die Geschichte
   bleibt unverändert, und die Zahl 533/2/0 gehört zu genau dem Stand, der jetzt HEAD ist.''')
R('''6. **Generalprobe:** Die Gewinn-Nachmessung in `lauf._generation_koerper` ist gelesen, nicht ausgeführt (0 von 16
   Urteilen im Verdrahtungslauf mit Nachmessung).''',
  '''6. **Generalprobe:** Die Gewinn-Nachmessung in `lauf._generation_koerper` ist gelesen, nicht ausgeführt (0 von 16
   Urteilen im Verdrahtungslauf mit Nachmessung).
7. **Die vier hohen Review-Befunde vor T4 beheben** (R4-1 … R4-4): Mit ihnen lässt die Deckung je Muster die K2868-Lage
   durch, sobald ein Kandidat einen Test mit doppeltem Leerzeichen mitbringt, und die Sonde schweigt bei Iterator-Objekten
   und `__slots__`-Klassen. Dazu eine Frage: Soll `weissraum` je Zeichen getrennt werden (Tab, Zeilenumbruch, CR, NBSP,
   doppeltes Leerzeichen), passend zu den Formvarianten?
8. **Sicherheitssperre des Filters für den Dienstprozess auf Befehle ohne Bezug dazu** (Runde 2 beim Prüfer, Runde 3
   zweimal bei mir): als Fehlalarm melden, oder gibt es eine Regel, die ich kennen muss?''')
R('''- **Zwischenmeldung nach der Iterationsgrenze** war richtig als „nicht geliefert“ gekennzeichnet; die Übergabe war dort
  aber zwei Stunden alt.''',
  '''- **Zwischenmeldung nach der Iterationsgrenze** war richtig als „nicht geliefert“ gekennzeichnet; die Übergabe war dort
  aber zwei Stunden alt — und in den beiden Zwischenberichten des Wächters (05:11, 05:19) anderthalb Stunden (§11).
- **Zwei Sicherheitssperren durch gebündelte Befehle** (§11).''')

fehlt = [a[:70] for a, _ in ops if b.count(a) != 1]
assert not fehlt, fehlt
for a, n in ops:
    b = b.replace(a, n)
assert '‹' not in b, re.findall('‹[^›]*›', b)
B.write_text(b)
print('BERICHT.md', len(b.splitlines()), 'Zeilen,', len(b.encode()), 'Byte; Ersetzungen', len(ops), 'von', len(ops),
      '; Platzhalter', b.count('‹'))
