"""Gestellte Eichung, MockTransport: kein Netz, kein Modellaufruf."""
import httpx
import sitecustomize as w
anzahl=[]
def antwort(req):
    anzahl.append(req)
    return httpx.Response(200,json={'model':'GESTELLTER-EICHWERT','usage':{'input_tokens':0,'output_tokens':0}})
with httpx.Client(transport=httpx.MockTransport(antwort)) as c:
    r=c.post('https://eichung.invalid/v1/messages',json={'model':'GESTELLTER-EICHWERT'})
    assert r.json()['model']=='GESTELLTER-EICHWERT'
    print('GRUEN: Erster Modell-POST gelangt zum MockTransport.')
    try:
        c.post('https://eichung.invalid/v1/messages',json={'model':'GESTELLTER-EICHWERT'})
    except w.Aufrufgrenze as e:
        assert str(e).startswith('W4:')
        print('ROT: Zweiter Modell-POST vor MockTransport gesperrt:',str(e))
    else:
        raise AssertionError('Zweiter POST wurde nicht gesperrt')
assert len(anzahl)==1
assert w.stand=={'zugelassen':1,'gesperrt':1}
print('2 von 2 Eichfaellen erfuellt; 1 von 2 POST-Versuchen erreicht den MockTransport; 0 echte Netzaufrufe.')
