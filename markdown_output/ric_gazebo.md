## Preliminary Setup

First make sure you have the latest ric meta-package installed. See
[Installation Instructions](ric#Installation) on the ric page.

Then, install additional packages:

```
$ sudo apt-get install ros-indigo-gazebo-ros-pkgs ros-indigo-gazebo-ros-control ros-indigo-hector-gazebo ros-indigo-ros-controllers
```

## Launch

To launch the simulation with default parameters run the specific robot
simulation launch file:

```
$ roslaunch ric_gazebo komodo_gazebo.launch
``` or:

```
$ roslaunch ric_gazebo lizi_gazebo.launch
``` or:

```
$ roslaunch ric_gazebo komodo_with_elev_gazebo.launch
``` To change the robot color, name, initial
position and orientation and sensors edit the robot spawn block in the
simulation launch file:

```
<include file="$(find ric_gazebo)/launch/spawn_lizi.launch">
    <include file="$(find ric_gazebo)/launch/spawn_lizi.launch">
    <arg name="name" value="lizi_1"/>
    <arg name="color" value='Green'/>
    <arg name="front_camera" value='false'/>
    <arg name="depth_camera" value='false'/>
    <arg name="laser_scanner" value='true'/>
    <arg name="urf" value='false'/>
    <arg name="imu" value='false'/>
    <arg name="pan_tilt" value='false'/>
    <arg name="x" value="0.0" />
    <arg name="y" value="0.0" />
    <arg name="z" value="0.1" />
    <arg name="R" value="0.0" />
    <arg name="P" value="0.0" />
    <arg name="Y" value="0.0" />
  </include>

Here is and example of the Komodo robot launched with default settings:
```
![alt text\|width=\"600\"](attachment:gazeboo.png)

To launch multiple robots in the same simulation add another block on
the launch file as bellow:

```
<include file="$(find ric_gazebo)/launch/spawn_komodo.launch">
    <arg name="name" value="komodo_1"/>
    <arg name="color" value="White"/>
    <arg name="x" value="0.0" />
    <arg name="y" value="0.0" />
    <arg name="z" value="0.1" />
    <arg name="R" value="0.0" />
    <arg name="P" value="0.0" />
    <arg name="Y" value="0.0" />
  </include>


  <include file="$(find ric_gazebo)/launch/spawn_komodo.launch">
  <arg name="name" value="komodo_2"/>
  <arg name="color" value="Grey"/>
  <arg name="x" value="0.0" />
  <arg name="y" value="1.0" />
  <arg name="z" value="0.1" />
  <arg name="R" value="0.0" />
  <arg name="P" value="0.0" />
  <arg name="Y" value="0.0" />
  </include>
```
![alt text\|width=\"600\"](attachment:gazeboo2.png)

You can view the robots sensors using rviz:

![alt text\|width=\"600\"](attachment:rviz.png)

## Topics that are good to know (only komodo models)

### Subscribers

1\. komodo\_\<ID\>/base_rotation_controller/command

-   Function: Rotate the arm.
-   Msg type: std_msgs/Float64 1.
    komodo\_\<ID\>/shoulder_controller/command
-   Function: Move the shoulder of the arm up and down.
-   Msg type: std_msgs/Float64 1.
    komodo\_\<ID\>/elbow1_controller/command
-   Function: Move the first elbow of the arm left and right.
-   Msg type: std_msgs/Float64 1.
    komodo\_\<ID\>/elbow2_controller/command
-   Function: Move the second elbow of the arm up and down.
-   Msg type: std_msgs/Float64 1.
    komodo\_\<ID\>/wrist_controller/command
-   Function: Rotate the wrist left and right.
-   Msg type: std_msgs/Float64 1.
    komodo\_\<ID\>/right_finger_controller/command
-   Function: move the right finger, left or right.
-   Msg type: std_msgs/Float64 1.
    komodo\_\<ID\>/left_finger_controller/command
-   Function: move the left finger, left or right.
-   Msg type: std_msgs/Float64 1. komodo\_\<ID\>/diff_driver/command
-   Function: steering the robot.
-   Msg type: geometry_msgs/Twist

\'\'\'Subscribers that are only present in the komodo with elevator and
arm\'\'\'

1\. komodo\_\<ID\>/elevator_controller/command

-   Function: Move the komodo elevator up and down.
-   Msg type: std_msgs/Float64

### Publishers

1\. komodo\_\<ID\>/scan

-   Function: Publish the laser scan.
-   Msg type: sensor_msgs/LaserScan 1.
    komodo\_\<ID\>/arm_camera/image_raw
-   Function: Publish images from the arm camera.
-   Msg type: sensor_msgs/Image 1. komodo\_\<ID\>/Front_Camera/image_raw
-   Function: Publish images from the front camera.
-   Msg type: sensor_msgs/Image 1. komodo\_\<ID\>/diff_driver/odometry
-   Function: Publish the odometry of the robot.
-   Msg type: nav_msgs/Odometry

\'\'\'Publishers that are only prasent in the komodo with elevator and
arm\'\'\'

1\. komodo\_\<ID\>/Creative_Camera/rgb/image_raw

-   Function: Publish images from the arm camera.
-   Msg type: sensor_msgs/Image 1.
    komodo\_\<ID\>/Creative_Camera/depth/image_raw
-   Function: Publish a depth images from the arm camera.
-   Msg type: sensor_msgs/Image 1.
    komodo\_\<ID\>/Asus_Camera/rgb/image_raw
-   Function: Publish images from the top asus camera.
-   Msg type: sensor_msgs/Image 1.
    komodo\_\<ID\>/Asus_Camera/depth/image_raw
-   Function: Publish a depth images from the asus camera
-   Msg type: sensor_msgs/Image 1. komodo\_\<ID\>/rear_camera/image_raw
-   Function: Publish images from the rear camera.
-   Msg type: sensor_msgs/Image 1. komodo\_\<ID\>/top_camera/image_raw
-   Function: Publish images from the top camera
-   Msg type: sensor_msgs/Image

## Moveit with ric_gazebo

### Launch

To launch the komodo with arm model type this commend in a new terminal:

```
$ roslaunch komodo_2_moveit_config komodo_gazebo_moveit.launch
``` To launch the komodo with elevator and arm
model type this commend in a new terminal:

```
$ roslaunch komodo_arm_moveit_config komodo_with_elev_gazebo_moveit.launch
```

## Videos

[Youtube](https://www.youtube.com/watch?v=TlfbsmkksNw)

Komodo with arm running moveit

[Youtube](https://www.youtube.com/watch?v=vS5BSWrXK8s)

Komodo with arm and elevator running moveit

[Youtube](https://www.youtube.com/watch?v=IAymw9QR0BY)

## Troubleshoot

If you see something like this after launching:

```
Warning [gazebo.cc:215] Waited 1seconds for namespaces.
Warning [gazebo.cc:215] Waited 1seconds for namespaces.
Warning [gazebo.cc:215] Waited 1seconds for namespaces.
Warning [gazebo.cc:215] Waited 1seconds for namespaces.
Warning [gazebo.cc:215] Waited 1seconds for namespaces.
Warning [gazebo.cc:215] Waited 1seconds for namespaces.
Warning [gazebo.cc:215] Waited 1seconds for namespaces.
Warning [gazebo.cc:215] Waited 1seconds for namespaces.
Warning [gazebo.cc:215] Waited 1seconds for namespaces.
Warning [gazebo.cc:215] Waited 1seconds for namespaces.
Error [gazebo.cc:220] Waited 11 seconds for namespaces. Giving up.
``` Try to upgrade to gazebo 2.2.5:

```
> sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu trusty main" > /etc/apt/sources.list.d/gazebo-latest.list'
> wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
``` Then if you update Ubuntu, It install Gazebo
2.2.5.
