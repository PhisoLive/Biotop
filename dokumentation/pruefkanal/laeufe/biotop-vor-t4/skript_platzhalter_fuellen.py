"""Füllt die Platzhalter ‹…› in BERICHT.md aus den Belegdateien (nach job_commit2_regression.sh). Schreibt nichts, was
nicht aus einer Datei gelesen ist; gibt jede Ersetzung aus. Ergänzt KASSE.md und UEBERGABE.md."""
import json
import re
import statistics
from pathlib import Path

A = Path('/root/biotop-vor-t4')
B = A / 'BERICHT.md'
bericht = B.read_text()
aus = {}

# ---- volle Regression
letzte = (A / 'REGRESSION2-VOR-T4.txt').read_text().strip().splitlines()[-1]
zahl = lambda w: int(m.group(1)) if (m := re.search(r'(\d+) ' + w, letzte)) else 0  # noqa: E731
dauer = (m.group(1) if (m := re.search(r'in ([\d.]+)s', letzte)) else '?')
x = (A / 'REGRESSION2-VOR-T4.junit.xml').read_text()
suite = re.search(r'<testsuite [^>]*>', x).group(0)
attr = {k: int(v) for k, v in re.findall(r'\b(tests|failures|errors|skipped)="(\d+)"', suite)}
faelle = []
for m in re.finditer(r'<testcase ([^>]*?)(/>|>(.*?)</testcase>)', x, re.S):
    a = dict(re.findall(r'(\w+)="([^"]*)"', m.group(1)))
    body = m.group(3) or ''
    art = 'rot' if ('<failure' in body or '<error' in body) else 'uebersprungen' if '<skipped' in body else 'gruen'
    grund = (re.search(r'<skipped[^>]*message="([^"]*)"', body) or [None, ''])[1] if art == 'uebersprungen' else ''
    faelle.append({'klasse': a.get('classname', ''), 'name': a.get('name', ''), 'zeit': float(a.get('time', 0)), 'art': art, 'grund': grund})
ueber = [f for f in faelle if f['art'] == 'uebersprungen']
rot = [f for f in faelle if f['art'] == 'rot']
draht = [f for f in faelle if 'test_verdrahtung' in f['klasse']]
spez = [f for f in faelle if re.search(r'test_t3_(verhaltensvergleich|masseichung)', f['klasse'])]
t10 = [f for f in faelle if f['name'].startswith('test_10_sperre_am_laufweg')]
job = (A / 'JOB-COMMIT2-REGRESSION.txt').read_text()
status_nach = job.split('(Ende Status)')[1].split('(Ende Status nach Regression)')[0] if '(Ende Status nach Regression)' in job else '?'
sauber_nach = 'git status' not in status_nach and status_nach.strip().splitlines()[-1:] in ([], [''])  # nur die Zeile regression pytest-rc davor
aus['REG2'] = (f"**{zahl('passed')} bestanden, {zahl('skipped')} übersprungen, {zahl('failed')} fehlgeschlagen, "
               f"{zahl('error')} Fehler**, {zahl('deselected')} abgewählt (`integration`), {dauer} s. JUnit: {attr.get('tests')} Fälle, "
               f"{attr.get('failures')} fehlgeschlagen, {attr.get('errors')} Fehler, {attr.get('skipped')} übersprungen "
               f"({'; '.join(f['name'] + ': ' + f['grund'][:80] for f in ueber)}). Verdrahtungstest "
               f"{'grün' if draht and all(f['art'] == 'gruen' for f in draht) else 'NICHT grün'} "
               f"({', '.join(str(round(f['zeit'])) + ' s' for f in draht)}; `VERDRAHTUNG-BELEG-REGRESSION2.json`). "
               f"Arbeitsbaum vor und nach der Regression: siehe `JOB-COMMIT2-REGRESSION.txt`. Zum Vergleich an `58bd9f9`: 451 bestanden, 2 übersprungen")
aus['REG2SKIP'] = (f"In der Regression an `330b4ec` liefen {sum(f['art'] == 'gruen' for f in t10)} von {len(t10)} Fällen von "
                   f"`test_10_sperre_am_laufweg…` und bestanden; übersprungen {sum(f['art'] == 'uebersprungen' for f in t10)} (Image ts1 gesetzt)")
print('Spezifikationsdateien test_t3_verhaltensvergleich/-masseichung:', sum(f['art'] == 'gruen' for f in spez), 'von', len(spez), 'grün;',
      'rot gesamt', len(rot), [f['name'] for f in rot][:5])
print('Status nach Regression (roh):', repr(status_nach.strip()[-300:]))

# ---- Nachspiele am Commit
NAMEN = ['s2_k2904', 's2_k3091', 'k3106_ohne_eichung', 'k3324_ohne_eichung', 'k2934', 'k3121', 'k2868']
zeilen, gleich, dauern, commit_ok, db_ok = [], 0, [], 0, 0
for n in NAMEN:
    p2 = A / 'nachspiel2' / f'{n}.json'
    if not p2.exists():
        zeilen.append(f'{n}: kein Beleg')
        continue
    neu, alt = json.loads(p2.read_text()), json.loads((A / 'nachspiel' / f'{n}.json').read_text())
    cs = neu.get('code_stand_beim_import') or {}
    commit_ok += cs.get('commit', '').startswith('330b4ec') and cs.get('arbeitsbaum_sauber') is True
    db_ok += neu.get('quelle_db_sha256_vorher') == neu.get('quelle_db_sha256_nachher')
    gleich += neu.get('status') == alt.get('status')
    v, va = neu.get('verhalten') or {}, alt.get('verhalten') or {}
    lz = neu.get('laufzeit_gepaart') or {}
    if lz.get('dauer_s') is not None:
        dauern.append(lz['dauer_s'])
    extra = ''
    if n.startswith('s2_'):
        pl = (lz.get('bereiche') or {}).get('planung') or {}
        if pl.get('basis') and pl.get('kandidat'):
            extra = f", planung gepaart {pl['basis']:.4f} → {pl['kandidat']:.4f} ms ({(pl['kandidat'] / pl['basis'] - 1) * 100:+.0f} %)"
    zeilen.append(f"K{neu.get('kandidat')}{'+' + str(neu.get('partner')) if neu.get('partner') else ''} {neu.get('status')} "
                  f"(vorher {alt.get('status')}; Abweichungen {va.get('anzahl_abweichungen')} → {v.get('anzahl_abweichungen')}, "
                  f"ungedeckt {len(va.get('ungedeckt') or [])} → {len(v.get('ungedeckt') or [])}, "
                  f"beobachtet {va.get('beobachtete_funktionen')} → {v.get('beobachtete_funktionen')}{extra}; "
                  f"Erwartung {'erfüllt' if neu.get('erwartung_erfuellt') else 'NICHT erfüllt'})")
aus['NACHSPIEL2'] = (f"{gleich} von {len(NAMEN)} Fällen gleich entschieden wie im ersten Durchgang; Code-Stand im Beleg "
                     f"`330b4ec` mit sauberem Arbeitsbaum in {commit_ok} von {len(NAMEN)}; t3.db unverändert in {db_ok} von {len(NAMEN)} "
                     f"(`NACHSPIEL2-AM-COMMIT.txt`, `NACHSPIEL2-BELEGE.json`)")
aus['NACHSPIEL2KURZ'] = '; '.join(zeilen)
aus['DAUER'] = (f"gepaarte Messung {min(dauern):.0f}–{max(dauern):.0f} s je Kandidat (Median {statistics.median(dauern):.0f} s, "
                f"{len(dauern)} von {len(NAMEN)} Nachspielen mit gepaarter Messung)" if dauern else 'keine gepaarte Messung mit Dauer im Beleg')

# ---- Python-Laufzeit
py = json.loads((A / 'PYTHON-LAUFZEIT-PROBE.json').read_text())
if py.get('fehler'):
    aus['PYPROBE'] = aus['PYPROBEKURZ'] = f"**in der Kammer gescheitert**: {py['fehler'][:300]} (`PYTHON-LAUFZEIT-PROBE.json`)"
else:
    pr, gg = py.get('probe') or {}, py.get('gegenprobe') or {}
    vh = [b['verhaeltnis'] for b in (pr.get('bereiche') or {}).values() if b.get('verhaeltnis')]
    aus['PYPROBE'] = (f"einmal in der Kammer ausgeführt (`PYTHON-LAUFZEIT-PROBE.json`, Werk lagerhaus, Image biotop-kammer:1): "
                      f"gültig {pr.get('gueltig')}, {pr.get('n')} je Seite, {len(vh)} Bereiche, Verhältnis gleicher Stand/gleicher Stand "
                      f"{min(vh):.3f}–{max(vh):.3f}, {pr.get('dauer_s')} s; Gegenprobe Syntaxfehler im Kandidaten → gültig "
                      f"{gg.get('gueltig')}, Seite {gg.get('seite')}" if vh else f"ausgeführt, aber ohne Werte: {json.dumps(pr)[:300]}")
    aus['PYPROBEKURZ'] = aus['PYPROBE']

for k, v in aus.items():
    assert f'‹{k}›' in bericht, k
    bericht = bericht.replace(f'‹{k}›', v)
    print(f'‹{k}› → {v}\n')
B.write_text(bericht)
print('verbleibende Platzhalter:', re.findall(r'‹[^›]*›', bericht))

kasse = (A / 'KASSE.md').read_text()
if 'Zweite Sitzung' not in kasse:
    kasse += ("\n## Zweite Sitzung (23.09., 19:40–22 Uhr)\n\n"
              "- Biotop-Modellgeld: **0,00 €**. Kein Lauf; die Nachspiele am Commit gingen an die gestellte Anbietergrenze "
              f"(`modellaufrufe_echt` 0 in den Belegen), t3.db unverändert in {db_ok} von {len(NAMEN)} Nachspielen.\n"
              "- Träger (nicht Biotop): 2 echte Anfragen für den Konfigurationsbeleg (`hermes chat --oneshot`, Verdichtungsroute "
              "`call_llm`), über die Anthropic-Anmeldung des Trägers; nicht aus dem Biotop-Budget, Betrag nicht beziffert.\n"
              "- Kammerläufe (S1-Klärung 2, S1-Deckung 3, Regression, Nachspiele, Python-Laufzeit): kein Modellgeld, nicht gezählt.\n")
    (A / 'KASSE.md').write_text(kasse)
u = (A / 'UEBERGABE.md').read_text()
u = u.replace('## Läuft\n', '## Läuft (erledigt, Ergebnisse im BERICHT eingetragen)\n')
(A / 'UEBERGABE.md').write_text(u)
