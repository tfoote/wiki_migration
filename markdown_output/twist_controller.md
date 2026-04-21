A Cartesian ROS-controller for commanding target twists to a robot.

This controller makes use of a `TwistCommandInterface` to set a user
specified twist message as reference for robot control.

## Configuration

A possible configuration looks like this:



```highlight
twist_controller:
   type:         ros_controllers_cartesianlers/TwistController

   # The controller uses this identifier to get the according command handle
   # from the hardware interface.
   frame_id:     "endpoint_to_control"

   joints:
   - joint1
   - joint2
   - joint3
   - joint4
   - joint5
   - joint6
```


