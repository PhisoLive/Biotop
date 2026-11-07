"""Stufe-2-Last bemessen und eichen (Behebungsrunde 5 vor T4, Entscheidung Chat-Claude 6): Rauschmessung der Stufe 2 —
dieselbe Regel und dasselbe Instrument wie der Vorspann (eichung.rauschmessung mit eichung.laufzeit_einmal) — an den
Vorgenerationen von K2904 (Lauf 37) und K3091 (Lauf 38), für Varianten der eingang-Last (Wiederholungen W.eingang;
Stufe 1 wurde ebenso „gemessen gewählt“). Varianten abwechselnd (nicht blockweise), je Messung eine JSON-Zeile.
Läuft an einer eingefrorenen Kopie des Baums (Argument 1), T3-DB nur gelesen (Kopie über nachspiel.vorbereiten).
Kein Modellaufruf. Aufruf: python stufe2_eichung.py <baumkopie> > STUFE2-EICHUNG.txt"""
import hashlib
import json
import shutil
import sys
import time
from pathlib import Path

BAUM = Path(sys.argv[1])
sys.path.insert(0, str(BAUM))
from biotop import lauf as L  # noqa: E402
from biotop import nachspiel  # noqa: E402
from biotop.organe import eichung, kammer  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
QUELLE = Path('/root/biotop-t3/schnappschuss-abschluss3/t3.db')
AUS = Path(__file__).with_name('STUFE2-EICHUNG.jsonl')
vorher = hashlib.sha256(QUELLE.read_bytes()).hexdigest()
ref2 = L._referenzlast('versandwerk-t3-02', 'src', 2)
ANKER = 'const W = { eingang: 60,'
assert ref2 and ref2.count(ANKER) == 1, 'Anker der Stufe-2-Last fehlt'
VARIANTEN = [('W60_ist', 60), ('W240', 240), ('W480', 480)]
RUNDEN = 4                 # je Stand und Variante; Varianten abwechselnd
AUS.write_text('')
print(f'start {time.strftime("%H:%M:%S")} baum={BAUM} ref2_sha={hashlib.sha256(ref2.encode()).hexdigest()[:16]}', flush=True)
for kid in (2904, 3091):
    arbeit = Path(f'/tmp/r5-eichung-k{kid}')
    shutil.rmtree(arbeit, ignore_errors=True)
    fall = nachspiel.vorbereiten(QUELLE, kid, arbeit, rauschen_stufe2=False)
    for runde in range(RUNDEN):
        for name, w in VARIANTEN:
            last = ref2.replace(ANKER, f'const W = {{ eingang: {w},')
            t0 = time.monotonic()
            r = eichung.rauschmessung(fall['con'], fall['lauf_id'], fall['werk_id'], fall['werk'], fall['bereiche'],
                                      fall['paket'], last, eichung.laufzeit_einmal)
            z = {'kandidat': kid, 'vorgeneration': fall['basis_generation'], 'variante': name, 'w_eingang': w,
                 'runde': runde, 'gesperrt': r['gesperrt'], 'toleranz': r['toleranz'],
                 'kammerlauf_s': r.get('kammerlauf_s'), 'dauer_s': round(time.monotonic() - t0, 1),
                 'eingang': {k: r['bereiche']['eingang'].get(k) for k in ('werte', 'toleranz', 'spannweite', 'meldung')},
                 'werte': {b: r['bereiche'][b].get('werte') for b in fall['bereiche']}}
            with AUS.open('a') as f:
                f.write(json.dumps(z, ensure_ascii=False) + '\n')
            print(f"K{kid} {name:8} r{runde} gesperrt={r['gesperrt']} eingang={z['eingang']['toleranz']} "
                  f"längster Kammerlauf={max(r.get('kammerlauf_s') or [0]):.1f}s", flush=True)
    fall['con'].close()
    shutil.rmtree(arbeit, ignore_errors=True)
print('t3.db unverändert:', hashlib.sha256(QUELLE.read_bytes()).hexdigest() == vorher, flush=True)
print(f'ende {time.strftime("%H:%M:%S")}', flush=True)
