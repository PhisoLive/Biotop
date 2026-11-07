#!/usr/bin/env python3
"""Zwischenbericht-Wächter: legt den Zwischenbericht in den Prüfkanal, bevor das Rundenlimit einer Sitzung greift.

Regel (Philipp, 23.09.2026): „Zwischenbericht in den Prüfkanal spätestens bei 120 von 150 Aufrufen einer Sitzung —
nicht erinnern, sondern auslösen, dieselbe Lehre wie beim Verdrahtungstest.“

Was gezählt wird. Eine Werkzeugrunde ist eine Assistentennachricht mit mindestens einem Werkzeugaufruf. Gezählt wird
seit der letzten echten Nutzernachricht der Sitzung. Die Fortsetzungsnachricht nach einer Kontextverdichtung beginnt
keine neue Zählung. Genau diese Größe begrenzt agent.max_turns. Gemessen am 23.09.2026 in Sitzung
20260921_015554_e79a4a0f: 111 Runden vor der Verdichtung und 39 danach, zusammen 150, dann die Meldung „maximum number
of tool-calling iterations“.

Wann ausgelöst wird. Bei Grenze − 40 und bei Grenze − 10 Runden, also 110 und 140 bei max_turns 150. Der erste Wert
liegt bei 110 statt 120: Der Wächter läuft einmal je Minute, und der Bericht soll trotz dieses Taktverzugs
spätestens bei Runde 120 im Prüfkanal liegen. Je Schwelle und Turn wird genau einmal ausgelöst. Kindsitzungen
(source 'subagent') und Cron-Sitzungen zählen nicht.

Was ausgelöst wird. Ein NEUER Ordner, bestehende Ordner werden nie überschrieben:
    <Prüfkanal>/laeufe/<auftrag>/zwischenbericht-<JJJJMMTT-HHMMSS>-r<runden>/
Darin liegen ZWISCHENBERICHT.md, die Übergabedateien, DATEIEN.txt (volle URLs, je eine Zeile), MANIFEST.sha256 und
PRUEFSUMME-ORDNER.txt. Rechte: root:caddy, Ordner 750, Dateien 640. Danach wird jede Datei über HTTPS abgerufen und
auf Bytegleichheit geprüft.
Auftrag, Übergabedateien, Repositories und Arbeitsordner stehen in <hermes-home>/zwischenbericht/auftrag.json; der
Agent pflegt diese Datei. Fehlt sie, geht der Bericht nach laeufe/zwischenberichte/ und enthält nur den mechanischen
Stand.

Nebenwirkungen. ~/.hermes/state.db wird nur gelesen, mit mode=ro und ausdrücklich nicht mit immutable=1, weil diese
Lesung die WAL übergeht. Der Wächter ruft kein Modell auf, verschickt keine Nachricht und startet nichts neu. Bei jedem
Lauf schreibt er <hermes-home>/zwischenbericht/herzschlag.json. Daran ist belegt, dass der Zeitplan ihn wirklich
aufruft; der Elternprozess wird mitgeschrieben. Ausgaben auf stdout gibt es nur bei einer Auslösung oder einem Fehler.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

FORTSETZUNG = ('[Your active task list was preserved', '[CONTEXT COMPACTION')
GEHEIM = [re.compile(p) for p in (r'sk-or-v1-[A-Za-z0-9]{16,}', r'sk-ant-[A-Za-z0-9_\-]{16,}', r'\bsk-[A-Za-z0-9]{32,}',
                                   r'(?i)\b(api[_-]?key|passwort|password|secret)\b\s*[=:]\s*\S+')]
HASH_GRENZE = 20 * 1024 * 1024


def iso(t) -> str:
    try:
        return datetime.fromtimestamp(float(t)).astimezone().isoformat(timespec='seconds')
    except (TypeError, ValueError, OSError):
        return str(t)


def schwaerzen(text: str) -> str:
    for m in GEHEIM:
        text = m.sub('[geschwärzt]', text)
    return text


def lade(p: Path) -> dict:
    try:
        return json.loads(p.read_text())
    except (OSError, ValueError):
        return {}


def schreibe(p: Path, daten: dict) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + '.tmp')
    tmp.write_text(json.dumps(daten, ensure_ascii=False, indent=1))
    tmp.replace(p)


def grenze(home: Path) -> int:
    """agent.max_turns aus config.yaml; ohne Eintrag die Hermes-Vorgabe 500 (`hermes chat --help`)."""
    try:
        text = (home / 'config.yaml').read_text()
    except OSError:
        return 500
    block = re.search(r'^agent:[^\n]*\n((?:[ \t]+[^\n]*\n?)*)', text, re.M)
    if block:
        m = re.search(r'^[ \t]+max_turns:\s*(\d+)', block.group(1), re.M)
        if m:
            return int(m.group(1))
    return 500


def schwellen(g: int) -> list[int]:
    return sorted({max(1, g - 40), max(1, g - 10)})


def sitzungen(con, jetzt: float, fenster_s: int = 7200) -> list[dict]:
    return [dict(r) for r in con.execute(
        "SELECT id, source, last_activity_at FROM sessions WHERE ended_at IS NULL "
        "AND COALESCE(source, '') NOT IN ('subagent', 'cron') AND COALESCE(last_activity_at, 0) > ? "
        "ORDER BY last_activity_at DESC", (jetzt - fenster_s,))]


def turn_beginn(con, sid: str):
    for r in con.execute("SELECT id, content, timestamp FROM messages WHERE session_id=? AND role='user' ORDER BY id DESC", (sid,)):
        text = r['content'] if isinstance(r['content'], str) else str(r['content'] or '')
        if not text.lstrip().startswith(FORTSETZUNG):
            return r['id'], {'zeit': r['timestamp'], 'text': text}
    return None


def runden(con, sid: str, ab_id: int) -> int:
    return con.execute(
        "SELECT COUNT(*) FROM messages WHERE session_id=? AND id>? AND role='assistant' AND tool_calls IS NOT NULL "
        "AND tool_calls NOT IN ('', '[]', 'null')", (sid, ab_id)).fetchone()[0]


def ordnername(auftrag: str, jetzt: float, n: int) -> str:
    name = re.sub(r'[^A-Za-z0-9._-]', '-', auftrag or 'zwischenberichte')
    return f"laeufe/{name}/zwischenbericht-{datetime.fromtimestamp(jetzt).strftime('%Y%m%d-%H%M%S')}-r{n}"


def _befehl(args: list[str], timeout: int = 20) -> str:
    try:
        p = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return (p.stdout + p.stderr).strip()
    except (OSError, subprocess.TimeoutExpired) as e:
        return f'({type(e).__name__}: {e})'


def _dateien_seit(ordner: list[str], ausschluss: list[str], seit: float, grenze_n: int = 60) -> list[str]:
    gefunden = []
    for wurzel in ordner:
        for dirpath, dirnames, filenames in os.walk(wurzel):
            dirnames[:] = [d for d in dirnames if d not in ('.git', 'node_modules', '__pycache__')
                           and not any(str(Path(dirpath) / d).startswith(a) for a in ausschluss)]
            for f in filenames:
                p = Path(dirpath) / f
                try:
                    st = p.stat()
                except OSError:
                    continue
                if st.st_mtime >= seit:
                    gefunden.append((st.st_mtime, p, st.st_size))
    zeilen = []
    for mtime, p, groesse in sorted(gefunden, reverse=True)[:grenze_n]:
        h = hashlib.sha256(p.read_bytes()).hexdigest()[:16] if groesse <= HASH_GRENZE else '(zu groß)'
        zeilen.append(f'- {iso(mtime)}  {groesse:>10} B  sha256 {h}…  `{p}`')
    if len(gefunden) > grenze_n:
        zeilen.append(f'- … {len(gefunden) - grenze_n} weitere')
    return zeilen or ['- (keine)']


def bericht(con, sid: str, turn_id: int, turn: dict, n: int, g: int, schwelle, auftrag: dict, jetzt: float) -> str:
    z = [f"# Zwischenbericht — automatisch ausgelöst ({auftrag.get('auftrag') or 'ohne Auftragsangabe'})", '',
         f"Ausgelöst {iso(jetzt)} vom Zwischenbericht-Wächter (Cron, ohne Modell). Sitzung `{sid}`, "
         f"Werkzeugrunde **{n} von {g}** (Schwelle {schwelle}).",
         "Regel (Philipp, 23.09.2026): Zwischenbericht spätestens bei 120 von 150 Aufrufen — ausgelöst, nicht erinnert.",
         "Die Übergabedateien sind der zuletzt vom Agenten geschriebene Stand; alle übrigen Abschnitte sind in diesem "
         "Augenblick mechanisch gelesen.", '',
         f"## Auftrag dieses Turns (Nachricht {turn_id}, {iso(turn['zeit'])})", '', '```',
         schwaerzen(turn['text'])[:3000], '```', '', '## Übergabe (vom Agenten gepflegt)', '']
    for q in auftrag.get('uebergabe') or []:
        p = Path(q)
        z.append(f"- `{p}` — Stand {iso(p.stat().st_mtime)}, als eigene Datei im Ordner" if p.is_file() else f"- `{p}` — fehlt")
    if not auftrag.get('uebergabe'):
        z.append('- keine Übergabedatei eingetragen (auftrag.json fehlt oder ist leer)')
    z += ['', '## Letzte Äußerungen des Agenten in diesem Turn (neueste zuletzt)', '']
    for r in reversed(con.execute(
            "SELECT timestamp, content FROM messages WHERE session_id=? AND id>? AND role='assistant' "
            "AND content IS NOT NULL AND TRIM(content) != '' ORDER BY id DESC LIMIT 8", (sid, turn_id)).fetchall()):
        text = ' '.join(schwaerzen(str(r['content'])).split())
        z.append(f"- {iso(r['timestamp'])}: {text[:1200]}")
    z += ['', '## Repositories', '']
    for repo in auftrag.get('repos') or []:
        z += [f'`{repo}`:', '```', _befehl(['git', '-C', repo, 'log', '--oneline', '-3']),
              _befehl(['git', '-C', repo, 'status', '--short'])[:3000] or '(Arbeitsbaum sauber)', '```']
    z += ['', f"## Seit Turnbeginn geänderte Dateien (neueste zuerst)", '']
    z += _dateien_seit(auftrag.get('arbeitsordner') or [], auftrag.get('ausschluss') or [], float(turn['zeit'] or 0))
    z += ['', '## Laufende Prozesse (Auszug)', '', '```']
    ps = _befehl(['ps', '-eo', 'pid,etimes,args'])
    muster = re.compile(r'pytest|nachspiel|biotop|job\d|docker run|vitest')
    z += [zl[:200] for zl in ps.splitlines() if muster.search(zl) and 'zwischenbericht_waechter' not in zl][:20] or ['(keine)']
    z += ['```', '']
    return '\n'.join(z)


def veroeffentlichen(*, con, sid, turn_id, turn, n, g, schwelle, home, wurzel, url_basis, jetzt, https, besitzer) -> str:
    auftrag = lade(home / 'zwischenbericht' / 'auftrag.json')
    rel = ordnername(auftrag.get('auftrag') or 'zwischenberichte', jetzt, n)
    ziel = Path(wurzel) / rel
    if ziel.exists():
        raise FileExistsError(f'{ziel} existiert — gelieferte Bytes werden nicht überschrieben')
    neu_eltern = [p for p in (ziel.parent,) if not p.exists()]
    ziel.mkdir(parents=True)
    inhalte = {'ZWISCHENBERICHT.md': bericht(con, sid, turn_id, turn, n, g, schwelle, auftrag, jetzt).encode()}
    for i, q in enumerate(auftrag.get('uebergabe') or [], 1):
        p = Path(q)
        if p.is_file():
            inhalte[f'UEBERGABE-{i}-{p.name}'] = schwaerzen(p.read_text(errors='replace')).encode()
    hashes = {}
    for name, daten in inhalte.items():
        (ziel / name).write_bytes(daten)
        hashes[name] = hashlib.sha256(daten).hexdigest()
    url = f'{url_basis}/{rel}'
    dateien = ['# Zwischenbericht — Dateien (je Zeile eine vollständige Abholadresse, dahinter sha256)', '']
    dateien += [f'{url}/{name}  {hashes[name]}' for name in sorted(hashes)]
    (ziel / 'DATEIEN.txt').write_text('\n'.join(dateien) + '\n')
    hashes['DATEIEN.txt'] = hashlib.sha256((ziel / 'DATEIEN.txt').read_bytes()).hexdigest()
    manifest = ''.join(f'{h}  {name}\n' for name, h in sorted(hashes.items()))
    (ziel / 'MANIFEST.sha256').write_text(manifest)
    ordner = hashlib.sha256(manifest.encode()).hexdigest()
    (ziel / 'PRUEFSUMME-ORDNER.txt').write_text(ordner + '\n')
    if besitzer:
        for d in [ziel, *neu_eltern]:
            subprocess.run(['chown', 'root:caddy', str(d)], check=True)
            subprocess.run(['chmod', '750', str(d)], check=True)
        for p in ziel.iterdir():
            subprocess.run(['chown', 'root:caddy', str(p)], check=True)
            subprocess.run(['chmod', '640', str(p)], check=True)
    alle = sorted(hashes) + ['MANIFEST.sha256', 'PRUEFSUMME-ORDNER.txt']
    pruefung = 'HTTPS nicht geprüft (Testmodus)'
    if https:
        gleich = 0
        for name in alle:
            try:
                with urllib.request.urlopen(f'{url}/{name}', timeout=30) as r:
                    gleich += hashlib.sha256(r.read()).hexdigest() == hashlib.sha256((ziel / name).read_bytes()).hexdigest()
            except Exception:  # eine nicht abrufbare Datei zählt als nicht bytegleich
                pass
        pruefung = f'HTTPS bytegleich {gleich} von {len(alle)}'
    return (f'Zwischenbericht ausgelöst: {url}/DATEIEN.txt | Runde {n} von {g} (Schwelle {schwelle}) | {pruefung} | '
            f'Ordnerprüfsumme {ordner}')


def main(argv=None) -> int:
    home_std = Path(os.environ.get('HERMES_HOME') or Path.home() / '.hermes')
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument('--hermes-home', default=str(home_std))
    a.add_argument('--state-db')
    a.add_argument('--pruefkanal-wurzel')
    a.add_argument('--url-basis')
    a.add_argument('--jetzt', type=float)
    a.add_argument('--ohne-https', action='store_true')
    a.add_argument('--kein-besitzer', action='store_true')
    a.add_argument('--sofort', action='store_true', help='jetzt einen Zwischenbericht für die zuletzt aktive Sitzung auslösen')
    a = a.parse_args(argv)
    home = Path(a.hermes_home)
    jetzt = a.jetzt or time.time()
    if not (a.pruefkanal_wurzel and a.url_basis):
        schluessel = Path('/etc/pruefkanal/schluessel').read_text().strip()
        a.pruefkanal_wurzel = a.pruefkanal_wurzel or f'/var/pruefkanal/oeffentlich/_akte/{schluessel}'
        a.url_basis = a.url_basis or f'https://milieulux-reinigung-muenchen.de/_akte/{schluessel}'
    con = sqlite3.connect(f"file:{a.state_db or home / 'state.db'}?mode=ro", uri=True, timeout=30)
    con.row_factory = sqlite3.Row
    g = grenze(home)
    sw = schwellen(g)
    zustand_p = home / 'zwischenbericht' / 'ausgeloest.json'
    zustand = lade(zustand_p)
    try:
        eltern = Path(f'/proc/{os.getppid()}/cmdline').read_bytes().replace(b'\0', b' ').decode(errors='replace').strip()
    except OSError:
        eltern = '?'
    herz = {'zeit': iso(jetzt), 'epoch': jetzt, 'grenze': g, 'schwellen': sw, 'pid': os.getpid(), 'eltern': eltern[:300],
            'sitzungen': []}
    ausgaben = []
    for i, s in enumerate(sitzungen(con, jetzt)):
        tb = turn_beginn(con, s['id'])
        if not tb:
            continue
        turn_id, turn = tb
        n = runden(con, s['id'], turn_id)
        herz['sitzungen'].append({'sitzung': s['id'], 'turn_ab': turn_id, 'runden': n})
        faellig = [x for x in sw if n >= x and f"{s['id']}:{turn_id}:{x}" not in zustand]
        schwelle = max(faellig) if faellig else None
        if a.sofort and i == 0:
            schwelle, faellig = 'sofort', [f'sofort-{int(jetzt)}']
        if schwelle is None:
            continue
        try:
            zeile = veroeffentlichen(con=con, sid=s['id'], turn_id=turn_id, turn=turn, n=n, g=g, schwelle=schwelle,
                                     home=home, wurzel=a.pruefkanal_wurzel, url_basis=a.url_basis, jetzt=jetzt,
                                     https=not a.ohne_https, besitzer=not a.kein_besitzer)
            for x in faellig:
                zustand[f"{s['id']}:{turn_id}:{x}"] = {'zeit': iso(jetzt), 'runden': n, 'zeile': zeile}
            ausgaben.append(zeile)
        except Exception as e:  # ein gescheiterter Bericht wird gemeldet, nie still übergangen
            ausgaben.append(f"Zwischenbericht-Wächter: Veröffentlichung für {s['id']} gescheitert ({type(e).__name__}: {e})")
    schreibe(home / 'zwischenbericht' / 'herzschlag.json', herz)
    schreibe(zustand_p, zustand)
    if ausgaben:
        print('\n'.join(ausgaben))
    # Ein gescheiterter Zwischenbericht darf nicht still bleiben: Exit 1 lässt den Zeitplan einen Fehler melden
    # (failure_deliver), während eine erfolgreiche Auslösung nur im Prüfkanal und lokal landet.
    return 1 if any('gescheitert' in x for x in ausgaben) else 0


if __name__ == '__main__':
    sys.exit(main())
