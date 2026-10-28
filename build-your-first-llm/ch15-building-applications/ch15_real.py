# Real llama3.2 3B (Ollama, CPU) run of the ch15 RAG + tools pipeline. Notebook code: FirstLLM/code (MIT).
import json, re, time, requests
from sentence_transformers import SentenceTransformer
import numpy as np
from datetime import datetime
exec(open('nb_defs.py').read())
def chat(prompt, system="You are a helpful assistant.", temperature=0.7):
    r=requests.post('http://localhost:11434/api/chat',json={'model':'llama3.2','stream':False,'options':{'temperature':temperature,'seed':0,'num_predict':200},
        'messages':[{'role':'system','content':system},{'role':'user','content':prompt}]},timeout=1200); return r.json()['message']['content']
rag=SimpleRAG(); rag.add_document(vacation_policy,"vacation_policy.txt"); rag.add_document(expense_policy,"expense_policy.txt"); rag.add_document(remote_work_policy,"remote_work_policy.txt")
def rag_answer(q):
    docs=rag.retrieve(q,top_k=3); p=build_rag_prompt(q,docs)
    return docs, chat(p,system="You are a helpful assistant that answers questions based on provided sources. Always cite your sources.",temperature=0.3)
def evaluate_response(response, t):
    res={}; low=response.lower()
    if "cites_source" in t: res["cites_source"]=(bool(re.search(r'\[\d+\]',response))==t["cites_source"])
    if "contains_keywords" in t: res["contains_keywords"]=all(k.lower() in low for k in t["contains_keywords"])
    if "not_refusal" in t:
        ref=any(p in low for p in ["i don't know","i cannot","not in the sources","no relevant"])
        res["not_refusal"]=(not ref) if t["not_refusal"] else ref
    if "min_words" in t: res["min_words"]=len(response.split())>=t["min_words"]
    return res
ev=[("How many vacation days do employees get?",{"contains_keywords":["15","days"],"cites_source":True,"not_refusal":True}),
    ("What is the expense reimbursement process?",{"contains_keywords":["receipt","submit"],"cites_source":True,"min_words":20}),
    ("What is the meaning of life?",{"not_refusal":False,"cites_source":False})]
R={'chunks':len(rag.documents),'cases':[]}
for q,t in ev:
    t0=time.time(); docs,a=rag_answer(q); r=evaluate_response(a,t)
    R['cases'].append(dict(q=q,scores=[round(d['score'],3) for d in docs],sources=[d['source'] for d in docs],answer=a,res=r,sec=round(time.time()-t0)))
    print(json.dumps(R['cases'][-1]),flush=True)
for q in ["Can I work from home?","How many vacation days can I carry over?"]:
    docs,a=rag_answer(q); R['cases'].append(dict(q=q,scores=[round(d['score'],3) for d in docs],sources=[d['source'] for d in docs],answer=a)); print(json.dumps(R['cases'][-1]),flush=True)
# tools
td="\n".join(f"- {n}: {i['description']}" for n,i in TOOLS.items())
tr=[]
for q in ["What is 15% of 847?","What's today's date?","What is the capital of France?"]:
    p=f"You have access to these tools:\n{td}\n\nTo use a tool, write: <tool>name(argument)</tool>\n\nOnly use a tool if you need it to answer the question.\n\nUser: {q}\nAssistant:"
    first=chat(p,temperature=0); n,a=parse_tool_call(first); res=execute_tool(n,a) if n else None
    final=chat(f"{p}{first}\nTool result: {res}\n\nNow provide your final answer to the user:",temperature=0.3) if n else first
    tr.append(dict(q=q,first=first,tool=n,arg=a,result=res,final=final)); print(json.dumps(tr[-1]),flush=True)
R['tools']=tr; json.dump(R,open('ch15_real.json','w'),indent=1); print('DONE')
