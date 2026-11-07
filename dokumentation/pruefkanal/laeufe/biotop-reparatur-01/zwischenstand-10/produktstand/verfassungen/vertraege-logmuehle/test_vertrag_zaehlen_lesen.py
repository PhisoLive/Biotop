"""Expliziter Vertrag an der Grenze zaehlen → lesen (Verfassung logmuehle Satz 3/4).
Konsument: zaehlen (liest status, groesse, pfad_ohne_abfrage). Lieferant: lesen.
Zusicherungen: status int in 100–599; groesse int ≥ 0; pfad_ohne_abfrage ohne '?'."""
import pytest
from logmuehle.lesen import LeseFehler, zeile_lesen


def test_status_bereich():
    assert 100 <= zeile_lesen('h - - [19/Sep/2026:10:15:32 +0000] "GET / HTTP/1.1" 599 1').status <= 599
    with pytest.raises(LeseFehler):
        zeile_lesen('h - - [19/Sep/2026:10:15:32 +0000] "GET / HTTP/1.1" 600 1')


def test_groesse_int_nicht_negativ_und_pfad_ohne_abfrage():
    e = zeile_lesen('h - - [19/Sep/2026:10:15:32 +0000] "GET /p?q=1&r=2 HTTP/1.1" 200 42')
    assert isinstance(e.groesse, int) and e.groesse >= 0
    assert "?" not in e.pfad_ohne_abfrage and e.pfad_ohne_abfrage == "/p"
