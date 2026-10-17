from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
import math
p=Path(__file__).resolve().parents[2];im=Image.new('RGB',(1800,1450),'#092b4d');d=ImageDraw.Draw(im)
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
f=lambda n:ImageFont.truetype(font,n)
white='#d8f2ff';cyan='#71cfff';gold='#ffd17b';grey='#66849e'
for x in range(0,1800,25):d.line((x,0,x,1450),fill='#123756')
for y in range(0,1450,25):d.line((0,y,1800,y),fill='#123756')
def t(x,y,s,n=21,c=white):d.text((x,y),s,font=f(n),fill=c)
def line(points,c=white,w=3):d.line(points,fill=c,width=w)
def box(r,c=white,w=2):d.rectangle(r,outline=c,width=w)
def arrow(a,b,c=cyan):
 line([a,b],c,3);ang=math.atan2(b[1]-a[1],b[0]-a[0]);s=12
 for z in [-.5,.5]:line([b,(b[0]-s*math.cos(ang+z),b[1]-s*math.sin(ang+z))],c,3)
def dim(a,b,label):
 arrow(a,b);arrow(b,a);t((a[0]+b[0])/2-65,(a[1]+b[1])/2-27,label,19,cyan)
box((25,25,1775,1425));t(55,43,'SGS / SUPPORTGROWSYSTEM',36);t(55,93,'REV 03  |  MOTORIZED BENDING WRIST + TWO-CLAW GRIPPER',23,cyan)
t(55,132,'Concept layout • dimensions in mm • not to scale • not a fabrication drawing',19,gold)
box((50,185,800,970));t(75,202,'01 / FRONT ELEVATION',24)
# Frame uses 600 px height for 3000 mm
for x in [200,620]:box((x,285,x+12,885))
box((200,285,632,310));box((200,860,632,885));box((330,310,390,340));box((350,340,370,700))
d.ellipse((347,695,375,723),outline=gold,width=3);line([(361,709),(402,750)],gold,7)
# Towers 130 px high from floor
for x in [260,475]:
 box((x,755,x+70,885))
 for yy in [805,777]:
  for s in [-1,1]:line([(x+35+s*35,yy),(x+35+s*52,yy-17)],white,6)
line([(180,885),(670,885)])
dim((145,285),(145,885),'3000');dim((200,925),(632,925),'1000')
line([(620,805),(705,805)],cyan);t(650,815,'400',18,cyan)
line([(620,777),(705,777)],cyan);t(650,750,'540',18,cyan)
t(230,365,'Overhead X / Y gantry',20);t(405,500,'Z travel',20);t(235,700,'650-high towers',19)
t(75,945,'Tower levels referenced to floor; basket axes at 45°.',17)
box((50,995,800,1380));t(75,1012,'02 / PLAN — FOUR TOWERS, 2 × 2',23)
box((180,1060,470,1350))
for x in [255,395]:
 for y in [1135,1275]:d.ellipse((x-43,y-43,x+43,y+43),outline=white,width=3)
t(505,1090,'1000 × 1000 footprint',20);t(505,1140,'Tower spacing: TBD',19,gold);t(505,1180,'260 opposite-basket',18);t(505,1208,'span: confirm datum',18);t(505,1260,'Tower positions shown',18);t(505,1288,'schematically.',18)
box((825,185,1750,1000));t(850,202,'03 / SIDE VIEW — SERVO BENDS THE WRIST',24)
box((1125,270,1170,525));t(880,290,'Z carriage',21);line([(1005,308),(1125,308)],cyan)
# Fork yoke and supported pivot
line([(1125,500),(1100,550),(1100,610)],white,5);line([(1170,500),(1210,550),(1210,610)],white,5)
d.ellipse((1120,570,1190,640),outline=gold,width=4);d.ellipse((1143,593,1167,617),outline=white,width=3)
box((1025,565,1090,645),gold);line([(1090,605),(1120,605)],gold,5)
t(850,465,'M1: wrist servo / geared motor',20,gold);t(850,495,'Bearing-supported pivot shaft',19)
# vertical rest ghost
for y in range(645,915,24):line([(1155,y),(1155,y+12)],grey,4)
t(870,855,'0° reference',20,grey);line([(1010,872),(1150,872)],grey)
# bent forearm
line([(1155,605),(1330,780)],white,14);box((1240,670,1278,708),gold)
t(1390,555,'M2: extraction drive',20);line([(1430,590),(1320,735)],cyan)
line([(1305,788),(1410,893)],cyan,5);line([(1320,773),(1425,878)],cyan,5)
arrow((1340,766),(1440,866));t(1435,735,'80 travel',20,cyan);t(1435,765,'proposed',18,cyan)
# gripper stylized cross to extraction axis
line([(1390,910),(1445,855)],gold,8);line([(1390,910),(1417,937)],gold,5);line([(1445,855),(1472,882)],gold,5)
d.ellipse((1412,875,1490,953),outline=white,width=3)
line([(1417,937),(1450,970),(1510,910),(1472,882)],white,3)
t(1500,865,'Basket',20);t(1500,898,'Ø55 rim',19);t(1500,930,'60 deep',19)
t(850,920,'M3: claw servo → two opposing jaws',21,gold)
line([(1185,668),(1206,656),(1220,639)],gold,3);t(1218,614,'45° target',22,gold)
t(850,965,'Alignment first → grip → straight extraction → clear tower → bend.',17)
box((825,1025,1750,1380));t(850,1043,'04 / CONFIRMED INTERFACE + DESIGN STATUS',23)
for i,s in enumerate(['Basket body below rim: Ø48.20  |  rim thickness: 2.15',
'Under-rim gap: ≥10  |  prototype claw thickness: 3',
'Claw clearance: 49 closed / approximately 62 open',
'NEW: powered wrist pivot; separate from claw actuation.',
'Wrist range, arm lengths, bearings and stops: to be engineered.',
'Motor torque / mounts depend on payload and extraction force.',
'Existing v2 STL pack does not include this new wrist.']):t(850,1090+i*36,s,19,gold if i>=4 else white)
t(55,1395,'SGS • 2026-10-17 • Proposed motion architecture; verify reach, collisions and root clearance before manufacture.',17)
im.save(p/'docs/blueprints/SGS_blueprint_bending_wrist_v3.png')
print(p/'SGS_blueprint_bending_wrist_v3.png')
