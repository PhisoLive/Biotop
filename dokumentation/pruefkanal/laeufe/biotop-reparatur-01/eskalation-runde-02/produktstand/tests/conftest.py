"""Eigen-Tests: ausschließlich temporäre Datenbanken, keine bezahlten Aufrufe."""
import copy
import socket
import pytest
from biotop.kern import datenbank


def pytest_collection_modifyitems(items):
    """Auftraggeber-Priorität: Kernmaß/Pareto vor den übrigen Eigen-Tests."""
    def prioritaet(item):
        if item.path.name == "test_kernmass_pareto.py":
            if "kernmass" in item.name:
                return 0
            if "einzelregression" in item.name or "altfehler" in item.name:
                return 1
            return 2
        return 3
    items.sort(key=prioritaet)

@pytest.fixture(autouse=True)
def keine_bezahlten_aufrufe(monkeypatch, tmp_path):
    monkeypatch.setenv("BIOTOP_DB", str(tmp_path / "biotop.db"))
    monkeypatch.setattr(datenbank, "DB_PFAD", tmp_path / "biotop.db")
    def gesperrt(*args, **kwargs):
        raise AssertionError("Netzaufruf in Eigen-Test gesperrt")
    monkeypatch.setattr(socket.socket, "connect", gesperrt)
    monkeypatch.setattr(socket, "create_connection", gesperrt)

@pytest.fixture
def messung():
    def bauen(**werte):
        bereich = dict(tests_bestanden=3, tests_fehlgeschlagen=0, sicherheit_punkte=0,
                       tote_funktionen=0, laufzeit_ms=100.0, groesste_funktion=10)
        bereich.update(werte)
        return dict(gueltig=True, kernmass=6,
                    bereiche={"alpha": copy.deepcopy(bereich), "beta": copy.deepcopy(bereich)},
                    werk=dict(baut=True, zyklen=0, bauzeit_ms=100, tests_fehlgeschlagen_liste=[]))
    return bauen

@pytest.fixture
def db_lauf(tmp_path, messung):
    con = datenbank.verbinden(tmp_path / "pruefung.db")
    (tmp_path / "paket" / "alpha").mkdir(parents=True)
    (tmp_path / "paket" / "alpha" / "__init__.py").write_text("")
    con.execute("INSERT INTO werke(id,name,pfad,bericht,status) VALUES(1,?,?,?,?)",
                ("eigenpruefung", str(tmp_path), datenbank.j({"paket":"paket"}), "aufgenommen"))
    con.execute("INSERT INTO laeufe(id,werk_id,budget_eur,status,mass) VALUES(1,1,5,'bereit',?)",
                (datenbank.j({"paket":"paket","bereiche":["alpha","beta"],"nischen":[]}),))
    con.execute("INSERT INTO generationen(lauf_id,nummer,status,masse) VALUES(1,0,'angenommen',?)",
                (datenbank.j(messung()),))
    yield con
    con.close()
