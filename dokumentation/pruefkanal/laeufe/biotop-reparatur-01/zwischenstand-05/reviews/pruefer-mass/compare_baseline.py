"""Reconstruct the exact old measurement source from the supplied diff, in memory only."""
import json
import re
from types import ModuleType
import run_unit_checks as guard
from biotop.kern import messgeraet as current

path='biotop/kern/messgeraet.py'
lines=(guard.ROOT/'AENDERUNGEN.diff').read_text().splitlines(keepends=True)
start=next(i for i,s in enumerate(lines) if s.startswith('diff --git a/'+path+' '))
end=next((i for i in range(start+1,len(lines)) if lines[i].startswith('diff --git ')),len(lines))
section=lines[start:end]
source=(guard.ROOT/'repo'/path).read_text().splitlines(keepends=True)
old=[]
pos=0
i=0
hunks=[]
while i<len(section):
    match=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',section[i])
    if not match:
        i+=1
        continue
    newstart=int(match.group(3))-1
    oldbody=[]
    newbody=[]
    header=section[i].strip()
    i+=1
    while i<len(section) and not section[i].startswith('@@ '):
        line=section[i]
        if line.startswith((' ','-')):
            oldbody.append(line[1:])
        if line.startswith((' ','+')):
            newbody.append(line[1:])
        i+=1
    assert source[newstart:newstart+len(newbody)]==newbody, header
    old+=source[pos:newstart]+oldbody
    pos=newstart+len(newbody)
    hunks.append(header)
old+=source[pos:]
module=ModuleType('review_baseline_measurement')
module.__package__='biotop.kern'
exec(compile(''.join(old),'<baseline-from-AENDERUNGEN.diff>','exec'),module.__dict__)
raw=json.loads((guard.OUT/'repro-raw.json').read_text())
case=raw['scope_cases'][0]
arguments=(case['baseline'],case['candidate_measurement_double'],case['baseline'],
           ['alpha','beta'],case['candidate_row']['wirkungskreis'],case['tausch'])
result={'provenance':'Exact reverse reconstruction from provided diff; original/review repo untouched',
        'hunks':hunks,'current':current.urteil_f2(*arguments),'baseline':module.urteil_f2(*arguments),
        'invalid_value_zero_current':None,'invalid_value_zero_baseline':module.rauschtoleranz_aus_werten([0.0]*5)}
try:
    result['invalid_value_zero_current']=current.rauschtoleranz_aus_werten([0.0]*5)
except Exception as e:
    result['invalid_value_zero_current']={'exception':type(e).__name__,'message':str(e)}
negotiation=json.loads((guard.OUT/'negotiation-raw.json').read_text())['cases'][0]
partner=negotiation['candidates'][0]
areas=list(partner['masse']['bereiche'])
args=(partner['masse']['_basis_paar'],partner['masse'],partner['masse']['_basis_paar'],areas,
      partner['wirkungskreis'],{'_gesperrte_bereiche':negotiation['blocked'],
                               '_rauschtoleranz':{b:1.15 for b in areas if b not in negotiation['blocked']}})
result['negotiation']={'baseline':module.urteil_f2(*args),'current':current.urteil_f2(*args)}
assert result['negotiation']['baseline']['ok'] is False
assert result['negotiation']['current']['ok'] is True
(guard.OUT/'baseline-comparison.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False,indent=2))
assert result['baseline']['ok'] is False
assert result['current']['ok'] is True
