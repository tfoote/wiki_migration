\'\'\'For [hydro](hydro) onward, see [orocos_kdl](orocos_kdl).\'\'\'

![\|height=\"413px\",width=\"224px\"](attachment:chain.png)

## What can I use KDL for?

-   \'\'\'3D frame and vector transformations: \'\'\'KDL includes
    excellent support to work with vectors, points, frame
    transformations, etc. You can calculate a vector product, transform
    a point into a different reference frame, or even change the
    reference point of a 6d twist. For more information take a look at
    the [geometry documentation](http://www.orocos.org/kdl/geometry) on
    the KDL homepage.
-   \'\'\'Kinematics and Dynamics of kinematic chains:\'\'\' You can
    represent a kinematic chain by a KDL Chain object, and use KDL
    solvers to compute anything from forward position kinematics, to
    inverse dynamics. For more information take a look at the
    [chain documentation](http://orocos.org/node/833) on the KDL
    homepage.The [kdl_parser](kdl_parser) includes support to construct
    a KDL chain from a XML Robot Description Format [(URDF)](urdf/XML)
    file.
-   \'\'\'Kinematics of kinematic trees: \'\'\'You can represent a
    kinematic chain by a KDL Chain object, and use KDL solvers to
    compute forward position kinematics. Currently no other solvers are
    provided.

## KDL examples

See the [examples page](http://orocos.org/kdl/examples)

## Building KDL

First install the external dependencies such as sip4, python, etc.

```
$ rosdep install kdl
``` Now build KDL

```
$ rosmake kdl
``` The \"rosmake\" command checks out code from
the KDL svn repository (see [kul-ros-pkg](kul-ros-pkg)).

## External Documentation

KDL is a 3rd party library that is part of the Orocos project
[KDL homepage](http://www.orocos.org/kdl).
