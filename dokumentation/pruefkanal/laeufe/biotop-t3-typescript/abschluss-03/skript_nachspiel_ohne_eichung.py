"""Zwei Zusatz-Nachspiele durch aegis.pruefen: K3106 und K3324 (Lauf 38) ohne Maßeichung, Verhaltensvergleich an.

Frage: Mit Maßeichung weist schon das Maß beide ab (ihr einziger Gewinn waren Punkte der stillgelegten Regel), der
Verhaltensvergleich kommt dann gar nicht zum Zug. Ohne Eichung (Zustand des Maßes in Lauf 38) bestehen beide das Maß —
erkennt der Verhaltensvergleich den Schaden von K3106 (laut Unteragent: tabellenbreiten([["",""]]) [0,0] → []) und lässt
er die folgenlose Umformung K3324 durch? Je Fall genau ein Durchgang, vorab festgelegt; keine Wiederholung.
"""
import sys

sys.path.insert(0, '/root/biotop-t3/abschluss3')
import nachspiel_gegenproben as ng  # noqa: E402

NAMEN = []
for kid in (3106, 3324):
    ng.FAELLE[f'l38_k{kid}_ohne_eichung'] = (kid, None, None, True, False, None)
    NAMEN.append(f'l38_k{kid}_ohne_eichung')

if __name__ == '__main__':
    ng.main(NAMEN)
