## Overview

This package contains an anytime search-based planner for dynamic
environments. The planner finds a collision free path (x,y,theta,time)
from a start state to a goal state given a static costmap and predicted
future trajectories for moving obstacles. The planner requires motion
primitives to be defined which are the basic motions the robot can
execute. The planner also requires the robot to be capable of waiting in
place. It then searches for a path from the start to the goal using
motions and waits. The planner uses a modified version of ARA\* (Anytime
Repairing A\*) in order to provide solutions quickly.

This planner clusters contiguous blocks of timesteps for an x,y cell
which have no collisions into "safe intervals". While the number of
timesteps in an x,y cell is huge, the number of safe intervals tends be
very small (generally on the order of the number of dynamic obstacles).
The search is performed in the (x,y,theta,interval) state space instead
of (x,y,theta,time) space, providing a large speed-up.

More detail about the planner can be found in this paper.
```
Mike Phillips and Maxim Likhachev, "SIPP: Safe Interval Path Planning for Dynamic Environments, "Proceedings of the IEEE International Conference on Robotics and Automation (ICRA), 2011.
```

### How to Use

The planner is compiled as a library and can be used directly. However,
unless you have a special use case, it is much easier to use the wrapper
package
[sbpl_dynamic_env_global_planner](sbpl_dynamic_env_global_planner) which
adheres to the nav_core::BaseGlobalPlanner interface specified in
[nav_core](nav_core).

The motion primitive file format is the same as for [sbpl](sbpl) except
that the time resolution needs to be added on the second line of the
file.

```
resolution_m: 0.050000
timeResolution: 0.001
numberofangles: 16
totalnumberofprimitives: 112
...
```

Some examples of this can be found in the matlab/mprim folder of the
package.

### Videos

The following video shows planner in use on the PR2 and in simulation.

[Youtube](https://www.youtube.com/watch?v=khzJUVnN4rw)
