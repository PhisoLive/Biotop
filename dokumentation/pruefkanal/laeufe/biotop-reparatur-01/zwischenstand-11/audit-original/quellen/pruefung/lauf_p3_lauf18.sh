#!/bin/bash
# Lauf 18: lagerhaus vom Stand Lauf 16 Gen 3 (Nachprobe-Ausgang), korrigierter Ankläger (F4 3.7 Fassung Philipp).
# Aufruf: PREFIX=8 lauf_p3_lauf18.sh <ausgaben-dir> <budget>
A=$1; BUDGET=$2; export PYTHONPATH=/root/biotop BIOTOP_AUFTRAG_LAUF_AB=14 BIOTOP_AUFTRAG_BUDGET_EUR=15; cd /root/biotop
python3 -m biotop lauf anlegen --budget $BUDGET > $A/${PREFIX}0-lauf-anlegen.txt
LAUF=$(python3 -c "import json;print(json.load(open('$A/${PREFIX}0-lauf-anlegen.txt'))['lauf'])"); echo "LAUF=$LAUF"
python3 -m biotop einlegen $LAUF lagerhaus-p3-$LAUF /root/uebungswerk-p3c > $A/${PREFIX}1-aufnahme.json
python3 -c "import json;d=json.load(open('$A/${PREFIX}1-aufnahme.json'));print('Aufnahme:',d['status'],d['erster_testlauf']['bestanden'],'von',d['erster_testlauf']['gesamt'],d['ethik']['urteil'],'werk_id',d['werk_id'])"
python3 -m biotop kartieren $LAUF > $A/${PREFIX}2-landkarte.json; tr -d '\n ' < $A/${PREFIX}2-landkarte.json | cut -c1-200; echo
python3 -m biotop verfassung $LAUF /root/biotop/verfassungen/lagerhaus.md /root/biotop/verfassungen/lagerhaus.regeln.json --von "Chat-Claude (Anhang A, Masterprompt v4), eingelegt durch Hermes" > $A/${PREFIX}3-verfassung.json
python3 -m biotop vertraege $LAUF /root/biotop/verfassungen/vertraege-lagerhaus --von "Hermes, abgeleitet aus Anhang A Satz 3-5 und Docstring-Vertraegen" > $A/${PREFIX}4-vertraege.json
# Vertragsfassung des Werks (mit test_katalog_wert_in_eur aus der Nachprobe) NICHT ueberschreiben:
python3 - <<'PY'
import sys, shutil; sys.path.insert(0,'/root/biotop')
from pathlib import Path
w = sorted(Path('/root/biotop/daten/werke').glob('lagerhaus-p3-*'))[-1]
q = Path('/root/uebungswerk-p3c/tests/vertraege/test_vertrag_bericht_preise.py')
(w / 'tests/vertraege/test_vertrag_bericht_preise.py').write_text(q.read_text())
print('Vertragsfassung der Nachprobe wiederhergestellt in', w.name, '| test_katalog_wert_in_eur:', 'test_katalog_wert_in_eur' in q.read_text())
PY
python3 -m biotop mass $LAUF --bestaetigt-von "Masterprompt v4 Abschnitt 3.5 (Philipp, 19.09.2026); Norm-Regel 3.7 in der Fassung Philipp 19.09.2026; Grenzmasse gegen Bestwert des Laufs" > $A/${PREFIX}6-mass.json
python3 -c "import json;d=json.load(open('$A/${PREFIX}6-mass.json'));print('Ausgang',d['schnappschuss']['tag'],d['schnappschuss']['pruefsumme'][:16],'Kernmass F1',d['kernmass']); [print(' ',b,{k:m.get(k) for k in ('tests_bestanden','tests_fehlgeschlagen','sicherheit_punkte','tote_funktionen','laufzeit_ms','groesste_funktion')}) for b,m in d['bereiche'].items()]"
echo $LAUF > $A/${PREFIX}LAUF
