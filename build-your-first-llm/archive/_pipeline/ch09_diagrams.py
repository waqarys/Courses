import sys,json; sys.path.insert(0,'.'); from style import *; import numpy as np, torch, torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer
O='/workspace/llm-course/ch09-the-embedding-layer/img/'; R={}
tok=AutoTokenizer.from_pretrained('gpt2'); m=AutoModel.from_pretrained('gpt2'); E=m.wte.weight.detach(); P=m.wpe.weight.detach()
for w in ['cat',' cat','kitten',' kitten',' dog',' car','mat',' mat']: R['id'+w]=tok.encode(w)
def sim(word,k=6):
    i=tok.encode(word)[0]; s=F.cosine_similarity(E[i:i+1],E,dim=1); s[i]=-1; idx=s.argsort(descending=True)[:k]
    return [(tok.decode([int(j)]),round(float(s[j]),3)) for j in idx]
for w in [' king',' computer',' happy',' Python',' doctor',' fast']: R['nn'+w]=sim(w)
def ana(a,b,c,k=5):
    ia,ib,ic=[tok.encode(x)[0] for x in (a,b,c)]; v=E[ia]-E[ib]+E[ic]; s=F.cosine_similarity(v[None],E,dim=1)
    for i in (ia,ib,ic): s[i]=-1
    idx=s.argsort(descending=True)[:k]; return [(tok.decode([int(j)]),round(float(s[j]),3)) for j in idx]
R['ana king']=ana(' king',' man',' woman'); R['ana paris']=ana(' Paris',' France',' Germany')
R['wte_std']=round(float(E.std()),4); R['wpe_std']=round(float(P.std()),4)
R['cos cat kitten']=round(float(F.cosine_similarity(E[3797],E[tok.encode(' kitten')[0]],dim=0)),3)
R['cos cat dog']=round(float(F.cosine_similarity(E[3797],E[4273],dim=0)),3); R['cos cat car']=round(float(F.cosine_similarity(E[3797],E[1097],dim=0)),3)
R['params wte']=E.numel(); R['params wpe']=P.numel(); R['total']=sum(p.numel() for p in m.parameters())
json.dump(R,open(O+'../_numbers.json','w'),indent=1); print(json.dumps(R,indent=0))
# position similarity heatmap
Pn=F.normalize(P,dim=1); S=(Pn@Pn.T).numpy()
fig,ax=plt.subplots(figsize=(9,8)); im=ax.imshow(S[:256,:256],cmap='viridis'); fig.colorbar(im); ax.set_title('GPT-2 wpe cosine similarity (pos 0–255)',fontsize=20); ax.set_xlabel('position'); ax.set_ylabel('position'); save(fig,O+'pos_heatmap.png')
# few wpe dims as curves
fig,ax=plt.subplots(figsize=(13,5.5))
for d,c in zip([0,1,2,3],[MINT,GOLD,PINK,BLUE]): ax.plot(P[:,d].numpy(),color=c,lw=1.5,label=f'dim {d}')
ax.set_xlabel('position'); ax.set_ylabel('value'); ax.set_title('GPT-2 learned position vectors: smooth, slowly varying curves'); ax.legend(fontsize=14); ax.grid(color=GRID); save(fig,O+'pos_curves.png')
# lookup diagram
fig,ax=canvas(17,6.5)
rows=['0  !','1  "','…','464  The','…','3797  ␣cat','…','50256  <|endoftext|>']
for i,r in enumerate(rows):
    hl= '3797' in r; box(ax,6.5,5.6-i*0.72,4.2,0.6,r,ec=GOLD if hl else GRID,fs=14,tc=GOLD if hl else FG)
    for j in range(8): ax.add_patch(plt.Rectangle((11.0+j*0.6,5.65-i*0.72),0.5,0.5,color=MINT if hl else BOX,alpha=0.9 if hl else 1))
box(ax,0.3,3.0,4.5,1.1,'token ID 3797',ec=GOLD,fs=19); arrow(ax,4.9,3.55,6.4,2.35,c=GOLD)
ax.text(13.3,6.4,'768 numbers per row',ha='center',fontsize=15,color=MINT); ax.text(8.6,6.4,'50,257 rows',ha='center',fontsize=15,color=FG)
ax.text(8.5,-0.1,'nn.Embedding = weight[token_id]  — no maths, just pick a row',ha='center',fontsize=17,color=GOLD); save(fig,O+'lookup.png')
# token + position add
fig,ax=canvas(17,5)
for k,(lab,c) in enumerate([('token "cat"\n(what)',MINT),('position 1\n(where)',PINK),('input vector\n(what + where)',GOLD)]):
    x=0.5+k*5.8; ax.text(x+1.9,4.4,lab,ha='center',fontsize=16,color=c)
    for j in range(8): ax.add_patch(plt.Rectangle((x+j*0.48,2.3),0.42,0.9,color=c,alpha=0.35+0.08*j))
ax.text(5.0,2.7,'+',fontsize=40,ha='center',va='center'); ax.text(10.8,2.7,'=',fontsize=40,ha='center',va='center')
ax.text(8.5,0.8,'same 768 dims · element-wise sum · shape stays (batch, seq, 768)',ha='center',fontsize=17,color=FG); save(fig,O+'add.png')
