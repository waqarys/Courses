import sys; sys.path.insert(0,'.'); from style import *; import numpy as np
O='/workspace/llm-course/ch08-building-the-tokenizer/img/'
# pipeline
fig,ax=canvas(17,4.2); st=[('"Hello, world!"',FG),('[15496, 11,\n995, 0]',MINT),('vectors\n(Ch 9)',GOLD),('Transformer\n(Ch 10–11)',PINK),('probabilities',BLUE),('decode → text',MINT)]
for i,(s,c) in enumerate(st):
    box(ax,0.2+i*2.85,1.4,2.45,1.4,s,ec=c,fs=15)
    if i<5: arrow(ax,2.65+i*2.85,2.1,3.05+i*2.85,2.1)
ax.text(1.4,3.3,'encode',ha='center',color=MINT,fontsize=17); ax.text(15.6,3.3,'decode',ha='center',color=MINT,fontsize=17)
ax.text(8.5,0.5,'the tokenizer is the front door and the back door of the model',ha='center',fontsize=17,color=GOLD); save(fig,O+'pipeline.png')
# three splits of "tokenization"
fig,ax=canvas(17,6.5)
rows=[('character',list('tokenization'),MINT,'12 tokens · vocab ~100'),('word',['tokenization'],GOLD,'1 token · vocab ~100k+ (or <UNK>)'),('subword (cl100k)',['token','ization'],PINK,'2 tokens · vocab ~100k')]
for r,(n,toks,c,cap) in enumerate(rows):
    y=5-r*2; ax.text(0.2,y+0.3,n,fontsize=19,color=c,weight='bold'); x=4.2
    for t in toks:
        w=0.75 if len(t)==1 else 0.6+0.36*len(t); box(ax,x,y,w,0.8,t,ec=c,fs=17); x+=w+0.08
    ax.text(0.2,y-0.35,cap,fontsize=14,color=FG)
save(fig,O+'three_ways.png')
# BPE merges
corpus=['low']*3+['lower']+['newest']*2
words=[list(w) for w in corpus]; from collections import Counter; steps=[]
for k in range(5):
    pc=Counter()
    for w in words:
        for a,b in zip(w,w[1:]): pc[(a,b)]+=1
    (a,b),n=pc.most_common(1)[0]; steps.append((a,b,n))
    nw=[]
    for w in words:
        o=[];i=0
        while i<len(w):
            if i<len(w)-1 and w[i]==a and w[i+1]==b: o.append(a+b); i+=2
            else: o.append(w[i]); i+=1
        nw.append(o)
    words=nw; steps[-1]=steps[-1]+([' '.join(x) for x in words],)
fig,ax=canvas(17,8.5); ax.text(0.2,8.0,'corpus: low low low lower newest newest  (my redraw, computed in code)',fontsize=17,color=GOLD)
for i,(a,b,n,ws) in enumerate(steps):
    y=6.9-i*1.45; box(ax,0.2,y,4.2,1.0,f'step {i+1}: {a}+{b} → {a+b}  (×{n})',ec=PINK,fs=16)
    uniq=[];[uniq.append(w) for w in ws if w not in uniq]
    ax.text(4.8,y+0.5,'   |   '.join(uniq),fontsize=17,va='center',family='DejaVu Sans Mono')
save(fig,O+'bpe_merges.png'); print(steps)
# vocab sweep (my experiment)
vs=[500,1000,2000,5000]; cpt=[2.49,2.91,3.36,3.86]; ntok=[448129,383663,332443,289150]
fig,ax=plt.subplots(figsize=(13,6)); ax.plot(vs,cpt,'o-',color=MINT,lw=3,ms=10)
for v,c,n in zip(vs,cpt,ntok): ax.annotate(f'{c} chars/token\n{n:,} tokens',(v,c),textcoords='offset points',xytext=(10,-45),fontsize=14,color=FG)
ax.axhline(1,color=PINK,ls='--'); ax.text(3200,1.1,'character-level = 1.0',color=PINK,fontsize=15)
ax.set_xscale('log'); ax.minorticks_off(); ax.set_xticks(vs); ax.set_xticklabels([str(v) for v in vs]); ax.set_ylim(0,4.5)
ax.set_xlabel('BPE vocab size (trained on TinyShakespeare, 1.1M chars)'); ax.set_ylabel('chars per token'); ax.set_title('Bigger vocab → shorter sequences (my run)'); ax.grid(color=GRID); save(fig,O+'vocab_sweep.png')
# leading space
fig,ax=canvas(17,4.5)
for i,(t,idn,c) in enumerate([('Hello','9906',MINT),('␣Hello','22691',GOLD),('world','14957',MINT),('␣world','1917',GOLD)]):
    box(ax,0.4+i*4.2,1.8,3.6,1.5,f'{t}\nID {idn}',ec=c,fs=20)
ax.text(8.5,0.6,'cl100k_base: the space is part of the token → different IDs (verified with tiktoken)',ha='center',fontsize=16,color=FG); save(fig,O+'space.png')
