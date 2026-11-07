# BIOTOP-LAGE-01 · Fassung 2 · `INVENTAR-TEIL2-01.md`

- **Inhalt:** Abschnitt 5 · Entwurf I, Stück 2 von 3
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Skript `entwurf/inventar/inventar.py` (Subagent Teil I), ausgeführt von Hermes zum Stichzeitpunkt (R191). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/inventar/lauf-stich-v3/INVENTAR-TEIL2.md` · 33290 B · SHA-256 `ce235064884c677292856afa386d6ec3612cb7e200fad8eca7b798d08cdbb65f`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (32 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
> INVENTAR Teil 2 von 3 (INVENTAR-TEIL1.md … INVENTAR-TEIL3.md)

## 5. I4 Fassungen und Auftragsdateien

Quellen: (a) `arbeit/dokumente/` — Wortlaut der Dokumente aus der Sitzungsdatenbank (R15, R17); (b) Suche nach Dateiname (Typregeln unten) und nach Inhalt (erste Zeile „# INFINITE EVOLUTION“ oder „# … Auftrag …“) in 67 Wurzeln: `/root/biotop`, Arbeitsordner `/root/biotop-*`, `/root/phase-4-*`, `/root/reparatur-0*`, `/root/wiedereinstieg*`, `/root/gesamtstand*`, `/root/uebungswerk*`, `/root/versandwerk*`, `auftrag/`, `arbeit/dokumente/` und Dokumentenspeicher `/root/.hermes/cache/documents` (beide nur mit „biotop“ im Inhalt), Prüfkanal `biotop-*`/`gedaechtnis` (ohne den eigenen Ordner), Biotop-Ordner in `/tmp`; ohne .git, .mypy_cache, .pytest_cache, .venv, __pycache__, coverage, dist, node_modules, site-packages, venv. Zeitpunkt 2026-09-25 19:45:17.
**Anzahl:** 6165 *.md/*.txt gesehen, 147 Treffer, 88 verschiedene Inhalte; ohne „biotop“ im Inhalt ausgelassen: 3 (anderes Vorhaben). *gerechnet*

**Masterprompt-Fassungen** (SHA-256 des Wortlauts ohne und mit abschließendem Zeilenumbruch; „Plattenkopien“ = Dateien mit gleichem SHA-256):

| Fassung | eingegangen | Bytes | SHA-256 (ohne NL) | Stand-Zeile | Plattenkopien |
|---|---|---|---|---|---|
| v1 | 18.09. 20:59 | 28754 | 93d358cdda6473f91fda795392e509212f75f1f9678bef31593cad9104fe1ea8 | Stand: 18.09.2026 · Fassung 1 · Auftraggeber: Philipp Zöllis | keine |
| v2 | 19.09. 00:36 | 37835 | acc42ad73f6111a3922993aaadb94ebb12aaeeb995f445f3fe7e8abaab1b4b9d | Stand: 19.09.2026 · Fassung 2 · Auftraggeber: Philipp Zöllis | keine |
| v3 | 19.09. 02:23 | 43497 | ca74ed53c33fd68f1ce1a5b172262197a173c118b1099a991a7dac0f350373a2 | Stand: 19.09.2026 (nach dem Nachlauf) · Fassung 3 · Auftragg | keine |
| v4 | 19.09. 12:39 | 53416 | ff1cda438d09c1b440d32700d1723b8e8df0daf6f45a7e2251372e035042e886 | Stand: 19.09.2026 (nach Phase 2) · Fassung 4 · Auftraggeber: | keine |
| v5 | 19.09. 19:35 | 64873 | a34d7e1ad4532fc1ea11fb805b3ef56d2ec09b0b1febad3dc3af1854f9f5035e | Stand: 19.09.2026 (nach Phase 3) · Fassung 5 · Auftraggeber: | keine |
| v6 | 20.09. 00:18 | 78968 | 3f63dec2a7d6f82e932699907dab42d71148fe84ba907a13c505fa2c010bd483 | Stand: 19.09.2026 (nach dem Nachlauf zu Phase 3) · Fassung 6 | /root/phase-4-vorbedingung-1/uebergabe-quellen/MASTERPROMPT-FASSUNG-6.md; https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/quellen/MASTERPROMPT-FASSUNG-6.md; https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6-01.md; /tmp/biotop-phase4-lektuere-mm6_llag/Masterprompt-v6.md |
| v7 | 21.09. 02:14 | 85728 | 0d3a07327b05da232adc49d56cf98e1369f04693c9e857b9e8199d558d38c6c1 | Stand: 21.09.2026 · Fassung 7 · Auftraggeber: Philipp Zöllis | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/MASTERPROMPT-v7.md |
| v8 | 23.09. 15:53 | 94876 | 4168a35ede38c31fe4fad21844105a148da5b5aa0d69d2672f29b774b7a67cc9 | Stand: 23.09.2026 · Fassung 8 · Auftraggeber: Philipp Zöllis | keine |

Bruchstücke (Masterprompt-Dokumente unter 10.000 Bytes, aus Verdichtungen): 2 — INFINITE-EVOLUTION-BIOTOP-Masterprompt-v1.md (4672 Bytes, 19.09. 14:01), INFINITE-EVOLUTION-BIOTOP-Masterprompt-v4.md (1500 Bytes, 19.09. 14:01)

**Typregeln (Auslegung Hermes, nach Dateiname):** Masterprompt: `(?i)masterprompt`; Spezifikation nächster Auftrag: `(?i)spezifikationen-naechster-auftrag`; Bauauftrag: `^BAU-.*`; Reviewauftrag: `(?i)^(review-auftrag|pruefauftrag)`; Auftraggeber-Wortlaut: `(?i)^auftraggeber-wortlaut`; Auftrag: `(?i)((^|[-_])(teil)?auftrag([-_.]|$)|auftrags(grenze|form|regeln|praezisierung))`; Dokument Chat-Claude/Philipp: `^(doc_[0-9a-f]+_)?(\d{4}-\d\d-\d\d_\d{6}_)?(PRUEFUNG\d?_|ABNAHME_|WIEDEREINSTIEG_|ANTWORT_W|GEDAECHTNIS_Hermes)`; Nachfrage/Antwort: `^(NACHFRAGE|ANTWORT)-\d+`; Übergabe: `(?i)uebergabe`. Treffer nur nach Inhalt: Typ aus der ersten Zeile.

| Typ | Datum (mtime) | Bytes | SHA-256 (16) | Fundorte | erster Fundort |
|---|---|---|---|---|---|
| Masterprompt-Fassung v6 | 20.09. 05:01 | 78969 | effefeec0fe2ea06 | 4 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6-01.md … |
| Dokument Chat-Claude/Philipp | 20.09. 05:17 | 8212 | 4920ade0d64feb24 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/quellen/doc_599e9e97ca3f_WIEDEREINSTIEG_Hermes_2026-09-20.md |
| Dokument Chat-Claude/Philipp | 20.09. 05:17 | 6476 | 7151e454a18622e5 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/quellen/doc_c8bde0a20a81_GEDAECHTNIS_Hermes_2026-09-20.md |
| Masterprompt-Auftrag/Auszug | 20.09. 07:52 | 2091 | 4a1fe8dabf154cb3 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/MASTERPROMPT-ABGLEICH-01.md |
| Auftrag | 20.09. 15:31 | 1677 | 9a3dc946a8805986 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/AUFTRAG-01.md |
| Auftrag | 20.09. 15:59 | 1311 | 7574f7d41c95feb7 | 2 | /root/reparatur-01/teil-acb/ORIGINALREPO-ABWEICHUNG.md … |
| Auftrag | 20.09. 16:01 | 13017 | 2b8dc4961d65cfb5 | 2 | /root/reparatur-01/teil-acb/BERICHT.md … |
| Dokument Chat-Claude/Philipp | 20.09. 16:51 | 10993 | 26412d2923debfbe | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-04/historische-referenzquellen/doc_f18e4c5d9f14_ABNAHME_Vorbedingung-1_2026-09-20.md |
| Auftraggeber-Wortlaut | 20.09. 17:40 | 1015 | ba2dc43ac778f112 | 4 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/auftragseingrenzung-01/AUFTRAGGEBER-WORTLAUT.txt … |
| Auftrag | 20.09. 17:40 | 2568 | c645ec16c661b831 | 5 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/auftragseingrenzung-01/AUFTRAGSGRENZE.md … |
| Auftraggeber-Wortlaut | 20.09. 18:24 | 1023 | 68d5c0f380479b54 | 6 | /root/reparatur-01/nachbesserung-02/messung/lieferung/auftrag/AUFTRAGGEBER-WORTLAUT.txt … |
| Auftraggeber-Wortlaut | 20.09. 18:38 | 990 | 86385f6d457428a3 | 5 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/auftragseingrenzung-02/AUFTRAGGEBER-WORTLAUT.txt … |
| Auftrag | 20.09. 20:55 | 981 | 8de7e6ece5b4c13b | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-02/AUFTRAG.md |
| Auftrag | 20.09. 22:37 | 1018 | 825f361caf589ebe | 3 | /root/phase-4-vorbedingung-1/AUFTRAG-REGELN.md … |
| Übergabe | 20.09. 22:37 | 31533 | 55f7c5441c727863 | 1 | /root/phase-4-vorbedingung-1/abschluss-entwurf/UEBERGABE-PHASE-4.md |
| Reviewauftrag | 20.09. 22:37 | 4982 | 3fafd0b4ee4fc90e | 2 | /root/phase-4-vorbedingung-1/review/PRUEFAUFTRAG.md … |
| Übergabe | 20.09. 22:48 | 32268 | 00a46e857745088b | 2 | /root/phase-4-vorbedingung-1/UEBERGABE-PHASE-4.md … |
| Masterprompt-Auftrag/Auszug | 20.09. 22:49 | 10696 | 202149ea99a319d0 | 1 | /root/phase-4-vorbedingung-1/belege/MASTERPROMPT-F6-AUSZUG.md |
| Reviewauftrag | 20.09. 23:07 | 6526 | 3cdee2c0b12c6037 | 3 | /root/phase-4-vorbedingung-1/nachtrag-01/entwurf/REVIEW-AUFTRAG.md … |
| Übergabe | 20.09. 23:11 | 1520 | 8e0656f4a050c2b5 | 1 | /root/phase-4-vorbedingung-1/nachtrag-01/entwurf/UEBERGABE-PHASE-4.md |
| Übergabe | 20.09. 23:39 | 1507 | 10212164f24d9814 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/nach-reparatur-02/abschluss-02/UEBERGABE-PHASE-4.md |
| Übergabe | 21.09. 00:09 | 3588 | b71376b41f4528cd | 3 | /root/phase-4-vorbedingung-1/uebergabe-abnahme-01/UEBERGABE-PHASE-4.md … |
| Masterprompt-Fassung v7 | 21.09. 02:24 | 85729 | a3b3ac0c17371306 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/MASTERPROMPT-v7.md |
| Reviewauftrag | 23.09. 14:18 | 5947 | b18b60535d928281 | 2 | /root/biotop-t3/abschluss3/REVIEW-AUFTRAG-03.md … |
| Übergabe | 23.09. 15:24 | 2784 | e3981dd560055395 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/zwischenbericht-20260923-152432-r9/UEBERGABE-1-UEBERGABE.md |
| Auftrag | 23.09. 15:40 | 6539 | 574153a5603dec0d | 2 | /root/biotop-t3/abschluss3/SPERREN.md … |
| Übergabe | 23.09. 15:47 | 867 | 6976b427b89ef0cc | 2 | /root/biotop-t3/abschluss3/UEBERGABE.md … |
| Reviewauftrag | 23.09. 17:15 | 3226 | 113f2eeaec2c33d1 | 2 | /root/biotop-vor-t4/REVIEW-AUFTRAG-VOR-T4.md … |
| Übergabe | 23.09. 21:32 | 2591 | f3213dcea33e6bb5 | 6 | /tmp/waechter-nachspiel/akte/laeufe/biotop-vor-t4/zwischenbericht-20260923-160100-r1-verdichtung/UEBERGABE-1-UEBERGABE.md … |
| Übergabe | 23.09. 22:00 | 2645 | d025b36c129021d9 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4/zwischenbericht-20260923-220002-r110/UEBERGABE-1-UEBERGABE.md |
| Übergabe | 23.09. 22:27 | 3148 | 7c36255be16b7d32 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4/UEBERGABE.md |
| Übergabe | 23.09. 22:27 | 3240 | 4eeb0eb4eda98e1b | 1 | /root/biotop-vor-t4/UEBERGABE.md |
| Übergabe | 23.09. 22:54 | 2015 | 83b5e1c5baad5e92 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-02/zwischenbericht-20260923-225416-r13-verdichtung/UEBERGABE-1-UEBERGABE.md |
| Reviewauftrag | 24.09. 00:31 | 5310 | 6c66cc130822f39e | 2 | /root/biotop-vor-t4-02/REVIEW-AUFTRAG.md … |
| Übergabe | 24.09. 00:48 | 3471 | 80dceb12f041a256 | 2 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-02/zwischenbericht-20260924-004847-r104-kontext80/UEBERGABE-1-UEBERGABE.md … |
| Übergabe | 24.09. 02:07 | 3445 | 6a74664282aa4c85 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-02/zwischenbericht-20260924-020708-r1-verdichtung/UEBERGABE-1-UEBERGABE.md |
| Spezifikation nächster Auftrag | 24.09. 02:10 | 3156 | 80345cc98a470c92 | 2 | /root/biotop-vor-t4-02/SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md … |
| Übergabe | 24.09. 02:10 | 3269 | fb9a9a3667befbf8 | 2 | /root/biotop-vor-t4-02/UEBERGABE.md … |
| Übergabe | 24.09. 05:11 | 3647 | 5eb78b8ac53be854 | 2 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-03/zwischenbericht-20260924-051104-r113/UEBERGABE-1-UEBERGABE.md … |
| Reviewauftrag | 24.09. 07:38 | 7650 | f9a080507a81e9e0 | 2 | /root/biotop-vor-t4-03/REVIEW-AUFTRAG.md … |
| Spezifikation nächster Auftrag | 24.09. 11:43 | 4248 | 4ce052612995d855 | 2 | /root/biotop-vor-t4-03/SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md … |
| Übergabe | 24.09. 11:44 | 10583 | f4aa205c84f47b8b | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-03/UEBERGABE.md |
| Übergabe | 24.09. 11:44 | 11029 | a2537809fc16a53f | 2 | /root/biotop-vor-t4-03/UEBERGABE.md … |
| Übergabe | 24.09. 14:17 | 8248 | c4049e31c917f346 | 2 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-04/zwischenbericht-20260924-141737-r103-kontext80/UEBERGABE-1-UEBERGABE.md … |
| Reviewauftrag | 24.09. 15:08 | 7046 | 147bf60c00cdfb88 | 2 | /root/biotop-vor-t4-04/REVIEW-AUFTRAG.md … |
| Übergabe | 24.09. 15:11 | 10412 | 3786716cecec0e18 | 2 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-04/zwischenbericht-20260924-151154-r22-kontext80/UEBERGABE-1-UEBERGABE.md … |
| Übergabe | 24.09. 16:10 | 11607 | bbdceb01116c5c80 | 2 | /root/biotop-vor-t4-04/UEBERGABE.md … |
| Spezifikation nächster Auftrag | 24.09. 17:19 | 3060 | b33a8637105303b4 | 2 | /root/biotop-vor-t4-04/SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md … |
| Masterprompt-Auftrag/Auszug | 24.09. 18:29 | 8912 | 888ab89a27871f31 | 2 | /root/biotop-vor-t4-05/bau/MASTERPROMPT-V8-TOR4.txt … |
| Reviewauftrag | 24.09. 19:48 | 7119 | c9487878650f6245 | 2 | /root/biotop-vor-t4-05/REVIEW-AUFTRAG.md … |
| Übergabe | 24.09. 20:33 | 7559 | 28b5a1080d705204 | 3 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-05/zwischenbericht-20260924-203327-r1-verdichtung/UEBERGABE-1-UEBERGABE.md … |
| Übergabe | 24.09. 21:41 | 8459 | 8430df03b5878315 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-05/zwischenbericht-20260924-214148-r2-verdichtung/UEBERGABE-1-UEBERGABE.md |
| Auftrag | 24.09. 21:50 | 2955 | f0b9cfa6c240a310 | 2 | /root/biotop-vor-t4-05/bau/SPEZIFIKATIONEN-vor-review.md … |
| Übergabe | 24.09. 21:50 | 9650 | 0f7c2d22d752e9ba | 2 | /root/biotop-vor-t4-05/UEBERGABE.md … |
| Spezifikation nächster Auftrag | 24.09. 23:44 | 6682 | e8906c54ccc84efa | 2 | /root/biotop-vor-t4-05/SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md … |
| Übergabe | 25.09. 00:06 | 7727 | 724ed0053fada518 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-06/zwischenbericht-20260925-000624-r29-verdichtung/UEBERGABE-1-UEBERGABE.md |
| Bauauftrag | 25.09. 00:17 | 8949 | 2bf51fa55f3d0106 | 1 | /root/biotop-vor-t4-06/BAU-S2-TOR4.md |
| Bauauftrag | 25.09. 00:17 | 5948 | 9dd730081a30224e | 1 | /root/biotop-vor-t4-06/BAU-S3-STUFE2.md |
| Bauauftrag | 25.09. 00:22 | 12558 | 1ca56afa889ca453 | 1 | /root/biotop-vor-t4-06/BAU-S1-SONDE.md |
| Übergabe | 25.09. 00:28 | 9686 | 5124105d070c9d33 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-06/zwischenbericht-20260925-002824-r0-verdichtung/UEBERGABE-1-UEBERGABE.md |
| Übergabe | 25.09. 01:08 | 10969 | ea5394e0f09ff7f0 | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-06/zwischenbericht-20260925-010825-r0-verdichtung/UEBERGABE-1-UEBERGABE.md |
| Übergabe | 25.09. 01:12 | 12946 | ebcf423d271f60da | 1 | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-06/zwischenbericht-20260925-011225-r12-verdichtung/UEBERGABE-1-UEBERGABE.md |
| Übergabe | 25.09. 03:44 | 4069 | 9d85a47f2fab39cf | 1 | /root/biotop-vor-t4-06/bau/S1-UEBERGABE-LESEN.txt |
| Bauauftrag | 25.09. 03:54 | 6107 | 4b49e45e1bb1def3 | 1 | /root/biotop-vor-t4-06/BAU-S1-FORTSETZUNG.md |
| Bauauftrag | 25.09. 05:06 | 12420 | 741cdb0f5f8db88d | 1 | /root/biotop-vor-t4-06/BAU-S4-VERDRAHTUNG.md |
| Bauauftrag | 25.09. 08:44 | 9495 | 8fdac4b10952a5f7 | 1 | /root/biotop-vor-t4-06/BAU-S1B-M2B.md |
| Bauauftrag | 25.09. 12:51 | 10219 | 341e5869a1c3ef0d | 1 | /root/biotop-vor-t4-06/BAU-S1C-UNBEOBACHTET.md |
| Übergabe | 25.09. 12:52 | 24382 | 09e213d6d916c761 | 1 | /root/biotop-vor-t4-06/UEBERGABE.md |
| Auftrag | 25.09. 14:44 | 41239 | 58ba8834b8c3ec08 | 2 | /root/sicherung/biotop-lage-01/auftrag/BIOTOP-LAGE-01-Auftrag-v2.md … |
| Masterprompt-Fassung v1 | 25.09. 15:18 | 28754 | 93d358cdda6473f9 | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-18_205908_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v1.md |
| Masterprompt-Fassung v3 | 25.09. 15:18 | 43497 | ca74ed53c33fd68f | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-19_022342_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v3.md |
| Masterprompt-Fassung v2 | 25.09. 15:18 | 37835 | acc42ad73f6111a3 | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-19_003630_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v2.md |
| Masterprompt-Fassung v4 | 25.09. 15:18 | 53416 | ff1cda438d09c1b4 | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-19_123925_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v4.md |
| Masterprompt-Bruchstück | 25.09. 15:18 | 1500 | 31ebecd20f1776ff | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-19_140146_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v4.md |
| Masterprompt-Bruchstück | 25.09. 15:18 | 4672 | 9f931fca28205438 | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-19_140146_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v1.md |
| Masterprompt-Fassung v5 | 25.09. 15:18 | 64873 | a34d7e1ad4532fc1 | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-19_193553_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v5.md |
| Masterprompt-Fassung v6 | 25.09. 15:18 | 78968 | 3f63dec2a7d6f82e | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-20_001844_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6.md |
| Dokument Chat-Claude/Philipp | 25.09. 15:18 | 10377 | d899daffa7a9fef2 | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-20_024630_PRUEFUNG4_Vorbedingung-1_2026-09-20.md |
| Dokument Chat-Claude/Philipp | 25.09. 15:18 | 8103 | ad26f5ff6b276101 | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-20_020147_PRUEFUNG2_Vorbedingung-1_2026-09-20.md |
| Dokument Chat-Claude/Philipp | 25.09. 15:18 | 9352 | 842383d1c08e1ab2 | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-20_014755_PRUEFUNG_Vorbedingung-1_2026-09-20.md |
| Dokument Chat-Claude/Philipp | 25.09. 15:18 | 8407 | a7ac16861fc2982b | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-20_022543_PRUEFUNG3_Vorbedingung-1_2026-09-20.md |
| Dokument Chat-Claude/Philipp | 25.09. 15:18 | 8435 | 060090b0631b0903 | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-20_040048_PRUEFUNG6_Lauf-25_2026-09-20.md |
| Dokument Chat-Claude/Philipp | 25.09. 15:18 | 10992 | 8a5a470f5a5ddac5 | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-20_045016_ABNAHME_Vorbedingung-1_2026-09-20.md |
| Dokument Chat-Claude/Philipp | 25.09. 15:18 | 8211 | a70abb8b962cb939 | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-20_045401_WIEDEREINSTIEG_Hermes_2026-09-20.md |
| Dokument Chat-Claude/Philipp | 25.09. 15:18 | 8449 | 55b23bc0c9a191e1 | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-20_052516_PRUEFUNG_Wiedereinstieg_2026-09-20.md |
| Masterprompt-Fassung v7 | 25.09. 15:18 | 85728 | 0d3a07327b05da23 | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-21_021434_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v7.md |
| Masterprompt-Fassung v8 | 25.09. 15:18 | 94876 | 4168a35ede38c31f | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-23_155353_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v8.md |
| Auftrag | 25.09. 15:18 | 41238 | 7d55e3e2143ab87d | 1 | /root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-25_144420_BIOTOP-LAGE-01-Auftrag-v2.md |

Vollständige SHA-256 und alle Fundorte: `LISTEN`, Abschnitt 6.

## 6. I5 Werke

Quellen: Tabelle `werke` der vier Zweige (`SELECT id, name, pfad, quelle, aufgenommen_am, sprache, status`), Werkordner auf der Platte (`/root/uebungswerk*`, `/root/versandwerk*`, `/root/biotop/daten/werke/*`, `/root/phase-4-vorbedingung-1/privat/werke/*`, `/root/reparatur-02/privat-cli/werk`). Zeitpunkt 2026-09-25 19:45:07.
**Anzahl:** 24 Werke in der Kasse (entdoppelt nach Name und Aufnahmezeit), 35 Werkordner auf der Platte. *gerechnet* Art nach Name (Auslegung Hermes: „lagerhaus*“, „logmuehle*“ = Übungswerk, „…-t<n>…“ = Testwerk T<n>). Umfang (Dateien, Zeilen, Tests) → `LAGE` FK25.

| Werk | Art | Sprache | aufgenommen | Zweige/id | Pfad | Quelle |
|---|---|---|---|---|---|---|
| lagerhaus | Übungswerk lagerhaus | Python | 18.09. 23:44 | S1 V1 R1 T1 | /root/biotop/daten/werke/lagerhaus | /root/uebungswerk |
| lagerhaus-ohne-tests | Übungswerk lagerhaus | Python | 19.09. 00:04 | S2 V2 R2 T2 | /root/biotop/daten/werke/lagerhaus-ohne-tests | /tmp/werk-ohne-tests-xf0aaqmv/w |
| lagerhaus-kasse | Übungswerk lagerhaus | Python | 19.09. 00:04 | S3 V3 R3 T3 | /root/biotop/daten/werke/lagerhaus-kasse | /root/uebungswerk |
| lagerhaus-kasse2 | Übungswerk lagerhaus | Python | 19.09. 00:11 | S4 V4 R4 T4 | /root/biotop/daten/werke/lagerhaus-kasse2 | /root/uebungswerk |
| lagerhaus-nachlauf | Übungswerk lagerhaus | Python | 19.09. 00:48 | S5 V5 R5 T5 | /root/biotop/daten/werke/lagerhaus-nachlauf | /root/uebungswerk |
| lagerhaus-nachlauf2 | Übungswerk lagerhaus | Python | 19.09. 01:20 | S6 V6 R6 T6 | /root/biotop/daten/werke/lagerhaus-nachlauf2 | /root/uebungswerk |
| lagerhaus-nachlauf8 | Übungswerk lagerhaus | Python | 19.09. 01:33 | S7 V7 R7 T7 | /root/biotop/daten/werke/lagerhaus-nachlauf8 | /root/uebungswerk |
| lagerhaus-nachlauf9 | Übungswerk lagerhaus | Python | 19.09. 01:53 | S8 V8 R8 T8 | /root/biotop/daten/werke/lagerhaus-nachlauf9 | /root/uebungswerk |
| lagerhaus-kasse3 | Übungswerk lagerhaus | Python | 19.09. 02:09 | S9 V9 R9 T9 | /root/biotop/daten/werke/lagerhaus-kasse3 | /root/uebungswerk |
| lagerhaus-p2 | Übungswerk lagerhaus | Python | 19.09. 02:41 | S10 V10 R10 T10 | /root/biotop/daten/werke/lagerhaus-p2 | /root/uebungswerk-p2 |
| lagerhaus-p2-13 | Übungswerk lagerhaus | Python | 19.09. 03:47 | S11 V11 R11 T11 | /root/biotop/daten/werke/lagerhaus-p2-13 | /root/uebungswerk-p2 |
| lagerhaus-p3-14 | Übungswerk lagerhaus | Python | 19.09. 13:03 | S12 V12 R12 T12 | /root/biotop/daten/werke/lagerhaus-p3-14 | /root/uebungswerk-p3 |
| lagerhaus-p3-15 | Übungswerk lagerhaus | Python | 19.09. 13:09 | S13 V13 R13 T13 | /root/biotop/daten/werke/lagerhaus-p3-15 | /root/uebungswerk-p3 |
| lagerhaus-p3-16 | Übungswerk lagerhaus | Python | 19.09. 13:26 | S14 V14 R14 T14 | /root/biotop/daten/werke/lagerhaus-p3-16 | /root/uebungswerk-p3 |
| logmuehle-17 | Übungswerk logmuehle | Python | 19.09. 13:55 | S15 V15 R15 T15 | /root/biotop/daten/werke/logmuehle-17 | /root/uebungswerk2 |
| lagerhaus-p3-18 | Übungswerk lagerhaus | Python | 19.09. 16:41 | S16 V16 R16 T16 | /root/biotop/daten/werke/lagerhaus-p3-18 | /root/uebungswerk-p3b |
| lagerhaus-p3-19 | Übungswerk lagerhaus | Python | 19.09. 17:06 | S17 V17 R17 T17 | /root/biotop/daten/werke/lagerhaus-p3-19 | /root/uebungswerk-p3c |
| lagerhaus-p3-20 | Übungswerk lagerhaus | Python | 19.09. 17:40 | S18 V18 R18 T18 | /root/biotop/daten/werke/lagerhaus-p3-20 | /root/uebungswerk-p3d |
| lagerhaus-p3-22 | Übungswerk lagerhaus | Python | 19.09. 22:57 | S19 V19 R19 T19 | /root/biotop/daten/werke/lagerhaus-p3-22 | /root/uebungswerk-nachlauf |
| logmuehle-23 | Übungswerk logmuehle | Python | 19.09. 23:32 | S20 V20 R20 T20 | /root/biotop/daten/werke/logmuehle-23 | /root/biotop/daten/werke/logmuehle-17 |
| lagerhaus-zeile8-24 | Übungswerk lagerhaus | Python | 20.09. 00:57 | S21 V21 R21 T21 | /root/biotop/daten/werke/lagerhaus-zeile8-24 | /root/uebungswerk-p3 |
| lagerhaus-c-25 | Übungswerk lagerhaus | Python | 20.09. 03:13 | S22 V22 R22 T22 | /root/biotop/daten/werke/lagerhaus-c-25; /root/reparatur-02/privat-cli/werk | /root/uebungswerk-p3 |
| lagerhaus-vorbedingung1-26 | Übungswerk lagerhaus | Python | 20.09. 21:31 | V23 | /root/phase-4-vorbedingung-1/privat/werke/lagerhaus-vorbedingung1-26 | /root/phase-4-vorbedingung-1/privat/werkquelle |
| versandwerk-t3-02 | Testwerk T3 | TypeScript | 22.09. 15:43 | T23 | /root/biotop/daten/werke/versandwerk-t3-02 | /root/versandwerk-t3-02 |

- Werkordner auf der Platte ohne Eintrag in einer Kasse (weder Pfad noch Quelle): 1: `/root/versandwerk-t3`
- Werke der Kasse, deren Pfad fehlt: 0.
- T4, T5, T6: NICHT GEFUNDEN (kein Werk in einer Kasse, kein Ordner unter /root mit t4/t5/t6 außer den Arbeitsordnern vor-t4).

## 7. I6 Commits und Änderungen

Quellen: `git --no-optional-locks -C /root/biotop log --all --since=2026-09-18T00:00:00+02:00 --format=%H…%s` (rc 0), `git log --all --no-walk --format=%H %D` (rc 0), `git rev-parse HEAD` (rc 0), `git rev-parse --symbolic-full-name --all` (rc 0), `git log --all --since=2026-09-21 --name-only` (rc 0); Dateisystem `os.walk(/root/biotop)` ohne .git, __pycache__, node_modules. Zeitpunkt 2026-09-25 19:45:06 / 2026-09-25 19:45:18.
**Anzahl:** 75 Commits seit 18.09. bis zum Stich (*abgelesen*); HEAD `0c2f058d57f6`; Referenzen: refs/heads/main; Markierungen (tags): 0; Spitzen mit Dekoration: `0c2f058` HEAD -> main.
Autoren: hermes <hermes@biotop> (46), Hermes (Biotop) <hermes@biotop.local> (19), hermes <hermes@local> (10) (*gerechnet*).
**Geänderte Dateien seit 21.09. 00:00 bis zum Stich:** 202 (zusammen 2803263 Bytes); nach dem Stich geändert: 0 (*abgelesen*, mtime). Liste mit Zeit und Größe: `LISTEN`, Abschnitt 5.
**Nicht Eingechecktes:** aus `/root/sicherung/biotop-lage-01/tmp/git-status-stich.txt`: 25 Zeilen, je Kennung: ` M` 19, `??` 6
Geänderte Dateien je oberster Ebene: daten 79, tests 55, biotop 54, pruefung_vorbedingung1 11, kammer 3 (*gerechnet*).

## 8. I7 Gedächtnis

Quelle: `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/` (Verzeichnis), Zeitpunkt 2026-09-25 19:45:12. **Anzahl:** 5 Dateien (*abgelesen*).

| Datei | Art | Nummer | Datum (mtime) | Bytes | SHA-256 (16) |
|---|---|---|---|---|---|
| DATEIEN-01.txt | DATEIEN | 1 | 2026-09-20 05:17:33 | 238 | 20ffc24c09285e84 |
| PRUEFSUMME-ORDNER-01.txt | PRUEFSUMME-ORDNER | 1 | 2026-09-20 05:17:33 | 341 | 2e5760a73bcf7f85 |
| REGELN-01.md | REGELN | 1 | 2026-09-20 05:17:33 | 4504 | 7de0078ce031bf2d |
| STAND-01.md | STAND | 1 | 2026-09-20 05:17:33 | 4386 | 6facfcc2de75857f |
| UNTERBAU-01.md | UNTERBAU | 1 | 2026-09-20 05:17:33 | 4965 | 841daa1b260b5ca4 |

Nummern je Art lückenlos ab 1: DATEIEN: ja, PRUEFSUMME-ORDNER: ja, REGELN: ja, STAND: ja, UNTERBAU: ja (*gerechnet*).

## 9. I8 Kosten

Quellen: Kasse der vier Zweige (entdoppelt wie I1), Tabelle `eichkosten` (entdoppelt nach allen Spalten), Umrechnung des Biotops: `USD_JE_EUR = 1.08` (/root/biotop/biotop/kern/kasse.py Zeile 20; Kosten € = USD ÷ 1.08), OpenRouter-Anzeige aus `arbeit/OR-STAND.jsonl` (2 Abfragen durch Hermes, dieses Skript fragt OpenRouter nicht ab).
**Anzahl:** 6919 Buchungen, Summe 18.8147 € bis zum Stich (*gerechnet*: Summe kosten_eur der entdoppelten Buchungen). Je Lauf → `KASSE-TEIL1.csv`; je Tag → Tagesbilanz (Abschnitt 10, Abgleich 7). Aufbau `KASSE`: zuerst die Läufe (Summe je Lauf), dann alle entdoppelten Buchungen (Spalten der Tabelle kasse, dazu Lauf und Zweige), zuletzt die Tabelle eichkosten (je Zweig); jeder Teil beginnt mit der Kopfzeile seiner Tabelle.
Eichkosten: 149 Zeilen, davon mit Modellaufrufen 8; bei 8 von 8 stehen im Zeitfenster [erstellt_am − dauer_s − 2 s, erstellt_am + 1 s] so viele aufeinanderfolgende Kassenbuchungen desselben Laufs wie Modellaufrufe, deren Summe kosten_eur der Eichkosten-Zeile auf 1e-6 € gleicht (die Tabelle eichkosten rundet auf 6 Nachkommastellen) — diese Eichkosten sind in der Kassensumme enthalten, nicht zusätzlich (*gerechnet*, Auslegung Hermes).

## 10. Abgleiche 1–9

### Abgleich 1 — Lauf ↔ Chronik ↔ Ordner

- Lauf → Ordner: zugeordnet 40 von 40; davon über Zeitfenster oder Zweig-Arbeitsordner 40, nur über Nennung außerhalb des Zeitfensters 0; offen 0. *gerechnet*
- Ordner → Lauf oder Auftrag: 20 Ordner; über Lauf 8, über Auftrag (Nennung) 12, offen 0. *gerechnet*
- Lauf ↔ Chronik: 40 von 40 Läufen in einer Chronikzeile genannt; ohne Zeile: 0 (*gerechnet*; Laufnummern in Chronikzeilen, Nummer 26 ist mehrdeutig).

### Abgleich 2 — Laufnummern lückenlos

| Zweig | Nummern | fehlend | doppelt |
|---|---|---|---|
| STAMM | 1–25 (25 Nummern) | keine | keine |
| VB1 | 1–26 (26 Nummern) | keine | keine |
| R02 | 1–26 (26 Nummern) | keine | keine |
| T3 | 1–38 (38 Nummern) | keine | keine |

- Über alle Zweige: Nummern 1–38, fehlend: keine; mehrfach vergeben (verschiedene Läufe mit derselben Nummer): 26: R02/26, VB1/26, T3/26. Erklärung: Die Zweige VB1, R02 und T3 sind Kopien des Stamms nach Lauf 25 und zählen je für sich weiter (R25); die Nummer allein ist deshalb keine eindeutige Kennung — Zuordnungstafel in Abgleich 8. *gerechnet*
- In Ordnertexten genannte Laufnummern ohne Lauf in einer der vier Kassen: 0 (biotop-phase-3-nachlauf, biotop-t3-typescript); 52 (biotop-t3-typescript); 53 (biotop-t3-typescript); 59 (biotop-t3-typescript); 60 (biotop-t3-typescript); 62 (biotop-t3-typescript); 66 (biotop-t3-typescript); 84 (biotop-t3-typescript); 128 (biotop-t3-typescript); 848 (biotop-wiedereinstieg-2026-09-20-01, gedaechtnis); 991 (biotop-vor-t4) (*gerechnet*; das Muster „Lauf n“/„Läufe n–m“ trifft auch Zahlen anderer Bedeutung — je Nummer offen, bis die Fundstelle gelesen ist).

### Abgleich 3 — Fassungen v1 bis zur höchsten, Verweise

- Fassungen im Wortlaut (arbeit/dokumente, ≥ 10.000 Bytes): v1, v2, v3, v4, v5, v6, v7, v8; höchste v8; fehlend zwischen v1 und v8: keine (*gerechnet*).
- Verweise „Masterprompt … v<n>/Fassung <n>/F<n>“ in Biotop-Nachrichten, Prüfkanal-Texten und Commit-Nachrichten: v1: 23 (Nachrichten/Prüfkanal), v2: 41 (Nachrichten/Prüfkanal), v3: 16 (Nachrichten/Prüfkanal), v4: 26 (Nachrichten/Prüfkanal), v5: 5 (Nachrichten/Prüfkanal), v6: 107 (Nachrichten/Prüfkanal), v7: 29 (Nachrichten/Prüfkanal), v8: 86 (Nachrichten/Prüfkanal/git) (*gerechnet*).
- Verweise auf eine Fassung ohne Wortlaut: keine.

### Abgleich 4 — Status je Auftrag

- Aufträge und Anweisungen Philipps (Biotop ja): 114; Status aus der Chronik: 60; UNBEKANNT: 54 (Zuordnung: Nachrichten-id in der Zeile oder Zeit ±10 min).
- Aufträge Hermes→Subagent: 131; Schlussbericht (Absender Subagent) in derselben Sitzung vorhanden: 124, fehlt: 7 (*gerechnet*; ein vorhandener Bericht belegt keinen Status „erledigt“).
- Status je Nachricht: `LISTEN`, Abschnitt 3 (Spalte Status).
- Davon ohne Bericht vor Beginn BIOTOP-LAGE-01: 5 (16285, 16712, 17153, 17290, 17293); ab Beginn: 2 (können beim Lesen noch laufen, darunter dieser Teilauftrag) (*gerechnet*, Nachrichten-id).
- Nachrichten Philipps (Biotop ja) ab 18.09. bis zum Stich: 115, davon ab 21.09. 00:00 CEST: 44 (*gerechnet* aus dem Verzeichnis; Vergleichszahl für Teil F).

### Abgleich 5 — Commit und geänderte Datei ↔ Auftrag oder Lauf

Regel (Auslegung Hermes, mechanisch, Reihenfolge): (a) Nennung des Kurz-Hashs in einem Prüfkanal-Text oder einer Biotop-Nachricht bis 2026-09-25 14:44:20; bei Dateien: ein Commit ab 21.09., der die Datei enthält und nicht älter ist als ihre mtime; (b) Zeitfenster eines Laufs [Beginn, Ende oder letzte Buchung + 30 min]; (c) Zeitregel: letzter Auftrag oder letzte Anweisung Philipps oder letzter Auftrag Hermes→Subagent (Biotop ja) höchstens 24 h davor. Sonst offen.

- Commits seit 18.09.: 75; Nennung 38, Lauf 25, Auftrag 12 (*gerechnet*).
- Geänderte Dateien seit 21.09.: 202; Commit 87, Lauf 62, Auftrag 53 (*gerechnet*). Zuordnung je Eintrag: `LISTEN`, Abschnitte 4 und 5.

### Abgleich 6 — Kosten Kasse ↔ OpenRouter

Auslegung Hermes (nicht geprüft): Die Anzeige führt `usage_daily` je UTC-Tag, `usage_weekly` je UTC-Woche ab Montag, `usage_monthly` je UTC-Monat, `usage` gesamt, alles in USD. Kasse in USD = Summe kosten_eur × 1.08.
| Abfrage | Fenster | OpenRouter USD | Kasse USD | Differenz USD | Differenz € |
|---|---|---|---|---|---|
| 25.09. 14:54 | gesamt | 20.5361 | 20.3199 | +0.2161 | +0.2001 |
| 25.09. 14:54 | UTC-Monat | 20.5361 | 20.3199 | +0.2161 | +0.2001 |
| 25.09. 14:54 | UTC-Woche | 10.7713 | 10.5069 | +0.2644 | +0.2448 |
| 25.09. 14:54 | UTC-Tag | 0.3076 | 0.0000 | +0.3076 | +0.2848 |

*abgelesen* (OpenRouter), *gerechnet* (Kasse, Differenz = OpenRouter − Kasse). Mögliche Ursachen (Auslegung Hermes, nicht geprüft): (1) derselbe Schlüssel wird außerhalb der Biotop-Kasse genutzt (Hermes-Verdichtung seit 25.09. 01:10 laut Teilauftrag, andere Vorhaben); (2) die Kasse rechnet Kosten aus Token und eigener Preistabelle (Stand 18.09.) mit festem Kurs, nicht aus der Abrechnung. Die Aufteilung ist UNBEKANNT, weil die Anzeige keine Einzelposten führt.

### Abgleich 7 — Tagesbilanz 18.09.2026 bis Stich

| Tag | Auftrag Ph. | Anweisung Ph. | Frage Ph. | Auftrag H→S | Auftragsdateien (mtime) | Läufe begonnen (Kasse) | lauf.angelegt (Protokoll) | Läufe mit Buchung (Kasse) | Meldungen Hermes | Berichte Subagent | Systemmeldungen | Commits (git) | Kosten € (Kasse) | OpenRouter |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-18 | 2 | 3 | 0 | 0 | 0 | 2 | 2 | 2 | 5 | 0 | 2 | 0 | 0.1905 | NICHT ABGEDECKT |
| 2026-09-19 | 4 | 22 | 0 | 0 | 0 | 21 | 20 | 21 | 36 | 0 | 10 | 45 | 7.1885 | NICHT ABGEDECKT |
| 2026-09-20 | 15 | 25 | 0 | 53 | 17 | 4 | 3 | 5 | 57 | 25 | 39 | 11 | 1.7071 | NICHT ABGEDECKT |
| 2026-09-21 | 3 | 18 | 1 | 8 | 1 | 11 | 11 | 11 | 49 | 2 | 28 | 8 | 2.3259 | NICHT ABGEDECKT |
| 2026-09-22 | 3 | 0 | 0 | 2 | 0 | 2 | 2 | 3 | 8 | 2 | 6 | 2 | 7.4027 | NICHT ABGEDECKT |
| 2026-09-23 | 5 | 3 | 0 | 10 | 3 | 0 | 0 | 0 | 19 | 4 | 15 | 3 | 0.0000 | NICHT ABGEDECKT |
| 2026-09-24 | 4 | 2 | 0 | 4 | 6 | 0 | 0 | 0 | 26 | 2 | 15 | 6 | 0.0000 | NICHT ABGEDECKT |
| 2026-09-25 | 1 | 4 | 0 | 54 | 25 | 0 | 0 | 0 | 17 | 18 | 8 | 0 | 0.0000 | 0.3076 USD (UTC-Tag bis 14:54) |

Quellen je Spalte: Nachrichtenverzeichnis (Ph. = Philipp, H→S = Hermes an Subagent, Meldungen, Berichte, System; nur Biotop ja), Auftragsdateien aus I4 (eindeutige Inhalte nach frühester mtime; zeigt nur die letzte Änderung), Kasse (entdoppelt), Protokoll (entdoppelt), git (Commit-Zeit), OpenRouter (nur Abfragetag). 0 heißt: die Quelle führt den Tag und zählt nichts; „bis hh:mm“: Quelle endet am Tag. Tage gelten in CEST, der letzte endet mit dem Stich 2026-09-25 17:29:59. Kasse: 0 gilt als abgedeckt, weil die Suche nach weiteren Kassen-Datenbanken unter /root 0 Buchungen außerhalb der vier Zweige fand (Quellenabdeckung). *gerechnet*
- Davon ab Beginn BIOTOP-LAGE-01 (2026-09-25 14:44:20): 83 Biotop-Nachrichten (Arbeit an diesem Auftrag und am Bau S1c). *gerechnet*

### Abgleich 8 — Nummernkreise: Kassen-Kennung ↔ Laufnummer ↔ Ordnername

| Lauf (Kennung dieses Inventars) | Kassen-id je Zweig | Beginn (UTC, Kasse) | Ordnername |
|---|---|---|---|
| R02/26 | R26 | 2026-09-20T18:42:07.075887+00:00 | biotop-reparatur-02 |
| VB1/26 | V26 | 2026-09-20T19:31:54.969+00:00 | biotop-phase-4-vorbedingung-1 |
| T3/26 | T26 | 2026-09-21T03:43:38.148+00:00 | biotop-t3-typescript |

Nur Läufe mit mehrfach vergebener Nummer oder ohne Ordner; alle übrigen 37 Läufe haben eine eindeutige Nummer — ihre Zuordnung steht in I1. Weitere Nummernkreise: „Lauf 3“ des Masterprompts v2 ist Kassen-Lauf 9 (Bericht `biotop-phase-1-nachlauf`, R30); Ordner der Behebungsrunden `biotop-vor-t4*` gehören zu Aufträgen ohne Lauf.

### Abgleich 9 — Gegenprobe

- Kopie der Inventare im Speicher: I1 40 → 41 Läufe (+ `ERFUNDEN/999`, Beginn 2026-09-22 12:00:00 CEST), I3 20 → 21 Ordner (+ `laeufe/biotop-erfunden-99/`, 3 Dateien). *gerechnet*
- Abgleich 1 am Original: unzugeordnet 0 Läufe, 0 Ordner: keine.
- Abgleich 1 an der Kopie: unzugeordnet 1 Läufe, 1 Ordner: ['ERFUNDEN/999', 'biotop-erfunden-99'].
- Neu unzugeordnet (Kopie − Original): ['ERFUNDEN/999', 'biotop-erfunden-99']; weggefallen (Original − Kopie): keine.
- **Gegenprobe angeschlagen: ja** — Bedingung: neu unzugeordnet sind genau ['ERFUNDEN/999', 'biotop-erfunden-99'] und nichts fällt weg. Genau diese beiden und sonst nichts unzugeordnet: ja.
- Regel: Zuordnung nur mit Beleg (Nennung im Ordnertext, Zweig-Arbeitsordner, Chronikzeile, Nennung des Ordnernamens in einer Biotop-Nachricht bis 2026-09-25 14:44:20 CEST oder in einer Auftragsdatei); der eigene Ordner `biotop-lage-01` zählt nicht als Beleg.
