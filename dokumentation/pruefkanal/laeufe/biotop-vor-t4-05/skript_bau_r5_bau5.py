"""Behebungsrunde 5 — Umbau Teil 5 (alles oder nichts), nach TEILLAUF-1 (25 grün, 2 rot):
- Iterator-Kappe 50 → 1000 (Python und TypeScript gleich): der eigene Randfall-Korpus der Sonde (Zahl 100) erzeugte an
  einem linearen Generator 100 Elemente — Kappe gerissen, Enthaltung durch die Sonde selbst (TEILLAUF-1: K4[24],
  E8[exakt] zurückgestellt an probewerk.werk.kern:zahlen).
- „Objekt ohne erfassbare Daten“ nur bei der Standarddarstellung (object.__repr__); ein eingebetteter Iterator
  (__next__) ist unvollständig (Elemente nicht erfasst).
- TypeScript: private Felder nur an Felddeklarationen erkennen (#name; bzw. #name =), nicht an privaten Methoden."""
import sys
from pathlib import Path

R = Path(sys.argv[1] if len(sys.argv) > 1 else '/root/biotop')
AENDERUNGEN = {}


def ers(pfad, alt, neu):
    AENDERUNGEN.setdefault(pfad, []).append((alt, neu))


V = 'biotop/kern/py/verhalten.py'
ers(V, "KAPPE, RAND_KAPPE, FORM_KAPPE, ITER_KAPPE = 8, 16, 16, 50\n",
    "# Behebungsrunde 5: ITER_KAPPE 50 → 1000 (der eigene Randfall-Korpus erzeugte mit der Zahl 100 an linearen Generatoren\n"
    "# 100 Elemente — eine Enthaltung durch die Sonde selbst; gemessen in TEILLAUF-1)\n"
    "KAPPE, RAND_KAPPE, FORM_KAPPE, ITER_KAPPE = 8, 16, 16, 1000\n")
ers(V, r'''        roh = repr(x)
        if fehlend is not None and _ADRESSE.search(roh):
            fehlend.append(f'{type(x).__qualname__}: Objekt ohne erfassbare Daten (Darstellung nur mit Adresse)')
''', r'''        roh = repr(x)
        if fehlend is not None:
            if hasattr(x, '__next__'):
                fehlend.append(f'{type(x).__qualname__}: Iterator in der Beobachtung, Elemente nicht erfasst')
            elif type(x).__repr__ is object.__repr__:
                fehlend.append(f'{type(x).__qualname__}: Objekt ohne erfassbare Daten (nur Standarddarstellung)')
''')

T = 'biotop/kern/ts/verhalten-runner.mjs'
ers(T, "const ITER_KAPPE = 50;\n", "const ITER_KAPPE = 1000;       // Behebungsrunde 5: wie Python (vorher 50)\n")

K = 'biotop/kern/ts/kanon.mjs'
ers(K, r"    if (/(^|[\s;{}])(static\s+)?#[A-Za-z_$]/.test(src)) { fehlend.push(`${name}: private Felder (#…) nicht erfassbar`); break; }",
    r"    if (/(^|[\s;{}])(static\s+)?#[A-Za-z_$][\w$]*\s*(=|;|\r?\n)/.test(src)) { fehlend.push(`${name}: private Felder (#…) nicht erfassbar`); break; }")


def main():
    neu_inhalt, fehler = {}, []
    for pfad, liste in AENDERUNGEN.items():
        text = (R / pfad).read_text()
        for alt, neu in liste:
            n = text.count(alt)
            if n != 1:
                fehler.append(f'{pfad}: Anker {n}×: {alt[:90]!r}')
                continue
            text = text.replace(alt, neu)
        neu_inhalt[pfad] = text
    if fehler:
        print('ABBRUCH — nichts geschrieben:\n' + '\n'.join(fehler))
        sys.exit(2)
    for pfad, text in neu_inhalt.items():
        (R / pfad).write_text(text)
    print(f'geschrieben: {len(neu_inhalt)} Dateien, {sum(len(v) for v in AENDERUNGEN.values())} Ersetzungen')


if __name__ == '__main__':
    main()
