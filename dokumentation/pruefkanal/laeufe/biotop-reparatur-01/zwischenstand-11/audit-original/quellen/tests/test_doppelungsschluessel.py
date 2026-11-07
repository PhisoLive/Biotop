"""Eigentests der bestehenden AST-Schlüsselregel: keine Dateipfad-Doppelung."""
import pytest

from biotop.organe.aegis import behauptung


@pytest.mark.parametrize("code,name,erwartet", [
    ("def test_a():\n    assert wert() == 1\n", "test_a", "wert|Eq:zahl"),
    ("def test_umbenannt():\n    assert wert() == 999\n", "test_umbenannt", "wert|Eq:zahl"),
    ("def test_a():\n    assert wert() == 'text'\n", "test_a", "wert|Eq:text"),
    ("def test_a():\n    assert wert() >= 1\n", "test_a", "wert|GtE:zahl"),
    ("def test_a():\n    assert anders() == 1\n", "test_a", "anders|Eq:zahl"),
    ("import pytest\ndef test_a():\n    with pytest.raises(ValueError):\n        wert()\n", "test_a", "wert|raises:ValueError"),
    ("def test_a():\n    assert wert()\n", "test_a", "wert|wahrheit"),
    ("def test_a():\n    xs.append(1)\n    assert wert() == 1\n", "test_a", "wert|Eq:zahl"),
])
def test_schluessel_beschreibt_ziel_und_zusicherung(code, name, erwartet):
    assert behauptung(code, name, "paket") == erwartet


def test_doppelung_ignoriert_namen_zeilen_und_zahlenwerte():
    a = "def test_eins():\n    assert wert() == 1\n"
    b = "# Anderer Pfad und andere Zeile\n\n\ndef test_zwei():\n    assert wert() == 42\n"
    assert behauptung(a, "test_eins") == behauptung(b, "test_zwei")
