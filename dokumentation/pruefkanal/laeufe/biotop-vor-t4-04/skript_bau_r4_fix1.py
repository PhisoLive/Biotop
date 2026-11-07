"""Behebungsrunde 4 vor T4 — Nachbesserung nach TEILLAUF-1 (2 von 28 rot):
1. verhaltensvergleich: instabile Funktionen als 'modul:funktion' (funktion_von liefert nur den Namen — der Vergleich mit
   dem Nenner `alle` ('modul:funktion') griff nie; test_r414 rot: „2 von 2“ statt „1 von 2“).
2. tests/test_vor_t4_04.py, E4: der eigene Test des Kandidaten muss nach den geltenden Regeln ein gültiger Behebungstest
   sein (Norm-Regel 3.7: Verfassungsbezug), sonst kommt er gar nicht in den Testbestand und E4 prüft nichts (TEILLAUF-1:
   `eigene_tests_ausgeschlossen` leer, abgelehnt aus anderem Grund). Der Kandidat bricht jetzt NUR Tab (K_TAB), die
   Soll-Tests decken alle übrigen Formvarianten — so entscheidet allein, ob der eigene Tab-Test decken darf. Gegenprobe:
   derselbe Test in der Vorgeneration → überlebt.
Alles-oder-nichts.
"""
import py_compile
from pathlib import Path

V = Path('/root/biotop/biotop/organe/verhaltensvergleich.py')
T = Path('/root/biotop/tests/test_vor_t4_04.py')
v, t = V.read_text(), T.read_text()
ops_v = [("""    instabil_fn = {mf for k in instabil if (mf := funktion_von(k))}""",
          """    instabil_fn = {f"{mf[0]}:{mf[1]}" for k in instabil if (mf := _modul_funktion(k))}""")]
alt_e4 = t[t.index('def test_e4_kandidat_mit_rueckschritt_und_eigenem_test_wird_abgelehnt('):t.index('def test_e4_eigene_tests_am_organ(')]
neu_e4 = '''K_TAB = '    if "\\\\t" in text:\\n        raise ValueError("Tab")\\n    return "_".join(text.split())\\n'
SOLL_OHNE_TAB = {**SOLL, "lf": ("a\\nb", "a_b"), "crlf": ("a\\r\\nb", "a_b"), "nbsp": ("a\\u00a0b", "a_b"),
                 "doppelt": ("a  b", "a_b")}
EIGENER_TEST = ("import pytest\\nfrom probewerk.werk.kern import normieren\\n\\n\\n"
                "def test_werk_rueckschritt_tab():\\n    \\"\\"\\"Verfassung Satz 2: Steuerzeichen werden abgewiesen.\\"\\"\\"\\n"
                "    with pytest.raises(ValueError):\\n        normieren('a\\\\tb')\\n    assert normieren('a b') == 'a_b'\\n")
VERFASSUNG = {"text": "1. Zweck: Prüfwerk ohne Betriebszweck.\\n2. Sicherheit: Eingaben sind Daten.\\n", "regeln": {}}


def test_e4_kandidat_mit_rueckschritt_und_eigenem_test_wird_abgelehnt(tmp_path, monkeypatch):
    """Entscheidung 4: der Kandidat bricht Tab (wirft ValueError) und bringt einen eigenen Test mit, der genau diesen
    Rückschritt zusichert — gültig nach der Norm-Regel (Verweis auf Verfassung Satz 2), er kommt also in den
    Testbestand, fällt an der Vorgeneration und besteht am Kandidaten. Er deckt trotzdem nicht: abgelehnt, alle
    ungedeckten Abweichungen tragen `tab`, der Test steht als ausgeschlossen im Urteil."""
    monkeypatch.setattr(aegis.verfassung, "lesen", lambda *a: VERFASSUNG)
    neu = QUELLE.replace(ALT_NORMIEREN, K_TAB)
    diff = R3._diff(QUELLE, neu, tests={"tests/test_werk_eigen.py": EIGENER_TEST})
    u, v = R3._pruefen(tmp_path, monkeypatch, diff, nische="sicher", werk_extra=_norm_tests(SOLL_OHNE_TAB))
    assert u["status"] == "abgelehnt" and u["grund"].startswith("Verhaltensvergleich:"), u["grund"]
    assert any("test_werk_rueckschritt_tab" in t for t in v.get("eigene_tests_ausgeschlossen") or []), v.get("eigene_tests_ausgeschlossen")
    auf = v.get("ungedeckt_aufschluesselung") or {}
    assert auf and all("tab" in s.split(" | ")[1].split("+") for s in auf), auf


def test_e4_gegenprobe_derselbe_test_in_der_vorgeneration_deckt(tmp_path, monkeypatch):
    """Gegenprobe: derselbe Test liegt schon in der Vorgeneration (dort rot) — er deckt die Tab-Abweichungen, der
    Kandidat überlebt. Nur die Herkunft des Tests unterscheidet die beiden Fälle."""
    monkeypatch.setattr(aegis.verfassung, "lesen", lambda *a: VERFASSUNG)
    neu = QUELLE.replace(ALT_NORMIEREN, K_TAB)
    extra = {**_norm_tests(SOLL_OHNE_TAB), "tests/test_werk_eigen.py": EIGENER_TEST}
    u, v = R3._pruefen(tmp_path, monkeypatch, R3._diff(QUELLE, neu), nische="sicher", werk_extra=extra)
    assert u["status"] == "ueberlebt" and v["ungedeckt"] == [], (u["grund"], v.get("ungedeckt_aufschluesselung"))
    assert not (v.get("eigene_tests_ausgeschlossen") or []), v


'''
fehl = [a[:60] for a, b in ops_v if v.count(a) != 1] + ([] if alt_e4 else ['E4-Block'])
if fehl:
    raise SystemExit(f'Anker fehlen, nichts geschrieben: {fehl}')
for a, b in ops_v:
    v = v.replace(a, b)
t = t.replace(alt_e4, neu_e4)
V.write_text(v)
T.write_text(t)
py_compile.compile(str(V), doraise=True)
py_compile.compile(str(T), doraise=True)
print('Nachbesserung 1: verhaltensvergleich 1 Ersetzung, E4-Block ersetzt, kompiliert')
