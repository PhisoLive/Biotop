"""Rote Spezifikation (nächster Auftrag): Bestätigungsmessung auch vor einer Ablehnung wegen der GEWINNSCHWELLE der
Nische schnell. Auftrag Runde 2: „Bestätigungsmessung vor jeder Laufzeitablehnung“; gebaut ist sie in 6243377 nur für
Laufzeitrisse (Grenzüberschreitung). Gemessen am Commit: K3091 (S2-Behebung) wurde im Durchgang 3 abgelehnt —
„Nische schnell: Laufzeit nicht um ≥ 15 % gesunken, Kernmaß unverändert“ (planung gepaart 9,6116 → 8,2913 = −13,7 %),
in den Durchgängen 1 und 2 überlebte er (−17 %, −22 %). Ohne Nachmessung entscheidet eine einzelne gepaarte Messung.
Erwartung: an 6243377 ist test_gewinnschwelle_wird_nachgemessen ROT, die Gegenprobe GRÜN."""
import sqlite3
from types import SimpleNamespace

from biotop.kern import datenbank, messgeraet
from biotop.organe import aegis
from biotop.organe import verhaltensvergleich as vv


def _pruefen(tmp_path, monkeypatch, erste, zweite):
    con = sqlite3.connect(":memory:", isolation_level=None)
    con.row_factory = sqlite3.Row
    con.executescript(datenbank.SCHEMA)
    w = tmp_path / "w"
    (w / "src" / "alpha").mkdir(parents=True)
    (w / "package.json").write_text('{"type":"module"}')
    (w / "src" / "alpha" / "a.ts").write_text("export function a(x: number): number {\n  return x;\n}\n")
    diff = ("--- a/src/alpha/a.ts\n+++ b/src/alpha/a.ts\n@@ -1,3 +1,3 @@\n export function a(x: number): number {\n"
            "-  return x;\n+  return x + 0;\n }\n")
    con.execute("INSERT INTO kandidaten(id,lauf_id,generation,bereich,nische,status,diff) VALUES(7,1,1,'alpha','schnell','erzeugt',?)", (diff,))
    monkeypatch.setattr(aegis, "aufrufen", lambda *a, **k: SimpleNamespace(text="KEIN ANGRIFF"))

    def messen(werk, bereiche, paket, ref, dateien=None, **k):            # Kernmaß unverändert (0 → 0)
        return {"gueltig": True, "kernmass": 0, "werk": {"baut": True, "zyklen": 0, "bauzeit_ms": 100,
                "tests_fehlgeschlagen_liste": [], "tests_fehlgeschlagen_ids": []},
                "bereiche": {"alpha": {"tests_bestanden": 1, "tests_fehlgeschlagen": 0, "sicherheit_punkte": 0,
                                       "sicherheit_befunde": [], "tote_funktionen": 0, "laufzeit_ms": None, "groesste_funktion": 3}}}
    monkeypatch.setattr(aegis.messgeraet, "messen", messen)
    zaehl = {"paare": 0}
    original = messgeraet.laufzeit_gepaart

    def gepaart(*a, **k):
        zaehl["paare"] += 1
        return original(*a, **k)
    monkeypatch.setattr(messgeraet, "laufzeit_gepaart", gepaart)

    def laufzeit(werk, bereiche, paket, ref, dateien=None, zeitlimit_s=150):
        kand, basis = erste if zaehl["paare"] == 1 else zweite
        return {"gueltig": True, "grund": "", "bereiche": {"alpha": {"laufzeit_ms": kand if dateien else basis}}}
    monkeypatch.setattr(messgeraet, "laufzeit_messen", laufzeit)
    ok = {"gueltig": True, "beobachtungen": {"alpha/a:a#0": "1"}, "eingewickelt": {"alpha/a": ["a"]}, "aufgerufen": {"alpha/a:a": 1}}
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: dict(ok))
    basis = messen(w, ["alpha"], "src", None)
    u = aegis.pruefen(con, 1, 1, 7, w, "src", ["alpha"], [], basis, basis, "// last", {"laufzeit_faktor": 2.0})
    return u, zaehl


def test_gewinnschwelle_wird_nachgemessen(tmp_path, monkeypatch):
    """Erste gepaarte Messung −12 % (unter 15 %), Nachmessung −20 %: die Ablehnung ist nicht bestätigt → nicht abgelehnt."""
    u, z = _pruefen(tmp_path, monkeypatch, erste=(8.8, 10.0), zweite=(8.0, 10.0))
    assert z["paare"] == 2 and u["status"] != "abgelehnt", (z, u["status"], u["grund"])


def test_gegenprobe_bestaetigte_gewinnschwelle_lehnt_ab(tmp_path, monkeypatch):
    """Beide Messungen unter 15 % → abgelehnt (bestätigt)."""
    u, z = _pruefen(tmp_path, monkeypatch, erste=(8.8, 10.0), zweite=(9.0, 10.0))
    assert u["status"] == "abgelehnt" and "15 %" in u["grund"], (z, u["grund"])


def test_gewinn_wird_vor_der_annahme_bestaetigt(tmp_path, monkeypatch):
    """Gegenrichtung (Review Nr. 14): erste Messung −20 %, Nachmessung −5 % → der Gewinn ist nicht bestätigt, keine Annahme."""
    u, z = _pruefen(tmp_path, monkeypatch, erste=(8.0, 10.0), zweite=(9.5, 10.0))
    assert z["paare"] == 2 and u["status"] != "ueberlebt", (z, u["status"], u["grund"])


def test_gegenprobe_bestaetigter_gewinn_ueberlebt(tmp_path, monkeypatch):
    u, z = _pruefen(tmp_path, monkeypatch, erste=(8.0, 10.0), zweite=(8.1, 10.0))
    assert u["status"] == "ueberlebt", (z, u["grund"])
