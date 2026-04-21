## Overview

A demo package for testing and demonstrating the uses of the
[sbpl_dynamic_env](sbpl_dynamic_env) stack.

### Demonstrations

There are a few launch files in the launch folder which show interesting
situations where a planner that takes dynamic obstacles and time into
account ([sbpl_dynamic_planner](sbpl_dynamic_planner)) will produce
intelligent behavior. In the same situations a planner that doesn't
handle time (treats dynamic obstacles as static ones) will produce
incorrect solutions, or no solution at all.

The demos all have the robot running the sbpl_dynamic_planner in blue
and the dynamic obstacles in green.



```
roscd demo_sbpl_dynamic_env
roslaunch launch/duck_and_wait.launch
```

 In this demo the robot's goal is on the right
and there is a dynamic obstacle moving toward it in a tight hallway. The
robot generates a plan that ducks into an alcove waits for the moving
obstacle to pass and then proceed to its goal. A planner that does not
take time into account would never find a solution to this situation.



```
roscd demo_sbpl_dynamic_env
roslaunch launch/slow_follow.launch
```

 In this demo a slow dynamic obstacle moves in
front of the robot (blocking its path to the goal). The robot follows it
(stopping and waiting often) until the tight hallway opens up into a
room where the robot can get past the moving obstacle.



```
roscd demo_sbpl_dynamic_env
roslaunch launch/two_robot_dodge.launch
```

 In this demo there are two moving obstacles
coming toward the robot. The robot must weave in between them in order
to get to the goal safely.

### Tests

There is a gtest in the test folder which makes sure all the packages in
this stack are working together properly in the [stage](stage)
simulator.
