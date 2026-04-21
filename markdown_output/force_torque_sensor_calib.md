## Overview

This package can calibrate through least-squares the following
parameters related to a wrist-mounted force-torque sensor:

-   Bias of the F/T sensor
-   Mass of the gripper
-   Location of the center of mass of the attached gripper

Running this software assumes that you have an **accelerometer/imu**
whose reference frame is already calibrated with respect to some
reference frame on the robot manipulator. It also assumes that you have
a manipulator previously configured to be controlled through
[MoveIt!](moveit).

The software calibrates the F/T sensor by moving the manipulator into a
number of different poses and using the resulting F/T sensor and
accelerometer signals for computing a least-squares estimate of the
parameters. Calibration can be done by either manually specifying
explicitly the manipulator poses in the parameter server (parameters
**pose0, pose1, pose2, \... poseN**) or by executing N random poses.

## ROS API

```clearsilver
name = ft_calib_node
desc = The `ft_calib_node` moves the robot arm into different positions and collects (raw) F/T sensor readings and accelerometer readings to calibrate the force-torque sensor.

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

param {
    0.name = ~loop_rate
    0.type = double
    0.default = 650.0
    0.desc = frequency (in Hz) of the ft_calib_node main loop (should be set equal to the publishing frequency of the force-torque sensor).

    1.name = ~wait_time
    1.type = double
    1.default = 4.0
    1.desc = waiting time (in sec) between the moment the manipulator reaches each pose and the calibration node starts taking force-torque measurements.

    2.name = ~moveit_group_name
    2.type = string
    2.desc = moveit group name of the robot arm to which the force-torque sensor is attached to.

    3.name = ~calib_file_name
    3.type = string
    3.default = 'ft_calib_data.yaml'
    3.desc = name of the output calibration file.

    4.name = ~calib_file_dir
    4.type = string
    4.default = '~/.ros/ft_calib'
    4.desc = directory for saving the output calibration file.

    5.name = ~meas_file_name
    5.type = string
    5.default = 'ft_calib_meas.txt'
    5.desc = name of the file to store the measurements used for calibration.

    6.name = ~meas_file_dir
    6.type = string
    6.default = '~/.ros/ft_calib'
    6.desc = name of the directory to store the measurements used for calibration.

    7.name = ~random_poses
    7.type = bool
    7.default = false
    7.desc = set to '''true''' to move the arm to random poses for calibration. Setting to '''false''' requires manually specifying the manipulator's calibration poses.

    8.name = ~number_random_poses
    8.type = int
    8.default = 30
    8.desc = specifies the number of random poses to execute for calibration.

    9.name = ~poses_frame_id
    9.type = string
    9.desc = specifies the frame ID in which the poses are expressed. Only used if the '''~random_poses''' parameter is set to `false`.

    10.name = ~poseN
    10.type = double array
    10.desc = 6x1 array of doubles which specifies the pose of the gripper with respect to the '''poses_frame_id''' frame ID. The representation is in [x y z r p y] (`x,y,z` translation and `roll/pitch/yaw` rotation). You can specify `pose0, pose1, pose2, ... poseN` parameters.
```

## Running the calibration node

Make sure that the robot is still and other objects don\'t obstruct the
arms while they move into the calibration poses.

You can look at the configuration/launch files in the *config* and
*launch* folders for examples on how to set the parameters and launch
the software for your robot.

The calibration software will produce a **yaml** calibration file that
can later be used for gravity compensation. By default the file will be
written in the **/.ros/ft_calib/** directory.

For more detailed instructions please visit the
[force_torque_tools tutorials page](force_torque_tools/Tutorials).

## Example calibration file

An example calibration file output from this calibration node can be
found under **config/ft_calib_data_example.yaml** in the
force_torque_sensor_calib package.

## Tutorials

Please visit the [tutorials page](force_torque_tools/Tutorials).

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.

Please submit your tickets through
[github](https://github.com/kth-ros-pkg/force_torque_tools/issues/)
(requires github account) or by emailing the maintainers.
