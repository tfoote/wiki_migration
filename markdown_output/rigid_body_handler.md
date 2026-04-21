# Rigid body handler

## Pose

This handler allows to publish the pose of an object in the V-REP scene
and/or to set its pose from ROS.

You can enable the publisher of the pose by adding in the child script
of the object the following line:

```
pose_handl = simGetObjectAssociatedWithScript(sim_handle_self)
simExtSetFloatCustomDataFromHeader(pose_handl, sim_ext_ros_bridge_obj_pose_data_main, 0.0)
```

You can change the third parameter as you wish to set the frequency of
the publisher. If you leave 0.0 the publishing frequency will be equal
to the simulation frequency.

## Twist

This handler allows to publish the twist of an object in the V-REP scene
and/or to apply a twist to it from ROS.

You can enable the subscriber of the twist adding in the child script of
the object the following line: ```
twist_handl = simGetObjectAssociatedWithScript(sim_handle_self)
simExtSetIntCustomDataFromHeader(twist_handl, sim_ext_ros_bridge_set_obj_twist_data_main, 0)
```

In this case the received velocities will be automatically applied to
the object. If the third argument of the function is "0" the velocity
is taken referred to the body frame, if equal to "1" is taken referred
to the world frame.
