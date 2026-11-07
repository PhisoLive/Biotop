from pathlib import Path
import re, py_compile
A = Path('/root/biotop-vor-t4-03')
B = A / 'BERICHT.md'
b = B.read_text()
ops = []
def R(a, n): ops.append((a, n))
R('# Behebungsrunde 3 vor T4: nicht abgenommen — die fünf Lücken der Python-Sonde sind geschlossen (vorher/nachher gemessen), aber K2904/K3091 wieder nur 2 von 3 (Vergleichslast), Methoden nur in Python, zwei Spezifikationen nur am Organ',
  '# Behebungsrunde 3 vor T4: nicht abgenommen — K2904/K3091 wieder nur 2 von 3 (Vergleichslast); die fünf Lücken der Python-Sonde sind für ihre Probenfälle geschlossen, aber das Review hat vier neue gemessen (Deckung: grobes Weißraum-Merkmal, Verfälschung je Funktion; Sonde: Iterator-Objekte, `__slots__`)')
R('- **Die fünf Lücken der Python-Sonde sind geschlossen, je mit einem Fall',
  '- **Die fünf Lücken der Python-Sonde sind für ihre Probenfälle geschlossen, je mit einem Fall')
R('  „nicht eingewickelt (Klasse)“ (§2). T4 ist ein Python-Werk.',
  '  „nicht eingewickelt (Klasse)“ (§2). T4 ist ein Python-Werk. Das Review fand auch in Python eine Lücke: Bei Klassen\n  mit `__slots__` (auch `@dataclass(slots=True)`) wird der Zustand von `self` nicht verglichen (§10 Nr. 4).')
R('  Test je Muster kommt am Prüfwerk durch (§3). **Grenze:**',
  '  Test je Muster kommt am Prüfwerk durch (§3). **Das Review hat zwei Lücken der Regel gemessen:** Ein Test mit doppeltem\n  Leerzeichen deckt einen Rückschritt bei Tab und Zeilenumbruch — die K2868-Lage, der Kandidat überlebt —, und ein Test\n  deckt mit einem Aufruf, den er nicht zusichert (§10 Nr. 1, 2). **Weitere Grenze:**')
R('- **Verdichtung** läuft seit dem Gateway-Neustart (§0).',
  '- **Verdichtung** läuft seit dem Gateway-Neustart (§0).\n'
  '- **Review (ein Durchgang): 18 Befunde, 4 hoch, 5 mittel, 9 niedrig** (§10). Bestätigt: alle nachgerechneten Zahlen des\n'
  '  Berichts; die alten Proben des Gutachtens 02 verhalten sich an HEAD in 14 von 14 Fallläufen wie spezifiziert. Die vier\n'
  '  hohen Befunde sind in der Kammer gemessen; Code baue ich nach dem Review nicht mehr, sie stehen als Spezifikationen in\n'
  '  `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`.\n'
  '- **Eine Sicherheitssperre bei mir** (§11, wörtlich): Die Kopie der Gutachterproben in den Abschlussordner ist blockiert\n'
  '  und nicht umgangen. Die Proben liegen unverändert unter `/tmp/review-vor-t4-03/`; dieser Ordner enthält sie nicht.')
R('Gesamtzahl war dieselbe wie im verhaltensgleichen Fall).',
  'Gesamtzahl war dieselbe wie im verhaltensgleichen Fall). Iteratoren werden bis zum 50. Element verglichen (Kappe N = 50);\ndarüber hinaus ist eine Änderung unsichtbar (Review Nr. 16).')
R('''Enthaltung; (5) aufrufbare Objekte mit `__wrapped__` werden eingewickelt (die Hülle ruft das dekorierte Objekt, der
Zwischenspeicher bleibt wirksam).''',
  '''Enthaltung; (5) aufrufbare Objekte mit `__wrapped__` werden eingewickelt (die Hülle ruft das dekorierte Objekt, der
Zwischenspeicher bleibt wirksam).

**Grenzen nach dem Review** (gemessen vom Prüfer an HEAD, `REVIEW.md`; die Proben liegen unter `/tmp/review-vor-t4-03/`,
§11):
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
- Jeden hohen Befund habe ich an den Ausgaben des Prüfers nachgesehen (`DECKPROBE.json` x1/x1k/x2/x2k,
  `SONDENPROBE-3.json` p18/p18b, `SONDENPROBE-4.json` p19/p19b/p20), bevor ich ihn übernahm.
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
SPERR_TEXT = '''**Bei mir: eine Sicherheitssperre** (Beleg `SPERRE-KOPIE-GUTACHTERPROBEN.txt`, dort der Befehl vollständig):
- Befehl: `mkdir -p /root/biotop-vor-t4-03/review-proben && cd /tmp/review-vor-t4-03 && for f in *.py *.json *.txt *.sh;
  do cp -p "$f" /root/biotop-vor-t4-03/review-proben/; done; …` samt sha256-Prüfung der Kopien und einem Lesen von
  `/root/.local/share/tirith/log.jsonl` (Zahl der Einträge) per `python -` mit Heredoc.
- Meldung: „Blocked: command or referenced script cannot restart, stop, or uninstall the gateway from inside the gateway
  process. The gateway would kill this command before it could complete (SIGTERM propagates to child processes). Run
  `hermes gateway restart` from a separate shell outside the running gateway.“
- Einordnung: Sicherheitsfilter, harte Linie 3. Der Befehl enthält keinen Gateway-Befehl; der Auslöser ist mir unbekannt
  (dieselbe Meldung traf in Runde 2 das nur lesende `r6.sh` des Prüfers). **Nicht umgangen:** kein Umformulieren, kein
  Teilbefehl, kein anderes Werkzeug. Nachgesehen um 08:44:08: `review-proben/` existiert nicht, es wurde nichts kopiert.
- Folge: Die Gutachterproben (Belege der Befunde 1–8, 16) sind **nicht** in diesem Ordner; sie liegen unverändert unter
  `/tmp/review-vor-t4-03/` (Schreibort-Nachweis in `REVIEW.md`). Wartet auf Philipp: Freigabe der Kopie; danach ein
  eigener Nachtragsordner mit eigener Prüfsumme, dieser Ordner bleibt unverändert.
- Mein Fehler dabei: Ich habe die Kopie mit einem unabhängigen Lesebefehl in einen Befehl gebündelt; so wartet jetzt
  auch die Kopie.

**Beim Prüfer:** keine Sperre (`REVIEW.md` → „Sperren: keine“). Er meldet eine Änderung am Protokoll der
Ausführungsschicht (`/root/.local/share/tirith/log.jsonl`), nicht von ihm geschrieben.

**Freigabeabfragen** in dieser Runde: keine.'''
R('‹REVIEW›', REVIEW_TEXT)
R('‹SPERREN›', SPERR_TEXT)
R('''7. **Vorher/Nachher an denselben Testfunktionen:** Die Fälle der Lücken wurden am alten Code aus `git archive 6243377`
   ausgeführt, statt eigene Altfälle zu bauen — dieselben Diffs, dieselbe Last, derselbe Ablauf.''',
  '''7. **Vorher/Nachher an denselben Testfunktionen:** Die Fälle der Lücken wurden am alten Code aus `git archive 6243377`
   ausgeführt, statt eigene Altfälle zu bauen — dieselben Diffs, dieselbe Last, derselbe Ablauf.
8. **Veröffentlichen ohne die Gutachterproben:** Die Sperre betrifft nur die Kopie (§11); nach der Arbeitsregel wartet nur
   diese Handlung. `REVIEW.md` nennt die Proben mit Pfad und Ergebnis; die Rohdateien folgen nach Freigabe als Nachtrag.
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
8. **Kopie der Gutachterproben freigeben** (§11), dann Nachtragsordner.
9. **Die Gateway-Sperre auf Befehle ohne Gateway-Bezug** (zweimal, Runde 2 und 3): Soll ich sie als Fehlalarm melden, oder
   gibt es eine Regel, die ich kennen muss?''')
fehlt = [a[:70] for a, _ in ops if b.count(a) != 1]
assert not fehlt, fehlt
for a, n in ops:
    b = b.replace(a, n)
assert '‹' not in b
B.write_text(b)

S = A / 'SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md'
S.write_text('''# Spezifikationen für den nächsten Auftrag (aus der Behebungsrunde 3 vor T4, Review und eigene offene Punkte)

Stand: Kern-Commit `0aac612` (Code wie `d54bf2f`). Nach „ein Review, keine Fix-Kaskade“ ist nach dem Review kein Code
gebaut. R4-1 … R4-7 sind **gemessen** (Proben des Prüfers in der Kammer, Ausgaben unter `/tmp/review-vor-t4-03/`; die
Kopie in den Abschlussordner ist gesperrt, BERICHT §11); die übrigen sind gelesen oder eigene offene Punkte. Erster
Schritt des nächsten Auftrags: jede Probe als pytest-Spezifikation fassen (rot an `0aac612`, Gegenprobe grün).

| Nr | Spezifikation | Beleg an `0aac612` | Gegenprobe |
|---|---|---|---|
| R4-1 | Merkmale feiner: Weißraum je Zeichen (`tab`, `zeilenumbruch`, `cr`, `nbsp`, `doppelleer`), gleich in Sonde und Aufzeichner, passend zu den Formvarianten. Ein Test mit doppeltem Leerzeichen deckt keinen Tab-/LF-Rückschritt | Review Nr. 1: x1 überlebt, 14 von 14 `ValueError` gedeckt | x1k: ohne den Test abgelehnt |
| R4-2 | Verfälschung je Aufruf mit dem Muster der Abweichung (nicht je Funktion); nur Fehlschläge in der `call`-Phase zählen; Klassen je Test und Funktion im Urteil | Review Nr. 2: x2 überlebt, 6 von 6 gedeckt | x2k: ohne den Tab-Aufruf abgelehnt |
| R4-3 | Nur echte Generatoren auslesen und ersetzen; andere Iterator-Objekte durchreichen, als Enthaltung „Iterator-Objekt“ zählen; Lastabbruch unter der Sonde, während das Messgerät die Last fehlerfrei lief = Messgerätausfall | Review Nr. 3: p18 0 Abweichungen, tragfähig | p18b: 6 Abweichungen |
| R4-4 | Zustand nach dem Aufruf auch für `__slots__` und `dataclass(slots=True)` (`_veraenderlich`, `schnappschuss`, `zuruecksetzen`, `_stoeren`) | Review Nr. 4: p19/p20 0 Abweichungen | p19b: 28 |
| R4-5 | Instanz aus der Signatur: weitere Argumentlisten versuchen, bis ein Methodenaufruf inhaltlich ist; eigener Enthaltungsgrund „Instanz ohne inhaltlichen Aufruf“ | Review Nr. 6: p16 0, „1 von 2“ | p16b: 4 |
| R4-6 | Koroutinen mit eigener Ereignisschleife beobachten; sonst: ist eine *geänderte* Funktion unbeobachtet, enthält sich das Urteil statt „tragfähig“ | Review Nr. 7: p13 tragfähig | — |
| R4-7 | K2868 mit gestelltem deckendem Test je Muster nachspielen (mit und ohne doppeltes Leerzeichen, mit und ohne `gewicht: 0`); Klassen der aufgezeichneten Aufrufe im Beleg | Review Nr. 8; BERICHT §3 (`null_zahl` in 40 von 40) | — |
| R4-8 | Annahmegrund nur mit bestätigten Gewinnbereichen | Review Nr. 11: K2904 D1 `bericht` −20 % → Nachmessung −8,4 % | — |
| R4-9 | Test: ungültige Gewinn-Nachmessung → zurückgestellt (Annahmepfad) bzw. Messgerätausfall (Generalprobe) | Review Nr. 12: 0 Tests | — |
| R4-10 | Kommentare in `aegis.py` an den Code angleichen (gepoolt; Deckung je Muster) | Review Nr. 13 | — |
| R4-11 | Verdrahtungslast mit einem Kandidaten im Gewinnband; `gewinn` ≠ `None` verlangen (Generalprobe einmal wirklich ausführen) | Review Nr. 9c, 14: 0 von 16 | — |
| R4-12 | Kappe für Verfälschungsproben mit gezählter Enthaltung; Zahl der Kammerläufe je Kandidat im Urteil | Review Nr. 15 | — |
| R4-13 | Iterator-Kappe als Teil-Enthaltung zählen („mehr“) | Review Nr. 16: p14 0, „1 von 1“ | — |
| R4-14 | Formart nur ergänzen, wenn `klassen_von` sie für den Wert liefert; instabile Funktionen aus „beobachtet“ nehmen | Review Nr. 17 (gelesen) | — |
| R4-15 | Vergleichslast der Nische „schnell“ vergrößern, bis K2904/K3091 3 von 3 gleich entschieden werden (Streuung der Quote < Abstand zur Schwelle) | BERICHT §4: K3091 3 von 9 über 0,85, s = 0,035 | K2904 0 von 9 |
| R4-16 | Muster: Merkmale nicht variierter Argumente — Entscheidung Philipp/Chat-Claude vor dem Bau | BERICHT §3, §14 Nr. 2 | — |
| R4-17 | Methoden von Klassen in TypeScript (Entscheidung 3) | BERICHT §2 | — |
| R4-18 | Doppelprüfung der Gegenzeugen verbindlich einhängen (Versiegelung/Aufnahme künftiger Testwerke) | BERICHT §5, §14 Nr. 4 | — |
| R4-19 | S-12 und S-3 (Wurzelmodul) durch den Laufweg belegen | BERICHT §6 | — |
''')
V = A / 'veroeffentlichen.py'
v = V.read_text()
for a, n in (("    'skript_veroeffentlichen.py': A / 'veroeffentlichen.py',\n",
              "    'skript_veroeffentlichen.py': A / 'veroeffentlichen.py',\n"
              "    'SPERRE-KOPIE-GUTACHTERPROBEN.txt': A / 'sperre/SPERRE-KOPIE-GUTACHTERPROBEN.txt',\n"
              "    'SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md': A / 'SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md',\n"),
             ("'skript_* = Skripte aus dem Arbeitsordner; *-arbeitsbaum = Läufe vor dem Commit; review_* = Proben des Gutachtens.',",
              "'skript_* = Skripte aus dem Arbeitsordner; *-arbeitsbaum = Läufe vor dem Commit. Die Proben des Gutachtens fehlen: '\n"
              "          'ihre Kopie ist gesperrt (SPERRE-KOPIE-GUTACHTERPROBEN.txt, BERICHT §11).',")):
    assert v.count(a) == 1, a[:60]
    v = v.replace(a, n)
V.write_text(v); py_compile.compile(str(V), doraise=True)
print('bericht', len(b.splitlines()), 'zeilen; platzhalter', b.count('‹'), '| review-proben dir:', (A / 'review-proben').exists())
