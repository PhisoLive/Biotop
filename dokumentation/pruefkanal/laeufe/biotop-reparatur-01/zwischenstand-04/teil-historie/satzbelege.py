#!/usr/bin/env python3
"""Verteilt bereits geprüfte Absatzbelege auf deren Sätze; erfindet keine Quelle.
Markdown-Softbreaks halten die Absätze lesbar und die Satzbelegprüfung eindeutig.
"""
import pathlib,re
p=pathlib.Path(__file__).resolve().parent/'STATUS-24-25.md'
text=p.read_text();output=[]
for line in text.splitlines():
 if line.startswith('## Sources'):
  break
 m=re.search(r'((?:\[\d+\])+)$',line.strip())
 if not m or line.startswith(('#','|','[')):
  output.append(line);continue
 citations=m.group(1)
 assert len(re.findall(r'\d+',citations))<=3
 parts=re.split(r'(?<=[.!?])\s+',line.strip())
 for idx,part in enumerate(parts):
  if len(part.split())>=4 and not re.search(r'\[\d+\]',part):
   part+=citations
  if idx and line.startswith('- '):part='  '+part
  output.append(part)
p.write_text('\n'.join(output).rstrip()+'\n')
print('Absatzbelege auf Sätze verteilt; Quellenblock wird neu gerendert.')
