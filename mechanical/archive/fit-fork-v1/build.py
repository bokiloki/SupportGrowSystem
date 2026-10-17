import math,struct,collections,zipfile
from pathlib import Path
p=Path(__file__).parent
# Flat fork, open toward negative Y; semicircular cradle radius 24.5.
r=24.5
pts=[(-34.5,-30),(-r,-30),(-r,0)]
pts += [(r*math.cos(math.pi-i*math.pi/48),r*math.sin(math.pi-i*math.pi/48)) for i in range(1,49)]
pts += [(r,-30),(34.5,-30),(34.5,40),(-34.5,40)]
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
if sum(pts[i][0]*pts[(i+1)%len(pts)][1]-pts[(i+1)%len(pts)][0]*pts[i][1] for i in range(len(pts)))<0:pts.reverse()
def inside(p,a,b,c):return min(cross(a,b,p),cross(b,c,p),cross(c,a,p))>=-1e-9
idx=list(range(len(pts))); tris=[]
while len(idx)>3:
 for k,b in enumerate(idx):
  a,c=idx[k-1],idx[(k+1)%len(idx)]
  if cross(pts[a],pts[b],pts[c])>1e-9 and not any(inside(pts[j],pts[a],pts[b],pts[c]) for j in idx if j not in (a,b,c)):
   tris.append((a,b,c));idx.pop(k);break
 else:raise RuntimeError('triangulation failed')
tris.append(tuple(idx));n=len(pts)
v=[(x,y,z) for z in (0,3) for x,y in pts];f=[]
for a,b,c in tris:f.extend([(c,b,a),(a+n,b+n,c+n)])
for a in range(n):
 b=(a+1)%n;f.extend([(a,b,b+n),(a,b+n,a+n)])
edges=collections.Counter(tuple(sorted(e)) for t in f for e in ((t[0],t[1]),(t[1],t[2]),(t[2],t[0])))
assert all(x==2 for x in edges.values())
with (p/'SGS_rim_fit_fork_v1.stl').open('wb') as o:
 o.write(b'SGS manual rim fit fork - millimetres'.ljust(80,b'\0'));o.write(struct.pack('<I',len(f)))
 for t in f:o.write(struct.pack('<12fH',0,0,0,*[q for i in t for q in v[i]],0))
(p/'SGS_rim_fit_fork_v1.scad').write_text('// Millimetres. Manual fit coupon only. Print flat.\nlinear_extrude(height=3) polygon(points='+str(pts)+');\n')
(p/'README.txt').write_text('''SGS basket rim fit fork v1 — MANUAL FIT TEST ONLY
Confirmed basket: rim OD 55 mm, body OD below rim 48.20 mm,
rim thickness 2.15 mm, depth 60 mm, under-rim gap at least 10 mm.

This is a single-piece manual fork, not the motorized gripper.
Dimensions: 69 x 70 x 3 mm; open slot and semicircular cradle 49 mm.
At full seating the nominal radial rim overlap is 3 mm.
This checks usable access and fit before designing two moving jaws.
No motor mount or fasteners are included.

PRINT: STL units mm; flat on the bed; prototype PETG, 0.2 mm layer,
4 walls, 100% infill; no supports. Deburr contact edges gently.

TEST:
1. Try on an empty loose basket. Slide the fork under the rim from the side.
2. Repeat while basket is seated in its actual hydrostack holder.
   The holder must allow the full fork approach; 10 mm vertical gap alone
   does not establish lateral clearance. Do not force it.
3. Support the basket by hand and pull along its insertion axis at 45 deg.
   Check holder release and interference before loading with a plant.
4. Report whether it fits, whether it slips, and a spring-scale measurement
   of extraction force in newtons (if possible). Also weigh a representative
   wet planted basket. These determine motor and jaw sizing.

NEXT DESIGN: two moving jaws with replaceable rim supports; nominal 60 mm
open tip clearance; adjustable closure; 80 mm axial extraction proposed.
Root entanglement and plant clearance still require a real extraction test.
The fit coupon has no verified load rating. Do not use overhead.

Included: STL mesh, editable OpenSCAD outline, generation script.
Mesh checked: every mesh edge belongs to two triangles (closed surface).
Physical fit and strength are untested.
''')
with zipfile.ZipFile(p.parent/'SGS_gripper_fit_test_v1.zip','w',zipfile.ZIP_DEFLATED) as z:
 for name in ['SGS_rim_fit_fork_v1.stl','SGS_rim_fit_fork_v1.scad','README.txt','build.py']:z.write(p/name,name)
print('Created closed STL:',len(f),'triangles; package ready')
