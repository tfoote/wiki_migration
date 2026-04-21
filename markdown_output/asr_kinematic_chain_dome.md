![\|width=\"333\",height=\"200\"](attachment:Logo-white-medium.jpg)

## Description

This package provides information about the PbD dome\'s kinematic chain
and contains launch-files to publish the chain to a
robot_state_publisher. Available launchfiles are: dome with real PTU,
dome with simulated PTU, dome with real PTU and Flock of Birds magnet
tracking system and additional transformation_publisher from
guppy-cameras to the kinect cameras mounted above. It also contains the
URDF model of the dome for visualization. There is no real program code
in this package only an urdf file and launch-files/-scripts. A
screenshot of RVIZ shows the visualization and the kinematic chain. The
red Box is the Flock of Birds magnet tracking system.

![height=\"417\",width=\"498\"\|width=\"493\",height=\"413\"](attachment:dome_1.png)

## Functionality

![height=\"241\",width=\"396\"\|width=\"254\",height=\"155\"](attachment:dome_2.png)

The kinematic chain consists of two major parts: The camera-system (PTU,
Guppy-Cameras and Kinect) and the Flock of Birds magnet tracking system
(Receiver and Tracker). Colors form the picture above. The fixed
reference Frame is in the PTU and is called **/ptu_pan_link**. There is
an identity transformation to **/map** which is mostly used.

**Map to Flock of Birds**

-   /map - the origin of the map in which the robot is located (=
    /ptu_pan_link)
-   /ptu_pan_link - the origin of the panning part of the PTU
-   /ptu_rot - the rotation of the metal plate under the PTU
-   /Root - the Flock_Of_Birds Tracking Box(red Box in picture)
-   /tracker_left_raw - the left tracker
-   /tracker_right_raw - the right tracker

**Map to Camera **

-   /ptu_pan_link - the origin of the pan joint
-   /ptu_tilt_link - the origin of the tilt joint
-   /ptu_tilted_link - the rotated part of the tilt joint
-   /camera_left_frame - the left camera\'s origin
-   /camera_right_frame - the right camera\'s origin

**Additional optional TF-Links for kinect**

-   /kinect_depth_frame - the kinects depth camera origin
-   /kinect_rgb_frame - the kinects RGB camera frame

An total overview of the frames:

![height=\"406\",width=\"957\"\|width=\"1113\",height=\"472\"](attachment:domke_frames.jpg)

## Usage

-   **dome_mock.launch**: Starts the **simulation of the PTU** and
    launches the TF-publisher of the dome, as well as its visualization.
-   **dome.launch**: Starts the **real PTU** and launches the
    transformation publisher of the Dome, as well as its visualization.
-   **dome_with_fob.launch**: Starts the **real PTU** and launches the
    transformation publisher of the Dome, as well as its visualization.
    In addition the Flock of Birds server is started and its
    TF-publisher are added to the kinematic chain.
-   **dome_with_fob.sh**: Same as dome_with_fob.launch but sets system
    variables before launching, e. g. when the Flock of Birds server is
    not on the same PC like the ROS_MASTER.
-   **transformation_publisher_for_kinect_left.launch**: Adds to the
    kinematic chain TF-Publisher form the normal camara System to the
    kinect camera.

The TF is published at topic /tf. The visualization is available in the
!RobotModel.

### Needed packages

**run depend: **

-   asr_flir_ptu_driver: TF of real and simulated PTU.
-   asr_flock_of_birds: TF and sensordata of Flock of Birds magnet
    tracking system.

### Needed hardware

For simulation nothing is needed. Additional hardware components:

-   Pan-Tilt-Unit (PTU)
-   Guppy-Stereo-Camera System
-   Kinect Camera
-   Flock_of_birds magnettracking system

### Start system

To launch the kinematic chain as simulation, run

```
roslauch asr_kinematic_chain_dome dome_mock.launch
``` To launch the kinematic chain on real hardware,
run

```
roslauch asr_kinematic_chain_dome dome.launch
``` or

```
rosrun asr_kinematic_chain_dome dome_with_fob.sh
``` to use the Kinect, run one of the commands
above and

```
roslauch asr_kinematic_chain_dome transformation_publishers_for_kinect_left.launch
``` start rviz and** enable the !RobotModel for
visualization**
