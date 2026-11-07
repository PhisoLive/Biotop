# Referenzlast für das Werk „logmuehle" — Teil des Messgeräts (Kern).
# Je Bereich eine Funktion last_<bereich>(), die eine feste Arbeit ausführt; beobachten() liefert ein festes Raster
# beobachtbarer Ausgaben (Äquivalenz-Beleg für Generation 0, F4).

import sys
sys.path.insert(0, "/werk")

_ZEILEN = None


def _zeilen(n=4000):
    global _ZEILEN
    if _ZEILEN is None:
        pfade = ["/", "/api/werke", "/api/werke?seite=2", "/static/app.js", "/api/lauf/13", "/gesund", "/api/kasse", "/bild.png"]
        status = [200, 200, 200, 304, 404, 500, 201, 403]
        _ZEILEN = [
            f'203.0.113.{i % 250} - {"anna" if i % 3 else "-"} [19/Sep/2026:{i % 24:02d}:{i % 60:02d}:{(i * 7) % 60:02d} +0200] '
            f'"GET {pfade[i % len(pfade)]} HTTP/1.1" {status[(i * 5) % len(status)]} {(i * 37) % 5000} "-" "curl/8.5"'
            for i in range(n)
        ] + ["murks"] * (n // 100)
    return _ZEILEN


def last_lesen():
    from logmuehle.lesen import zeilen_lesen
    for _ in range(3):
        zeilen_lesen(_zeilen())


def last_filtern():
    from datetime import datetime, timezone
    from logmuehle.filtern import nach_pfad, nach_status, nach_zeit
    from logmuehle.lesen import zeilen_lesen
    e = zeilen_lesen(_zeilen()).eintraege
    for _ in range(20):
        nach_pfad(nach_status(nach_zeit(e, datetime(2026, 9, 19, 6, tzinfo=timezone.utc), datetime(2026, 9, 19, 20, tzinfo=timezone.utc)), ["2xx", "404"]), "/api/*")


def last_zaehlen():
    from logmuehle.lesen import zeilen_lesen
    from logmuehle.zaehlen import zusammenfassen
    e = zeilen_lesen(_zeilen()).eintraege
    for _ in range(15):
        zusammenfassen(e, unlesbar=40, top_n=5)


def last_ausgabe():
    from logmuehle.ausgabe import als_csv, als_json, als_text
    from logmuehle.lesen import zeilen_lesen
    from logmuehle.zaehlen import zusammenfassen
    z = zusammenfassen(zeilen_lesen(_zeilen(800)).eintraege, unlesbar=8)
    for _ in range(60):
        als_text(z); als_csv(z); als_json(z)


def beobachten():
    """Festes Eingaberaster → beobachtbare Ausgaben (jede ein Wert)."""
    import io, json
    from datetime import datetime, timezone
    from logmuehle.lesen import LeseFehler, zeile_lesen, zeilen_lesen
    from logmuehle.lesen.eintrag import zeit_lesen
    from logmuehle.filtern import FilterFehler, nach_pfad, nach_status, nach_zeit, status_passt
    from logmuehle.zaehlen import je_pfad, je_status, perzentil, top, bytes_gesamt, zusammenfassen
    from logmuehle.ausgabe import als_csv, als_json, als_text, hauptprogramm
    out = []
    zeilen = [
        '203.0.113.7 - anna [19/Sep/2026:10:15:32 +0200] "GET /api/werke?seite=2 HTTP/1.1" 200 1532 "-" "curl/8.5"',
        'h - - [19/Sep/2026:10:15:32 +0000] "HEAD / HTTP/1.1" 304 -', 'h - - [19/Sep/2026:10:15:32 +0000] "GET / HTTP/1.0" 200 12',
        'h - - [31/Dec/2025:23:59:59 -0500] "POST /a HTTP/1.1" 201 1', 'h - - [29/Feb/2026:00:00:00 +0000] "GET /a HTTP/1.1" 200 1',
        'h - - [19/Sep/2026:10:15:32 +0000] "GET /a HTTP/1.1" 099 1', 'h - - [19/Sep/2026:10:15:32 +0000] "GET /a HTTP/1.1" 600 1',
        'h - - [19/Sep/2026:10:15:32 +0000] "GET /a" 200 1', "", "   ", "kaputt", 'h - - [19/Sxp/2026:10:15:32 +0000] "GET / HTTP/1.1" 200 1',
        'h - - [19/Sep/2026:10:15:32 +0000] "GET /x HTTP/1.1" 599 0 "ref" "agent"',
    ]
    for zl in zeilen:
        try:
            e = zeile_lesen(zl); out.append(("zeile", e.host, e.nutzer, e.zeit.isoformat(), e.methode, e.pfad, e.pfad_ohne_abfrage, e.status, e.groesse, e.referer, e.agent))
        except LeseFehler as ex:
            out.append(("zeile", "LeseFehler", str(ex)[:50]))
    for t in ("01/Jan/2026:00:30:00 -0500", "01/Jan/2026:00:30:00 +0000", "31/Dec/2026:23:59:59 +1400", "00/Jan/2026:00:00:00 +0000", "01/Jan/2026:24:00:00 +0000"):
        try:
            out.append(("zeit", t, zeit_lesen(t).isoformat()))
        except LeseFehler as ex:
            out.append(("zeit", t, "LeseFehler"))
    r = zeilen_lesen(zeilen); out.append(("zeilen_lesen", len(r.eintraege), r.unlesbar, r.gesamt, r.fehler))

    def z(stunde, minute=0, status=200, pfad="/a", groesse=10):
        return zeile_lesen(f'h - - [19/Sep/2026:{stunde:02d}:{minute:02d}:00 +0000] "GET {pfad} HTTP/1.1" {status} {groesse}')
    E = [z(8), z(9, 0, 404, "/b?x=1", 0), z(10, 0, 500, "/api/x", 50), z(11, 0, 200, "/static/app.js", 300), z(12, 0, 201, "/api/y", 100), z(12, 30, 200, "/api/y", 100), z(23, 59, 302, "/z", 7)]
    T = lambda h, m=0: datetime(2026, 9, 19, h, m, tzinfo=timezone.utc)
    for von, bis in ((None, None), (T(9), T(11, 30)), (T(10), None), (None, T(12)), (T(12), T(12)), (T(12, 30), T(12, 30)), (None, T(23, 59)), (T(8), T(8)), (T(0), T(7, 59))):
        try:
            out.append(("nach_zeit", von and von.isoformat(), bis and bis.isoformat(), [e.zeit.hour * 100 + e.zeit.minute for e in nach_zeit(E, von, bis)]))
        except FilterFehler:
            out.append(("nach_zeit", "FilterFehler"))
    try:
        nach_zeit(E, T(12), T(8)); out.append(("nach_zeit_verkehrt", "kein Fehler"))
    except FilterFehler:
        out.append(("nach_zeit_verkehrt", "FilterFehler"))
    for s in (200, 201, 299, 300, 404, 499, 500, 599):
        for a in ("200", 200, "2xx", "4xx", "5xx", "404", "abc", "44", "3xx"):
            try:
                out.append(("status_passt", s, a, status_passt(s, a)))
            except FilterFehler:
                out.append(("status_passt", s, a, "FilterFehler"))
    for ang in ([], ["4xx", "5xx"], [201], ["2xx"], ["3xx"], ["599"]):
        out.append(("nach_status", ang, [e.status for e in nach_status(E, ang)]))
    for m in ("*", "/api/*", "/b", "/api/?", "/static/*.js", "/nix", "*.js"):
        out.append(("nach_pfad", m, [e.pfad for e in nach_pfad(E, m)]))
    try:
        nach_pfad(E, ""); out.append(("nach_pfad_leer", "kein Fehler"))
    except FilterFehler:
        out.append(("nach_pfad_leer", "FilterFehler"))
    out.append(("je_status", je_status(E))); out.append(("je_pfad", je_pfad(E))); out.append(("bytes", bytes_gesamt(E), bytes_gesamt([])))
    for n in (0, 1, 2, 3, 10):
        out.append(("top", n, top({"/x": 3, "/a": 5, "/b": 5, "/c": 1, "/d": 3}, n)))
    for w in ([15, 20, 35, 40, 50], [1], [], [1, 2], [5, 1, 4, 2, 3, 6]):
        for p in (0, 1, 25, 40, 50, 75, 95, 99, 100):
            out.append(("perzentil", w, p, perzentil(w, p)))
    for p in (-1, 101):
        try:
            perzentil([1], p); out.append(("perzentil_grenze", p, "kein Fehler"))
        except ValueError:
            out.append(("perzentil_grenze", p, "ValueError"))
    for tn in (0, 2, 5):
        zs = zusammenfassen(E, unlesbar=2, top_n=tn)
        out.append(("zusammenfassen", tn, zs.anzahl, zs.unlesbar, zs.bytes, zs.status, zs.top_pfade, zs.p50_groesse, zs.p95_groesse, round(zs.fehleranteil, 6)))
        out.append(("text", als_text(zs))); out.append(("csv", als_csv(zs))); out.append(("json", json.loads(als_json(zs))))
    zs0 = zusammenfassen([]); out.append(("leer", zs0.anzahl, zs0.p50_groesse, zs0.fehleranteil, als_text(zs0), als_csv(zs0), als_json(zs0)))
    import tempfile, os
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "a.log"); open(p, "w").write("\n".join(zeilen) + "\n")
        for argv in ([p], [p, "--format", "json"], [p, "--status", "4xx,5xx", "--format", "csv"], [p, "--pfad", "/api/*", "--top", "1"], [p, "--von", "2026-09-19T08:00:00+00:00", "--bis", "2026-09-19T08:15:32+00:00"],
                     [p, "--status", "abc"], [p, "--format", "xml"], [os.path.join(d, "nein.log")], [p, "--von", "murks"]):
            buf = io.StringIO()
            try:
                rc = hauptprogramm(argv, out=buf)
            except SystemExit as ex:
                rc = ("SystemExit", ex.code)
            out.append(("cli", argv[1:], rc, buf.getvalue()))
    return out
