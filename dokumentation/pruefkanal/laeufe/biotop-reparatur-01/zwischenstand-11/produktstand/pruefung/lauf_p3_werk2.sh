#!/bin/bash
# Phase-3-Lauf am Übungswerk 2 logmuehle: anlegen, einlegen, kartieren, Verfassung, Verträge, Gen 0 (Biotop-Mutanten), Maß
A=$1; BUDGET=$2; QUELLE=${3:-/root/uebungswerk2}; export PYTHONPATH=/root/biotop BIOTOP_AUFTRAG_LAUF_AB=14 BIOTOP_AUFTRAG_BUDGET_EUR=15; cd /root/biotop
python3 -m biotop lauf anlegen --budget $BUDGET > $A/${PREFIX}0-lauf-anlegen.txt
LAUF=$(python3 -c "import json;print(json.load(open('$A/${PREFIX}0-lauf-anlegen.txt'))['lauf'])"); echo "LAUF=$LAUF"
python3 -m biotop einlegen $LAUF logmuehle-$LAUF $QUELLE > $A/${PREFIX}1-aufnahme.json
python3 -c "import json;d=json.load(open('$A/${PREFIX}1-aufnahme.json'));print('Aufnahme:',d['status'],d['erster_testlauf']['bestanden'],'von',d['erster_testlauf']['gesamt'],d['ethik']['urteil'],'werk_id',d['werk_id'], 'Bereiche', d.get('bereiche'))"
python3 -m biotop kartieren $LAUF > $A/${PREFIX}2-landkarte.json; tr -d '\n ' < $A/${PREFIX}2-landkarte.json | cut -c1-300; echo
python3 -m biotop verfassung $LAUF /root/biotop/verfassungen/logmuehle.md /root/biotop/verfassungen/logmuehle.regeln.json --von "Hermes (Entwurf, Masterprompt v4 Phase 3; Chat-Claude bestätigt am Bericht)" > $A/${PREFIX}3-verfassung.json
python3 -m biotop vertraege $LAUF /root/biotop/verfassungen/vertraege-logmuehle --von "Hermes, abgeleitet aus Verfassung logmuehle Satz 3–5 und Docstring-Verträgen" > $A/${PREFIX}4-vertraege.json; tr -d '\n ' < $A/${PREFIX}4-vertraege.json | cut -c1-300; echo
python3 -m biotop gen0 $LAUF --ziel 0.8 > $A/${PREFIX}5-generation0.json 2> $A/${PREFIX}5-generation0.err
python3 -c "import json;d=json.load(open('$A/${PREFIX}5-generation0.json'));print('Gen0:',d['bezugsgroesse'],'| vorher',d['gefangen_vorher'],'| erreicht',d['erreicht'],'| neue Tests',d['neue_tests'],'| äquivalent',len(d['aequivalent']),'| blind nachher',d['blind_nachher'])"
python3 -m biotop mass $LAUF --bestaetigt-von "Masterprompt v4 Abschnitt 3.5 (Philipp, 19.09.2026); Tauschregel Verfassung logmuehle Satz 2; Grenzmaße gegen Bestwert des Laufs; groesste_funktion absolut 60" > $A/${PREFIX}6-mass.json
python3 -c "import json;d=json.load(open('$A/${PREFIX}6-mass.json'));print('Ausgang Schnappschuss',d['schnappschuss']['tag'],d['schnappschuss']['pruefsumme'][:16],'Kernmaß F1',d['kernmass']); [print(' ',b,{k:m.get(k) for k in ('tests_bestanden','tests_fehlgeschlagen','sicherheit_punkte','tote_funktionen','laufzeit_ms','groesste_funktion')}) for b,m in d['bereiche'].items()]"
echo $LAUF > $A/${PREFIX}LAUF
