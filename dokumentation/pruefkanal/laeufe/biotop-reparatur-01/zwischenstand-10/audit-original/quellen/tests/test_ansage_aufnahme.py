"""Gestellte, netzfreie Eigentests; kein Ersatz für den Bestands-Replay."""
import sqlite3
from types import SimpleNamespace

import pytest

from biotop.kern import datenbank, protokoll
from biotop.organe import aegis


@pytest.fixture
def con():
    c = sqlite3.connect(":memory:", isolation_level=None)
    c.row_factory = sqlite3.Row
    c.executescript(datenbank.SCHEMA)
    yield c
    c.close()


@pytest.mark.parametrize("art", ["fund", "norm"])
def test_erster_neuer_test_wird_nicht_von_eigener_ansage_gesperrt(con, tmp_path, monkeypatch, art):
    """Echte _angriff→Ansage→pruefen→Fund/Norm-Aufnahme, nur Außenwirkungen ersetzt."""
    p = tmp_path / "paket" / "bereich" / "quelle.py"
    p.parent.mkdir(parents=True)
    p.write_text("def wert():\n    return 1\n")
    diff = "--- a/paket/bereich/quelle.py\n+++ b/paket/bereich/quelle.py\n@@ -1,2 +1,2 @@\n def wert():\n-    return 1\n+    return 2\n"
    con.execute("INSERT INTO kandidaten(id,lauf_id,generation,bereich,nische,status,diff) VALUES(7,1,1,'bereich','test','erzeugt',?)", (diff,))
    code = "from paket.bereich.quelle import wert\ndef test_neu():\n    assert wert() == 3\n"
    replies = iter(["wert|Eq:zahl", f"```python\n{code}```"])
    monkeypatch.setattr(aegis, "aufrufen", lambda *a, **k: SimpleNamespace(text=next(replies)))

    def junit(werk, paket, dateien, testdateien):
        return {f"{t}::test_neu": {"ok": False, "bestaetigt": True,
                "ort": "paket/bereich/quelle.py" if art == "fund" else "",
                "meldung": "ValueError" if art == "fund" else "AssertionError"} for t in testdateien}

    monkeypatch.setattr(aegis, "junit_lauf", junit)
    # Endpunkt nach Aufnahme; keine Kammer, kein Messgerät-/Modellaufruf.
    monkeypatch.setattr(aegis.messgeraet, "messen", lambda *a, **k: {"gueltig": False, "grund": "Test-Endpunkt"})
    aegis.pruefen(con, 1, 1, 7, tmp_path, "paket", ["bereich"], [],
                  {"bereiche": {"bereich": {}}}, {}, None, None)
    rows = list(con.execute("SELECT name,status,ursprung FROM immunsystem"))
    assert len(rows) == 1, "Die aktuelle eigene Ansage darf den ersten neuen Test nicht sperren"
    assert rows[0]["name"] == ("aegis_k7_bereich" if art == "fund" else "norm_k7_bereich")
    assert "behauptung=wert|Eq:zahl" in rows[0]["ursprung"]
    assert not con.execute("SELECT 1 FROM protokoll WHERE art='immun.aufnahme_gesperrt'").fetchone()


CODE = "def test_neu():\n    assert wert() == 3\n"


def immun(con, schluessel, name="vorher"):
    con.execute("INSERT INTO immunsystem(werk_id,lauf_id,bereich,name,ursprung,status) VALUES(1,1,'bereich',?,?,'offen_norm')",
                (name, f"behauptung={schluessel}"))


def ansage(con, schluessel="wert|Eq:zahl", kandidat=7):
    return protokoll.schreiben(con, "aegis.ansage", lauf_id=1, werk_id=1, bereich="bereich",
                              kandidat=kandidat, behauptung=schluessel, ausgefuehrt=True)


@pytest.mark.parametrize("quelle", ["vorherige_eigene_ansage", "fremde_ansage", "immun", "im_selben_angriff_aufgenommen"])
@pytest.mark.parametrize("art", ["fund", "norm"])
def test_nur_die_aktuelle_ansagezeile_ist_ausgenommen(con, quelle, art):
    if quelle == "vorherige_eigene_ansage":
        ansage(con, kandidat=7)
    elif quelle == "fremde_ansage":
        ansage(con, kandidat=6)
    elif quelle == "immun":
        immun(con, "wert|Eq:zahl")
    nr = ansage(con)
    if quelle == "im_selben_angriff_aufgenommen":
        immun(con, "wert|Eq:zahl")
    nehmen, sperren = aegis.aufnahmesperre(con, 1, 1, "bereich", CODE, ["test_neu"], "paket", 7, art,
                                         eigene_ansage_nr=nr)
    assert nehmen == []
    assert sperren == [("test_neu", "wert|Eq:zahl")]


def test_abweichende_neue_behauptung_bleibt_zulaessig(con):
    nr = ansage(con, "anderes|Eq:zahl")
    nehmen, sperren = aegis.aufnahmesperre(con, 1, 1, "bereich", CODE, ["test_neu"], "paket", 7, "fund",
                                         eigene_ansage_nr=nr)
    assert nehmen == [("test_neu", "wert|Eq:zahl")]
    assert sperren == []


def test_zweiter_test_selben_schluessels_im_angriff_gesperrt(con):
    nr = ansage(con)
    code = CODE + "\ndef test_zweiter():\n    assert wert() == 99\n"
    nehmen, sperren = aegis.aufnahmesperre(con, 1, 1, "bereich", code, ["test_neu", "test_zweiter"], "paket", 7, "norm",
                                         eigene_ansage_nr=nr)
    assert nehmen == [("test_neu", "wert|Eq:zahl")]
    assert sperren == [("test_zweiter", "wert|Eq:zahl")]


@pytest.mark.parametrize("quelle,anzahl", [("immun", 220), ("ansage", 420), ("immun", 520)])
def test_aufnahme_prueft_den_ganzen_vorrat_nicht_nur_ein_fenster(con, quelle, anzahl):
    schreiben = (lambda s, i: immun(con, s, str(i))) if quelle == "immun" else (lambda s, i: ansage(con, s))
    schreiben("wert|Eq:zahl", 0)
    for i in range(1, anzahl):
        schreiben(f"anders{i}|Eq:zahl", i)
    nehmen, sperren = aegis.aufnahmesperre(con, 1, 1, "bereich", CODE, ["test_neu"], "paket", 7, "fund")
    assert nehmen == []
    assert sperren == [("test_neu", "wert|Eq:zahl")]


def test_ansagesperre_nutzt_vollstaendigen_vorrat_statt_promptfenster(con, tmp_path, monkeypatch):
    immun(con, "wert|Eq:zahl")
    for i in range(30):
        immun(con, f"anders{i}|Eq:zahl", str(i))
    anfragen = []
    def antwort(*args, **kwargs):
        anfragen.append(kwargs["zweck"])
        return SimpleNamespace(text="wert|Eq:zahl")
    monkeypatch.setattr(aegis, "aufrufen", antwort)
    ergebnis = aegis._angriff(con, 1, 1, "paket", "bereich", "", {}, tmp_path, [])
    assert anfragen == ["aegis.ansage.bereich"], "Bekannte Ansage muss den Testgenerierungs-Aufruf sparen"
    assert ergebnis == (None, aegis.MODELL_ANGRIFF[1], "wert|Eq:zahl")


@pytest.mark.parametrize("antwort_text", ["KEIN ANGRIFF", "wert|Eq:zahl"])
def test_ansageprotokoll_bindet_auch_abstinenz_und_sperre_an_kandidat(con, tmp_path, monkeypatch, antwort_text):
    immun(con, "wert|Eq:zahl")
    monkeypatch.setattr(aegis, "aufrufen", lambda *a, **k: SimpleNamespace(text=antwort_text))
    aegis._angriff(con, 1, 1, "paket", "bereich", "", {}, tmp_path, [], kandidat_id=7)
    row = con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.ansage'").fetchone()
    d = datenbank.lj(row["inhalt"])
    assert (d.get("kandidat"), d.get("werk_id")) == (7, 1)


def test_fund_aus_selbem_angriff_sperrt_nachfolgenden_normzweig(con, tmp_path, monkeypatch):
    p = tmp_path / "paket" / "bereich" / "quelle.py"
    p.parent.mkdir(parents=True)
    p.write_text("x = 1\n")
    diff = "--- a/paket/bereich/quelle.py\n+++ b/paket/bereich/quelle.py\n@@ -1 +1 @@\n-x = 1\n+x = 2\n"
    con.execute("INSERT INTO kandidaten(id,lauf_id,generation,bereich,nische,status,diff) VALUES(7,1,1,'bereich','test','erzeugt',?)", (diff,))
    code = "def test_fund():\n    assert wert() == 3\ndef test_norm():\n    assert wert() == 4\n"
    replies = iter(["wert|Eq:zahl", f"```python\n{code}```"])
    monkeypatch.setattr(aegis, "aufrufen", lambda *a, **k: SimpleNamespace(text=next(replies)))
    def junit(werk, paket, dateien, testdateien):
        return {f"{t}::{n}": {"ok": False, "bestaetigt": True,
                "ort": "paket/bereich/quelle.py" if n == "test_fund" else "",
                "meldung": "ValueError" if n == "test_fund" else "AssertionError"}
                for t in testdateien for n in ["test_fund", "test_norm"]}
    monkeypatch.setattr(aegis, "junit_lauf", junit)
    monkeypatch.setattr(aegis.messgeraet, "messen", lambda *a, **k: {"gueltig": False, "grund": "Test-Endpunkt"})
    aegis.pruefen(con, 1, 1, 7, tmp_path, "paket", ["bereich"], [],
                  {"bereiche": {"bereich": {}}}, {}, None, None)
    assert [r[0] for r in con.execute("SELECT name FROM immunsystem")] == ["aegis_k7_bereich"]
    d = datenbank.lj(con.execute("SELECT inhalt FROM protokoll WHERE art='immun.aufnahme_gesperrt'").fetchone()[0])
    assert (d["test"], d["sperrart"], d["gegenstueck"]) == ("test_norm", "norm", "bereits im Vorrat des Bereichs")


def test_halbe_gespeicherte_schluessel_sperren_nichts(con):
    for i, s in enumerate(["|", "wert|", "|Eq:zahl"]):
        immun(con, s, str(i))
    assert aegis.bisherige_behauptungen(con, 1, "bereich", 1, limit=None) == []


def test_doppelung_ist_behauptung_statt_fundort(con):
    code = CODE + "\ndef test_andere_datei():\n    assert wert() == 17\n"
    einzig, doppel = aegis._doppelungen({"test_neu", "test_andere_datei"}, {}, "datei.py", con, 1, "bereich", code, "paket")
    assert einzig == {"test_andere_datei"}
    assert doppel == {"test_neu"}
