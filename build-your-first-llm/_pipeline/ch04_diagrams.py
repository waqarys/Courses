import sys,json,math; sys.path.insert(0,'.'); from style import *; import numpy as np, torch
O='/workspace/llm-course/ch04-the-transformer-architecture/img/'; R={}
# permutation equivariance demo (my own)
torch.manual_seed(0); x=torch.randn(5,16); W=[torch.randn(16,16)/4 for _ in range(3)]
def att(x): Q,K,V=x@W[0],x@W[1],x@W[2]; return torch.softmax(Q@K.T/4,-1)@V
p=torch.tensor([4,2,0,3,1]); R['perm_equiv']=bool(torch.allclose(att(x)[p],att(x[p]),atol=1e-6))
# sinusoidal
def sinus(n,d):
    pe=np.zeros((n,d)); pos=np.arange(n)[:,None]; div=np.exp(np.arange(0,d,2)*(-math.log(10000.0)/d)); pe[:,0::2]=np.sin(pos*div); pe[:,1::2]=np.cos(pos*div); return pe
pe=sinus(100,128)
fig,(a1,a2)=plt.subplots(1,2,figsize=(18,6.5),gridspec_kw={'width_ratios':[1.4,1]})
im=a1.imshow(pe.T,aspect='auto',cmap='RdBu'); a1.set_xlabel('position'); a1.set_ylabel('dimension'); a1.set_title('Sinusoidal encodings (d=128): fast → slow waves')
for i,c in zip([0,10,40],[GOLD,MINT,PINK]): a2.plot(pe[:,i],color=c,lw=2.5,label=f'dim {i}')
a2.legend(facecolor=BOX,labelcolor=FG); a2.set_xlabel('position'); a2.set_title('three "clock hands"'); a2.grid(color=GRID); save(fig,O+'sinusoidal.png')
# similarity of sinusoidal positions
pn=pe/np.linalg.norm(pe,axis=1,keepdims=True); S=pn@pn.T
# GPT-2 learned positions
from transformers import GPT2LMHeadModel,GPT2Tokenizer
tok=GPT2Tokenizer.from_pretrained('gpt2'); m=GPT2LMHeadModel.from_pretrained('gpt2').eval()
wpe=m.transformer.wpe.weight.detach().numpy(); R['wpe_shape']=list(wpe.shape)
wn=wpe/np.linalg.norm(wpe,axis=1,keepdims=True); S2=wn[:200]@wn[:200].T
fig,(a1,a2)=plt.subplots(1,2,figsize=(17,7.5))
a1.imshow(S[:100,:100],cmap='magma'); a1.set_title('sinusoidal: cos-sim between positions'); a2.imshow(S2[:100,:100],cmap='magma'); a2.set_title('GPT-2 learned wpe (1024×768): cos-sim')
for a in (a1,a2): a.set_xlabel('position'); a.set_ylabel('position')
save(fig,O+'pos_similarity.png')
R['wpe_cos_0_1']=round(float(wn[10]@wn[11]),3); R['wpe_cos_10_90']=round(float(wn[10]@wn[90]),3)
# GELU vs ReLU
xs=torch.linspace(-4,4,400); g=torch.nn.functional.gelu(xs); r=torch.relu(xs)
R['gelu']={v:round(float(torch.nn.functional.gelu(torch.tensor(v))),3) for v in [2.0,-2.0,-0.5]}
fig,ax=plt.subplots(figsize=(13,7)); ax.plot(xs,r,color=PINK,lw=3,label='ReLU'); ax.plot(xs,g,color=MINT,lw=3,label='GELU')
for v,c in R['gelu'].items(): ax.scatter([v],[c],color=GOLD,s=120,zorder=4); ax.text(v+0.1,c+0.25,f'GELU({v:g}) = {c:.3f}',fontsize=17,color=GOLD)
ax.legend(facecolor=BOX,labelcolor=FG,fontsize=18); ax.grid(color=GRID); ax.set_title('ReLU cuts negatives to 0; GELU is smooth (small negative tail)'); save(fig,O+'gelu.png')
# FFN diagram
fig,ax=canvas(17,6)
box(ax,0.3,2.4,2.6,1.3,'768',fs=24); arrow(ax,2.9,3.05,4.2,3.05); box(ax,4.2,0.6,2.8,4.9,'Linear\n768→3072\n(expand)',ec=BLUE,fs=18)
arrow(ax,7.0,3.05,8.2,3.05); box(ax,8.2,0.6,2.6,4.9,'GELU\n(×3072\n"judges")',ec=GOLD,fs=18); arrow(ax,10.8,3.05,12.0,3.05)
box(ax,12.0,0.6,2.8,4.9,'Linear\n3072→768\n(contract)',ec=BLUE,fs=18); arrow(ax,14.8,3.05,15.6,3.05); ax.text(15.7,3.05,'768',fontsize=24,va='center')
save(fig,O+'ffn.png')
R['ffn_shapes']=[tuple(m.transformer.h[0].mlp.c_fc.weight.shape),tuple(m.transformer.h[0].mlp.c_proj.weight.shape)]
# linear collapse demo
A=torch.randn(4,4);B=torch.randn(4,4);v=torch.randn(4); R['linear_collapse']=bool(torch.allclose(B@(A@v),(B@A)@v,atol=1e-5))
# signal decay & growth
L=np.arange(0,97); fig,ax=plt.subplots(figsize=(13,6.5)); ax.plot(L,0.99**L,color=PINK,lw=3,label='0.99ⁿ (degradation) → 0.38 at 96'); ax.plot(L,1.01**L,color=GOLD,lw=3,label='1.01ⁿ (growth) → 2.60 at 96'); ax.axhline(1,color=MINT,ls='--',lw=2,label='residual + norm: stays ~1')
ax.legend(facecolor=BOX,labelcolor=FG,fontsize=17); ax.set_xlabel('layers'); ax.grid(color=GRID); ax.set_title('Why depth needs residuals and normalisation'); save(fig,O+'depth.png')
R['pow']=(round(0.99**96,3),round(1.01**96,3))
# residual diagram
fig,ax=canvas(16,5.5); box(ax,0.3,2,2.4,1.4,'x',fs=26); arrow(ax,2.7,2.7,5,2.7); box(ax,5,2,4,1.4,'f(x)\nattention or FFN',ec=GOLD,fs=19); arrow(ax,9,2.7,11.2,2.7)
ax.add_patch(plt.Circle((11.8,2.7),0.55,fill=False,ec=MINT,lw=3)); ax.text(11.8,2.7,'+',fontsize=34,ha='center',va='center',color=MINT); arrow(ax,12.35,2.7,14,2.7); ax.text(14.2,2.7,'x + f(x)',fontsize=24,va='center')
ax.annotate('',xy=(11.8,3.25),xytext=(1.5,3.4),arrowprops=dict(arrowstyle='->',color=MINT,lw=3,connectionstyle='arc3,rad=-0.35')); ax.text(6.8,5.0,'skip connection (the highway)',ha='center',fontsize=19,color=MINT); save(fig,O+'residual.png')
# layernorm example
x4=torch.tensor([102.5,98.3,105.7,95.2]); ln=torch.nn.functional.layer_norm(x4,(4,)); R['ln']=ln.numpy().round(2).tolist()
rms=x4/x4.pow(2).mean().sqrt(); R['rms']=rms.numpy().round(3).tolist()
# layer diagram pre-norm
fig,ax=canvas(10,12)
y=0.3; box(ax,3,y,4,0.9,'input x',fs=19)
steps=[('LayerNorm',GRID),('Multi-head attention',GOLD),('+  (residual)',MINT),('LayerNorm',GRID),('Feed-forward (768→3072→768)',BLUE),('+  (residual)',MINT)]
ys=[]
for i,(s,c) in enumerate(steps):
    yy=1.9+i*1.6; arrow(ax,5,yy-0.7,5,yy); box(ax,1.5,yy,7,0.9,s,ec=c,fs=18); ys.append(yy)
arrow(ax,5,ys[-1]+0.9,5,ys[-1]+1.5); ax.text(5,ys[-1]+1.8,'output (same shape) → next layer',ha='center',fontsize=18)
ax.annotate('',xy=(8.5,ys[2]+0.45),xytext=(7,0.75),arrowprops=dict(arrowstyle='->',color=MINT,lw=2.5,connectionstyle='arc3,rad=0.4'))
ax.annotate('',xy=(8.5,ys[5]+0.45),xytext=(8.5,ys[2]+0.6),arrowprops=dict(arrowstyle='->',color=MINT,lw=2.5,connectionstyle='arc3,rad=-0.4'))
save(fig,O+'layer.png')
# post vs pre
fig,ax=canvas(17,5)
for k,(t,seq) in enumerate([('Post-Norm (2017)',['x','Attn','+x','LN']),('Pre-Norm (GPT-2 onward)',['x','LN','Attn','+x'])]):
    ax.text(0.3,4.3-k*2.4,t,fontsize=20,color=GOLD)
    for i,s in enumerate(seq): box(ax,5+i*3,3.6-k*2.4,2.2,1.0,s,fs=19,ec=GRID if s!='LN' else MINT); 
    for i in range(3): arrow(ax,7.2+i*3,4.1-k*2.4,8+i*3,4.1-k*2.4)
save(fig,O+'pre_post.png')
# param breakdown GPT-2
c=lambda mod: sum(p.numel() for p in mod.parameters())
tf=m.transformer; blk=tf.h[0]
R['params']=dict(total=c(tf),wte=tf.wte.weight.numel(),wpe=tf.wpe.weight.numel(),attn_per_layer=c(blk.attn),mlp_per_layer=c(blk.mlp),ln_per_layer=c(blk.ln_1)+c(blk.ln_2),layers=len(tf.h))
P=R['params']; parts={'token emb (wte)':P['wte'],'pos emb (wpe)':P['wpe'],'attention ×12':12*P['attn_per_layer'],'FFN ×12':12*P['mlp_per_layer'],'LayerNorms':12*P['ln_per_layer']+c(tf.ln_f)}
fig,ax=plt.subplots(figsize=(14,6)); ks=list(parts); vs=[parts[k]/1e6 for k in ks]; ax.barh(ks[::-1],vs[::-1],color=[GRID,BLUE,GOLD,PINK,MINT][::-1])
for i,v in enumerate(vs[::-1]): ax.text(v+0.5,i,f'{v:.2f}M',va='center',fontsize=17)
ax.set_xlabel('parameters (millions)'); ax.set_title(f'Real GPT-2 small: {P["total"]/1e6:.1f}M parameters'); ax.grid(axis='x',color=GRID); save(fig,O+'gpt2_params.png')
# inference: next-token
ids=tok('The capital of France is',return_tensors='pt')
with torch.no_grad(): lg=m(**ids).logits[0,-1]
pr=torch.softmax(lg,-1); top=torch.topk(pr,6); R['next']=[(tok.decode([i]),round(float(p),3)) for p,i in zip(top.values,top.indices)]
# greedy 8 tokens
with torch.no_grad(): g=m.generate(**ids,max_new_tokens=8,do_sample=False,pad_token_id=50256)
R['greedy']=tok.decode(g[0])
fig,ax=plt.subplots(figsize=(13,6)); ws=[w for w,_ in R['next']]; ps=[p for _,p in R['next']]; ax.barh([repr(w) for w in ws][::-1],ps[::-1],color=MINT); [ax.text(p+0.002,5-i,f'{p:.3f}',va='center',fontsize=17) for i,p in enumerate(ps)]
ax.set_title('GPT-2 small: P(next token | "The capital of France is")'); ax.grid(axis='x',color=GRID); save(fig,O+'next_token.png')
# causal mask
M=np.tril(np.ones((5,5))); fig,ax=plt.subplots(figsize=(8,7)); t=['The','cat','sat','on','mat']; ax.imshow(M,cmap='Greens',vmin=-0.3,vmax=1.2)
for i in range(5):
    for j in range(5): ax.text(j,i,'✓' if M[i,j] else '✗',ha='center',va='center',fontsize=24,color='black' if M[i,j] else PINK)
ax.set_xticks(range(5)); ax.set_yticks(range(5)); ax.set_xticklabels(t,fontsize=18); ax.set_yticklabels(t,fontsize=18); ax.set_xlabel('can attend to'); ax.set_ylabel('query'); ax.set_title('Decoder (causal) mask'); save(fig,O+'causal.png')
# encoder/decoder family
fig,ax=canvas(17,5.5)
for i,(t,s,c) in enumerate([('Encoder-only','BERT · full visibility\nclassification, NER, retrieval',MINT),('Decoder-only','GPT, Llama, Claude · causal\ngeneration (and much more)',GOLD),('Encoder–decoder','original Transformer, T5\ntranslation, summarisation',PINK)]):
    box(ax,0.4+i*5.6,1.0,5.0,3.4,t+'\n\n'+s,ec=c,fs=18)
save(fig,O+'families.png')
json.dump(R,open(O+'../_numbers.json','w'),indent=1,default=str); print(json.dumps(R,default=str))
