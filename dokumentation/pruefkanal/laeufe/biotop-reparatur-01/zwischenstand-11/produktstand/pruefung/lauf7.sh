#!/bin/bash
# Lauf 7: Ausgang = Lauf-2-Ausgang (/root/uebungswerk, Commit 058b33e), Verfassung Anhang A, Maß F2, dann Generationen 1..N
A=$1; N=$2; export PYTHONPATH=/root/biotop; cd /root/biotop
python3 -m biotop lauf anlegen --budget 2 > $A/${PREFIX}0-lauf-anlegen.txt
LAUF=$(python3 -c "import json;print(json.load(open('$A/${PREFIX}0-lauf-anlegen.txt'))['lauf'])")
echo "LAUF=$LAUF"
python3 -m biotop einlegen $LAUF lagerhaus-nachlauf$PREFIX /root/uebungswerk > $A/${PREFIX}1-aufnahme.json
python3 -c "import json;d=json.load(open('$A/${PREFIX}1-aufnahme.json'));print('Aufnahme:',d['status'],d['erster_testlauf']['bestanden'],'von',d['erster_testlauf']['gesamt'],d['ethik']['urteil'],'werk_id',d['werk_id'])"
python3 -m biotop kartieren $LAUF > $A/${PREFIX}2-landkarte.json; cat $A/${PREFIX}2-landkarte.json | tr -d '\n '; echo
python3 -m biotop verfassung $LAUF /root/biotop/verfassungen/lagerhaus.md /root/biotop/verfassungen/lagerhaus.regeln.json --von "Chat-Claude (Anhang A, Masterprompt v2), eingelegt durch Hermes" > $A/${PREFIX}3-verfassung.json
python3 -m biotop mass $LAUF --bestaetigt-von "Masterprompt v2 Abschnitt 3.5 (Philipp, 19.09.2026); Tauschregel Anhang A Satz 2" > $A/${PREFIX}4-mass.json
python3 -c "import json;d=json.load(open('$A/${PREFIX}4-mass.json'));print('Ausgang F1',d['kernmass'],'Schnappschuss',d['schnappschuss']['tag'],d['schnappschuss']['pruefsumme'][:16]); [print(' ',b,{k:m[k] for k in ('tests_bestanden','tests_fehlgeschlagen','sicherheit_punkte','tote_funktionen','laufzeit_ms','groesste_funktion')}) for b,m in d['bereiche'].items()]"
/root/biotop/pruefung/generationen.sh $LAUF 1 $N $A
