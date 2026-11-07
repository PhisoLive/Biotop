"""Behebungsrunde 5 — Tests Teil 1 (alles oder nichts): drahtwerk (Stufe 2, Altlastenliste), test_verdrahtung (Register,
Tor-4-Schritt, Wirkung der Torzeile). Aufruf: python r5_tests1.py /root/biotop"""
import sys
from pathlib import Path

R = Path(sys.argv[1] if len(sys.argv) > 1 else '/root/biotop')
AENDERUNGEN = {}


def ers(pfad, alt, neu):
    AENDERUNGEN.setdefault(pfad, []).append((alt, neu))


DW = 'tests/drahtwerk.py'
ers(DW, '''VERFASSUNG = """# Verfassung drahtwerk (Prüfwerk ohne Betriebszweck)
''', '''# Behebungsrunde 5 (Entscheidung 6): ohne Vergleichslast Stufe 2 verweigert der Vorspann den Lauf. Dieselben Lasten mit
# zehnfacher Eingabegröße (alpha: 50.000 statt 5.000 Werte; beta: zehnmal so viele Aufrufe), Verhaltensraster wie Stufe 1.
REFERENZLAST_STUFE2 = REFERENZLAST.replace("// Referenzlast drahtwerk (Kern, Messgerät)",
                                           "// Referenzlast drahtwerk, STUFE 2 (Kern, Messgerät)") \\
    .replace("Array.from({ length: 5000 }", "Array.from({ length: 50000 }") \\
    .replace("i < 15000000", "i < 150000000")

# Behebungsrunde 5 (Entscheidung 5): Altlastenliste für das Tor-4-Skript. Eine Altlast in alpha (toter Code `ungenutzt`,
# den der Schwarm im Verdrahtungslauf entfernt): der Gegenzeuge liest die Quelldatei (Schwäche weg, wenn die Funktion
# fehlt); nicht verhaltensändernd — der Normalvergleich ist das Verhalten der Vorgeneration über den Verhaltensvergleich.
ALTLASTEN = {"werk": "drahtwerk", "quelle": "Verdrahtungsnachweis (gestellte Liste)", "bezugsgroesse": "1 Altlast",
             "altlasten": [{"kennung": "A1", "beschreibung": "toter Code: ungenutzt() in alpha/liste.ts",
                            "bereich": "alpha", "verhaltensaendernd": False, "unabhaengiger_test": None,
                            "gegenzeuge": {"datei": "tests/test_altlast_a1.test.ts", "code": (
                                "import { test, expect } from 'vitest';\\nimport fs from 'node:fs';\\n\\n"
                                "test('altlast_a1_toter_code_weg', () => {\\n"
                                "  expect(fs.readFileSync('src/alpha/liste.ts', 'utf8')).not.toContain('function ungenutzt');\\n"
                                "});\\n")}}]}

VERFASSUNG = """# Verfassung drahtwerk (Prüfwerk ohne Betriebszweck)
''')
ers(DW, '''    (ref / f"{NAME}.mjs").write_text(REFERENZLAST)
''', '''    (ref / f"{NAME}.mjs").write_text(REFERENZLAST)
    (ref / f"{NAME}.stufe2.mjs").write_text(REFERENZLAST_STUFE2)
    (ziel / "ALTLASTEN.json").write_text(json.dumps(ALTLASTEN, ensure_ascii=False, indent=1))
''')
ers(DW, '''            "regeln": ziel / "VERFASSUNG.regeln.json", "mutanten": ziel / "MUTANTEN.json"}
''', '''            "regeln": ziel / "VERFASSUNG.regeln.json", "mutanten": ziel / "MUTANTEN.json",
            "altlasten": ziel / "ALTLASTEN.json"}
''')

VT = 'tests/test_verdrahtung.py'
ers(VT, '''sys.path.insert(0, str(Path(__file__).parent))
import drahtwerk  # noqa: E402
''', '''sys.path.insert(0, str(Path(__file__).parent))
import drahtwerk  # noqa: E402
from biotop.kern import register  # noqa: E402
''')
ers(VT, '''def test_organliste_kommt_aus_dem_verzeichnis():
''', '''def test_register_meldet_eintrag_ohne_kante_und_falsche_phase():
    """Gegenprobe des Registers (Behebungsrunde 5, Entscheidung 5): ein Eintrag ohne Kante wird gemeldet; gerufen, aber
    von anderswo oder in einer anderen Phase, ebenso; die richtige Kante nicht."""
    e = ("tor4.ausfuehren", "biotop.__main__:main", "tor4", "Probe")
    assert register.fehlend(set(), (e,)) == ["tor4.ausfuehren ← biotop.__main__:main @ tor4"]
    assert register.fehlend({"tor4.ausfuehren ← biotop.__main__:main @ generation"}, (e,)) != []
    assert register.fehlend({"tor4.ausfuehren ← tests.x:y @ tor4"}, (e,)) != []
    assert register.fehlend({"tor4.ausfuehren ← biotop.__main__:main @ tor4"}, (e,)) == []


def test_register_nennt_torzeile_schwaechen_und_tor4():
    """Die Torzeile „Schwächen“ und das Tor-4-Skript stehen im Register (Review 04 Nr. 7: gebaut, nie gerufen)."""
    funktionen = {e[0] for e in register.VERLANGT}
    assert {"gegenzeugen.torzeile_schwaechen", "tor4.ausfuehren", "verhaltensvergleich.pruefen",
            "masseichung.anwenden", "eichung.laufzeit_einmal"} <= funktionen
    assert set(register.MODULE) >= {e[0].split(".")[0] for e in register.VERLANGT} - set(organe_finden(ORGANE))


def test_organliste_kommt_aus_dem_verzeichnis():
''')
ers(VT, '''    organe = organe_finden(ORGANE)
    module = {o: importlib.import_module(f"biotop.organe.{o}") for o in organe}
    kanten: set = set()
    phase: dict = {"schritt": None}
    gerufen = aufzeichnen(module, monkeypatch, kanten, phase)
''', '''    organe = organe_finden(ORGANE)
    module = {o: importlib.import_module(f"biotop.organe.{o}") for o in organe}
    # Behebungsrunde 5 (Entscheidung 5): auch die Kernmodule des Registers aufzeichnen (Torzeilen, Tor-4-Skript)
    module.update({k: importlib.import_module(m) for k, m in register.MODULE.items()})
    kanten: set = set()
    phase: dict = {"schritt": None}
    gerufen = aufzeichnen(module, monkeypatch, kanten, phase)
''')
ers(VT, '''    phase["schritt"] = "freigabe"
    rc = cli.main(["freigabe", "1", "1", "frei", "--von", "Verdrahtungsnachweis", "--grund", "Nachspiel"])
    capsys.readouterr()
    assert rc == 0
''', '''    phase["schritt"] = "freigabe"
    rc = cli.main(["freigabe", "1", "1", "frei", "--von", "Verdrahtungsnachweis", "--grund", "Nachspiel"])
    capsys.readouterr()
    assert rc == 0
    # Behebungsrunde 5 (Entscheidung 5): das Tor-4-Skript über die Befehlszeile — es ruft die Torzeile „Schwächen“.
    phase["schritt"] = "tor4"
    rc = cli.main(["tor4", "1", "--altlasten", str(d["altlasten"])])
    aus = capsys.readouterr()
    protokoll.append({"schritt": "tor4", "rc": rc, "stderr": aus.err[-1500:]})
    assert rc == 0, f"tor4 scheiterte: {aus.err[-3000:]}"
    tor4 = json.loads(aus.out)
''')
ers(VT, '''    fehlend = nie_gerufen(organe, gerufen)
''', '''    fehlend = nie_gerufen(organe, gerufen)
    register_fehlend = register.fehlend(kanten)
''')
ers(VT, '''    beleg = {"organe": len(organe), "gerufen": len(organe) - len(fehlend), "nie_gerufen": fehlend,
''', '''    beleg = {"organe": len(organe), "gerufen": len(organe) - len(fehlend), "nie_gerufen": fehlend,
             "register": {"eintraege": len(register.VERLANGT), "fehlend": register_fehlend},
             "tor4": {"zeile": tor4["schwaechen"]["zeile"], "behoben": tor4["schwaechen"]["behoben"],
                      "je_schwaeche": tor4["schwaechen"]["je_schwaeche"]},
''')
ers(VT, '''    assert fehlend == [], f"Organ existiert und wird im Lauf nie gerufen: {fehlend} (gerufen {len(organe) - len(fehlend)} von {len(organe)})"
''', '''    assert fehlend == [], f"Organ existiert und wird im Lauf nie gerufen: {fehlend} (gerufen {len(organe) - len(fehlend)} von {len(organe)})"
    # Behebungsrunde 5 (Entscheidung 5): jeder Registereintrag als Kante im echten Lauf (Aufrufer und Phase).
    assert register_fehlend == [], f"Register: verlangt, aber im Lauf nicht so gerufen: {register_fehlend}"
    # Wirkung der Torzeile, nicht nur Aufruf: die Altlast A1 (toter Code) ist nach der Generation weg und das Verhalten
    # der Vorgeneration unverändert (Verhaltensvergleich des angenommenen Kandidaten) — beide Prüfungen gemessen.
    a1 = tor4["schwaechen"]["je_schwaeche"]["A1"]
    assert a1["schwaeche_weg"] is True and a1["normal_unveraendert"] is True and tor4["schwaechen"]["behoben"] == ["A1"], a1
''')


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
