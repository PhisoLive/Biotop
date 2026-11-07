"""Rauschregeln: ein Messwert ist bereits ein Median, nicht ein Einzelaufruf."""
import pytest
from biotop.kern import messgeraet as M
from biotop.organe import eichung
from pathlib import Path


@pytest.mark.parametrize("anzahl", [0, 1, 2, 3, 4, 6])
def test_rauschmessung_braucht_genau_fuenf_werte(anzahl):
    r = M.rauschtoleranz_aus_werten([100.0] * anzahl)
    assert r["nachmessen"] is True
    assert r["meldung"]


@pytest.mark.parametrize("wert", [0, -1, float("nan"), float("inf"), -float("inf"), True])
def test_ungueltige_rauschwerte_sind_keine_toleranz(wert):
    with pytest.raises(ValueError, match="endlich|positiv"):
        M.rauschtoleranz_aus_werten([100.0, 100.0, 100.0, 100.0, wert])


def test_aussetzer_wird_ungekuerzt_entfernt_und_einmal_ersetzt(db_lauf, monkeypatch):
    werte = iter([1., 1., 1., 1., 9.8765, 1.])
    aufrufe = []
    def messen(*args):
        aufrufe.append(True)
        return {"alpha": next(werte)}
    monkeypatch.setattr(eichung, "_messen_einmal", messen)
    r = eichung.rauschmessung(db_lauf, 1, 1, Path("."), ["alpha"], "paket", "# Last")
    assert len(aufrufe) == 6
    assert r["lauf_startet"] is True
    assert r["bereiche"]["alpha"]["nachgemessen"] is True
    assert r["bereiche"]["alpha"]["werte"] == [1., 1., 1., 1., 1.]


@pytest.mark.parametrize("ersatz", [9.8765, None])
def test_gescheitertes_nachmessen_sperrt_den_bereich(db_lauf, monkeypatch, ersatz):
    werte = iter([1., 1., 1., 1., 9.8765, ersatz])
    aufrufe = []
    def messen(*args):
        aufrufe.append(True)
        return {"alpha": next(werte)}
    monkeypatch.setattr(eichung, "_messen_einmal", messen)
    r = eichung.rauschmessung(db_lauf, 1, 1, Path("."), ["alpha"], "paket", "# Last")
    assert r["lauf_startet"] is False
    assert r["gesperrt"] == ["alpha"]
    assert r["toleranz"] == {}
    assert len(aufrufe) == 6


@pytest.mark.parametrize("laufzeit,toleranz,erwartet", [(118., 1.2, True), (118., 1.15, False),
                                                     (120., 1.2, True), (120.01, 1.2, False)])
def test_urteil_verwendet_gemessene_statt_fester_rauschtoleranz(messung, laufzeit, toleranz, erwartet):
    basis, kandidat = messung(), messung()
    kandidat["bereiche"]["alpha"]["laufzeit_ms"] = laufzeit
    kandidat["bereiche"]["beta"]["laufzeit_ms"] = 80.
    r = M.urteil_f2(basis, kandidat, basis, ["alpha", "beta"], ["beta"],
                    {"_rauschtoleranz": {"alpha": toleranz, "beta": 1.15}}, nische="schnell")
    assert r["ok"] is erwartet


@pytest.mark.parametrize("wirkungskreis,erwartet", [(["alpha"], True), (["alpha", "beta"], False)])
def test_rauschsperre_wirkt_nur_auf_betroffenen_wirkungskreis(messung, wirkungskreis, erwartet):
    basis, kandidat = messung(tote_funktionen=1), messung(tote_funktionen=1)
    kandidat["bereiche"]["alpha"]["tote_funktionen"] = 0
    kandidat["bereiche"]["beta"]["laufzeit_ms"] = 10000.
    r = M.urteil_f2(basis, kandidat, basis, ["alpha", "beta"], wirkungskreis,
                    {"_rauschtoleranz": {"alpha": 1.15}, "_gesperrte_bereiche": ["beta"]})
    assert r["ok"] is erwartet
    if not erwartet:
        assert "gesperrt" in r["grund"] and "beta" in r["grund"]


def test_streuung_verbietet_innerhalb_einer_messung():
    with pytest.raises(ValueError, match="zwischen Messungen"):
        M.streuung([1., 2., 3.], ebene="innerhalb")


def test_streuung_trim_mt_zwischen_fuenf_medianen():
    r = M.streuung([1., 2., 2., 3., 9.])
    assert r["spannweite"] == (3. - 2.) / 2.
    assert r["median"] == 2.
    assert r["getrimmt"] == 2
    assert r["n"] == 5


@pytest.mark.parametrize("werte", [[], [100.]])
def test_zu_wenige_messungen_sind_nicht_streuung_null(werte):
    assert M.streuung(werte)["spannweite"] is None


@pytest.mark.parametrize("werte,toleranz,meldet", [
    ([100., 100., 100., 100., 100.], 1.15, False),
    ([100., 100., 120., 140., 140.], 1.5, False),
    ([100., 100., 120., 150., 150.], 1.6, True),
    ([100., 100., 150., 300., 300.], 2.0, True),
])
def test_rauschtoleranz_boden_meldeschwelle_und_deckel(werte, toleranz, meldet):
    r = M.rauschtoleranz_aus_werten(werte)
    assert r["toleranz"] == toleranz
    assert bool(r["meldung"]) is meldet


@pytest.mark.parametrize("hoch,erwartet", [(500., []), (501., [501.])])
def test_aussetzer_erst_ueber_fuenffachem_median(hoch, erwartet):
    r = M.rauschtoleranz_aus_werten([100., 100., 100., 100., hoch])
    assert r["aussetzer"] == erwartet
    assert r["nachmessen"] is bool(erwartet)
