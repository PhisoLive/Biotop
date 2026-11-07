"""Gegenproben der Vorbedingungen für T4 durch den Annahmepfad (aegis.pruefen) — aufgezeichnete T3-Kandidaten,
Lazarus-Vorgeneration, echte netzlose Kammer, Anbietergrenze gestellt (nur aufgezeichnete Ansagen), 0 Modellaufrufe.

Quelle: Schnappschuss der Lauf-DB mit WAL (nur gelesen; das Nachspiel arbeitet an einer Kopie unter /tmp).
Aufruf: python nachspiel_vor_t4.py <fall> [...]. Je Fall ein vorab festgelegter Durchgang; Beleg unter nachspiel/<fall>.json.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

os.environ.setdefault('BIOTOP_AUFTRAG_LAUF_AB', '26')
os.environ.setdefault('BIOTOP_AUFTRAG_BUDGET_EUR', '10')
sys.path.insert(0, '/root/biotop')
from biotop import nachspiel  # noqa: E402
from biotop.organe import kammer  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
QUELLE = Path('/root/biotop-t3/schnappschuss-abschluss3/t3.db')
AUS = Path(os.environ.get('NACHSPIEL_AUS', '/root/biotop-vor-t4-04/nachspiel/d1'))  # Review Nr. 7: zweiter Durchgang am Commit in eigenen Ordner
AUS.mkdir(parents=True, exist_ok=True)

# fall: (kandidat, urteil_nr, partner, verhaltensvergleich_an, masseichung_an, erwartung, vorbedingung, vv_optionen)
# Behebungsrunde 4 vor T4: Gegenprobe Entscheidung 1 (Vergleichslast Stufe 2) — K2904 und K3091 in drei Durchgängen
# gleich; Gegenprobe Entscheidung 3 — K2868 mit Deckung je Muster: die Abweichungen bei ungültigen Eingaben
# (Randfälle 'a', 'Ä-1', 'x'×40) gedeckt, die Weißraum-Muster ungedeckt (abgelehnt).
FAELLE = {
    's2_k2904': (2904, None, None, True, True, 'ueberlebt', 1, {}),
    's2_k3091': (3091, None, None, True, True, 'ueberlebt', 1, {}),
    'k2868': (2867, 21057, 2868, True, True, 'abgelehnt', 2, {'korpus_erweitert': True, 'deckungsregel': 'muster'}),
}


def code_stand():
    """Review vor T4 Nr. 7: jeder Beleg trägt den Code-Stand, an dem er entstand (Commit + sauberer Arbeitsbaum)."""
    head = subprocess.run(['git', '-C', '/root/biotop', 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    st = subprocess.run(['git', '-C', '/root/biotop', 'status', '--short', '--', 'biotop', 'tests'],
                        capture_output=True, text=True).stdout.strip()
    return {'commit': head, 'arbeitsbaum_sauber': st == '', 'status': st[:500]}


STAND_BEIM_IMPORT = code_stand()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main(namen):
    vorher = sha(QUELLE)
    for name in namen:
        kid, nr, partner, vv_an, eich_an, erwartung, vb, vv_opt = FAELLE[name]
        arbeit = Path(f'/tmp/nachspiel-vor-t4-{name}')
        shutil.rmtree(arbeit, ignore_errors=True)
        fremd = subprocess.run(['docker', 'ps', '-q'], capture_output=True, text=True).stdout.split()
        t0 = time.monotonic()
        try:
            fall = nachspiel.vorbereiten(QUELLE, kid, arbeit, urteil_nr=nr, partner_id=partner, masseichung_an=eich_an)
            beleg = nachspiel.spielen(fall, verhaltensvergleich_an=vv_an, vv_optionen=vv_opt)
            fall['con'].close()
        except Exception as e:  # ein gescheiterter Fall ist ein Befund, kein stilles Weiter
            beleg = {'kandidat': kid, 'fehler': f'{type(e).__name__}: {e}'[:3000]}
        beleg.update(code_stand_beim_import=STAND_BEIM_IMPORT, code_stand_nach_fall=code_stand(),
                     fall=name, vorbedingung=vb, erwartung=erwartung, vv_optionen=vv_opt,
                     erwartung_erfuellt=None if erwartung is None else beleg.get('status') == erwartung,
                     dauer_s=round(time.monotonic() - t0, 1), fremde_container_beim_start=len(fremd),
                     quelle_db_sha256_vorher=vorher, quelle_db_sha256_nachher=sha(QUELLE))
        (AUS / f'{name}.json').write_text(json.dumps(beleg, ensure_ascii=False, indent=1))
        v = beleg.get('verhalten') or {}
        lz = beleg.get('laufzeit_gepaart') or {}
        lz_txt = {b: (x.get('basis'), x.get('kandidat')) for b, x in (lz.get('bereiche') or {}).items()} if lz else None
        print(f"{name:20} status={beleg.get('status')!s:15} erwartet={erwartung!s:10} erfuellt={beleg.get('erwartung_erfuellt')!s:5} "
              f"vv={v.get('grund_art')}/{v.get('anzahl_abweichungen')} beob={v.get('beobachtete_funktionen')} "
              f"bezug={beleg.get('laufzeit_bezug')} {beleg['dauer_s']}s | {(beleg.get('grund') or beleg.get('fehler') or '')[:230]}"
              f" | gepaart={lz_txt} | gewinn={(beleg.get('gewinn_nachmessung') or {}).get('ergebnis')}"
              f" | ungedeckt={v.get('ungedeckt_aufschluesselung')} | gedeckt={len(v.get('gedeckt') or {})}"
              f" | stufe={beleg.get('laufzeit_stufe')} | rauschen={beleg.get('rauschen_herkunft')}"
              f" | toleranz={beleg.get('rauschtoleranz')} gesperrt={beleg.get('gesperrte_bereiche')}", flush=True)
        shutil.rmtree(arbeit, ignore_errors=True)


if __name__ == '__main__':
    main(sys.argv[1:] or list(FAELLE))
