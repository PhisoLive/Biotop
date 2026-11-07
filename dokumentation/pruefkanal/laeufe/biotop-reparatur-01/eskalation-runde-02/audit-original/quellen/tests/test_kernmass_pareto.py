"""Direkte Eigen-Tests der F2-Regeln, nicht Tests der Übungswerke."""
import pytest
from biotop.kern import messgeraet as M


@pytest.mark.parametrize("bestandene", [0, 1, 1000])
def test_kernmass_belohnt_keine_bestehenden_tests(messung, bestandene):
    m = messung(tests_bestanden=bestandene, tests_fehlgeschlagen=2,
                sicherheit_punkte=3, tote_funktionen=4)
    assert M.kernmass_f2(m) == sum(-(2 + 3 + 4) for _ in m["bereiche"])


def test_kernmass_null_ist_der_hoechstwert(messung):
    assert M.kernmass_f2(messung()) == 0


@pytest.mark.parametrize("merkmal", M.PARETO_F2)
def test_kernmass_zaehlt_jeden_schaden_einzeln(messung, merkmal):
    basis, kandidat = messung(), messung()
    kandidat["bereiche"]["beta"][merkmal] = 1
    assert M.kernmass_f2(kandidat) == M.kernmass_f2(basis) - 1


@pytest.mark.parametrize("merkmal", M.PARETO_F2)
def test_fehlende_kernmass_spalte_ist_nicht_null(messung, merkmal):
    m = messung()
    del m["bereiche"]["alpha"][merkmal]
    with pytest.raises(KeyError):
        M.kernmass_f2(m)


def test_pareto_sieht_schaden_im_nachbarn_trotz_gesamtgewinn(messung):
    basis, kandidat = messung(), messung()
    basis["bereiche"]["alpha"]["sicherheit_punkte"] = 10
    kandidat["bereiche"]["beta"]["tote_funktionen"] = 1
    assert M.kernmass_f2(kandidat) > M.kernmass_f2(basis)
    schlechter, besser = M.pareto_f2(basis, kandidat, ["alpha", "beta"])
    assert any("beta.tote_funktionen" in s for s in schlechter)
    assert any("alpha.sicherheit_punkte" in s for s in besser)


def test_pareto_erkennt_einzelregression_trotz_sinkender_fehlsumme(messung):
    basis, kandidat = messung(), messung()
    basis["bereiche"]["alpha"]["tests_fehlgeschlagen"] = 2
    basis["werk"]["tests_fehlgeschlagen_liste"] = ["test_alt_eins", "test_alt_zwei"]
    kandidat["bereiche"]["alpha"]["tests_fehlgeschlagen"] = 1
    kandidat["werk"]["tests_fehlgeschlagen_liste"] = ["test_regression"]
    schlechter, _ = M.pareto_f2(basis, kandidat, ["alpha", "beta"])
    assert any("Regression je Test" in s and "test_regression" in s for s in schlechter)


def test_pareto_haelt_gemeinsamen_altfehler_nicht_fuer_regression(messung):
    basis, kandidat = messung(), messung()
    basis["werk"]["tests_fehlgeschlagen_liste"] = ["test_offen"]
    kandidat["werk"]["tests_fehlgeschlagen_liste"] = ["test_offen"]
    schlechter, besser = M.pareto_f2(basis, kandidat, ["alpha", "beta"])
    assert schlechter == [] and besser == []


def test_pareto_baufehler_wird_nicht_weggezaehlt(messung):
    basis, kandidat = messung(), messung()
    kandidat["werk"]["baut"] = False
    schlechter, _ = M.pareto_f2(basis, kandidat, ["alpha", "beta"])
    assert "werk.baut: True → False" in schlechter


def test_rauschsperre_blendet_keinen_semantischen_nachbarschaden_aus(messung):
    basis, kandidat = messung(tote_funktionen=1), messung(tote_funktionen=1)
    kandidat["bereiche"]["alpha"]["tote_funktionen"] = 0
    kandidat["bereiche"]["beta"]["tests_fehlgeschlagen"] = 1
    r = M.urteil_f2(basis, kandidat, basis, ["alpha", "beta"], ["alpha"],
                    {"_rauschtoleranz": {"alpha": 1.15}, "_gesperrte_bereiche": ["beta"]})
    assert r["ok"] is False
    assert "Pareto" in r["grund"] and "beta" in r["grund"]
