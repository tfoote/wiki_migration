## Hardware Requirements

This package configures the [cob_powercube_chain](cob_powercube_chain)
to use seven powercubes for the Care-O-bot arm. Alternatively you can
use a simulated version without any hardware, see
[cob_gazebo](cob_gazebo).

## ROS API

This package doesn\'t have a own ROS API, it just configures the
[cob_powercube_chain](cob_powercube_chain) with 7 DOF.

## Usage/Examples

For starting only the arm use ```
roslaunch cob_arm solo.launch
``` For including the
arm in your overall launch file use ```
<include file="$(find cob_arm)/ros/launch/arm.launch" />
``` A sample
parameter file could look like this ```
can_module: PCAN
can_device: /dev/pcan0
can_baudrate: 1000
module_ids: [4,5,6,7,8,9,10]
joint_names: [arm_1_joint, arm_2_joint, arm_3_joint, arm_4_joint, arm_5_joint, arm_6_joint, arm_7_joint]
max_accelerations: [0.8,0.8,0.8,0.8,0.8,0.8,0.8]
OperationMode: position
``` For moving
the arm start the [cob_dashboard](cob_dashboard)
```
export ROBOT=cob3-2
roslaunch cob_dashboard dashboard.launch
``` Press the \"init\" button to call the init
service for connecting to the hardware. Afterwards use the buttons to
move to predefined positions.
