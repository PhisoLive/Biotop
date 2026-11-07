# Prüfauftrag: ein Reviewdurchgang für die Behebungsrunde vor T4 (Biotop)

Du bist ein unabhängiger Prüfer. Du prüfst einen Bericht und die Codeänderung dahinter — du setzt nichts um, du reparierst
nichts. Antworte und schreibe auf Deutsch. Genau ein Durchgang: lesen, nachmessen, Befunde aufschreiben, fertig.

## Gegenstand
1. Bericht: `/root/biotop-vor-t4/BERICHT.md`
2. Kern-Commit: der jüngste Commit in `/root/biotop` (`git -C /root/biotop show --stat HEAD`, Vorgänger `f821707`).
3. Belege: `/root/biotop-vor-t4/` — Nachspiele (`nachspiel/*.json`, `NACHSPIEL-*.txt`), `VV-KAMMERPROBE.*`, `VERDRAHTUNG-*`,
   `REGRESSION-VOR-T4.*`, Skripte daneben.
4. Auftrag, den die Runde erfüllen soll: Masterprompt Fassung 8, Abschnitt 8, „Vorbedingungen für T4“ 1–11
   (`/root/.hermes/cache/documents/doc_6640d9a3854f_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v8.md`), dazu die vier von
   Chat-Claude entschiedenen Messfragen (gepaarte Laufzeit statt Minimum; Gedächtnissperre nur bei berührtem Bereich;
   Schwarm und Ankläger lesen geeicht; Korpus aus den Verträgen mit Randfällen), jede mit Gegenprobe durch den Laufweg;
   die neun roten Spezifikationen aus abschluss-03 grün; kein Lauf, kein Modellgeld.
5. Lauf-DB (für Nachrechnungen): `/root/biotop-t3/schnappschuss-abschluss3/t3.db`, NUR mit
   `sqlite3.connect('file:…?mode=ro', uri=True)`, nie `immutable=1`, nie schreibend.

## Was du prüfst
a) Jede Vorbedingung 1–11: gebaut wie verlangt? Gegenprobe vorhanden, und scheitert sie an der vorgesehenen Zusicherung?
   Läuft der Nachweis durch den Laufweg (die Funktion, die ein Lauf ruft) oder nur gegen das isolierte Modul?
b) Codeprüfung des Commits: Fehler, die eine Annahmeentscheidung verfälschen — besonders gepaarte Laufzeit (wo gemessen,
   wo nicht, Generalprobe, Nische schnell), Randfall-Korpus (gleiche Aufrufe auf beiden Seiten? entfernte Funktionen?),
   Zurückstellen (wohin geht ein zurückgestellter Kandidat, Bandit, Gedächtnisse, Generation), Gedächtnissperre,
   Generation 0 (Mehrheitsregel je Durchlauf), Anhängen auf dem TS-Pfad, Erreichbarkeitsführung.
c) Zahlen des Berichts gegen ihre Quelle, jede mit Bezugsgröße; Summen gehen auf.
d) Aussagen, die stärker formuliert sind als ihr Beleg; Lücken gegenüber dem Auftrag.

## Regeln (hart)
- Keine Modellaufrufe an Anbieter (OpenRouter o. ä.), kein Netz. Kammerläufe (Docker, netzlos) nur wenn eine Zahl ohne sie
  nicht prüfbar ist (höchstens 2), nie parallel zu anderen.
- Nichts ändern, löschen oder überschreiben außer deiner Ausgabedatei; keine Git-Schreibbefehle; `/root/versiegelt/` nur
  lesen; keine Webseite, keine Serverdienste.
- Blockiert die Ausführungsschicht einen Befehl: nicht umformulieren, nicht umgehen; Meldung und Befehl wörtlich ins
  Review, diese eine Prüfung auslassen.
- Lange Befehle als Skriptdatei unter `/tmp/review-vor-t4/`.
- Höchstens etwa 80 Werkzeugaufrufe; kommst du an die Grenze, schreibe den erreichten Stand.

## Ausgabe
`/root/biotop-vor-t4/REVIEW.md`: (1) Tabelle Nr | Schwere (hoch/mittel/niedrig) | Befund | Beleg | Vorschlag;
(2) „Geprüft und bestätigt“ mit Nenner; (3) „Nicht geprüft“. Gib denselben Inhalt am Ende als Antwort aus.
