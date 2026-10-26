**Please note that the source link above is wrong. Please download the
SBPL here:**

**git clone <https://github.com/sbpl/sbpl.git>**

This package implements a generic set of motion planners using search
based planning. It was developed by Maxim Likhachev at the University of
Pennsylvania in collaboration with Willow Garage.

## Video

[Youtube](https://www.youtube.com/watch?v=LaThdWSOT8U)

## Documentation

The API documentation for this package can be found
[here](http://www.ros.org/doc/api/sbpl/html/index.html).

A good resource for technical information on the planners in the SBPL
package is Maxim Likhachev's presentation
([pdf](http://www.ros.org/wiki/Events/CoTeSys-ROS-School?action=AttachFile&do=get&target=robschooltutorial_oct10.pdf),[movie](http://fallschool2010.cs.tum.edu/public/lectures/saturday/index.html#maxim))
at the ROS Cotesys School at TUM, Germany in November 2010.

### Motion Primitives

Motion primitives are short, kinematically feasible motions which form
the basis of movements that can be performed by the robot platform.
Search-based planners (like the ones in this library) can generate paths
from start to goal configurations by combining a series of these motion
primitives. The result is a smooth kinematically feasible path for the
robot to follow.

Several planners make use of SBPL and these motion primitives to produce
smooth paths:

- [sbpl_arm_planner](http://ros.org/wiki/sbpl_arm_planner) - 3DoF and
  6DoF arm planning for the PR2
- [sbpl_lattice_planner](http://ros.org/wiki/sbpl_lattice_planner) -
  (x,y,yaw) planning for robot navigation (handles non-circular
  footprints and nonholonomic constraints)

#### Pre-made Motions (x,y,yaw navigation)

This package has two pre-made motion primitive files for the PR2 (though
these motions are a reasonable choice for many other robots).

- matlab/mprim/pr2.mprim - Motion primitives that only allow forward,
  backward, turn-in-place, and forward-and-turn-arc motions
- matlab/mprim/pr2sides.mprim - Same as pr2.mprim (previous) but
  includes strafing left and right as allowable motions

#### Generating your own Motions (x,y,yaw navigation)

Sometimes the pre-made will not be good enough either because you are
using a map of a different resolution (a motion primitive file only
works on a map with its corresponding resolution) or because your
robot's motions don't match with any of the pre-made motions.

In the matlab/mprim folder there are several matlab scripts which are
easy to modify and generate new motion primitives. They are named
according to the types of motions they generate.

- genmprim_unicycle.m - forward, backward, turn-in-place,
  forward-turn-arcs
- genmprim_unicycleplussideways.m - like previous but with strafing
  left/right
- genmprim_unicycleplussidewaysplusbackturn.m - like previous but with
  backward-turn-arcs
- genmprim_unicycleplussidewaysplusbackturnplusdiag.m - like previous
  but with diagonal moves

Parameters

- Resolution - Near the top of each of these files there is a
  "resolution" variable which you can set you your map's resolution.
- Number of angles - The variable "numberofangles" represents the yaw
  discretization. The more you have the better your paths will look but
  the planning time will also increase because there are more states to
  search. Be careful changing this as you will need to add/remove motion
  vectors in the rest of the script.
- Number of motions - The variable "numberofprimsperangle" represents
  the number of motions
- Multipliers - There is a multiplier for each type of motion
  (forwardcostmult, backwardcostmult, etc) which is multiplied by the
  cost of using the motion. You can use these multipliers to discourage
  certain motions (making the multiplier larger) so that the robot only
  uses them if it has to.
- Motions - There will be several vectors (each for a different
  direction) of motions. Each element of a vector is a 4-tuple
  representing (dx, dy, dyaw, multiplier). You can change what
  multiplier a motion uses and how it moves by changing these. Remember
  that the number of 4-tuples in each vector must equal the
  "numberofprimsperangle" variable.

## ROS API

- The ROS API is UNREVIEWED and UNSTABLE
- The C++ API is UNREVIEWED and UNSTABLE
