import sys,json,time; sys.path.insert(0,'.'); from style import *; import numpy as np, torch, torch.nn as nn, torch.nn.functional as F
O='/workspace/llm-course/ch06-numpy-pytorch-survival-guide/img/'; R={}
# shape ladder
fig,ax=canvas(17,6)
lab=[('scalar','3.14','()'),('vector','[0.1, 0.2, 0.3]','(3,)'),('matrix','rows × cols','(batch, seq)'),('3-D tensor','stack of matrices','(batch, seq, d_model)'),('4-D tensor','cabinet of stacks','(batch, heads, seq, seq)')]
for i,(a,b,c) in enumerate(lab):
    box(ax,0.2+i*3.4,2.2,3.0,2.0,a+'\n'+b,ec=[FG,MINT,GOLD,PINK,BLUE][i],fs=16); ax.text(1.7+i*3.4,1.5,c,ha='center',fontsize=15,family='monospace',color=[FG,MINT,GOLD,PINK,BLUE][i])
save(fig,O+'ladder.png')
# 1D->2D->3D
fig,ax=canvas(17,6.5)
box(ax,0.3,4.5,4.5,0.9,'[2, 3, 4, 6]   shape (4,)',fs=17,ec=MINT); arrow(ax,4.8,4.95,5.8,4.95)
box(ax,5.8,4.0,4.8,1.9,'[[2, 3, 4, 6],\n [5, 7, 8, 9]]   (2, 4)',fs=17,ec=GOLD); arrow(ax,10.6,4.95,11.6,4.95)
box(ax,11.6,3.5,5.2,2.9,'each ID → 768 numbers\n(2, 4, 768)\n[batch, token, feature]',fs=17,ec=PINK)
ax.text(8.5,2.4,'filing cabinet: drawer = sentence · folder = token · page = feature',ha='center',fontsize=18)
ax.text(8.5,1.3,'+ heads → (2, 8, 4, 4) attention scores',ha='center',fontsize=18,color=BLUE); save(fig,O+'dims.png')
# broadcasting
fig,ax=canvas(17,6); a=np.arange(1,13).reshape(3,4); b=np.array([10,20,30,40])
def grid(x0,y0,M,ec,dash=False):
    for i in range(M.shape[0]):
        for j in range(M.shape[1]): ax.add_patch(plt.Rectangle((x0+j*0.9,y0-i*0.9),0.85,0.85,fill=False,ec=ec,lw=2,ls='--' if (dash and i>0) else '-')); ax.text(x0+j*0.9+0.42,y0-i*0.9+0.42,str(M[i,j]),ha='center',va='center',fontsize=16)
grid(0.4,4,a,BLUE); ax.text(2.2,5.1,'a (3, 4)',ha='center',fontsize=18); ax.text(4.4,3.1,'+',fontsize=34)
grid(5.3,4,np.tile(b,(3,1)),GOLD,True); ax.text(7.1,5.1,'b (4,) → virtually (3, 4)',ha='center',fontsize=18); ax.text(9.3,3.1,'=',fontsize=34)
grid(10.2,4,a+b,MINT); ax.text(12,5.1,'result (3, 4)',ha='center',fontsize=18)
ax.text(8.5,0.6,'rules, right-to-left: equal, or one of them is 1, or missing (treated as 1)',ha='center',fontsize=18,color=GOLD); save(fig,O+'broadcast.png')
# broadcasting experiments
A=torch.randn(4,3,768); R['ex1_a']=list((A+torch.randn(768)).shape); R['ex1_b']=list((A+torch.randn(3,768)).shape)
try: A+torch.randn(4,768); R['ex1_c']='ok'
except RuntimeError as e: R['ex1_c']=str(e).split('\n')[0]
x=torch.randn(2,5,512); h=x.reshape(2,5,8,64).permute(0,2,1,3); R['ex2']=list((h@h.transpose(-2,-1)).shape); R['ex2_contig']=h.is_contiguous()
try: h.view(2,8,320); R['view_err']='ok'
except RuntimeError as e: R['view_err']=str(e)[:90]
# zero-copy
na=np.array([1,2,3]); pt=torch.from_numpy(na); na[0]=999; R['shared']=pt.tolist(); R['dtypes']=(str(np.array([1.0]).dtype),str(torch.tensor([1.0]).dtype))
# manual vs sdpa
torch.manual_seed(0); Q,K,V=[torch.randn(2,5,64) for _ in range(3)]
m=torch.triu(torch.ones(5,5),1).bool(); s=(Q@K.transpose(-2,-1)/8).masked_fill(m,float('-inf')); man=torch.softmax(s,-1)@V
R['sdpa_match']=bool(torch.allclose(man,F.scaled_dot_product_attention(Q,K,V,is_causal=True),atol=1e-5))
# timing CPU at bigger size
Q,K,V=[torch.randn(4,12,512,64) for _ in range(3)]
def tm(f,n=10):
    f(); t=time.perf_counter(); [f() for _ in range(n)]; return (time.perf_counter()-t)/n*1000
mk=torch.triu(torch.ones(512,512),1).bool()
t1=tm(lambda: torch.softmax((Q@K.transpose(-2,-1)/8).masked_fill(mk,float('-inf')),-1)@V); t2=tm(lambda: F.scaled_dot_product_attention(Q,K,V,is_causal=True))
R['timing_ms']=(round(t1,1),round(t2,1))
# ex3 tiny MLP one step
torch.manual_seed(0); model=nn.Sequential(nn.Linear(10,20),nn.ReLU(),nn.Linear(20,5)); opt=torch.optim.Adam(model.parameters(),lr=1e-2); lf=nn.CrossEntropyLoss()
xx=torch.randn(16,10); yy=torch.randint(0,5,(16,)); 
with torch.no_grad(): l0=lf(model(xx),yy).item()
opt.zero_grad(); loss=lf(model(xx),yy); loss.backward(); gn=torch.nn.utils.clip_grad_norm_(model.parameters(),1.0); opt.step()
with torch.no_grad(): l1=lf(model(xx),yy).item()
R['ex3']=dict(before=round(l0,4),after=round(l1,4),grad_norm_before_clip=round(float(gn),4),clipped=bool(gn>1.0))
# training curve longer
torch.manual_seed(42); model=nn.Sequential(nn.Linear(16,32),nn.ReLU(),nn.Linear(32,2)); opt=torch.optim.Adam(model.parameters(),lr=1e-3)
xi=torch.randn(64,16); yi=torch.randint(0,2,(64,)); L=[]
for e in range(300):
    opt.zero_grad(set_to_none=True); loss=lf(model(xi),yi); loss.backward(); torch.nn.utils.clip_grad_norm_(model.parameters(),1.0); opt.step(); L.append(loss.item())
with torch.no_grad(): acc=(model(xi).argmax(-1)==yi).float().mean().item()
R['curve']=dict(first=round(L[0],4),at3=round(L[2],4),last=round(L[-1],4),acc=round(acc,3))
fig,ax=plt.subplots(figsize=(13,6)); ax.plot(L,color=MINT,lw=3); ax.axvline(3,color=GOLD,ls='--'); ax.text(6,L[0],'the notebook stops here (3 epochs)',color=GOLD,fontsize=17)
ax.set_xlabel('step (same 64 random examples)'); ax.set_ylabel('cross-entropy loss'); ax.set_title(f'Same loop, 300 steps: loss {L[0]:.3f} → {L[-1]:.3f}, train acc {acc:.2f} (memorising noise)'); ax.grid(color=GRID); save(fig,O+'train_curve.png')
# training loop diagram
fig,ax=canvas(17,5.5)
st=['1 zero_grad()','2 forward\nlogits = model(x)','3 loss_fn(logits, y)','4 loss.backward()','+ clip_grad_norm_','5 optimizer.step()']
for i,s in enumerate(st):
    box(ax,0.2+i*2.8,2.0,2.5,1.7,s,ec=GOLD if s.startswith('+') else MINT,fs=15)
    if i<5: arrow(ax,2.7+i*2.8,2.85,3.0+i*2.8,2.85)
ax.annotate('',xy=(1.45,3.7),xytext=(15.45,3.7),arrowprops=dict(arrowstyle='->',color=PINK,lw=2.5,connectionstyle='arc3,rad=0.25')); ax.text(8.5,5.0,'repeat',ha='center',fontsize=19,color=PINK); save(fig,O+'loop.png')
# autograd graph
fig,ax=canvas(16,5)
box(ax,0.3,2,3,1.3,'x = [2, 3]\nrequires_grad',ec=MINT,fs=17); arrow(ax,3.3,2.65,5.2,2.65); box(ax,5.2,2,3,1.3,'y = x²\n[4, 9]',fs=18); arrow(ax,8.2,2.65,10.1,2.65); box(ax,10.1,2,3,1.3,'z = y.sum()\n13',fs=18)
ax.annotate('',xy=(1.8,1.9),xytext=(11.6,1.9),arrowprops=dict(arrowstyle='->',color=PINK,lw=2.5,connectionstyle='arc3,rad=0.3')); ax.text(6.7,0.25,'backward(): dz/dx = 2x = [4, 6]',ha='center',fontsize=19,color=PINK); save(fig,O+'autograd.png')
# view vs reshape memory
fig,ax=canvas(16,5.2)
for i in range(12): ax.add_patch(plt.Rectangle((0.4+i*1.2,3.4),1.1,0.9,fill=False,ec=MINT,lw=2)); ax.text(0.95+i*1.2,3.85,str(i),ha='center',va='center',fontsize=17)
ax.text(8,4.8,'memory: 0 1 2 … 11 (contiguous) → view() just relabels',ha='center',fontsize=18,color=MINT)
order=np.arange(12).reshape(3,4).T.flatten()
for i,v in enumerate(order): ax.add_patch(plt.Rectangle((0.4+i*1.2,1.0),1.1,0.9,fill=False,ec=PINK,lw=2)); ax.text(0.95+i*1.2,1.45,str(v),ha='center',va='center',fontsize=17)
ax.text(8,0.3,'x.T reads 0 4 8 1 5 9 … (strided) → view() fails, reshape() copies',ha='center',fontsize=18,color=PINK); save(fig,O+'contig.png')
json.dump(R,open(O+'../_numbers.json','w'),indent=1,default=str); print(json.dumps(R,default=str))
