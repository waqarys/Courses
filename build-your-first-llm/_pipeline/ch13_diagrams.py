import sys,glob; sys.path.insert(0,'.'); from style import *
O=glob.glob('/workspace/llm-course/ch13-*/')[0]+'img/'
fig,ax=canvas(17,6.5)
box(ax,0.5,1.0,4.5,4.5,'W\n(frozen)\n256 × 256\n65,536',ec=BLUE,fs=17)
ax.text(5.6,3.2,'+',fontsize=40,ha='center',va='center')
box(ax,6.4,1.0,1.2,4.5,'B\n256×8',ec=MINT,fs=13); ax.text(8.0,3.2,'×',fontsize=30,ha='center',va='center')
box(ax,8.5,2.6,4.5,1.2,'A   8 × 256',ec=MINT,fs=15)
ax.text(14.9,3.2,'trainable:\n2 × 256 × 8\n= 4,096\n(16× fewer)',fontsize=17,ha='center',va='center',color=MINT)
ax.text(8.5,6.0,'LoRA: keep W, learn a small low-rank change  ΔW = B·A · (α/r)',ha='center',fontsize=18); save(fig,O+'lora.png')
fig,ax=canvas(17,4.5)
toks=['[INST]','What','are','your','hours','?','[/INST]','We','open','9','to','5','<eos>']
for i,t in enumerate(toks):
    c=FG if i<7 else MINT; box(ax,0.2+i*1.3,1.4,1.2,1.0,t,ec=c,fs=12)
    ax.text(0.8+i*1.3,0.8,'-100' if i<7 else 'learn',ha='center',fontsize=12,color=c)
ax.text(8.5,3.4,'Loss masking: only the answer tokens are trained',ha='center',fontsize=19); save(fig,O+'mask.png')
fig,ax=canvas(16,5.5)
for i,(t,v,c) in enumerate([('full model file',61.4,PINK),('LoRA file',0.13,MINT)]):
    ax.add_patch(__import__('matplotlib').patches.Rectangle((3.5,3.2-i*1.8),v/61.4*11,1.0,color=c))
    ax.text(3.3,3.7-i*1.8,t,ha='right',va='center',fontsize=17); ax.text(3.7+max(v/61.4*11,0.1),3.7-i*1.8,f'{v} MB' if v>1 else '131.6 KB',va='center',fontsize=16)
ax.text(8,5.0,'What you ship per task (notebook run, 16M-param model)',ha='center',fontsize=18); save(fig,O+'size.png')
fig,ax=canvas(17,5.2)
st=[('base model\n(pretrained!)',BLUE),('freeze\nall weights',FG),('add LoRA\nto attention',MINT),('train on\ninstruction pairs',GOLD),('test on\nheld-out pairs',PINK)]
for i,(t,c) in enumerate(st):
    box(ax,0.3+i*3.4,1.8,2.9,1.6,t,ec=c,fs=15)
    if i<4: arrow(ax,3.2+i*3.4,2.6,3.7+i*3.4,2.6)
ax.text(8.5,4.3,'The fine-tuning recipe',ha='center',fontsize=19); save(fig,O+'recipe.png')
