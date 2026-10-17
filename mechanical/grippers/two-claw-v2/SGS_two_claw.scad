// SGS v2 symmetric sliding claws. Units mm. Prototype; servo mount is model-dependent.
$fn=64;
part="assembly"; // right_claw,left_claw,base,keeper,link,horn_gauge,assembly
closed_anchor=28.45;
module claw(){
 difference(){
 union(){
 // slider, neck, and curved under-rim ledge
 translate([24,-7,0]) cube([34,14,3]);
 hull(){translate([32,-5,0]) cylinder(r=5,h=3);translate([30,-32,0]) cylinder(r=5,h=3);}
 translate([0,-45,0]) intersection(){difference(){cylinder(r=34,h=3);translate([0,0,-1]) cylinder(r=24.5,h=5);}translate([0,-16,-1])cube([40,32,5]);}
 }
 translate([closed_anchor,0,-1]) cylinder(d=3.3,h=5);
 }
}
module base(){difference(){
 union(){translate([-65,-14,0])cube([130,28,4]);
 // rail fences, 0.4 mm lateral clearance
 for(y=[-11.4,7.4]) translate([-65,y,4])cube([130,4,3.4]);}
 for(s=[-1,1]) translate([s==1?19:-44,-16,3.9])cube([25,9,8]);
 // servo shaft clearance; this is not a servo mounting pattern
 translate([0,0,-1])cylinder(d=24,h=6);
 for(x=[-58,-18,18,58],y=[-9.4,9.4])translate([x,y,-1])cylinder(d=2.5,h=10);
 }}
module keeper(){difference(){cube([130,4,3]);for(x=[7,47,83,123])translate([x,2,-1])cylinder(d=3.3,h=5);}}
module front_keeper(){difference(){keeper();for(x=[21,84])translate([x,-1,-1])cube([25,6,5]);}}
module link(){difference(){hull(){cylinder(d=8,h=3);translate([25,0,0])cylinder(d=8,h=3);}for(x=[0,25])translate([x,0,-1])cylinder(d=3.3,h=5);}}
module horn_gauge(){difference(){hull(){translate([-10,0,0])cylinder(d=8,h=3);translate([10,0,0])cylinder(d=8,h=3);}for(x=[-10,0,10])translate([x,0,-1])cylinder(d=3.3,h=5);}}
if(part=="right_claw")claw();
if(part=="left_claw")mirror([1,0,0])claw();
if(part=="base")base();
if(part=="keeper")keeper();
if(part=="front_keeper")front_keeper();
if(part=="link")link();
if(part=="horn_gauge")horn_gauge();
if(part=="assembly"){
 color("gray")base();
 for(s=[-1,1]){color("orange")translate([0,0,4.2])scale([s,1,1])claw();color("gray")translate([-65,s*9.4-2,7.4])if(s<0)front_keeper();else keeper();}
 // 60 degree horn position = nominal closed state. Links shown at shared z.
 color("blue")translate([0,0,8])rotate([0,0,60])horn_gauge();
 for(s=[-1,1])let(a=[s*5,s*8.660],b=[s*closed_anchor,0],ang=atan2(b[1]-a[1],b[0]-a[0]))color("green")translate([a[0],a[1],11.2])rotate([0,0,ang])link();
}
