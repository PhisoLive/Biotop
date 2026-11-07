# Fehlalarm eines Sicherheitsfilters: Sperre „Gateway-Lebenszyklus“ auf Befehle ohne Bezug zum Dienstprozess

Stand 2026-09-24. Sachliche Meldung zur Einreichung beim Hersteller des Agentenrahmens. Ob sie eingereicht wird,
entscheidet der Betreiber. Keine Projektinterna: Pfade und Inhalte sind durch neutrale Platzhalter ersetzt; das
Befehlsmuster ist erhalten.

## Umgebung
- Agent läuft als Teil des Gateway-Dienstes (Chat-Anbindung) auf einem Linux-Host.
- Betroffene Werkzeuge: `terminal` (Shell-Befehl) und `execute_code` (Python-Skript).
- Der Filter blockiert Befehle mit der Begründung, sie könnten den Gateway-Prozess neu starten oder beenden.

## Beobachtung: drei Sperren an Befehlen, die keinen Gateway-Befehl enthalten

**Fall A** (Werkzeug `terminal`, 23.09.2026, Prüfagent): ein nur lesendes Shell-Skript, das Dateien listete und Zeilen
zählte. Meldung:

> Blocked: command or referenced script cannot restart, stop, or uninstall the gateway from inside the gateway process. The gateway would kill this command before it could complete (SIGTERM propagates to child processes). Run `hermes gateway restart` from a separate shell outside the running gateway.

**Fall B** (Werkzeug `terminal`, 24.09.2026). Befehlsmuster (Pfade ersetzt):

```bash
mkdir -p <ziel>/proben && cd <quelle> && for f in *.py *.json *.txt *.sh; do cp -p "$f" <ziel>/proben/; done; \
cd <ziel>/proben && ls | wc -l && for f in *; do [ "$(sha256sum < $f)" = "$(sha256sum < <quelle>/$f)" ] || echo "ABWEICHUNG $f"; done; \
echo "kopien geprueft"; <venv>/bin/python - <<'EOF'
import json, collections
from pathlib import Path
p = Path('<home>/.local/share/<werkzeugprotokoll>/log.jsonl')
zeilen = p.read_text(errors='replace').splitlines()
print('eintraege', len(zeilen))
EOF
```

Meldung: wörtlich wie in Fall A.

**Fall C** (Werkzeug `execute_code`, 24.09.2026): ein Python-Skript, das drei Textdateien im Arbeitsordner per
String-Ersetzung bearbeitet. Es enthielt keinen Prozess-, Dienst- oder Signalaufruf. Es enthielt aber als Zeichenkette
(Berichtstext) den Wortlaut der Meldung aus Fall B, also auch die Zeichenfolge `hermes gateway restart`. Meldung:

> Blocked: cannot restart or stop the gateway from inside the gateway process. The gateway would kill this script before it could complete (SIGTERM propagates to child processes). Run the lifecycle command from a shell outside the gateway.

## Was dafür spricht, dass es Fehlalarme sind
- Keiner der drei Befehle ruft `hermes gateway …`, `systemctl`, `kill`, `pkill` oder ein anderes Werkzeug zur
  Prozesssteuerung auf.
- Nach der Sperre wurden dieselben Schritte **einzeln** ausgeführt (je ein `mkdir`, `cp -p`, `cmp`, ein
  Python-Skript aus einer Datei). Keiner wurde gesperrt, und das Ergebnis war vollständig (17 von 17 Dateien
  bytegleich kopiert). Das Auszählen der Protokolldatei war dabei weggelassen und wurde nie ausgeführt.
- In Fall C ist die einzige Nähe zum Gateway eine **Zeichenkette in einem Datenliteral**, nämlich eine zitierte
  frühere Meldung.

## Vermutung (nicht geprüft)
- Fall C: Der Filter prüft den Skripttext auf die Zeichenfolge eines Lebenszyklusbefehls, auch innerhalb von
  Zeichenketten.
- Fall B: Möglicherweise wirkt die Kombination aus Heredoc, Interpreteraufruf und einem Pfad unter `~/.local/share/…`.
  Der Auslöser ist nicht bekannt.

## Wirkung
- Zweimal ist eine berechtigte Arbeit gestoppt worden, bis der Betreiber freigab.
- Der Agent umgeht Sperren nach seiner Regel nicht. Das ist richtig so, macht die Fehlalarme aber teuer.

## Bitte an den Hersteller
- Die Prüfung auf Lebenszyklusbefehle auf ausführbare Aufrufe beschränken, nicht auf Zeichenketten und Kommentare.
- Die Meldung um den auslösenden Ausschnitt ergänzen, damit Anwender den Fehlalarm belegen können, ohne zu raten.
