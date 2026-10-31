# Book's complete app.py (Ch 16.7), transcribed. Code: FirstLLM/code (MIT License)
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, field_validator
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
import json, time, re
from llm_helper import chat
MAX_PROMPT_LENGTH = 4000; RATE_LIMIT = 20; RATE_WINDOW = timedelta(minutes=1)
LOG_FILE = Path("logs/requests.jsonl"); LOG_FILE.parent.mkdir(exist_ok=True)
def log_request(prompt_length, response_length, latency_ms, success, error=None):
    entry = {"timestamp": datetime.now().isoformat(),"prompt_length": prompt_length,"response_length": response_length,"latency_ms": round(latency_ms, 2),"success": success}
    if error: entry["error"] = error
    with open(LOG_FILE, "a") as f: f.write(json.dumps(entry) + "\n")
request_counts = defaultdict(list)
def check_rate_limit(request: Request):
    ip = request.client.host; now = datetime.now()
    request_counts[ip] = [t for t in request_counts[ip] if now - t < RATE_WINDOW]
    if len(request_counts[ip]) >= RATE_LIMIT: raise HTTPException(429, "Too many requests. Please wait.")
    request_counts[ip].append(now)
SUSPICIOUS_PATTERNS = [r"ignore (?:all )?(?:previous )?instructions", r"you are now", r"act as"]
def validate_input(text):
    if len(text) > MAX_PROMPT_LENGTH: return False, f"Message too long (max {MAX_PROMPT_LENGTH} chars)"
    for p in SUSPICIOUS_PATTERNS:
        if re.search(p, text.lower()): return False, "Invalid input"
    return True, ""
app = FastAPI(title="My LLM API", version="1.0.0")
class ChatRequest(BaseModel):
    message: str
    @field_validator('message')
    @classmethod
    def not_empty(cls, v):
        if not v.strip(): raise ValueError('Message cannot be empty')
        return v
class ChatResponse(BaseModel):
    response: str; latency_ms: float
metrics = {"requests": 0, "errors": 0, "latency_sum": 0}
@app.get("/health")
def health(): return {"status": "healthy", "version": "1.0.0"}
@app.get("/metrics")
def get_metrics():
    avg = metrics["latency_sum"] / max(metrics["requests"], 1)
    return {"requests": metrics["requests"], "errors": metrics["errors"], "avg_latency_ms": round(avg, 2)}
@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest, http_request: Request):
    check_rate_limit(http_request)
    ok, err = validate_input(request.message)
    if not ok: log_request(len(request.message), 0, 0, False, err); raise HTTPException(400, err)
    start = time.time()
    try:
        r = chat(request.message); ms = (time.time()-start)*1000
        log_request(len(request.message), len(r), ms, True); metrics["requests"] += 1; metrics["latency_sum"] += ms
        return ChatResponse(response=r, latency_ms=round(ms, 2))
    except Exception as e:
        ms=(time.time()-start)*1000; log_request(len(request.message),0,ms,False,str(e)); metrics["requests"]+=1; metrics["errors"]+=1
        raise HTTPException(500, "Generation failed. Please try again.")
