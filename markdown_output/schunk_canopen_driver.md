## Overview

This package provides a driver interface for the Schunk LWA4P robot arm
through the CANOPEN interface. It provides a simple interface that
accepts position commands and another interface for ros_control.

## Installation

### Dependencies

To control the arm you will need a PEAK can adapter as the driver
communicates through a pcan interface. We recommend to install the PEAK
driver from source as this works best. For example this can be done
through the fzi_icl_can package, which is a dependency for this package:
```
rosrun fzi_icl_can install_pcan_module.sh
``` Note: You will be asked for your sudo password
during execution.

You can also build the driver from source by hand, see the PEAK website
for instructions. \'\'\'IMPORTANT:\'\'\' Build the driver in
\'\'\'\'\'CHARDEV\'\'\'\'\' mode, not the default netdev mode.

Please note that the fzi_icl_can library is linked against version
7.15.2. If you decide to use a different driver version for the kernel
module, this might work, however this cannot be guaranteed.

### Building from source

You will need to checkout the following packages into your workspace:

-   <https://github.com/fzi-forschungszentrum-informatik/fzi_icl_core>
-   <https://github.com/fzi-forschungszentrum-informatik/fzi_icl_can>
-   <https://github.com/fzi-forschungszentrum-informatik/schunk_canopen_driver>

then just call ```
catkin_make_isolated
   source devel_isolated/setup.bash
   # If Peak driver was not installed before.
   # Note: You will be asked for your sudo password during execution.
   rosrun fzi_icl_can install_pcan_module.sh
```

If you have the fzi_icl_core or fzi_icl_can package in your workspace
you\'ll have to build it with \'\'catkin_make_isolated\'\', as those
packages are plain cmake packages. See the
[REP 134](http://www.ros.org/reps/rep-0134.html) for details.

### Installing via package manager

To install the package use your apt-get package manager:
```
sudo apt-get install ros-indigo-schunk-canopen-driver
  # If Peak driver was not installed before.
  # Note: You will be asked for your sudo password during execution.
  rosrun fzi_icl_can install_pcan_module.sh
```

## ROS API

### Understanding the different modes

The package offers two different interfaces, which both differ in the
action topics, parameters and the way commanded waypoints are
interpreted by the hardware.

The simpler \'\'profile_position\'\'-interface accepts series of
waypoints which the robot will drive to with internal interpolation. It
is not guaranteed (and might almost never happen), that all joints
finish moving at the same time. If multiple waypoints are given, a new
waypoint is started for all joints at the same time as soon as the last
joint reached it\'s previous destination. Ramping up and down between
waypoints is done by the robot internally depending on it\'s
configuration. The ramping setup will be treated later on.

The \'\'ros_control\'\'-interface provides a position controller in
joint space which will interpolate between waypoints inside the
controller (on the host PC). You can set joint velocities and time
constraints for each waypoint which the controller will take care of.

```clearsilver

name = schunk_canopen_driver_node
desc = Handles controlling of a Schunk robot.
pub {
  0.name = joint_states
  0.type = sensor_msgs/JointState
  0.desc = Current positions of all joints. 
  1.name = joint_currents
  1.type = std_msgs/Int16MultiArray
  1.desc = Torque generating currents in all joints in mA.
}
srv {
  0.name = close_brakes
  0.type = std_srvs/TriggerRequest
  0.desc = Close the brakes on all nodes. Use this when the device is standing still for a longer time to reduce high motor currents for doing nothing. Remember to call the enable_nodes service when you want to go on. 
  1.name = enable_nodes
  1.type = std_srvs/TriggerRequest
  1.desc = Enables the devices after a fault, a quick stop or simply when the brakes have been closed by hand (via the ''close_brakes'' service call)
  2.name = quick_stop_nodes
  2.type = std_srvs/TriggerRequest
  2.desc = Performs a quick stop on all nodes. You should prefer this service to aborting the followJointTrajectory action, as this will instantaniously stop the robot's movement without resulting in a fault state.
  3.name = home_reset_offset_by_id
  3.type = schunk_canopen_driver/HomeWithIDs
  3.desc = Perform a reset offset for a given list of nodes. You should call service, after driving the device to it's zero position manually. Only the nodes given in the node list are affected by this service call. The position of all unlisted joints is irrelevant. In this service call the canopen IDs (e.g. 3 are used.)
  4.name = home_reset_offset_by_name
  4.type = schunk_canopen_driver/HomeWithJointNames
  4.desc = Perform a reset offset for a given list of nodes. You should call this service, after driving the device to it's zero position manually. Only the nodes given in the node list are affected by this service call. The position of all unlisted joints is irrelevant. In this service the joint names from the urdf (e.g. 'arm_1_joint') are used.
  5.name = home_reset_offset_all
  5.type = schunk_canopen_driver/HomeAll
  5.desc = Perform a reset offset for all nodes. You should call this service only after driving all devices to their zero position manually.
  6.name = init_devices
  6.type = std_srvs/TriggerRequest
  6.desc = Triggers initialization of the canopen devices. This service will only be advertised when the ''autostart'' parameter is set to false. Otherwise initialization will be triggered automatically at startup.
}
goal {
  0.name = follow_joint_trajectory/follow_joint_trajectory
  0.type = control_msgs/FollowJointTrajectoryActionGoal
  0.desc = Command the robot arm with a trajectory. For this action server the robot will take care of controlling the joint values.
  1.name = pos_based_pos_traj_controller/follow_joint_trajectory
  1.type = control_msgs/FollowJointTrajectoryActionGoal
  1.desc = Command the robot arm with a trajectory. For this action server the robot will be controlled using a position controller from ros_control. The hardware will operate in the ''interpolated-position''-mode. The namespace of this controller can be set using the ''traj_controller_name''-parameter.
}
param {
  0.name = autostart
  0.type = bool
  0.desc = If set to ''true'' this will trigger device initialization automatically. Otherwise the ''init_devices'' service is created for device initialization.
  1.name = can_device_name
  1.type = string
  1.desc = Name of the tty-Device the PEAK CAN device is registered to. If you use a pcanusb device, you might want to use the keyword ''auto'' which will search for a working pcanusb device. This is the default behaviour.
  2.name = frequency
  2.type = int
  2.desc = Frequency of the state publisher. The joint values and currents are published with this rate. This frequency has no influence on the control frequency.
  3.name = traj_controller_name
  3.type = string
  3.desc = The namespace where the controller action server will be registered to. Note, that this only has an effect on the ros_control action server.
  4.name = use_ros_control
  4.type = bool
  4.desc = If set to true the robot will work in the ''interpolated-position''-mode. It will be controlled by a position-based controller from ros-control. If set to false, the robot will work in the ''profile-position''-mode, where position commands will be simply forwarded to the arm and the hardware itself takes care about the movement towards the given configuration. Note that synchronous movement of all joints can't be achieved using this mode.
}
```

## Usage

### Example launchfiles

#### standalone_profile_position

This launchfile gives a ready-to-use action interface to simply access
position configurations. It also loads a urdf description of the arm and
starts a robot state publisher. Parameters:

. pcan_device: Device name of the can adapter. Defaults to \"auto\".

#### standalone_interpolated_position

This launchfile gives a ready-to-use action interface for ros_control.
It loads controllers defined in \'\'config/arm_controllers.yaml\'\'
(This can be changed in the ros_control.launch file). Parameters:

. pcan_device: Device name of the can adapter. Defaults to
/dev/pcanusb1. controller_name::Name of a loaded controller that should
be used (when using ros_control). Defaults to
\'\'pos_based_pos_traj_controller\'\'

#### move_to_home_position.launch

This moves the robot to it\'s zero position using the profile_position
mode. Parameters:

. pcan_device: Device name of the can adapter. Defaults to \"auto\".

## Advanced usage

### Defining custom canopen IDs

If your robot arm does use custom canopen IDs, you can modify those in
the \'\'config/example_config\'\' file. When modifying the canopen IDs
you will also have to modify the node mapping in
\'\'config/node_mapping.yaml\'\' which will perform the mapping between
the canopen IDs and the URDF joint names. See the example config file
for a syntax explanation.

In Principal you can configure multiple canopen chains, for example an
arm and a gripper. The example configuration file already contains such
a setup, however this is untested and might not work.

### Setting up Profile Position ramps

When using the simple profile position mode Ramping up and down is
controlled by the hardware. The velocity and acceleration can be
configured in the \'\'config/example_config.yaml\'\'file. Also, targets
can be commanded as a relative motion to the current position or as an
absolute position relative to the home position (which is the default).
Change the \'\'ppm_use_relative_targets\'\' parameter if you like to
change this behavior.

## Troubleshooting

### Fault after canceling a goal

Canceling a goal at high speeds seems to set the robot into a fault
state. This comes from within the used position controller as it
commands the robot to hold a position which is too far away to be
reached within one control cycle. As a workaround prefer the
\'\'quick_stop_nodes\'\' service

### Fault after starting ros_control mode

Sometimes the robot gets into a fault mode after enabling the
interpolated position mode (ros_control mode) when the arm is at a
non-zero position. This should not happen with a recent version of
ros_control, but if it happens, move the robot to it\'s zero position
using the move_to_home_position.launch launchfile.
