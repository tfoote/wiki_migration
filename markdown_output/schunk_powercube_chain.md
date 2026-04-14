## Hardware Requirements

To use this package you need one or more powercubes
[www.schunk-modular-robotics.com](http://www.schunk-modular-robotics.com).
Alternatively you can use a simulated version without any hardware, see
[schunk_bringup_sim](schunk_bringup_sim).

## Software Requirements

The installation is tested for Ubuntu 14.04 using ROS [indigo](indigo).
If you discover problems installing them on other platforms, please
[tell us](http://www.care-o-bot-research.org/contributing/mailing-lists).

## ROS API

The [schunk_powercube_chain](schunk_powercube_chain) package provides a
configurable node for operating a chain of powercube modules.
```clearsilver
 name = schunk_powercube_chain
 desc = The `schunk_powercube_chain` node takes in <<MsgLink(brics_actuator/JointVelocities)>> messages and sends this directly to the hardware. The chain can be initialized, stopped or recovered via [[Services|services]].

sub{
 0.name = joint_group_velocity_controller/command
 0.type = std_msgs/Float64MultiArray
 0.desc = Receives velocity commands.
 1.name = joint_group_position_controller/command
 1.type = std_msgs/Float64MultiArray
 1.desc = Receives position commands (Not implemented yet).
}

pub{
  0.name = /joint_states
  0.type = sensor_msgs/JointState
  0.desc = Joint state information for all modules in chain.
  1.name = joint_trajectory_controller/state
  1.type = control_msgs/JointTrajectoryControllerState
  1.desc = Controller state information for all modules in chain.
  2.name = driver/current_operationmode
  2.type = std_msgs/String
  2.desc = Current operation mode for chain.
  3.name = /diagnostics
  3.type = diagnostic_msgs/DiagnosticArray
  3.desc = Diagnostics information about chain.
}

srv{
 0.name = driver/init
 0.type = std_srvs/Trigger
 0.desc = Initializes the node and connects to the hardware.
 1.name = driver/stop
 1.type = std_srvs/Trigger
 1.desc = Stops immediately all hardware movements.
 2.name = driver/recover
 2.type = std_srvs/Trigger
 2.desc = Recovers the hardware after an emergency stop.
 3.name = driver/set_operation_mode
 3.type = cob_srvs/SetString
 3.desc = Sets the operation mode for the node. Currently only "velocity" mode implemented.
}

param{
 0.name = can_module
 0.type = string
 0.default = Required
 0.desc = Can module specifier, e.g. PCAN, ESD
 1.name = can_device
 1.type = string
 1.default = Required
 1.desc = Device address of can module, e.g. /dev/can0, /dev/pcan2,...
 2.name = can_baudrate
 2.type = int
 2.default = Required
 2.desc = Baudrate of can module, e.g. 1000, 500,...
 3.name = module_ids
 3.type = list of ints
 3.default = Required
 3.desc = Modul IDs of the powercubes, e.g. [10,11,12,13,...]
 4.name = force_use_movevel
 4.type = bool
 4.default = false
 4.desc = Forces using the M5API moveVel command instead of moveStep.
 5.name = joint_names
 5.type = list of strings
 5.default = Required
 5.desc = List of joint names corresponding to urdf description, e.g. [arm_1_joint, arm_2_joint, arm_3_joint,...]
 6.name = max_accelerations
 6.type = list of doubles
 6.default = Required
 6.desc = List of maximal accelerations for the modules in rad/sec^2, e.g. [0.8,0.8,0.8,...]
 7.name = horizon
 7.type = double
 7.default = 0.05
 7.desc = Horizon in seconds for commanding moveStep. E.g. 0.1 commands a step size of 0.1 seconds into the future.
 8.name = frequency
 8.type = double
 8.default = 10 Hz
 8.desc = Controller frequency.
 9.name = min_publish_duration
 9.type = double
 9.default = Required
 9.desc = Minimum duration of publishing joint states if no command is received, otherwise for each received command one joint state message is published.
 10.name = /robot_description
 10.type = urdf model
 10.default = Required
 10.desc = Urdf model of the robot, including the joints and links describing the chain of powercubes
}

req_tf{
}

prov_tf{
}
```

## Usage/Examples

This package is not intended to be used directly, but with the
corresponding launch and yaml files from e.g.
[schunk_bringup](schunk_bringup) in the [schunk_robots](schunk_robots)
stack. For starting only the lwa use ```
roslaunch schunk_bringup lwa_solo.launch
``` For
including the lwa in your overall launch file use
```
<include file="$(find schunk_bringup)/components/lwa.launch" />
``` All hardware configuration is done in the
[schunk_hardware_config](schunk_hardware_config) package. A sample
parameter file in \"schunk_hardware_config/lwa/config/lwa.yaml\" could
look like this ```
can_module: PCAN
can_device: /dev/pcan1
can_baudrate: 1000
modul_ids: [1,2,3,4,5,6,7]
joint_names: [arm_1_joint, arm_2_joint, arm_3_joint, arm_4_joint, arm_5_joint, arm_6_joint, arm_7_joint]
max_accelerations: [0.8,0.8,0.8,0.8,0.8,0.8,0.8]
frequency: 68
OperationMode: position
ptp_vel: 0.4 # rad/sec
ptp_acc: 0.1 # rad/sec^2
max_error: 0.2 # rad
```
