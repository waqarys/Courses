#!/bin/bash
# usage: finish.sh NN  (chapter dir auto-detected)
set -e
N=$1; cd /workspace/llm-course; D=$(ls -d ch${N}-*/ | head -1); D=${D%/}
U=/workspace/upload; mkdir -p $U
cp $D/video.mp4 $U/ch$N.mp4; cp $D/thumbnail.png $U/ch$N-thumb.png; cp $D/captions.srt $U/ch$N.srt
python3 - "$D" "$U/ch$N-description.txt" <<'PY'
import sys,re
t=open(sys.argv[1]+'/youtube.md').read()
d=t.split('## Description\n',1)[1].split('\n## Tags',1)[0].strip()+'\n'
open(sys.argv[2],'w').write(d)
PY
TITLE=$(sed -n 's/^\*\*Title:\*\* //p' $D/youtube.md); DUR=$(sed -n 's/^\*\*Duration:\*\* \([0-9:]*\).*/\1/p' $D/youtube.md)
grep -q "^ch$N |" $U/READY.txt 2>/dev/null || echo "ch$N | $TITLE | $DUR" >> $U/READY.txt
R=_src/courses-repo; B=$R/build-your-first-llm/$D; mkdir -p $B/img
cp $D/{slides.md,notes.md,script.md,youtube.md,captions.srt,timings.json,thumbnail.png} $B/; cp $D/img/*.png $B/img/ 2>/dev/null || true; cp $D/*.py $B/ 2>/dev/null || true
cp _pipeline/*.py _pipeline/*.css _pipeline/*.sh $R/build-your-first-llm/_pipeline/ 2>/dev/null || true
[ -f ERRATA.md ] && cp ERRATA.md $R/build-your-first-llm/ERRATA.md
python3 - "$R/build-your-first-llm/README.md" "$D" "$((10#$N))" <<'PY'
import sys,re
p,d,n=sys.argv[1],sys.argv[2],int(sys.argv[3]); t=open(p).read().split('\n')
for i,l in enumerate(t):
    if l.startswith(f'| {n} |') and 'planned' in l:
        c=[x.strip() for x in l.strip('|').split('|')]
        c[2]=f'[slides]({d}/slides.md)'; c[3]=f'[notes]({d}/notes.md)'
        if c[4].startswith('[ch'): nb=f'ch{n:02d}'; c[4]+=f' · [Colab](https://colab.research.google.com/github/FirstLLM/code/blob/main/notebooks/{nb}.ipynb)'
        c[5]='✅'; t[i]='| '+' | '.join(c)+' |'
s='\n'.join(t)
if 'ERRATA.md' not in s: s=s.replace('## Rebuilding a video','## Errata\nBook mistakes found while verifying the code: [ERRATA.md](ERRATA.md)\n\n## Rebuilding a video')
open(p,'w').write(s)
PY
cd $R && git add -A build-your-first-llm && git -c user.name="Waqar Shaikh" -c user.email=waqaryshaikh@gmail.com commit -q -m "Build Your First LLM: add Ch $((10#$N)) ($D)" && git push -q origin build-your-first-llm && git log -1 --format=%H
