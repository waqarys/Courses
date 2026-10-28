import torch, json, time
exec(open('ch11_lib.py').read())
from transformers import GPT2LMHeadModel, AutoTokenizer
tok=AutoTokenizer.from_pretrained('gpt2'); hf=GPT2LMHeadModel.from_pretrained('gpt2').eval()
R={}
m=load_gpt2_weights(MiniGPT(GPTConfig(dropout=0.0)),'gpt2').eval()
ids=tok.encode("The quick brown fox jumps over the lazy",return_tensors='pt')
with torch.no_grad(): a=m(ids); b=hf(ids).logits
R['book_maxdiff']=float((a-b).abs().max()); R['book_next']=tok.decode(a[0,-1].argmax()); R['hf_next']=tok.decode(b[0,-1].argmax())
# fix: biases
import torch.nn as nn
for blk in m.blocks:
    blk.attn.qkv_proj.bias=nn.Parameter(torch.zeros(2304)); blk.attn.out_proj.bias=nn.Parameter(torch.zeros(768))
hs=hf.state_dict()
with torch.no_grad():
    for i,blk in enumerate(m.blocks):
        blk.attn.qkv_proj.bias.copy_(hs[f'transformer.h.{i}.attn.c_attn.bias']); blk.attn.out_proj.bias.copy_(hs[f'transformer.h.{i}.attn.c_proj.bias'])
    a2=m(ids)
R['bias_fix_maxdiff']=float((a2-b).abs().max())
# gelu tanh
import torch.nn.functional as F
_g=F.gelu
def ff(self,x): return self.fc2(self.dropout(_g(self.fc1(x),approximate='tanh')))
FeedForward.forward=ff
with torch.no_grad(): a3=m(ids)
R['bias+tanh_maxdiff']=float((a3-b).abs().max())
gen={}
for p in ["The quick brown fox","Artificial intelligence will","Once upon a time","The capital of France is","def fibonacci(n):"]:
    gen[p]=generate_simple(m,tok,p,max_new_tokens=20)
R['gen_fixed']=gen
R['params_fixed']=sum(p.numel() for p in m.parameters())
c=GPTConfig(vocab_size=500,max_seq_len=16,embed_dim=64,num_heads=2,num_layers=2,d_ff=256); R['tiny_checkpoint_params']=sum(p.numel() for p in MiniGPT(c).parameters())
R['state_keys_has_lm_head']='lm_head.weight' in m.state_dict()
# timing
t=time.time(); generate_simple(m,tok,"Hello",max_new_tokens=30); R['cpu_30tok_s']=round(time.time()-t,2)
json.dump(R,open('ch11_res.json','w'),indent=1); print(json.dumps(R,indent=1))
