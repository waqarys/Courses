import sys,math,json; sys.path.insert(0,'.'); from style import *; import numpy as np, torch, torch.nn as nn, torch.nn.functional as F
O='/workspace/llm-course/ch10-attention-is-all-you-need/img/'; R={}
torch.manual_seed(42)
# --- real tiny attention on 'The cat sat on the mat' (random weights, d_model=768, d_k=64)
toks=['The','cat','sat','on','the','mat']
E=torch.randn(1,6,768); Wq,Wk,Wv=[nn.Linear(768,64,bias=False) for _ in range(3)]
Q,K,V=Wq(E),Wk(E),Wv(E); S=(Q@K.transpose(-2,-1)).detach()[0]; Ss=S/8; W=F.softmax(Ss,-1)
mask=torch.tril(torch.ones(6,6)); Wm=F.softmax(Ss.masked_fill(mask==0,float('-inf')),-1)
R['raw_row0']=[round(x,2) for x in S[0].tolist()]; R['scaled_row0']=[round(x,2) for x in Ss[0].tolist()]; R['w_row0']=[round(x,3) for x in W[0].tolist()]; R['wm_row2']=[round(x,3) for x in Wm[2].tolist()]
def heat(ax,M,title,fmt='{:.2f}',cmap='viridis',vmin=None,vmax=None):
    im=ax.imshow(M,cmap=cmap,vmin=vmin,vmax=vmax); ax.set_xticks(range(6)); ax.set_yticks(range(6)); ax.set_xticklabels(toks,fontsize=16); ax.set_yticklabels(toks,fontsize=16); ax.set_title(title,fontsize=20)
    for i in range(6):
        for j in range(6):
            v=M[i][j]; ax.text(j,i,'-∞' if v==-np.inf else fmt.format(v),ha='center',va='center',fontsize=13,color='white' if (vmax is None or v<0.6*vmax) else 'black')
fig,axs=plt.subplots(1,3,figsize=(21,7.2))
heat(axs[0],S.numpy(),'1. raw scores  Q·Kᵀ',cmap='magma'); heat(axs[1],Ss.numpy(),'2. scaled  ÷ √64 = ÷8',cmap='magma'); heat(axs[2],W.detach().numpy(),'3. softmax (rows sum to 1)',vmin=0,vmax=1)
axs[0].set_ylabel('query (from)'); [a.set_xlabel('key (to)') for a in axs]; save(fig,O+'scores_steps.png')
fig,axs=plt.subplots(1,3,figsize=(21,7.2))
heat(axs[0],mask.numpy(),'causal mask (1 = allowed)',fmt='{:.0f}',cmap='Greens',vmin=0,vmax=1.6)
Sm=Ss.masked_fill(mask==0,float('-inf')).numpy(); heat(axs[1],Sm,'scaled scores after masked_fill',cmap='magma')
heat(axs[2],Wm.detach().numpy(),'softmax → future gets exactly 0',vmin=0,vmax=1); save(fig,O+'causal.png')
# --- dot product growth with d
ds=[2,4,8,16,32,64,128,256,512,768,1024]; raw=[];sc=[]
for d in ds:
    q=torch.randn(20000,d);k=torch.randn(20000,d);dp=(q*k).sum(-1); raw.append(dp.std().item()); sc.append((dp/math.sqrt(d)).std().item())
R['std']={d:round(r,2) for d,r in zip(ds,raw)}
fig,ax=plt.subplots(figsize=(14,6.3)); ax.plot(ds,raw,'o-',color=PINK,lw=3,label='std of q·k (unscaled)'); ax.plot(ds,np.sqrt(ds),'--',color=GOLD,label='√d (theory)'); ax.plot(ds,sc,'o-',color=MINT,lw=3,label='std of q·k / √d')
ax.set_xscale('log',base=2); ax.set_xlabel('dimension d'); ax.set_ylabel('standard deviation'); ax.legend(facecolor=BOX,labelcolor=FG); ax.grid(color=GRID); ax.set_title('Measured: dot products grow like √d — scaling keeps them ≈ 1')
save(fig,O+'dot_std.png')
x=torch.tensor([1.,2.,3.]); big=F.softmax(x*8,0).numpy(); small=F.softmax(x,0).numpy(); R['softmax_big']=big.round(4).tolist(); R['softmax_small']=small.round(3).tolist()
fig,axs=plt.subplots(1,2,figsize=(16,5.8))
for a,p,t,c in [(axs[0],small,'scores [1, 2, 3]  → spread out',MINT),(axs[1],big,'scores ×8 = [8, 16, 24] → winner takes all',PINK)]:
    a.bar(['tok A','tok B','tok C'],p,color=c); a.set_ylim(0,1.05); a.set_title(t); [a.text(i,v+0.02,f'{v:.3f}',ha='center') for i,v in enumerate(p)]; a.grid(axis='y',color=GRID)
save(fig,O+'softmax_sharp.png')
# --- GELU vs ReLU
xs=torch.linspace(-4,4,400); fig,ax=plt.subplots(figsize=(13,6)); ax.plot(xs,F.relu(xs),color=GOLD,lw=4,label='ReLU'); ax.plot(xs,F.gelu(xs),color=MINT,lw=4,label='GELU ≈ x·Φ(x)')
ax.axhline(0,color=GRID); ax.axvline(0,color=GRID); ax.legend(facecolor=BOX,labelcolor=FG); ax.grid(color=GRID); ax.set_title(f'GELU(−1) = {F.gelu(torch.tensor(-1.)).item():.3f}, ReLU(−1) = 0  ·  GELU(1) = {F.gelu(torch.tensor(1.)).item():.3f}')
save(fig,O+'gelu.png'); R['gelu']=[round(F.gelu(torch.tensor(v)).item(),4) for v in (-1.,1.,2.)]
# --- residual gradient experiment: 12 layers, measure grad at input
def gradnorm(res,n=12,d=256):
    torch.manual_seed(0); layers=[nn.Sequential(nn.LayerNorm(d),nn.Linear(d,d),nn.Tanh()) for _ in range(n)]
    x=torch.randn(8,d,requires_grad=True); h=x
    for L in layers: h=h+L(h) if res else L(h)
    h.pow(2).mean().backward(); return x.grad.norm().item()
R['grad_nores']=[round(gradnorm(False,n),5) for n in (1,6,12,24,48)]; R['grad_res']=[round(gradnorm(True,n),4) for n in (1,6,12,24,48)]
ns=list(range(0,25)); fig,ax=plt.subplots(figsize=(14,6)); ax.plot(ns,[0.5*0.8**n for n in ns],'o-',color=PINK,lw=3,label='no skip: 0.5 × 0.8ⁿ'); ax.plot(ns,[0.5]*len(ns),'o-',color=MINT,lw=3,label='skip path: gradient passes through "+" unchanged')
ax.set_xlabel('layers the gradient travels back through'); ax.set_ylabel('gradient size'); ax.legend(facecolor=BOX,labelcolor=FG); ax.grid(color=GRID); ax.set_title('Why residuals: 0.5 × 0.8¹² ≈ 0.034')
save(fig,O+'residual_grad.png')
# --- memory O(n^2)
ns2=[256,512,1024,2048,4096,8192]; mem=[8*12*n*n*4/1e9 for n in ns2]
fig,ax=plt.subplots(figsize=(14,6)); ax.bar([str(n) for n in ns2],mem,color=[MINT,MINT,MINT,GOLD,PINK,PINK]); [ax.text(i,v*1.05+0.1,f'{v:.2f} GB',ha='center',fontsize=17) for i,v in enumerate(mem)]
ax.set_xlabel('sequence length n'); ax.set_ylabel('GB (float32)'); ax.set_title('Attention score memory for ONE layer, batch=8, heads=12: 8·12·n²·4 bytes'); ax.grid(axis='y',color=GRID); save(fig,O+'memory.png')
# --- params bar
parts=[('QKV proj',768*2304),('out proj',768*768),('fc1 (+bias)',768*3072+3072),('fc2 (+bias)',3072*768+768),('2× LayerNorm',4*768)]
fig,ax=plt.subplots(figsize=(14,6)); ax.barh([p[0] for p in parts][::-1],[p[1]/1e6 for p in parts][::-1],color=[GRID,PINK,PINK,BLUE,MINT]); [ax.text(v/1e6+0.03,4-i,f'{v:,}',va='center',fontsize=17) for i,(n,v) in enumerate(parts)]
ax.set_xlabel('millions of parameters'); ax.set_title(f'One GPT-2-small block = {sum(p[1] for p in parts):,} parameters'); ax.set_xlim(0,3.1); save(fig,O+'params.png'); R['block_params']=sum(p[1] for p in parts)
# --- diagrams
fig,ax=canvas(18,7.5)
box(ax,0.2,3,2.8,1.6,'x\n(6, 768)',fs=22)
for i,(n,c,yy) in enumerate([('W_q',GOLD,5.6),('W_k',BLUE,3.1),('W_v',MINT,0.6)]):
    box(ax,4,yy,2.4,1.3,n+'\n768→64',ec=c,fs=19); arrow(ax,3,3.8,4,yy+0.65,c=c); box(ax,7.2,yy,2.2,1.3,['Q','K','V'][i]+'\n(6, 64)',ec=c,fs=20); arrow(ax,6.4,yy+0.65,7.2,yy+0.65,c=c)
box(ax,10.3,4.2,2.6,1.6,'scores\nQ·Kᵀ/√64\n(6, 6)',ec=PINK,fs=19); arrow(ax,9.4,6.2,10.3,5.3,c=GOLD); arrow(ax,9.4,3.75,10.3,4.6,c=BLUE)
box(ax,13.4,4.2,2.2,1.6,'mask +\nsoftmax\n(6, 6)',ec=PINK,fs=19); arrow(ax,12.9,5,13.4,5,c=PINK)
box(ax,15.6,1.8,2.3,1.6,'output\nweights·V\n(6, 64)',fc='#22665a',fs=19); arrow(ax,14.5,4.2,16.5,3.4,c=PINK); arrow(ax,9.4,1.25,15.6,2.4,c=MINT)
save(fig,O+'qkv_flow.png')
fig,ax=canvas(18,7.5)
box(ax,0.2,3,2.6,1.5,'x (2,6,768)',fs=19); arrow(ax,2.8,3.75,3.6,3.75)
box(ax,3.6,3,3,1.5,'qkv_proj\n(2,6,2304)',fs=19); arrow(ax,6.6,3.75,7.3,3.75)
for h in range(12):
    c=[GOLD,BLUE,MINT,PINK][h%4]; ax.add_patch(FancyBboxPatch((7.6+(h%6)*0.95,4.4 if h<6 else 2.2),0.8,1.6,boxstyle='round,pad=0.02',fc=BOX,ec=c,lw=2)); ax.text(7.6+(h%6)*0.95+0.4,(4.4 if h<6 else 2.2)+0.8,f'h{h}\n64',ha='center',va='center',fontsize=13)
ax.text(10.4,6.6,'12 heads × 64 dims, attention run in parallel',ha='center',fontsize=18,color=GOLD); ax.text(10.4,1.4,'(2, 12, 6, 64) per Q, K, V',ha='center',fontsize=18,color=BLUE)
arrow(ax,13.4,3.75,14.1,3.75); box(ax,14.1,3,1.9,1.5,'concat\n(2,6,768)',fs=17); arrow(ax,16,3.75,16.4,3.75); box(ax,16.4,3,1.5,1.5,'out_proj\n768',fs=16,fc='#22665a')
save(fig,O+'multihead.png')
fig,ax=canvas(12,13)
X=6; ys=[12,10.3,8.6,6.9,5.2,3.5,1.8,0.2]; labels=['x  (batch, seq, 768)','LayerNorm ln1','Multi-Head Attention (12 heads)','⊕  x + dropout(attn)','LayerNorm ln2','FeedForward 768→3072→768 (GELU)','⊕  x + dropout(ffn)','out (batch, seq, 768)']
cols=[BLUE,GOLD,PINK,MINT,GOLD,PINK,MINT,BLUE]
for y,l,c in zip(ys,labels,cols): box(ax,X-3.2,y,6.4,1.1,l,ec=c,fs=19)
for a,b in zip(ys[:-1],ys[1:]): arrow(ax,X,a,X,b+1.1)
ax.plot([X+3.2,X+4.3,X+4.3,X+3.2],[12.55,12.55,7.45,7.45],color=MINT,lw=3,ls='--'); ax.text(X+4.45,10,'skip',color=MINT,fontsize=18,rotation=90,va='center')
ax.plot([X+3.2,X+4.3,X+4.3,X+3.2],[7.3,7.3,2.35,2.35],color=MINT,lw=3,ls='--'); ax.text(X+4.45,4.8,'skip',color=MINT,fontsize=18,rotation=90,va='center')
save(fig,O+'block.png')
fig,axs=plt.subplots(1,2,figsize=(18,7.5))
for a,t,steps in [(axs[0],'Pre-norm (GPT-2)',['x','x + Attn(LN(x))','x + FFN(LN(x))','out']),(axs[1],'Post-norm (2017 paper)',['x','LN(x + Attn(x))','LN(x + FFN(x))','out'])]:
    a.axis('off'); a.set_xlim(0,10); a.set_ylim(0,10); a.set_title(t,fontsize=26,color=MINT if 'Pre' in t else GOLD)
    for i,s in enumerate(steps): box(a,2,8-i*2.6,6,1.4,s,fs=22,ec=MINT if 'Pre' in t else GOLD)
    for i in range(3): arrow(a,5,8-i*2.6,5,8-(i+1)*2.6+1.4)
axs[0].text(5,-0.6,'residual stream never passes through a norm',ha='center',fontsize=18,color=MINT); axs[1].text(5,-0.6,'every add is followed by a norm',ha='center',fontsize=18,color=GOLD)
save(fig,O+'prepost.png')
fig,ax=canvas(19,4.5)
st=[('text','"The cat sat\non the mat"'),('Ch 8 tokenizer','IDs (1, 6)'),('Ch 9 embeddings','(1, 6, 768)\nstatic'),('Ch 10 block ×12','(1, 6, 768)\ncontext-aware'),('Ch 11 LM head','logits\n(1, 6, 50257)'),('sample','next token')]
for i,(a,b) in enumerate(st):
    box(ax,0.2+i*3.15,0.8,2.7,2.4,a+'\n\n'+b,fs=17,ec=GOLD if 'Ch 10' in a else MINT,fc='#22665a' if 'Ch 10' in a else BOX)
    if i<5: arrow(ax,2.9+i*3.15,2,3.35+i*3.15,2)
save(fig,O+'pipeline.png')
json.dump(R,open(O+'../_build_numbers.json','w'),indent=1); print(json.dumps(R))
