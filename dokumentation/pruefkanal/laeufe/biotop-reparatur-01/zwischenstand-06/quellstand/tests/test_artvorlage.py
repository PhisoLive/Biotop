"""Gestellte Vorlagenfälle; echte Bestandsmessung liegt separat im Replay."""
import json
import re
import sqlite3

import pytest

from biotop.kern import datenbank
from biotop.organe import gedaechtnis as g


@pytest.fixture
def con():
    c = sqlite3.connect(":memory:", isolation_level=None)
    c.row_factory = sqlite3.Row
    c.executescript(datenbank.SCHEMA)
    g.tabellen(c)
    c.execute("INSERT INTO werke(id,bericht,sprache) VALUES(1,?,'Python')", (json.dumps({"paket": "eigen"}),))
    yield c
    c.close()


def eintraege(con, werk, anzahl):
    ids = []
    for i in range(anzahl):
        cur = con.execute("INSERT INTO artgedaechtnis(werk,werkklasse,lauf_id,generation,bereich,nische,kategorie,ergebnis,zuwachs,beschreibung,muster) VALUES(?,'python/klein/bibliothek',1,1,'b','n','sonst','angenommen',1,'Instanz',?)",
                          (werk, f"Übertragbares Muster {werk} {i}"))
        ids.append(cur.lastrowid)
    return ids


def gezeigt(con):
    text = g.art_text(con, 1)
    ids = [int(i) for i in re.findall(r"\[A(\d+)\]", text)]
    rows = [con.execute("SELECT * FROM artgedaechtnis WHERE id=?", (i,)).fetchone() for i in ids]
    return [r["id"] for r in rows if r["werk"] != "eigen"], [r["id"] for r in rows if r["werk"] == "eigen"]


def test_ungerades_fenster_reserviert_mindestens_die_haelfte(con):
    eintraege(con, "eigen", 30)
    fremd_ids = eintraege(con, "fremd", 13)
    fremd, eigen = gezeigt(con)
    assert len(fremd) + len(eigen) == 25
    assert len(fremd) * 2 >= len(fremd) + len(eigen)
    assert set(fremd) == set(fremd_ids)


def test_alte_fremde_muster_bleiben_trotz_mehr_als_200_eigener_sichtbar(con):
    fremd_ids = eintraege(con, "fremd", 13)
    eintraege(con, "eigen", 220)
    fremd, eigen = gezeigt(con)
    assert set(fremd) == set(fremd_ids), "Ein Gesamtlimit vor der Fremdauswahl versteckt verfügbare Muster"
    assert len(eigen) == 12


@pytest.mark.parametrize("fremd_anzahl,eigen_anzahl", [(0,0), (0,30), (3,30), (5,30), (12,30), (13,30), (30,30), (30,0), (5,2)])
def test_mindestanteil_soweit_vorhanden_ohne_erfundene_eintraege(con, fremd_anzahl, eigen_anzahl):
    alle_ids = set(eintraege(con, "fremd", fremd_anzahl) + eintraege(con, "eigen", eigen_anzahl))
    fremd, eigen = gezeigt(con)
    gesamt = len(fremd) + len(eigen)
    assert gesamt == min(25, fremd_anzahl + eigen_anzahl)
    assert len(fremd) >= min(fremd_anzahl, max(5, (gesamt + 1) // 2))
    assert set(fremd + eigen) <= alle_ids
    assert len(set(fremd + eigen)) == gesamt


def test_deduplizierung_verbraucht_keine_plaetze_fuer_aeltere_muster(con):
    alte = eintraege(con, "fremd", 13)
    neue = eintraege(con, "fremd", 220)
    con.executemany("UPDATE artgedaechtnis SET muster='derselbe Satz' WHERE id=?", [(i,) for i in neue])
    eintraege(con, "eigen", 30)
    fremd, eigen = gezeigt(con)
    assert len(fremd) == 13
    assert len(set(fremd) & set(alte)) == 12
    assert len(eigen) == 12
