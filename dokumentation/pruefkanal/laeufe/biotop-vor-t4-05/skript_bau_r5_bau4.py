"""Behebungsrunde 5 — Umbau Teil 4 (alles oder nichts; berührt keine Datei, die TEILLAUF-1 liest):
- drahtwerk: Stufe 2 nur für alpha zehnfach (dort ändern die Kandidaten); beta unverändert (Laufzeit des Verdrahtungslaufs)
- test_verdrahtung: Nachspiel als echter Durchlauf (Entscheidung 8, Review 04 Nr. 18); Stufe 2 in jedem Aegis-Urteil
- TypeScript (Entscheidung 1): Vollständigkeitsprüfung im Kanon — private Felder (#…), nicht aufzählbare und
  Symbol-Eigenschaften, eingebaute Objekte ohne erfassbare Daten; RegExp/URL/Puffer als Werte; Runner meldet sie."""
import sys
from pathlib import Path

R = Path(sys.argv[1] if len(sys.argv) > 1 else '/root/biotop')
AENDERUNGEN = {}


def ers(pfad, alt, neu):
    AENDERUNGEN.setdefault(pfad, []).append((alt, neu))


DW = 'tests/drahtwerk.py'
ers(DW, '''# Behebungsrunde 5 (Entscheidung 6): ohne Vergleichslast Stufe 2 verweigert der Vorspann den Lauf. Dieselben Lasten mit
# zehnfacher Eingabegröße (alpha: 50.000 statt 5.000 Werte; beta: zehnmal so viele Aufrufe), Verhaltensraster wie Stufe 1.
REFERENZLAST_STUFE2 = REFERENZLAST.replace("// Referenzlast drahtwerk (Kern, Messgerät)",
                                           "// Referenzlast drahtwerk, STUFE 2 (Kern, Messgerät)") \\
    .replace("Array.from({ length: 5000 }", "Array.from({ length: 50000 }") \\
    .replace("i < 15000000", "i < 150000000")
''', '''# Behebungsrunde 5 (Entscheidung 6): ohne Vergleichslast Stufe 2 verweigert der Vorspann den Lauf. Im Prüfwerk ist nur
# alpha zehnfach (50.000 statt 5.000 Werte; dort ändern die Kandidaten); beta bleibt wie Stufe 1 (sauberer
# Vergleichsbereich, schon einige zehn Millisekunden). Geprüft wird hier die Verdrahtung der Stufe, nicht ihre Größe.
REFERENZLAST_STUFE2 = REFERENZLAST.replace("// Referenzlast drahtwerk (Kern, Messgerät)",
                                           "// Referenzlast drahtwerk, STUFE 2 (Kern, Messgerät)") \\
    .replace("Array.from({ length: 5000 }", "Array.from({ length: 50000 }")
assert REFERENZLAST_STUFE2 != REFERENZLAST and "length: 50000" in REFERENZLAST_STUFE2
''')

VT = 'tests/test_verdrahtung.py'
ers(VT, '''    k_masse = _json.loads(con.execute("SELECT masse FROM kandidaten WHERE id=?", (gewaehlt["alpha"],)).fetchone()[0])
''', '''    k_masse = _json.loads(con.execute("SELECT masse FROM kandidaten WHERE id=?", (gewaehlt["alpha"],)).fetchone()[0])
    # Behebungsrunde 5 (Entscheidung 8, Review 04 Nr. 18): das Nachspiel als echter Durchlauf in der Regression — der
    # gewählte Kandidat dieses Laufs durch nachspiel.vorbereiten/spielen, derselbe Weg wie die Gegenproben der Runden.
    # An 1d9a5aa brachen alle Nachspiele ab, während die Regression grün war.
    from biotop import nachspiel as NS
    phase["schritt"] = "nachspiel"
    fall = NS.vorbereiten(Path(os.environ["BIOTOP_DB"]), gewaehlt["alpha"], tmp_path / "nachspiel")
    try:
        ns_beleg = NS.spielen(fall)
    finally:
        fall["con"].close()
''')
ers(VT, '''        nachmessungen.append({"schluessel": sorted(k for k in ("laufzeit_nachmessung", "gewinn_nachmessung") if k in z),
                              "laufzeit": z.get("laufzeit_nachmessung"),
''', '''        nachmessungen.append({"schluessel": sorted(k for k in ("laufzeit_nachmessung", "gewinn_nachmessung") if k in z),
                              "stufe": z.get("laufzeit_stufe"),
                              "laufzeit": z.get("laufzeit_nachmessung"),
''')
ers(VT, '''             "register": {"eintraege": len(register.VERLANGT), "fehlend": register_fehlend},
''', '''             "register": {"eintraege": len(register.VERLANGT), "fehlend": register_fehlend},
             "nachspiel": {k: ns_beleg.get(k) for k in ("kandidat", "status", "status_aufgezeichnet", "grund", "laufzeit_stufe",
                                                         "kammerlaeufe", "modellaufrufe_echt")},
''')
ers(VT, '''    assert jury_zeilen, "Die Jury hat nicht entschieden — der Gleichstand kam nicht zustande"
''', '''    assert jury_zeilen, "Die Jury hat nicht entschieden — der Gleichstand kam nicht zustande"
    # Behebungsrunde 5: jedes Aegis-Urteil mit Laufzeitmessung misst an Stufe 2; das Nachspiel urteilt wie der Lauf.
    stufen = [n["stufe"] for n in nachmessungen if n["stufe"] is not None]
    assert stufen and set(stufen) == {2}, f"Laufzeitstufe in den Aegis-Urteilen: {stufen}"
    assert ns_beleg["status"] == ns_beleg["status_aufgezeichnet"] == "ueberlebt" and ns_beleg["laufzeit_stufe"] == 2, \\
        beleg["nachspiel"]
''')

KA = 'biotop/kern/ts/kanon.mjs'
ers(KA, ('__BEREICH__', 'export function kan(x, anc) {\n', 'export function knapp(t) {\n'), r'''function nativ(c) {
  try { return typeof c === 'function' && /\[native code\]\s*\}\s*$/.test(Function.prototype.toString.call(c)); } catch { return false; }
}
// Behebungsrunde 5 (Entscheidung 1): Vollständigkeitsprüfung nach jedem Erfassen eines Objekts. Was Object.keys nicht
// liefert — private Felder (#…), nicht aufzählbare und Symbol-Eigenschaften, interne Daten eingebauter Objekte —, steht
// in `fehlend`; der Wirt zählt die Funktion dann als Enthaltung, nie als „0 Abweichungen, tragfähig“.
function vollstaendig(x, fehlend) {
  if (!fehlend) return;
  const name = x?.constructor?.name ?? 'Object';
  const versteckt = Object.getOwnPropertyNames(x).filter(k => !Object.prototype.propertyIsEnumerable.call(x, k));
  if (versteckt.length) fehlend.push(`${name}: nicht aufzählbare Eigenschaften ${JSON.stringify(versteckt.slice(0, 5))}`);
  if (Object.getOwnPropertySymbols(x).length) fehlend.push(`${name}: Symbol-Eigenschaften nicht erfasst`);
  for (let p = Object.getPrototypeOf(x); p && p !== Object.prototype; p = Object.getPrototypeOf(p)) {
    const k = Object.hasOwn(p, 'constructor') ? p.constructor : null;
    if (typeof k !== 'function') continue;
    if (nativ(k)) {
      if (!Object.keys(x).length) fehlend.push(`${name}: eingebautes Objekt ohne erfassbare Daten`);
      break;
    }
    let src = '';
    try { src = Function.prototype.toString.call(k); } catch { src = ''; }
    if (/(^|[\s;{}])(static\s+)?#[A-Za-z_$]/.test(src)) { fehlend.push(`${name}: private Felder (#…) nicht erfassbar`); break; }
  }
}
export function kan(x, anc, fehlend) {
  if (x === null) return null;
  if (x && typeof x === 'object' && x[VERFAELSCHT]) return '__verfaelscht';
  switch (typeof x) {
    case 'number':
      if (Number.isNaN(x)) return '__NaN';
      if (!Number.isFinite(x)) return x > 0 ? '__Inf' : '__-Inf';
      return Object.is(x, -0) ? '__-0' : x;
    case 'string': case 'boolean': return x;
    case 'undefined': return '__undefined';
    case 'bigint': return '__big:' + x;
    case 'function': return '__fn';
    case 'symbol': return '__sym';
  }
  if (anc.has(x)) return '__zyklus';
  anc.add(x);
  let r;
  if (Array.isArray(x)) r = x.map(v => kan(v, anc, fehlend));
  else if (x instanceof Map) r = {__map: [...x.entries()].map(([k, v]) => [kan(k, anc, fehlend), kan(v, anc, fehlend)])};
  else if (x instanceof Set) r = {__set: [...x.values()].map(v => kan(v, anc, fehlend))};
  else if (x instanceof Error) r = {__fehler: x.constructor?.name ?? 'Error', meldung: String(x.message)};
  else if (x instanceof Date) r = {__datum: x.getTime()};
  else if (x instanceof RegExp) r = {__regex: String(x)};                                   // Behebungsrunde 5: Werte
  else if (typeof URL === 'function' && x instanceof URL) r = {__url: x.href};
  else if (x instanceof ArrayBuffer) r = {__puffer: Array.from(new Uint8Array(x))};
  else if (ArrayBuffer.isView(x) && !(x instanceof DataView)) r = {__typisiert: x.constructor?.name, werte: Array.from(x)};
  else { vollstaendig(x, fehlend); r = {}; for (const k of Object.keys(x).sort()) r[k] = kan(x[k], anc, fehlend); }
  anc.delete(x);
  return r;
}

''')

RU = 'biotop/kern/ts/verhalten-runner.mjs'
ers(RU, "function wert(f, name) {\n  let v;\n", "function wert(f, name) {\n  let v;\n  const fehl = [];         // Behebungsrunde 5 (Entscheidung 1)\n")
ers(RU, "    try { text = JSON.stringify(kan({__iterator_objekt: v}, new Set())); }",
    "    try { text = JSON.stringify(kan({__iterator_objekt: v}, new Set(), fehl)); }")
ers(RU, ": (mehr ? 'mehr' : 'ende')}, new Set())); }\n    catch { text = '__unkanonisch'; }\n",
    ": (mehr ? 'mehr' : 'ende')}, new Set(), fehl)); }\n    catch { text = '__unkanonisch'; }\n"
    "    for (const g of fehl) unvoll(name, g);\n")
ers(RU, "  try { text = JSON.stringify(kan(v, new Set())); } catch { return {text: '__unkanonisch', roh: v, inhaltlich: false}; }\n",
    "  try { text = JSON.stringify(kan(v, new Set(), fehl)); } catch { return {text: '__unkanonisch', roh: v, inhaltlich: false}; }\n"
    "  for (const g of fehl) unvoll(name, g);\n")
ers(RU, "function zustandObs(k, args) {\n  if (args.some(a => a !== null && typeof a === 'object')) {\n"
        "    try { beob[k + '>args'] = knapp(JSON.stringify(kan(args, new Set()))); } catch { beob[k + '>args'] = '__unkanonisch'; }\n",
    "function zustandObs(k, args, name) {\n  if (args.some(a => a !== null && typeof a === 'object')) {\n    const fehl = [];\n"
    "    try { beob[k + '>args'] = knapp(JSON.stringify(kan(args, new Set(), fehl))); } catch { beob[k + '>args'] = '__unkanonisch'; }\n"
    "    for (const g of fehl) unvoll(name, g);\n")
ers(RU, "    zustandObs(schluessel, args);\n", "    zustandObs(schluessel, args, name);\n")
ers(RU, "      zustandObs(k, args);\n", "      zustandObs(k, args, name);\n")


def main():
    neu_inhalt, fehler = {}, []
    for pfad, liste in AENDERUNGEN.items():
        text = (R / pfad).read_text()
        for alt, neu in liste:
            if isinstance(alt, tuple):
                _, start, ende_vor = alt
                if text.count(start) != 1 or text.count(ende_vor) != 1:
                    fehler.append(f'{pfad}: Bereich {text.count(start)}×/{text.count(ende_vor)}×')
                    continue
                i, j = text.index(start), text.index(ende_vor)
                text = text[:i] + neu + text[j:]
            else:
                n = text.count(alt)
                if n != 1:
                    fehler.append(f'{pfad}: Anker {n}×: {alt[:90]!r}')
                    continue
                text = text.replace(alt, neu)
        neu_inhalt[pfad] = text
    if fehler:
        print('ABBRUCH — nichts geschrieben:\n' + '\n'.join(fehler))
        sys.exit(2)
    for pfad, text in neu_inhalt.items():
        (R / pfad).write_text(text)
    print(f'geschrieben: {len(neu_inhalt)} Dateien, {sum(len(v) for v in AENDERUNGEN.values())} Ersetzungen')


if __name__ == '__main__':
    main()
