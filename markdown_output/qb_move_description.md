This package contains the description resources for the *qbrobotics®
qbmove* device. It includes the [urdf](urdf)/[xacro](xacro) model of the
cube with its simplified meshes and its configuration setup.

## Launch files

The single launch file in this package is a simple test to verify that
everything is well configured.

### qb_move

This launch file calls the template
[description_bringup](qb_device_bringup#description_bringup) with the
default settings to visualize a *qbmove* in [rviz](rviz) (and nothing
more). ```
roslaunch qb_move_description qb_move.launch
``` ```wiki
If it does not bringup an [[rviz]] node with the ''qbmove'' loaded inside, something is not working as expected and we recommend to check your configuration (cf. [[Robots/qbmove]]).
```
