# Integration: Eichung 01

## Umfang und Konfliktregel

Basis ist ausschließlich `b42dc941e7fcb66632ba6a0e13b8df106a270a31`. Die Quellkopie stammt aus `git archive`, nicht aus einer Kopie von `.git` oder `daten/`. Vier vollständige geänderte Dateien werden unter `lieferung/dateien/` geliefert. `lauf.py`, `__main__.py`, `gedaechtnis.py`, das Messgerät sowie `_angriff`, `_ansage`, `bisherige_behauptungen`, `aufnahmesperre` wurden in diesem Teilauftrag nicht geändert.

**Nicht die vollständige Aegis-Datei über den inzwischen integrierten A/C-Stand kopieren.** Sie ist nur die vollständige Referenzfassung gegen die eingefrorene Basis. `AEGIS-PROBEOPTION.diff` enthält ausschließlich die drei Einfügungen in `pruefen`: optionale Parameter, Markierungswache und explizite Auswahl des festen Probeangriffs. Beim Zusammenführen den aktuellen `_angriff(...)`-Aufruf einschließlich `kandidat_id`/`ansage_kontext` im normalen `else`-Zweig unverändert erhalten. Ebenso aktuelle Ansage-Nummer und beide C-Aufnahmestellen erhalten.

Die anderen Dateien aus `dateien/` sind `biotop/organe/eichproben.py`, `biotop/organe/kammer.py` und `tests/test_eichproben.py`. Alternativ zuerst den vollständigen Git-Diff mit `git apply --check` im Integrationsstand prüfen. Der Teilagent hat keinen Patch an `/root/biotop` angewendet.

## API

```python
proben(con, lauf_id, werk_id, pfad, paket, bereiche,
       bstrassen, basis, ausgang, ref, tausch, generation=0) -> dict
```

Positionsparameter unverändert, keine neue Pflichtkonfiguration. `basis` und `ausgang` sind explizite frische Messungen. `laeufe.mass` darf NULL sein; Generation-0-Zeilen werden nicht gelesen. Ablaufpflicht Gen−1→Gen0→Freeze→Generation bleibt beim Eltern-Gate.

Die übergebene Verbindung muss außerhalb einer Transaktion stehen (sonst lauter Fehler statt hängendem SQLite-Backup). `proben` kopiert Werk und SQLite-Verbindung, versiegelt nur in der Kopie und erstellt für **jeden der acht Fälle** wieder eigene Kopien. Sämtliche Aegis-, Ansage-, Immun-, Gedächtnis- und Kandidatennebenwirkungen bleiben dort. Temporäre Kopien werden geschlossen/verworfen. **Auch Ergebnis-/Eichkostenzeilen werden nicht in die übergebene DB geschrieben**; der Eltern-Vorspann persistiert die Rückgabe als Abnahmebeleg.

Rückgabe:
- `proben` und `gegenproben`: jeweils genau `nebenwirkung`, `regression`, `norm`, `vertrag`.
- Jede ausgeführte Zeile: `ausgefuehrt`, `pruefbar`, `bestanden`, `kandidat` (nur private ID!), `status`, `grund`, `befund`, `diff`, `belege`, `kammer` (reale Container/RC/stdout/stderr), `kammerlaeufe`, `modellaufrufe`, `kosten_eur`, `dauer_s`.
- `belege.urteil` ist das originale Aegis-Urteil; `belege.messung` die zurückgelesene private Kandidatenmessung mit `_basis_paar`, `_dateien`, `_urteil_f2`.
- Bei Bau-/Infrastrukturfehlern: `ausgefuehrt=False`, `pruefbar=False`, `bestanden=False`, `status='prueffehler'`, `fehlerart`; bereits ausgeführte Kammern werden dennoch mitgezählt. Ein fehlender Gegenstand erzeugt acht explizit nicht ausgeführte Zeilen.
- `bestanden`/`lauf_startet` sind nur bei **4×True und 4×False mit jeweils ausgeführt=True, prüfbar=True und exakter Schlüsselmenge** wahr. `lauf_startet` bleibt eine kompatible Aussage, keine selbst erteilte Ausführungsberechtigung.
- `kosten` summiert ausschließlich diese acht Fälle; Eingangsmessung und übrige pytest-Läufe sind nicht darin enthalten.

```python
aegis.pruefen(..., extra_code=None, *,
              probe_ohne_modell=False, probe_angriff=None)
```

Beide neuen Parameter sind optional. Der modellfreie Pfad ist nur mit explizitem `probe_ohne_modell=True` und Kandidatenfeld `ist_probe=1` zulässig; sonst `ValueError` vor Anklage/Modell. Der feste `probe_angriff` durchläuft danach die originale Norm-/C-/Immun-/Maßlogik. Keine Modellglobal-Änderung. Für Norm wird ein eigener Kandidatentest **und** derselbe feste Angriff benutzt, um Nichtaufnahme und offenen Normeintrag nachzuweisen. Der Norm-Gegenfall lässt diese Tests im Aegis-Eingang weg, behält aber die reale Verhaltensänderung und extern ausgeführte Zeugen.

`kammer.zaehlung()` ist ein kontextlokaler Zähler an der tatsächlichen Ausführung; verschachtelte Aufrufe werden einschließlich ihrer Rückgabedaten erfasst. Normaler `kammer.ausfuehren` bleibt signaturkompatibel.

## Prüfbefehl

Nur an Privatkopien. Der folgende Befehl ist im Teilordner ausgeführt worden (Rohausgabe `28-endstand-gruen.txt`, 21 Fälle ohne Skip). Der Echtwerktest kopiert die private DB erneut und legt einen neuen privaten Lauf mit Budget 0 und NULL-Maß an; er führt keinen ursprünglichen Lauf fort.

```bash
cd /root/reparatur-01/teil-eichung/repo
export TMPDIR=/root/reparatur-01/teil-eichung/tmp
export BIOTOP_DB=/root/reparatur-01/teil-eichung/unbenutzt.db
export PYTHONPATH=/root/reparatur-01/teil-eichung/repo
export BIOTOP_EICHWERK=/root/reparatur-01/teil-eichung/werk-lauf25-kopie
export BIOTOP_EICHDB=/root/reparatur-01/ausgang.db
export BIOTOP_EICHWERK_ID=22
export BIOTOP_EICHBELEG=/root/reparatur-01/teil-eichung/ausgaben/integration-echtes-werk.json
/root/reparatur-01/venv/bin/python -m pytest tests/test_eichproben.py -v -s --tb=short
```

Ohne `BIOTOP_EICHWERK` wird nur der zusätzliche Echtwerktest übersprungen; das ist **keine Ersatzabnahme**. Die vertrauliche DB ist absichtlich **nicht** Bestandteil des Lieferpakets. Für Eltern-Wiederholung dessen eigene Quell-/Werk-/DB-Kopien verwenden und PYTHONPATH entsprechend setzen.

## Auswertungsgrenze

Die Batterie prüft mechanische Test-/Pareto-/Norm-/Vertragsentscheidungen, keine neue Rauschkalibrierung. Gemessene Grenzmaßbefunde bleiben vollständig in `belege.urteil.mass.grenzen_gerissen` und den Rohgründen stehen. Ein nachgewiesener Normpfad mit Zuwachs 0 und Nichtaufnahme wird nicht durch einen unabhängigen Zeitbefund zum nicht ausgeführten Normpfad umetikettiert. Der zeitbehaftete Positiv- und Gegenfall ist eigens real getestet. Das Eltern-Gate muss seine separate Rausch-/Bereichssperre weiterhin durchsetzen.

Die Zielauswahl bleibt AST-basiert innerhalb des versiegelten Bereichspaars. Im echten Werk ist es `bericht→lager`; es wurde nicht auf `preise` umgestellt, als zuerst eine skalar aufrufbare freie Funktion fehlte. Stattdessen wurde die vorhandene Methode `Lager.bestand` unterstützt. A-Ausgangsdefekte sind ausdrücklich gesetzte **private Eichfixtures**, keine behaupteten vorgefundenen Produktfehler. Gegenprobe bedeutet hier absichtlich falsches Bestehensprädikat desselben Prüfers, nicht pauschal irgendeine abgelehnte Änderung.
