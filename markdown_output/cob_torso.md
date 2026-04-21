## Hardware Requirements

This package configures the [cob_powercube_chain](cob_powercube_chain)
to use two pan tilt units for the Care-O-bot torso. Alternatively you
can use a simulated version without any hardware, see
[cob_gazebo](cob_gazebo).

## ROS API

This package doesn't have a own ROS API, it just configures the
[cob_powercube_chain](cob_powercube_chain) with 4 DOF.

## Usage/Examples

For starting only the torso use 

```
roslaunch cob_torso solo.launch
```

 For including
the torso in your overall launch file use 

```
<include file="$(find cob_torso)/ros/launch/torso.launch" />
```

 A
sample parameter file could look like this 

```
can_module: PCAN
can_device: /dev/pcan0
can_baudrate: 500
module_ids: [14,13,16,15]
joint_names: [torso_lower_neck_pan_joint, torso_lower_neck_tilt_joint, torso_upper_neck_pan_joint, torso_upper_neck_tilt_joint]
max_accelerations: [0.8,0.8,0.8,0.8]
OperationMode: position
```

 For
moving the torso start the [cob_dashboard](cob_dashboard)


```
roslaunch cob_dashboard dashboard.launch
```

 Press the "init" button to call the init
service for connecting to the hardware. Afterwards use the buttons to
move to predefined positions.
