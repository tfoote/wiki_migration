![\|height="200",width="333"](attachment:Logo-white-medium.jpg)

## Description

This package provides a description of the robot's kinematic chain
containing all relevant frames as well as both static transformations
and dynamic joints connecting frames among each other.

![height="590",width="335"\|height="661",width="377"](attachment:MILD_Degrees_Of_Freedom.png)
![height="590",width="335"\|height="659",width="365"](attachment:MILD_Transformations.png)

*Left: The robot's rotational and translational degrees of freedom.
Right: Overview over the robot's most important frames and
transformations.*

## Functionality

The mild's kinematic chain is described in
**robot_description/mild.urdf **within this package. (See the
[ros wiki](http://wiki.ros.org/urdf/Tutorials) for a detailed
explanation of the urdf format)

The kinematic chain consists of two major parts: The robot's
environment (map) as well as the robot's base and the camera-system
including PTU, Guppy-Cameras (and Kinect as an optional component). The
fixed reference Frame is in the PTU and is called **/ptu_pan_link**.

**Map to Robot Base**

-   /map - the origin of the map in which the robot is located
-   /odom - the robot's position in the map, located by the odometry
-   /base_link - the robot's base center point
-   /base_laser - the 2D-laserscanner's sensor frame

**PTU Base to Camera**

-   /ptu_base_link - the base frame of the pan-tilt-unit
-   /ptu_pan_link - the origin of the pan joint
-   /ptu_pan_link_rotated - the rotated part of the pan joint
-   /ptu_tilt_link - the origin of the tilt joint
-   /ptu_tilted_link - the rotated part of the tilt joint
-   /ptu_mount_link - the mounting frame for both cameras
-   /camera_left_frame - the left camera's origin
-   /camera_right_frame - the right camera's origin

![height="1443",width="1000"\|height="1578",width="1119"](attachment:Mild_Frames.png)

## Usage

### Needed packages

**run depend: **

-   [asr_flir_ptu_driver](asr_flir_ptu_driver): TF of real and simulated
    PTU.
-   [asr_mild_base_driving](asr_mild_base_driving) /
    [asr_mild_base_fake_driving](asr_mild_base_fake_driving): TF of the
    mild's base from real / simulated odometry

### Needed hardware

For simulation nothing is needed. Additional hardware components:

-   Pan-Tilt-Unit (PTU)
-   MILD base plattform (See [here](asr_mild_base_driving) for detailed
    description)

### Start system

The transformation publisher is usually not run directly from this
package. Instead, use the launch files provided in
[asr_mild_navigation](asr_mild_navigation).

The following launch file can be used to publish additional
transformations needed for the use of a mounted kinect camera:

```
roslaunch asr_mild_kinematic_chain transformation_publishers_kinect_left.launch
```

## Tutorials

See [asr_mild_navigation](asr_mild_navigation) for tutorials on how to
set up the full kinematic chain.
