"""Drahtwerk: kleinstes TypeScript-Werk, an dem ein ganzer Lauf jedes Organ erreicht.

Aufbau, mit Begründung je Teil (der Vorspann verlangt vier bestandene Eichproben und vier Gegenproben):
- src/beta/wert.ts   halb(x) zuerst, plus(a,b) zuletzt: halb ist die numerische Einparameterfunktion der
                     Normprobe; plus ist die letzte numerische Funktion, die die Nebenwirkungs- und die
                     Regressionsprobe in B beschädigen.
- src/alpha/liste.ts summen(werte: number[]) (Array-Rückgabe für den privaten Defekt der Nebenwirkungsprobe,
                     rein, ohne beta) und gesamt(werte) über beta.plus (Verbraucher für die Regressionsprobe).
                     Der Import aus beta macht alpha zum Vertragsverbraucher. `ungenutzt` ist toter Code, den
                     zwei Schwarmkandidaten gleich gut entfernen — Gleichstand, also Jury.
- tests/test_alpha.test.ts: summen([]) (Leereingang-Verbraucherzeuge der Vertragsprobe), zwei Tests, die der
                     private Defekt bricht, ein Test auf gesamt, den der Eingriff in B bricht. Damit sinkt alpha
                     in der Nebenwirkungsprobe von 2 auf 1 fallende Tests, während beta steigt.
- tests/test_beta.test.ts prüft plus und halb genau.
- tests/vertraege/test_vertrag_alpha_beta.test.ts expliziter Grenzvertrag (zählt zu beta).
- Referenzlast: last_alpha/last_beta mit Arbeit im Bereich einiger zehn Millisekunden (sonst sperrt die
  Rauschmessung, wie in T3 gemessen), beobachten() als Verhaltensraster.
- Mutantenplan: zwei Mutanten, die der vorhandene Bestand fängt — Generation 0 erreicht ihr Ziel ohne Testbau.
"""
from __future__ import annotations

import difflib
import json
from pathlib import Path

NAME = "drahtwerk"

LISTE = ("import { plus } from '../beta/wert.js';\n\n"
         "/** Erhöht jeden Wert um eins. */\nexport function summen(werte: number[]): number[] {\n"
         "  const aus: number[] = [];\n  for (const w of werte) {\n    aus.push(w + 1);\n  }\n  return aus;\n}\n\n"
         "/** Summe aller Werte. */\nexport function gesamt(werte: number[]): number {\n"
         "  let s = 0;\n  for (const w of werte) {\n    s = plus(s, w);\n  }\n  return s;\n}\n\n"
         "function ungenutzt(x: number): number {\n  return x * 3;\n}\n")

WERT = ("/** Halbiert eine Zahl. */\nexport function halb(x: number): number {\n  return x / 2;\n}\n\n"
        "/** Addiert zwei Zahlen. */\nexport function plus(a: number, b: number): number {\n  return a + b;\n}\n")

DATEIEN = {
    "package.json": json.dumps({"name": NAME, "version": "0.1.0", "private": True, "type": "module",
                                "description": "Prüfwerk ohne Betriebszweck für den Verdrahtungsnachweis"}, indent=2) + "\n",
    "README.md": "# drahtwerk\n\nKleines Prüfwerk ohne Betriebszweck: Zahlenlisten summieren.\n",
    "tsconfig.json": json.dumps({"compilerOptions": {"target": "ES2022", "module": "NodeNext", "moduleResolution": "NodeNext",
                                                     "strict": True, "skipLibCheck": True, "outDir": "dist", "rootDir": "src"},
                                 "include": ["src/**/*.ts"]}, indent=2) + "\n",
    "vitest.config.ts": ("import { defineConfig } from 'vitest/config';\n\nexport default defineConfig({\n"
                         "  cacheDir: '/tmp/vitest-cache',\n  test: { include: ['tests/**/*.test.ts'], pool: 'forks' },\n});\n"),
    "src/beta/wert.ts": WERT,
    "src/alpha/liste.ts": LISTE,
    "tests/test_alpha.test.ts": ("import { test, expect } from 'vitest';\nimport { summen, gesamt } from '../src/alpha/liste.js';\n\n"
                                 "test('test_alpha_leer', () => {\n  expect(summen([])).toEqual([]);\n});\n\n"
                                 "test('test_alpha_werte', () => {\n  expect(summen([1, 2])).toEqual([2, 3]);\n});\n\n"
                                 "test('test_alpha_drei', () => {\n  expect(summen([5])).toEqual([6]);\n});\n\n"
                                 "test('test_alpha_gesamt', () => {\n  expect(gesamt([1, 2])).toBe(3);\n});\n"),
    "tests/test_beta.test.ts": ("import { test, expect } from 'vitest';\nimport { plus, halb } from '../src/beta/wert.js';\n\n"
                                "test('test_beta_plus', () => {\n  expect(plus(2, 3)).toBe(5);\n});\n\n"
                                "test('test_beta_halb', () => {\n  expect(halb(8)).toBe(4);\n});\n"),
}

VERTRAG = ("import { test, expect } from 'vitest';\nimport { summen } from '../../src/alpha/liste.js';\n"
           "import { plus } from '../../src/beta/wert.js';\n\n"
           "test('test_vertrag_alpha_beta_plus_eins', () => {\n  expect(summen([4])).toEqual([plus(4, 1)]);\n});\n")

REFERENZLAST = """// Referenzlast drahtwerk (Kern, Messgerät) — Laufzeitlast je Bereich und Verhaltensraster.
import { summen, gesamt } from './dist/alpha/liste.js';
import { plus, halb } from './dist/beta/wert.js';

const WERTE = Array.from({ length: 5000 }, (_, i) => (i * 7) % 101);

export function last_alpha() {
  let s = 0;
  for (let r = 0; r < 400; r++) s += gesamt(summen(WERTE));
  return s;
}

export function last_beta() {
  let s = 0;
  for (let i = 0; i < 15000000; i++) s = plus(s, halb(i % 13));
  return s;
}

export function beobachten() {
  return { summen: summen([1, 2, 3]), leer: summen([]), gesamt: gesamt([1, 2, 3]), plus: plus(2, 3), halb: halb(9) };
}
"""

VERFASSUNG = """# Verfassung drahtwerk (Prüfwerk ohne Betriebszweck)

1. **Zweck:** Das Werk summiert Zahlenlisten; es dient nur dem Verdrahtungsnachweis des Biotops.
2. **Sicherheit:** Eingaben sind Daten; kein Code wird aus Eingaben ausgeführt.
3. **Korrektheit:** `summen` erhöht jeden Wert um genau eins; `gesamt` addiert über `plus`; `halb` halbiert exakt.
4. **Grenzen:** `alpha` verwendet `beta`; der Grenzvertrag steht in tests/vertraege.
5. **Tragender Pfad:** `alpha` → `beta`. `beta` ist der saubere Vergleichsbereich.
"""

REGELN = {"uebungswerk": True, "sprache": "TypeScript", "tragender_pfad": [["alpha", "beta"]],
          "tausch": {"laufzeit_faktor": 2.0, "laufzeit_faktor_bei_sicherheitsgewinn": 2.0, "sonst_faktor": 1.25,
                     "groesste_funktion_absolut": 60},
          "verbotene_muster": [".skip(", ".todo(", "eslint-disable", "@ts-ignore"]}

MUTANTEN = [
    {"datei": "src/beta/wert.ts", "zeile": 8, "art": "arithmetik", "beschreibung": "+ → -",
     "code": WERT.replace("return a + b;", "return a - b;")},
    {"datei": "src/alpha/liste.ts", "zeile": 7, "art": "zahlengrenze", "beschreibung": "1 → 2",
     "code": LISTE.replace("aus.push(w + 1);", "aus.push(w + 2);")},
]


def diff(rel: str, alt: str, neu: str) -> str:
    return "".join(difflib.unified_diff(alt.splitlines(True), neu.splitlines(True), f"a/{rel}", f"b/{rel}"))


def toter_code_entfernt(variante: int) -> str:
    """Zwei gleich gute Kandidaten: beide entfernen `ungenutzt` (Kernmaß +1), sie unterscheiden sich nur im Kommentar."""
    neu = LISTE.replace("\n\nfunction ungenutzt(x: number): number {\n  return x * 3;\n}\n", "\n")
    if variante == 2:
        neu = neu.replace("/** Summe aller Werte. */", "/** Summe aller Werte der Liste. */")
    return diff("src/alpha/liste.ts", LISTE, neu)


def anlegen(ziel: Path) -> dict:
    """Legt Werk, Vertragsverzeichnis, Referenzlast, Verfassung und Mutantenplan unter `ziel` an."""
    werk = ziel / "quelle"
    for rel, inhalt in DATEIEN.items():
        p = werk / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(inhalt)
    vertraege = ziel / "vertraege"
    vertraege.mkdir(parents=True, exist_ok=True)
    (vertraege / "test_vertrag_alpha_beta.test.ts").write_text(VERTRAG)
    ref = ziel / "referenzlast"
    ref.mkdir(parents=True, exist_ok=True)
    (ref / f"{NAME}.mjs").write_text(REFERENZLAST)
    (ziel / "VERFASSUNG.md").write_text(VERFASSUNG)
    (ziel / "VERFASSUNG.regeln.json").write_text(json.dumps(REGELN, ensure_ascii=False, indent=1))
    (ziel / "MUTANTEN.json").write_text(json.dumps(MUTANTEN, ensure_ascii=False, indent=1))
    return {"werk": werk, "vertraege": vertraege, "referenzlast": ref, "verfassung": ziel / "VERFASSUNG.md",
            "regeln": ziel / "VERFASSUNG.regeln.json", "mutanten": ziel / "MUTANTEN.json"}
