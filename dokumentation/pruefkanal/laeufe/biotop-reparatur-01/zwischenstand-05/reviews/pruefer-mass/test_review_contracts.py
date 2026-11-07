"""Reviewer acceptance checks: two demonstrated defects, paired with valid controls."""
import pytest
from repro_negotiation import run
from repro_mass import invalid_area


def test_negotiated_adaptation_must_block_its_blocked_dependents():
    r = run(['gamma'])
    assert 'gamma' in r['actual_adaptation_scope']
    assert r['generation']['status'] == 'abgelehnt', r['generation']['grund']
    assert r['beta_before'] == r['beta_after']


def test_control_directly_blocked_partner_is_rejected():
    r = run(['beta','gamma'])
    assert r['generation']['status'] == 'abgelehnt'
    assert r['beta_before'] == r['beta_after']


@pytest.mark.parametrize('bad', [0.0,float('nan')])
def test_invalid_area_must_not_discard_valid_other_area(bad):
    r = invalid_area(bad)
    assert 'exception' not in r, r.get('exception')
    assert r['result']['gesperrt'] == ['alpha']
    assert r['result']['toleranz'] == {'beta':1.15}
    assert r['result']['lauf_startet'] is True


def test_control_missing_area_does_preserve_valid_other_area():
    r = invalid_area(None)
    assert 'exception' not in r
    assert r['result']['gesperrt'] == ['alpha']
    assert r['result']['toleranz'] == {'beta':1.15}
    assert r['result']['lauf_startet'] is True
