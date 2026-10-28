import sys,json; sys.path.insert(0,'.'); from style import *; import numpy as np
from gensim.models import KeyedVectors
O='/workspace/llm-course/ch02-how-computers-understand-words/img/'; R={}
# ascii
fig,ax=plt.subplots(figsize=(15,5.5)); ws=['cat','car','kitten','feline']
for i,w in enumerate(ws):
    codes=[ord(c) for c in w]; ax.plot(range(len(codes)),codes,'o-',lw=3,ms=10,label=f'{w} = {codes}',color=[MINT,PINK,GOLD,BLUE][i])
ax.legend(facecolor=BOX,labelcolor=FG,fontsize=16); ax.set_xlabel('character position'); ax.set_ylabel('ASCII code'); ax.grid(color=GRID); ax.set_title('ASCII: "cat" ≈ "car" (spelling), but "cat" ≠ "kitten" (meaning)')
save(fig,O+'ascii.png')
# 2D word space
P={'boy':(1,2),'man':(1,7),'grandfather':(1,9.5),'girl':(9,2),'woman':(9,7),'grandmother':(9,9.5),'baby':(5,0.5)}
fig,ax=plt.subplots(figsize=(13,8))
for w,(x,y) in P.items(): ax.scatter(x,y,s=260,color=BLUE if x<5 else PINK if x>5 else GOLD,zorder=3); ax.text(x+0.25,y+0.25,w,fontsize=20)
ax.annotate('',xy=(1,7),xytext=(1,2),arrowprops=dict(arrowstyle='<->',color=MINT,lw=2)); ax.text(0.2,4.4,'5.0',color=MINT,fontsize=20)
ax.annotate('',xy=(9,7),xytext=(1,2),arrowprops=dict(arrowstyle='<->',color=GOLD,lw=2)); ax.text(5.2,4.0,'√(8²+5²) ≈ 9.43',color=GOLD,fontsize=20)
ax.set_xlabel('"gender" axis (illustrative)'); ax.set_ylabel('"age" axis (illustrative)'); ax.set_xlim(-0.5,11.5); ax.set_ylim(-0.5,11); ax.grid(color=GRID); ax.set_title('A toy 2-D word space: position = meaning')
save(fig,O+'wordspace2d.png')
# 3D
from mpl_toolkits.mplot3d import Axes3D
P3={'boy':(1,2,0),'girl':(9,2,0),'man':(1,7,0),'woman':(9,7,0),'prince':(1,2,9),'princess':(9,2,9),'king':(1,7,9.5),'queen':(9,7,9.5)}
fig=plt.figure(figsize=(12,9)); ax=fig.add_subplot(projection='3d'); ax.set_facecolor(BG)
for w,(x,y,z) in P3.items(): ax.scatter(x,y,z,s=220,color=GOLD if z>5 else BLUE); ax.text(x+0.3,y+0.3,z+0.4,w,fontsize=17,color=FG)
ax.set_xlabel('gender',labelpad=12); ax.set_ylabel('age',labelpad=12); ax.set_zlabel('royalty',labelpad=12)
for a in (ax.xaxis,ax.yaxis,ax.zaxis): a.set_pane_color((0.1,0.14,0.22,1))
ax.view_init(20,-60); save(fig,O+'wordspace3d.png')
# GloVe
m=KeyedVectors.load('/workspace/llm-course/_src/gensim/glove100.kv')
words=['king','queen','man','woman','prince','princess','boy','girl','uncle','aunt']
X=np.array([m[w] for w in words]); Xc=X-X.mean(0); U,S,Vt=np.linalg.svd(Xc,full_matrices=False); Y=Xc@Vt[:2].T
fig,ax=plt.subplots(figsize=(13,8.5))
for w,(x,y) in zip(words,Y): ax.scatter(x,y,s=200,color=PINK if w in('queen','woman','princess','girl','aunt') else BLUE,zorder=3); ax.text(x+0.08,y+0.08,w,fontsize=19)
for a,b in [('man','woman'),('king','queen'),('boy','girl'),('uncle','aunt'),('prince','princess')]:
    i,j=words.index(a),words.index(b); ax.annotate('',xy=Y[j],xytext=Y[i],arrowprops=dict(arrowstyle='->',color=GOLD,lw=2.5))
ax.grid(color=GRID); ax.set_title('Real GloVe-100 vectors, projected to 2-D (PCA): parallel "gender" arrows'); ax.set_xlabel('PC 1'); ax.set_ylabel('PC 2')
save(fig,O+'glove_pca.png')
# similarity bars
pairs=[('cat','dog'),('king','queen'),('cat','kitten'),('cat','feline'),('cat','car'),('king','banana')]
v=[float(m.similarity(a,b)) for a,b in pairs]; R['sims']={f'{a}/{b}':round(x,3) for (a,b),x in zip(pairs,v)}
fig,ax=plt.subplots(figsize=(14,6)); ax.barh([f'{a} · {b}' for a,b in pairs][::-1],v[::-1],color=[PINK,PINK,BLUE,BLUE,MINT,MINT]); [ax.text(x+0.01,5-i,f'{x:.3f}',va='center',fontsize=18) for i,x in enumerate(v)]
ax.set_xlim(0,1.05); ax.set_xlabel('cosine similarity (GloVe-100, real)'); ax.set_title('Related words point in similar directions'); save(fig,O+'cosine_glove.png')
# cosine geometry
fig,ax=plt.subplots(figsize=(10,8)); 
for vec,c,l in [((4,3),MINT,'a'),((3,4),GOLD,'b (similar)'),((-3,1),PINK,'c (different)')]:
    ax.annotate('',xy=vec,xytext=(0,0),arrowprops=dict(arrowstyle='->',color=c,lw=4)); ax.text(vec[0]*1.05,vec[1]*1.05,l,fontsize=20,color=c)
ax.set_xlim(-4,5); ax.set_ylim(-1,5); ax.set_aspect('equal'); ax.grid(color=GRID)
a,b,c=np.array([4,3]),np.array([3,4]),np.array([-3,1]); cs=lambda x,y: x@y/np.linalg.norm(x)/np.linalg.norm(y)
ax.set_title(f'cos(a,b) = 24/25 = {cs(a,b):.2f}    cos(a,c) = {cs(a,c):.2f}'); save(fig,O+'cosine_geom.png')
# analogy results
an=[('king','man','woman','queen'),('paris','france','italy','rome'),('tokyo','japan','germany','berlin'),('walking','walk','swim','swimming'),('bigger','big','small','smaller'),('brother','man','woman','sister'),('uncle','man','woman','aunt')]
rows=[]
for a,b,c,exp in an:
    r=m.most_similar(positive=[a,c],negative=[b],topn=3); rows.append((f'{a} − {b} + {c}',exp,', '.join(f'{w} ({s:.2f})' for w,s in r),r[0][0]==exp))
R['analogies']=rows
fig,ax=plt.subplots(figsize=(18,6.5)); ax.axis('off')
t=ax.table(cellText=[[a,e,r,'✓' if ok else '✗'] for a,e,r,ok in rows],colLabels=['query','expected','GloVe top-3 (real)','top-1?'],loc='center',cellLoc='left',colWidths=[0.25,0.11,0.52,0.08])
t.auto_set_font_size(False); t.set_fontsize(17); t.scale(1,2.4)
for (i,j),cell in t.get_celld().items():
    cell.set_facecolor('#1d2b42' if i==0 else BOX); cell.set_edgecolor(GRID); cell.get_text().set_color(MINT if i==0 else (PINK if (j==3 and cell.get_text().get_text()=='✗') else FG))
save(fig,O+'analogies.png')
# king-man+woman geometry in PCA of those four
ws=['king','queen','man','woman']; X=np.array([m[w] for w in ws]); res=m['king']-m['man']+m['woman']; Xa=np.vstack([X,res]); mu=Xa.mean(0); U,S,Vt=np.linalg.svd(Xa-mu); Y=(Xa-mu)@Vt[:2].T
fig,ax=plt.subplots(figsize=(12,8))
for w,(x,y) in zip(ws+['king−man+woman'],Y): ax.scatter(x,y,s=260,color=GOLD if '−' in w else MINT if w=='queen' else BLUE,zorder=3,marker='o' if '−' not in w else 'X'); ax.text(x+0.1,y+0.12,w,fontsize=19)
ax.annotate('',xy=Y[3],xytext=Y[2],arrowprops=dict(arrowstyle='->',color=PINK,lw=3)); ax.annotate('',xy=Y[4],xytext=Y[0],arrowprops=dict(arrowstyle='->',color=PINK,lw=3))
R['res_queen_cos']=round(float(res@m['queen']/np.linalg.norm(res)/np.linalg.norm(m['queen'])),3)
ax.grid(color=GRID); ax.set_title(f'king − man + woman lands near queen (cosine {R["res_queen_cos"]})'); save(fig,O+'king_queen.png')
# averaging problem
fig,ax=canvas(16,5.5)
box(ax,0.3,3.2,5,1.5,'"Dog bites man"',fs=24); box(ax,0.3,0.6,5,1.5,'"Man bites dog"',fs=24)
box(ax,7,1.9,3.6,1.5,'average of\nword vectors',ec=GOLD,fs=20); arrow(ax,5.3,3.9,7,2.9); arrow(ax,5.3,1.4,7,2.4)
box(ax,11.8,1.9,4,1.5,'identical vector\n(cosine = 1.000)',ec=PINK,fs=20); arrow(ax,10.6,2.65,11.8,2.65)
s1=(m['dog']+m['bites']+m['man'])/3; s2=(m['man']+m['bites']+m['dog'])/3; R['avg_equal']=bool(np.allclose(s1,s2)); save(fig,O+'averaging.png')
# animals checkpoint
an=['Cat','Lion','Dog','Goldfish','Shark','Hamster','Bear','Horse','Wolf','Rabbit']
A=np.array([[-0.5,0.9,-0.7],[0.8,-1.0,0.9],[0.0,0.9,-0.3],[-0.9,0.8,-1.0],[0.7,-1.0,0.9],[-0.9,0.9,-0.9],[0.9,-0.9,0.8],[0.7,0.7,-0.2],[0.3,-0.8,0.6],[-0.7,0.7,-0.9]])
C=(A/np.linalg.norm(A,axis=1,keepdims=True)); S=C@C.T
fig,ax=plt.subplots(figsize=(12,10)); im=ax.imshow(S,cmap='magma',vmin=-1,vmax=1); ax.set_xticks(range(10)); ax.set_yticks(range(10)); ax.set_xticklabels(an,rotation=45,fontsize=16); ax.set_yticklabels(an,fontsize=16)
for i in range(10):
    for j in range(10): ax.text(j,i,f'{S[i,j]:.2f}',ha='center',va='center',fontsize=12,color='black' if S[i,j]>0.3 else 'white')
ax.set_title('Checkpoint table (size, domestic, dangerous): cosine similarity'); save(fig,O+'animals.png')
R['cat_lion']=round(float(S[0,1]),3); R['cat_hamster']=round(float(S[0,5]),3); R['cat_rabbit']=round(float(S[0,9]),3); R['lion_shark']=round(float(S[1,4]),3)
# learning from context: sliding window
fig,ax=canvas(17,5)
toks=['the','cat','sat','on','the','mat']
for i,t in enumerate(toks): box(ax,0.5+i*2.7,2.6,2.3,1.3,t,ec=GOLD if i==2 else (MINT if i in(0,1,3,4) else GRID),fs=24)
ax.text(8.5,1.4,'window ±2 around "sat": predict the context words (skip-gram) or predict "sat" from them (CBOW)',ha='center',fontsize=19,color=FG)
ax.text(8.5,0.5,'repeat over billions of windows → words in similar contexts get similar vectors',ha='center',fontsize=19,color=MINT); save(fig,O+'window.png')
json.dump(R,open(O+'../_numbers.json','w'),indent=1,default=str); print(json.dumps(R,default=str)[:2500])
