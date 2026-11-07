"""Doppelprüfung der Gegenzeugen versiegelter Testwerke (Entscheidung Chat-Claude 4, 24.09.2026).

Befund der Behebungsrunden 1 und 2 vor T4: K3044 (Lauf 38) führte den versiegelten Marker von S1 nicht mehr aus — ein
Gegenzeuge, der nur die Schwäche prüft, meldete „Schwäche weg“ —, wies aber 12.206 von 12.206 Ausdrücken mit
Zeilenumbruch ab, die die Normalversion rechnet. So zählt eine neue Fehlfunktion als Behebung.

Regel: Für jedes künftige Testwerk prüft jeder Gegenzeuge zweierlei — (a) die Schwäche ist weg und (b) das gültige
Verhalten ist gegen die Normalversion unverändert. „Behoben“ nur, wenn beides gemessen ist und beides hält. Scheitert
eine gemessene Prüfung: nicht behoben. Fehlt eine Prüfung oder ist ihr Vergleich leer (und keine gemessene ist
gescheitert): nicht beurteilbar (None) — nie „behoben“.

Das Kriterium S1 des T3-Versandwerks wird dafür NICHT neu versiegelt (nach der Messung ändert man kein Kriterium). Am
T3-Werk wird die Regel nur zusätzlich angewandt und getrennt berichtet (s1_aus_messung)."""
from __future__ import annotations


def doppelurteil(schwaeche: dict | None, normal: dict | None) -> dict:
    """(a) `schwaeche`: {"verletzt": bool, …} — Ergebnis des (unveränderten) Gegenzeugen am Stand.
    (b) `normal`: {"faelle": int, "abweichungen": int, "aufschluesselung": {teil: "x von y"}} — Eingaben am Stand gegen
        die Normalversion verglichen; der Bezug steht je Teil in der Aufschlüsselung.
    Rückgabe {"behoben": True | False | None, "schwaeche_weg", "normal_unveraendert", "grund"}."""
    weg = None
    if isinstance(schwaeche, dict) and isinstance(schwaeche.get("verletzt"), bool):
        weg = not schwaeche["verletzt"]
    unv = None
    if (isinstance(normal, dict) and isinstance(normal.get("faelle"), int) and isinstance(normal.get("abweichungen"), int)
            and normal["faelle"] > 0):
        unv = normal["abweichungen"] == 0
    if weg is False or unv is False:
        behoben = False
    elif weg is None or unv is None:
        behoben = None
    else:
        behoben = True
    teile = ["Schwäche weg" if weg else "Schwäche noch da" if weg is False else "Schwäche nicht gemessen"]
    if unv is None:
        teile.append("gültiges Verhalten gegen die Normalversion nicht gemessen (oder leerer Vergleich)")
    else:
        auf = normal.get("aufschluesselung") or {}
        teile.append(f"Verhalten gegen die Normalversion {'unverändert' if unv else 'verändert'}: "
                     f"{normal['abweichungen']} Abweichung(en)"
                     + (" (" + ", ".join(f"{k} {v}" for k, v in sorted(auf.items())) + ")" if auf else
                        f" in {normal['faelle']} Fällen"))
    return {"behoben": behoben, "schwaeche_weg": weg, "normal_unveraendert": unv, "grund": "; ".join(teile)}


def torzeile_schwaechen(schwaechen: dict[str, dict], schwelle: float = 0.8) -> dict:
    """Torzeile „Schwächen“ (Tor 4, Fassung 8: ≥ 80 % der versiegelten Schwächen behoben) — Entscheidung Chat-Claude 5
    (Behebungsrunde 4 vor T4): die doppelte Gegenzeugen-Prüfung ist hier VERBINDLICH, nicht im Annahmepfad.
    `schwaechen`: {Kennung: {"schwaeche": {...}, "normal": {...}}} — je Schwäche beide Prüfungen (doppelurteil).
    Behoben zählt eine Schwäche nur mit doppelurteil True; nicht beurteilbar (eine Prüfung fehlt) zählt NICHT als
    behoben und wird eigens gezählt. Rückgabe {"behoben", "gesamt", "anteil", "erfuellt", "je_schwaeche",
    "nicht_beurteilbar", "zeile"}. Ohne Schwäche: nicht erfüllt (null Fälle sind keine Mehrheit)."""
    je = {k: doppelurteil((v or {}).get("schwaeche"), (v or {}).get("normal")) for k, v in sorted(schwaechen.items())}
    behoben = sorted(k for k, u in je.items() if u["behoben"] is True)
    offen = sorted(k for k, u in je.items() if u["behoben"] is None)
    n = len(je)
    anteil = len(behoben) / n if n else 0.0
    return {"behoben": behoben, "gesamt": n, "anteil": round(anteil, 4), "erfuellt": bool(n) and anteil >= schwelle,
            "je_schwaeche": je, "nicht_beurteilbar": offen,
            "zeile": (f"Schwächen: {len(behoben)} von {n} behoben nach doppelter Prüfung (Schwäche weg UND Verhalten gegen "
                      f"die Normalversion unverändert) = {anteil * 100:.0f} %, Schwelle {schwelle * 100:.0f} % — "
                      f"{'erfüllt' if bool(n) and anteil >= schwelle else 'nicht erfüllt'}"
                      + (f"; nicht beurteilbar: {', '.join(offen)}" if offen else ""))}


def s1_aus_messung(e: dict) -> tuple[dict, dict]:
    """S1 des T3-Versandwerks aus einer Messung mit s1_harness.mjs (Stand gegen Normalversion) → (schwaeche, normal).
    Dieselben Größen wie das Kriterium der Behebungsrunde 2 (S1_sauber_nach_entscheidung), keine neue Einteilung:
    (a) Marker 0-mal ausgeführt; (b) Leerzeichen-Korpus K: Stand ≠ Normalversion (Bezug: ALLE Fälle von K — der Harness
    zählt neu_ungleich_norm über jeden Fall, gültig oder nicht) und Weißraum-Korpus W je Trenner: der Stand weist ab, was
    Vorgeneration und Normalversion rechnen (Bezug: Ausdrücke, die die Normalversion rechnet)."""
    K, W = e["K"], e["W"]
    schwaeche = {"verletzt": int(e["marker_neu_gesamt"]) > 0, "marker": int(e["marker_neu_gesamt"])}
    auf = {"leerzeichen": [int(K["neu_ungleich_norm"]), int(K["faelle"])]}
    for w, v in sorted(W.items()):
        auf[w] = [int(v["neu_weist_ab_alt_und_norm_zahl"]), int(v["norm_zahl"])]
    return schwaeche, {"faelle": sum(b for _, b in auf.values()), "abweichungen": sum(a for a, _ in auf.values()),
                       "aufschluesselung": {k: f"{a} von {b}" for k, (a, b) in auf.items()}}
