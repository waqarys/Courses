import sys; sys.path.insert(0,'.'); from style import *; import numpy as np
O='/workspace/llm-course/ch17-deployment-options/img/'
# cost: always-on vs per-second
fig,ax=plt.subplots(figsize=(13,5.8)); h=np.arange(0,301)
ax.plot(h,np.full_like(h,0.59*24*30,dtype=float),color=PINK,lw=3,label='T4 VM rented 24/7 (~$425/mo at $0.59/h)')
ax.plot(h,0.59*h,color=MINT,lw=3,label='serverless T4: pay per busy hour')
ax.axhline(30,color=GOLD,ls='--'); ax.text(5,40,'$30/mo included (Starter)',color=GOLD,fontsize=15)
ax.set_xlabel('GPU hours actually used per month'); ax.set_ylabel('$ per month'); ax.legend(facecolor=BG,labelcolor=FG,fontsize=14); ax.grid(color=GRID)
ax.set_title('Why serverless suits hobby LLM apps (GPU cost only, list prices)'); save(fig,O+'cost.png')
# deploy flow
fig,ax=canvas(17,4.5)
for x,t,c in [(0.3,'llm_service.py\n(your laptop)',FG),(4.6,'modal deploy',GOLD),(8.9,'image build +\ncontainer on T4',BLUE),(13.2,'https://…modal.run\n/health /chat /docs',MINT)]:
    box(ax,x,1.5,3.6,1.5,t,ec=c,fs=16)
for x in [3.9,8.2,12.5]: arrow(ax,x,2.25,x+0.7,2.25)
ax.text(8.5,3.8,'From Python file to public HTTPS URL',ha='center',fontsize=19); save(fig,O+'flow.png')
# cold start timeline
fig,ax=plt.subplots(figsize=(14,4.6))
segs=[('container start',0,3,BLUE),('pip image (cached)',3,1,GRID),('download weights\n(no volume)',4,20,PINK),('load to GPU',24,8,GOLD),('generate',32,3,MINT)]
for n,s,d,c in segs: ax.barh(1,d,left=s,color=c); ax.text(s+d/2,1.45,n,ha='center',fontsize=12)
segs2=[('start',0,3,BLUE),('weights from volume',3,4,BLUE),('load',7,8,GOLD),('gen',15,3,MINT)]
for n,s,d,c in segs2: ax.barh(0,d,left=s,color=c); ax.text(s+d/2,-0.5,n,ha='center',fontsize=12)
ax.barh(-1,3,color=MINT); ax.text(4,-1,'warm container: generate only',va='center',fontsize=13)
ax.set_yticks([1,0,-1]); ax.set_yticklabels(['cold, no cache','cold + volume','warm']); ax.set_xlabel('seconds (illustrative, my sketch, not measured)'); ax.set_ylim(-1.6,2); ax.grid(axis='x',color=GRID); save(fig,O+'cold.png')
# request path
fig,ax=canvas(17,5)
for x,t,c in [(0.3,'client\n(curl / phone)',FG),(3.8,'HTTPS edge',BLUE),(7.3,'FastAPI app\nPydantic + API key',GOLD),(10.8,'get_model()\nloaded once',PINK),(14.0,'vLLM\ngenerate',MINT)]:
    box(ax,x,1.8,2.9,1.5,t,ec=c,fs=15)
for x in [3.2,6.7,10.2,13.7]: arrow(ax,x,2.55,x+0.6,2.55)
ax.text(8.5,4.2,'One request through the deployed service',ha='center',fontsize=19); ax.text(12.3,0.9,'@modal.concurrent(max_inputs=10)\nshares one model per container',ha='center',fontsize=14,color=PINK); save(fig,O+'request.png')
