"""Nur lesend: Verdrahtungsbeleg Teillauf 3 auswerten (Register, tor4, Nachspiel, Stufen)."""
import json
import sys

p = sys.argv[1]
d = json.load(open(p))
print('datei', p)
print('schluessel', sorted(d))
print('organe', d.get('organe'), 'gerufen', d.get('gerufen'), 'nie_gerufen', d.get('nie_gerufen'))
print('register', d.get('register'))
print('nachspiel', json.dumps(d.get('nachspiel'), ensure_ascii=False)[:900])
print('tor4', json.dumps(d.get('tor4'), ensure_ascii=False)[:1500])
nm = d.get('nachmessungen') or []
print('nachmessungen', len(nm), 'stufen', sorted({str(n.get('stufe')) for n in nm}))
kanten = d.get('kanten') or []
print('kanten gesamt', len(kanten))
for k in kanten:
    if any(s in k for s in ('tor4', 'gegenzeugen', 'laufzeit_gepaart', 'laufzeit_einmal', 'rauschmessung', 'masseichung',
                             'eichproben.proben', 'aegis.pruefen', 'verhaltensvergleich.pruefen')):
        print('  ', k)
print('schritte', [(s.get('schritt'), s.get('rc')) for s in d.get('schritte') or []])
