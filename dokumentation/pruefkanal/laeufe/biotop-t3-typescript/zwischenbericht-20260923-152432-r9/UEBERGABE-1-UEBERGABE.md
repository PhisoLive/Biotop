# Übergabe abschluss-03 (T3 TypeScript), Stand 2026-09-23 nachmittags

Diese Datei ist so geschrieben, dass eine frische Sitzung ohne Vorgeschichte übernehmen kann.

## Erledigt (Belege in /root/biotop-t3/abschluss3/)
- **Kern-Commit `f821707`:** Maßeichung und Verhaltensvergleich hängen in `aegis.pruefen`; dazu `nachspiel.py` und der
  Verdrahtungstest.
  - Regression: 404 bestanden, 2 übersprungen.
  - Eichpfad: 4 von 4 am Commit.
  - Verdrahtungstest rot gegen `1cf2eb1` und rot in der Pflicht-Gegenprobe.
- **Nachspiele:** 33 Fälle durch `aegis.pruefen` (`AUSWERTUNG-ABSCHLUSS3.txt`, `NACHSPIEL-*.txt`, `nachspiel*/`).
- **Lauf 38 bereinigt:**
  - `AUSWERTUNG-ABSCHLUSS3.*`, gerechnet am Schnappschuss mit WAL: `/root/biotop-t3/schnappschuss-abschluss3/t3.db`.
  - S1–S5 selbst gemessen: `S1S5-ABSCHLUSS3.*`.
  - Zusatzmessungen: `ZUSATZ-ABSCHLUSS3.*`.
- **Review:** ein Durchgang, `REVIEW-03.md`: 21 Befunde, davon 3 hoch, 9 mittel, 9 niedrig. Noch nicht in den Bericht
  eingearbeitet.
- **Entscheidungen von Chat-Claude (23.09.):**
  - Sperre 3 wird nicht aufgelöst; die Dateien in `lauf38/` werden nicht verwendet.
  - Laufzeit: Median mehrerer Messungen je Seite, als erste Änderung vor T4. Gegenprobe: K2904 und K3091 werden gleich
    entschieden.
- **Dauerregel:** Zwischenbericht spätestens bei 120 von 150 Werkzeugrunden.
  - Wächter: `/root/.hermes/scripts/zwischenbericht_waechter.py`.
  - Tests: `/root/.hermes/zwischenbericht/test_waechter.py`.
  - Auftrag: `/root/.hermes/zwischenbericht/auftrag.json`.

## Läuft
- `job5.sh`: `gen0_ursache.py` klärt die Ursache von „0 von 100“ in Lauf 37; `umformung_lauf38.py` misst K3045, K3212,
  K3260, K3324 und K3106 nach. Ausgaben: `GEN0-URSACHE.*` und `UMFORMUNG-LAUF38.*`, Status in `JOB5.txt`.

## Offen, in dieser Reihenfolge
1. Wächter:
   - Tests grün machen;
   - Cron-Job minütlich, ohne Modell;
   - Herzschlag aus Cron belegen (`~/.hermes/zwischenbericht/herzschlag.json`, Feld `eltern`);
   - einen echten Zwischenbericht mit `--sofort` auslösen.
2. `ABSCHLUSS-03.md` überarbeiten:
   - Review-Befunde einarbeiten;
   - Kasse: die 49 WAL-Zeilen sind in 9,728638 € enthalten;
   - Befund zu Generation 0;
   - Umformungen;
   - Entscheidungen von Chat-Claude;
   - Wächter;
   - Liste der Vorbedingungen für T4.
3. `SPERREN.md`: Sperre 5 (Formatsperre im Review) nachtragen.
4. Veröffentlichen mit `abschluss03_veroeffentlichen.py`:
   - QUELLEN um `REVIEW-03.md`, `GEN0-URSACHE.*`, `UMFORMUNG-LAUF38.*`, die Wächter-Dateien und `KASSE-WAL` ergänzen;
   - der Zielordner darf nicht existieren.
5. Endmeldung: `…/abschluss-03/DATEIEN.txt` und `ABSCHLUSS-03.md` als ganze URL-Zeilen, dazu die Ordnerprüfsumme.

## Nicht verwenden
`/root/biotop-t3/abschluss3/lauf38/` (Sperre 3).
