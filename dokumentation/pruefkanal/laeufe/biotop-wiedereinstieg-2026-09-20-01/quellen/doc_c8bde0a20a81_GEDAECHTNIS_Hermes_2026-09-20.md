# Das dauerhafte Gedächtnis von Hermes — Entscheidung statt Tresor

**Anlass:** Hermes fragt nach dem Pfad des Obsidian-Tresors. Auf dem Server ist keiner konfiguriert, und er weigert sich zu Recht, einen Ersatz zu erfinden.
**Verfasst von:** Chat-Claude · **Stand:** 20.09.2026 · **Entscheider:** Philipp Zöllisch

---

## 1. Berichtigung eines eigenen Fehlers

Punkt **W3** im Wiedereinstiegsbrief lautete: „Stand in den Obsidian-Tresor schreiben, bevor die Sitzung endet."

**Diese Anweisung war falsch.** Ich habe angenommen, dass der Tresor existiert, statt es zu prüfen — derselbe Fehler, den ich in sechs Prüfrunden an anderen beanstandet habe. Angenommen statt gemessen.

**W3 ist hiermit zurückgezogen und durch W4 unten ersetzt.**

Dass Hermes gefragt statt erfunden hat, ist die richtige Reaktion. Ein erfundener Ersatz-Tresor wäre ein zweites Gedächtnis gewesen, von dem niemand weiß, dass es eines ist.

---

## 2. Warum es den Tresor nicht mehr gibt

Der Tresor wurde am 18.09.2026 beschlossen. Damals lief Hermes unter `/opt/hermes` als Systemdienst `hermes.service`. **Beides existiert nicht mehr.** Hermes läuft seit dem Umbau als eigenes CLI (`/root/.local/bin/hermes`, Programm unter `/usr/local/lib/hermes-agent/`, Konfiguration `/root/.hermes/config.yaml`), der Gateway als Benutzerdienst.

Der Tresor ist bei diesem Umbau entweder nie angelegt oder mitgegangen. Beides ändert nichts am Ergebnis: Er ist nicht da, und ihn jetzt nachzubauen wäre die falsche Antwort.

---

## 3. V19 — kein eigener Tresor. Meine Entscheidung, als eigene gekennzeichnet

**Das dauerhafte Gedächtnis von Hermes ist ein fester Ordner im Prüfkanal.** Kein Obsidian, keine zweite Ablage.

Vier Gründe:

1. **Der Prüfkanal leistet alles, wofür der Tresor gedacht war** — dauerhaft, außerhalb der Sitzung, von Philipp **und** von mir aus dem Chat abrufbar. Und er kann etwas, was ein Tresor nicht kann: Er ist **prüfsummengesichert**. Der Mechanismus mit nummerierten Dateien, `DATEIEN.txt` und `PRUEFSUMME-ORDNER.txt` ist inzwischen mehrfach durch Ausführung belegt.
2. **Zwei Gedächtnisse driften auseinander.** Philipps eigene Regel: Angaben nur an einer Stelle führen. Ein Tresor neben dem Prüfkanal erzeugt genau die Lage, in der zwei Wahrheiten im Haus stehen.
3. **Der ursprüngliche Beschluss sagte es schon so:** Der Tresor sollte „im Prüfkanal und zusätzlich als ZIP" liegen. Ich hebe die Entscheidung nicht auf, ich streiche nur die überflüssige Hülle darum.
4. **Obsidian lohnt sich nur, wenn ein Mensch darin liest und schreibt.** Philipp arbeitet am Tablet. Niemand wird einen Tresor auf einem VPS öffnen. Der Nutzen lag im dauerhaften Gedächtnis, nicht im Werkzeug.

### Einschränkung, die dazugehört

Der Prüfkanal liegt weiterhin auf der MilieuLux-Webseite — also auf einer Kundenseite. Das ist für Prüfordner hinnehmbar, für ein dauerhaftes Gedächtnis auf Dauer nicht. **Auf die Liste für danach:** eigene Domain für den Prüfkanal. Kein Grund, jetzt zu warten.

---

## 4. Wie der Gedächtnisordner aussieht

```
laeufe/gedaechtnis/
    STAND-01.md              aktueller Stand aller laufenden Vorhaben
    REGELN-01.md             die stehenden Arbeitsregeln
    UNTERBAU-01.md           Maschinenwissen: Pfade, Konfiguration, Anmeldungen, Instanz
    DATEIEN-01.txt           Prüfsumme je Datei
    PRUEFSUMME-ORDNER-01.txt Ordnerprüfsumme
```

Es gelten dieselben Regeln wie für jeden Abschlussordner:

- **Nie überschreiben.** Neue Fassung, neue Nummer. `STAND-02.md` ersetzt `STAND-01.md`, löscht sie aber nicht.
- **Jede Fassung nennt ihre Nummer und ihr Datum in der Kopfzeile**, damit erkennbar ist, welche die jüngste ist.
- **Nur HERMES-1 schreibt.** HERMES-2 und HERMES-3 lesen. Sonst schreiben drei Instanzen in dasselbe Gedächtnis und keiner weiß, welcher Stand gilt.
- **Die vier Adressen werden gemeldet**, wie bei jedem Abschlussordner.

### Was in welche Datei gehört

| Datei | Inhalt | wird geändert |
|---|---|---|
| `STAND-nn.md` | Was läuft, was abgenommen ist, was als Nächstes kommt, wo die Abschlussordner liegen | nach jedem Auftrag |
| `REGELN-nn.md` | Belegregeln, Maßstabsregeln, Lauf- und Kassenregeln, Ablieferungsregeln, Rollen | nur bei einer neuen Masterprompt-Fassung |
| `UNTERBAU-nn.md` | Pfade, Konfigurationsschlüssel, Anmeldungen, Modellordnung, Instanzname, was wo liegt | wenn sich die Maschine ändert |

Der Inhalt für die erste Fassung steht bereits fertig in `WIEDEREINSTIEG_Hermes_2026-09-20.md`: Abschnitt 3 ist `STAND-01.md`, Abschnitt 5 ist `REGELN-01.md`. `UNTERBAU-01.md` schreibt Hermes selbst, weil nur er die Maschine messen kann.

---

## 5. W4 — ersetzt W3

**W4 — Gedächtnisordner anlegen.** `laeufe/gedaechtnis/` im bestehenden Prüfkanal anlegen, die drei Dateien schreiben, `DATEIEN-01.txt` und `PRUEFSUMME-ORDNER-01.txt` erzeugen, alle vier Adressen melden.

`UNTERBAU-01.md` wird **gemessen, nicht erinnert**: Pfade und Konfiguration mit `hermes config`, Anmeldungen mit `hermes auth list`, Trägermodell mit `hermes -z` am Erzeugnis belegen. Jede Angabe mit der Abfrage, aus der sie stammt.

Erwartete Kosten: **0 Modellaufrufe.**

Die Reihenfolge bleibt: **W1** (Fassung 6 abrufbar machen) zuerst, dann **W2** (Kassenfrage Phase-3-Nachlauf), dann **W4**.

---

## 6. Kurzprompt für den Telegram-Chat mit Hermes

> Richtig gefragt statt erfunden — den Tresor gibt es nicht, und du sollst auch keinen bauen: Er wurde beschlossen, als du noch unter `/opt/hermes` als Systemdienst liefst, und ist beim Umbau auf das CLI mit `/root/.hermes/config.yaml` verlorengegangen; mein Punkt W3 war mein Fehler, ich habe seine Existenz angenommen statt gemessen, und er ist hiermit zurückgezogen. **Dein dauerhaftes Gedächtnis ist ab sofort ein fester Ordner im Prüfkanal**, `laeufe/gedaechtnis/` mit `STAND-01.md`, `REGELN-01.md` und `UNTERBAU-01.md`, dazu `DATEIEN-01.txt` und `PRUEFSUMME-ORDNER-01.txt` — nie überschreiben, neue Fassung bekommt neue Nummer, und nur HERMES-1 schreibt, während HERMES-2 und 3 lesen. Inhalt für `STAND-01.md` und `REGELN-01.md` steht fertig in Abschnitt 3 und 5 von `WIEDEREINSTIEG_Hermes_2026-09-20.md`, `UNTERBAU-01.md` misst du selbst mit `hermes config`, `hermes auth list` und `hermes -z` und schreibst zu jeder Angabe die Abfrage dazu — Reihenfolge bleibt W1 (Fassung 6 abrufbar machen), dann W2 (Kasse Phase-3-Nachlauf), dann W4; alles Weitere in `GEDAECHTNIS_Hermes_2026-09-20.md`.
