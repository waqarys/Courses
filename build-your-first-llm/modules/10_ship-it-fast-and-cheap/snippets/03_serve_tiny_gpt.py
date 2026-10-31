# M10 · snippet 03 — a stdlib web API around the M07 tiny GPT.
# Run: python serve.py   then:  curl -X POST localhost:8000/generate -d "{\"prompt\": \"Holmes\", \"n\": 120}"
import json, torch
from http.server import BaseHTTPRequestHandler, HTTPServer
from gpt_model import GPT, GPTConfig

ck = torch.load("tiny_gpt.pt")
model = GPT(GPTConfig(**ck["cfg"])); model.load_state_dict(ck["model"]); model.eval()   # load ONCE
stoi = {c: i for i, c in enumerate(ck["chars"])}; itos = dict(enumerate(ck["chars"]))

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        req = json.loads(self.rfile.read(int(self.headers["Content-Length"])) or b"{}")
        ids = [stoi[c] for c in req.get("prompt", "\n") if c in stoi] or [0]
        n = min(int(req.get("n", 100)), 500)                            # cap work per request
        out = model.generate(torch.tensor([ids]), n, float(req.get("temperature", 0.8)))
        body = json.dumps({"text": "".join(itos[i] for i in out[0].tolist())}).encode()
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers()
        self.wfile.write(body)

print("serving on http://localhost:8000/generate")
HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
