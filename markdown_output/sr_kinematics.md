## Overview

sr_kinematics currently contains a specific analytical inverse
kinematics for the [shadow_robot](shadow_robot) hand. Currently, only
the 4 fingers have an IK solution, the thumb will come later. The
solution takes care of the coupled joint J1/J2 (assuming it is 1:1) and
accepts 3D requests (instead of 6D). There is an approximation in this
solution.

## Detail of the solution

### Approximation

The developed IK uses an approximation of the fingertip center to create
a virtually simplified 2 links (3 dof) kinematic chain. The method
considers the isoceles triangle formed by the coupled joint to solve the
inverse kinematics.

.
![\|height=\"336px\",width=\"393px\"](attachment:finger_approximation.png)

### Limits

-   Because the finger chain (J4+J3+J1/J2) provides only 3 dof, the
    request only takes the position of the finger tip into account (no
    requested orientation can be reached).
-   The Little finger joint 5 (inside the palm) is not considered
    either.
-   IK for the thumb is not solved by the current version.

## ROS API

### Services

The node proposes the same services and parameters as the
[arm_kinematics](arm_kinematics)

NOTE that \'\'\'epsilon\'\'\' parameter is used to detect singularities
for J4 joint.
