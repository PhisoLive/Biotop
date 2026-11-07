"""Stichprobendauer der Bereichslast eingang an Stufe 2 bei 60, 240 und 480 Wiederholungen (Hinweis Philipp 24.09.:
„bis eingang nicht mehr sperrt“ richtet die Last nach dem Ergebnis; nur die Dauer zeigt, ob 240 nach Maß gewählt ist).
Quelle: STUFE2-EICHUNG.jsonl (je Rauschmessung die fünf laufzeit_ms-Werte jedes Bereichs; ein Wert = Median aus
5 Messdurchläufen der Bereichslast in einem Kammerlauf). Zum Vergleich: die übrigen Bereiche (unverändert) und Stufe 1
(t3.db, Tabelle eichung der Läufe 37/38, nur gelesen mit mode=ro). Nur lesen und rechnen."""
import collections
import json
import sqlite3
import statistics
from pathlib import Path

A = Path('/root/biotop-vor-t4-05/proben')
zs = [json.loads(l) for l in (A / 'STUFE2-EICHUNG.jsonl').read_text().splitlines()]
print('Beispiel werte eingang:', zs[0]['werte'].get('eingang'), '| Schlüssel:', sorted(zs[0]))
je = collections.defaultdict(list)
for z in zs:
    je[z['variante']].append(z)


def zahl(xs):
    xs = [float(x) for x in xs]
    return (f"Median {statistics.median(xs):.1f} ms, {min(xs):.1f} … {max(xs):.1f} ms (n = {len(xs)})")


aus = {}
for v, rs in je.items():
    werte = [x for r in rs for x in (r['werte'].get('eingang') or [])]
    med_je = [statistics.median(r['werte']['eingang']) for r in rs if r['werte'].get('eingang')]
    spann = [(max(r['werte']['eingang']) - min(r['werte']['eingang'])) / statistics.median(r['werte']['eingang'])
             for r in rs if r['werte'].get('eingang')]
    sperren = sum(1 for r in rs if 'eingang' in r['gesperrt'])
    aus[v] = {'werte': werte, 'median_je_messung': med_je, 'spannweite_rel': spann, 'sperren': sperren, 'n': len(rs)}
    print(f"eingang {v:8}: Einzelwerte {zahl(werte)} | Median je Rauschmessung {min(med_je):.1f} … {max(med_je):.1f} ms"
          f" | relative Spannweite je Messung {min(spann):.2f} … {max(spann):.2f} | Sperren {sperren} von {len(rs)}")
print()
for b in ('bericht', 'planung', 'tarife', 'zahlen'):
    werte = [x for r in je['W60_ist'] for x in (r['werte'].get(b) or [])]
    spann = [(max(r['werte'][b]) - min(r['werte'][b])) / statistics.median(r['werte'][b]) for r in je['W60_ist'] if r['werte'].get(b)]
    sperren = sum(1 for rs in je.values() for r in rs if b in r['gesperrt'])
    print(f"{b:8} (Stufe 2, unverändert): Einzelwerte {zahl(werte)} | relative Spannweite je Messung "
          f"{min(spann):.2f} … {max(spann):.2f} | Sperren {sperren} von {sum(len(rs) for rs in je.values())}")
print()
con = sqlite3.connect('file:/root/biotop-t3/schnappschuss-abschluss3/t3.db?mode=ro', uri=True)
for lauf, b, med, werte in con.execute("SELECT lauf_id, bereich, median, werte FROM eichung WHERE lauf_id IN (37,38) "
                                       "ORDER BY bereich, lauf_id"):
    print(f"Stufe 1, Lauf {lauf}, {b:8}: Median {med} ms, Werte {werte}")
con.close()
(A / 'STUFE2-EINGANG-DAUER.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1))
