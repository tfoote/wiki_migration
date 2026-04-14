## Hardware Requirements

This package offers a cartesian interface for a kinematical chain on
Care-O-bot. E.g. for the 7 DOF arms (Schunk LWA and Kuka LBR), but also
for the 4 DOF torso. The interface works for real hardware as well as
for simulation. To bringup a Care-O-bot see [cob_bringup](cob_bringup).

## Usage/Examples

For starting the ik solver ```
roslaunch cob_manipulator kdl_solver.launch
```
