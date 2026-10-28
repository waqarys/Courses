#!/bin/bash
# runnb.sh chNN  -> executes notebook (pip cells neutralized) and prints outputs/errors
. /workspace/venv/bin/activate; mkdir -p /workspace/llm-course/_src/run; cd /workspace/llm-course/_src/run
python - $1 <<'PY'
import json,sys
nb=json.load(open(f'/workspace/llm-course/_src/firstllm-code/notebooks/{sys.argv[1]}.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        s=''.join(c['source'])
        c['source']=[l if not l.lstrip().startswith(('!','%pip')) else '# '+l for l in s.splitlines(True)]
        c['source']=[l.replace('plt.show()',f'plt.savefig("/workspace/llm-course/_src/run/{sys.argv[1]}_fig.png",dpi=100,bbox_inches="tight")') for l in c['source']]
json.dump(nb,open(f'{sys.argv[1]}.ipynb','w'))
PY
MPLBACKEND=Agg timeout ${T:-1500} jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=${CT:-900} $1.ipynb --output $1.out.ipynb >/dev/null 2>&1
python - $1 <<'PY'
import json,sys
nb=json.load(open(f'{sys.argv[1]}.out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        if o['output_type']=='error': print(f'### ERR cell {i}:',o['ename'],o['evalue'][:300])
        t=''.join(o.get('text','')) or ''.join(o.get('data',{}).get('text/plain',''))
        if t: print(f'--- cell {i}'); print(t[:700])
PY
