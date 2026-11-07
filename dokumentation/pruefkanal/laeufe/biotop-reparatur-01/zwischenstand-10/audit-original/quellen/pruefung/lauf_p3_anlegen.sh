#!/bin/bash
# Phase-3-Lauf am lagerhaus vom Ausgang Lauf 13 Gen 13 (/root/uebungswerk-p3): anlegen, einlegen, kartieren, Verfassung, Verträge, Gen 0, Maß.
# Aufruf: PREFIX=n lauf_p3_anlegen.sh <ausgaben-dir> <laufbudget_eur> [werkname-suffix]
A=$1; BUDGET=$2; SUF=${3:-p3}; export PYTHONPATH=/root/biotop BIOTOP_AUFTRAG_LAUF_AB=14 BIOTOP_AUFTRAG_BUDGET_EUR=15; cd /root/biotop
python3 -m biotop lauf anlegen --budget $BUDGET > $A/${PREFIX}0-lauf-anlegen.txt
LAUF=$(python3 -c "import json;print(json.load(open('$A/${PREFIX}0-lauf-anlegen.txt'))['lauf'])"); echo "LAUF=$LAUF"
python3 -m biotop einlegen $LAUF lagerhaus-$SUF-$LAUF /root/uebungswerk-p3 > $A/${PREFIX}1-aufnahme.json
python3 -c "import json;d=json.load(open('$A/${PREFIX}1-aufnahme.json'));print('Aufnahme:',d['status'],d['erster_testlauf']['bestanden'],'von',d['erster_testlauf']['gesamt'],d['ethik']['urteil'],'werk_id',d['werk_id'])"
python3 -m biotop kartieren $LAUF > $A/${PREFIX}2-landkarte.json; tr -d '\n ' < $A/${PREFIX}2-landkarte.json | cut -c1-300; echo
python3 -m biotop verfassung $LAUF /root/biotop/verfassungen/lagerhaus.md /root/biotop/verfassungen/lagerhaus.regeln.json --von "Chat-Claude (Anhang A, Masterprompt v4), eingelegt durch Hermes" > $A/${PREFIX}3-verfassung.json
python3 -m biotop vertraege $LAUF /root/biotop/verfassungen/vertraege-lagerhaus --von "Hermes, abgeleitet aus Anhang A Satz 3–5 und Docstring-Verträgen (unverändert seit Lauf 12)" > $A/${PREFIX}4-vertraege.json; tr -d '\n ' < $A/${PREFIX}4-vertraege.json | cut -c1-300; echo
python3 -m biotop gen0 $LAUF --mutanten /root/versiegelt/MUTANTEN-phase3.json --ziel 16 > $A/${PREFIX}5-generation0.json 2> $A/${PREFIX}5-generation0.err
python3 -c "import json;d=json.load(open('$A/${PREFIX}5-generation0.json'));print('Gen0:',d['bezugsgroesse'],'| vorher',d['gefangen_vorher'],'| erreicht',d['erreicht'],'| neue Tests',d['neue_tests'],'| äquivalent',d['aequivalent'],'| blind nachher',d['blind_nachher'])"
python3 -m biotop mass $LAUF --bestaetigt-von "Masterprompt v4 Abschnitt 3.5 (Philipp, 19.09.2026); Tauschregel Anhang A Satz 2; Grenzmaße gegen Bestwert des Laufs; groesste_funktion absolut 60" > $A/${PREFIX}6-mass.json
python3 -c "import json;d=json.load(open('$A/${PREFIX}6-mass.json'));print('Ausgang Schnappschuss',d['schnappschuss']['tag'],d['schnappschuss']['pruefsumme'][:16],'Kernmaß F1',d['kernmass']); [print(' ',b,{k:m.get(k) for k in ('tests_bestanden','tests_fehlgeschlagen','sicherheit_punkte','tote_funktionen','laufzeit_ms','groesste_funktion')}) for b,m in d['bereiche'].items()]"
echo $LAUF > $A/${PREFIX}LAUF
