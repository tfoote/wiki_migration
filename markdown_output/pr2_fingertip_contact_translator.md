## Stability

This package has not been reviewed, so the API documented below should
be considered unstable. Also, this package has not been user-tested, so
there may be usability issues with the nodes.

## ROS API

Please see the [finger tip pressure sensors](fingertip_pressure) we are
simulating on the PR2 hardware.

\'\'\'Note\'\'\': All nodes assume that \`\<gripper_motor_name\>\` is
either \`r_gripper_motor\` or \`l_gripper_motor\`.

```clearsilver

node.0 {
name=sensor_info
desc=Publishes sensor geometry, tf frame and unit scaling information.
pub{
 0.name= /pressure/<gripper_motor_name>_info
 0.type= fingertip_pressure/PressureInfo
 0.desc= For each sensor, the tf frame is specified, and for each pressure sensing element, a scaling factor to Newtons, and rectangular geometry approximation are provided.
}
sub{
 0.name="l_gripper_l_finger_tip_bumper/state"
 0.type= gazebo_plugins/ContactState
 0.desc= Contact states from gazebo simulation plugin (gazebo_ros_bumper) for the left arm left finger tip
 1.name="l_gripper_r_finger_tip_bumper/state"
 1.type= gazebo_plugins/ContactState
 1.desc= Contact states from gazebo simulation plugin (gazebo_ros_bumper) for the left arm right finger tip
 2.name="r_gripper_l_finger_tip_bumper/state"
 2.type= gazebo_plugins/ContactState
 2.desc= Contact states from gazebo simulation plugin (gazebo_ros_bumper) for the right arm left finger tip
 3.name="r_gripper_r_finger_tip_bumper/state"
 3.type= gazebo_plugins/ContactState
 3.desc= Contact states from gazebo simulation plugin (gazebo_ros_bumper) for the right arm right finger tip
}
}
```

### Launch files

To test this node: ```
rosrun pr2_fingertip_contact_translator pr2_fingertip_contact_translator.py
```
