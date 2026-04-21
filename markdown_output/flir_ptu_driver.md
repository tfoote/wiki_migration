![\|align="right"](attachment:PTU-D46.png)

## Overview

This driver is particularly intended for use with the
[FLIR D46](http://www.flir.com/mcs/view/?id=53707) line of pan-tilt
units. However, because FLIR uses a common serial protocol for their
products, this node is likely to work on related FLIR devices, or be
adaptable without too much trouble.

### URDF

![\|width="200",align="right"](attachment:flir-ptu-frames.png)

Alongside the basic serial driver, there is also included a URDF
description of the D46. This is structured as a xacro macro, so it
should be straightforward to integrate into your complete robot
description. The
[example.urdf.xacro](https://github.com/ros-drivers/flir_ptu/blob/master/flir_ptu_description/urdf/example.urdf.xacro)
file provides an example of how to use the macro.

To visualize the model without running the driver, you can launch it
like so:



```
roslaunch flir_ptu_viz view_model.launch
```



This should produce an [rviz](rviz) window showing the device model, as
well as a [joint_state_publisher](joint_state_publisher) window letting
you adjust the joint values.

### Usage

To try out the driver prior to integration with a larger robot, you can
connect and power it, and run:



```
roslaunch flir_ptu_driver ptu.launch port:=/dev/ttyUSB0
```



Once up, you can bring up the visualization in rviz:



```
roslaunch flir_ptu_viz view_ptu.launch
```



You can send it one-off commands using a provided convenience script:



```
ROS_NAMESPACE=ptu rosrun flir_ptu_driver cmd_angles -0.6 0.3
```



## Nodes



```clearsilver
node.0 {
 name = ptu_driver
 desc = Basic serial driver.
 pub {
  0.name = state
  0.type = sensor_msgs/JointState
  0.desc = Angles of the pan and tilt joints, as reported by the device. Note that if too-large velocities are commanded, the steppers will slip, which this 
 }
 sub {
  0.name = cmd
  0.type = sensor_msgs/JointState
  0.desc = Target angles for the pan and tilt joints. The device will attempt to travel to the specified angles, using the velocities given. The effort array is ignored.
 }
 param {
  0.name = ~port
  0.type = string
  0.desc = Serial device to connect to.
  0.default = /dev/ttyUSB0
  1.name = ~baud
  1.type = int
  1.desc = Baud rate of serial link.
  1.default = 9600
  2.name = ~hz
  2.type = int
  2.desc = Rate at which to publish the `state` message. Note that the device is polled for this data.
  2.default = 10
 }
}
```



## Roadmap

The basic driver is stable and usable, but various improvements and
fixes are needed, as tracked on Github. Pull requests addressing these
are very welcome.

## License Note

The driver portion of this package is an evolution of the old
[ptu46](ptu46) package, and thus retains its GPL licensing. However, as
it is a standalone binary, this should not be an obstacle to using this
code. The URDF description macro is BSD, so you are free to integrate
that into other projects without implications on their licensing.
