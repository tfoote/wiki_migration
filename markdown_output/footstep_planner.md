![\|](attachment:footsteps_nao_video.png)

## Overview

This package provides footstep planning for humanoid (biped) robots. The
first release built on D\* Lite (Koenig et al. 2002) for efficient
replanning. The current version now builds on [sbpl](sbpl). This enables
D\* and A\* implementations with anytime capabilities, and the
randomized A\* (R\*) search.

Details are available at
<http://hrl.informatik.uni-freiburg.de/research/animations/footsteps/>
and in the following publications. Please consider citing our paper if
you use the footstep planner in your research.

-   **[Anytime Search-Based Footstep Planning with Suboptimality Bounds](http://hrl.informatik.uni-freiburg.de/papers/hornung12humanoids.pdf)**
    by A. Hornung, A. Dornbush, M. Likhachev, and M. Bennewitz
    (Humanoids 2012). ```
@INPROCEEDINGS{hornung12humanoids,
  author = {Armin Hornung and Andrew Dornbush and Maxim Likhachev and 
  Maren Bennewitz},
  title = {Anytime Search-Based Footstep Planning with Suboptimality 
  Bounds},
  booktitle = {Proc. of the IEEE-RAS International Conference on Humanoid 
  Robots (HUMANOIDS)},
  year = 2012
}
```

```{=html}
<!-- -->
```
-   **[Humanoid Navigation with Dynamic Footstep Plans](http://hrl.informatik.uni-freiburg.de/papers/garimort11icra.pdf)**
    by J. Garimort, A. Hornung, and M. Bennewitz (ICRA 2011).
    ```
@INPROCEEDINGS{garimort11icra,
  author = {Johannes Garimort and Armin Hornung and Maren Bennewitz},
  title = {Humanoid Navigation with Dynamic Footstep Plans},
  booktitle = {Proc. of the IEEE International Conference on Robotics and
  Automation (ICRA)},
  year = 2011
}
```

The planner can be invoked by interacting with it via RViz, or by
continuously using it during plan execution (Video below). A pose
estimate from a localization system is required in the latter case.

[Youtube](https://www.youtube.com/watch?v=o0rlrEHN1w4)

## Getting started

First, follow the installation instructions of the
[humanoid_navigation](humanoid_navigation) stack (you might have to
check out the source for that or
[download a recent package](http://code.google.com/p/alufr-ros-pkg/downloads/list)).

For interactive planning (without any plan execution by a robot),
you\'re almost set now. Simply run ```
roslaunch footstep_planner footstep_planner_complete.launch
``` which loads
a sample map, starts up the planner, and launches RViz to interact with
it. Set a \"2D pose estimate\" as start, and a \"2D nav goal\" as goal
(Hotkeys **P** and **G**). After some time (depending on footsteps,
heuristic and the environment), the planner will visualize the footstep
plan in RViz or output an error on the terminal.

![\|](attachment:footsteps_rviz_sample.png)

## Planners

For footstep planning, the planners Anytime Repairing A\* (ARA\*),
Anytime Dynamic A\* (AD\*), and Randomized A\* (R\*) are supported. All
of them offer anytime capabilities (see parameters below) and may be
suitable for different scenarios.

The parameter planner_type can have the following values: ARAPlanner,
ADPlanner, RSTARPlanner.

The R\* implementation in the currently released SBPL version (1.1.0)
unfortunately segfaults, so using R\* requires the compilation and
installation of a newer version (see
[Tutorial](footstep_planner/Tutorials/Compile footstep_planner with the latest SBPL version)).

## Heuristics

Currently, there are three heuristics available to the planner,
described in detail in the paper. They can be selected with the
`heuristic_type` parameter:

-   \"!EuclideanHeuristic\": Straight-line distance to the goal
-   \"!EuclStepCostHeuristic\": Straight-line distance to the goal with
    added footstep costs
-   \"!PathCostHeuristic\": Distance along 2D path pre-planned with A\*
    (preferred). This heuristic works best in most cases, as it is most
    informed of the environment. Note that it is potentially
    inadmissible in the case of stepping over obstacles.

## Footstep parameterization

### Model

![\|height=\"150px\"](attachment:footstep_model2.png)

Since version 0.3, footsteps are parameterized as a general 2D transform
(x,y,theta) of the swinging (walking) leg\'s foot from the current
supporting leg\'s foot origin. Footstep sets are specified in the
parameter arrays \`footsteps/{x,y,theta}\` (see below).

#### Old Model (v0.2 and before)

![\|height=\"150px\"](attachment:footstep_model.png)

Before, footsteps were parametrized by the displacement (x,y,theta) of
the swinging (walking) leg\'s foot from its default position next to the
current supporting leg\'s foot, which was specific to the Nao\'s old
walking algorithm. For a displacement of (0,0,0), the walking foot is
placed next to the supporting foot at a distance of \`foot/separation\`.

### Parameterization for the Nao

![\|](attachment:footsteps_nao.png)

A footstep parameterization for the [Nao humanoid](Robots/Nao) is given
in \`config/footsteps_nao.yaml\`.

### Parameterization for larger humanoids

![\|](attachment:footsteps_asimo.png)

A footstep set for a larger humanoid which is capable of stepping over
obstacles (e.g. Asimo or HRP-2) is given in
\`config/footsteps_asimo.yaml\`.

![\|](attachment:footstep_plan_asimo.png)

## ROS API

See
[Code API](http://www.ros.org/doc/api/footstep_planner/html/index.html)
for documentation of all classes and relevant code. The ROS node
interface is described below. Both might be subject to change in the
future as we develop the package further.

```clearsilver
node.0 {
 name = footstep_planner_node
 desc = The planning ROS node which listens to pose callbacks to plan footstep paths, either interactively in RViz (set pose estimate and navigation goal) or continuously while a robot executes the path.
 sub {
  0.name = goal
  0.type = geometry_msgs/PoseStamped
  0.desc = Goal pose (x, y, theta) in the map frame
  1.name = initialpose
  1.type = geometry_msgs/PoseWithCovarianceStamped
  1.desc = Current starting pose (x, y, theta) in the map frame
  3.name = map
  3.type = nav_msgs/OccupancyGrid
  3.desc = 2D Grid Map e.g. originating from `map_server`. A map change will trigger replanning.
 }

 pub {
  0.name=~footsteps_array
  0.type=visualization_msgs/MarkerArray
  0.desc=Visualization of the planned footsteps

  1.name=~path
  1.type=nav_msgs/Path
  1.desc=Visualization of the planned path (connecting left and right footsteps)

  2.name=~heuristic_path
  2.type=nav_msgs/Path
  2.desc=Visualization of the heuristic

  3.name=~expanded_states
  3.type=sensor_msgs/PointCloud
  3.desc=Visualization of the expaded nodes

  4.name=~start
  4.type=visualization_msgs/PoseStamped
  4.desc=Visualization of the requested start pose
 }

 srv {
  0.name = plan_footsteps
  0.type = humanoid_nav_msgs/PlanFootsteps
  0.desc = Plan a footstep sequence from a given start to goal, return the costs and success.
 }

 param {
  1.name = ~heuristic_type
  1.type = string
  1.desc = Which heuristic to use (see [[http://www.ros.org/wiki/footstep_planner#Heuristics|Heuristics]]). For the fastest results, !PathCostHeuristic is recommended.
  1.default = !EuclideanHeuristic

  2.name = ~planner_type
  2.type = string
  2.desc = Which SBPL planner to use. Choices: ARAPlanner, ADPlanner, RSTARPlanner
  2.default = ARAPlanner

  3.name = ~search_until_first_solution
  3.type = bool
  3.desc = Search until a the first (non-optimal) solution is found (True), or incrementally improve the solution if allocated_time allows (False)
  3.default = False

  4.name = ~allocated_time
  4.type = float
  4.desc = Maximum search time (anytime planning) if search_until_first_solution is set to False
  4.default = 7.0

  5.name = ~initial_epsilon
  5.type = float
  5.desc = Initial epsilon to overestimate costs (for anytime planning). 1.0= no overestimation.
  5.default = 8.0

  6.name = ~forward_search
  6.type = bool
  6.desc = Search forward (start to goal) or backwards (goal to start)
  6.default = False

  7.name = ~num_random_nodes
  7.type = int
  7.desc = Number of random node expansions for R*
  7.default = 20
  
  8.name = ~random_node_dist
  8.type = float
  8.desc = Distance (in m) at which the random nodes in R* should be placed
  8.default = 1.0

  9.name = ~heuristic_scale
  9.type = float
  9.desc = Scaling factor by which the heuristic value (e.g. euclidean distance) will be multiplied. This can make the heuristic more realistic in terms of costs, but may not overestimate them.
  9.default = 1.0

  19.name = ~step_cost
  19.type = float
  19.desc = Constant costs associated to executing one step
  19.default = 0.1

  20.name = ~diff_angle_cost
  20.type = float
  20.desc = Costs to estimate the difference between the current foot orientation and the goal foot orientation.
  20.default = 0.0

  21.name= ~footsteps/{x,y,theta}
  21.type = array of floats
  21.desc = Footstep actions as displacement vectors (see Model above). Make sure that each array of x,y,theta has the same length and contains only floats.

  22.name = ~foot/size/{x,y,z}
  22.type = float
  22.desc = Size of each foot's bounding rectangle in m. (z only used for visualization)

  23.name = ~foot/separation
  23.type = float
  23.desc = Default footstep separation (see old model above) in m. No longer used since v0.3!

  24.name = ~foot/max/step/{x,y,theta}
  24.type = float
  24.desc = The maximal allowed step has to be in the range defined by x, y, theta.

  25.name = ~foot/max/inverse/step/{x,y,theta}
  25.type = float
  25.desc = The maximal allowed backward step has to be in the range defined by x, y, theta.

  26.name = ~foot/origin_shift/{x,y}
  26.type = float
  26.desc = Translation of the foot origin from the center of the bounding rectangle in m.

  27.name = ~accuracy/collision_check
  27.type = int
  27.desc = The accuracy of the collision check performed for each step. (0: just the circumcircle of the foot, 1: just the incircle of the foot, 2: circumcircle and incircle recursivly checked for the whole foot).
  27.default = 2

  28.name = ~accuracy/cell_size
  28.type = float
  28.desc = The size of each grid cell used to discretize the robot positions in cm.
  28.default = 0.01

  29.name = ~accuracy/num_angle_bins
  29.type = int
  29.desc = The number of bins used to discretize the robot orientations.
  29.default = 128
 }
}
```

```clearsilver
node.0 {
 name = footstep_navigation_node
 desc = The navigation ROS node for the NAO robot which listens to goal callbacks to plan and execute footstep paths. This node is an extension of the footstep_planner_node, so it offers the same topics, parameters etc as above in addition.
 sub {
  1.name = amcl_pose
  1.type = geometry_msgs/PoseWithCovarianceStamped
  1.desc = Current robot pose (x, y, theta) in the map frame, e.g. from RViz.
 }

 srv_called {
  0.name = footstep_srv
  0.type = humanoid_nav_msgs/StepTargetService
  0.desc = Used to send a footstep to be executed by the NAO robot.

  1.name = clip_footstep_srv
  1.type = humanoid_nav_msgs/ClipFootstep
  1.desc = Used to clip a footstep into the executable range.
 }

 param {
  1.name = ~feedback_frequency
  1.type = float
  1.desc = Determines how often the action server should send its feedback.
  1.default = 5.0

  2.name = ~safe_execution
  2.type = bool
  2.desc = Determines whether to use the slower but more cautious footstep execution or not.
  2.default = true

  3.name = ~accuracy/footstep/{x,y,theta}
  3.type = float
  3.desc = Determines how accurate a executed footstep has to fit into a planned one.
  3.default = {x: 0.01, y: 0.01, theta: 0.1}

  30.name = ~{r,l}foot_frame_id
  30.type = string
  30.desc = tf frame ID of the right and left foot
  30.default = /{r,l}_sole
 }
}
```

```clearsilver
node.3 {
 name = footstep_planner_walls
 desc = Extended from footstep_planner_node with identical functionality. New feature is a second map topic that indicates tall obstacles such as walls to which a larger clearing needs to be maintained. Topics / parameters are the same except the ones listed below:
 sub {
  3.name = map_walls
  3.type = nav_msgs/OccupancyGrid
  3.desc = 2D Grid Map that only contains large obstacles such as walls on a second topic. 
 }
param {
  1.name = ~footstep_wall_dist
  1.type = float
  1.desc = The wall map will be inflated by this radius so that footsteps remain at a safe distance
  1.default = 0.15
}
}
```
