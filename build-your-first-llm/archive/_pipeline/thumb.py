import sys; from PIL import Image, ImageDraw, ImageFont, ImageOps
num,title,sub,art,out=sys.argv[1:6]
W,H=1280,720; im=Image.new('RGB',(W,H)); d=ImageDraw.Draw(im)
for x in range(W):  # brand gradient (navy -> purple)
    t=x/W; d.line([(x,0),(x,H)],fill=(int(18+60*t),int(16+10*t),int(60+90*t)))
B='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; F=lambda s: ImageFont.truetype(B,s)
if art!='-':
    a=Image.open(art).convert('RGB'); a.thumbnail((520,480)); im.paste(a,(W-a.width-40,H-a.height-60))
    d.rectangle([W-a.width-44,H-a.height-64,W-36,H-56],outline=(255,143,224),width=4)
av=Image.open('/workspace/x-brand/avatar.png').resize((120,120)); m=Image.new('L',(120,120),0); ImageDraw.Draw(m).ellipse([0,0,119,119],fill=255); im.paste(av,(40,30),m)
d.text((178,52),'Waqar Shaikh Builds',font=F(40),fill=(255,255,255)); d.text((178,104),'Build Your First LLM · study series',font=F(26),fill=(180,200,255))
d.rounded_rectangle([40,190,300,280],radius=18,fill=(126,224,195)); d.text((60,200),f'CH {num}',font=F(64),fill=(15,23,36))
y=310
for line in title.split('|'):
    d.text((40,y),line,font=F(76),fill=(255,212,121)); y+=92
d.text((40,y+10),sub,font=F(34),fill=(230,237,243))
d.text((40,H-50),'Based on the book by Hasan Degismez',font=F(22),fill=(170,180,200))
im.save(out); print(out,im.size)
