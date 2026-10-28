#!/usr/bin/env python
"""Build script.md, frames, narration, video.mp4, captions.srt, timings.json from slides.md.
Narration lives in each slide as <!-- say: ... --> (Marp presenter note)."""
import re,sys,os,json,hashlib,subprocess,numpy as np,soundfile as sf,shutil
ch=os.path.abspath(sys.argv[1]); P=os.path.dirname(os.path.abspath(__file__))
VOICE=os.environ.get('VOICE','am_michael'); SPEED=float(os.environ.get('SPEED','1.0')); PAUSE=0.6; SR=24000
src=open(f'{ch}/slides.md').read()
m=re.match(r'^---\n.*?\n---\n',src,re.S); body=src[m.end():]
slides=re.split(r'\n---\n',body)
items=[]
for i,s in enumerate(slides,1):
    say=re.findall(r'<!--\s*say:(.*?)-->',s,re.S)
    if not say: sys.exit(f'slide {i} has no narration')
    t=' '.join(x.strip() for x in say); t=re.sub(r'\s+',' ',t)
    h=re.search(r'^#\s+(.+)$',s,re.M); title=h.group(1).strip() if h else f'Slide {i}'
    div='_class: divider' in s or '_class: lead' in s
    vis=re.sub(r'<!--.*?-->','',s,flags=re.S); lines=[l for l in vis.strip().split('\n') if l.strip()]
    codel=sum(len(b.split('\n'))-2 for b in re.findall(r'```.*?```',vis,re.S))
    if len(lines)>19 or codel>17: print(f'WARN dense slide {i} ({title}): {len(lines)} lines, {codel} code lines')
    items.append(dict(n=i,title=title,say=t,divider=div))
print(len(items),'slides')
# script.md
title=re.search(r'^#\s+(.+)$',body,re.M).group(1)
with open(f'{ch}/script.md','w') as f:
    f.write(f'# Narration script — {title}\n\nOne block per slide, in order. Generated from the `say:` notes in slides.md.\n\n')
    for it in items: f.write(f"## Slide {it['n']} — {it['title']}\n\n{it['say']}\n\n")
B=f'{ch}/_build'; os.makedirs(B+'/frames',exist_ok=True); os.makedirs(P+'/ttscache',exist_ok=True)
if not os.environ.get('SKIPRENDER'):
    for f in os.listdir(B+'/frames'): os.remove(B+'/frames/'+f)
    subprocess.run(['marp','--theme-set',P+'/theme.css','--images','png','--allow-local-files','-o',B+'/frames/s.png',f'{ch}/slides.md'],check=True,cwd=ch)
frames=sorted(f for f in os.listdir(B+'/frames') if f.endswith('.png'))
assert len(frames)==len(items),(len(frames),len(items))
from kokoro_onnx import Kokoro
k=None
def fix(t):  # pronunciation helpers for TTS only
    rep={'Q·K^T':'Q times K transpose','QKᵀ':'Q K transpose','K^T':'K transpose','√':'square root of ','d_k':'d k','d_model':'d model','d_head':'d head','d_ff':'d f f','LLMs':'L L Ms','LLM':'L L M','GPT-2':'G P T 2','GPT-3':'G P T 3','GPT-4':'G P T 4','GELU':'gelu','softmax':'soft-max','numpy':'num pie','NumPy':'num pie','PyTorch':'pie torch','e.g.':'for example','i.e.':'that is','→':' to ','×':' by ','≈':' about ','—':', ','nn.Linear':'n n dot Linear'}
    for a,b in rep.items(): t=t.replace(a,b)
    return t
audio=[]; t0=0.0; srt=[]; tim=[]
def ts(x): h=int(x//3600);m_=int(x%3600//60);s=x%60; return f'{h:02d}:{m_:02d}:{int(s):02d},{int((s%1)*1000):03d}'
for it in items:
    key=hashlib.md5((VOICE+str(SPEED)+fix(it['say'])).encode()).hexdigest()
    cp=f'{P}/ttscache/{key}.wav'
    if not os.path.exists(cp):
        if k is None: k=Kokoro('/workspace/tts/kokoro-v1.0.onnx','/workspace/tts/voices-v1.0.bin')
        s,sr=k.create(fix(it['say']),voice=VOICE,speed=SPEED,lang='en-us'); sf.write(cp,s,sr)
    a,_=sf.read(cp); a=np.concatenate([np.zeros(int(0.25*SR)),a,np.zeros(int(PAUSE*SR))])
    d=len(a)/SR; audio.append(a)
    sents=[x for x in re.split(r'(?<=[.!?])\s+',it['say']) if x]; tot=sum(len(x) for x in sents); c=t0+0.25
    for x in sents:
        dd=(d-0.25-PAUSE)*len(x)/tot; srt.append((c,c+dd,x)); c+=dd
    tim.append(dict(slide=it['n'],title=it['title'],start=round(t0,2),dur=round(d,2),divider=it['divider'])); t0+=d
    print(it['n'],round(d,1),end='; ',flush=True)
sf.write(B+'/audio.wav',np.concatenate(audio),SR)
with open(B+'/list.txt','w') as f:
    for fr,tm in zip(frames,tim): f.write(f"file 'frames/{fr}'\nduration {tm['dur']:.3f}\n")
    f.write(f"file 'frames/{frames[-1]}'\n")
with open(f'{ch}/captions.srt','w') as f:
    for i,(a,b,x) in enumerate(srt,1): f.write(f'{i}\n{ts(a)} --> {ts(b)}\n{x}\n\n')
json.dump(tim,open(f'{ch}/timings.json','w'),indent=1)
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',B+'/list.txt','-i',B+'/audio.wav','-vf','fps=30,format=yuv420p,scale=1920:1080','-c:v','libx264','-preset','medium','-tune','stillimage','-crf','23','-c:a','aac','-b:a','128k','-ar','48000','-shortest','-movflags','+faststart',f'{ch}/video.mp4'],check=True,cwd=B)
print('\nTOTAL',round(t0,1),'s')
