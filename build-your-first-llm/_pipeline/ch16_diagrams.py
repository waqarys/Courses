import sys; sys.path.insert(0,'.'); from style import *
O='/workspace/llm-course/ch16-preparing-for-production/img/'
fig,ax=canvas(17,5.6)
st=[('request',FG),('rate limit\n429',PINK),('Pydantic\n422',GOLD),('validate_input\n400',GOLD),('chat()\n500 on error',MINT),('log JSONL\n+ metrics',BLUE)]
for i,(t,c) in enumerate(st):
    box(ax,0.2+i*2.85,2.0,2.4,1.6,t,ec=c,fs=15)
    if i<5: arrow(ax,2.6+i*2.85,2.8,3.05+i*2.85,2.8)
ax.text(8.5,4.5,'One /chat request, and where it can be stopped',ha='center',fontsize=19); save(fig,O+'flow.png')
fig,ax=canvas(16,6.5)
for i,(t,c) in enumerate([('detect\n(logs, metrics, users)',PINK),('diagnose\n(replay the input)',GOLD),('fix + test\n(regression test)',MINT),('monitor\n(did it work?)',BLUE)]):
    import math; a=math.pi/2-i*math.pi/2; x=8+4.6*math.cos(a)-1.6; y=3.2+2.3*math.sin(a)-0.6
    box(ax,x,y,3.2,1.2,t,ec=c,fs=15)
ax.text(8,3.2,'the production\nloop',ha='center',va='center',fontsize=18); save(fig,O+'loop.png')
fig,ax=canvas(17,5.5)
box(ax,0.4,0.6,7.8,4.2,'',ec=MINT); ax.text(4.3,4.3,'Development',ha='center',fontsize=20,color=MINT)
ax.text(0.8,2.4,'• one user: you\n• errors = lessons\n• print() debugging\n• re-run the cell',fontsize=17,va='center')
box(ax,8.8,0.6,7.8,4.2,'',ec=PINK); ax.text(12.7,4.3,'Production',ha='center',fontsize=20,color=PINK)
ax.text(9.2,2.4,'• many users at once\n• errors = angry users\n• read last night\'s logs\n• must recover by itself',fontsize=17,va='center'); save(fig,O+'devprod.png')
