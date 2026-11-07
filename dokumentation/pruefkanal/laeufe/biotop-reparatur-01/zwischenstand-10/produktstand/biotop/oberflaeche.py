"""Web-Oberfläche des Biotops (3.15, Phase 3). Eine HTML-Seite hinter der Anmeldung; jedes Bedienelement liest oder
schreibt genau eine Stelle im Kern — die Zuordnung steht in ELEMENTE (Element → Route → Datei:Funktion) und wird von
`biotop oberflaeche-belege` mit Zeilennummern ausgegeben (Tor 3, Zeile „Oberfläche").

Der HTML/JS-Text ist bewusst schlicht (kein Framework), vom Tablet bedienbar (große Schaltflächen, eine Spalte).
Der Token liegt nach der Anmeldung im sessionStorage des Browsers; jede Anfrage trägt ihn als Bearer.
"""

from __future__ import annotations

# Element-ID im HTML → (HTTP-Methode, Route, Kernstelle „modul.funktion“, Lese-/Schreibzugriff)
ELEMENTE = {
    "anmelden":            ("POST", "/anmelden",                        "kern/anmeldung.py:anmelden",             "schreibt tokens"),
    "abmelden":            ("—",    "sessionStorage.clear",             "oberflaeche.py:JS abmelden",              "löscht Token im Browser"),
    "lauf-wahl":           ("GET",  "/laeufe",                          "dienst.py:do_GET /laeufe$",               "liest laeufe"),
    "werk-landkarte":      ("GET",  "/werke/<id>/landkarte",            "dienst.py:do_GET /werke/<id>/landkarte",  "liest landkarte, strassen, vertraege"),
    "verfassung":          ("GET",  "/laeufe/<id>/verfassung",          "organe/verfassung.py:lesen",              "liest verfassung_werk"),
    "mass":                ("GET",  "/laeufe/<id>",                     "dienst.py:do_GET /laeufe/<id>$",          "liest laeufe.mass (eingefroren)"),
    "kurve":               ("GET",  "/laeufe/<id>/generationen",        "dienst.py:do_GET /laeufe/<id>/generationen", "liest generationen.masse"),
    "generation-aktuell":  ("GET",  "/laeufe/<id>/kandidaten",          "dienst.py:do_GET /laeufe/<id>/kandidaten", "liest kandidaten je Nische"),
    "vorlage":             ("GET",  "/laeufe/<id>/vorlage",             "dienst.py:do_GET /laeufe/<id>/vorlage",   "liest generationen(vorgelegt), kandidaten.diff/masse, Anklägerurteil, gedaechtnis.geschmack_vorhersage"),
    "freigabe-frei":       ("POST", "/laeufe/<id>/freigabe",            "lauf.py:freigabe",                        "schreibt generationen.status, protokoll freigabe.frei, geschmack"),
    "freigabe-ablehnen":   ("POST", "/laeufe/<id>/freigabe",            "lauf.py:freigabe",                        "schreibt generationen.status, lazarus.rueckkehr, geschmack"),
    "entropie":            ("GET",  "/laeufe/<id>/entropie",            "organe/entropie.py:verlauf",              "liest entropie"),
    "kasse":               ("GET",  "/laeufe/<id>/kasse",               "kern/kasse.py:stand",                     "liest kasse"),
    "archiv":              ("GET",  "/laeufe/<id>/lazarus",             "organe/lazarus.py:liste",                 "liest lazarus"),
    "mentor-richtungen":   ("GET",  "/laeufe/<id>/mentor",              "dienst.py:do_GET /laeufe/<id>/mentor",    "liest mentor"),
    "richtung-waehlen":    ("POST", "/laeufe/<id>/richtung",            "organe/mentor.py:waehlen",                "schreibt laeufe.richtung, mentor.gewaehlt, protokoll mentor.gewaehlt"),
    "immunsystem":         ("GET",  "/laeufe/<id>/immunsystem",         "dienst.py:do_GET /laeufe/<id>/immunsystem", "liest immunsystem"),
    "protokoll":           ("GET",  "/protokoll",                       "kern/protokoll.py:lesen",                 "liest protokoll"),
}

HTML = r"""<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Biotop</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;background:#f4f4f2;color:#222}
header{background:#1d3b2a;color:#fff;padding:12px 16px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}
header h1{font-size:18px;margin:0;flex:1}
main{max-width:1100px;margin:0 auto;padding:12px}
section{background:#fff;border-radius:10px;padding:14px;margin:12px 0;box-shadow:0 1px 3px #0002}
h2{font-size:16px;margin:0 0 8px;color:#1d3b2a}
button{font-size:16px;padding:10px 16px;border-radius:8px;border:1px solid #1d3b2a;background:#fff;color:#1d3b2a;margin:4px 4px 4px 0;min-height:44px}
button.primaer{background:#1d3b2a;color:#fff}
button.rot{border-color:#8a1c1c;color:#8a1c1c}
input,select,textarea{font-size:16px;padding:8px;border-radius:8px;border:1px solid #bbb;min-height:40px}
table{border-collapse:collapse;width:100%;font-size:14px}
td,th{border-bottom:1px solid #e3e3e3;padding:6px 4px;text-align:left;vertical-align:top}
pre{background:#f7f7f5;padding:8px;border-radius:8px;overflow:auto;font-size:12px;max-height:340px}
.hinweis{color:#666;font-size:13px}
.kasse{font-weight:600}
.diff-plus{color:#116611}.diff-minus{color:#991111}
svg{width:100%;height:220px;background:#fafaf8;border-radius:8px}
#anmeldung{max-width:420px;margin:60px auto}
.zeile{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.abzeichen{display:inline-block;padding:2px 8px;border-radius:12px;background:#e8efe9;font-size:12px}
</style></head><body>
<header><h1>Biotop — Oberfläche</h1>
 <span id="kasse-kopf" class="kasse" title="Kostenstand des gewählten Laufs (kern/kasse.py:stand)"></span>
 <select id="lauf-wahl" title="Lauf wählen (GET /laeufe)"></select>
 <button id="abmelden">Abmelden</button></header>
<main>
<section id="anmeldung"><h2>Anmeldung</h2>
 <div class="zeile"><input id="name" placeholder="Benutzer" autocomplete="username"><input id="kennwort" type="password" placeholder="Kennwort" autocomplete="current-password">
 <button id="anmelden" class="primaer">Anmelden</button></div><p class="hinweis" id="anmelde-hinweis">Ohne Anmeldung liefert jede Route 401.</p></section>
<div id="inhalt" style="display:none">
<section><h2>Vorlage zur Freigabe</h2><div id="vorlage"></div>
 <div class="zeile"><input id="freigabe-grund" placeholder="Begründung (Pflicht bei Ablehnung)" style="flex:1">
 <button id="freigabe-frei" class="primaer">Freigeben</button><button id="freigabe-ablehnen" class="rot">Ablehnen</button></div><p class="hinweis" id="freigabe-hinweis"></p></section>
<section><h2>Verlauf der Maße (Kurve)</h2><svg id="kurve" viewBox="0 0 800 220" preserveAspectRatio="none"></svg><div id="kurve-legende" class="hinweis"></div></section>
<section><h2>Aktuelle Generation — Kandidaten je Nische</h2><div id="generation-aktuell"></div></section>
<section><h2>Mentor — Richtungen</h2><div id="mentor-richtungen"></div>
 <div class="zeile"><select id="richtung-name"></select><button id="richtung-waehlen" class="primaer">Richtung wählen</button></div><p class="hinweis" id="richtung-hinweis"></p></section>
<section><h2>Entropie</h2><div id="entropie"></div></section>
<section><h2>Kasse</h2><div id="kasse"></div></section>
<section><h2>Eingefrorenes Maß</h2><pre id="mass"></pre></section>
<section><h2>Verfassung des Werks</h2><pre id="verfassung"></pre></section>
<section><h2>Landkarte</h2><div id="werk-landkarte"></div></section>
<section><h2>Immunsystem</h2><div id="immunsystem"></div></section>
<section><h2>Archiv (Lazarus)</h2><div id="archiv"></div></section>
<section><h2>Protokoll (letzte 60)</h2><pre id="protokoll"></pre></section>
</div></main>
<script>
const $=id=>document.getElementById(id);
const tok=()=>sessionStorage.getItem('biotop_token');
async function api(m,p,body){const r=await fetch(p,{method:m,headers:{'Authorization':'Bearer '+(tok()||''),'Content-Type':'application/json'},body:body?JSON.stringify(body):undefined});
 if(r.status===401){zeigeAnmeldung();throw new Error('401')} return r.json();}
function zeigeAnmeldung(){$('anmeldung').style.display='';$('inhalt').style.display='none';}
function esc(s){return String(s??'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}
$('anmelden').onclick=async()=>{const r=await fetch('/anmelden',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:$('name').value,kennwort:$('kennwort').value})});
 const d=await r.json(); if(d.token){sessionStorage.setItem('biotop_token',d.token);$('kennwort').value='';await start();} else {$('anmelde-hinweis').textContent='Anmeldung fehlgeschlagen ('+r.status+')';}};
$('abmelden').onclick=()=>{sessionStorage.clear();zeigeAnmeldung();};
let LAUF=null;
async function start(){const laeufe=await api('GET','/laeufe'); $('anmeldung').style.display='none';$('inhalt').style.display='';
 const s=$('lauf-wahl'); s.innerHTML=laeufe.map(l=>`<option value="${l.id}">Lauf ${l.id} — ${esc(l.status)}</option>`).join('');
 LAUF=LAUF||laeufe[laeufe.length-1]?.id; s.value=LAUF; s.onchange=()=>{LAUF=+s.value;laden();}; await laden();}
async function laden(){const id=LAUF; const [lauf,gens,kand,kasse,laz,vorl,ent,ment,imm,verf,prot]=await Promise.all([
 api('GET',`/laeufe/${id}`),api('GET',`/laeufe/${id}/generationen`),api('GET',`/laeufe/${id}/kandidaten`),api('GET',`/laeufe/${id}/kasse`),api('GET',`/laeufe/${id}/lazarus`),
 api('GET',`/laeufe/${id}/vorlage`),api('GET',`/laeufe/${id}/entropie`),api('GET',`/laeufe/${id}/mentor`),api('GET',`/laeufe/${id}/immunsystem`),api('GET',`/laeufe/${id}/verfassung`),api('GET','/protokoll?limit=60')]);
 $('kasse-kopf').textContent=`Kasse: ${(kasse.stand.ausgegeben_eur||0).toFixed(4)} € von ${(kasse.stand.budget_eur||0).toFixed(2)} € · ${kasse.stand.aufrufe} Aufrufe`;
 $('kasse').innerHTML=`<p><b>${(kasse.stand.ausgegeben_eur||0).toFixed(4)} €</b> von ${(kasse.stand.budget_eur||0).toFixed(2)} € (${kasse.stand.aufrufe} Aufrufe, ${kasse.stand.tokens_ein} ein / ${kasse.stand.tokens_aus} aus Token; Kontingent-Aufrufe ${kasse.stand.kontingent_aufrufe})</p>`+
  `<table><tr><th>Zweck</th><th>Aufrufe</th><th>€</th></tr>${Object.entries(kasse.aufrufe.reduce((a,x)=>{const k=x.zweck.split('.').slice(0,2).join('.');a[k]=a[k]||[0,0];a[k][0]++;a[k][1]+=x.kosten_eur;return a},{})).sort((a,b)=>b[1][1]-a[1][1]).slice(0,12).map(([k,v])=>`<tr><td>${esc(k)}</td><td>${v[0]}</td><td>${v[1].toFixed(4)}</td></tr>`).join('')}</table>`;
 $('mass').textContent=JSON.stringify(lauf.mass,null,1); $('verfassung').textContent=verf.text||'(keine)';
 // Kurve
 const ang=gens.filter(g=>g.status==='angenommen'&&g.bereiche); const W=800,H=220,P=30; const svg=$('kurve'); const ber=ang.length?Object.keys(ang[0].bereiche):[];
 const farben=['#1d3b2a','#8a1c1c','#1c4b8a','#8a6a1c','#5a1c8a']; let s='';
 const kern=g=>Object.values(g.bereiche).reduce((a,b)=>a-(b.tests_fehlgeschlagen||0)-(b.sicherheit_punkte||0)-(b.tote_funktionen||0),0);
 const ks=ang.map(kern); const kmin=Math.min(-1,...ks), kmax=Math.max(0,...ks); const x=i=>P+(W-2*P)*(ang.length>1?i/(ang.length-1):0.5); const y=v=>H-P-(H-2*P)*((v-kmin)/(kmax-kmin||1));
 s+=`<polyline fill="none" stroke="#000" stroke-width="2" points="${ang.map((g,i)=>`${x(i)},${y(kern(g))}`).join(' ')}"/>`;
 ang.forEach((g,i)=>{s+=`<circle cx="${x(i)}" cy="${y(kern(g))}" r="4" fill="#000"/><text x="${x(i)}" y="${H-8}" font-size="11" text-anchor="middle">G${g.nummer}</text>`});
 const lz=ber.map(b=>ang.map(g=>g.bereiche[b].laufzeit_ms||0)); const lmax=Math.max(1,...lz.flat()); const yl=v=>H-P-(H-2*P)*(v/lmax);
 ber.forEach((b,bi)=>{s+=`<polyline fill="none" stroke="${farben[bi%5]}" stroke-dasharray="4 3" stroke-width="1.5" points="${ang.map((g,i)=>`${x(i)},${yl(g.bereiche[b].laufzeit_ms||0)}`).join(' ')}"/>`});
 s+=`<text x="4" y="14" font-size="11">Kernmaß F2 (schwarz, ${kmin}…${kmax})</text><text x="${W-4}" y="14" font-size="11" text-anchor="end">Laufzeit ms (gestrichelt, 0…${lmax.toFixed(0)})</text>`;
 svg.innerHTML=s; $('kurve-legende').innerHTML=ber.map((b,i)=>`<span class="abzeichen" style="border-left:6px solid ${farben[i%5]}">${esc(b)}</span> `).join('')+` — ${ang.length} angenommene Generationen von ${gens.length}`;
 // Generation aktuell
 const letzte=Math.max(0,...kand.map(k=>k.generation)); const kk=kand.filter(k=>k.generation===letzte); const nischen={};
 kk.forEach(k=>{(nischen[k.nische]=nischen[k.nische]||[]).push(k)});
 $('generation-aktuell').innerHTML=`<p>Generation ${letzte}: ${kk.length} Kandidaten</p>`+Object.entries(nischen).map(([n,ks])=>`<p><b>${esc(n)}</b> (${ks.length}): `+ks.map(k=>`<span class="abzeichen" title="${esc(k.grund)}">K${k.id} ${esc(k.bereich)} ${esc(k.status)}</span>`).join(' ')+`</p>`).join('');
 // Vorlage
 if(vorl.generation){$('vorlage').innerHTML=`<p><b>Generation ${vorl.generation.nummer}</b> — ${esc(vorl.generation.grund)}</p>`+
  vorl.kandidaten.map(k=>`<h3>${esc(k.bereich)} · K${k.id} (${esc(k.nische)}, ${esc(k.modell)})</h3><p>${esc(k.begruendung)}</p>`+
   `<p>Maß: ${esc(JSON.stringify(k.urteil&&{kern:[k.urteil.kern_basis,k.urteil.kern_kandidat],pareto_schlechter:k.urteil.pareto_schlechter,grenzen:k.urteil.grenzen_gerissen,laufzeit:k.urteil.laufzeit_gewinne}))}</p>`+
   `<p>Ankläger: ${esc(JSON.stringify(k.anklaeger))}</p>`+(k.geschmack?`<p>Geschmacksvorhersage: <b>${esc(k.geschmack.vorhersage)}</b> (${(k.geschmack.sicherheit*100).toFixed(0)} %, gelernt aus ${k.geschmack.gelernt_aus}; Merkmale ${esc(k.geschmack.merkmale.join(', '))})</p>`:'<p class="hinweis">Geschmacksvorhersage: noch keine 20 Entscheidungen</p>')+
   `<pre>${k.diff.split('\n').map(l=>l.startsWith('+')?`<span class="diff-plus">${esc(l)}</span>`:l.startsWith('-')?`<span class="diff-minus">${esc(l)}</span>`:esc(l)).join('\n')}</pre>`).join('');
  $('freigabe-frei').disabled=$('freigabe-ablehnen').disabled=false;} else {$('vorlage').innerHTML='<p class="hinweis">Keine Generation wartet auf Freigabe.</p>';$('freigabe-frei').disabled=$('freigabe-ablehnen').disabled=true;}
 // Mentor
 const rs=ment.richtungen||[]; $('mentor-richtungen').innerHTML=rs.length?`<p>Empfehlung: <b>${esc(ment.empfehlung)}</b> — ${esc(ment.begruendung)} ${ment.gewaehlt?`<span class="abzeichen">gewählt: ${esc(ment.gewaehlt)} (${esc(ment.gewaehlt_von)})</span>`:''}</p><table><tr><th>Richtung</th><th>Ertrag</th><th>Risiko</th><th>Aufwand</th><th>Bereiche</th><th>Artgedächtnis</th></tr>`+
  rs.map(r=>`<tr><td><b>${esc(r.name)}</b><br>${esc(r.ziel)}</td><td>${esc(r.ertrag)}</td><td>${esc(r.risiko)}</td><td>${esc(r.aufwand_generationen)} Gen</td><td>${esc((r.bereiche||[]).join(', '))}</td><td>${esc((r.artgedaechtnis||[]).join(', '))}</td></tr>`).join('')+'</table>':'<p class="hinweis">Noch keine Richtungen (CLI: biotop mentor &lt;lauf&gt;).</p>';
 $('richtung-name').innerHTML=rs.map(r=>`<option>${esc(r.name)}</option>`).join('');
 // Entropie
 $('entropie').innerHTML=(ent.verlauf||[]).length?`<table><tr><th>Gen</th><th>Status</th><th>Kernmaß</th><th>Verbesserung %</th><th>Doppelgänger-Anteil</th></tr>`+ent.verlauf.map(e=>`<tr><td>${e.generation}</td><td>${esc(e.status)}</td><td>${e.kernmass_vor} → ${e.kernmass_nach}</td><td>${e.verbesserung_prozent}</td><td>${(e.verschiedenheit.anteil*100).toFixed(0)} % (${e.verschiedenheit.doppelgaenger} von ${e.verschiedenheit.kandidaten_mit_diff})</td></tr>`).join('')+'</table>'+(ent.saettigung?`<p><b>${esc(ent.saettigung.meldung)}</b></p>`:''):'<p class="hinweis">Noch keine Generation.</p>';
 // Landkarte
 const wk=await api('GET',`/werke/${lauf.werk_id}/landkarte`); const st0=wk.stufen.filter(z=>z.stufe===0), st1=wk.stufen.filter(z=>z.stufe===1);
 $('werk-landkarte').innerHTML=`<p>${esc(st0.map(z=>z.inhalt).join(' '))}</p>`+st1.map(z=>`<p><b>${esc(z.schluessel)}</b>: ${esc(typeof z.inhalt==='string'?z.inhalt:JSON.stringify(z.inhalt))}</p>`).join('')+`<p class="hinweis">Straßen: ${wk.strassen.length} · Verträge (abgeleitet): ${wk.vertraege.length} · Stufen 2/3: ${wk.stufen.filter(z=>z.stufe>=2).length} Einträge</p>`;
 $('immunsystem').innerHTML=`<table><tr><th>Bereich</th><th>Name</th><th>Status</th><th>Gen</th></tr>${imm.map(i=>`<tr><td>${esc(i.bereich)}</td><td>${esc(i.name)}</td><td>${esc(i.status)}</td><td>${i.generation}</td></tr>`).join('')}</table>`;
 $('archiv').innerHTML=`<table><tr><th>Gen</th><th>Tag</th><th>Prüfsumme</th><th>Zeit</th></tr>${laz.map(l=>`<tr><td>${l.generation}</td><td>${esc(l.tag)}</td><td>${esc(l.pruefsumme.slice(0,16))}…</td><td>${esc(l.erstellt_am)}</td></tr>`).join('')}</table>`;
 $('protokoll').textContent=prot.map(p=>`#${p.nr} ${p.zeit} ${p.art} ${typeof p.inhalt==='string'?p.inhalt.slice(0,160):JSON.stringify(p.inhalt).slice(0,160)}`).join('\n');
}
async function freigabe(ent){const g=$('freigabe-grund').value; if(ent==='ablehnen'&&!g){$('freigabe-hinweis').textContent='Ablehnung braucht eine Begründung.';return;}
 const r=await api('POST',`/laeufe/${LAUF}/freigabe`,{entscheidung:ent,grund:g}); $('freigabe-hinweis').textContent=JSON.stringify(r); await laden();}
$('freigabe-frei').onclick=()=>freigabe('frei'); $('freigabe-ablehnen').onclick=()=>freigabe('ablehnen');
$('richtung-waehlen').onclick=async()=>{const r=await api('POST',`/laeufe/${LAUF}/richtung`,{name:$('richtung-name').value}); $('richtung-hinweis').textContent=JSON.stringify(r).slice(0,300); await laden();};
if(tok()) start().catch(()=>zeigeAnmeldung()); else zeigeAnmeldung();
</script></body></html>"""


def belege() -> list[dict]:
    """Für jedes Bedienelement: Dateipfad und Zeile der Stelle, die es liest oder schreibt (mechanisch gesucht)."""
    import re
    from pathlib import Path
    wurzel = Path(__file__).resolve().parent
    out = []
    for el, (methode, route, stelle, wirkung) in ELEMENTE.items():
        datei, _, funktion = stelle.partition(":")
        pfad = wurzel / datei if not datei.startswith("oberflaeche") else wurzel / "oberflaeche.py"
        zeile = None
        html_zeile = next((i for i, l in enumerate(HTML.splitlines(), 1) if f'id="{el}"' in l), None)
        if pfad.exists():
            text = pfad.read_text().splitlines()
            muster = funktion.split(" ")[0]
            if muster.startswith("do_GET") or muster.startswith("do_POST"):
                ziel = funktion.split(" ", 1)[1] if " " in funktion else ""
                zeile = next((i for i, l in enumerate(text, 1) if ziel and (ziel.replace("<id>", "(\\d+)") in l or ziel in l) and ("re.match" in l or "pfad ==" in l)), None)
            elif muster.startswith("JS"):
                zeile = next((i for i, l in enumerate(HTML.splitlines(), 1) if "sessionStorage.clear" in l), None)
                pfad = wurzel / "oberflaeche.py"
            elif "Tabelle" in funktion:
                zeile = next((i for i, l in enumerate(text, 1) if "CREATE TABLE IF NOT EXISTS mentor" in l), None)
            else:
                zeile = next((i for i, l in enumerate(text, 1) if re.match(rf"\s*def {re.escape(muster)}\b", l)), None)
        out.append({"element": el, "methode": methode, "route": route, "html_zeile_oberflaeche_py": html_zeile, "kernstelle": f"{pfad.relative_to(wurzel.parent) if pfad.exists() else datei}:{zeile}", "wirkung": wirkung, "belegt": zeile is not None and html_zeile is not None})
    return out
