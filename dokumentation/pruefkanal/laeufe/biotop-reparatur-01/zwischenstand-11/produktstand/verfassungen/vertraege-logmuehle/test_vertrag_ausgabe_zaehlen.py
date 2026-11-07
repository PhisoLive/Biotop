"""Expliziter Vertrag an der Grenze ausgabe → zaehlen (Verfassung logmuehle Satz 4/5; abgeleitet aus logmuehle/zaehlen/__init__.py).
Konsument: ausgabe (liest Zusammenfassung-Felder). Lieferant: zaehlen.
Zusicherungen: zusammenfassen ist rein; Zusammenfassung hat anzahl, unlesbar, bytes, status, top_pfade, p50_groesse,
p95_groesse, fehleranteil; Summe status = anzahl; top höchstens n, absteigend, Gleichstand alphabetisch;
perzentil nach nächstem Rang, leer → None; bytes ≥ 0."""
from logmuehle.lesen import zeile_lesen
from logmuehle.zaehlen import Zusammenfassung, perzentil, top, zusammenfassen


def _e(status=200, pfad="/a", g=10):
    return zeile_lesen(f'h - - [19/Sep/2026:10:00:00 +0000] "GET {pfad} HTTP/1.1" {status} {g}')


def test_felder_und_summen():
    e = [_e(), _e(404, "/b", 0), _e(500, "/c", 5)]
    z = zusammenfassen(e, unlesbar=1, top_n=2)
    assert isinstance(z, Zusammenfassung)
    for f in ("anzahl", "unlesbar", "bytes", "status", "top_pfade", "p50_groesse", "p95_groesse", "fehleranteil"):
        assert hasattr(z, f)
    assert sum(z.status.values()) == z.anzahl == 3 and z.bytes >= 0 and len(z.top_pfade) <= 2


def test_rein():
    e = [_e(), _e(404)]
    k = list(e)
    zusammenfassen(e)
    assert e == k


def test_top_und_perzentil():
    assert top({"b": 2, "a": 2, "c": 1}, 2) == [("a", 2), ("b", 2)]
    assert perzentil([15, 20, 35, 40, 50], 40) == 20.0
    assert perzentil([], 50) is None
