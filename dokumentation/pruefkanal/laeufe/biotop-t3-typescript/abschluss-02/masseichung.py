"""Maßeichung: Prüferregeln am sauberen Vergleichsbereich messen, bevor sie zählen.

Befund aus Lauf 37 (T3, TypeScript): Der Bereich `zahlen` ist laut Verfassung der
saubere Vergleichsbereich — die versiegelte Bauakte nennt dort keine Schwäche. Die
ESLint-Regel `security/detect-object-injection` meldete dort trotzdem acht Punkte,
weil sie jeden Array-Zugriff mit variablem Index meldet, unabhängig von dessen
Herkunft. Der Schwarm „behob" sie mit `arr[i]` → `arr.at(i)`: in der Kammer gemessen
identisches Verhalten, Tests unverändert 29/29 — und gewann dafür 7 Kernmaßpunkte.

Das ist keine Verbesserung des Werks, sondern eine Optimierung der Messung. Genau das
soll die Halluzinationsprobe fangen, und sie hat es gefangen.

Die Abhilfe ist dieselbe Figur wie die Rauschmessung, eine Ebene höher angewandt: Die
Rauschmessung misst das Messgerät am unveränderten Werk, bevor sie Laufzeiten bewertet.
Die Maßeichung misst jede Prüferregel am sauberen Bereich, bevor sie Punkte bewertet.
Schlägt eine Regel dort an, wo laut Verfassung nichts ist, ist sie für dieses Werk kein
Maß — sie wird stillgelegt und zählt nicht zum Kernmaß.

Stillgelegt heißt nicht abgeschaltet: Die Befunde bleiben in der Messung sichtbar und im
Bericht, sie tragen nur keine Punkte. Wer eine stillgelegte Regel für echt hält, muss den
Vergleichsbereich in der Verfassung korrigieren — nicht die Regel.
"""
from __future__ import annotations


class MasseichungFehler(RuntimeError):
    """Der genannte Vergleichsbereich existiert nicht — kein stilles Weiterlaufen."""


def eichen(messung: dict, sauberer_bereich: str | None) -> dict:
    """Misst jede Prüferregel am sauberen Bereich. Rückgabe: Eichung mit Nenner.

    `sauberer_bereich` kommt aus der Verfassung (regeln.sauberer_bereich). Fehlt er,
    wird nichts stillgelegt: ohne benannten Vergleichsbereich gibt es keinen Maßstab,
    und geraten wird nicht.
    """
    bereiche = messung.get("bereiche") or {}
    alle_regeln = {x["test"] for b in bereiche.values() for x in (b.get("sicherheit_befunde") or [])}

    if sauberer_bereich is None:
        return {"sauberer_bereich": None, "stillgelegt": [], "gemessen": sorted(alle_regeln),
                "funde_im_sauberen": {}, "regeln_geprueft": len(alle_regeln),
                "regeln_stillgelegt": 0, "begruendung": {},
                "hinweis": "kein sauberer Bereich in der Verfassung benannt — jede Regel zählt"}

    if sauberer_bereich not in bereiche:
        raise MasseichungFehler(
            f"Vergleichsbereich '{sauberer_bereich}' ist nicht im Werk "
            f"(vorhanden: {sorted(bereiche)}). Eine Maßeichung gegen einen Bereich, den es "
            f"nicht gibt, meldet null Fehlalarme und ist damit eine leere Prüfung.")

    funde: dict[str, int] = {}
    for x in (bereiche[sauberer_bereich].get("sicherheit_befunde") or []):
        funde[x["test"]] = funde.get(x["test"], 0) + 1

    stillgelegt = sorted(funde)
    begruendung = {
        r: (f"schlägt im sauberen Vergleichsbereich '{sauberer_bereich}' {n}× an, wo die "
            f"Verfassung keine Schwäche nennt — für dieses Werk kein Maß")
        for r, n in sorted(funde.items())}
    return {"sauberer_bereich": sauberer_bereich, "stillgelegt": stillgelegt,
            "gemessen": sorted(alle_regeln - set(stillgelegt)), "funde_im_sauberen": funde,
            "regeln_geprueft": len(alle_regeln), "regeln_stillgelegt": len(stillgelegt),
            "begruendung": begruendung}


def sicherheit_bereinigt(bereich_messung: dict, eichung: dict) -> int:
    """Sicherheitspunkte eines Bereichs ohne stillgelegte Regeln."""
    still = set(eichung.get("stillgelegt") or [])
    return sum(x["punkte"] for x in (bereich_messung.get("sicherheit_befunde") or [])
               if x["test"] not in still)


def kernmass_bereinigt(messung: dict, eichung: dict) -> int:
    """Kernmaß F2 ohne die Punkte stillgelegter Regeln. Höchstwert 0."""
    summe = 0
    for b in (messung.get("bereiche") or {}).values():
        summe += (b.get("tests_fehlgeschlagen", 0)
                  + sicherheit_bereinigt(b, eichung)
                  + b.get("tote_funktionen", 0))
    return -summe


def bericht(eichung: dict) -> list[str]:
    """Zeilen für den Abschlussbericht."""
    if eichung.get("sauberer_bereich") is None:
        return ["  Maßeichung: kein Vergleichsbereich benannt, jede Regel zählt"]
    z = [f"  Maßeichung am sauberen Bereich '{eichung['sauberer_bereich']}': "
         f"{eichung['regeln_stillgelegt']} von {eichung['regeln_geprueft']} Regeln stillgelegt"]
    for r, n in sorted((eichung.get("funde_im_sauberen") or {}).items()):
        z.append(f"      {r}: {n} Fund(e) im sauberen Bereich → zählt nicht zum Kernmaß")
    return z
