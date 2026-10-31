# M09 · snippet 02 — retrieval-augmented generation in pure Python, answered by Grok (optional)
# Set XAI_API_KEY in your environment to call Grok; otherwise the prompt is printed to paste into Grok chat.
import json, math, os, re, urllib.request
from collections import Counter

docs = [
    "Module 7 trains a tiny GPT on a public-domain book on a laptop CPU in about ten minutes.",
    "Module 8 uses LoRA so only about a quarter of a percent of GPT-2's weights are trained.",
    "The course videos are recorded in OBS with three scenes: camera, slides and IntelliJ.",
    "Module 5 explains attention as a group chat with queries, keys and values.",
    "Thumbnails use a dark navy background with one neon-cyan keyword and Waqar's face.",
]

STOP = {"the", "a", "an", "of", "in", "on", "to", "is", "does", "how", "with", "and", "so", "only", "about", "what"}

def vec(text):                      # bag-of-words "embedding" (stop-words removed)
    return Counter(w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP)

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in a)
    return dot / (math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values())) or 1)

def retrieve(q, k=2):
    qv = vec(q)
    ranked = sorted(((cosine(qv, vec(d)), d) for d in docs), reverse=True)
    for s, d in ranked:
        print(f"  {s:.2f}  {d[:60]}")
    return [d for _, d in ranked[:k]]

question = "How long does the training run in module 7 take?"
context = "\n".join(f"- {c}" for c in retrieve(question))
prompt = f"""Answer using ONLY the context between <context> tags. If it is not there, say "I don't know".
<context>
{context}
</context>
Question: {question}
Answer in one sentence."""

key = os.environ.get("XAI_API_KEY")
if not key:
    print("\n(no XAI_API_KEY) paste this into Grok:\n\n" + prompt)
else:
    body = {"model": os.environ.get("GROK_MODEL", "grok-4"), "messages": [{"role": "user", "content": prompt}]}
    req = urllib.request.Request("https://api.x.ai/v1/chat/completions", data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        print("\nGrok:", json.load(r)["choices"][0]["message"]["content"])
