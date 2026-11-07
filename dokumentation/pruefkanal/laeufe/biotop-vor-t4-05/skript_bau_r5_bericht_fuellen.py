"""Bericht der Runde 5 füllen (ohne ‹REVIEW›, ‹SPERREN›, ‹REVIEW_SPEZ› — die hängen am Reviewdurchgang). Jede Zahl aus
den Belegen (AUSWERTUNG.json, NACHSPIEL-Belege, VORHER/NACHHER, T4-GROESSE, T4-DIAGNOSE, SPEZ-R6-*); Abbruch, wenn eine
Quelle nicht passt."""
import json
import re
from pathlib import Path

A = Path('/root/biotop-vor-t4-05')
a = json.loads((A / 'AUSWERTUNG.json').read_text())
ns = [e for e in a['nachspiele'] if e['durchgang'] in ('n1', 'n2', 'n3')]
assert len(ns) == 7 and all(e['commit'] == '0c2f058' and e['sauber'] and e['db_gleich'] and e['modell'] == 0 for e in ns)
k04 = sorted((e for e in ns if e['fall'] == 's2_k2904'), key=lambda e: e['durchgang'])
k91 = sorted((e for e in ns if e['fall'] == 's2_k3091'), key=lambda e: e['durchgang'])
k68 = [e for e in ns if e['fall'] == 'k2868'][0]
assert len(k04) == len(k91) == 3 and all(e['status'] == 'ueberlebt' and e['gewinn'] == 'klar' for e in k04 + k91)
gesperrt = sum('eingang' in (e['gesperrt'] or []) for e in k04 + k91)
m = re.match(r'Verhaltensvergleich: (\d+) von (\d+) Abweichung', k68['grund'])
k68_ungedeckt, k68_abw = int(m.group(1)), int(m.group(2))
assert k68['status'] == 'abgelehnt' and k68_abw == k68['abweichungen'] == 40 and k68['gedeckt'] == 16
auf68 = k68['aufschluesselung']
assert sum(auf68.values()) == k68_ungedeckt


def q(x):
    return f'{x:.3f}'.replace('.', ',')


vorher, nachher = a['VORHER-43b8fad'], a['NACHHER-HEAD']
rot_vorher = {k: v for k, v in vorher['faelle'].items() if v != 'grün'}
api = sorted(k for k, v in rot_vorher.items() if re.match(r"rot: AttributeError: .*has no attribute", v))
assert nachher['gruen'] == nachher['n'] == 27 and vorher['gruen'] == 9 and len(rot_vorher) == 18 and len(api) == 3, api
reg = (A / 'REGRESSION.txt').read_text().strip().splitlines()[-1]
m = re.match(r'(\d+) passed, (\d+) skipped, (\d+) deselected in ([\d.]+)s', reg)
r_pass, r_skip, r_desel, r_s = int(m.group(1)), int(m.group(2)), int(m.group(3)), float(m.group(4))
ju = a['junit']
vb = a['VERDRAHTUNG-BELEG-REGRESSION.json']
assert vb['nie_gerufen'] == [] and vb['register']['fehlend'] == [] and vb['tor4']['behoben'] == ['A1']
assert vb['nachspiel']['status'] == vb['nachspiel']['status_aufgezeichnet'] == 'ueberlebt' and vb['nachspiel']['laufzeit_stufe'] == 2
assert vb['modellkosten_eur'] == 0 and a['VERDRAHTUNG-BELEG-TEILLAUF3.json']['modellkosten_eur'] == 0
stufen = vb['stufen']
t4 = {('24' if x.get('kappe') == 24 else 'ohne'): x for x in a['t4'] if 'kappe' in x}
t4_kopf = [x for x in a['t4'] if 'module' in x][0]
diag = (A / 'proben' / 'T4-DIAGNOSE.txt').read_text()
null_halter = sorted(set(re.findall(r'^\s+0\s+grosswerk\.werk\.(m\d:m\d_f\d)\|rueckgabe\|$', diag, re.M)))
assert len(null_halter) == 5, null_halter
r6l = (A / 'spez' / 'SPEZ-R6-LAUFWEG.txt').read_text()
r64 = (A / 'spez' / 'SPEZ-R6-4.txt').read_text()
assert '1 failed, 1 passed' in r6l and '@@ True zurueckgestellt' in r6l and '@@ False ueberlebt' in r6l
assert '3 failed, 2 passed' in r64 and 'commit 0c2f058' in r64

T = {}
T['URTEIL'] = ('nicht abgenommen — die Gegenproben der Runde halten, aber an 0c2f058 sind zwei Messfehler derselben '
               'Klasse gemessen, die vor T4 behoben sein müssen (R6-1, R6-4)')
T['ERGEBNIS'] = f"""- **Nicht abgenommen.** An `0c2f058` sind zwei Messfehler gemessen, die T4 gefährden; beide sind als rote
  Spezifikationen gefasst, keiner ist nachträglich gebaut (ein Review, keine Fix-Kaskade).
  - **R6-1 (Hinweis Philipp):** Bei unvollständiger Erfassung enthält sich der ganze Vergleich statt nur der betroffenen
    Beobachtung. Durch `aegis.pruefen` gemessen: Eine richtige Behebung plus eine unveränderte Funktion, die ein
    `StringIO` liefert, wird zurückgestellt; ohne diese Funktion überlebt sie (`spez/SPEZ-R6-LAUFWEG.txt`).
  - **R6-4 (eigener Befund nach dem Commit):** Ein Test mit `assert f(1) == 3` hält nichts fest. pytest meldet
    umgeschriebene Zusicherungen ohne Anführungszeichen ohne das Präfix „AssertionError:“, und die neue Regel verlangt es.
    Rot in 3 von 3 Fällen (Zahl, Liste, Wahrheitswert), die Gegenproben 2 von 2 grün (`spez/SPEZ-R6-4.txt`). Folge in
    der T4-Größen-Messung: Für {len(null_halter)} von {len(t4_kopf['geaendert'])} geänderten Funktionen hält kein Test
    fest.
- **Die Fälle aus Review 04 sind geschlossen** (Vorher/Nachher, 27 Fälle): {vorher['gruen']} von 27 grün an `43b8fad`
  (Kontrollen und die schon gebaute 60-s-Grenze), 27 von 27 an `0c2f058`. Von den {len(rot_vorher)} roten Fällen scheitern
  {len(rot_vorher) - len(api)} am Verhalten und {len(api)} an einer fehlenden Schnittstelle.
- **Gegenprobe Entscheidung 1 der Runde 4 an `0c2f058`:** K2904 überlebt in 3 von 3 Nachspielen (`planung`-Quote
  {q(min(e['planung'] for e in k04))} … {q(max(e['planung'] for e in k04))}), K3091 in 3 von 3
  ({q(min(e['planung'] for e in k91))} … {q(max(e['planung'] for e in k91))}), alle Gewinne klar. `eingang` war in
  {gesperrt} von 6 Nachspielen gesperrt (Runde 4: 3 von 6). K2868 wird abgelehnt: {k68_ungedeckt} von {k68_abw}
  Abweichungen ungedeckt (Weißraum und führende Null), 16 gedeckt, wie in Runde 4. 7 von 7 Belegen tragen den Commit
  `0c2f058`, sauberen Arbeitsbaum, unveränderte T3-DB und 0 Modellaufrufe.
- **Regression an `0c2f058`:** {r_pass} bestanden, {r_skip} übersprungen, 0 rot (JUnit {ju['faelle']} Fälle,
  {ju['failure']} Fehlschläge, {ju['error']} Fehler), {r_s:.0f} s. Verdrahtung: {vb['gerufen']} von {vb['organe']}
  Organen, Register 10 von 10 Kanten, Tor-4-Zeile „Schwächen“ an A1 doppelt geprüft und behoben, das Nachspiel im
  Verdrahtungstest urteilt wie der Lauf (überlebt, Stufe 2), 0,00 €.
- **Stufe 2, `eingang`:** Mit 240 Wiederholungen sperrte es in 0 von 8 Rauschmessungen (mit 60: 3 von 8); die Stichprobe
  dauert 170,5 statt 35,1 ms. 240 ist nach der Sperrzahl gewählt, nicht nach einer Regel der Dauer (R6-3, Offen Nr. 3).
- **Entscheidung 4 ist nicht belegt.** Gemessen ist der Bedarf eines breiten Kandidaten, 8 geänderte Funktionen:
  {t4['24']['bedarf']} Verfälschungsläufe, bei Kappe 24 also {t4['24']['ausgelassen']} ausgelassen. Das Werk hat aber nur
  {t4_kopf['zeilen_werk']} Zeilen, T4 dagegen 6.000–10.000. Das Urteil beider Messläufe ist wegen R6-4 nicht verwertbar.
- **Biotop-Modellgeld 0,00 €**; kein Lauf."""

T['T4'] = f"""- **Aufbau:** Ein Python-Prüfwerk aus {t4_kopf['module']} Modulen mit {t4_kopf['funktionen']} Funktionen
  ({t4_kopf['zeilen_werk']} Zeilen). Der Kandidat ändert {len(t4_kopf['geaendert'])} Funktionen in einem Zug; für jede
  bringt das Werk Soll-Tests je Formvariante mit, die an der Vorgeneration rot sind.
- **Messung durch `aegis.pruefen`** in der echten Kammer (Modell und Laufzeit gestellt), einmal mit Kappe 24 und einmal
  ohne:
  - Kappe 24: Bedarf {t4['24']['bedarf']} Verfälschungsläufe, davon {t4['24']['verfaelschungen']} gelaufen und
    {t4['24']['ausgelassen']} ausgelassen; {t4['24']['kammerlaeufe']} Kammerläufe, {str(t4['24']['dauer_s']).replace('.', ',')} s;
    Urteil {t4['24']['status']}.
  - Ohne Kappe: {t4['ohne']['verfaelschungen']} Verfälschungsläufe, {t4['ohne']['kammerlaeufe']} Kammerläufe,
    {str(t4['ohne']['dauer_s']).replace('.', ',')} s; Urteil {t4['ohne']['status']}.
  - Beide Male {t4['24']['abweichungen']} Abweichungen, „15 von 15 beobachtet“.
- **Nicht verwertbar für die Kappe.** Die Diagnose (`proben/T4-DIAGNOSE.txt`, ohne Kappe) zeigt: Für
  {len(null_halter)} von {len(t4_kopf['geaendert'])} geänderten Funktionen ({', '.join(null_halter)}), die Zahlen und Listen
  liefern, hält kein Test fest. Deren Tests sind Zusicherungen ohne Anführungszeichen (R6-4). Dass mit Kappe 24 abgelehnt
  statt zurückgestellt wird, liegt an diesen Abweichungen, die ohnehin ungedeckt bleiben, nicht an der Kappe.
- **Belastbar ist nur der Bedarf:** {t4['24']['bedarf']} Verfälschungsläufe für einen Kandidaten mit
  {len(t4_kopf['geaendert'])} geänderten Funktionen, etwa 1 s je Lauf in diesem kleinen Werk. Ein T4-Werk hat
  6.000–10.000 Zeilen und längere Testläufe; die Kappe ist dort erneut zu messen, nach R6-4 und am echten T4-Werk
  (Offen Nr. 4). **„Gemessen an einem Kandidaten in T4-Größe“ ist damit nicht erfüllt**, nur die Breite des Kandidaten
  ist nachgebildet."""

T['REGRESSION'] = f"""| Stand | bestanden | übersprungen | fehlgeschlagen | JUnit (Fälle / Fehlschläge / Fehler) | Dauer | Verdrahtung |
|---|---|---|---|---|---|---|
| `0c2f058` | {r_pass} | {r_skip} | 0 | {ju['faelle']} / {ju['failure']} / {ju['error']} | {r_s:.0f} s | grün: {vb['gerufen']} von {vb['organe']} Organen, Register 10 von 10, 0,00 € |

- Übersprungen sind dieselben 2 Fälle wie in den Vorrunden (private Werk-/DB-Kopie nicht angegeben); {r_desel} Fälle
  sind abgewählt (`integration`). `tests/test_vor_t4_05.py`: {ju['vor_t4_05']} von {ju['vor_t4_05']} grün. `git status`
  war vorher und nachher leer.
- **Verdrahtungsbeleg:**
  - Tor-4-Zeile: „{vb['tor4']['zeile']}“.
  - Nachspiel des gewählten Kandidaten K{vb['nachspiel']['kandidat']}: {vb['nachspiel']['status']}, aufgezeichnet
    {vb['nachspiel']['status_aufgezeichnet']}, Stufe {vb['nachspiel']['laufzeit_stufe']},
    {vb['nachspiel']['kammerlaeufe']} Kammerläufe.
  - Aegis-Urteile: {stufen.get('2', 0)} mit Laufzeitmessung, alle an Stufe 2; {stufen.get('None', 0)} endeten vor der
    Laufzeitmessung."""

zeilen = []
for e in k04 + k91:
    zeilen.append(f"| {e['durchgang'].upper()} | {'K2904' if '2904' in e['fall'] else 'K3091'} | {q(e['planung'])} | "
                  f"{e['status']} | {e['gewinn']} | {', '.join(e['gesperrt'] or []) or '—'} |")
T['NACHSPIEL'] = (f"""**Gegenprobe Entscheidung 1 (Runde 4) an `0c2f058`: K2904 und K3091 in 3 von 3 Durchgängen gleich entschieden**,
beide überlebt. 7 von 7 Belegen tragen den Commit `0c2f058`, sauberen Arbeitsbaum, unveränderte T3-DB und 0 Modellaufrufe.

| Durchgang | Kandidat | `planung` Quote (Stufe 2) | Urteil | Gewinn | gesperrt |
|---|---|---|---|---|---|
""" + '\n'.join(sorted(zeilen)) + f"""

- `eingang` war in {gesperrt} von 6 Nachspielen gesperrt (Runde 4 mit 60 Wiederholungen: 3 von 6).
- **K2868 (N1):** {k68['status']}, {k68_ungedeckt} von {k68_abw} Abweichungen ungedeckt, 16 gedeckt — wie in Runde 4.
  Ungedeckt: """ + ', '.join(f"`{k.split(' | ')[1]}` {n}" for k, n in sorted(auf68.items())) + ".")
T['VORHER_NACHHER'] = f"""**{vorher['gruen']} von 27 grün an `43b8fad`, 27 von 27 an `0c2f058`.**
- Die {vorher['gruen']} an `43b8fad` grünen Fälle sind die Kontrollen, dazu die 60-s-Grenze des Vorspanns: Sie war schon
  in Runde 4 gebaut, aber ungetestet.
- Von den {len(rot_vorher)} roten Fällen scheitern {len(rot_vorher) - len(api)} am Verhalten (Zusicherung oder
  Sondenausfall).
- {len(api)} scheitern an einer fehlenden Schnittstelle ({', '.join(f'`{x}`' for x in api)}); für diese {len(api)} ist
  „vorher rot“ kein Verhaltensnachweis."""
T['R6_LAUFWEG'] = ("rot an `0c2f058` (`spez/SPEZ-R6-LAUFWEG.txt`, 1 rot, 1 grün): Mit `puffer` wird der Kandidat "
                   "zurückgestellt, „Verhaltensvergleich enthält sich … unvollständig erfasst (probewerk.werk.kern:puffer: "
                   "StringIO: Iterator-Objekt …) … (8 von 9 Funktionen beobachtet)“. Die Gegenprobe ohne `puffer` "
                   "überlebt.")
T['OFFEN'] = f"""1. **R6-4 vor T4 bauen?** Ein Test, der eine Zahl, eine Liste oder einen Wahrheitswert zusichert, hält nach
   Entscheidung 2 nichts fest (pytest-Meldung ohne Präfix).
   - Optionen: (a) vor T4 zusammen mit R6-1 und R6-2 (empfohlen); (b) nach T4.
   - Gemessene Folge von (b): In der T4-Größen-Messung hält für {len(null_halter)} von {len(t4_kopf['geaendert'])}
     geänderten Funktionen kein Test fest. Jede ihrer Abweichungen bleibt ungedeckt, der Kandidat wird abgelehnt — auch
     eine richtige Behebung mit Tests.
2. **Welche Tor-4-Zeilen berechnet das Skript (R6-2)?**
   - Optionen: (a) die 10 aus der Datenbank berechenbaren Zeilen, je mit Nachweis im nächsten Auftrag (empfohlen);
     (b) meine Einteilung zuerst von dir bestätigen lassen.
   - Folge von (b): ein Schritt mehr vor dem Bau.
3. **Maß der Stufe-2-Lasten (R6-3).**
   - Optionen: (a) eine vorab festgelegte Mindestdauer der Stichprobe je Bereichslast an Stufe 2, für alle Bereiche
     gleich, z. B. 100 ms Median (empfohlen); (b) die Regel der Stufe 1, „einige zehn Millisekunden“; (c) 240 belassen.
   - Gemessene Folge von (a) bei 100 ms: `eingang` mit 240 Wiederholungen (170,5 ms), `planung` (346,0 ms) und `bericht`
     (100,5 ms) erfüllen sie; `zahlen` (18,9 ms) und `tarife` (96,0 ms) wären neu zu bemessen. Der längste Kammerlauf
     lag bisher bei 12,3 s, weit unter 60 s.
   - Folge von (b): 60 Wiederholungen (35,1 ms) genügten, `eingang` sperrte damit aber in 3 von 8 Rauschmessungen.
   - Folge von (c): kein Maß, nur die Sperrzahl.
4. **Kappe der Verfälschungsläufe (Entscheidung 4) neu messen.**
   - Optionen: (a) nach R6-4 am echten T4-Werk vor dem Lauf, mit einem breiten gestellten Kandidaten (empfohlen);
     (b) am erweiterten Prüfwerk.
   - Gemessen bisher: Bedarf {t4['24']['bedarf']} Läufe bei {len(t4_kopf['geaendert'])} geänderten Funktionen in einem
     Werk mit {t4_kopf['zeilen_werk']} Zeilen; das Urteil war wegen R6-4 nicht verwertbar.
5. **TypeScript-Proben für die Entscheidungen 2 und 3.** Der TypeScript-Weg ist gebaut, aber ohne eigene Kammerprobe.
   - Optionen: (a) vor T5, zusammen mit den TS-Methoden (empfohlen, T4 ist Python); (b) vor T4.
   - Folge von (a): keine für T4."""
KASSE = {'VERDRAHTUNG_KOSTEN': '0.0 an `0c2f058` (Regression) und am Arbeitsbaum (`VERDRAHTUNG-BELEG-TEILLAUF3.json`)',
         'NACHSPIEL_DB': 'vorher = nachher in 8 von 8 Belegen dieser Runde (n1–n3 am Commit, Vorprobe am Arbeitsbaum)'}
SPEZ = {'R6_LAUFWEG_KURZ': 'rot: mit einer unveränderten `StringIO`-Funktion zurückgestellt, ohne sie überlebt '
                           '(`spez/SPEZ-R6-LAUFWEG.txt`)'}

b = (A / 'BERICHT.md').read_text()
for k, v in T.items():
    assert b.count(f'‹{k}›') == 1, k
    b = b.replace(f'‹{k}›', v)
R64 = f"""
**Befund nach dem Commit (R6-4, eigener Befund):** Die Regel erkennt umgeschriebene Zusicherungen ohne einfache
Anführungszeichen nicht.
- Ursache: pytest kürzt dort „AssertionError: “ aus der Meldung weg (`ExceptionInfo._striptext`). Gemessen in pytest
  8.3.3 in der Kammer und 9.1.1 lokal (`proben/VORPROBE-E2b.txt`).
- `assert f(1) == 3`, `assert f(1) == [3, 2, 1]` und `assert f(1)` halten deshalb nichts fest. `assert f(1) == 'a_b'`
  hält fest.
- `VORPROBE-E2` hatte nur Zusicherungen mit Text geprüft; das war eine zu enge Stichprobe (§14 Nr. 9).
- Die rote Spezifikation `spez/test_spez_r6_4.py` führt echtes pytest aus und prüft `_zusicherung_faellt` des Commits:
  rot in 3 von 3 Fällen (Zahl, Liste, Wahrheitswert); grün in 2 von 2 Gegenproben (Text hält, Werk-Ausnahme hält nicht).
- Folge: Für Werke, deren Tests Zahlen oder Listen zusichern — T4 ist ein Python-Werk —, wird jede Abweichung, die nur
  solche Tests decken, abgelehnt statt gedeckt. Die T4-Größen-Messung zeigt das (§4).
"""
anker = '## 3. Sondenausfall nur der betroffenen Funktion (Entscheidung 3)\n'
assert b.count(anker) == 1
b = b.replace(anker, R64 + '\n' + anker)
F = '''8. **Die Stufe-2-Last habe ich nach der Sperrzahl gewählt, nicht nach der Stichprobendauer.** Die Dauer stand in
   `STUFE2-EICHUNG.jsonl`, ich habe sie aber erst auf Nachfrage ausgewertet (§6).
'''
assert b.count(F) == 1
b = b.replace(F, F + '''9. **R6-4: Die Vorprobe zu Entscheidung 2 (`VORPROBE-E2`) prüfte nur Zusicherungen mit Text.** Dass pytest das Präfix
   bei Meldungen ohne Anführungszeichen wegkürzt, fiel erst nach dem Commit auf, und zwar an der T4-Größen-Messung.
   Rote Spezifikation R6-4; keine Nachbesserung nach dem Commit.
10. **„Gemessen an einem Kandidaten in T4-Größe“ (Entscheidung 4) ist nicht erfüllt.** Nachgebildet ist nur die Breite
    des Kandidaten, nicht die Größe des Werks (126 Zeilen statt 6.000–10.000). Das Urteil der Messung ist wegen R6-4 nicht
    verwertbar (§4).
''')
b = b.replace('4. **Normalvergleich einer Altlast', '8. **Normalvergleich einer Altlast') if False else b
b = b.replace('streng (Offen Nr. 4).', 'streng; so gelesen steht es im Wortlaut der Entscheidung 5 („einen unabhängigen '
              'Test aus der Altlastenliste“).')
(A / 'BERICHT.md').write_text(b)
k = (A / 'KASSE.md').read_text()
for kk, v in KASSE.items():
    assert k.count(f'‹{kk}›') == 1, kk
    k = k.replace(f'‹{kk}›', v)
(A / 'KASSE.md').write_text(k)
s = (A / 'SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md').read_text()
for kk, v in SPEZ.items():
    assert s.count(f'‹{kk}›') == 1, kk
    s = s.replace(f'‹{kk}›', v)
s = s.replace('‹REVIEW_SPEZ›', f"""| R6-4 | **Festhalten erkennt Zusicherungen ohne Anführungszeichen.** Eine fallende Zusicherung im Test hält fest, auch wenn pytest die Meldung ohne „AssertionError:“ liefert (umgeschriebenes `assert` ohne `'` in der Darstellung). Die Regel prüft Art und Ort am Ausnahmetyp und an der Absturzstelle, nicht am Meldungstext. **Vor T4** (Offen Nr. 1). | `spez/test_spez_r6_4.py` rot in 3 von 3 (Zahl, Liste, Wahrheitswert); T4-Diagnose: {len(null_halter)} von {len(t4_kopf['geaendert'])} geänderten Funktionen ohne festhaltenden Test | Text-Zusicherung hält fest, Werk-Ausnahme hält nicht (2 von 2 grün) | eigener Befund nach dem Commit |
| R6-5 | **Kappe der Verfälschungsläufe am echten T4-Werk messen**, nach R6-4 (Offen Nr. 4). | `proben/T4-GROESSE.txt`: Bedarf {t4['24']['bedarf']}, Werk {t4_kopf['zeilen_werk']} Zeilen, Urteil wegen R6-4 nicht verwertbar | — | Entscheidung 4 |
‹REVIEW_SPEZ›""")
(A / 'SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md').write_text(s)
print('gefüllt; offen im BERICHT:', sorted(set(re.findall(r'‹([A-Z_0-9]+)›', b))), '| KASSE offen:',
      re.findall(r'‹([A-Z_]+)›', k), '| SPEZ offen:', re.findall(r'‹([A-Z_]+)›', s))
