"""Expliziter Vertrag an der Grenze bericht → lager (Anhang A Satz 3–5; abgeleitet aus lagerhaus/lager/__init__.py, bestand.py).
Konsument: bericht (liest artikel(), bestand(), gesamtmenge(), journal.alle()). Lieferant: lager.
Zusicherungen: bestand() ≥ 0 jederzeit; verfuegbar() = bestand − reserviert; eingelöste Reservierung zählt nicht weiter;
entnehmen bucht ganz oder gar nicht; Journal fortlaufend nummeriert; artikel() sortiert, nur Bestand > 0."""
import pytest
from lagerhaus.lager import Buchung, Journal, Lager, NichtGenugBestand


def test_schnittstelle_vorhanden():
    l = Lager()
    for name in ("bestand", "reserviert", "verfuegbar", "artikel", "zugang", "entnehmen", "reservieren", "freigeben", "reservierung_einloesen", "inventur", "gesamtmenge"):
        assert callable(getattr(l, name))
    assert isinstance(l.journal, Journal)


def test_bestand_nie_negativ_entnahme_ganz_oder_gar_nicht():
    l = Lager(); l.zugang("A", 3)
    with pytest.raises(NichtGenugBestand):
        l.entnehmen("A", 4)
    assert l.bestand("A") == 3
    assert l.journal.anzahl() == 1


def test_verfuegbar_ist_bestand_minus_reserviert():
    l = Lager(); l.zugang("A", 10); l.reservieren("A", 4)
    assert l.verfuegbar("A") == l.bestand("A") - l.reserviert("A") == 6


def test_eingeloeste_reservierung_zaehlt_nicht_weiter():
    l = Lager(); l.zugang("A", 10); l.reservieren("A", 4); l.reservierung_einloesen("A", 4)
    assert l.reserviert("A") == 0
    assert l.bestand("A") == 6
    assert l.verfuegbar("A") == 6


def test_journal_fortlaufend_und_unveraenderlich():
    l = Lager(); l.zugang("A", 1); l.zugang("B", 2); l.entnehmen("A", 1)
    nummern = [b.nummer for b in l.journal.alle()]
    assert nummern == [1, 2, 3]
    b = l.journal.alle()[0]
    assert isinstance(b, Buchung)
    with pytest.raises(Exception):
        b.menge = 99  # frozen dataclass


def test_artikel_sortiert_nur_positiver_bestand():
    l = Lager(); l.zugang("B", 1); l.zugang("A", 1); l.zugang("C", 1); l.entnehmen("C", 1)
    assert l.artikel() == ["A", "B"]
