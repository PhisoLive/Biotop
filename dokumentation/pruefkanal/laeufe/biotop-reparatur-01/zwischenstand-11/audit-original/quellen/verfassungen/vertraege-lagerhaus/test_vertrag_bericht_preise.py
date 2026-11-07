"""Expliziter Vertrag an der Grenze bericht → preise (Anhang A Satz 3–5; abgeleitet aus lagerhaus/preise/__init__.py).
Konsument: bericht (liest Katalog.enthaelt, holen, grundpreis, runde_cent). Lieferant: preise.
Zusicherungen: preis_fuer ≥ 0 auf Cent gerundet; Staffel ab Mindestmenge einschließlich; rabatt_anwenden ≥ 0,
nie über summe, auf Cent gerundet; keine negativen Rabatte; runde_cent kaufmännisch."""
import pytest
from lagerhaus.preise import Artikel, Katalog, Rabattregel, Staffel, UnbekannterArtikel, rabatt_anwenden, rabatt_betrag, runde_cent


def test_schnittstelle_katalog():
    k = Katalog()
    for name in ("aufnehmen", "entfernen", "holen", "enthaelt", "alle", "preis_fuer", "anzahl"):
        assert callable(getattr(k, name))
    with pytest.raises(UnbekannterArtikel):
        k.holen("nix")


def test_preis_fuer_cent_gerundet_nie_negativ():
    k = Katalog(); k.aufnehmen(Artikel("A", "a", 0.333))
    p = k.preis_fuer("A", 3)
    assert p == round(p, 2) and p >= 0


def test_staffel_inklusiv():
    k = Katalog(); k.aufnehmen(Artikel("A", "a", 1.0, [Staffel(10, 0.5)]))
    assert k.preis_fuer("A", 10) == 5.0
    assert k.preis_fuer("A", 9) == 9.0


def test_rabatt_nie_negativ_nie_ueber_summe():
    r = Rabattregel("x", "summe > 0", "summe * 3")
    assert rabatt_betrag(r, 10.0, 1, 10.0) == 10.0
    r2 = Rabattregel("neg", "summe > 0", "0 - 5")
    assert rabatt_betrag(r2, 10.0, 1, 10.0) == 0.0
    assert rabatt_anwenden(10.0, [r, r2], 1, 10.0) >= 0.0


def test_runde_cent_kaufmaennisch():
    assert runde_cent(2.675) == 2.68
    assert runde_cent(1.005) == 1.01
