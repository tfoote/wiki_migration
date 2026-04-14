## Prerequisites

Running this node requires you to have a calibrated force-torque sensor
(bias of the sensor + mass & center of mass of gripper) and an
accelerometer whose reference frame has already been calibrated to some
reference frame of the robot. You can do this by using the
[force_torque_sensor_calib](force_torque_sensor_calib) package. Please
look at the [ tutorials page](force_torque_tools/Tutorials) of the
[force_torque_tools](force_torque_tools) metapackage for instructions on
how to run the calibration node.

## ROS API

```clearsilver
name = gravity_compensation_node
desc = The `gravity_compensation_node` compensates gravitational forces on the gripper of the robot so that force-torque signals are zeroed. Assumes previously calibrated accelerometer and F/T sensor. It also broadcasts through '''tf''' the pose of the center of mass of the gripper from the force-torque sensor calibration.

sub {
   0{
    name = ~/ft_raw
    type = geometry_msgs/WrenchStamped
    desc = The raw (uncalibrated) F/T sensor readings.
    }

   1{
    name = ~/imu
    type = sensor_msgs/Imu
    desc = Measurements from an accelerometer already calibrated to the robot's frame.
    }
   }

pub {

   0 {
    name = ~/ft_zeroed
    type = geometry_msgs/WrenchStamped
    desc = force torque measurements after subtracting the sensor bias.
     }

   1 {
     name = ~/ft_compensated
     type = geometry_msgs/WrenchStamped
     desc = force torque measurements after subtracting the sensor bias and the gravitational forces.
     }
    }

param {
    0.name = ~ns
    0.type = string
    0.default = "~"
    0.desc = All published topics are pushed down into the <ns> namespace, i.e., the topics for the compensated force-torque measurements (`ft_zeroed` and `ft_compensated`) will be published under <ns> (`<ns>/ft_zeroed` and `<ns>/ft_compensated`.

    1.name = ~bias
    1.type = double array
    1.desc = 6x1 double array which contains the ([fx, fy, fz, tx, ty, tz]) force-torque bias of the force-torque sensor.

    2.name = ~gripper_mass
    2.type = double
    2.desc = mass of the gripper attached to the force-torque sensor.
    
    3.name = ~gripper_com_frame_id
    3.type = string
    3.desc = ID of the frame in which the gripper center of mass is expressed.

    4.name = ~gripper_com_child_frame_id
    4.type = string
    4.desc = ID of the (child) frame of the gripper center of mass. This can be freely chosen by the user.

    5.name = ~gripper_com_pose
    5.type = double array
    5.desc = 6x1 array ([x y z r p y]) with `x,y,z` translation and `roll, pitch, yaw` orientation (in meters and radians) containing the pose of the gripper COM expressed in the `gripper_com_frame_id` frame

    6.name = ~gripper_com_broadcast_frequency
    6.type = double
    6.default = 100.0
    6.desc = broadcast frequency (in Hz) of the gripper COM pose on /tf.

    7.name = ~loop_rate
    7.type = double
    7.default = 1000.0
    7.desc = frequency (in Hz) of the main loop of the gravity compensation node (should be at the same frequency as the publish frequency of the force-torque sensor).

      }
```

## Launching the node

An example calibration file required to run this node can be found under
\'\'\'config/ft_calib_data_example.yaml\'\'\' in the
[force_torque_sensor_calib](force_torque_sensor_calib) package.

You can launch the node using the
\'\'\'gravity_compensation.launch\'\'\' file contained in the \`launch\`
folder of the package and setting a few roslaunch arguments, e.g.:

```
roslaunch gravity_compensation gravity_compensation.launch node_name:=gravity_compensation calib_data_file:=$HOME/.ros/ft_calib/ft_calib_data.yaml ft_raw:=/ft_sensor/ft_raw imu:=/imu/data loop_rate:=650.0 ns=/ft_sensor gripper_com_child_frame_id:=gripper_com
```

where the arguments are:

-   \'\'\'node_name\'\'\' sets the name of the gravity_compensation node
    being launched.
-   \'\'\'calib_data_file\'\'\': location of the force-torque sensor
    calibration data.
-   \'\'\'ft_raw\'\'\': name of topic where raw force-torque sensor
    readings are published.
-   \'\'\'imu\'\'\': name of the topic where the accelerometer readings
    are published.
-   \'\'\'loop_rate\'\'\': frequency (in Hz) of the main loop of the
    node.
-   \'\'\'ns\'\'\': namespace under which to publish the topics for the
    compensated force-torque measurements (\`ns/ft_zeroed\` and
    \`ns/ft_compensated\`).
-   \'\'\'gripper_com_child_frame_id\'\'\': ID of the (child) frame of
    the gripper center of mass. This can be freely chosen by the user.

## Tutorials

Please visit the [ tutorials page](force_torque_tools/Tutorials) of the
[force_torque_tools](force_torque_tools) metapackage.

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.

Please submit your tickets through
[github](https://github.com/kth-ros-pkg/force_torque_tools/issues/)
(requires github account) or by emailing the maintainers.
