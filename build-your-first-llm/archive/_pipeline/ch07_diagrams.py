import sys,json,re,unicodedata,hashlib,random; sys.path.insert(0,'.'); from style import *; import numpy as np
from collections import Counter
O='/workspace/llm-course/ch07-preparing-your-data/img/'; G='/workspace/llm-course/_src/gutenberg/'; R={}
# pipeline
fig,ax=canvas(17,4.5); st=['raw text','clean','dedup','split','chunk','JSONL']
for i,s in enumerate(st):
    box(ax,0.3+i*2.8,1.5,2.3,1.4,s,ec=[FG,MINT,GOLD,PINK,BLUE,MINT][i],fs=20)
    if i<5: arrow(ax,2.6+i*2.8,2.2,3.1+i*2.8,2.2)
ax.text(8.5,0.5,'a bug at any stage is inherited by every later stage → check after each one',ha='center',fontsize=17,color=GOLD); save(fig,O+'pipeline.png')
# overlap
fig,ax=canvas(17,5)
for i,(s,c) in enumerate([(0,MINT),(600,GOLD),(1200,PINK),(1800,BLUE)]):
    e=min(s+800,2000); ax.add_patch(plt.Rectangle((0.5+s/2000*15,3.6-i*0.85),(e-s)/2000*15,0.6,color=c,alpha=0.6)); ax.text(0.5+s/2000*15+0.1,3.75-i*0.85,f'chunk {i+1}: {s}–{e}',fontsize=15)
for x in [600,1200,1800]: ax.axvline(0.5+x/2000*15,color=FG,ls=':',lw=1)
ax.text(8.5,0.2,'max_chars=800, overlap=200 → stride 600; 2,000 chars → 4 chunks (last one 200 chars, already inside chunk 3)',ha='center',fontsize=15,color=GOLD); save(fig,O+'overlap.png')
# real experiment
def strip_gb(t):
    a=t.find('*** START'); a=t.find('\n',a); b=t.find('*** END'); return t[a:b]
def clean_text(text):
    text=unicodedata.normalize("NFKC",text); text=re.sub(r"<[^>]+>"," ",text); text=re.sub(r"[\r\t]"," ",text); return re.sub(r"\s+"," ",text).strip()
docs={}
for f,n in [('time_machine.txt','The Time Machine'),('war_worlds.txt','The War of the Worlds'),('invisible_man.txt','The Invisible Man')]:
    raw=open(G+f,encoding='utf-8').read(); body=strip_gb(raw)
    paras=[clean_text(p) for p in re.split(r'\n\s*\n',body)]; paras=[p for p in paras if p]
    docs[n]=dict(raw=len(raw),body=len(body),paras=paras)
R['docs']={n:dict(raw_chars=d['raw'],body_chars=d['body'],paragraphs=len(d['paras'])) for n,d in docs.items()}
allp=[p for d in docs.values() for p in d['paras']]; hs=[hashlib.sha1(p.encode()).hexdigest() for p in allp]
R['dup_rate_paragraphs']=round(1-len(set(hs))/len(hs),4); dups=Counter(allp).most_common(5); R['top_dups']=[(p[:40],c) for p,c in dups if c>1]
short=sum(len(p)<40 for p in allp); R['short_paras_lt40']=short
def chunk_text(text,max_chars=800,overlap=200):
    ch=[];s=0
    while s<len(text):
        e=min(len(text),s+max_chars); c=text[s:e].strip()
        if c: ch.append(c)
        s+=max_chars-overlap
    return ch
lens={}
for n,d in docs.items():
    seen=set(); keep=[]
    for p in d['paras']:
        h=hashlib.sha1(p.encode()).hexdigest()
        if h in seen or len(p)<40: continue
        seen.add(h); keep.append(p)
    d['chunks']=chunk_text("\n\n".join(keep)); lens[n]=[len(c) for c in d['chunks']]
R['chunks']={n:len(v) for n,v in lens.items()}
# chars/token
from transformers import GPT2TokenizerFast
tok=GPT2TokenizerFast.from_pretrained('gpt2'); sample=" ".join(docs['The Time Machine']['chunks'][:200])
R['chars_per_token']=round(len(sample)/len(tok(sample)['input_ids']),2)
toks=[len(tok(c)['input_ids']) for c in docs['The Time Machine']['chunks']]; R['tokens_per_800chunk']=(min(toks),round(float(np.mean(toks)),1),max(toks))
# top words
words=" ".join(docs['The Time Machine']['chunks']).lower().split(); R['top10']=Counter(words).most_common(10)
fig,ax=plt.subplots(figsize=(13,6)); ax.hist(toks,bins=30,color=MINT); ax.axvline(512,color=PINK,lw=2,ls='--'); ax.text(500,ax.get_ylim()[1]*0.8,'512-token context',color=PINK,fontsize=17,ha='right')
ax.set_xlabel('GPT-2 tokens per 800-char chunk'); ax.set_title(f'The Time Machine (public domain): {len(toks)} chunks, mean {np.mean(toks):.0f} tokens, {R["chars_per_token"]} chars/token'); ax.grid(color=GRID); save(fig,O+'tokens_hist.png')
# split by document: 3 docs
R['note']='3 books = 3 documents; split by document'
# leakage demo: dedup after vs before
json.dump(R,open(O+'../_numbers.json','w'),indent=1,default=str); print(json.dumps(R,default=str)[:3000])
