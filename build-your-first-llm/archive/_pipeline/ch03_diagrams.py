import sys,json; sys.path.insert(0,'.'); from style import *; import numpy as np, torch
O='/workspace/llm-course/ch03-the-attention-mechanism/img/'; R={}
# RNN vs attention
fig,ax=canvas(17,6.5); ws=['The','cat','that','the','dog','chased','ran']
for i,w in enumerate(ws):
    box(ax,0.4+i*2.35,4.3,1.9,1.1,w,fs=19); 
    if i: arrow(ax,0.4+i*2.35-0.45,4.85,0.4+i*2.35,4.85)
    ax.add_patch(plt.Circle((1.35+i*2.35,3.6),0.25,color=MINT,alpha=1-i*0.13))
ax.text(8.5,2.9,'RNN: one fixed-size "sticky note" passed along — early words fade',ha='center',fontsize=19,color=PINK)
for i,w in enumerate(ws): box(ax,0.4+i*2.35,0.4,1.9,1.1,w,fs=19,ec=GOLD if w in('cat','ran') else GRID)
for i in range(6): ax.annotate('',xy=(1.35+i*2.35,1.5),xytext=(1.35+6*2.35,1.5),arrowprops=dict(arrowstyle='->',color=GOLD,lw=4 if i==1 else 1,connectionstyle='arc3,rad=0.35'))
ax.text(8.5,2.25,'Attention: "ran" reaches every word directly',ha='center',fontsize=19,color=GOLD); save(fig,O+'rnn_vs_attn.png')
# library QKV
fig,ax=canvas(17,6)
box(ax,0.3,2.3,3.4,1.6,'Query\n"about cats?"',ec=GOLD,fs=20)
books=[('Feline Biology',.46),('Dog Training',.08),('Cat Psychology',.41),('Medieval History',.05)]
for i,(b,w) in enumerate(books):
    y=4.8-i*1.45; box(ax,5.2,y,3.8,1.1,'Key: '+b,ec=MINT if w>.3 else GRID,fs=16); arrow(ax,3.7,3.1,5.2,y+0.55)
    ax.text(9.3,y+0.55,f'weight {w:.2f}',fontsize=17,va='center',color=MINT if w>.3 else FG)
    box(ax,11.3,y,2.6,1.1,'Value',ec=MINT if w>.3 else GRID,fs=16)
box(ax,14.5,2.3,2.3,1.6,'Σ weight\n× Value',ec=PINK,fs=19); [arrow(ax,13.9,4.8-i*1.45+0.55,14.5,3.1) for i in range(4)]
save(fig,O+'library.png')
# projections
fig,ax=canvas(16,6); box(ax,0.4,2.4,3.4,1.4,'embedding x\n[2, 4, 1]',fs=20)
for i,(n,c) in enumerate([('Q = x·W_Q',GOLD),('K = x·W_K',MINT),('V = x·W_V',PINK)]):
    y=4.5-i*2; arrow(ax,3.8,3.1,6.5,y+0.6); box(ax,6.5,y,3.8,1.2,n,ec=c,fs=20)
ax.text(10.9,3.1,'one Q entry:\n2×0.5 + 4×0.25 + 1×1.0\n= 1 + 1 + 1 = 3',fontsize=20,va='center',color=GOLD); save(fig,O+'qkv_proj.png')
# softmax example
toks=['The','cat','sat','on','the','mat']; s=np.array([0.1,0.8,0.4,0.2,0.1,0.5]); w=np.exp(s)/np.exp(s).sum(); R['softmax']=w.round(3).tolist()
fig,(a1,a2)=plt.subplots(1,2,figsize=(16,5.5)); a1.bar(toks,s,color=BLUE); a1.set_title('Step 1: raw scores  q_sat · k_j'); a2.bar(toks,w,color=[GOLD if t=='cat' else MINT for t in toks]); a2.set_title('Step 2: softmax → weights (sum = 1)')
for i,v in enumerate(w): a2.text(i,v+0.005,f'{v:.2f}',ha='center',fontsize=17)
for a in (a1,a2): a.grid(axis='y',color=GRID)
save(fig,O+'softmax_example.png')
# scaling demo
rng=np.random.default_rng(0); rows=[]
for d in [4,64,768]:
    q=rng.standard_normal((2000,d)); k=rng.standard_normal((2000,d)); dots=(q*k).sum(1); rows.append((d,dots.std(),(dots/np.sqrt(d)).std()))
R['scale']=[(d,round(a,2),round(b,2)) for d,a,b in rows]
sc=rng.standard_normal((6,768))@rng.standard_normal(768); 
def sm(x): e=np.exp(x-x.max()); return e/e.sum()
fig,(a1,a2)=plt.subplots(1,2,figsize=(16,5.5)); a1.bar(range(6),sm(sc),color=PINK); a1.set_title(f'd=768, unscaled: max weight {sm(sc).max():.2f}'); a2.bar(range(6),sm(sc/np.sqrt(768)),color=MINT); a2.set_title(f'scaled by 1/√768: max weight {sm(sc/np.sqrt(768)).max():.2f}')
R['scale_max']=(round(float(sm(sc).max()),3),round(float(sm(sc/np.sqrt(768)).max()),3))
for a in (a1,a2): a.set_ylim(0,1.05); a.set_xlabel('key position'); a.grid(axis='y',color=GRID)
save(fig,O+'scaling.png')
# numpy toy attention heatmap (my own)
torch.manual_seed(0); x=torch.randn(6,8); Wq,Wk,Wv=[torch.randn(8,8)/8**.5 for _ in range(3)]
Q,K,V=x@Wq,x@Wk,x@Wv; A=torch.softmax(Q@K.T/8**.5,-1)
# GPT-2 real attention
from transformers import GPT2Tokenizer,GPT2Model
tok=GPT2Tokenizer.from_pretrained('gpt2'); m=GPT2Model.from_pretrained('gpt2',attn_implementation='eager',output_attentions=True).eval()
def att(s):
    ids=tok(s,return_tensors='pt'); 
    with torch.no_grad(): o=m(**ids)
    return [tok.decode([i]) for i in ids['input_ids'][0]], torch.stack(o.attentions)[:,0]  # L,H,T,T
t,a=att('The cat sat on the mat'); avg=a[4:8].mean((0,1)).numpy()
fig,ax=plt.subplots(figsize=(10,8.5)); ax.imshow(avg,cmap='magma'); ax.set_xticks(range(len(t))); ax.set_yticks(range(len(t))); ax.set_xticklabels(t,fontsize=18); ax.set_yticklabels(t,fontsize=18)
for i in range(len(t)):
    for j in range(len(t)):
        if j<=i: ax.text(j,i,f'{avg[i,j]:.2f}',ha='center',va='center',fontsize=14,color='white' if avg[i,j]<0.5 else 'black')
ax.set_xlabel('key (attended to)'); ax.set_ylabel('query'); ax.set_title('Real GPT-2 attention (layers 5–8, all heads, averaged)'); save(fig,O+'gpt2_heatmap.png')
R['gpt2_sat_row']=dict(zip(t,avg[2].round(3).tolist()))
# heads differ: layer 5 four heads
fig,axs=plt.subplots(1,4,figsize=(19,5.5))
for ax,h in zip(axs,[0,1,5,9]):
    ax.imshow(a[4,h].numpy(),cmap='magma'); ax.set_xticks(range(len(t))); ax.set_xticklabels(t,rotation=60,fontsize=13); ax.set_yticks(range(len(t))); ax.set_yticklabels(t,fontsize=13); ax.set_title(f'layer 5 · head {h}',fontsize=17)
save(fig,O+'gpt2_heads.png')
# cake freezer: attention from "it" (excluding first token sink), best head + avg
res={}
for adj in ['warm','cold']:
    t2,a2=att(f'I put the cake in the freezer because it was {adj}.')
    it=t2.index(' it'); ic,ifr=t2.index(' cake'),t2.index(' freezer'); row=a2[:,:,it]
    res[adj]=dict(avg_cake=round(float(row[:,:,ic].mean()),3),avg_freezer=round(float(row[:,:,ifr].mean()),3))
R['cake']=res
t3,a3=att('The cat chased the mouse because it was hungry'); it=t3.index(' it'); row=a3[:,:,it]
R['catmouse']=dict(cat=round(float(row[:,:,t3.index(' cat')].mean()),3),mouse=round(float(row[:,:,t3.index(' mouse')].mean()),3))
# multi-head diagram
fig,ax=canvas(17,6); box(ax,0.3,2.5,2.6,1.2,'x (768)',fs=20)
for i in range(4):
    y=5-i*1.45; arrow(ax,2.9,3.1,4.2,y+0.5); box(ax,4.2,y,3.6,1.0,f'head {i+1}: Q,K,V (64)',ec=[GOLD,MINT,PINK,BLUE][i],fs=16); arrow(ax,7.8,y+0.5,9.3,3.1)
ax.text(5.9,-0.1,'… 12 heads in GPT-2 small (12 × 64 = 768)',ha='center',fontsize=17)
box(ax,9.3,2.5,3,1.2,'concat (768)',fs=19); arrow(ax,12.3,3.1,13.4,3.1); box(ax,13.4,2.5,3.3,1.2,'output proj W_O',ec=MINT,fs=18); save(fig,O+'multihead.png')
# self vs cross
fig,ax=canvas(17,6)
for i,tk in enumerate('ABC'): box(ax,0.5+i*2.2,1.0,1.6,1.0,tk,fs=22)
for i in range(3):
    for j in range(3): ax.annotate('',xy=(1.3+j*2.2,2.0),xytext=(1.3+i*2.2,2.0),arrowprops=dict(arrowstyle='->',color=GOLD,connectionstyle='arc3,rad=-0.5',lw=1.6))
ax.text(3.5,4.8,'Self-attention\nQ, K, V from the same sequence',ha='center',fontsize=19,color=GOLD)
for i,tk in enumerate(['E1','E2','E3']): box(ax,9.5+i*2.4,0.6,1.8,1.0,tk,fs=20,ec=MINT)
for i,tk in enumerate(['D1','D2','D3']): box(ax,9.5+i*2.4,3.2,1.8,1.0,tk,fs=20,ec=PINK)
for i in range(3):
    for j in range(3): arrow(ax,10.4+i*2.4,3.2,10.4+j*2.4,1.6)
ax.text(12.8,5.0,'Cross-attention: Q from decoder,\nK & V from encoder',ha='center',fontsize=19,color=PINK); save(fig,O+'self_cross.png')
# quadratic cost
n=np.array([512,1024,2048,4096,8192]); fig,ax=plt.subplots(figsize=(13,6)); ax.bar([str(x) for x in n],n**2/1e6,color=PINK); [ax.text(i,v+0.8,f'{v:.1f}M',ha='center',fontsize=16) for i,v in enumerate(n**2/1e6)]
ax.set_xlabel('sequence length (tokens)'); ax.set_ylabel('pairwise scores (millions)'); ax.set_title('Attention cost grows with n²: double the length → 4× the scores'); ax.grid(axis='y',color=GRID); save(fig,O+'quadratic.png')
json.dump(R,open(O+'../_numbers.json','w'),indent=1,default=float); print(json.dumps(R,default=float))
