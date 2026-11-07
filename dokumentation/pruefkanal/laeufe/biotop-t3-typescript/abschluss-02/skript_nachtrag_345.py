"""Torzeilen 3, 4 und 5 aus der vorhandenen Datenbank."""
import json
import sqlite3
from collections import Counter

c = sqlite3.connect('file:/root/biotop-t3/t3.db?mode=ro', uri=True)
c.row_factory = sqlite3.Row
L = 37
erg = {}

print('=== TORZEILE 3a: DOPPELUNGSANTEIL DER ANGRIFFSTESTS (Schwelle 20 %) ===')
print('  Nicht zu verwechseln mit dem Doppelgaenger-Anteil der VORSCHLAEGE (0 %),')
print('  der in der Saettigungsmeldung steht. Hier: wie oft stellte ein Angriffstest')
print('  dieselbe Behauptung wie ein frueherer im selben Bereich?')
ansagen = [json.loads(z['inhalt']) for z in c.execute(
    "SELECT inhalt FROM protokoll WHERE art='aegis.ansage' ORDER BY nr")]
ansagen = [a for a in ansagen if a.get('lauf_id') == L]
gesamt = len(ansagen)
doppelt = sum(1 for a in ansagen if a.get('ausgefuehrt') is False
              and 'bereits aufgestellt' in str(a.get('grund', '')))
ohne = sum(1 for a in ansagen if a.get('behauptung') is None)
print(f'  Ansagen gesamt            : {gesamt}')
print(f'  davon Doppelung (gesperrt): {doppelt}')
print(f'  davon ohne Behauptung     : {ohne}')
basis = gesamt - ohne
anteil = 100 * doppelt / basis if basis else 0.0
print(f'  Doppelungsanteil          : {doppelt} von {basis} = {anteil:.1f} %')
print(f'  Schwelle 20 %             : {"EINGEHALTEN" if anteil <= 20 else "GERISSEN"}')
erg['doppelung'] = {'doppelt': doppelt, 'nenner': basis, 'prozent': round(anteil, 1),
                    'schwelle': 20, 'eingehalten': anteil <= 20}

print('\n=== TORZEILE 3b: WELCHE ZEILE HAENGT AN aegis._anhaengen? ===')
print('  _anhaengen fuegt neue Testfunktionen an eine BESTEHENDE Testdatei an.')
print('  Fuer TypeScript gibt es stattdessen je Angriff eine eigene Datei')
print('  (tests/test_<bereich>_immun_aegis_k<id>_<bereich>.test.ts).')
immun = [z['pfad'] for z in c.execute(
    "SELECT DISTINCT pfad FROM landkarte WHERE 0")] if False else []
n_immun = 0
for z in c.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil'"):
    d = json.loads(z['inhalt'])
    if d.get('lauf_id') == L:
        n_immun += len(d.get('tests_neu') or [])
print(f'  In Lauf {L} uebernommene neue Tests aus Angriffen: {n_immun}')
print('  Die Torzeile "Immunisierung: nur bestandene Tests, Doppelungen gekennzeichnet"')
print('  (Mass, 3.10 F3) haengt an _anhaengen. Sie ist fuer TypeScript NICHT belegt:')
print('  0 von 0 Faellen, das Organ wurde nie erreicht.')
erg['anhaengen'] = {'faelle': 0, 'tests_neu_uebernommen': n_immun,
                    'zeile': 'Immunisierung 3.10 F3', 'belegt': False}

print('\n=== TORZEILE 4a: KEIN RUECKSCHRITT JE ANGENOMMENER GENERATION ===')
felder = ('tests_fehlgeschlagen', 'sicherheit_punkte', 'tote_funktionen')
vorher = None
rueckschritte = []
for g in c.execute("SELECT nummer,masse FROM generationen WHERE lauf_id=? "
                   "AND status='angenommen' ORDER BY nummer", (L,)):
    m = json.loads(g['masse'])
    jetzt = {b: {f: m['bereiche'][b][f] for f in felder} for b in m['bereiche']}
    if vorher is not None:
        for b in jetzt:
            for f in felder:
                if jetzt[b][f] > vorher[b][f]:
                    rueckschritte.append(f"Gen {g['nummer']} {b}.{f}: "
                                         f"{vorher[b][f]} → {jetzt[b][f]}")
    print(f"  Gen {g['nummer']:>2}: kernmass={m['kernmass']:>4}  " +
          '  '.join(f"{b}={jetzt[b]['sicherheit_punkte']}/{jetzt[b]['tests_fehlgeschlagen']}/"
                    f"{jetzt[b]['tote_funktionen']}" for b in sorted(jetzt)))
    vorher = jetzt
print(f'  (je Bereich: sicherheit/testfehler/tote)')
print(f'  RUECKSCHRITTE: {len(rueckschritte)}')
for r in rueckschritte:
    print(f'    {r}')
erg['rueckschritt'] = {'anzahl': len(rueckschritte), 'liste': rueckschritte}

print('\n=== TORZEILE 4b: WOHER KAMEN DIE DREI TESTFEHLER IN `eingang`? ===')
for g in c.execute("SELECT nummer,status,masse FROM generationen WHERE lauf_id=? "
                   "ORDER BY nummer", (L,)):
    if not g['masse']:
        continue
    m = json.loads(g['masse'])
    e = m['bereiche'].get('eingang')
    if e:
        print(f"  Gen {g['nummer']:>2} ({g['status']:<11}): eingang "
              f"{e['tests_bestanden']}/{e['tests_gesamt']} bestanden, "
              f"{e['tests_fehlgeschlagen']} fehlgeschlagen")

print('\n=== TORZEILE 5: EICHUNG VON LAUF 37 ===')
d = json.loads(c.execute("SELECT ergebnis FROM vorspann_nachweise WHERE lauf_id=?",
                         (L,)).fetchone()['ergebnis'])
r = d['rauschen']
print(f"  Rauschmessung: gesperrt={r.get('gesperrt')}, lauf_startet={r.get('lauf_startet')}")
for b in sorted(r['bereiche']):
    e = r['bereiche'][b]
    print(f"    {b:<9} toleranz={e.get('toleranz'):<6} werte={[round(x,2) for x in sorted(e.get('werte') or [])]}")
p = d['eichproben']
for gruppe, soll in (('proben', True), ('gegenproben', False)):
    treffer = sum(1 for v in (p.get(gruppe) or {}).values()
                  if v.get('ausgefuehrt') and v.get('pruefbar') and v.get('bestanden') is soll)
    print(f"  {gruppe}: {treffer} von {len(p.get(gruppe) or {})} mit Sollurteil {soll}")
    for k, v in sorted((p.get(gruppe) or {}).items()):
        print(f"    {k:<14} ausgefuehrt={v.get('ausgefuehrt')} pruefbar={v.get('pruefbar')} "
              f"bestanden={v.get('bestanden')}")
print(f"  Gesamturteil: {p.get('bestanden')}")
print(f"  Nachweis: {d.get('nachweis_sha256') or '(im Lauf gespeichert)'}")
erg['eichung'] = {'gesperrt': r.get('gesperrt'), 'lauf_startet': r.get('lauf_startet'),
                  'proben_ok': sum(1 for v in (p.get('proben') or {}).values()
                                   if v.get('bestanden') is True),
                  'gegenproben_ok': sum(1 for v in (p.get('gegenproben') or {}).values()
                                        if v.get('bestanden') is False),
                  'bestanden': p.get('bestanden')}

json.dump(erg, open('/root/biotop-t3/NACHTRAG-345.json', 'w'), ensure_ascii=False, indent=2)
