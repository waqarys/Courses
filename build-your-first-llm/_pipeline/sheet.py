import sys,glob; from PIL import Image
fs=sorted(glob.glob(sys.argv[1]+'/*.png')); a,b=int(sys.argv[3]),int(sys.argv[4]); fs=fs[a:b]
W,H=480,270; c=4; r=(len(fs)+c-1)//c; im=Image.new('RGB',(W*c,H*r))
for i,f in enumerate(fs): im.paste(Image.open(f).resize((W,H)),((i%c)*W,(i//c)*H))
im.save(sys.argv[2])
