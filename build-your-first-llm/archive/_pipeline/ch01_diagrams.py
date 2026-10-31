import sys; sys.path.insert(0,'.'); from style import *; import numpy as np
O='/workspace/llm-course/ch01-what-is-ai/img/'
# 1 rule-based vs ML
fig,ax=canvas(16,7)
ax.text(4,6.5,'Traditional programming',ha='center',fontsize=26,color=GOLD,weight='bold')
ax.text(12,6.5,'Machine learning',ha='center',fontsize=26,color=MINT,weight='bold')
box(ax,1,4.3,2.6,1.2,'Rules\n(hand-written)',ec=GOLD); box(ax,4.4,4.3,2.6,1.2,'Data',ec=GOLD)
box(ax,2.5,2.2,3,1.2,'Program',ec=GOLD); box(ax,2.5,0.2,3,1.2,'Answers',ec=GOLD)
arrow(ax,2.3,4.3,3.4,3.4); arrow(ax,5.7,4.3,4.6,3.4); arrow(ax,4,2.2,4,1.4)
box(ax,9,4.3,2.6,1.2,'Data\n(emails)'); box(ax,12.4,4.3,2.6,1.2,'Answers\n(labels)')
box(ax,10.5,2.2,3,1.2,'Training'); box(ax,10.5,0.2,3,1.2,'Rules\n(learned patterns)')
arrow(ax,10.3,4.3,11.4,3.4); arrow(ax,13.7,4.3,12.6,3.4); arrow(ax,12,2.2,12,1.4)
ax.plot([8,8],[0,6.8],color=GRID,lw=2); save(fig,O+'rules_vs_ml.png')
# 2 spam toy: learned word weights
fig,ax=plt.subplots(figsize=(14,6))
words=['FREE','winner','$$$','urgent','meeting','invoice','lunch','report']; w=[2.1,1.8,1.6,1.2,-1.3,-0.6,-1.5,-1.1]
ax.barh(words[::-1],w[::-1],color=[PINK if x>0 else MINT for x in w[::-1]]); ax.axvline(0,color=FG,lw=1)
ax.set_xlabel('learned weight (positive → spam, negative → not spam)'); ax.set_title('Toy spam filter: weights it discovered from labelled emails')
save(fig,O+'spam_weights.png')
# 3 line fitting: real gradient descent
rng=np.random.default_rng(0); x=np.linspace(0,5,40); y=3*x+2+rng.normal(0,1.2,40)
wgt,b=4.5,0.4; lr=0.02; hist=[(wgt,b)]
for step in range(400):
    p=wgt*x+b; e=p-y; wgt-=lr*2*(e*x).mean(); b-=lr*2*e.mean(); hist.append((wgt,b))
hist=np.array(hist)
fig,axs=plt.subplots(1,2,figsize=(16,6.2))
for a,(ww,bb,t) in zip(axs,[(4.5,0.4,'Before training: w=4.5, b=0.4'),(hist[-1,0],hist[-1,1],f'After 400 steps: w={hist[-1,0]:.2f}, b={hist[-1,1]:.2f}')]):
    a.scatter(x,y,color=BLUE,s=40); a.plot(x,ww*x+bb,color=MINT,lw=4); a.set_title(t); a.set_xlabel('x'); a.set_ylabel('y'); a.grid(color=GRID)
save(fig,O+'line_fit.png')
fig,ax=plt.subplots(figsize=(14,6)); ax.plot(hist[:,0],color=GOLD,lw=4,label='weight w (slope)'); ax.plot(hist[:,1],color=MINT,lw=4,label='bias b (intercept)')
ax.axhline(3,color=GOLD,ls='--',lw=1.5); ax.axhline(2,color=MINT,ls='--',lw=1.5); ax.set_xlabel('training step'); ax.legend(facecolor=BOX,labelcolor=FG); ax.grid(color=GRID); ax.set_title('Learning = nudging two numbers to reduce error (true values dashed)')
save(fig,O+'wb_steps.png')
loss=[((hh[0]*x+hh[1]-y)**2).mean() for hh in hist]
fig,ax=plt.subplots(figsize=(14,5.5)); ax.plot(loss,color=PINK,lw=4); ax.set_yscale('log'); ax.set_xlabel('training step'); ax.set_ylabel('mean squared error'); ax.grid(color=GRID); ax.set_title('The error shrinks as the numbers are adjusted')
save(fig,O+'loss.png')
open(O+'fit_numbers.txt','w').write(f'final w={hist[-1,0]:.3f} b={hist[-1,1]:.3f} loss0={loss[0]:.2f} lossN={loss[-1]:.2f} step10 w={hist[10,0]:.2f} b={hist[10,1]:.2f}')
# 4 nested hierarchy
fig,ax=canvas(16,9)
for r,c,t,yy in [(4.3,'#1d2b42','Artificial Intelligence',8.25),(3.3,'#1f3b4f','Machine Learning',7.25),(2.3,'#1f4d55','Deep Learning',6.25),(1.25,'#22665a','Large Language\nModels',4.6)]:
    ax.add_patch(Circle((8,4.5-(4.3-r)*0.0),r,fc=c,ec=MINT,lw=2.5)); ax.text(8,yy if r>1.3 else 4.5,t,ha='center',va='center',fontsize=26 if r>1.3 else 22,weight='bold',color=GOLD if r<1.3 else FG)
ax.text(13.3,7.2,'rules, search,\nchess engines',fontsize=18,color=BLUE); ax.text(13.3,5.0,'learns from data\n(spam filters)',fontsize=18,color=BLUE)
ax.text(0.2,5.0,'many-layer\nneural networks',fontsize=18,color=BLUE); ax.text(0.2,3.0,'predict the\nnext token',fontsize=18,color=BLUE)
save(fig,O+'hierarchy.png')
# 5 timeline
ev=[(1950,'Turing Test'),(1956,'"AI" coined\n(Dartmouth)'),(1974,'AI winter'),(1997,'Deep Blue\nbeats Kasparov'),(2012,'AlexNet'),(2017,'Transformer\npaper'),(2018,'GPT-1\n117M'),(2020,'GPT-3\n175B'),(2022,'ChatGPT')]
fig,ax=plt.subplots(figsize=(18,6)); ax.axis('off'); ax.set_xlim(1945,2027); ax.set_ylim(-3,3); ax.plot([1946,2026],[0,0],color=MINT,lw=4)
for i,(yr,t) in enumerate(ev):
    up=1 if i%2==0 else -1; ax.plot([yr,yr],[0,1.1*up],color=GRID,lw=2); ax.scatter([yr],[0],s=160,color=GOLD if yr==2017 else MINT,zorder=3)
    ax.text(yr,1.35*up,f'{yr}\n{t}' if up>0 else f'{t}\n{yr}',ha='center',va='bottom' if up>0 else 'top',fontsize=17,color=GOLD if yr==2017 else FG)
save(fig,O+'timeline.png')
# 6 LLM vs product
fig,ax=canvas(16,7.5)
box(ax,5.5,2.6,5,2.2,'Base LLM\npredicts the next token',fc='#22665a',fs=24,bold=True)
for (x,y,t) in [(0.3,5.6,'Web search\n(fresh facts)'),(11.7,5.6,'Code interpreter\n(exact math)'),(0.3,0.3,'Memory\n(across chats)'),(11.7,0.3,'Document retrieval\n(RAG)'),(6,5.8,'Chat interface\n+ system prompt')]:
    box(ax,x,y,4,1.5,t,ec=GOLD); arrow(ax,x+2 if x!=6 else 8, y if y>4 else y+1.5, 8 if x==6 else (5.5 if x<5 else 10.5), 4.8 if y>4 else 2.6,c=GOLD,style='<|-|>')
ax.text(8,0.6,'The product = LLM + tools',ha='center',fontsize=24,color=MINT,weight='bold'); save(fig,O+'llm_vs_product.png')
# 7 next token probabilities (illustrative)
fig,ax=plt.subplots(figsize=(14,6)); toks=['mat','floor','sofa','roof','moon']; p=[0.46,0.21,0.17,0.12,0.04]
ax.bar(toks,p,color=[MINT,BLUE,BLUE,BLUE,PINK]); ax.set_ylabel('probability'); ax.set_title('"The cat sat on the ___"  (illustrative next-token probabilities)')
for i,v in enumerate(p): ax.text(i,v+0.01,f'{v:.2f}',ha='center',fontsize=20)
ax.grid(axis='y',color=GRID); save(fig,O+'next_token.png')
# 8 lossy compression
fig,ax=canvas(16,6)
box(ax,0.3,1.5,4.2,3,'Training text\n~10 trillion tokens\n(tens of TB)',ec=BLUE,fs=22)
box(ax,6,2,3.8,2,'Model weights\nbillions of numbers\n(GBs)',fc='#22665a',fs=22)
box(ax,11.3,1.5,4.4,3,'Answer = reconstruction\nmostly right,\nsometimes a plausible\nbut wrong guess',ec=PINK,fs=21)
arrow(ax,4.6,3,5.9,3); arrow(ax,9.9,3,11.2,3); ax.text(5.25,3.4,'compress',ha='center',fontsize=17,color=GOLD); ax.text(10.55,3.4,'generate',ha='center',fontsize=17,color=GOLD)
save(fig,O+'lossy.png')
# 9 AI formula
fig,ax=canvas(16,4.5)
for i,(t,c) in enumerate([('Statistics',BLUE),('Lots of data',GOLD),('Computing power',PINK)]): box(ax,0.3+i*5.3,1.2,4.4,2,t,ec=c,fs=28,bold=True)
for i in range(2): ax.text(4.95+i*5.3,2.2,'+',fontsize=48,ha='center',va='center',color=FG)
save(fig,O+'formula.png')
# 10 training loop
fig,ax=canvas(16,7)
pts=[(6,5.3,'1. Predict'),(11,3,'2. Measure error\n(loss)'),(6,0.5,'3. Nudge the numbers\n(gradient step)'),(1,3,'4. Repeat\n(billions of times)')]
for x,y,t in pts: box(ax,x,y,4,1.4,t,fs=22)
arrow(ax,10,5.9,12.5,4.5); arrow(ax,12.5,3,10,1.3); arrow(ax,6,1.2,3.2,3); arrow(ax,3.2,4.4,6,5.9)
save(fig,O+'train_loop.png')
print(open(O+'fit_numbers.txt').read())
