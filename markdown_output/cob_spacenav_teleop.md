## Overview

Package contains node for teleoperating Care-O-Bot or any other
holonomic robot by [Space Navigator](spacenav) 3D mouse.

Control input from SN is recomputed to make robot teleoperation in *user
perspective*. This helps to lower mental load of an operator and leads
to very intuitive way of interaction. To enable this functionality
position of RVIZ camera must be published as TF transformation for
instance, by plugin from [srs_env_model_ui](srs_env_model_ui).

Node can publish to two Twist topics. Normally it publish to first one
(*safe* topic in case of Care-O-Bot) and when the left button is pressed
on SN, it publishes to second topic (*unsafe* in case of Care-O-Bot).
When right button is pressed once, robot control is switched to the
*robot perspective*. Next press will switch control back to default
mode.

Teleop node also offers *axis preference* which can be useful for some
robot bases. This means if user tries to command robot to move in *x*
axis direction for instance, then in some cases (depending on the
parameters) small movements in other axes can be ignored.

## ROS API

```clearsilver

sub {
  
  0.name= /spacenav/offset
  0.type= geometry_msgs/Vector3
  0.desc= Space Navigator topic.

  1.name= /spacenav/rot_offset
  1.type= geometry_msgs/Vector3
  1.desc= Space Navigator topic.

  2.name= /spacenav/joy
  2.type= sensor_msgs/Joy
  2.desc= Space Navigator topic.
  
}

pub {
  0.name= /cmd_vel_safe
  0.type=geometry_msgs/Twist
  0.desc= Commands are published to this topic by default.
  
  1.name= /cmd_vel_unsafe
  1.type=geometry_msgs/Twist
  1.desc= Commands are published to this topic while the left button is pressed.
}

srv{

  0.name= ~disable
  0.type= std_srvs/Empty
  0.desc= Disables SN teleop so, it can be used as a control for different task.

  1.name= ~enable
  1.type= std_srvs/Empty
  1.desc= Enables previously disabled SN teleop.

}

param {

  0.name=~max_vel_x
  0.default=`"0.3"`
  0.type= double
  0.desc= Maximal translational velocity in `"x"` axis.

  1.name=~max_vel_y
  1.default=`"0.2"`
  1.type= double
  1.desc= Maximal translational velocity in `"y"` axis.

  2.name=~max_vel_th
  2.default=`"0.3"`
  2.type= double
  2.desc= Maximal rotational velocity in `"z"` (theta) axis.

  3.name=~spacenav/max_val
  3.default=`"350.0"`
  3.type= double
  3.desc= Maximal value on offset/rot_offset topic.

  4.name=~spacenav/min_val_th
  4.default=`"0.05"`
  4.type= double
  4.desc= Lower values (normalized to 0-1 range) will be ignored.

  5.name=~spacenav/ignore_th_high
  5.default=`"0.9"`
  5.type= double
  5.desc= Upper threshold for axis preference. If user's ''effort' to move robot in any axis is higher than this threshold and in all other axes lower then ''ignore_th_low'', then one axis will be prefered and others ignored - setted to zero.

  6.name=~spacenav/ignore_th_low
  6.default=`"0.1"`
  6.type= double
  6.desc= Lower threshold for axis preference.

  7.name=~spacenav/instant_stop_enabled
  7.default=`"false"`
  7.type= bool
  7.desc= When enabled, robot can be stopped by pressing SN. Teleop will then publish zero velocities for few seconds.

  8.name=~use_rviz_cam
  8.default=`"false"`
  8.type= bool
  8.desc= Enables/disables usage of RVIZ camera position to transform control commands according to it.

  9.name=~rviz_cam_link
  9.default=`"/rviz_cam"`
  9.type= string
  9.desc= RVIZ camera TF frame.

}
```

## Usage example

To test with simulated Care-O-Bot run following command:
```
roslaunch cob_spacenav_teleop spacenav_teleop_test_sim.launch
```

To test with a real robot, connect SN and launch its driver:

```
rosrun spacenav_node spacenav_node
```

Launch teleop:

```
roslaunch cob_spacenav_teleop spacenav_teleop.launch
```
