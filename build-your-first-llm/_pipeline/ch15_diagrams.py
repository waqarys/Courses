import sys; sys.path.insert(0,'.'); from style import *
O='/workspace/llm-course/ch15-building-applications/img/'
fig,ax=canvas(17,6.4)
ax.text(0.3,5.8,'offline (once)',color=GOLD,fontsize=17)
for x,t in [(0.3,'documents'),(3.6,'chunk 200 words\noverlap 50'),(6.9,'MiniLM encoder\n→ 384-d, normalised'),(10.2,'vectors +\nsource metadata')]:
    box(ax,x,4.1,2.9,1.3,t,ec=GOLD,fs=15)
for x in [3.2,6.5,9.8]: arrow(ax,x,4.75,x+0.4,4.75)
ax.text(0.3,3.1,'per question',color=MINT,fontsize=17)
for x,t in [(0.3,'question'),(3.6,'embed query'),(6.9,'dot product →\ntop-k ≥ min_score'),(10.2,'prompt with\n[1] [2] sources'),(13.5,'LLM answer\nwith citations')]:
    box(ax,x,1.4,2.9,1.3,t,ec=MINT,fs=15)
for x in [3.2,6.5,9.8,13.1]: arrow(ax,x,2.05,x+0.4,2.05)
arrow(ax,11.6,4.05,8.4,2.75,c=GOLD,ls='--'); save(fig,O+'rag.png')
fig,ax=canvas(17,5)
for x,t,c in [(0.3,'user question',FG),(3.7,'LLM turn 1\n(temp 0)',MINT),(7.1,'<tool>calculate(847*0.15)</tool>',GOLD),(11.0,'whitelisted\nexecute → "127.05"',PINK),(14.2,'LLM turn 2\nfinal answer',MINT)]:
    box(ax,x,1.8,3.0 if x!=7.1 else 3.5,1.5,t,ec=c,fs=14)
for x1,x2 in [(3.3,3.7),(6.7,7.1),(10.6,11.0),(14.0,14.2)]: arrow(ax,x1,2.55,x2,2.55)
ax.text(8.5,4.2,'Two-turn tool calling',ha='center',fontsize=19); save(fig,O+'tools.png')
fig,ax=canvas(17,5.2)
for i,(t,s,c) in enumerate([('1 · Prompting','model already knows',MINT),('2 · RAG','model lacks your data',GOLD),('3 · Tools','model must act / compute',PINK)]):
    box(ax,0.5+i*5.6,1.6,4.8,2.0,t+'\n'+s,ec=c,fs=18)
    if i<2: arrow(ax,5.35+i*5.6,2.6,6.05+i*5.6,2.6)
ax.text(8.5,4.4,'Start simple; add capability only when needed',ha='center',fontsize=19); save(fig,O+'patterns.png')
