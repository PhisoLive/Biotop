"""R6-1 durch den Laufweg (aegis.pruefen, echte Kammer biotop-kammer:1, gestellt nur Modell und Laufzeit — derselbe
Ablauf wie tests/test_vor_t4_03.py::_pruefen). Kandidat: die richtige Behebung von normieren („ “ → „_“) mit einem Soll-Test
je Formvariante — die H1-Gegenprobe der Runde 4, die an 43b8fad und 0c2f058 überlebt. Dazu im selben Modul eine
UNVERÄNDERTE Funktion puffer(), die ein io.StringIO liefert (Iterator-Objekt: schwer erfassbar). Der Kandidat berührt
puffer nicht.
ROT an 0c2f058 (erwartet): zurückgestellt — „Verhaltensvergleich enthält sich … unvollständig erfasst (…puffer…)“.
Soll: überlebt; puffer als Enthaltung gezählt. Gegenprobe (grün): dasselbe ohne puffer — überlebt.
Nur ausführen, wenn kein Job der Runde läuft (pgrep -f job_kette leer)."""
import sys

import pytest

sys.path.insert(0, "/root/biotop")
sys.path.insert(0, "/root/biotop/tests")
import test_vor_t4_03 as R3  # noqa: E402

ALT = '    return " ".join(text.split())\n'
NEU = '    return "_".join(text.split())\n'
PUFFER = ('\n\nimport io  # noqa: E402\n\n\ndef puffer(text: str):\n'
          '    """Text als Datei-Objekt (vom Kandidaten nicht verändert)."""\n    return io.StringIO(text)\n')
SOLL = {"gewoehnlich": ("a b", "a_b"), "rand": (" a b ", "a_b"), "gross": ("A B", "A_B"),
        "lang": ("x " * 25, "_".join(["x"] * 25)), "zahlform": ("a 01 2.50", "a_01_2.50"), "nichtascii": ("Ä ö", "Ä_ö"),
        "tab": ("a\tb", "a_b"), "lf": ("a\nb", "a_b"), "crlf": ("a\r\nb", "a_b"), "nbsp": ("a\u00a0b", "a_b"),
        "doppelt": ("a  b", "a_b")}


def _tests():
    return {f"tests/test_werk_normieren_{n}.py": R3.TEST_NORMIEREN.format(name=n, eingabe=e, erwartet=x)
            for n, (e, x) in SOLL.items()}


@pytest.mark.parametrize("mit_puffer", [True, False])
def test_r6_1_laufweg_schwer_erfassbares_objekt_stellt_nicht_jeden_kandidaten_zurueck(tmp_path, monkeypatch, mit_puffer):
    q = R3.QUELLE + (PUFFER if mit_puffer else "")
    monkeypatch.setattr(R3, "QUELLE", q)
    u, v = R3._pruefen(tmp_path, monkeypatch, R3._diff(q, q.replace(ALT, NEU)), nische="sicher", werk_extra=_tests())
    print("\n@@", mit_puffer, u["status"], "|", str(u["grund"])[:300], "| unvollstaendig:", v.get("unvollstaendig"))
    assert u["status"] == "ueberlebt", u["grund"]
    if mit_puffer:
        assert "probewerk.werk.kern:puffer" in (v.get("enthaltungen") or {}), v.get("enthaltungen")
