[hebiros:](hebiros) [hebiros_description](hebiros_description) \|
[hebiros_basic_examples](hebiros_basic_examples) \|
**hebiros_advanced_examples**

# Setup

The physical setup for the rviz, Gazebo, and MoveIt! examples is a
3-dof-arm, the same one used in
[hebiros_basic_examples](hebiros_basic_examples). In addition, these
examples are constructed using a [urdf](urdf), a description of the
robot containing the meshes, dimensions, inertial properties, Gazebo
controllers, etc. For more details, see
[hebiros_description](hebiros_description).

\

The Mobile Robot example uses two modules arranged in a differential
drive configuration. The hardware is discussed more in detail in its
respective section.

\

# Examples

## rviz

This example demonstrates using [rviz](rviz) in order to visualize a
physical robot in real-time.

```
roslaunch hebiros_advanced_examples x_demo_rviz.launch
```\

You should see rviz open. First, add a new display and select
\`RobotModel\`.

![](attachment:rviz_displays.png)

\

Next, type \`robot_description\` as the parameter for the Robot
Description. This parameter should contain the URDF of the robot. You
should be able to see the model move as in the following video when you
move the physical robot.
[Youtube](https://www.youtube.com/watch?v=hu11NaS-CPg)

\

## Gazebo

This example demonstrates using [gazebo](gazebo) in order to simulate
the 3-dof-arm robot. The actual controller is the same as in Example 3
of [hebiros_basic_examples](hebiros_basic_examples), the virtual spring.
The difference is that the group is constructed using
\`/hebiros/add_group_from_urdf\`, thus the *same* program can be used
either in simulation via Gazebo or on the hardware.

First, launch the setup file. This will load the urdf to
\`robot_parameter\`, open Gazebo and start the \`hebiros_node\` and
example node.

```
roslaunch hebiros_advanced_examples x_demo_gazebo_setup.launch
``` Next, launch the start file. This will start
the [controller_manager](controller_manager),
[robot_state_publisher](robot_state_publisher), and spawn the model.

```
roslaunch hebiros_advanced_examples x_demo_gazebo_start.launch
```\

You should see the robot simulated in Gazebo as in the following video.
[Youtube](https://www.youtube.com/watch?v=C147k-d7fbM)

\

You can also use the same node to run the example on the hardware.
```
roslaunch hebiros_advanced_examples x_demo_gazebo_hardware.launch
```

\

## MoveIt!

This example demonstrates using [moveit](moveit) in order to visualize
trajectory planning of the 3-dof-arm robot. You can also use this to
command the physical robot.

The launch file assumes that you have a package named \`x_demo\`. In
order to create the package, follow MoveIt!\'s
[setup assistant tutorial](http://docs.ros.org/kinetic/api/moveit_tutorials/html/doc/setup_assistant/setup_assistant_tutorial.html).
This will take you through selecting a URDF, assigning joints, assigning
labeled positions, and more. There is also an example generated package
called \`x_demo\` in the \`hebiros_advanced_examples\` source files. To
use it, place the folder in your catkin workspace.

Launch the visualization file in order to visualize planning and
executing paths to different positions ```
roslaunch hebiros_advanced_examples x_demo_moveit_visualization.launch
```

\

With labeled positions, you can control the visualization as in the
following video.

[Youtube](https://www.youtube.com/watch?v=9e2CDlnnbV8)

\

You can also try using the visualization interface to execute
trajectories on the physical robot. ```
roslaunch hebiros_advanced_examples x_demo_moveit_control.launch
```

\

## Mobile Robot

This example demonstrates using [move_base](move_base),
[rtabmap_ros](rtabmap_ros), and an Intel RealSense camera in order to
create a mobile robot which performs SLAM and is able to navigate using
visual odometry.

\

## OmniBase
