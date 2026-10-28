# My experiment: same MiniGPT config as ch12, but (a) contiguous token stream (no padding), (b) no ignore_index=0 bug,
# (c) tied weights+biases fixed model from ch11. Track train/val loss every 50 steps.
import torch, json, math, time, torch.nn.functional as F
torch.set_num_threads(4); torch.manual_seed(42)
exec(open('ch11_lib.py').read().split('print("GPT-2 Small (default):")')[0])
exec(open('ch11_lib.py').read().split('print("MiniGPT class defined!")')[0].split('tiny_config = GPTConfig(embed_dim=64, num_heads=2, num_layers=2, d_ff=256)')[1]) if False else None
src=open('ch11_lib.py').read()
start=src.index('class MiniGPT'); end=src.index('print("MiniGPT class defined!")'); exec(src[start:end])
from transformers import AutoTokenizer
tok=AutoTokenizer.from_pretrained('gpt2'); txt=open('shakespeare.txt').read()
ids=torch.tensor(tok(txt)['input_ids']); n=int(0.9*len(ids)); tr,va=ids[:n],ids[n:]
cfg=GPTConfig(vocab_size=50257,max_seq_len=128,embed_dim=256,num_heads=4,num_layers=4,d_ff=1024,dropout=0.1)
m=MiniGPT(cfg); opt=torch.optim.AdamW(m.parameters(),lr=3e-4,weight_decay=0.01)
B,T=32,128; steps=1200; warm=100
sched=torch.optim.lr_scheduler.LambdaLR(opt,lambda s: min(1,(s+1)/warm)*max(0.0,(steps-s)/(steps)))
def batch(d):
    ix=torch.randint(len(d)-T-1,(B,)); x=torch.stack([d[i:i+T] for i in ix]); y=torch.stack([d[i+1:i+T+1] for i in ix]); return x,y
@torch.no_grad()
def ev():
    m.eval(); L=[]
    g=torch.Generator().manual_seed(0)
    for _ in range(10):
        ix=torch.randint(len(va)-T-1,(B,),generator=g); x=torch.stack([va[i:i+T] for i in ix]); y=torch.stack([va[i+1:i+T+1] for i in ix])
        L.append(F.cross_entropy(m(x).view(-1,50257),y.view(-1)).item())
    m.train(); return sum(L)/len(L)
log=[]; t0=time.time(); run=0
for s in range(steps+1):
    if s%50==0:
        v=ev(); log.append(dict(step=s,train=run,val=v,ppl=math.exp(v),t=round(time.time()-t0))); print(log[-1],flush=True)
        json.dump(log,open('ch12_mine.json','w'))
    if s==steps: break
    x,y=batch(tr); loss=F.cross_entropy(m(x).view(-1,50257),y.view(-1))
    opt.zero_grad(set_to_none=True); loss.backward(); torch.nn.utils.clip_grad_norm_(m.parameters(),1.0); opt.step(); sched.step()
    run=0.9*run+0.1*loss.item() if s else loss.item()
torch.save(m.state_dict(),'ch12_mine.pt')
@torch.no_grad()
def gen(p,n=60,temp=0.8):
    m.eval(); x=torch.tensor([tok.encode(p)])
    for _ in range(n):
        lg=m(x[:,-128:])[:,-1]/temp; x=torch.cat([x,torch.multinomial(F.softmax(lg,-1),1)],1)
    return tok.decode(x[0])
torch.manual_seed(1); out={p:gen(p) for p in ["ROMEO:","The king","To be or not to be","KING HENRY:"]}
json.dump(dict(log=log,gen=out),open('ch12_mine.json','w'),indent=1); print(json.dumps(out,indent=1))
