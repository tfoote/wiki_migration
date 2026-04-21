This is the ROS interface to the OMPL motion planning package. This
package will allow you to easily create and configure a motion planner
for your robot. Most configuration is automated, however you will have
to specify the parts of the robot for which you want to create a motion
planner. You can also define the planner in a "task" space by defining
your own instance of a state transformation function that will convert
back and forth between the task and configuration space of the robot.

## Ompl Ros Interface

### Installation

#### ROS Electric

To install this package, you will have to install the *arm_navigation*
stack:

` sudo apt-get install ros-electric-arm-navigation`

### Documentation and Tutorials

Examples for how to setup and configure motion planners for your robot
can be found in the accompanying
[tutorials](ompl_ros_interface/Tutorials).

### Videos

Coming soon.

### Example (In simulation)

A quick example for use with the PR2 robot in simulation (Gazebo) can be
found in the
[PR2 pick and place demo](http://www.ros.org/wiki/pr2_simulator/Tutorials/SimpleGraspingDemo)
in Gazebo. Follow the instructions on that page to see
ompl_ros_interface in action.

### Example (On the PR2 Robot)

The tabletop manipulation stacks in diamondback now use the
ompl_ros_interface for planning using OMPL. To run these stacks on the
PR2 robot, try the tabletop manipulation demo
[following these instructions](http://www.ros.org/wiki/pr2_pick_and_place_demos/Tutorials/The%20Pick%20and%20Place%20Autonomous%20Demo).
