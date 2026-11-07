"""Anbieterschicht: ein Port, mehrere Adapter.

Jeder Aufruf geht durch `aufrufen()`, das die Kasse VOR dem Aufruf fragt
(Verfassungssatz 8) und NACH dem Aufruf die tatsächlichen Token bucht und
protokolliert. Es gibt keinen anderen Weg zu einem Modell.
"""

from __future__ import annotations

import json
import os
import sqlite3
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from ..kern import kasse, protokoll


@dataclass
class Antwort:
    text: str
    tokens_ein: int
    tokens_aus: int
    modell: str
    anbieter: str
    kosten_eur: float
    protokoll_nr: int


class AnbieterFehler(RuntimeError):
    pass


def _schluessel(name: str) -> str:
    v = os.environ.get(name)
    if v:
        return v
    env = Path("/root/.hermes/.env")
    if env.exists():
        for zeile in env.read_text().splitlines():
            if zeile.startswith(name + "="):
                return zeile.split("=", 1)[1].strip().strip('"').strip("'")
    raise AnbieterFehler(f"{name} nicht gesetzt")


def _tokens_schaetzen(text: str) -> int:
    return max(1, len(text) // 3)


class OpenRouterAdapter:
    """Tokenabgerechnete Schnellmodelle. Hersteller steckt im Modellnamen."""

    name = "openrouter"
    url = "https://openrouter.ai/api/v1/chat/completions"

    def __init__(self) -> None:
        self.key = _schluessel("OPENROUTER_API_KEY")

    def hersteller(self, modell: str) -> str:
        return modell.split("/", 1)[0]

    def senden(self, modell: str, system: str, nutzer: str, max_tokens: int,
               temperatur: float) -> tuple[str, int, int]:
        body = {
            "model": modell,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": nutzer}],
            "max_tokens": max_tokens,
            "temperature": temperatur,
            "usage": {"include": True},
        }
        # Schnellmodelle mit eingebautem Denken (deepseek/qwen) würden sonst das Token-Budget mit Denk-Token
        # füllen und leere Antworten liefern (gemessen 19.09.2026, ausgaben/01-modellwahl-rauchtest.txt).
        # gemini-3.x lehnt das Abschalten ab („Reasoning is mandatory“, HTTP 400, gemessen 19.09.2026) → dort minimaler Aufwand.
        if modell.startswith("google/gemini-3"):
            body["reasoning"] = {"effort": "minimal"}
        else:
            # auch das schwere Modell: Denk-Token würden bei langen JSON-Antworten das Ausgabebudget aufbrauchen
            # (Mentor Lauf 16: 3000 Token aus, 0 Zeichen Text, gemessen 19.09.2026, Protokoll #7558)
            body["reasoning"] = {"enabled": False}
        req = urllib.request.Request(
            self.url, data=json.dumps(body).encode(),
            headers={"Authorization": f"Bearer {self.key}", "Content-Type": "application/json",
                     "HTTP-Referer": "https://biotop.local", "X-Title": "Biotop Phase 1"},
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                d = json.load(r)
        except urllib.error.HTTPError as e:
            raise AnbieterFehler(f"{modell}: HTTP {e.code} {e.read()[:300]!r}") from e
        except Exception as e:  # noqa: BLE001
            raise AnbieterFehler(f"{modell}: {e}") from e
        if "error" in d:
            raise AnbieterFehler(f"{modell}: {d['error']}")
        text = d["choices"][0]["message"]["content"] or ""
        u = d.get("usage") or {}
        return text, int(u.get("prompt_tokens", 0)), int(u.get("completion_tokens", 0))


_ADAPTER: dict[str, OpenRouterAdapter] = {}


def adapter(name: str) -> OpenRouterAdapter:
    if name not in _ADAPTER:
        if name == "openrouter":
            _ADAPTER[name] = OpenRouterAdapter()
        else:
            raise AnbieterFehler(f"unbekannter Anbieter {name}")
    return _ADAPTER[name]


def aufrufen(
    con: sqlite3.Connection, lauf_id: int, anbieter: str, modell: str, system: str,
    nutzer: str, zweck: str, max_tokens: int = 4000, temperatur: float = 0.2,
) -> Antwort:
    """Einziger Weg zu einem Modell. Kasse vor dem Aufruf, Buchung danach."""
    ad = adapter(anbieter)
    geschaetzt = _tokens_schaetzen(system + nutzer)
    schaetzung = kasse.vorpruefung(con, lauf_id, modell, geschaetzt, max_tokens, zweck)
    nr = protokoll.schreiben(
        con, "modell.aufruf", lauf_id=lauf_id, anbieter=anbieter, modell=modell,
        zweck=zweck, tokens_ein_geschaetzt=geschaetzt, max_tokens=max_tokens,
        schaetzung_eur=round(schaetzung, 6), temperatur=temperatur,
    )
    try:
        text, t_ein, t_aus = ad.senden(modell, system, nutzer, max_tokens, temperatur)
    except AnbieterFehler as e:
        protokoll.schreiben(con, "modell.fehler", lauf_id=lauf_id, modell=modell, fehler=str(e), aufruf_nr=nr)
        raise
    k = kasse.buchen(con, lauf_id, anbieter, modell, t_ein, t_aus, zweck, nr)
    protokoll.schreiben(
        con, "modell.antwort", lauf_id=lauf_id, modell=modell, aufruf_nr=nr,
        tokens_ein=t_ein, tokens_aus=t_aus, kosten_eur=round(k, 6), zeichen=len(text),
    )
    return Antwort(text, t_ein, t_aus, modell, anbieter, k, nr)
