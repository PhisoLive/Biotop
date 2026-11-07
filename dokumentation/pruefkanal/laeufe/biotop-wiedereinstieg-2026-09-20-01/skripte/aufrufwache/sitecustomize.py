"""Prozesslokale HTTP-Wache: hoechstens ein POST, keine Modellwahl.
Nur fuer den freigegebenen CLI-Nachweis; nicht im Hermes-Programm installiert.
"""
import json
import os
import threading
from pathlib import Path

if os.environ.get('W4_WACHE_VERZEICHNIS'):
    import httpx
    ordner = Path(os.environ['W4_WACHE_VERZEICHNIS'])
    sperre = threading.Lock()
    stand = {'zugelassen': 0, 'gesperrt': 0}

    class Aufrufgrenze(BaseException):
        pass

    def protokoll(art, **werte):
        with (ordner / 'HTTP-WACHE-01.jsonl').open('a') as f:
            f.write(json.dumps({'art': art, **werte}, ensure_ascii=False) + '\n')

    def pruefe(request):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return False
        with sperre:
            try:
                koerper = json.loads(request.content)
            except Exception:
                koerper = {}
            modell = koerper.get('model') if isinstance(koerper, dict) else None
            if stand['zugelassen'] or request.method != 'POST' or not modell:
                stand['gesperrt'] += 1
                protokoll('vor_netz_gesperrt', methode=request.method,
                          host=request.url.host, pfad=request.url.path,
                          modell=modell, **stand)
                raise Aufrufgrenze('W4: weiterer oder nicht zuordenbarer Schreibaufruf vor dem Netz gesperrt')
            stand['zugelassen'] += 1
            protokoll('vor_netz_zugelassen', methode=request.method,
                      host=request.url.host, pfad=request.url.path,
                      modell=modell, **stand)
            return True

    def erfasse(response):
        roh = response.content
        (ordner / 'HTTP-ANTWORT-01.txt').write_bytes(roh)
        protokoll('antwort', status=response.status_code, bytes=len(roh))

    original_sync = httpx.Client.send
    original_async = httpx.AsyncClient.send

    def senden(self, request, *args, **kwargs):
        messen = pruefe(request)
        response = original_sync(self, request, *args, **kwargs)
        if messen:
            response.read()
            erfasse(response)
        return response

    async def senden_async(self, request, *args, **kwargs):
        messen = pruefe(request)
        response = await original_async(self, request, *args, **kwargs)
        if messen:
            await response.aread()
            erfasse(response)
        return response

    httpx.Client.send = senden
    httpx.AsyncClient.send = senden_async
    protokoll('wache_geladen', pid=os.getpid())
