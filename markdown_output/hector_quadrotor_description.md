## Overview

This package provides a URDF model of a generic quadrotor UAV. The
visual geometry is provided as a COLLADA model and the collision
geometry is provided as a STL mesh. The extensions/additions that allow
the use of the model in gazebo simulation can be found in the
[hector_quadrotor_gazebo](hector_quadrotor_gazebo) package.

## Available Models

Currently, the following models are available:

-   [quadrotor_base.urdf.xacro](https://github.com/tu-darmstadt-ros-pkg/hector_quadrotor/blob/HEAD/hector_quadrotor_description/urdf/quadrotor_base.urdf.xacro)
    is the xacro macro for generating an instance of the quadrotor base
    (e.g. meshes, inertia etc.)
-   [quadrotor.urdf.xacro](https://github.com/tu-darmstadt-ros-pkg/hector_quadrotor/blob/HEAD/hector_quadrotor_description/urdf/quadrotor.urdf.xacro)
    provides a plain instance of the quadrotor base without additionally
    mounted sensors. This can be used for the \'robot_description\'
    parameter.
-   [quadrotor_hokuyo_utm30lx.urdf.xacro](https://github.com/tu-darmstadt-ros-pkg/hector_quadrotor/blob/HEAD/hector_quadrotor_description/urdf/quadrotor_hokuyo_utm30lx.urdf.xacro)
    provides a instance of the quadrotor base with additional sensors, a
    Hokuyo UTM-30LX LIDAR as well as a forward facing camera. This can
    be used for the \'robot_description\' parameter.

This is a Blender render of the COLLADA quadrotor model:

![\|width=720](attachment:hector_quadrotor_render.png)
