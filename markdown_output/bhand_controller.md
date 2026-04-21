## Overview

This controller for the Barrett Hand is a python node based on the
original library pyHand. By using this controller it will be able to set
the position or velocity of the motorized joints of the hand and read
from all of its sensors (fingertip torque and tactile sensors,
temperature) and joint positions.

## Configuration

### launch file

```
<?xml version="1.0"?>
<launch>
 
  <node pkg="bhand_controller" type="bhand_node.py" name="bhand_node" output="screen">
      <rosparam command="load" file="$(find bhand_controller)/config/bhand.yaml" />
      <param name="topic_state" value="state" />
      <param name="port" value="/dev/pcanusb0" />
      <param name="tactile_sensors" value="True" />
  </node>
 
</launch>
```

-   topic_state: Name of the topic to publish the state.
-   port: can device connected to the hand.
-   tactile_sensors: Flag to set if the tactile sensors are available
    and want to be published.

### config file

```
# Joint ids (don't modify) 
joint_ids: [ F1, F1_TIP, F2, F2_TIP, F3, F3_TIP, SPREAD_1, SPREAD_2]
# Joint names associated with the ids
joint_names: [bh_j12_joint, bh_j13_joint, bh_j22_joint, bh_j23_joint, bh_j32_joint, bh_j33_joint, bh_j11_joint, bh_j21_joint]
# Default control mode
control_mode: POSITION
# Desired freq
desired_freq: 250.0
```

-   joint_ids: ID associated with every joint
-   joint_names: Joint names associated with every joint id
-   control_mode: Default hand control mode
-   desired_freq: Desired frequency of the controller's control loop. A
    frequency higher than 300 Hz is not recommendable for now.

![BHand Joints\|width=650](attachment:bhand_joints.png)

## Topics

### Published

#### state

-   General state of the hand.
-   Type:
    [ bhand_controller/State.msg](http://docs.ros.org/hydro/api/bhand_controller/html/msg/State.html)
-   Example:

```
state: 300
control_mode: VELOCITY
hand_initialized: True
desired_freq: 250.0
real_freq: 246.000228882
state_description: READY_STATE
temp_f1: [37.0, 58.0]
temp_f2: [36.0, 60.0]
temp_f3: [35.0, 54.0]
temp_spread: [30.0, 62.0]
```

#### tact_array

-   Values from BHand tactile array
-   Unit: N/cm2
-   Type:
    [ bhand_controller/TactileArray.msg](http://docs.ros.org/hydro/api/bhand_controller/html/msg/TactileArray.html)
-   Example:

```
header: 
  seq: 15277
  stamp: 
    secs: 1408685936
    nsecs: 928946018
  frame_id: ''
finger1: [0.09000000357627869, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.019999999552965164, 0.009999999776482582, 0.0, 0.009999999776482582, 0.0, 0.0, 0.019999999552965164, 0.0, 0.03999999910593033, 0.0]
finger2: [0.0, 0.019999999552965164, 0.0, 0.03999999910593033, 0.029999999329447746, 0.029999999329447746, 0.019999999552965164, 0.019999999552965164, 0.029999999329447746, 0.019999999552965164, 0.019999999552965164, 0.019999999552965164, 0.029999999329447746, 0.029999999329447746, 0.07000000029802322, 0.09000000357627869, 0.0, 0.09000000357627869, 0.009999999776482582, 0.019999999552965164, 0.05999999865889549, 0.009999999776482582, 0.0, 0.03999999910593033]
finger3: [0.0, 0.0, 0.0, 0.0, 0.019999999552965164, 0.029999999329447746, 0.0, 0.0, 0.019999999552965164, 0.0, 0.009999999776482582, 0.029999999329447746, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.019999999552965164, 0.0, 0.0, 0.0]
palm: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```

#### joint_states

-   Joint states of the hand.
-   Type:
    [ sensor_msgs/JointState.msg](http://docs.ros.org/indigo/api/sensor_msgs/html/msg/JointState.html)
-   Fingertip torque sensors are published in *effort* field (N/m)
-   Example:

```
header: 
  seq: 4912
  stamp: 
    secs: 1408685894
    nsecs: 728996992
  frame_id: ''
name: ['bh_j23_joint', 'bh_j12_joint', 'bh_j22_joint', 'bh_j32_joint', 'bh_j33_joint', 'bh_j13_joint', 'bh_j11_joint', 'bh_j21_joint']
position: [0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0, 0.0]
velocity: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
effort: [0.03743090386539949, 0.06140198104320094, 0.03743090386539949, 0.06676343437499943, 0.06676343437499943, 0.06140198104320094, 0.0, 0.0]
```

![BHand Sensors\|width=650](attachment:bhand_sensors.png)

### Subscribed

#### command

-   Sets the position/velocity of the hand joints.
-   Joints available to set positions/velocities:
-   *bh_j32_joint* -> F3-Base
-   *bh_j11_joint* -> F1-Spread
-   *bh_j12_joint* -> F1-Base
-   *bh_j21_joint* -> F2-Spread
-   *bh_j22_joint* -> F2-Base
-   bh_j11_joint and bh_j21_joint set the same motor (able publishing on
    both)

```{=html}
<!-- -->
```
-   Type:
    [ sensor_msgs/JointState.msg](http://docs.ros.org/indigo/api/sensor_msgs/html/msg/JointState.html)
-   Example:

```
$ rostopic pub /bhand_node/command sensor_msgs/JointState "header:
  seq: 0
  stamp: {secs: 0, nsecs: 0}
  frame_id: ''
name: ['bh_j11_joint', 'bh_j32_joint', 'bh_j12_joint', 'bh_j22_joint']
position: [0 , 0, 0, 0]
velocity: [0]
effort: [0]"
```

## Services

### Server

#### actions

-   Performs specific actions and movements (see
    [bhand_controller/Service.msg](http://docs.ros.org/hydro/api/bhand_controller/html/msg/Service.html))
-   Type:
    [ bhand_controller/Actions.srv](http://docs.ros.org/hydro/api/bhand_controller/html/srv/Actions.html)
-   Example:

```
$ rosservice call /bhand_node/actions "action: 1"  (Inits the hand)
```

#### set_control_mode

-   Sets the control mode in position or velocity
-   Type:
    [ bhand_controller/SetControlMode.srv](http://docs.ros.org/hydro/api/bhand_controller/html/srv/SetControlMode.html)
-   Example:

```
$ rosservice call /bhand_node/set_control_mode "mode: 'VELOCITY'"
```
