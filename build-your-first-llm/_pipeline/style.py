import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
BG='#0f1724'; FG='#e6edf3'; MINT='#7ee0c3'; GOLD='#ffd479'; BLUE='#9ecbff'; PINK='#ff8fa3'; GRID='#2b3a52'; BOX='#1b2638'
plt.rcParams.update({'figure.facecolor':BG,'axes.facecolor':BG,'savefig.facecolor':BG,'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG,'axes.edgecolor':GRID,'font.size':20,'font.family':'DejaVu Sans','axes.titlesize':24,'axes.titlecolor':MINT})
def canvas(w=16,h=7):
    fig,ax=plt.subplots(figsize=(w,h)); ax.set_xlim(0,w); ax.set_ylim(0,h); ax.axis('off'); return fig,ax
def box(ax,x,y,w,h,text,fc=BOX,ec=MINT,fs=20,tc=FG,bold=False):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.15',fc=fc,ec=ec,lw=2.5))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fs,color=tc,weight='bold' if bold else 'normal',wrap=True)
def arrow(ax,x1,y1,x2,y2,c=FG,lw=2.5,style='-|>',ls='-'):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle=style,mutation_scale=25,color=c,lw=lw,linestyle=ls))
def save(fig,path): fig.savefig(path,dpi=100,bbox_inches='tight',pad_inches=0.2); plt.close(fig)
