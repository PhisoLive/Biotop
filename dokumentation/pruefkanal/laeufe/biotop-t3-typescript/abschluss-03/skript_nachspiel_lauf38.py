"""Nachspiel aller in Lauf 38 angenommenen Kandidaten durch den Annahmepfad (aegis.pruefen) mit eingehängter Abwehr.

Frage: Welche der 13 Kandidaten, die Lauf 38 ohne Verhaltensvergleich und ohne Maßeichung angenommen hat, hätte der
Annahmepfad mit beiden Organen angenommen? Gleiche Maschinerie wie nachspiel_gegenproben.py (Wegwerfkopie der DB,
Lazarus-Vorgeneration, gestellte Anbietergrenze nur für aufgezeichnete Ansagen, echte netzlose Kammer, 0 Modellaufrufe).
Je Kandidat genau ein Durchgang, vorab festgelegt; kein Kandidat wird wiederholt.
"""
import sys

sys.path.insert(0, '/root/biotop-t3/abschluss3')
import nachspiel_gegenproben as ng  # noqa: E402

ANGENOMMEN_LAUF38 = [3030, 3044, 3045, 3091, 3096, 3106, 3121, 3186, 3212, 3240, 3242, 3260, 3324]
namen = []
for kid in ANGENOMMEN_LAUF38:
    name = f'l38_k{kid}'
    # (kandidat, urteil_nr, partner, verhaltensvergleich_an, masseichung_an, erwartung) — keine Erwartung vorab:
    # das ist eine Messung, keine Gegenprobe.
    ng.FAELLE[name] = (kid, None, None, True, True, None)
    namen.append(name)

if __name__ == '__main__':
    ng.main(namen)
