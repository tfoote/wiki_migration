This package contains the description resources for the \'\'qb SoftHand
Research\'\' and \'\'qb SoftHand2 Research\'\' devices. It includes the
[urdf](urdf)/[xacro](xacro) model of the hands with their simplified
meshes and their configuration setup.

## Launch files

The single launch file in this package is a simple test to verify that
everything is well configured.

### qb_hand

This launch file calls the template
[description_bringup](qb_device_bringup#description_bringup) with the
default settings to visualize the desired qb SoftHand Research in
[rviz](rviz) (and nothing more). ```
roslaunch qb_hand_description qb_hand.launch
```
```wiki
If it does not bringup an [[rviz]] node with the ''qbhand'' loaded inside, something is not working as expected and we recommend to check your configuration (cf. [[Robots/qbhand]]).
```
