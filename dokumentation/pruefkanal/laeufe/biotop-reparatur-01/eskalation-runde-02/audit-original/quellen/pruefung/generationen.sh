#!/bin/bash
# Generationen laufen lassen mit Freigabe unter Vollmacht (Abschnitt 4 F2), bis Abbruch oder BIS erreicht.
LAUF=$1; VON=$2; BIS=$3; A=$4; export PYTHONPATH=/root/biotop BIOTOP_AUFTRAG_LAUF_AB=${BIOTOP_AUFTRAG_LAUF_AB:-14} BIOTOP_AUFTRAG_BUDGET_EUR=${BIOTOP_AUFTRAG_BUDGET_EUR:-15}; cd /root/biotop
for g in $(seq $VON $BIS); do
  offen=$(python3 -c "
import sys; sys.path.insert(0,'/root/biotop')
from biotop.kern.datenbank import verbinden
z=verbinden().execute(\"SELECT nummer FROM generationen WHERE lauf_id=$LAUF AND status='vorgelegt'\").fetchone(); print(z[0] if z else '')")
  if [ -n "$offen" ]; then
    grund=$(python3 -c "
import sys,json; sys.path.insert(0,'/root/biotop')
from biotop.kern.datenbank import verbinden, lj
z=verbinden().execute(\"SELECT masse, grund FROM generationen WHERE lauf_id=$LAUF AND nummer=$offen\").fetchone(); m=lj(z['masse']) or {}
u=m.get('_urteil_f2') or {}; print('Generalprobe: '+z['grund'][:160]+' | Pareto schlechter: '+str(u.get('pareto_schlechter'))+' | Grenzen: '+str(u.get('grenzen_gerissen')))")
    python3 -m biotop freigabe $LAUF $offen frei --von "Hermes unter Vollmacht Abschnitt 4 (Masterprompt v4; Übungswerk, regeln.uebungswerk=true)" --grund "$grund" > $A/${PREFIX:-2}${offen}-gen${offen}-freigabe.json
    echo "Gen $offen freigegeben: $grund"
  fi
  echo "=== Generation $g ==="
  python3 -m biotop generation $LAUF > $A/${PREFIX:-2}$g-gen$g.json 2>$A/${PREFIX:-2}$g-gen$g.err; rc=$?
  cat $A/${PREFIX:-2}$g-gen$g.err
  python3 -c "
import json; d=json.load(open("$A/${PREFIX:-2}$g-gen$g.json")); print(d['status'], d['grund'][:250])
for b,ks in d['kandidaten'].items():
    if isinstance(ks,list): print(' ', b, [(k['kandidat'],k['status'],k['grund'][:100]) for k in ks])
gp=d['kandidaten'].get('_generalprobe'); print('  generalprobe:', {k:gp.get(k) for k in ('kern_basis','kern_kandidat','zuwachs','grenzen_gerissen')} if gp else None)
print('  kasse', d['kasse']['ausgegeben_eur'], d['kasse']['aufrufe'])" 2>/dev/null
  [ $rc -ne 0 ] && break
  # Sättigung (3.11): Lauf beendet sich selbst → Schleife endet; letzte vorgelegte Generation vorher freigeben
  st=$(python3 -c "
import sys; sys.path.insert(0,'/root/biotop')
from biotop.kern.datenbank import verbinden
print(verbinden().execute(\"SELECT status FROM laeufe WHERE id=$LAUF\").fetchone()[0])")
  if [ "$st" = "gesaettigt" ]; then echo "=== Lauf $LAUF GESÄTTIGT nach Generation $g ==="; break; fi
done
# Hängt noch eine Vorlage? Freigeben (Vollmacht), damit Entropie/Sättigung auch für die letzte Generation gemessen ist
offen=$(python3 -c "
import sys; sys.path.insert(0,'/root/biotop')
from biotop.kern.datenbank import verbinden
z=verbinden().execute(\"SELECT nummer FROM generationen WHERE lauf_id=$LAUF AND status='vorgelegt'\").fetchone(); print(z[0] if z else '')")
if [ -n "$offen" ]; then
  python3 -m biotop freigabe $LAUF $offen frei --von "Hermes unter Vollmacht Abschnitt 4 (Masterprompt v4; Übungswerk, regeln.uebungswerk=true)" --grund "Generalprobe bestanden (letzte Generation der Reihe)" > $A/${PREFIX:-2}${offen}-gen${offen}-freigabe.json
  echo "Gen $offen freigegeben (Ende)"; cat $A/${PREFIX:-2}${offen}-gen${offen}-freigabe.json | tr -d '\n' | cut -c1-300; echo
fi
