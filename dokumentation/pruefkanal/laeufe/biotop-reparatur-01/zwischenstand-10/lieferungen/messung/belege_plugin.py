"""Nur Belegtreiber: zählt echte Kammeraufrufe aller ausgewählten Eigen-Tests."""
import hashlib
import json
import os
from pathlib import Path

import pytest
from biotop.organe import kammer


@pytest.fixture(autouse=True)
def alle_kammerbelege(request):
    with kammer.zaehlung() as aufrufe:
        yield
    ziel = Path(os.environ["KAMMER_GESAMT"])
    ziel.mkdir(parents=True, exist_ok=True)
    name = hashlib.sha256(request.node.nodeid.encode()).hexdigest()
    (ziel / (name + ".json")).write_text(json.dumps({"nodeid": request.node.nodeid, "kammer": aufrufe}, indent=2))
