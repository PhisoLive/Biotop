"""Maßeichung am sauberen Bereich: eine Regel, die dort anschlägt, zählt nicht.

Befund aus Lauf 37: Der Bereich `zahlen` ist laut Verfassung sauber. Dort meldete
`security/detect-object-injection` acht Punkte. Der Schwarm „behob" sie mit
`arr[i]` → `arr.at(i)` — gemessen identisches Verhalten, Tests unverändert 29/29 —
und gewann dafür 7 Kernmaßpunkte. Das Biotop optimierte die Messung statt den Code.

Dieselbe Figur wie die Rauschmessung, auf die Maße selbst angewandt: Vor dem Lauf wird
jede Prüferregel am Vergleichsbereich gemessen. Schlägt sie dort an, wo laut Verfassung
keine Schwäche liegt, ist sie für dieses Werk kein Maß und zählt nicht zum Kernmaß.
"""
import json
from pathlib import Path

import pytest

from biotop.kern import messgeraet
from biotop.organe import masseichung


def _messung(befunde_je_bereich):
    """Baut eine Messung, wie messgeraet.messen sie liefert."""
    return {'gueltig': True, 'bereiche': {
        b: {'tests_bestanden': 10, 'tests_fehlgeschlagen': 0, 'tests_gesamt': 10,
            'sicherheit_punkte': sum(x['punkte'] for x in bef),
            'sicherheit_befunde': bef, 'tote_funktionen': 0, 'tote_liste': [],
            'groesste_funktion': 5, 'laufzeit_ms': 1.0}
        for b, bef in befunde_je_bereich.items()}}


def _befund(regel, datei, punkte=1, schwere='LOW'):
    return {'test': regel, 'datei': datei, 'zeile': 1, 'schwere': schwere,
            'punkte': punkte, 'text': regel}


def test_regel_die_im_sauberen_bereich_anschlaegt_zaehlt_nicht():
    """Der Kern der Eichung: Fehlalarm im Vergleichsbereich → Regel stillgelegt."""
    messung = _messung({
        'zahlen': [_befund('security/detect-object-injection', 'src/zahlen/a.ts')],
        'tarife': [_befund('no-new-func', 'src/tarife/b.ts', 10, 'HIGH'),
                   _befund('security/detect-object-injection', 'src/tarife/c.ts')],
    })
    e = masseichung.eichen(messung, sauberer_bereich='zahlen')
    assert e['stillgelegt'] == ['security/detect-object-injection']
    assert e['gemessen'] == ['no-new-func'] or 'no-new-func' in e['gemessen']
    assert e['begruendung']['security/detect-object-injection'].startswith('schlägt im sauberen')


def test_gegenprobe_regel_die_nur_ausserhalb_anschlaegt_bleibt_in_kraft():
    """Ohne diese Probe würde eine Eichung, die alles stilllegt, ebenso bestehen."""
    messung = _messung({
        'zahlen': [],
        'tarife': [_befund('no-new-func', 'src/tarife/b.ts', 10, 'HIGH')],
    })
    e = masseichung.eichen(messung, sauberer_bereich='zahlen')
    assert e['stillgelegt'] == []
    assert 'no-new-func' in e['gemessen']


def test_kernmass_rechnet_stillgelegte_regeln_nicht_mit():
    messung = _messung({
        'zahlen': [_befund('security/detect-object-injection', 'src/zahlen/a.ts')],
        'tarife': [_befund('no-new-func', 'src/tarife/b.ts', 10, 'HIGH'),
                   _befund('security/detect-object-injection', 'src/tarife/c.ts'),
                   _befund('security/detect-object-injection', 'src/tarife/d.ts')],
    })
    e = masseichung.eichen(messung, sauberer_bereich='zahlen')
    roh = messgeraet.kernmass_f2(messung)
    bereinigt = masseichung.kernmass_bereinigt(messung, e)
    # roh: 1 + 10 + 1 + 1 = 13 Punkte; bereinigt nur die 10 von no-new-func
    assert roh == -13, roh
    assert bereinigt == -10, bereinigt


def test_ohne_sauberen_bereich_wird_nichts_stillgelegt():
    """Nennt die Verfassung keinen Vergleichsbereich, gilt jede Regel — nichts wird geraten."""
    messung = _messung({'tarife': [_befund('no-new-func', 'src/t.ts', 10, 'HIGH')]})
    e = masseichung.eichen(messung, sauberer_bereich=None)
    assert e['stillgelegt'] == []
    assert e['sauberer_bereich'] is None


def test_unbekannter_bereich_ist_ein_fehler_kein_stillschweigen():
    """Ein falsch benannter Vergleichsbereich darf nicht als 'keine Fehlalarme' gelesen werden."""
    messung = _messung({'tarife': [_befund('no-new-func', 'src/t.ts', 10, 'HIGH')]})
    with pytest.raises(masseichung.MasseichungFehler, match='nicht im Werk'):
        masseichung.eichen(messung, sauberer_bereich='gibtsnicht')


def test_anwenden_rechnet_stillgelegte_regeln_aus_und_laesst_sie_sichtbar():
    """Der Annahmepfad bewertet die geeichte Messung: Punkte ohne die Regel, Befunde bleiben lesbar."""
    messung = _messung({
        'zahlen': [_befund('security/detect-object-injection', 'src/zahlen/a.ts')],
        'tarife': [_befund('no-new-func', 'src/tarife/b.ts', 10, 'HIGH'),
                   _befund('security/detect-object-injection', 'src/tarife/c.ts')],
    })
    e = masseichung.eichen(messung, sauberer_bereich='zahlen')
    g = masseichung.anwenden(messung, e)
    assert g['bereiche']['tarife']['sicherheit_punkte'] == 10
    assert g['bereiche']['tarife']['sicherheit_punkte_roh'] == 11
    assert [x['test'] for x in g['bereiche']['tarife']['sicherheit_stillgelegt']] == ['security/detect-object-injection']
    assert g['bereiche']['zahlen']['sicherheit_punkte'] == 0
    assert messgeraet.kernmass_f2(g) == masseichung.kernmass_bereinigt(messung, e) == -10
    # Rohmessung unverändert; zweites Anwenden ändert nichts
    assert messung['bereiche']['tarife']['sicherheit_punkte'] == 11
    assert masseichung.anwenden(g, e) is g


def test_gegenprobe_anwenden_ohne_stilllegung_laesst_die_messung_gleich():
    messung = _messung({'tarife': [_befund('no-new-func', 'src/t.ts', 10, 'HIGH')]})
    e = masseichung.eichen(messung, sauberer_bereich=None)
    assert masseichung.anwenden(messung, e) is messung
    assert masseichung.anwenden(messung, None) is messung


def test_sauberer_bereich_aus_der_verfassung():
    """T3: die versiegelte Verfassung nennt den Bereich im Text, nicht in den Regeln."""
    v = {'text': '5. **Tragender Pfad:** ... `zahlen` ist der saubere Vergleichsbereich.', 'regeln': {}}
    assert masseichung.sauberer_bereich(v) == 'zahlen'
    assert masseichung.sauberer_bereich({'text': 'x', 'regeln': {'sauberer_bereich': 'eingang'}}) == 'eingang'
    assert masseichung.sauberer_bereich({'text': 'kein solcher Satz', 'regeln': {}}) is None
    assert masseichung.sauberer_bereich(None) is None


def test_zwei_verschiedene_saubere_bereiche_sind_ein_widerspruch():
    v = {'text': '`zahlen` ist der saubere Vergleichsbereich. `eingang` ist der saubere Vergleichsbereich.',
         'regeln': {}}
    with pytest.raises(masseichung.MasseichungFehler, match='mehrere'):
        masseichung.sauberer_bereich(v)


def test_eichung_meldet_jede_regel_mit_nenner():
    """Für den Bericht: welche Regeln geprüft, welche stillgelegt, mit Fundzahl."""
    messung = _messung({
        'zahlen': [_befund('security/detect-object-injection', 'src/zahlen/a.ts'),
                   _befund('security/detect-object-injection', 'src/zahlen/b.ts')],
        'tarife': [_befund('no-new-func', 'src/tarife/b.ts', 10, 'HIGH')],
    })
    e = masseichung.eichen(messung, sauberer_bereich='zahlen')
    assert e['funde_im_sauberen'] == {'security/detect-object-injection': 2}
    assert e['regeln_geprueft'] == 2
    assert e['regeln_stillgelegt'] == 1


def test_anwenden_mit_anderer_eichung_ist_ein_fehler():
    """REVIEW-03 Nr. 20: „schon geeicht“ wurde nur am Marker erkannt — eine andere Eichung blieb still wirkungslos."""
    messung = _messung({'zahlen': [_befund('security/detect-object-injection', 'src/zahlen/a.ts')],
                        'tarife': [_befund('no-new-func', 'src/tarife/b.ts', 10, 'HIGH')]})
    e1 = {'sauberer_bereich': 'zahlen', 'stillgelegt': ['security/detect-object-injection']}
    einmal = masseichung.anwenden(messung, e1)
    assert masseichung.anwenden(einmal, e1) is einmal                      # dieselbe Eichung: idempotent
    with pytest.raises(masseichung.MasseichungFehler, match='andere'):
        masseichung.anwenden(einmal, {'sauberer_bereich': 'zahlen', 'stillgelegt': ['no-new-func']})
    with pytest.raises(masseichung.MasseichungFehler, match='andere'):
        masseichung.anwenden(einmal, {'sauberer_bereich': 'zahlen', 'stillgelegt': []})
