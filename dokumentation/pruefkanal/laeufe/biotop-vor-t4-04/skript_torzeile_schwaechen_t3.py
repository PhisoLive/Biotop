"""Torzeile „Schwächen“ am T3-Versandwerk (Behebungsrunde 4 vor T4, Entscheidung Chat-Claude 5): die doppelte
Gegenzeugen-Prüfung ist verbindlich in der Torzeile, nicht im Annahmepfad. Nicht neu versiegelt; alle Zeilen lesen
unveränderte Messungen:
- S1: s1_harness (Stand gegen Normalversion) aus laeufe/biotop-vor-t4-02/s1/S1-STAENDE.json (Endstände Lauf 37/38),
- S2–S5: die Gegenzeugen-Ergebnisse von T3 (/root/biotop-t3/abschluss3/lauf38/c_gegenzeugen_roh.json) für Schwäche weg;
  „Verhalten gegen die Normalversion unverändert“ ist für S2–S5 NICHT gemessen (kein Harness wie für S1) — dann ist die
  Schwäche nach der Regel nicht beurteilbar, nie behoben.
Keine Kammer, kein Modell. Aufruf: python torzeile_schwaechen_t3.py > TORZEILE-SCHWAECHEN-T3.txt"""
import json
import sys
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop.kern import gegenzeugen  # noqa: E402

S1 = json.loads(Path('/root/biotop-vor-t4-02/s1/S1-STAENDE.json').read_text())
ROH = Path('/root/biotop-t3/abschluss3/lauf38/c_gegenzeugen_roh.json')
roh = json.loads(ROH.read_text()) if ROH.exists() else {}
aus = {'_quellen': {'s1': 'laeufe/biotop-vor-t4-02/s1/S1-STAENDE.json', 's2_s5': str(ROH), 's2_s5_vorhanden': ROH.exists()}}
for lauf, s1_schl, stand in (('Lauf 38', 'endstand38', 'lauf38-gen16'), ('Lauf 37', 'endstand37', 'lauf37-gen8')):
    schwaechen = {}
    s1_schw, s1_norm = gegenzeugen.s1_aus_messung(S1[s1_schl])
    schwaechen['S1'] = {'schwaeche': s1_schw, 'normal': s1_norm}
    ergebnisse = {e['id']: e for e in (roh.get(stand) or {}).get('ergebnisse') or []}
    for s in ('S2', 'S3', 'S4', 'S5'):
        e = ergebnisse.get(s)
        schwaechen[s] = {'schwaeche': {'verletzt': bool(e['verletzt'])} if e is not None else None, 'normal': None}
    z = gegenzeugen.torzeile_schwaechen(schwaechen)
    bisher = sorted(s for s in ('S1', 'S2', 'S3', 'S4', 'S5') if (schwaechen[s]['schwaeche'] or {}).get('verletzt') is False)
    aus[lauf] = {'stand': stand, 'zeile': z['zeile'], 'behoben': z['behoben'], 'nicht_beurteilbar': z['nicht_beurteilbar'],
                 'schwaeche_weg_nur_gegenzeuge': bisher,
                 'je': {k: {x: v[x] for x in ('behoben', 'schwaeche_weg', 'normal_unveraendert')} for k, v in z['je_schwaeche'].items()}}
    print(f"{lauf} ({stand}): {z['zeile']}")
    print(f"   nur der versiegelte Gegenzeuge (Schwäche weg): {len(bisher)} von 5 {bisher}")
Path(__file__).with_name('TORZEILE-SCHWAECHEN-T3.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1))
