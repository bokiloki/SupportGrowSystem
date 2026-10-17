SGS TWO-CLAW SERVO GRIPPER v2 — FIT/MECHANISM PROTOTYPE
Units: millimetres. Physical fit, force capacity and servo compatibility untested.

PRINT ONCE: right_claw.stl, left_claw.stl, base.stl, keeper.stl,
front_keeper.stl. PRINT TWICE: link.stl.
Optional horn_gauge.stl is a hole-spacing gauge, NOT a servo spline adapter.
Editable design and nominal closed assembly: SGS_two_claw.scad.

Basket: rim OD55; body below rim48.20; rim thickness2.15; depth60;
under-rim gap>=10. Curved jaw ledges are 3 mm thick, inner radius24.5.
Nominal rim overlap at the side is 3 mm. Closed body clearance49.
The base sits behind the rim, with basket centre 45 mm forward of servo axis.
Check that the actual tower allows the entire approach, including claw arms.

MECHANISM:
Two sliding jaws. Central servo shaft normal to the jaw plane.
Opposed horn link holes: 20 mm centre-to-centre, 10 mm each side of shaft.
Links: 25 mm between M3 clearance holes.
At horn angle0 relative to slider axis, jaw anchors are +/-35 mm (open).
At angle60 deg, anchors are +/-28.45 mm (closed).
Each claw translates 6.55 mm, giving ~62.1 mm open and49 mm closed.
Stay away from the exact 0-degree dead centre during powered testing;
start around10 degrees and approach60 gradually. Calibrate to real basket.
This is horn angle in the drawing, NOT necessarily servo command angle.

ASSEMBLY:
Print flat; prototype PETG,0.2 mm layers,4 walls,100% infill.
Deburr/slightly finish slides as needed. Do not force printed fits.
Place both claws on the base top at z=4.2 mm, leaving0.2 mm vertical clearance.
Fit rear keeper and slotted front keeper to rail tops; nominal overhead
clearance is0.2 mm. Use eight M3 screws in2.5 mm pilot holes; size lengths
for engagement without breaking through. Verify free sliding manually first.
Link pin axes on each claw at x=+/-28.45,y=0 in closed state.
Links sit at z=11.2..14.2. Use equal-height rigid spacers so their lower faces
clear the keeper tops at z=10.4; set pivot stacks to rotate freely.
Use M3 pin hardware/washers/locknuts with lengths chosen for actual stack.
A compatible servo horn must place its pin contact plane at the same height.
Use servo-supplied horn/spline; do not press the printed gauge onto the shaft.

SERVO MOUNT NOT INCLUDED:
24 mm base shaft opening is clearance only. No servo bolt pattern is assumed.
Provide exact servo model (or dimensions plus horn photograph) to finish
an underside bracket and confirm torque, shaft position and horn compatibility.
Some included horn gauges or link stacks may need model-specific revision.

FIRST TEST:
1. Move jaws by hand; check slider and link clearance over full travel.
2. Fit an empty basket, then repeat in actual tower. Support it by hand.
3. With servo unpowered, check linkage travel and rim engagement.
4. Only after proper mounting and calibration, test servo slowly with
   conservative travel limits. Do not drive against a hard stop.
5. Measure wet basket mass and extraction force before selecting final torque.

Gripper handles rim capture only. The proposed80 mm extraction slide and
45-degree mounting are separate mechanisms and are not included in this pack.
Roots and plant mass may prevent simple basket withdrawal.
