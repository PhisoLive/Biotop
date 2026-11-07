# Unabhängige Eichungsprüfung: NICHT BESTANDEN

**passed=false. Vier Logikfehler; keine bestätigten neuen Sicherheitsfunde.**
`kammer.py:103 token=_ZAEHLUNGEN.set(...)` ist ein ContextVar-Rücksetz-Token,
kein Zugangstoken. Keine Implementierung, kein Schreibzugriff auf das geprüfte Repository.

## Blocker

1. **EICH-1 — Bereichssperre umgehbar.** `biotop/kern/messgeraet.py:432,463–465`
   und `biotop/lauf.py:325–330` prüfen den deklarierten statt des tatsächlichen
   Änderungsbereichs. Ein als **alpha** geführter Diff verändert **beta**, obwohl
   beta gesperrt ist. Der ausgeführte Unit-Durchlauf endet **vorgelegt** und
   schreibt beta. Ohne den neuen Skip lehnt derselbe Messinput die Zeitgrenze ab.
2. **EICH-2 — Gen0-Fehlschlag gilt als Vorbedingung.**
   `biotop/organe/vorspann.py:227–229` verlangt nur einen Ergebnisdatensatz.
   Im Repro: `erreicht=false`, **0 von 1** Mutanten gefangen; danach trotzdem
   CLI-`mass` **rc=0**, Maß gebunden, Lauf **bereit**.
3. **EICH-3 — Eichvertrag nachträglich austauschbar.**
   `biotop/organe/vorspann.py:54–59,241–245` bindet die aktuelle Vertragsdatei
   nicht. Reguläres `vertraege.einlegen` nach dem Vorspann ändert die Prüfsumme;
   Gen0, Freeze und Generationsgate akzeptieren weiter **bestanden** bei gültiger
   Protokollkette. Kein nachträgliches Manipulieren des Nachweises nötig.
4. **EICH-4 — unbrauchbare Vertragsgegenprobe.**
   `biotop/organe/eichproben.py:349–360` kopiert Imports und Testfunktion, aber
   keine benötigte Modulkonstante. Ein normaler Test mit `EINGABE=2` erzeugt
   dadurch in **beiden** Vertragsvarianten einen `NameError` im Test selbst.
   Der ursprüngliche Verbraucher besteht nach Anpassung; deshalb ergibt das
   Originalprädikat dennoch **True/False**, obwohl der benannte Vertrag weiter
   defekt ist. Lokale pytest-Rohbelege liegen bei; die Prädikat-Messhülle ist
   ausdrücklich ein Unit-Input, keine vorgetäuschte Docker-Messung.

## Verifiziert und begrenzt

- Mitgelieferte fokussierte Suite: **116/116 Unit-Fälle bestanden**.
- Eigene Repros: **4 Fehler / 2 bestandene Fälle**; zusätzlicher Isolations- und
  Nichtausführungscheck: **5/5 bestanden**. Einzelne IDs und Ergebnisse in `BELEGE.json`.
- Positive Route Vorspann → Gen0 → Freeze → Generationskörper ausgeführt;
  fehlende Reihenfolge, Instrument-/Maßmanipulation und fehlende Kontrollen geprüft.
- Vier Probeprädikate und ihre Konstruktion gelesen. Die vollständigen vier
  Dockerpaare **nicht ausgeführt**; fehlende Ausführung wird nicht als negative
  Gegenprobe oder Abnahmegrün gezählt. Normkontrolle ohne Klassifikatoreingabe,
  reine Bool-Hüllen am Qualitätsgate und lückenhafte Rohbelege weiterer
  Vorspannstufen stehen als Empfehlungen in `REVIEW.json`.
- **0 Dockerläufe, 0 Netzaufrufe, 0 bezahlte Modellaufrufe.** Nur selbst angelegte
  synthetische Fixtures/private Datenbanken; kein produktiver Bestand verwendet.
- Alle **125 Quelldateien** sind nach Inhalt, Größe und mtime unverändert.
  Diff: **24 Dateien, +2264/−215 Zeilen**.
  Quellsnapshot: **13168 physische Zeilen**; vollständige
  Dateiliste, Token-LOC-Definition, Prüfsummen und Outputzählung in `BELEGE.json`.

## Dateien und Wiederholung

- Ergebnis mit exakten Fundstellen und minimalen Repro-Befehlen:
  `/root/reparatur-01/review-01/pruefer-eichung/REVIEW.json`
- Vollständige LOC-/Test-/Quellbelege: `/root/reparatur-01/review-01/pruefer-eichung/BELEGE.json`
- Ungekürzte Ausgaben: `provided-unit.stdout.txt`, `independent-review.stdout.txt`,
  `supplemental.stdout.txt`, jeweilige stderr- und JUnit-Dateien.
- Vertragszeugen: `contract-local-pytest-raw.json`, `contract-junit-summary.json`.
- Repros: `test_review.py`; sichere Auswahlaufrufe vollständig in `REVIEW.json`.
- Manifest: `/root/reparatur-01/review-01/pruefer-eichung/SHA256SUMS.txt`

Die vier roten eigenen Tests prüfen die geforderte Sperrwirkung; ihr Exit 1
ist der reproduzierte Produktbefund, kein Sammel-/Importfehler. Unveränderte
Altprobleme werden nicht als zusätzliche Reparaturblocker gezählt.
