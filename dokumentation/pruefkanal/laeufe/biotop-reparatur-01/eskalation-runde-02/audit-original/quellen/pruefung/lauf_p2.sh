#!/bin/bash
# Phase-2-Lauf vom Ausgang Lauf 9 Gen 6 (/root/uebungswerk-p2): anlegen, einlegen, kartieren, Verfassung, Verträge, Gen 0, Maß, Generationen 1..N
A=$1; N=$2; export PYTHONPATH=/root/biotop BIOTOP_AUFTRAG_LAUF_AB=11 BIOTOP_AUFTRAG_BUDGET_EUR=10; cd /root/biotop
python3 -m biotop lauf anlegen --budget 8 > $A/${PREFIX}0-lauf-anlegen.txt
LAUF=$(python3 -c "import json;print(json.load(open('$A/${PREFIX}0-lauf-anlegen.txt'))['lauf'])"); echo "LAUF=$LAUF"
python3 -m biotop einlegen $LAUF lagerhaus-p2-$LAUF /root/uebungswerk-p2 > $A/${PREFIX}1-aufnahme.json
python3 -c "import json;d=json.load(open('$A/${PREFIX}1-aufnahme.json'));print('Aufnahme:',d['status'],d['erster_testlauf']['bestanden'],'von',d['erster_testlauf']['gesamt'],d['ethik']['urteil'],'werk_id',d['werk_id'])"
python3 -m biotop kartieren $LAUF > $A/${PREFIX}2-landkarte.json; tr -d '\n ' < $A/${PREFIX}2-landkarte.json; echo
python3 -m biotop verfassung $LAUF /root/biotop/verfassungen/lagerhaus.md /root/biotop/verfassungen/lagerhaus.regeln.json --von "Chat-Claude (Anhang A, Masterprompt v3), eingelegt durch Hermes" > $A/${PREFIX}3-verfassung.json
python3 -m biotop vertraege $LAUF /root/biotop/verfassungen/vertraege-lagerhaus --von "Hermes, abgeleitet aus Anhang A Satz 3–5 und Docstring-Verträgen" > $A/${PREFIX}4-vertraege.json; tr -d '\n ' < $A/${PREFIX}4-vertraege.json; echo
python3 -m biotop gen0 $LAUF --mutanten /root/versiegelt/MUTANTEN-phase2.json --ziel 16 > $A/${PREFIX}5-generation0.json 2> $A/${PREFIX}5-generation0.err
python3 -c "import json;d=json.load(open('$A/${PREFIX}5-generation0.json'));print('Gen0: vorher',d['gefangen_vorher'],'nachher',d['gefangen_nachher'],'von',d['mutanten'],'erreicht',d['erreicht'],'neue Tests',d['neue_tests'],'blind nachher',d['blind_nachher'])"
python3 -m biotop mass $LAUF --bestaetigt-von "Masterprompt v3 Abschnitt 3.5 (Philipp, 19.09.2026); Tauschregel Anhang A Satz 2; groesste_funktion absolut 60" > $A/${PREFIX}6-mass.json
python3 -c "import json;d=json.load(open('$A/${PREFIX}6-mass.json'));print('Ausgang Schnappschuss',d['schnappschuss']['tag'],d['schnappschuss']['pruefsumme'][:16]); [print(' ',b,{k:m[k] for k in ('tests_bestanden','tests_fehlgeschlagen','sicherheit_punkte','tote_funktionen','laufzeit_ms','groesste_funktion')}) for b,m in d['bereiche'].items()]"
PREFIX=${PREFIX}g /root/biotop/pruefung/generationen.sh $LAUF 1 $N $A
