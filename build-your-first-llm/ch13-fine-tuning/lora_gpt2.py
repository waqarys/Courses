# My ch13 experiment: LoRA (rank 8, alpha 16) on a *pretrained* GPT-2 small's c_attn, with loss masking,
# a held-out split, and EOS-terminated responses. Book's FAQ data (FirstLLM/code, MIT License).
import torch, math, random, json, time, torch.nn as nn, torch.nn.functional as F
from transformers import GPT2LMHeadModel, AutoTokenizer
torch.set_num_threads(4); torch.manual_seed(0); random.seed(0)
exec(open('faq.py').read())
data=FAQ_DATA[:]; random.shuffle(data); test=data[:14]; train=data[14:]
tok=AutoTokenizer.from_pretrained('gpt2'); m=GPT2LMHeadModel.from_pretrained('gpt2')
class LoRAConv1D(nn.Module):  # HF Conv1D: y = x @ W + b, W is (in, out)
    def __init__(s, base, r=8, alpha=16):
        super().__init__(); s.base=base; i,o=base.weight.shape
        s.A=nn.Parameter(torch.empty(i,r)); nn.init.kaiming_uniform_(s.A,a=math.sqrt(5)); s.B=nn.Parameter(torch.zeros(r,o)); s.scale=alpha/r
    def forward(s,x): return s.base(x)+(x@s.A@s.B)*s.scale
for p in m.parameters(): p.requires_grad=False
for blk in m.transformer.h: blk.attn.c_attn=LoRAConv1D(blk.attn.c_attn)
tr=sum(p.numel() for p in m.parameters() if p.requires_grad); tot=sum(p.numel() for p in m.parameters()); print('trainable',tr,'total',tot)
def enc(ex):
    p=f"[INST] {ex['instruction']} [/INST] "; ids=tok.encode(p+ex['response'])+[tok.eos_token_id]; n=len(tok.encode(p))
    lab=[-100]*n+ids[n:]; return ids,lab
@torch.no_grad()
def answer(q,n=40):
    m.eval(); x=torch.tensor([tok.encode(f"[INST] {q} [/INST]")]); L=x.shape[1]
    for _ in range(n):
        nt=m(x).logits[0,-1].argmax().item()
        if nt==tok.eos_token_id: break
        x=torch.cat([x,torch.tensor([[nt]])],1)
    return tok.decode(x[0,L:]).strip()
def score(ds):
    em=ov=0; out=[]
    for ex in ds:
        g=answer(ex['instruction']); e=ex['response']; em+=g.lower()==e.lower()
        gw,ew=set(g.lower().split()),set(e.lower().split()); ov+=len(gw&ew)/max(len(ew),1); out.append((ex['instruction'],e,g))
    return em/len(ds), ov/len(ds), out
res={'before':score(test)[:2]}; print('before',res['before'])
opt=torch.optim.AdamW([p for p in m.parameters() if p.requires_grad],lr=1e-3)
E=int(__import__('os').environ.get('EPOCHS','12')); hist=[]; t0=time.time()
for ep in range(E):
    m.train(); random.shuffle(train); L=[]
    for b in range(0,len(train),8):
        bt=[enc(x) for x in train[b:b+8]]; T=max(len(i) for i,_ in bt)
        ids=torch.tensor([i+[tok.eos_token_id]*(T-len(i)) for i,_ in bt]); lab=torch.tensor([l+[-100]*(T-len(l)) for _,l in bt])
        lg=m(ids).logits; loss=F.cross_entropy(lg[:,:-1].reshape(-1,lg.size(-1)),lab[:,1:].reshape(-1),ignore_index=-100)
        opt.zero_grad(); loss.backward(); opt.step(); L.append(loss.item())
    hist.append(sum(L)/len(L)); print(ep+1,round(hist[-1],4),round(time.time()-t0),flush=True)
res['hist']=hist; a=score(test); b=score(train[:14])
res.update(test_em=a[0],test_overlap=a[1],train_em=b[0],train_overlap=b[1],test_samples=a[2][:6],train_samples=b[2][:4],trainable=tr,total=tot)
lora={k:v for k,v in m.state_dict().items() if k.endswith('.A') or k.endswith('.B')}; torch.save(lora,'lora.pt')
res['lora_kb']=__import__('os').path.getsize('lora.pt')/1024
json.dump(res,open('lora_gpt2.json','w'),indent=1); print(json.dumps({k:v for k,v in res.items() if 'samples' not in k},indent=1)); print(json.dumps(a[2][:6],indent=1))
