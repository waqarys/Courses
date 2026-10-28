import sys,glob,numpy as np
from PIL import Image
bad=[]
for f in sorted(glob.glob(sys.argv[1]+'/*.png')):
    a=np.asarray(Image.open(f).convert('RGB')).astype(int)
    band=a[945:1012,60:1780]; bg=a[1075,960]
    if (np.abs(band-bg).sum(-1)>60).sum()>40: bad.append(f.split('.')[-2])
print('OVERFLOW:',bad)
