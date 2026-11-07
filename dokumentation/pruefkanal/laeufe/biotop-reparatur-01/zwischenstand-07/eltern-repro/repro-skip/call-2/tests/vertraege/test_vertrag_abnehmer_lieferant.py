from beispiel.lieferant import wert
def test_alt():
    assert wert(2) == 4

def test_eichprobe_vertrag_neue_zusicherung():
    import runpy
    verbraucher = runpy.run_path('tests/test_abnehmer.py')
    verbraucher['test_bericht']()
    from beispiel.lieferant import eichprobe_zusicherung
    assert eichprobe_zusicherung() == 'da'
