## Hardware Requirements

This package configures the [cob_powercube_chain](cob_powercube_chain)
to use one powercube for the Care-O-bot tray. Alternatively you can use
a simulated version without any hardware, see [cob_gazebo](cob_gazebo).

## ROS API

This package doesn't have a own ROS API, it just configures the
[cob_powercube_chain](cob_powercube_chain) with 1 DOF.

## Usage/Examples

For starting only the tray use 

```
roslaunch cob_tray solo.launch
```

 For including
the tray in your overall launch file use 

```
<include file="$(find cob_tray)/ros/launch/tray.launch" />
```

 A
sample parameter file could look like this 

```
can_module: PCAN
can_device: /dev/pcan0
can_baudrate: 500
module_ids: [10]
joint_names: [torso_tray_joint]
max_accelerations: [0.8]
OperationMode: position
```

 For
moving the tray start the [cob_dashboard](cob_dashboard)


```
roslaunch cob_dashboard dashboard.launch
```

 Press the "init" button to call the init
service for connecting to the hardware. Afterwards use the buttons to
move to predefined positions.
