"""CLI-Gate-Tests. Erfolgsfall = kontrollierter Unit-Test, keine echte Eichung."""
import json
import os
from pathlib import Path
import subprocess
import sys

import pytest
from biotop import __main__ as cli
from biotop import lauf as L
from biotop.kern.datenbank import lj
from test_vorspann import unit_vorspann


def test_unit_cli_vorspann_fuehrt_denselben_kernpfad_aus(unit_vorspann, monkeypatch, capsys):
    con, raw = unit_vorspann
    monkeypatch.setattr(cli, 'verbinden', lambda:con)
    assert cli.main(['vorspann','1']) == 0
    aus = json.loads(capsys.readouterr().out)
    assert aus['qualitaet'] == {'positive':4,'negative':4,'erwartet_je':4}
    assert raw['reihenfolge'] == ['rauschen','gegenstand','funde','proben']
    assert L.vorspann.verlangen(con,1,'gen0')['nachweis_sha256'] == aus['nachweis_sha256']


def _subprozess(tmp_path, con, argv):
    root = Path(L.__file__).resolve().parents[1]
    db = con.execute('PRAGMA database_list').fetchone()[2]
    # Netzsperre gilt auch im echten CLI-Kindprozess, nicht nur im pytest-Elternprozess.
    shim = tmp_path / 'netzschutz'; shim.mkdir(exist_ok=True)
    (shim / 'sitecustomize.py').write_text('import socket\ndef gesperrt(*a,**k):\n    raise AssertionError("Eigen-Test: Netz/Kammer gesperrt")\nsocket.socket.connect=gesperrt\nsocket.create_connection=gesperrt\nfrom biotop.organe import kammer\nkammer.ausfuehren=gesperrt\n')
    child_tmp = tmp_path.parent / (tmp_path.name + '-child-tmp')
    child_tmp.mkdir(exist_ok=True)
    env = dict(os.environ, PYTHONPATH=os.pathsep.join([str(shim),str(root)]), TMPDIR=str(child_tmp),
               BIOTOP_DB=db, PYTHONDONTWRITEBYTECODE='1')
    return subprocess.run([sys.executable,*argv],env=env,cwd=root,capture_output=True,text=True,timeout=30)


@pytest.mark.parametrize('cmd', [['vorspann','1'],['gen0','1'],['mass','1','--bestaetigt-von','Unit'],['generation','1']])
def test_cli_sperre_hat_exit_eins_und_keine_modellkosten(db_lauf,tmp_path,cmd):
    p = _subprozess(tmp_path, db_lauf, ['-m','biotop',*cmd])
    assert p.returncode == 1, p.stdout+p.stderr
    assert 'Vorspann' in p.stderr
    assert db_lauf.execute('SELECT count(*) FROM kasse').fetchone()[0] == 0
    assert db_lauf.execute('SELECT count(*) FROM generationen WHERE nummer>0').fetchone()[0] == 0


def test_pruefskript_ist_wrapper_mit_fehlerexit_und_rohdaten(db_lauf,tmp_path):
    out = tmp_path / 'ausgaben'
    p = _subprozess(tmp_path,db_lauf,['pruefung/vorspann.py',str(out),'1'])
    assert p.returncode == 1, p.stdout+p.stderr
    assert 'Vorspann' in p.stderr
    assert 'Vorspann' in (out/'15-vorspann-lauf1.txt').read_text()
    e = db_lauf.execute("SELECT inhalt FROM protokoll WHERE art='vorspann.gescheitert'").fetchone()
    assert e and lj(e[0])['ergebnis']['generation'] == -1
