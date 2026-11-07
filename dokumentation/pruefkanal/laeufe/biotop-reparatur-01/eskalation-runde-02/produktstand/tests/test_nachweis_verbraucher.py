"""F7-Verbraucher: echte Eigenfixture-Kammerläufe + markierte Status-I/O-Doubles.

Kein Werkcode auf dem Host, keine produktiven Werke/DBs und keine Modellaufrufe.
Die Kammerzählung erfasst nur echte kammer.ausfuehren-Aufrufe, nicht I/O-Doubles.
"""
import json
import os
from pathlib import Path
from copy import deepcopy
import xml.etree.ElementTree as ET

import pytest

from biotop.kern import datenbank, messgeraet
from biotop.organe import fundpruefung as F, kammer

EINS = "def test_eins():\n    assert 2 + 2 == 4\n"
ZWEI = EINS + "\ndef test_zwei():\n    assert 3 + 3 == 6\n"
SKIP = EINS + "\ndef test_zwei():\n    import pytest\n    pytest.skip('absichtlich nicht ausgeführt')\n"


@pytest.fixture(autouse=True)
def rohbelege(request):
    with kammer.zaehlung() as aufrufe:
        yield
    ziel = os.environ.get("NACHWEIS_BELEGE")
    if ziel:
        with (Path(ziel) / "kammer.jsonl").open("a") as f:
            for e in aufrufe:
                f.write(json.dumps({"test": request.node.nodeid, **e}, ensure_ascii=False) + "\n")
    print("ECHTE_KAMMERLAEUFE", request.node.nodeid, len(aufrufe))


@pytest.fixture
def eigenwerk(tmp_path):
    werk = tmp_path / "eigenwerk"
    (werk / "paket" / "alpha").mkdir(parents=True)
    (werk / "paket" / "__init__.py").write_text("")
    (werk / "paket" / "alpha" / "__init__.py").write_text("from .quelle import wert\n")
    (werk / "paket" / "alpha" / "quelle.py").write_text("def wert():\n    return 4\n")
    (werk / "tests").mkdir()
    (werk / "tests" / "test_alpha.py").write_text("from paket.alpha import wert\ndef test_wert():\n    assert wert() == 4\n")
    return werk


def io_ergebnis(status="gut", datei="tests/test_neubewertung_probe.py"):
    """Gestelltes Kammer-I/O, KEIN ausgeführter Werk-/JUnit-Nachweis."""
    root = ET.Element("testsuites")
    suite = ET.SubElement(root, "testsuite")
    for name in ("test_eins", "test_zwei"):
        if status in ("leer", "fehlender_test") and (status == "leer" or name == "test_zwei"):
            continue
        tc = ET.SubElement(suite, "testcase", classname=datei[:-3].replace("/", "."), name=name)
        if name == "test_zwei" and status in ("skip", "xfail", "error", "rot"):
            tag = {"skip": "skipped", "xfail": "skipped", "error": "error", "rot": "failure"}[status]
            ET.SubElement(tc, tag, message="AssertionError" if status == "rot" else status)
    xml = ET.tostring(root, encoding="unicode")
    summary = {"skip": "1 passed, 1 skipped", "xfail": "1 passed, 1 xfailed", "error": "1 passed, 1 error",
               "leer": "0 passed", "fehlender_test": "1 passed", "rot": "1 passed, 1 failed"}.get(status, "2 passed")
    stdout = summary + "\n@@NACHWEIS@@" + xml + "@@ENDE@@\n"
    if status == "fehlend":
        stdout = "2 passed\n"
    if status == "kaputtes_xml":
        stdout = "2 passed\n@@NACHWEIS@@<testsuites>@@ENDE@@\n"
    rc = {"abbruch": 124, "prozessfehler": 2, "rot": 1, "error": 1}.get(status, 0)
    return kammer.Ergebnis(rc, stdout, "", 0.0, status in ("abbruch", "zeitlimit_trotz_rc0"), "IO-DOUBLE")


def io_installieren(monkeypatch, ergebnis):
    def lauf(*args, **kwargs):
        print("KAMMER_IO_DOUBLE", json.dumps(ergebnis.__dict__, ensure_ascii=False))
        return ergebnis
    monkeypatch.setattr(kammer, "ausfuehren", lauf)


@pytest.mark.parametrize("status", ["skip", "xfail", "abbruch", "prozessfehler", "zeitlimit_trotz_rc0",
                                   "leer", "fehlend", "fehlender_test", "kaputtes_xml", "error"])
def test_fund_verweigert_nicht_ausgefuehrten_nachweis(monkeypatch, eigenwerk, status):
    io_installieren(monkeypatch, io_ergebnis(status))
    with pytest.raises(RuntimeError, match="Nachweis"):
        F._ausfuehren(eigenwerk, "probe", ZWEI)


@pytest.mark.integration
@pytest.mark.parametrize("code,besteht,absturz", [
    (ZWEI, True, False),
    ("def test_eins():\n    assert False\n", False, False),
    ("from paket.alpha import wert\ndef test_eins():\n    wert()\n", False, True),
])
def test_fund_ausgefuehrte_gegenrouten(eigenwerk, code, besteht, absturz):
    if absturz:
        (eigenwerk / "paket/alpha/quelle.py").write_text("def wert():\n    raise ValueError('Produktfehler')\n")
    assert F._ausfuehren(eigenwerk, "probe", code)[:2] == (besteht, absturz)


@pytest.mark.integration
def test_fund_echter_skip_ist_kein_bestandener_fundtest(eigenwerk):
    with pytest.raises(RuntimeError, match="Nachweis"):
        F._ausfuehren(eigenwerk, "probe", SKIP)


@pytest.mark.integration
@pytest.mark.parametrize("code", [
    "", "raise ImportError('Sammelfehler')\n", ZWEI + "test_zwei.__test__ = False\n",
    EINS + "\ndef test_zwei():\n    import pytest\n    pytest.xfail('nicht bestanden')\n",
    EINS + "\ndef test_zwei():\n    import pytest\n    pytest.exit('Abbruch', returncode=2)\n",
    EINS + "\ndef test_zwei():\n    import os\n    os._exit(0)\n",
], ids=["leer", "sammelfehler", "test_fehlt", "xfail", "abbruch", "exit0_ohne_junit"])
def test_fund_echte_unvollstaendige_laeufe(eigenwerk, code):
    with pytest.raises(RuntimeError, match="Nachweis"):
        F._ausfuehren(eigenwerk, "probe", code)


def test_fund_abbruch_mit_vertragsverweis_wird_nicht_zum_fund(monkeypatch, eigenwerk, tmp_path):
    con = datenbank.verbinden(tmp_path / "fund.db")
    con.execute("INSERT INTO immunsystem(werk_id, name, bereich, code, status) VALUES(1, 'probe', 'alpha', ?, 'offen_norm')", (ZWEI,))
    monkeypatch.setattr(F.verfassung, "lesen", lambda *a: {})
    monkeypatch.setattr(F.aegis, "_nennt_vertrag", lambda *a: True)
    io_installieren(monkeypatch, io_ergebnis("prozessfehler"))
    try:
        with pytest.raises(RuntimeError, match="Nachweis"):
            F.bewerten(con, 1, 1, eigenwerk)
        assert con.execute("SELECT status FROM immunsystem").fetchone()[0] == "offen_norm"
    finally:
        con.close()


@pytest.fixture
def verhandlung(db_lauf, monkeypatch, eigenwerk, messung, tmp_path):
    """Originaler Urteilleser; Hersteller und Aegis-I/O explizite Unit-Doubles."""
    from biotop import lauf as L
    monkeypatch.setattr(L.aufnahme, "WERKE", tmp_path / "private-werke")
    con = db_lauf
    for kid in (1, 2):
        con.execute("INSERT INTO kandidaten(id,lauf_id,generation,bereich,diff,status,grund,begruendung,vertraege) "
                    "VALUES(?,1,1,'alpha','Unit-Diff','erzeugt','','Unit','test_vertrag_alpha_beta')", (kid,))
    monkeypatch.setattr(L.vertraege, "nachbar_von", lambda *a: "beta")
    monkeypatch.setattr(L.vertraege, "fuer_bereich", lambda *a: [])
    monkeypatch.setattr(L.vertraege, "text_fuer_bereich", lambda *a: "Unit-Vertrag")
    monkeypatch.setattr(L.genesis, "erzeugen", lambda *a, **kw: [2])
    monkeypatch.setattr(L.aegis, "kandidat_dateien", lambda *a: {"paket/alpha/quelle.py": "# Unit-Diff"})
    basis = messung()
    # Echter Kernmaß-/Pareto-Entscheider auf ausdrücklich gestellten Messwerten.
    mass = messgeraet.urteil_f2(basis, deepcopy(basis), basis, ["alpha", "beta"], ["alpha", "beta"])
    assert mass["ok"] is False and mass["pareto_schlechter"] == [] and mass["grenzen_gerissen"] == []
    urteil = dict(status="abgelehnt", grund="Kernmaß unverändert", mass=mass, vertrag_verletzt=[])
    alt = dict(status="abgelehnt", grund="Vertrag verletzt", vertrag_verletzt=["test_vertrag_alpha_beta.py::test_v"])

    def pruefen(u):
        calls = []
        def paar(*a, **kw):
            calls.append(kw)
            print("AEGIS_URTEIL_IO_DOUBLE", json.dumps(u, ensure_ascii=False))
            return deepcopy(u)
        monkeypatch.setattr(L.aegis, "pruefen", paar)
        r = L._verhandeln(con, 1, {"id": 1}, 1, eigenwerk, "paket", ["alpha", "beta"], [],
                         basis, basis, None, {}, "alpha", 1, deepcopy(alt))
        assert len(calls) == 1
        assert calls[0]["extra_code"]
        return r
    return con, urteil, pruefen


@pytest.mark.parametrize("fehlt", ["mass", "mass_null", "mass_leer", "vertrag_verletzt", "vertrag_null",
                                    "pareto_schlechter", "grenzen_gerissen", "kern_basis", "kern_kandidat",
                                    "zuwachs", "ok", "grund", "pareto_null", "grenzen_null", "kern_null"])
def test_verhandlung_ohne_vollstaendiges_messurteil_ist_nicht_bestanden(verhandlung, fehlt):
    con, u, pruefen = verhandlung
    if fehlt == "mass_null":
        u["mass"] = None
    elif fehlt == "mass_leer":
        u["mass"] = {}
    elif fehlt == "vertrag_null":
        u["vertrag_verletzt"] = None
    elif fehlt == "pareto_null":
        u["mass"]["pareto_schlechter"] = None
    elif fehlt == "grenzen_null":
        u["mass"]["grenzen_gerissen"] = None
    elif fehlt == "kern_null":
        u["mass"]["kern_kandidat"] = None
    elif fehlt in ("mass", "vertrag_verletzt"):
        del u[fehlt]
    else:
        del u["mass"][fehlt]
    r = pruefen(u)
    assert r.get("verhandlung_bestanden") is not True, "Fehlende Messung ist keine bestandene Verhandlung"
    assert r["status"] == "abgelehnt"
    assert not con.execute("SELECT 1 FROM protokoll WHERE art='verhandlung.bestanden'").fetchone()


def test_verhandlung_vollstaendiges_kernurteil_ohne_gewinn_besteht(verhandlung):
    con, u, pruefen = verhandlung
    r = pruefen(u)
    assert r["verhandlung_bestanden"] is True
    assert r["anpassungen"] == [2]
    assert r["mass"]["ok"] is False, "Vertragsprüfung ist nicht die Annahmeentscheidung"
    assert con.execute("SELECT 1 FROM protokoll WHERE art='verhandlung.bestanden'").fetchone()


@pytest.mark.parametrize("verletzung", ["vertrag_verletzt", "pareto_schlechter", "grenzen_gerissen"])
def test_verhandlung_ausgefuehrtes_rotes_urteil_bleibt_rot(verhandlung, verletzung):
    con, u, pruefen = verhandlung
    if verletzung == "vertrag_verletzt":
        u[verletzung] = ["test_vertrag_alpha_beta.py::test_v"]
    else:
        u["mass"][verletzung] = ["alpha: echte Abweichung (Unit-Messwert)"]
    assert pruefen(u).get("verhandlung_bestanden") is not True
    assert not con.execute("SELECT 1 FROM protokoll WHERE art='verhandlung.bestanden'").fetchone()


@pytest.fixture
def fund_vorspann(db_lauf, eigenwerk, monkeypatch, messung, tmp_path):
    """Gate-UNIT: echte Fundprüfung, übrige Vorspannstufen ausdrücklich I/O-Doubles."""
    import hashlib
    from biotop import lauf as L
    from biotop.organe import vorspann as V
    monkeypatch.setattr(L.aufnahme, "WERKE", tmp_path / "private-werke")
    con = db_lauf
    con.execute("DELETE FROM generationen")
    con.execute("UPDATE laeufe SET mass=NULL, status='kartiert'")
    con.execute("UPDATE werke SET pfad=?", (str(eigenwerk),))
    con.execute("INSERT INTO landkarte(werk_id,stufe,schluessel,inhalt) VALUES(1,1,'unit','{}')")
    monkeypatch.setattr(L, "_referenzlast", lambda *a: "# Unit-Vorbedingung")
    monkeypatch.setattr(V.verfassung, "lesen", lambda *a: {"regeln": {}})
    monkeypatch.setattr(V.vertraege, "alle", lambda *a: ["Unit-Vertrag"])
    monkeypatch.setattr(V, "_quellen", lambda *a: {"Unit-Quellbindung": True, "bereiche": ["alpha"]})
    monkeypatch.setattr(F.aegis, "_nennt_vertrag", lambda *a: False)
    monkeypatch.setattr(V.eichung, "rauschmessung", lambda *a: {
        "toleranz": {"alpha": 1.2}, "gesperrt": [], "lauf_startet": True,
        "bereiche": {"alpha": {"toleranz": 1.2, "gesperrt": False, "werte": [100, 100, 100, 110, 120]}}})
    vertrag = eigenwerk / "tests/test_unitvertrag.py"
    vertrag.write_text(EINS)
    g = {"vertrag_pfad": str(vertrag.relative_to(eigenwerk)), "vertrag_pruefsumme": hashlib.sha256(vertrag.read_bytes()).hexdigest()}
    monkeypatch.setattr(V.eichgegenstand, "sichern", lambda *a: {"gegenstand": g})
    monkeypatch.setattr(V.eichgegenstand, "lesen", lambda *a: g)
    monkeypatch.setattr(V.messgeraet, "messen", lambda *a, **kw: messung())
    calls = []
    def proben(*a, **kw):
        calls.append(True)
        gruppen = {}
        for gruppe, bestanden in (("proben", True), ("gegenproben", False)):
            gruppen[gruppe] = {n: {"ausgefuehrt": True, "pruefbar": True, "bestanden": bestanden,
                                   "kammerlaeufe": 0, "dauer_s": 0, "modellaufrufe": 0, "kosten_eur": 0}
                               for n in ("nebenwirkung", "regression", "norm", "vertrag")}
        return dict(bestanden=True, gegenstand=g, **gruppen)
    monkeypatch.setattr(V.eichproben, "proben", proben)
    return con, V, calls


@pytest.mark.integration
def test_pflichtvorspann_fundskip_stoppt_vor_proben_und_freigabe(fund_vorspann):
    con, V, calls = fund_vorspann
    con.execute("INSERT INTO immunsystem(werk_id, name, bereich, code, status) VALUES(1,'probe','alpha',?,'offen')", (SKIP,))
    with pytest.raises(V.VorspannFehler, match="Nachweis"):
        V.ausfuehren(con, 1)
    assert calls == []
    r = con.execute("SELECT status,nachweis_sha256 FROM vorspann_nachweise").fetchone()
    assert tuple(r) == ("gescheitert", None)
    assert con.execute("SELECT status FROM immunsystem").fetchone()[0] == "offen"
    with pytest.raises(V.VorspannFehler, match="Nachweis"):
        V.verlangen(con, 1, "gen0")


@pytest.mark.integration
def test_pflichtvorspann_ausgefuehrter_fund_erreicht_proben(fund_vorspann):
    con, V, calls = fund_vorspann
    con.execute("INSERT INTO immunsystem(werk_id,name,bereich,code,status,ursprung) VALUES(1,'probe','alpha',?,'offen','Eigenfixture')", (ZWEI,))
    r = V.ausfuehren(con, 1)
    assert calls == [True]
    assert r["funde"]["kammerlaeufe"] == 1
    assert r["funde"]["ergebnisse"][0]["besteht_am_ausgang"] is True
    assert con.execute("SELECT status FROM immunsystem").fetchone()[0] == "offen_norm"
    assert V.verlangen(con, 1, "gen0")["nachweis_sha256"] == r["nachweis_sha256"]


def test_pflichtvorspann_leerer_fundbestand_ist_keine_fehlende_pruefung(fund_vorspann, monkeypatch):
    con, V, calls = fund_vorspann
    def kein_gegenstand(*a, **kw):
        pytest.fail("Kein Fundbestand: keine künstliche Kammer-Testpflicht")
    monkeypatch.setattr(kammer, "ausfuehren", kein_gegenstand)
    r = V.ausfuehren(con, 1)
    assert r["funde"]["geprueft"] == 0 and r["funde"]["kammerlaeufe"] == 0
    assert calls == [True]
    assert V.verlangen(con, 1, "gen0")["nachweis_sha256"] == r["nachweis_sha256"]
