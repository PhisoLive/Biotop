"""Expliziter Vertrag an der Grenze filtern → lesen (Verfassung logmuehle Satz 3/4; abgeleitet aus logmuehle/lesen/__init__.py).
Konsument: filtern (liest Eintrag.zeit, .status, .pfad_ohne_abfrage, .pfad). Lieferant: lesen.
Zusicherungen: Eintrag ist unveränderlich; zeit zeitzonenbewusst in UTC; groesse ≥ 0 ('-' = 0); zeile_lesen wirft LeseFehler,
verändert die Eingabe nicht; zeilen_lesen zählt unlesbare Zeilen (unlesbar) statt sie zu verschlucken."""
import pytest
from datetime import timezone
from logmuehle.lesen import Eintrag, LeseFehler, zeile_lesen, zeilen_lesen

Z = 'h - anna [19/Sep/2026:10:15:32 +0200] "GET /a?x=1 HTTP/1.1" 200 5'


def test_schnittstelle_eintrag():
    e = zeile_lesen(Z)
    for f in ("host", "nutzer", "zeit", "methode", "pfad", "status", "groesse", "pfad_ohne_abfrage"):
        assert hasattr(e, f)
    assert e.pfad_ohne_abfrage == "/a"


def test_zeit_utc_bewusst():
    e = zeile_lesen(Z)
    assert e.zeit.tzinfo is not None and e.zeit.utcoffset().total_seconds() == 0
    assert e.zeit.hour == 8


def test_groesse_nie_negativ_strich_null():
    assert zeile_lesen('h - - [19/Sep/2026:10:15:32 +0000] "HEAD / HTTP/1.1" 304 -').groesse == 0
    assert zeile_lesen(Z).groesse >= 0


def test_unveraenderlich_und_lesefehler():
    e = zeile_lesen(Z)
    with pytest.raises(Exception):
        e.status = 1
    with pytest.raises(LeseFehler):
        zeile_lesen("murks")


def test_unlesbare_gezaehlt_nicht_verschluckt():
    r = zeilen_lesen([Z, "murks", Z])
    assert len(r.eintraege) == 2 and r.unlesbar == 1
