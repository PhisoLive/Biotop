"""Behebungsrunde 5 abschließen (nach dem Review): füllt BERICHT ‹REVIEW›/‹SPERREN›, SPEZIFIKATIONEN ‹REVIEW_SPEZ›,
berichtigt §6 (Review Nr. 9), ergänzt §14 (eigener Fehler: zwei Reviews) und §15 (Entscheidungen zu Runde 6).
Alles oder nichts: jede Ersetzung muss genau einmal treffen, sonst wird nichts geschrieben. Stand davor:
bau/BERICHT-vor-review.md, bau/SPEZIFIKATIONEN-vor-review.md."""
import shutil
from pathlib import Path

A = Path('/root/biotop-vor-t4-05')
B = A / 'BERICHT.md'
S = A / 'SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md'
b, s = B.read_text(), S.read_text()
review = (A / 'bau/R5-REVIEW-ABSCHNITT.md').read_text().rstrip('\n')

SPERREN = ('Keine. Weder der Auftragnehmer (`UEBERGABE.md`, Arbeitsordner: keine Sperrbelege) noch der geltende '
           'Reviewdurchgang (`REVIEW.md`, Abschnitt „Sperren“) wurden durch eine Sicherheitssperre, Freigabeabfrage oder '
           'Formatsperre angehalten. Zeitüberschreitungen eines Werkzeugaufrufs (Review: `warte.sh` nach 420 s) sind '
           'keine Sperren.')

SPEZ = """| R6-6 | **Typtreue Verfälschung** (Entscheidung 1, zusammen mit R6-4): verfälscht wird mit einem Wert desselben Typs und anderen Inhalts, nie mit einem Objekt, das beim Weiterrechnen wirft; ein Test hält nur fest, wenn seine Zusicherung am geänderten Wert fällt. | Review Nr. 1: x5 (`isinstance`) und x5b (Tautologie) überleben durch `aegis.pruefen`, `festhaltend …\\|tab` = `[test_normieren_x]` (`review-proben/kammerprobe05.out.txt:1-2`) | x3k abgelehnt; x3 bleibt abgelehnt | Review 05 Nr. 1 |
| R6-7 | **Undurchsichtige Objekte** (Entscheidung 2): Zustand aus C-Typen über eine bekannte Darstellung (getvalue, str, pickle/`__reduce_ex__`), sonst gezählte Enthaltung — nie „0 Abweichungen“. | p24b (`StringIO`-Argument) und p25 (`Decimal`-Unterklasse): 0 Abweichungen, tragfähig (`kammerprobe05.out.txt:4-5`); lokal 11 blinde Arten (`review-proben/lokal_b.out.txt:2-12`) | Kontrollen `Decimal`, Klasse mit `__slots__` und `__dict__`: gesehen | Review 05 Nr. 2 |
| R6-8 | **Enthaltung einer geänderten Funktion stellt zurück** (Entscheidung 3, mit R6-1): enthält sich eine geänderte Funktion, wird der Kandidat zurückgestellt; enthalten sich nur unveränderte, urteilt der Vergleich am Rest. | a3x: `naechste` geändert und im Sondenausfall — tragfähig, 0 Abweichungen (`kammerprobe05.out.txt:7`) | f1, f2 (unveränderte Funktionen schwer erfassbar): geurteilt statt zurückgestellt | Review 05 Nr. 3, 6 |
| R6-9 | **Ausnahmen nach Typ und Inhalt** (Entscheidung 7). | p26: `ValueError('PLZ …')` vs. `('Ort …')` — 0 Abweichungen (`kammerprobe05.out.txt:6`) | gleiche Meldung: tragfähig | Review 05 Nr. 4 |
| R6-10 | **Zeitgrenze je Funktion** (Entscheidung 3): eine hängende Last trifft nur die hängende Funktion. | d1: `SondeAusgefallen` nach 245 s für den ganzen Kandidaten (`kammerprobe05.out.txt:36`) | eine Last ohne Hänger: unverändert | Review 05 Nr. 5 |
| R6-11 | **Register vollständig, einschließlich Verhandlung** (Entscheidung 6); der Verdrahtungslauf löst eine Verhandlung aus. | Register 10 Einträge; keine Kante aus `lauf._verhandeln` im Verdrahtungsbeleg | — | Review 05 Nr. 7 |
| R6-12 | **Verhaltensändernde Altlast erreichbar** (Entscheidung 5): unabhängiger Test am End- und Ausgangsstand, Kennungen einheitlich, `erlaubt` je Altlast. | Kennungsform `test_x.py::…` vs. Liste `tests/…`; kein Test mit `verhaltensaendernd: true` | nicht verhaltensändernde Altlast (A1) bleibt behoben | Review 05 Nr. 8 |
| R6-13 | **TS-Kanon**: blinde Arten und Fehlalarme; typtreue Verfälschung und Ausnahmeinhalt in TS; TS-Proben zu Entscheidungen 2 und 3. **Vor T5** (Entscheidung 8). | `review-proben/lokal_ts.out.txt` | — | Review 05 Nr. 10 |
| R6-14 | **Zählung an der Vorgeneration des T4-Werks** bei der Aufnahme: unvollständig erfasste Funktionen je Modul (wie w1/w2). | w1 `lagerhaus` 0 von 42, w2 `logmuehle` 0 von 24 | — | Review 05 Nr. 6 |
| R6-15 | **`ITER_KAPPE` an der T4-Last messen** (Vorauslesen bis Element 1.001). | gerechnet, nicht gemessen | — | Review 05 Nr. 11 |

**Unbestätigt** (nur im verworfenen ersten Reviewdurchgang, `REVIEW-verworfen-erster-durchgang.md`; ohne Nachprüfung):

| Nr | Befund (gelesen, nicht gemessen) | Quelle |
|---|---|---|
| U-1 | `os.fork` in einem Werk mit laufenden Threads kann das Kind der Eingrenzung verklemmen. | erster Durchgang Nr. 7 |
| U-2 | Lastaufrufe tragen auch `klein`/`gross`; in x2 sind 16 von 36 ungedeckten Beobachtungen Lastaufrufe (Überstrenge). | erster Durchgang Nr. 11 |
| U-3 | Der TS-Weg prüft nicht „ohne Sonde“; ein Lastabbruch als Werkverhalten wird zur Enthaltung. | erster Durchgang Nr. 12 |
| U-4 | Die Stufen-Zusicherung im Verdrahtungstest filtert `None`. | erster Durchgang Nr. 10 (e) |"""

ERSETZE = [
    (B, '‹REVIEW›', review),
    (B, '‹SPERREN›', SPERREN),
    (B, '- `zahlen` 18,9 ms (Spannweite 0,05 … 0,39, 0 Sperren in 24 Messungen);',
     '- `zahlen` 18,9 ms (Median und Spannweite 0,05 … 0,39 aus 8 Rauschmessungen mit 40 Werten; 0 Sperren in 24\n'
     '  Messungen; über alle 24 Messungen gerechnet 19,0 ms und 0,04 … 0,70 — berichtigt nach Review Nr. 9);'),
    (B, '10. **„Gemessen an einem Kandidaten in T4-Größe“ (Entscheidung 4) ist nicht erfüllt.**',
     '11. **Zwei Reviewdurchgänge statt einem** (`ZWEI-REVIEWS.md`). Der Reviewer startete eine Kammerprobe als\n'
     '    Hintergrundprozess mit Abschlussmeldung; die Meldung band den Chat an seine Sitzung, und zwei Instanzen\n'
     '    arbeiteten im selben Ordner weiter. Es gilt der zweite Durchgang. Regeln ab Runde 6: eigener Ordner je Review,\n'
     '    Prüfung vor dem Start, keine Hintergrundprozesse in Subagenten.\n'
     '10. **„Gemessen an einem Kandidaten in T4-Größe“ (Entscheidung 4) ist nicht erfüllt.**'),
]
neu = {B: b, S: s}
for datei, alt, ersatz in ERSETZE:
    n = neu[datei].count(alt)
    if n != 1:
        raise SystemExit(f'Anker {alt[:60]!r} in {datei.name}: {n} Treffer statt 1 — nichts geschrieben')
    neu[datei] = neu[datei].replace(alt, ersatz)
if neu[S].count('‹REVIEW_SPEZ›') != 1:
    raise SystemExit('‹REVIEW_SPEZ› fehlt — nichts geschrieben')
neu[S] = neu[S].replace('‹REVIEW_SPEZ›', SPEZ)
neu[B] = neu[B].rstrip('\n') + ('\n\n**Entschieden am 24.09.** (Entscheidungen Chat-Claude zu Runde 6): Nr. 1 → (1) mit typtreuer '
                                'Verfälschung; Nr. 2 → (5); Nr. 3 → (4), Eichphase mit Spannweite < 0,25 über 8 Messungen '
                                'und ≥ 10 ms je Stichprobe; Nr. 4 → (8), Kappe am echten T4-Werk; Nr. 5 → (8), TS-Proben vor '
                                'T5. Dazu (2), (3), (6), (7) aus dem Review und die Startregel für T4.\n')
for datei, text in neu.items():
    if '‹' in text:
        raise SystemExit(f'{datei.name} enthält noch Platzhalter — nichts geschrieben')
shutil.copy2(B, A / 'bau/BERICHT-vor-review.md')
shutil.copy2(S, A / 'bau/SPEZIFIKATIONEN-vor-review.md')
for datei, text in neu.items():
    datei.write_text(text)
print('geschrieben:', ', '.join(d.name for d in neu), '| Ersetzungen', len(ERSETZE) + 2)
