## About

The `carl_safety` package contains various nodes for ensuring the safe
operation of the [CARL robot](carl_bot) for both local and remote users.
This includes safety features for arm control, autonomous navigation,
manual navigation teleoperation, and tipping detection.

## Nodes

```clearsilver
node.0 {
  name = arm_safety
  desc = Provides terminal and audible warnings for when any of the arm's joints exceed a dangerous current threshold.
  sub {
    0.name = jaco_arm/joint_states
    0.type = sensor_msgs/JointState
    0.desc = Joint state updates for the arm.
  }
  param {
    0.name = enable_audible_warnings
    0.type = bool
    0.desc = Option for allowing CARL to produce audible warnings for arm joint over-current.
    0.default = false
  }
}
node.1 {
  name = nav_safety
  desc = Safety overrides for manual and autonomous navigation, by providing an extra layer to filter move_base and `cmd_vel` commands from a remote source, preventing them if the arm is in an unsafe position or allowing an operator to temporarily disable these inputs completely.
  pub {
    0.name = cmd_vel
    0.type = geometry_msgs/Twist
    0.desc = Manual base navigation commands.
  }
  pub {
    1.name = cmd_vel_safety_check
    1.type = geometry_msgs/Twist
    1.desc = Manual base navigation commands with safety check preventing the robot from driving into obstacles on the map.  This will replace the `cmd_vel` publisher if the `use_teleop_safety` parameter is set to true.
  }
  sub {
    0.name = cmd_vel_safe
    0.type = geometry_msgs/Twist
    0.desc = An extra layer for `cmd_vel` commands that can be disabled or enabled for safety reasons; this node will pass commands either directly to `cmd_vel` or through the `cmd_vel_safety_check` depending on the `use_teleop_safety` parameter.
  }
  sub {
    1.name = joy
    1.type = sensor_msgs/Joy
    1.desc = joystick input, used for reading in commands to disable or enable all navigation commands.
  }
  sub {
    2.name = robot_pose
    2.type = geometry_msgs/Pose
    2.desc = Robot pose subscriber.
  }
  srv_called {
    0.name = jaco_arm/get_angular_position
    0.type = wpi_jaco_msgs/GetAngularPosition
    0.desc = Read the angular position of the arm.
  }
  srv_called {
    1.name = jaco_arm/get_cartesian_position
    1.type = wpi_jaco_msgs/GetCartesianPosition
    1.desc = Read the Cartesian position of the arm.
  }
  srv {
    0.name = carl_safety/stop_base_nav
    0.type = std_srvs/Empty
    0.desc = Stop all autonomous and manual base navigation.
  }
  goal {
    0.name = move_base_safe
    0.type = move_base_msgs/MoveBaseAction
    0.desc = Safe version of the `move_base` action server which will not allow the command to be passed on to the `move_base` action server if the arm is in an unsafe position.
  }
  act_called {
    0.name = move_base
    0.type = move_base_msgs/MoveBaseGoal
    0.desc = Call to the move base action server.
  }
  param {
    0.name = controller_type
    0.type = string
    0.desc = Type of controller used, either "analog" or "digital".
    0.default = digital
  }
  param {
    1.name = use_teleop_safety
    1.type = bool
    1.desc = Option to pass teleop commands through the `teleop_safety` node.
    1.default = false
  }
}
node.2 {
  name = teleop_safety
  desc = Base teleoperation safety layer that prevents the robot from driving into obstacles seen from the navigation map.
  sub {
    0.name = cmd_vel_safety_check
    0.type = geometry_msgs/Twist
    0.desc = Incoming `cmd_vel` commands to be checked for safety.
  }
  sub {
    1.name = scan
    1.type = sensor_msgs/LaserScan
    1.desc = Incoming laser scan data.
  }
  sub {
    2.name = map
    2.type = nav_msgs/OccupancyGrid
    2.desc = Navigation map.
  }
  sub {
    3.name = amcl_pose
    3.type = geometry_msgs/PoseWithCovarianceStamped
    3.desc = Robot pose on navigation map.
  }
  pub {
    0.name = cmd_vel
    0.type = geometry_msgs/Twist
    0.desc = Base movement commands.
  }
}
node.3 {
  name = tipping_safety
  desc = Base tipping detection and prevention through emergency stop.
  sub {
    0.name = frame_joint_states
    0.type = sensor_msgs/JointState
    0.desc = Filtered orientation of the base relative to the ground, calculated from IMU data.
  }
  srv_called {
    0.name = jaco_arm/software_estop
    0.type = wpi_jaco_msgs/EStop
    0.desc = Arm software emergency stop.
  }
  srv_called {
    1.name = carl_safety/stop_base_nav
    1.type = std_srvs/Empty
    1.desc = Base manual and autonomous navigation emergency stop.  Note that this will only stop manual navigation commands that are sent through the `nav_safety` node.
  }
  param {
    0.name = enable_audible_warnings
    0.type = string
    0.desc = Allow CARL to give an audible warning when tipping is detected.
    0.default = false
  }
}
```

## Operation

When using the `nav_safety` node, a controller is required to input
stop and restart commands. With a controller connected, pressing the
back button will cut off all manual base teleoperation commands going
through the safety node, and all autonomous navigation commands will be
canceled. Both manual and autonomous base navigation commands can then
be re-enabled by pressing the start button.

## Installation

To install the `carl_safety` package, you can install from source with
the following commands: . ```shell
cd /(your catkin workspace)/src
git clone https://github.com/WPI-RAIL/carl_safety.git
cd ..
catkin_make
catkin_make install
```

## Startup

The `carl_safety` package contains safety nodes that are categorized
into two groups: basic safety functionality that should always be
active, and remote interface safety that only affects users who are not
copresent with the robot. As such, the package contains two launch
files: . ```
roslaunch carl_safety carl_safety_basic.launch
``` . ```
roslaunch carl_safety carl_safety_interface.launch
```
