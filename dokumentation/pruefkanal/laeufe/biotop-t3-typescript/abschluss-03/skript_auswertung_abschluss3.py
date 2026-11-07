"""Auswertung für abschluss-03 (nur lesend, kein Kammerlauf, kein Modellaufruf).

Quellen:
- Schnappschuss der Lauf-DB einschließlich WAL: /root/biotop-t3/schnappschuss-abschluss3/t3.db (mode=ro). Eine frühere
  Lesung mit immutable=1 hatte die WAL übergangen (190 Protokollzeilen, Freigabe Gen 16, Gen 17). Diese Auswertung
  ersetzt die damit gerechneten Zahlen; KERNMASS-BEREINIGT.*, AUSWERTUNG38-DB.txt und DOPPELUNG-LAUF38.json bleiben als
  Beleg des Fehlers liegen.
- Belege der Nachspiele durch aegis.pruefen: abschluss3/nachspiel-serie1/, abschluss3/nachspiel/.
- Lazarus-Archive (nur gelesen).
Ausgabe: AUSWERTUNG-ABSCHLUSS3.json (+ stdout als AUSWERTUNG-ABSCHLUSS3.txt).
"""
import json
import sqlite3
import sys
import tarfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop.kern import messgeraet  # noqa: E402
from biotop.organe import masseichung, verfassung  # noqa: E402

DB = '/root/biotop-t3/schnappschuss-abschluss3/t3.db'
B = Path('/root/biotop-t3/abschluss3')
REGEL = 'security/detect-object-injection'
c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
c.row_factory = sqlite3.Row
aus = {'quelle_db': DB}


def lj(s):
    return json.loads(s) if s else None


def abschnitt(t):
    print(f'\n======== {t} ========')


def sicher(name, f):
    try:
        f()
    except Exception as e:  # ein gescheiterter Abschnitt ist ein Befund; die anderen laufen weiter
        print(f'!! Abschnitt {name} gescheitert: {type(e).__name__}: {e}')
        aus.setdefault('fehler', {})[name] = f'{type(e).__name__}: {e}'


def a_nachspiele():
    abschnitt('A. Nachspiele durch aegis.pruefen (Annahmepfad)')
    zeilen = []
    for serie in ('nachspiel-serie1', 'nachspiel'):
        for p in sorted((B / serie).glob('*.json')):
            b = json.loads(p.read_text())
            km = b.get('kernmass_kandidat') or {}
            ber = km.get('bereiche') or {}
            v = b.get('verhalten') or {}
            ung = v.get('ungedeckt')
            grenze = b.get('anbietergrenze') or []
            ms = b.get('mass') or {}
            g_text = b.get('grund') or ''
            if b.get('status') == 'ueberlebt':
                entscheid = 'ueberlebt'
            elif g_text.startswith('Verhaltensvergleich'):
                entscheid = 'verhaltensvergleich'
            elif g_text.startswith('Grenzmaß gerissen') and 'laufzeit_ms' in g_text:
                entscheid = 'grenzmass_laufzeit'
            elif g_text.startswith('Kernmaß unverändert'):
                entscheid = 'kernmass_unveraendert'
            elif g_text.startswith('Nische schnell: Laufzeit nicht'):
                entscheid = 'nische_schnell_unter_15_prozent'
            else:
                entscheid = 'sonst: ' + g_text[:40]
            nische = (c.execute('SELECT nische FROM kandidaten WHERE id=?', (b.get('kandidat'),)).fetchone() or {'nische': None})['nische']
            z = {'serie': serie, 'fall': b.get('fall') or p.stem, 'kandidat': b.get('kandidat'), 'partner': b.get('partner'),
                 'nische': nische, 'entscheidung': entscheid,
                 'zuwachs': ms.get('zuwachs'), 'kern_basis': ms.get('kern_basis'), 'kern_kandidat_mass': ms.get('kern_kandidat'),
                 'grenzen_gerissen': ms.get('grenzen_gerissen'), 'laufzeit_gewinne': ms.get('laufzeit_gewinne'),
                 'lauf': b.get('lauf'), 'generation': b.get('generation'), 'vorgeneration': b.get('vorgeneration'),
                 'vv_an': b.get('verhaltensvergleich_an'), 'eichung_an': b.get('masseichung_an'),
                 'eichung_herkunft': b.get('eichung_herkunft'),
                 'status': b.get('status'), 'erwartung': b.get('erwartung'), 'erfuellt': b.get('erwartung_erfuellt'),
                 'status_lauf': b.get('status_aufgezeichnet'), 'grund_lauf': (b.get('grund_aufgezeichnet') or '')[:220],
                 'grund': (b.get('grund') or b.get('fehler') or '')[:300],
                 'vv_art': v.get('grund_art'), 'vv_abweichungen': v.get('anzahl_abweichungen'),
                 'vv_ungedeckt': len(ung) if isinstance(ung, list) else ung,
                 'kern_gespeichert': km.get('kernmass_gespeichert'), 'kern_roh': km.get('kernmass_roh'),
                 'regel_gezaehlt_in': sorted(x for x, y in ber.items() if REGEL in (y.get('regeln_gezaehlt') or [])),
                 'regel_stillgelegt_in': sorted(x for x, y in ber.items() if REGEL in (y.get('regeln_stillgelegt') or [])),
                 'lazarus_stimmt': (b.get('lazarus') or {}).get('stimmt'),
                 'db_unveraendert': b.get('quelle_db_sha256_vorher') == b.get('quelle_db_sha256_nachher'),
                 'modellaufrufe_echt': b.get('modellaufrufe_echt'), 'anbieter_anfragen': len(grenze),
                 'anbieter_beantwortet': sum(1 for x in grenze if x.get('beantwortet')),
                 'kammerlaeufe': b.get('kammerlaeufe'), 'dauer_s': b.get('dauer_s'),
                 'fremde_container': b.get('fremde_container_beim_start'), 'fehler': b.get('fehler')}
            zeilen.append(z)
            print(f"{serie:17} {z['fall']:26} K{z['kandidat']} {z['status']!s:9} (Lauf: {z['status_lauf']!s:9}) "
                  f"erwartet={z['erwartung']!s:9} vv={z['vv_art']}/{z['vv_abweichungen']}/ungedeckt {z['vv_ungedeckt']} "
                  f"kern={z['kern_gespeichert']}/{z['kern_roh']} Regel gezählt {z['regel_gezaehlt_in']} ruht {z['regel_stillgelegt_in']}")
            print(f"{'':44} Grund: {z['grund'][:200]}")
    aus['nachspiele'] = zeilen
    print('\nEntscheidende Stufe je Fall (Eichung an/aus × Verhaltensvergleich an/aus):')
    tafel = Counter((z['eichung_an'], z['vv_an'], z['entscheidung']) for z in zeilen)
    for (e, v, s), n in sorted(tafel.items(), key=lambda x: (str(x[0][0]), str(x[0][1]), x[0][2])):
        print(f'   Eichung {e!s:5} VV {v!s:5} {s:34} {n}')
    lz = [z for z in zeilen if z['entscheidung'] == 'grenzmass_laufzeit']
    print(f'Laufzeit-Grenzmaß entschied in {len(lz)} von {len(zeilen)} Fällen; im Lauf waren alle {len(lz)} Kandidaten angenommen/überlebend: '
          f'{all(z["status_lauf"] == "ueberlebt" for z in lz)}')
    for z in lz:
        print(f"   {z['serie']:17} {z['fall']:24} K{z['kandidat']} ({z['nische']}) zuwachs {z['zuwachs']} gerissen: "
              f"{'; '.join(g[:70] for g in (z['grenzen_gerissen'] or []))}")
    print('Fälle mit Eichung, deren Maßzuwachs ohne die stillgelegte Regel ≤ 0 ist (außer Nische schnell) — die Eichung weist sie '
          'unabhängig von der Laufzeit ab (Kernmaßfelder sind deterministisch):')
    for z in zeilen:
        if z['eichung_an'] and z['nische'] != 'schnell' and z['zuwachs'] is not None and z['zuwachs'] <= 0:
            print(f"   {z['serie']:17} {z['fall']:24} K{z['kandidat']} ({z['nische']}) Kernmaß {z['kern_basis']} → {z['kern_kandidat_mass']} "
                  f"(Zuwachs {z['zuwachs']}), entschieden durch {z['entscheidung']}")
    mit = [z for z in zeilen if z['eichung_an'] and not z['fehler']]
    ohne = [z for z in zeilen if z['eichung_an'] is False and not z['fehler']]
    print(f'\nFälle gesamt {len(zeilen)}, davon mit Fehler {sum(1 for z in zeilen if z["fehler"])}')
    print(f'Eichung an: {len(mit)} Fälle; Regel {REGEL} im gespeicherten Maß gezählt in {sum(1 for z in mit if z["regel_gezaehlt_in"])} '
          f'von {len(mit)}; als stillgelegt ausgewiesen in {sum(1 for z in mit if z["regel_stillgelegt_in"])} von {len(mit)}')
    print(f'Eichung aus (Gegenprobe): {len(ohne)} Fälle; Regel gezählt in {sum(1 for z in ohne if z["regel_gezaehlt_in"])} von {len(ohne)}')
    print(f'Original-DB unverändert: {sum(z["db_unveraendert"] for z in zeilen)} von {len(zeilen)}; Lazarus-Prüfsumme stimmt: '
          f'{sum(1 for z in zeilen if z["lazarus_stimmt"])} von {len(zeilen)}; echte Modellaufrufe Σ '
          f'{sum(z["modellaufrufe_echt"] or 0 for z in zeilen)}; Anbieteranfragen Σ {sum(z["anbieter_anfragen"] for z in zeilen)}, '
          f'davon aus Aufzeichnung beantwortet {sum(z["anbieter_beantwortet"] for z in zeilen)}')


def b_kernmass():
    abschnitt('B. Kernmaß roh und ohne die stillgelegte Regel, je angenommener Generation')
    for lauf in (37, 38):
        nachweis = lj(c.execute('SELECT ergebnis FROM vorspann_nachweise WHERE lauf_id=?', (lauf,)).fetchone()['ergebnis'])
        werk_id = c.execute('SELECT werk_id FROM laeufe WHERE id=?', (lauf,)).fetchone()['werk_id']
        eich = masseichung.eichen(nachweis['basis'], masseichung.sauberer_bereich(verfassung.lesen(c, werk_id)))
        kurz = {k: eich.get(k) for k in ('sauberer_bereich', 'stillgelegt', 'funde_im_sauberen', 'regeln_geprueft', 'regeln_stillgelegt')}
        print(f'Lauf {lauf}: Eichung aus der versiegelten Vorspann-Messung: {kurz}')
        reihe = []
        for g in c.execute("SELECT nummer, masse, kandidaten FROM generationen WHERE lauf_id=? AND status='angenommen' "
                           "ORDER BY nummer", (lauf,)):
            m = lj(g['masse'])
            k = lj(g['kandidaten']) or {}
            je = {b: [-(x['tests_fehlgeschlagen'] + x['sicherheit_punkte'] + x['tote_funktionen']),
                      -(x['tests_fehlgeschlagen'] + masseichung.sicherheit_bereinigt(x, eich) + x['tote_funktionen'])]
                  for b, x in m['bereiche'].items()}
            z = {'gen': g['nummer'], 'roh': messgeraet.kernmass_f2(m), 'bereinigt': masseichung.kernmass_bereinigt(m, eich),
                 'gewaehlt': k.get('_gewaehlt'), 'je_bereich_roh_bereinigt': je}
            reihe.append(z)
            print(f"  Gen {z['gen']:>2}: roh {z['roh']:>4}  bereinigt {z['bereinigt']:>4}  gewählt {z['gewaehlt']}  "
                  + '; '.join(f'{b} {r}/{s}' for b, (r, s) in je.items()))
        aus[f'kernmass_lauf{lauf}'] = {'eichung': kurz, 'reihe': reihe}


def c_minderungen():
    abschnitt('C. Sicherheitsminderungen Lauf 38 je Regel, angenommener Generation und Kandidat')
    nsp = {z['kandidat']: z for z in aus.get('nachspiele', []) if z['serie'] == 'nachspiel'
           and z['fall'] == f"l38_k{z['kandidat']}"}
    vorher, zeilen = None, []
    for g in c.execute("SELECT nummer, masse, kandidaten FROM generationen WHERE lauf_id=38 AND status='angenommen' ORDER BY nummer"):
        m = lj(g['masse'])
        k = lj(g['kandidaten']) or {}
        punkte = {b: Counter() for b in m['bereiche']}
        for b, x in m['bereiche'].items():
            for f in x.get('sicherheit_befunde') or []:
                punkte[b][f['test']] += masseichung._punkte(f)
        if vorher is not None:
            for b in punkte:
                for regel in sorted(set(punkte[b]) | set(vorher[b])):
                    d = punkte[b][regel] - vorher[b][regel]
                    if d:
                        kid = (k.get('_gewaehlt') or {}).get(b)
                        n = nsp.get(kid) or {}
                        z = {'gen': g['nummer'], 'bereich': b, 'regel': regel, 'vorher': vorher[b][regel], 'nachher': punkte[b][regel],
                             'kandidat': kid, 'nachspiel_status': n.get('status'), 'nachspiel_grund': (n.get('grund') or '')[:160]}
                        zeilen.append(z)
                        print(f"  Gen {z['gen']:>2} {b:8} {regel:36} {z['vorher']:>3} → {z['nachher']:>3}  K{kid}  "
                              f"mit Abwehr: {z['nachspiel_status']}  | {z['nachspiel_grund'][:110]}")
        vorher = punkte
    aus['minderungen_lauf38'] = zeilen
    print('\n  Angenommene Kandidaten Lauf 38 mit Abwehr am Annahmepfad (je 1 Durchgang):')
    for g in c.execute("SELECT nummer, kandidaten FROM generationen WHERE lauf_id=38 AND status='angenommen' AND nummer>0 ORDER BY nummer"):
        for b, kid in sorted(((lj(g['kandidaten']) or {}).get('_gewaehlt') or {}).items()):
            kz = c.execute('SELECT nische, grund FROM kandidaten WHERE id=?', (kid,)).fetchone()
            n = nsp.get(kid) or {}
            print(f"  Gen {g['nummer']:>2} {b:8} K{kid} ({kz['nische']}): Lauf 38 „{(kz['grund'] or '')[:90]}“ → {n.get('status')}: "
                  f"{(n.get('grund') or '')[:120]}")


def d_doppelung():
    abschnitt('D. Tor 2 Zeile 8 nach der Methode aus Vorbedingung 1, Lauf 38')
    urteile = [dict(lj(r['inhalt']), nr=r['nr']) for r in c.execute("SELECT nr, inhalt FROM protokoll WHERE art='aegis.urteil' ORDER BY nr")]
    u38 = [u for u in urteile if u.get('lauf_id') == 38]
    mit = [u for u in u38 if isinstance(u.get('angriff'), dict) and 'gesamt' in u['angriff']]
    je = {}
    for u in mit:
        je.setdefault(u['kandidat'], u)
    zeilen, gesehen = [], {}
    for kid, u in sorted(je.items(), key=lambda x: x[1]['nr']):
        for test, schl in sorted((u.get('behauptungen') or {}).items()):
            gruppe = (u['bereich'], schl)
            zeilen.append({'kandidat': kid, 'urteil_nr': u['nr'], 'bereich': u['bereich'], 'test': test, 'schluessel': schl,
                           'doppelung': gruppe in gesehen, 'erste': gesehen.get(gruppe)})
            gesehen.setdefault(gruppe, f'K{kid}:{test}')
    n, d = len(zeilen), sum(z['doppelung'] for z in zeilen)
    gesamt_alle = sum(u['angriff']['gesamt'] for u in mit)
    gesamt_je = sum(u['angriff']['gesamt'] for u in je.values())
    print(f'Urteile Lauf 38: {len(u38)}; mit ausgeführtem Angriff: {len(mit)} (verschiedene Kandidaten: {len(je)})')
    print(f'erzeugte Angriffstests: Σ über alle Urteile {gesamt_alle}; Σ je Kandidat (erstes Urteil) {gesamt_je}')
    print(f'davon mit aufgezeichneter Behauptung (nur Treffer, seit 1cf2eb1): {n}; Doppelungen {d} von {n}')
    aus['doppelung_lauf38'] = {'urteile': len(u38), 'urteile_mit_angriff': len(mit), 'kandidaten_mit_angriff': len(je),
                               'angriffstests_alle_urteile': gesamt_alle, 'angriffstests_je_kandidat': gesamt_je,
                               'mit_behauptung': n, 'doppelungen': d, 'zeilen': zeilen}


def e_immun():
    abschnitt('E. Immunisierung auf dem TypeScript-Pfad, Lauf 38')
    st = Counter(r['status'] for r in c.execute('SELECT status FROM immunsystem WHERE lauf_id=38'))
    namen_db = [r['name'] for r in c.execute('SELECT name FROM immunsystem WHERE lauf_id=38')]
    arch = c.execute('SELECT archiv FROM lazarus WHERE lauf_id=38 AND generation=16').fetchone()['archiv']
    with tarfile.open(arch) as t:
        dateien = [m.name for m in t.getmembers() if m.isfile()]
    imm = sorted(x for x in dateien if '_immun_' in x)
    im_werk = sorted(n for n in namen_db if any(n in x for x in imm))
    nz = {r['art']: r['n'] for r in c.execute("SELECT art, COUNT(*) n FROM neutralzaehler WHERE lauf_id=38 AND organ='aegis._anhaengen' GROUP BY art")}
    print(f'Immunsystem Lauf 38: {sum(st.values())} Einträge, je Status {dict(st)}')
    print(f'Immun-Testdateien im Endstand lauf38-gen16: {len(imm)}: {imm}')
    print(f'Einträge des Laufs, die als Datei im Endstand liegen: {len(im_werk)} von {len(namen_db)}')
    print(f'Neutralzähler aegis._anhaengen Lauf 38: {nz or "0 Fälle"}')
    aus['immunisierung_lauf38'] = {'status': dict(st), 'eintraege': len(namen_db), 'immun_dateien_endstand': imm,
                                   'eintraege_im_endstand': im_werk, 'anhaengen_neutralzaehler': nz}


def f_testbestand():
    abschnitt('F. Testbestand und Generation 0')
    for lauf in (37, 38):
        g = c.execute("SELECT nummer, masse FROM generationen WHERE lauf_id=? AND status='angenommen' ORDER BY nummer", (lauf,)).fetchall()
        for x in (g[0], g[-1]):
            m = lj(x['masse'])
            je = {b: y['tests_gesamt'] for b, y in m['bereiche'].items()}
            print(f'  Lauf {lauf} Gen {x["nummer"]:>2}: tests_gesamt Σ {sum(je.values())} {je}')
    for r in c.execute("SELECT lauf_id, art, grund, COUNT(*) n FROM neutralzaehler WHERE organ='generation0._testlauf' "
                       "AND lauf_id IN (37, 38) GROUP BY lauf_id, art, grund ORDER BY lauf_id, art"):
        print(f'  Neutralzähler generation0._testlauf Lauf {r["lauf_id"]}: {r["art"]} {r["grund"]} {r["n"]}')


def g_neutral():
    abschnitt('G. Neutralzähler Lauf 38 (Mehrheitsregel: geurteilt > Hälfte der Fälle)')
    je = {}
    for r in c.execute("SELECT organ, art, COUNT(*) n FROM neutralzaehler WHERE lauf_id=38 GROUP BY organ, art"):
        je.setdefault(r['organ'], Counter())[r['art']] = r['n']
    for organ in ('aegis.behauptung', 'aegis._anhaengen', 'gedaechtnis.aenderungsziel', 'generation0._testlauf', 'verhaltensvergleich'):
        z = je.get(organ, Counter())
        n = sum(z.values())
        print(f"  {organ:30} geurteilt {z['geurteilt']} von {n}  → {'trägt' if n and z['geurteilt'] * 2 > n else 'trägt NICHT (keine Mehrheit)'}")
    aus['neutralzaehler_lauf38'] = {o: dict(z) for o, z in je.items()}


def h_kasse():
    abschnitt('H. Kasse (Auftrag = Läufe 26–38)')
    zeilen = [dict(r) for r in c.execute('SELECT lauf_id, COUNT(*) n, ROUND(SUM(kosten_eur), 6) eur FROM kasse WHERE lauf_id >= 26 '
                                         'GROUP BY lauf_id ORDER BY lauf_id')]
    for z in zeilen:
        print(f"  Lauf {z['lauf_id']}: {z['n']} Buchungen, {z['eur']} €")
    n = sum(z['n'] for z in zeilen)
    eur = round(sum(z['eur'] or 0 for z in zeilen), 6)
    print(f'  Σ Läufe 26–38: {n} Buchungen, {eur} € von 10,00 €')
    aus['kasse'] = {'je_lauf': zeilen, 'buchungen': n, 'eur': eur}


def i_generationen():
    abschnitt('I. Generationen Lauf 38')
    st = [(r['nummer'], r['status']) for r in c.execute('SELECT nummer, status FROM generationen WHERE lauf_id=38 ORDER BY nummer')]
    print('  ', st)
    print(f"  angenommen ohne Gen 0: {sum(1 for n, s in st if s == 'angenommen' and n > 0)} von {sum(1 for n, s in st if n > 0)}")
    aus['generationen_lauf38'] = st


def j_grenze():
    abschnitt('J. Rauschtoleranzen und die knappste Grenzmaß-Ablehnung im Nachspiel')
    for lauf in (37, 38):
        n = lj(c.execute('SELECT ergebnis FROM vorspann_nachweise WHERE lauf_id=?', (lauf,)).fetchone()['ergebnis'])
        tol = (n.get('rauschen') or {}).get('toleranz') or {}
        print(f'  Lauf {lauf} Rauschtoleranz je Bereich (ungerundet): {tol}')
        aus.setdefault('rauschtoleranz', {})[lauf] = tol
    b = json.loads((B / 'nachspiel' / 'l38_k3121.json').read_text())
    best = (b.get('laufzeit_ms') or {}).get('bericht', {}).get('bestwert')
    kand = (b.get('laufzeit_ms') or {}).get('bericht', {}).get('kandidat')
    tol = aus['rauschtoleranz'][38].get('bericht')
    if best and kand and tol:
        g = best * tol
        print(f'  l38_k3121 bericht: Bestwert {best} × Toleranz {tol} = Grenze {g!r}; Kandidat {kand!r}; '
              f'überschritten um {kand - g:.6f} ms ({100 * (kand / g - 1):.4f} %); die Meldung rundet die Grenze auf „{g:.1f}“')
        aus['knappste_grenze'] = {'bestwert': best, 'toleranz': tol, 'grenze': g, 'kandidat': kand, 'differenz_ms': kand - g}


for name, f in (('A', a_nachspiele), ('B', b_kernmass), ('C', c_minderungen), ('D', d_doppelung), ('E', e_immun),
                ('F', f_testbestand), ('G', g_neutral), ('H', h_kasse), ('I', i_generationen), ('J', j_grenze)):
    sicher(name, f)
(B / 'AUSWERTUNG-ABSCHLUSS3.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1, default=str))
