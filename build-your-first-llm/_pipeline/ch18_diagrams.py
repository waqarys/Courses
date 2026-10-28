import sys; sys.path.insert(0,'.'); from style import *
O='/workspace/llm-course/ch18-whats-next/img/'
fig,ax=canvas(17,5.2); parts=[('Part I\nUnderstand','ch1–4',BLUE),('Part II\nFoundations','ch5–6',MINT),('Part III\nBuild & train','ch7–12',GOLD),('Part IV\nMake it useful','ch13–15',PINK),('Part V\nShip it','ch16–17',FG)]
for i,(t,s,c) in enumerate(parts):
    box(ax,0.3+i*3.35,2.0,2.9,1.8,t,ec=c,fs=17); ax.text(1.75+i*3.35,1.4,s,ha='center',fontsize=15,color=c)
    if i<4: arrow(ax,3.2+i*3.35,2.9,3.65+i*3.35,2.9)
ax.text(8.5,4.5,'The journey, redrawn',ha='center',fontsize=20); save(fig,O+'journey.png')
fig,ax=canvas(17,6.5); box(ax,6.5,4.6,4,1.2,'You, after ch17',ec=GOLD,fs=18)
for x,t,c in [(0.5,'Path 1 · Research\nevaluation · architectures\ninterpretability',BLUE),(6.0,'Path 2 · Builder\nstructured outputs · retrieval\nUX',MINT),(11.5,'Path 3 · Systems\ncost · observability\nLLMOps',PINK)]:
    box(ax,x,0.8,5,2.4,t,ec=c,fs=16); arrow(ax,8.5,4.55,x+2.5,3.25,c=c)
save(fig,O+'paths.png')
fig,ax=canvas(17,5.5)
for i,(t,w,c) in enumerate([('Capstone 1 · RAG with citations','2–3 weekends · medium',MINT),('Capstone 2 · Fine-tuned domain assistant','3–4 weekends · medium-hard',GOLD),('Capstone 3 · Single-tool agent','2 weekends · medium',PINK)]):
    box(ax,0.5,4.0-i*1.6,10.5,1.2,t,ec=c,fs=18); ax.text(11.4,4.6-i*1.6,w,va='center',fontsize=16,color=c)
save(fig,O+'capstones.png')
