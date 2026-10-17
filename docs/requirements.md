# SGS requirements

## Confirmed in project discussion

| Item | Value |
|---|---|
| Name | SupportGrowSystem (SGS) |
| Crop | Strawberries; replaces earlier tomato concept |
| Tasks | Move whole baskets and harvest fruit |
| Layout | Four towers, 2 × 2 |
| Nominal frame envelope | 1000 × 1000 × 3000 mm |
| Tower height | 650 mm |
| Basket level heights | 400 and 540 mm above floor |
| Basket socket angle | 45 degrees; verify exact datum on physical tower |
| Basket rim outside diameter | 55 mm including rim |
| Basket body diameter immediately below rim | 48.20 mm |
| Rim thickness | 2.15 mm |
| Basket depth | 60 mm |
| Under-rim gap | At least 10 mm |
| Requested minimum extraction | 60 mm |
| Arm construction | Printed links/housings with metal shafts, bearings and fasteners |
| Openness | Open source and open hardware |

## Proposed, not validated

Six arm axes: base rotation, shoulder, elbow, forearm roll, wrist tilt and tool roll. Separate claw servo. X–Y gantry and Z lift provide positioning. Coordinated joint movement provides straight extraction; an additional dedicated extraction slide is no longer assumed mandatory.

80 mm axial extraction target; 49 mm nominal closed gripper opening and approximately 62 mm open. Two tool heads; manual changes first, automatic tool changes later. Camera near wrist and fruit collection tray proposed.

## Unresolved before arm sizing

- Wet planted basket mass, fruit load, root entanglement and measured extraction force.
- Socket positions and orientations, number of sockets, tower centre spacing.
- Earlier 350 mm diameter and 260 mm opposite-basket span descriptions need a drawing and unambiguous reference points; neither is treated as the net-pot diameter.
- Exact tower geometry, lateral claw access, approach path and arm collision envelope.
- Motors, servo models, reductions, bearings, shafts, printable material and joint stiffness.
- Link lengths, joint limits, payload, accuracy, duty cycle, cable routing and reach validation.
- Harvest stem access, fruit support, cutter mechanism and tool attachment.

No motor torque, payload capacity or guaranteed access to every socket is claimed.
