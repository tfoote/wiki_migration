This package extends JRL Dynamics to load URDF models.

[jrl-dynamics](http://jrl-umi3218.github.com/jrl-dynamics/doxygen/HEAD/index.html)
is an open source library dedicated to dynamics and kinematics
computation for robotics and in particular humanoids robots. It relies
on
[abstract-robot-dynamics](http://laas.github.com/abstract-robot-dynamics/doxygen/HEAD/)
packages defining the C++ interface.

See [sot_pr2](sot_pr2) to learn how to use the PR-2 URDF model with the
dynamic-graph and stack of tasks control framework.

## jrl-dynamics models specificities

The loader automatically adds a free floating joint as the root joint of
the kinematic tree in order to link the world frame origin to the robot
root body (i.e. `base_link`).

`jrl-dynamics` also requires additional data to define foot and hand
parameters. These information are not setted currently.

## Displaying robots structure in a console

Three robots are supported currently. Make sure that the required
packages are available on your system as the packages does not directly
depend on them:

-   PR-2 (requires [pr2_mechanism_model](pr2_mechanism_model)),
-   Nao (requires [nao_description](nao_description)),
-   Romeo (requires [romeo_description](romeo_description)),
-   HRP-2 (requires [hrp2_14_description](laas-ros-pkg)).

They can be respectively loaded using: 

```
rosrun jrl_dynamics_urdf display-pr2
rosrun jrl_dynamics_urdf display-nao
rosrun jrl_dynamics_urdf display-hrp2
rosrun jrl_dynamics_urdf display-romeo
```


