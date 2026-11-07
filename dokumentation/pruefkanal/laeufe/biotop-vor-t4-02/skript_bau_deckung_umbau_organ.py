"""Nachtrag zu deckung_umbau.py: Der Organteil brach ab (Anker für die zweite Löschung existierte nicht — der Bereich
[_muster_erfuellt, _testdatei_pfade) enthält die vorige deckung() schon). TS- und Python-Teil waren bereits geschrieben.
Hier nur das Organ; nichts wurde vom Organ geschrieben (O.write_text lief nicht)."""
from pathlib import Path

O = Path('/root/biotop/biotop/organe/verhaltensvergleich.py')
s = O.read_text()
assert '_muster_erfuellt' in s and s.count('def deckung(') == 1
a0 = s.index('def _muster_erfuellt(')
a1 = s.index('def _testdatei_pfade(')
neu_deckung = '''def deckung(abweichungen: list[str], aufrufe: list[dict], argumente: dict[str, str],
            neu: dict[str, str]) -> dict[str, list[str]]:
    """{abweichung: [test]} — Deckung JE ABWEICHUNG (Grundsatz 11, Entscheidung Chat-Claude 23.09.2026).

    Ein Test deckt eine Abweichung, wenn er an der Vorgeneration fällt und am Kandidaten besteht (das stellt der
    Aufrufer sicher: `aufrufe` stammen nur von solchen Tests, aufgezeichnet AM KANDIDATEN) und die abweichende Funktion
    mit DERSELBEN EINGABE gerufen und DASSELBE ERGEBNIS bekommen hat, das die Sonde am Kandidaten für diese Beobachtung
    sah — `argumente[k]` ist die Eingabe unmittelbar vor dem Aufruf des Musters (nach Mutation bzw. Rücksetzung),
    `neu[k]` das Ergebnis (kanonisch, auch Fehlerklasse). Damit hält der Test genau das neue Verhalten fest, das die
    Abweichung zeigt. Ein Zwischenspeicher, der nach einer Mutation das alte Ergebnis liefert, ist so nicht deckbar: ein
    frischer Aufruf mit der mutierten Eingabe bekommt am Kandidaten das richtige Ergebnis, nicht das veraltete.
    Bisher (Deckung je Funktion) deckte jeder Test, der `f(` enthielt, JEDE Abweichung von f."""
    je_test: dict[str, dict[str, set[tuple[str, str]]]] = {}
    for c in aufrufe or []:
        je_test.setdefault(c.get("test", ""), {}).setdefault(c.get("f", ""), set()).add((c.get("args"), c.get("erg")))
    out: dict[str, list[str]] = {}
    for k in abweichungen:
        mf = _modul_funktion(k)
        x, y = argumente.get(k), neu.get(k, _FEHLT)
        if not mf or x is None or y is _FEHLT:
            continue
        f = f"{mf[0]}:{mf[1]}"
        treffer = sorted(t for t, fs in je_test.items() if (x, y) in fs.get(f, set()))
        if treffer:
            out[k] = treffer
    return out


'''
s = s[:a0] + neu_deckung + s[a1:]


def ersetze(alt, neu):
    global s
    assert s.count(alt) == 1, (s.count(alt), alt[:100])
    s = s.replace(alt, neu)


ersetze('''        argumente = {**(neu.get("argumente") or {}), **(alt.get("argumente") or {})}
        decke = deckung(roh["abweichungen"], d.get("aufrufe") or [], argumente, a, n)''',
        '''        decke = deckung(roh["abweichungen"], d.get("aufrufe") or [], neu.get("argumente") or {}, n)''')
ersetze('''            "eingaben": {k: (alt.get("argumente") or {}).get(k.partition("@")[0]) for k in r["ungedeckt"][:10]},''',
        '''            "eingaben": {k: (neu.get("argumente") or {}).get(k) for k in r["ungedeckt"][:10]},''')
ersetze('''  Form) — bei @mutation und @nach_ruecksetzung zusätzlich im selben Aufrufmuster (dasselbe Objekt, an Ort und Stelle
  geändert, erneut gerufen). Beweis ist der aufgezeichnete Aufruf am Kandidaten, nicht der Quelltext des Tests:''',
        '''  Form) und dasselbe Ergebnis bekommt, das die Sonde am Kandidaten sah. Beweis ist der aufgezeichnete Aufruf am
  Kandidaten, nicht der Quelltext des Tests:''')
assert s.count('def deckung(') == 1 and '_muster_erfuellt' not in s
O.write_text(s)
print('Organ: Deckungsregel vereinheitlicht')
