"""Gegenproben durch den Annahmepfad (aegis.pruefen) mit aufgezeichneten Kandidaten und Lazarus-Ständen.

Aufruf: python nachspiel_gegenproben.py <fall> [<fall> ...]   — Fälle siehe FAELLE.
Jeder Fall schreibt seinen Beleg nach abschluss3/nachspiel/<fall>.json. Die Arbeitskopie (DB-Sicherung, Werk)
liegt unter /tmp und wird danach entfernt; die Original-DB wird nur gelesen.
"""
import hashlib
import json
import os
import shutil
import sys
import time
from pathlib import Path

# Dieselbe Auftragsgrenze wie im Lauf (lauf38_kette.sh). Die Kasse prüft sie auch im Nachspiel — gebucht wird
# dort nur 0 € in die Arbeitskopie, weil die Anbietergrenze ersetzt und das Netz gesperrt ist.
os.environ.setdefault('BIOTOP_AUFTRAG_LAUF_AB', '26')
os.environ.setdefault('BIOTOP_AUFTRAG_BUDGET_EUR', '10')
sys.path.insert(0, '/root/biotop')
from biotop import nachspiel  # noqa: E402
from biotop.organe import kammer  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
QUELLE = Path('/root/biotop-t3/t3.db')
AUS = Path('/root/biotop-t3/abschluss3/nachspiel')
AUS.mkdir(parents=True, exist_ok=True)

# fall: (kandidat, urteil_nr, partner, verhaltensvergleich_an, masseichung_an, erwartung)
FAELLE = {
    'k2934':            (2934, None, None, True, True, 'abgelehnt'),
    'k2934_ohne_vv':    (2934, None, None, False, True, 'ueberlebt'),
    'k3121':            (3121, None, None, True, True, 'abgelehnt'),
    'k3121_ohne_vv':    (3121, None, None, False, True, 'ueberlebt'),
    'k2868':            (2867, 21057, 2868, True, True, 'ueberlebt'),
    'k2868_ohne_eichung': (2867, 21057, 2868, True, False, None),
    's2_k2904':         (2904, None, None, True, True, 'ueberlebt'),
    's2_k2904_ohne_eichung': (2904, None, None, True, False, None),
    's2_k3091':         (3091, None, None, True, True, 'ueberlebt'),
}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main(namen):
    import subprocess
    vorher = sha(QUELLE)
    for name in namen:
        kid, nr, partner, vv_an, eich_an, erwartung = FAELLE[name]
        arbeit = Path(f'/tmp/nachspiel-{name}')
        shutil.rmtree(arbeit, ignore_errors=True)
        fremd = subprocess.run(['docker', 'ps', '-q'], capture_output=True, text=True).stdout.split()
        t0 = time.monotonic()
        try:
            fall = nachspiel.vorbereiten(QUELLE, kid, arbeit, urteil_nr=nr, partner_id=partner, masseichung_an=eich_an)
            beleg = nachspiel.spielen(fall, verhaltensvergleich_an=vv_an)
            fall['con'].close()
            beleg['fall'] = name
            beleg['erwartung'] = erwartung
            beleg['erwartung_erfuellt'] = None if erwartung is None else beleg['status'] == erwartung
        except Exception as e:  # ein gescheiterter Fall ist ein Befund, kein stilles Weiter
            beleg = {'fall': name, 'kandidat': kid, 'fehler': f'{type(e).__name__}: {e}'[:3000], 'erwartung': erwartung,
                     'erwartung_erfuellt': False}
        beleg['dauer_s'] = round(time.monotonic() - t0, 1)
        beleg['fremde_container_beim_start'] = len(fremd)
        beleg['quelle_db_sha256_vorher'] = vorher
        beleg['quelle_db_sha256_nachher'] = sha(QUELLE)
        (AUS / f'{name}.json').write_text(json.dumps(beleg, ensure_ascii=False, indent=1))
        v = beleg.get('verhalten') or {}
        km = beleg.get('kernmass_kandidat') or {}
        print(f"{name:24} status={beleg.get('status')!s:10} erwartet={erwartung!s:10} "
              f"erfuellt={beleg.get('erwartung_erfuellt')!s:5} vv={v.get('grund_art')}/{v.get('anzahl_abweichungen')} "
              f"kern(gespeichert/roh)={km.get('kernmass_gespeichert')}/{km.get('kernmass_roh')} "
              f"still_im_mass={km.get('stillgelegte_regel_im_mass')} {beleg['dauer_s']}s "
              f"{beleg.get('fehler', '')[:300]}", flush=True)
        shutil.rmtree(arbeit, ignore_errors=True)


if __name__ == '__main__':
    main(sys.argv[1:] or list(FAELLE))
