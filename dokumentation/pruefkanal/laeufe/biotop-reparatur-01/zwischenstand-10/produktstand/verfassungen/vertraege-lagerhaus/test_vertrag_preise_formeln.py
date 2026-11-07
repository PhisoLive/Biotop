"""Expliziter Vertrag an der Grenze preise → formeln (Anhang A Satz 4; abgeleitet aus lagerhaus/formeln/__init__.py).
Konsument: preise (rabatt.py ruft auswerten). Lieferant: formeln.
Zusicherungen: auswerten(formel, menge, preis, summe) -> float | bool; unbekannte Namen → FormelFehler;
keine Nebenwirkungen; Vergleiche liefern bool, Rechnungen float; min/max/abs/round erlaubt."""
import inspect
import pytest
from lagerhaus.formeln import FormelFehler, auswerten


def test_signatur_auswerten_vier_parameter():
    p = list(inspect.signature(auswerten).parameters)
    assert p == ["formel", "menge", "preis", "summe"]


def test_rechnung_liefert_float():
    assert auswerten("summe * 0.05", 3, 10.0, 30.0) == pytest.approx(1.5)
    assert isinstance(auswerten("summe * 0.05", 3, 10.0, 30.0), float)


def test_vergleich_liefert_bool():
    assert auswerten("menge >= 10", 10, 1.0, 10.0) is True
    assert auswerten("menge >= 10", 9, 1.0, 9.0) is False


def test_unbekannter_name_formelfehler():
    with pytest.raises(FormelFehler):
        auswerten("rabatt * 2", 1, 1.0, 1.0)


def test_erlaubte_funktionen():
    assert auswerten("min(summe, 20)", 5, 10.0, 50.0) == 20.0
    assert auswerten("max(menge, 7)", 5, 10.0, 50.0) == 7.0
    assert auswerten("abs(0 - 3)", 1, 1.0, 1.0) == 3.0


def test_keine_nebenwirkung_auf_eingaben():
    menge, preis, summe = 3, 10.0, 30.0
    auswerten("summe + menge", menge, preis, summe)
    assert (menge, preis, summe) == (3, 10.0, 30.0)
