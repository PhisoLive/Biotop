"""Kern: Befundklassen-Katalog — je statischer Befundklasse (Bandit-Kennung) die
bekannten Umgehungen als Immuntests. Teil des Messgeräts (nur Philipp ändert).

Regel 3.5 Fassung 2: „Behoben heißt verschwunden" — ein Sicherheitsbefund gilt
erst als behoben, wenn der statische Befund weg ist UND die Umgehung der
Befundklasse als Immuntest im Werk liegt. Diese Tests werden jedem Kandidaten
und seiner Vorgeneration paarweise mitgegeben, sobald ein Bereich einen Befund
dieser Klasse trägt. Die Tests sind werkunabhängig formuliert und werden über
eine Einstiegsfunktion (`einstieg`) an das Werk gebunden.
"""

from __future__ import annotations

KLASSEN = {
    "B307": {
        "beschreibung": "Use of possibly insecure function eval(): Eingaben werden als Python-Ausdruck ausgewertet. "
                        "Bekannte Umgehungen eines eingeschränkten eval (auch mit leeren __builtins__): Objekt-Introspektion "
                        "(().__class__.__base__.__subclasses__() erreicht ~160 Klassen inkl. BuiltinImporter → os, subprocess), "
                        "__globals__ von Funktionsobjekten, Format-String-Zugriffe auf Attribute, Ausdrucks-Explosion. "
                        "Ein Auswerter, der den Ausdruck erst ausführt und dann das Ergebnis verwirft, ist NICHT behoben — "
                        "die Nebenwirkung ist schon passiert.",
        # (name, ausdruck, nebenwirkung_marker): Ausdrücke liefern eine ZAHL, damit eine Typprüfung nach der Auswertung sie nicht rettet;
        # Ausdrücke mit Marker setzen eine Umgebungsvariable — wird sie gesetzt, wurde Code ausgeführt.
        "umgehungen": [
            ("introspektion_subclasses", "().__class__.__base__.__subclasses__().__len__()", None),
            ("introspektion_mro", "().__class__.__mro__[1].__subclasses__().__len__()", None),
            ("globals_ueber_funktion", "(lambda: 0).__globals__.__len__()", None),
            ("format_string_attribut", "'{0.__class__.__base__.__subclasses__}'.format(()).__len__()", None),
            ("import_os_ueber_klasse_nebenwirkung",
             "[c for c in ().__class__.__base__.__subclasses__() if c.__name__ == 'BuiltinImporter'][0].load_module('os').environ.setdefault('BIOTOP_UMGEHUNG_B307', 'ausgefuehrt').__len__()",
             "BIOTOP_UMGEHUNG_B307"),
            ("getattr_kette_nebenwirkung",
             "().__class__.__base__.__subclasses__().__class__.__mro__[0].__init__.__globals__.setdefault('BIOTOP_UMGEHUNG_B307_G', 1)",
             None),
        ],
    },
    "B602": {
        "beschreibung": "subprocess call with shell=True: Ein Befehl vom Aufrufer wird durch eine Shell interpretiert. Bekannte "
                        "Umgehungen einer Scheinlösung (z. B. Anführungszeichen um den Befehl, Verbotsliste einzelner Zeichen, "
                        "shlex.quote auf den GANZEN String): Verkettung mit ';' oder '&&', Kommandosubstitution $(…) und Backticks, "
                        "Umleitung '>' in Dateien, Umgebungsvariablen. Behoben heißt: keine Shell (Argumentliste, shell=False) — "
                        "ein Verkettungsversuch führt den zweiten Befehl NICHT aus und setzt keinen Nebeneffekt-Marker.",
        # Marker-Datei: der zweite Befehl legt sie an; existiert sie, wurde die Shell benutzt.
        "umgehungen": [
            ("verkettung_semikolon", "cat; touch {marker}", "{marker}"),
            ("verkettung_und", "cat && touch {marker}", "{marker}"),
            ("kommandosubstitution", "cat $(touch {marker})", "{marker}"),
            ("backticks", "cat `touch {marker}`", "{marker}"),
            ("umleitung", "cat > {marker}", "{marker}"),
        ],
        "art": "shell",
    },
    "B404": {
        "beschreibung": "import subprocess: nur Hinweis (LOW); verschwindet mit B602 nicht zwingend. Zählt 1 Punkt.",
        "umgehungen": [],
    },
    "B102": {
        "beschreibung": "Use of exec(): Eingaben werden als Python-Anweisungen ausgeführt. Umgehungen wie B307.",
        "umgehungen": [
            ("introspektion_subclasses", "().__class__.__base__.__subclasses__().__len__()", None),
            ("globals_ueber_funktion", "(lambda: 0).__globals__.__len__()", None),
        ],
    },
}


def immuntest_code(klasse: str, einstieg_import: str, einstieg_aufruf: str, fehlerklasse_import: str, fehlerklasse: str) -> str | None:
    """Erzeugt eine pytest-Datei: jede Umgehung muss mit `fehlerklasse` abgewiesen werden, OHNE ausgeführt
    worden zu sein (Nebenwirkungs-Marker bleibt ungesetzt). `einstieg_aufruf` enthält den Platzhalter {formel}."""
    k = KLASSEN.get(klasse)
    if not k or not k["umgehungen"]:
        return None
    if k.get("art") == "shell":
        return _immuntest_shell(klasse, k, einstieg_import, einstieg_aufruf)
    zeilen = [
        "# Immuntest der Befundklasse %s (Kern: biotop/kern/befundklassen.py) — bekannte Umgehungen eines eingeschraenkten eval/exec." % klasse,
        "# Jede Umgehung muss abgewiesen werden, bevor sie ausgefuehrt wird: Ergebnisse sind Zahlen (Typpruefung rettet nicht),",
        "# Nebenwirkungs-Varianten setzen eine Umgebungsvariable, die danach nicht existieren darf.",
        "import os", "import pytest", "import signal", einstieg_import, fehlerklasse_import, "",
        "def _abgewiesen(formel, marker=None):",
        "    if marker: os.environ.pop(marker, None)",
        "    def _alarm(*a): raise TimeoutError('Ausdruck nicht in 5 s abgewiesen')",
        "    signal.signal(signal.SIGALRM, _alarm); signal.alarm(5)",
        "    try:",
        "        with pytest.raises(%s):" % fehlerklasse,
        "            " + einstieg_aufruf.replace("{formel}", "formel"),
        "    finally:",
        "        signal.alarm(0)",
        "    if marker:",
        "        assert os.environ.get(marker) is None, 'Umgehung wurde AUSGEFUEHRT (Marker gesetzt) und erst danach abgewiesen'",
        "",
    ]
    for name, ausdruck, marker in k["umgehungen"]:
        zeilen.append(f"def test_umgehung_{klasse}_{name}():")
        zeilen.append(f"    _abgewiesen({ausdruck!r}, {marker!r})")
        zeilen.append("")
    return "\n".join(zeilen)


def beschreibung(klasse: str) -> str:
    k = KLASSEN.get(klasse)
    return f"{klasse}: {k['beschreibung']}" if k else f"{klasse}: (keine Katalogbeschreibung)"


def _immuntest_shell(klasse: str, k: dict, einstieg_import: str, einstieg_aufruf: str) -> str:
    """Shell-Befundklassen: `einstieg_aufruf` enthält {befehl}; jede Umgehung darf den zweiten Befehl nicht ausführen
    (Marker-Datei entsteht nicht). Ob der Aufruf eine Ausnahme wirft oder leer filtert, ist egal — nur die Nebenwirkung zählt."""
    zeilen = [
        "# Immuntest der Befundklasse %s (Kern: biotop/kern/befundklassen.py) — Shell-Verkettungen duerfen NICHT ausgefuehrt werden." % klasse,
        "import os", "import tempfile", einstieg_import, "",
        "def _nicht_ausgefuehrt(befehl_vorlage):",
        "    marker = os.path.join(tempfile.gettempdir(), 'biotop_umgehung_%s_' + str(os.getpid()))" % klasse,
        "    if os.path.exists(marker): os.remove(marker)",
        "    befehl = befehl_vorlage.replace('{marker}', marker)",
        "    try:",
        "        " + einstieg_aufruf.replace("{befehl}", "befehl"),
        "    except Exception:",
        "        pass  # Abweisen ist erlaubt; entscheidend ist, dass die Shell den zweiten Befehl nicht ausgefuehrt hat",
        "    assert not os.path.exists(marker), 'Shell-Verkettung wurde AUSGEFUEHRT (Marker-Datei entstanden): ' + befehl_vorlage",
        "",
    ]
    for name, befehl, _m in k["umgehungen"]:
        zeilen.append(f"def test_umgehung_{klasse}_{name}():")
        zeilen.append(f"    _nicht_ausgefuehrt({befehl!r})")
        zeilen.append("")
    return "\n".join(zeilen)
