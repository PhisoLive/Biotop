"""Rote Spezifikation (nächster Auftrag): Fehlt einer Seite in einem Bereich der Wert (laufzeit_ms None, z. B.
`last_<bereich>` wirft), ist die gepaarte Messung ein Messgerätausfall (gueltig False, seite) — nicht gültig mit
`kandidat: None`, das `laufzeit_einsetzen` stillschweigend überspringt. Gemessen an 330b4ec: Python-Kandidat mit
Syntaxfehler in lagerhaus/formeln/auswertung.py → gueltig True (PYTHON-LAUFZEIT-PROBE, NACHLESE.json)."""
from biotop.kern import messgeraet


def test_teilausfall_kandidat_ist_messgeraetausfall(monkeypatch):
    def messen(werk, bereiche, paket, ref, dateien, zeitlimit_s=150):
        kand = dateien is not None
        return {"gueltig": True, "grund": "", "bereiche": {
            "a": {"laufzeit_ms": 1.0}, "b": ({"laufzeit_ms": None, "laufzeit_fehler": "SyntaxError"} if kand else {"laufzeit_ms": 2.0})}}
    monkeypatch.setattr(messgeraet, "laufzeit_messen", messen)
    r = messgeraet.laufzeit_gepaart(".", ["a", "b"], "p", "last", None, {"x": "y"}, n=3)
    assert r["gueltig"] is False and r.get("seite") == "kandidat", r


def test_gegenprobe_vollstaendige_messung_bleibt_gueltig(monkeypatch):
    monkeypatch.setattr(messgeraet, "laufzeit_messen", lambda *a, **k: {"gueltig": True, "grund": "", "bereiche": {
        "a": {"laufzeit_ms": 1.0}, "b": {"laufzeit_ms": 2.0}}})
    r = messgeraet.laufzeit_gepaart(".", ["a", "b"], "p", "last", None, {"x": "y"}, n=3)
    assert r["gueltig"] is True and r["bereiche"]["b"]["kandidat"] == 2.0, r
