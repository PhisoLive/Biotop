"""Expliziter Vertrag an der Grenze ausgabe → filtern (Verfassung logmuehle Satz 3/4; abgeleitet aus logmuehle/filtern/__init__.py).
Konsument: ausgabe (befehl.py ruft nach_zeit, nach_status, nach_pfad, extern_filtern). Lieferant: filtern.
Zusicherungen: jeder Filter liefert eine neue Liste in Eingabereihenfolge, Eingabe unverändert; Statusfilter nimmt Codes und
Klassen ('4xx'); Pfadmuster sind Glob-Muster auf dem Pfad ohne Abfrage; ungültige Angaben → FilterFehler; Zeitfenster
[von, bis] ist an beiden Enden einschließlich (Satz 3)."""
import pytest
from datetime import datetime, timezone
from logmuehle.filtern import FilterFehler, nach_pfad, nach_status, nach_zeit
from logmuehle.lesen import zeile_lesen


def _e(h, m=0, status=200, pfad="/a"):
    return zeile_lesen(f'h - - [19/Sep/2026:{h:02d}:{m:02d}:00 +0000] "GET {pfad} HTTP/1.1" {status} 1')


def test_neue_liste_reihenfolge_eingabe_unveraendert():
    e = [_e(8), _e(9, 0, 404), _e(10, 0, 500, "/b")]
    k = list(e)
    r = nach_status(e, ["4xx", "5xx"])
    assert r is not e and [x.status for x in r] == [404, 500] and e == k


def test_status_codes_und_klassen_filterfehler():
    e = [_e(8), _e(9, 0, 404)]
    assert [x.status for x in nach_status(e, [404])] == [404]
    assert [x.status for x in nach_status(e, ["2xx"])] == [200]
    with pytest.raises(FilterFehler):
        nach_status(e, ["4x"])


def test_pfadmuster_glob_ohne_abfrage():
    e = [_e(8, 0, 200, "/api/x?y=1"), _e(9, 0, 200, "/s.js")]
    assert [x.pfad for x in nach_pfad(e, "/api/*")] == ["/api/x?y=1"]
    with pytest.raises(FilterFehler):
        nach_pfad(e, "")


def test_zeitfenster_beide_enden_einschliesslich():
    """Verfassung logmuehle Satz 3: Zeitfenster sind an beiden Enden einschließlich."""
    e = [_e(8), _e(9), _e(10)]
    von = datetime(2026, 9, 19, 8, tzinfo=timezone.utc); bis = datetime(2026, 9, 19, 10, tzinfo=timezone.utc)
    assert [x.zeit.hour for x in nach_zeit(e, von, None)] == [8, 9, 10]
    assert [x.zeit.hour for x in nach_zeit(e, von, bis)] == [8, 9, 10]
