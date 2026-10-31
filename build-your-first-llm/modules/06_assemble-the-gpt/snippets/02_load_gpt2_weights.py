# M06 · snippet 02 — pour OpenAI's GPT-2 weights into OUR model, verify, generate
# Put this file next to 01_gpt_model.py (rename that to gpt_model.py) — pip install transformers tiktoken
import sys, torch, tiktoken
from transformers import GPT2LMHeadModel
from gpt_model import GPT, GPTConfig

def load(attn_bias=True):
    hf = GPT2LMHeadModel.from_pretrained("gpt2").eval()
    sd_hf = hf.state_dict()
    ours = GPT(GPTConfig(attn_bias=attn_bias)).eval()
    sd = ours.state_dict()
    transposed = ("attn.c_attn.weight", "attn.c_proj.weight", "mlp.c_fc.weight", "mlp.c_proj.weight")
    for k in sd:
        src = sd_hf["transformer." + k] if "transformer." + k in sd_hf else sd_hf.get(k)
        if src is None:
            continue                                     # silently skipped -> the classic bug
        with torch.no_grad():
            sd[k].copy_(src.t() if k.endswith(transposed) else src)
    return ours, hf

enc = tiktoken.get_encoding("gpt2")
x = torch.tensor([enc.encode("The quick brown fox")])
bias = "--no-bias" not in sys.argv
ours, hf = load(attn_bias=bias)
with torch.no_grad():
    diff = (ours(x)[0] - hf(x).logits).abs().max().item()
print(f"attn_bias={bias}  max logit diff vs HF: {diff:.2e}")
torch.manual_seed(0)
out = ours.generate(x, 20, temperature=0.8, top_k=40)
print(enc.decode(out[0].tolist()))
