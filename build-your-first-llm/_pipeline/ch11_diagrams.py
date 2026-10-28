import sys; sys.path.insert(0,'.'); from style import *
O='/workspace/llm-course/ch11-building-the-transformer/img/'
# stack
fig,ax=canvas(16,9)
items=[('token IDs (B, T)',FG),('token_embed + pos_embed → (B, T, 768)',MINT),('Block 1: LN → attn → +  ·  LN → FFN → +',BLUE),('Block 2',BLUE),('⋮  (blocks 3–11)',FG),('Block 12',BLUE),('ln_f (final LayerNorm)',GOLD),('lm_head → logits (B, T, 50257)',PINK)]
for i,(t,c) in enumerate(items):
    y=8.0-i*1.02; box(ax,2.5,y,9,0.75,t,ec=c,fs=17)
    if i<7: arrow(ax,7,y,7,y-0.25)
ax.add_patch(FancyArrowPatch((11.6,7.0),(11.6,0.9),connectionstyle='arc3,rad=-0.35',arrowstyle='<|-|>',mutation_scale=22,color=GOLD,lw=2.5,ls='--'))
ax.text(14.6,4.0,'weight tying:\nsame 50,257×768\nmatrix',ha='center',fontsize=16,color=GOLD)
ax.text(0.2,4.6,'shape stays\n(B, T, 768)',fontsize=15,color=MINT); save(fig,O+'stack.png')
# param breakdown
labels=['token embed (tied)','position embed','attention ×12','FFN ×12','LayerNorms']
vals=[38597376,786432,12*(768*2304+2304+768*768+768),12*(768*3072+3072+3072*768+768),12*4*768+2*768]
fig,ax=plt.subplots(figsize=(13,6)); cols=[MINT,BLUE,PINK,GOLD,FG]
ax.barh(labels[::-1],[v/1e6 for v in vals[::-1]],color=cols[::-1])
for i,v in enumerate(vals[::-1]): ax.text(v/1e6+0.5,i,f'{v:,} ({100*v/sum(vals):.1f}%)',va='center',fontsize=15)
ax.set_xlim(0,75); ax.set_xlabel('millions of parameters'); ax.set_title(f'GPT-2 small: {sum(vals):,} parameters (my count = HF)'); ax.grid(axis='x',color=GRID); save(fig,O+'params.png'); print(sum(vals))
# bug vs fix
fig,ax=plt.subplots(figsize=(13,5.5)); L=['notebook\n(no attn biases)','+ attention\nbiases','+ tanh GELU']; V=[58.15,0.0749,0.000061]
ax.bar(L,V,color=[PINK,GOLD,MINT]); ax.set_yscale('log'); ax.set_ylabel('max |logit − HF GPT-2|')
for i,v in enumerate(V): ax.text(i,v*1.4,f'{v:g}',ha='center',fontsize=17)
ax.set_title('Loading GPT-2 into MiniGPT: how far from the real model? (my run)'); ax.grid(axis='y',color=GRID); ax.set_ylim(1e-5,500); save(fig,O+'bugfix.png')
