"""Vorbedingungen der Spezifikationsläufe: kein Netz, keine echte Datenbank (wie tests/conftest.py des Kerns)."""
import socket

import pytest


@pytest.fixture(autouse=True)
def abgeschottet(monkeypatch, tmp_path):
    monkeypatch.setenv("BIOTOP_DB", str(tmp_path / "biotop.db"))

    def gesperrt(*a, **k):
        raise AssertionError("Spezifikationslauf: Netz gesperrt")
    monkeypatch.setattr(socket.socket, "connect", gesperrt)
    monkeypatch.setattr(socket, "create_connection", gesperrt)
