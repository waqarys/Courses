import json, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import sys; sys.path.insert(0,'.'); from style import *
d=json.load(open('/workspace/llm-course/_src/exp/ch12_mine.json'))['log']
fig=plt.figure(figsize=(14,6.2),facecolor='#0f1420'); ax=fig.add_subplot(111,facecolor='#0f1420')
ax.plot([x['step'] for x in d],[x['val'] for x in d],'-o',color=MINT,lw=3,ms=4,label='my stream training (val, no padding)')
ax.plot([123,246,369],[6.22,5.66,5.51],'-s',color=PINK,lw=3,ms=9,label='notebook, 3 epochs (val)')
ax.set_xlabel('optimizer steps',color=FG,fontsize=16); ax.set_ylabel('validation loss',color=FG,fontsize=16)
ax.tick_params(colors=FG,labelsize=13); [s.set_color('#556') for s in ax.spines.values()]
ax.set_ylim(4.5,11); ax.legend(fontsize=15,facecolor='#1a2030',labelcolor=FG,edgecolor='#556'); ax.grid(alpha=.15)
ax.annotate('4.87 (ppl 130)',(1200,4.87),xytext=(950,6.3),color=MINT,fontsize=16,arrowprops=dict(color=MINT,arrowstyle='->'))
fig.tight_layout(); fig.savefig('/workspace/llm-course/ch12-training-your-model/img/results.png',dpi=110,facecolor='#0f1420')
