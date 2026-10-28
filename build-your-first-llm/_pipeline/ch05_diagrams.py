import sys,json,re,os,tempfile; sys.path.insert(0,'.'); from style import *
O='/workspace/llm-course/ch05-your-first-python-program/img/'; R={}
# tokenizer flow
fig,ax=canvas(17,5)
st=[('"The secret to AI"','raw text',FG),('["the","secret",\n"to","ai"]','lower + split',MINT),('vocab lookup\n{"the":2,…}','dict',GOLD),('[2, 3, 4, 6]','token IDs',PINK)]
for i,(a,b,c) in enumerate(st):
    box(ax,0.3+i*4.25,1.6,3.6,1.9,a,ec=c,fs=18); ax.text(2.1+i*4.25,0.9,b,ha='center',fontsize=17,color=c)
    if i<3: arrow(ax,3.9+i*4.25,2.55,4.55+i*4.25,2.55)
save(fig,O+'tok_flow.png')
# pipeline stages
fig,ax=canvas(17,5.2)
st=['1 Tokenize\ntext → IDs','2 Embed\nIDs → vectors','3 12 Transformer\nlayers','4 Sample\nnext token','5 Decode\nID → text']
for i,s in enumerate(st):
    box(ax,0.2+i*3.4,1.7,2.9,1.9,s,ec=MINT if i==0 else GRID,fs=17)
    if i<4: arrow(ax,3.1+i*3.4,2.65,3.6+i*3.4,2.65)
ax.text(1.65,1.0,'you built this today',ha='center',fontsize=16,color=MINT); ax.annotate('',xy=(1.65,1.6),xytext=(1.65,1.2),arrowprops=dict(arrowstyle='->',color=MINT))
ax.text(8.5,4.4,'loop: append the new token and run again',ha='center',fontsize=17,color=GOLD); save(fig,O+'pipeline.png')
# data structures cheat
fig,ax=canvas(17,6)
items=[('variable','prompt = "Hello"',FG),('string','"Hi there".lower().split()',MINT),('list','ids = [2, 3, 4]  ids[-1] ids[:-1]',GOLD),('dict','vocab = {"the": 2}  vocab.get(w, 1)',PINK),('function','def encode(text): ...',BLUE),('class','class SimpleTokenizer: ...',MINT)]
for i,(a,b,c) in enumerate(items):
    y=5-i*0.95; ax.text(0.5,y,a,fontsize=21,color=c,va='center'); ax.text(3.3,y,b,fontsize=20,family='monospace',va='center')
save(fig,O+'python_cheat.png')
# input/target shift
fig,ax=canvas(17,4.6); ids=[464,3797,3332,319,262,2603]; w=['The',' cat',' sat',' on',' the',' mat']
for i,(t,s) in enumerate(zip(ids,w)):
    box(ax,0.5+i*2.6,2.6,2.2,1.1,f'{s!r}\n{t}',fs=15,ec=GOLD if i<5 else GRID)
    box(ax,0.5+i*2.6,0.4,2.2,1.1,'—' if i==0 else f'{w[i]!r}',fs=15,ec=MINT if i>0 else GRID)
ax.text(16.4,3.15,'tokens[:-1]\n= inputs',fontsize=16,color=GOLD,va='center'); ax.text(16.4,0.95,'tokens[1:]\n= targets',fontsize=16,color=MINT,va='center')
for i in range(5): arrow(ax,1.6+i*2.6,2.6,1.6+(i+1)*2.6,1.5)
save(fig,O+'shift.png')
# exercises solved (my own code) -- executed here
code=r'''
import json, string
class SimpleTokenizer:
    def __init__(self):
        self.word_to_id = {"<PAD>": 0, "<UNK>": 1}; self.id_to_word = {0: "<PAD>", 1: "<UNK>"}
    @staticmethod
    def _clean(text):                      # Exercise 1
        return text.lower().translate(str.maketrans("", "", string.punctuation)).split()
    def fit(self, texts):
        for t in texts:
            for w in self._clean(t):
                if w not in self.word_to_id:
                    i = len(self.word_to_id); self.word_to_id[w] = i; self.id_to_word[i] = w
    def encode(self, text): return [self.word_to_id.get(w, 1) for w in self._clean(text)]
    def decode(self, ids): return " ".join(self.id_to_word.get(i, "<UNK>") for i in ids)
    def count_unknowns(self, sentences):   # Exercise 2
        return sum(self.encode(s).count(1) for s in sentences)
    def save(self, path):                  # Exercise 3
        json.dump(self.word_to_id, open(path, "w"))
    @classmethod
    def load(cls, path):
        t = cls(); t.word_to_id = json.load(open(path))
        t.id_to_word = {i: w for w, i in t.word_to_id.items()}; return t
'''
exec(code); tok=SimpleTokenizer(); tok.fit(["The key to machine learning, is data!","AI systems learn from examples."])
R['ex1']=tok.encode("learning, data!"); R['ex1_dec']=tok.decode(R['ex1'])
R['ex2']=tok.count_unknowns(["AI systems learn quickly","Neural networks learn from data"])
p=tempfile.mktemp(suffix='.json'); tok.save(p); t2=SimpleTokenizer.load(p); R['ex3']=t2.encode("machine learning")==tok.encode("machine learning")
open(O+'../exercises_solution.py','w').write('# My own solutions to Ch 5 exercises (not from the book repo)\n'+code.strip()+'\n')
json.dump(R,open(O+'../_numbers.json','w'),indent=1); print(R)
