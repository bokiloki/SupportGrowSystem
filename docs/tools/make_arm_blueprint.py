from pathlib import Path
exec(Path(__file__).with_name('make_blueprint.py').read_text().split('im.save(')[0])
# Replace the right panels with the articulated-arm architecture.
d.rectangle((826,186,1749,1379),fill='#092b4d');box((825,185,1750,1000));box((825,1025,1750,1380))
d.rectangle((50,85,1750,170),fill='#092b4d')
t(55,93,'REV 04  |  SIX-AXIS ARTICULATED ARM ON X–Y GANTRY',23,cyan)
t(55,132,'Concept layout • dimensions in mm • arm geometry illustrative • not a fabrication drawing',19,gold)
t(850,202,'03 / SIX POWERED JOINTS + CLAW SERVO',24)
box((1070,275,1410,310));box((1160,310,1230,345));t(1430,280,'X–Y carriage',18)
# arm chain, from overhead mount down to basket
pts=[(1195,370),(1195,460),(1380,610),(1230,760),(1295,815),(1350,850)]
line([(1195,345),pts[0]],white,12)
for a,b in zip(pts,pts[1:]):line([a,b],white,15)
for i,(x,y) in enumerate(pts):
 d.ellipse((x-19,y-19,x+19,y+19),fill='#092b4d',outline=gold,width=4)
 t(x-12,y-13,str(i+1),18,gold)
# Labels placed away from links
labels=[(870,350,'J1 / base rotation',pts[0]),(870,440,'J2 / shoulder',pts[1]),(1430,565,'J3 / elbow',pts[2]),(870,700,'J4 / forearm roll',pts[3]),(1430,750,'J5 / wrist tilt',pts[4]),(1430,817,'J6 / tool roll',pts[5])]
for x,y,s,b in labels:
 t(x,y,s,19);a=(x+205,y+13) if x<1100 else (x-10,y+13);line([a,b],cyan,2)
line([(1330,890),(1375,845)],gold,7);line([(1330,890),(1352,912)],gold,5);line([(1375,845),(1397,867)],gold,5)
d.ellipse((1350,867,1415,932),outline=white,width=2)
t(850,920,'G / independent servo opens and closes both claws',20,gold)
t(850,960,'Coordinated joints provide straight basket extraction.',19)
t(850,1043,'04 / MOTION + DESIGN STATUS',24)
for i,s in enumerate(['X–Y: selects tower and approach position.',
'J1–J3: position the gripper; J4–J6: orient it.',
'Align at 45° → grip rim → withdraw straight → transfer.',
'Basket: Ø55 rim / Ø48.20 body / 60 deep / 2.15 rim.',
'Withdrawal target: 80 mm along the basket axis.',
'Arm lengths, joint limits, payload and motors: TBD.',
'Reach and collision study required for every socket.',
'Existing v2 STLs cover claws only; arm CAD not yet built.']):t(850,1085+i*34,s,18,gold if i>=5 else white)
# Replace schematic wrist in front elevation with miniature articulated arm
# Keep tower drawing below untouched.
d.rectangle((335,340,455,752),fill='#092b4d')
line([(360,340),(360,430),(435,520),(370,600),(400,650)],gold,7)
for x,y in [(360,365),(360,430),(435,520),(370,600),(385,625),(400,650)]:d.ellipse((x-7,y-7,x+7,y+7),fill='#092b4d',outline=white,width=2)
t(465,490,'6-axis arm',19);t(215,710,'650-high towers',19)
d.rectangle((55,1390,1745,1420),fill='#092b4d');t(55,1395,'SGS • REV 04 • Proposed articulated-arm architecture; no reach, strength or collision validation yet.',17)
d.rectangle((185,260,640,748),fill='#092b4d')
for x in [200,620]:box((x,285,x+12,748))
box((200,285,632,310));box((330,310,390,340));box((350,340,370,640))
line([(360,640),(360,675),(425,700),(385,735)],gold,6)
for x,y in [(360,645),(360,675),(425,700),(385,735)]:d.ellipse((x-6,y-6,x+6,y+6),fill='#092b4d',outline=white,width=2)
t(400,365,'X–Y gantry',18);t(400,480,'Z positioning lift',18);t(435,690,'6-axis arm',18)
t(1430,310,'+ Z lift',18,cyan)
im.save(p/'docs/blueprints/SGS_articulated_arm_blueprint_v4.png')
