"""Controlled gate consumer, not real calibration/mutation measurement."""
import json
from pathlib import Path
import pytest
from biotop import lauf as L
from biotop.organe import generation0 as G0, vorspann as V
from test_vorspann import unit_vorspann
from conftest import db_lauf, messung, keine_bezahlten_aufrufe
ROOT=Path(__file__).resolve().parent

@pytest.mark.parametrize('valid',[False,True])
def test_battery_validity_controls_actual_gen0_entry(unit_vorspann,monkeypatch,valid):
    con,raw=unit_vorspann
    entered=[]
    def generate(*a):
        entered.append('generate')
        return [{'quelle':'review-unit','datei':'paket/alpha/__init__.py','zeile':1,'beschreibung':'controlled non-equivalent mutant'}]
    monkeypatch.setattr(G0,'erzeugen',generate)
    monkeypatch.setattr(G0,'aequivalenz_pruefen',lambda *a:None)
    monkeypatch.setattr(G0,'messen',lambda *a: {'nicht_aequivalent':1,'gefangen':1,'blind':[]})
    def forbidden(*a,**kw):
        pytest.fail('No model test evolution permitted in review')
    monkeypatch.setattr(G0,'tests_evolutionieren',forbidden)
    if not valid: raw['proben']['gegenproben']['vertrag']['pruefbar']=False
    if valid:
        proof=V.ausfuehren(con,1)
        result=L.generation0(con,1,None,.8)
        assert result['erreicht'] is True
        assert entered==['generate']
        assert L._lauf(con,1)['mass'] is None
    else:
        with pytest.raises(V.VorspannFehler): V.ausfuehren(con,1)
        with pytest.raises(L.LaufFehler): L.generation0(con,1,None,.8)
        assert entered==[]
        proof=result=None
    row=dict(valid_battery=valid,entered=entered,proof_hash=proof['nachweis_sha256'] if proof else None,
             gen0=result,boundary='real gate, proof hashing/protocol/DB and gen0 entry; calibration, infrastructure and mutant measurement explicitly doubled; no Freeze')
    (ROOT/f'gen0-route-{valid}.json').write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(row,ensure_ascii=False))
