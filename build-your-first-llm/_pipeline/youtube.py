import json,sys,os
ch,num,title,blurb,nb=sys.argv[1:6]
T=json.load(open(f'{ch}/timings.json'))
import re
_sl=open(f'{ch}/slides.md').read().split('\n---\n')[1:]
for t in T:
    if t['divider'] and t['slide']-1 < len(_sl):
        m=re.search(r'^##\s+(.+)$',_sl[t['slide']-1],re.M)
        if m and t['title'].startswith('Part'): t['title']=t['title']+' — '+m.group(1).strip()
def f(s): s=int(s); return f'{s//3600}:{s%3600//60:02d}:{s%60:02d}' if s>=3600 else f'{s//60}:{s%60:02d}'
stamps=[('0:00','Intro & roadmap')]
for t in T[1:]:
    if t['divider']: stamps.append((f(t['start']),t['title']))
    elif t['title'].startswith(('Review questions 1','Review questions (1','Practice this','Credits')): stamps.append((f(t['start']),t['title']))
tot=T[-1]['start']+T[-1]['dur']
code=(f"- Notebook: https://github.com/FirstLLM/code/blob/main/notebooks/{nb}.ipynb\n- Run in Colab: https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/{nb}.ipynb\n" if nb!='-' else "- This chapter has no notebook (notebooks start at Ch 5). Repo: https://github.com/FirstLLM/code\n")
yt=f"""# YouTube upload — Chapter {int(num)}

**Title:** Build Your First LLM — Ch {int(num)}: {title} (Full Walkthrough)

**Duration:** {f(tot)} · **Slides:** {len(T)} · **Thumbnail:** thumbnail.png · **Captions:** captions.srt (English)

**Playlist:** Build Your First LLM (study series) · **Visibility:** set by Waqar at upload

## Description

{blurb}

This is part of my study series on the book "Build Your First LLM: A Hands-On Guide to Language Models" by Hasan Degismez. All slides, narration and diagrams are my own teaching adaptation. Please support the author and buy the book: https://leanpub.com/FirstLLM/

📌 Chapters
""" + "\n".join(f"{a} {b}" for a,b in stamps) + f"""

💻 Code (FirstLLM/code, MIT License)
{code}- Slides + study notes: https://github.com/waqarys/Courses/tree/build-your-first-llm/build-your-first-llm

📚 Credit
Based on "Build Your First LLM" by Hasan Degismez — https://leanpub.com/FirstLLM/
Code: https://github.com/FirstLLM/code (MIT License)
Narration voice: synthetic (Kokoro TTS).

#LLM #Transformers #MachineLearning

## Tags
build your first llm, llm from scratch, transformers, attention mechanism, gpt-2, pytorch, deep learning, machine learning, large language models, hasan degismez, waqar shaikh builds, ai tutorial, {title.lower()}
"""
open(f'{ch}/youtube.md','w').write(yt); print(yt[:1500])
