import sys,json; sys.path.insert(0,'.'); from style import *
O='/workspace/llm-course/ch12-training-your-model/img/'
# shift
fig,ax=canvas(17,5); toks=['The','␣cat','␣sat','␣on','␣the','␣mat']
for i,t in enumerate(toks):
    if i<5: box(ax,0.6+i*2.7,3.2,2.2,0.9,t,ec=MINT,fs=18)
    if i>0: box(ax,0.6+(i-1)*2.7,0.9,2.2,0.9,t,ec=GOLD,fs=18)
for i in range(5): arrow(ax,1.7+i*2.7,3.15,1.7+i*2.7,1.85,c=FG)
ax.text(14.9,3.65,'inputs = ids[:, :-1]',fontsize=16,color=MINT); ax.text(14.9,1.35,'targets = ids[:, 1:]',fontsize=16,color=GOLD)
ax.text(8,4.6,'one sequence of 6 tokens → 5 next-token training examples (causal mask keeps it fair)',ha='center',fontsize=16); save(fig,O+'shift.png')
# loop
fig,ax=canvas(17,5.5); st=[('1  zero_grad',FG),('2  forward',MINT),('3  loss',GOLD),('4  backward',PINK),('(clip)',BLUE),('5  step',MINT)]
for i,(s,c) in enumerate(st):
    box(ax,0.3+i*2.8,2.3,2.3,1.2,s,ec=c,fs=18)
    if i<5: arrow(ax,2.6+i*2.8,2.9,3.1+i*2.8,2.9)
ax.add_patch(FancyArrowPatch((15.3,2.25),(1.4,2.25),connectionstyle='arc3,rad=-0.25',arrowstyle='-|>',mutation_scale=22,color=FG,lw=2))
ax.text(8.5,4.3,'+ scheduler.step() after optimizer.step()',ha='center',fontsize=16,color=GOLD); ax.text(8.5,0.2,'repeat for every batch',ha='center',fontsize=16); save(fig,O+'loop.png')
import numpy as np
# control loop
fig,ax=canvas(17,5.5)
for x,t,c in [(0.3,'target\n(next token)',FG),(3.6,'error signal\n= loss',GOLD),(6.9,'controller\n= AdamW',PINK),(10.2,'control action\n= weight update',BLUE),(13.5,'plant output\n= predictions',MINT)]:
    box(ax,x,2.2,2.9,1.4,t,ec=c,fs=16)
for x in [3.2,6.5,9.8,13.1]: arrow(ax,x,2.9,x+0.4,2.9)
ax.add_patch(FancyArrowPatch((15,2.15),(5,2.15),connectionstyle='arc3,rad=-0.3',arrowstyle='-|>',mutation_scale=22,color=MINT,lw=2,ls='--'))
ax.text(10,0.3,'feedback: compare predictions with targets again',ha='center',fontsize=15,color=MINT)
ax.text(8.5,4.6,'Training = a feedback control loop',ha='center',fontsize=19); save(fig,O+'control.png')
# -ln p
fig,ax=plt.subplots(figsize=(13,5.8)); p=np.linspace(0.001,1,400); ax.plot(p,-np.log(p),color=MINT,lw=3)
for pp,l,c in [(0.9,'90% on right token\nloss 0.11',MINT),(0.1,'10% on right token\nloss 2.30',GOLD),(0.01,'1% on right token\nloss 4.61',PINK)]:
    ax.scatter([pp],[-np.log(pp)],s=90,color=c,zorder=3); ax.annotate(l,(pp,-np.log(pp)),(pp+0.08,-np.log(pp)+0.8),fontsize=15,color=c)
ax.axhline(np.log(50257),color=GRID,ls='--'); ax.text(0.45,np.log(50257)-0.7,'uniform guess over 50,257 tokens → 10.82',fontsize=14)
ax.set_xlabel('probability the model gave the correct token'); ax.set_ylabel('cross-entropy = −ln p'); ax.set_ylim(0,11.5); ax.grid(color=GRID); save(fig,O+'xent.png')
# regimes
fig,axs=plt.subplots(1,3,figsize=(17,5)); x=np.arange(30)
cur=[(3+5*np.exp(-x/6),3.3+5*np.exp(-x/6),'healthy'),(2+6*np.exp(-x/5),np.r_[4+4*np.exp(-x[:12]/5),4+4*np.exp(-11/5)+0.05*(x[12:]-11)],'overfitting'),(7.5-0.3*np.log1p(x),7.6-0.3*np.log1p(x),'underfitting')]
for a,(t,v,n) in zip(axs,cur):
    a.plot(x,t,color=MINT,lw=3,label='train'); a.plot(x,v,color=GOLD,lw=3,label='val'); a.set_title(n); a.set_ylim(0,9); a.set_xticks([]); a.grid(color=GRID)
axs[0].legend(facecolor=BG,labelcolor=FG); axs[0].set_ylabel('loss'); save(fig,O+'regimes.png')
