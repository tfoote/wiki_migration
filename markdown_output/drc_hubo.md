## Overview

[Youtube](https://www.youtube.com/watch?v=LtcKGVNkHHw)

## DRC-HUBO+

![](attachment:drc_hubo.png)

DRC-HUBO+ is a humanoid robot platform which was developed for DARPA
Robotics Challenge (DRC). It has 32 DOFs (1: head, 8x2: arm & hand, 7x2:
leg & wheel, 1: waist), 4 FT sensors, 1 IMU, and 1 fiber obtic gyro
(FOG). It also has one fixed camera and one more camera attached to one
LIDAR actuated by motor for scanning.

[Youtube](https://www.youtube.com/watch?v=BGOUSvaQcBs)

## PODO

PODO is a real-time robot controlling framework which name stands for
"grape" in Korean. It provides users with multiple processes called
ALs (which means "grape berries" in Korean). Software architecture of
PODO is shown in the below figure.

![](attachment:podo.png)

There is a special process called Daemon that directly accesses the
hardware. The hardware information is abstracted and categorized, and
this information is located between Daemon and the ALs as Shared Memory;
this Inter Process Communication (IPC) method is chosen because it is
very fast and easy to use, and there is no increasing of the complexity
regardless of the number of connected processes. Thus, ALs can control
the hardware indirectly through the Shared Memory and through Daemon.
This means that users do not have to know the details of how to
communicate with and manipulate the hardware devices. The only thing
that changes when the hardware is modified or expanded is the Shared
Memory: ALs and Daemon are not affected by hardware changes.

PODO suggests synchronization of threads between Daemon and ALs, as can
be seen in the below figure.

![](attachment:podo_sync.png)

Daemon updates the sensor data in the Shared Memory, and sends
synchronization (Sync) signals to ALs. The ALs keep watching these Sync
signals and read the sensor values when the signals are received. After
that, the ALs update the joint references that were calculated in the
previous step. At this time, acknowledgement (Ack) signals are also sent
to Daemon via the Shared memory. The ALs can calculate their algorithms
and generate joint references with the sensor values after sending an
Ack signal. Because time gaps between the obtaining of a current Sync
signals and of the next Sync signals are almost identical and periodic,
the time allowed to calculate a joint reference is almost the same as
the control period of Daemon. While the ALs are working, each AL
recognizes an Ack signal and proceeds to the next step. ALs send the
received joint references to Daemon and then request the sensor's next
data. Through this procedure, ALs synchronize with Daemon.

In this package, PODO uses ROS as its external process and Gazebo as its
simulator. They are synchronized each other using [/clock](Clock) topic
(simulation time), and it is shown in the below figure.

![](attachment:podo_ros_gazebo.png)

## Installation & Setting

1\. Get the source from the
[repository](https://github.com/JeongsooLim/drc_hubo).
```
// clone the source from repository
cd ~/catkin_ws/src
git clone -b indigo-devel https://github.com/JeongsooLim/drc_hubo
```

2\. If you are using Indigo, you need to remove default Gazebo2 and
install Gazebo5. ```
// remove default Gazebo2
sudo apt-get remove ros-indigo-gazebo-*

// add source list
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt-get update

// install Gazebo5
sudo apt-get install ros-indigo-gazebo5-*
```

3\. Move the contents of
"home/{user_name}/catkin_ws/src/drc_hubo/gazebo_model" in the source
to "home/{user_name}/.gazebo/models/".

Change the absolute paths in the source.

a\. home/{user_name}/.gazebo/models/DRC_hubo/DRC_hubo.sdf
```
<plugin name="drc_plugin" filename="/home/hubo/catkin_ws/devel/lib/libdrc_plugin.so"/>
-->
<plugin name="drc_plugin" filename="/home/{user_name}/catkin_ws/devel/lib/libdrc_plugin.so"/>
```

b\. home/{user_name}/.gazebo/models/DRC_head/DRC_head.sdf

home/{user_name}/.gazebo/models/DRC_head_kinect/DRC_head_kinect.sdf
```
<plugin name="head_plugin" filename="/home/hubo/catkin_ws/devel/lib/libhead_plugin.so"/>
-->
<plugin name="head_plugin" filename="/home/{user_name}/catkin_ws/devel/lib/libhead_plugin.so"/>
```

c\.
home/{user_name}/catkin_ws/src/drc_hubo/ros/drc_podo_connector/src/podo_connector.cpp
```
fpNet = fopen("/home/hubo/catkin_ws/src/drc_hubo/ros/settings/network.txt", "r");
-->
fpNet = fopen("/home/{user_name}/catkin_ws/src/drc_hubo/ros/settings/network.txt", "r");
```

d\.
home/{user_name}/catkin_ws/src/drc_hubo/ros/drc_plugin/src/drc_plugin.cpp
```
fpNet = fopen("/home/hubo/catkin_ws/src/drc_hubo/ros/settings/network.txt", "r");
-->
fpNet = fopen("/home/{user_name}/catkin_ws/src/drc_hubo/ros/settings/network.txt", "r");
----
fpGain = fopen("/home/hubo/catkin_ws/src/drc_hubo/ros/settings/gain.txt", "r");
-->
fpGain = fopen("/home/{user_name}/catkin_ws/src/drc_hubo/ros/settings/gain.txt", "r");
```

e\.
home/{user_name}/catkin_ws/src/drc_hubo/ros/drc_podo_connector/launch/drc_hubo.launch
```
args="-sdf -file /home/hubo/.gazebo/models/DRC_hubo/DRC_hubo.sdf -model DRC_hubo"
-->
args="-sdf -file /home/{user_name}/.gazebo/models/DRC_hubo/DRC_hubo.sdf -model DRC_hubo"
```

## Nodes

```clearsilver
 name = podo_connector
 desc = The `podo_connector` node receives robot data from PODO and publishes <<MsgLink(sensor_msgs/JointState)>>. It also subscribes velocity commands (<<MsgLink(geometry_msgs/Twist)>>) from other nodes such as [[move_base]]. Because of DRC-HUBO+ has two modes of operation, podo_connector subscribes [[tf]] to change appropriate basis, and it also publishes <<MsgLink(nav_msgs/Odometry)>> for [[gmapping]] and [[navigation]]. 
 sub {
   0{
    name = tf
    type = tf/tfMessage
    desc = Transforms depending on the posture of robot (wheel mode or walking mode) for generating another transform 'base_footprint' to 'Body_TORSO'
    }
   1{
    name = cmd_vel
    type = geometry_msgs/Twist
    desc = A stream of velocity commands for navigation in wheel mode
    }
  }
 pub {
   0{
    name = joint_states
    type = sensor_msgs/JointState
    desc = [[robot_state_publisher]] will subscribe this topic and generate [[tf]] of robot frames
   }
   1{
    name = odom
    type = nav_msgs/Odometry
    desc = the odometry information of robot in wheel mode
   }
   2{
    name = drc_head_cmd
    type = drc_podo_connector/DRC_HEAD_CMD
    desc = control command for head_plugin (change angle, 3D scan)
   }
  }
 
 req_tf{
  0{
    from = Body_TORSO
    to = Body_LWH
    desc = broadcast periodically by a [[robot_state_publisher]]
  }
  1{
    from = Body_TORSO
    to = Body_RWH
    desc = broadcast periodically by a [[robot_state_publisher]]
  }
  2{
    from = Body_TORSO
    to = Body_RAFT
    desc = broadcast periodically by a [[robot_state_publisher]]
  }
  3{
    from = Body_TORSO
    to = Body_LAFT
    desc = broadcast periodically by a [[robot_state_publisher]]
  }
 }
 prov_tf{
  0{
    from = base_footprint
    to = Body_TORSO
    desc = the current estimate of the robot's pose from the basis of robot
  }
  1{
    from = odom
    to = base_footprint
    desc = the current estimate of the robot's basis from the global odometry frame
  }
 }
```

```clearsilver

 name = head_plugin
 desc = The `head_plugin` node receives operating command of head module of the robot and <<MsgLink(sensor_msgs/LaserScan)>> from existing [[gazebo_plugins]] ([[http://gazebosim.org/tutorials?tut=ros_gzplugins|libgazebo_ros_camera, libgazebo_ros_laser, libgazebo_ros_openni_kinect]]) implemented in SDF model file, and publishes <<MsgLink(sensor_msgs/PointCloud2)>>. This node also publishes <<MsgLink(sensor_msgs/JointState)>> of scanning joint and [[tf]] of sensor frames.
sub {
   0{
    name = drc_head_cmd
    type = drc_plugin/DRC_HEAD_CMD
    desc = control command for head_plugin (change angle, 3D scan)
    }
   1{
    name = scan
    type = sensor_msgs/LaserScan
    desc = Laser scans to create 3D point cloud
    }
  }
pub {
   0{
    name = joint_states
    type = sensor_msgs/JointState
    desc = [[robot_state_publisher]] will subscribe this topic and generate [[tf]] of robot frames
   }
   1{
    name = odom
    type = nav_msgs/Odometry
    desc = the odometry information of robot in wheel mode
   }
   2{
    name = point_cloud
    type = sensor_msgs/PointCloud2
    desc = point cloud data from the head module
   }
  }
 prov_tf{
  0{
    from = Body_Hokuyo
    to = Sensor_scan
    desc = Neck frame to Hokuyo LIDAR frame
  }
  1{
    from = Body_Hokuyo
    to = Sensor_camera
    desc = Neck frame to camera frame which is attached below the LIDAR
  }
  2{
    from = Body_Hokuyo
    to = Sensor_streaming
    desc = Neck frame to camera frame which is attached on the outer shield
  }
 }
```

## Examples

### SLAM (wheel mode)

a\. launch PODO (Daemon and PODOGUI)

b\. launch drc_hubo.launch ```
roslaunch drc_podo_connector drc_hubo.launch
```

c\. launch slam.launch ```
// remove default Gazebo2
sudo apt-get remove ros-indigo-gazebo-*

// add source list
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt-get update

// install Gazebo5
sudo apt-get install ros-indigo-gazebo5-*
```0

d\. make wheel mode using PODOGUI and click the "ROS MODE"

e\. use [teleop_twist_joy](teleop_twist_joy) to make a map

### Navigation (wheel mode)

[Youtube](https://www.youtube.com/watch?v=Mv8wr_y9XOc)

a\. launch PODO (Daemon and PODOGUI)

b\. launch drc_hubo.launch ```
// remove default Gazebo2
sudo apt-get remove ros-indigo-gazebo-*

// add source list
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt-get update

// install Gazebo5
sudo apt-get install ros-indigo-gazebo5-*
```1

c\. launch navi.launch ```
// remove default Gazebo2
sudo apt-get remove ros-indigo-gazebo-*

// add source list
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt-get update

// install Gazebo5
sudo apt-get install ros-indigo-gazebo5-*
```2

d\. make wheel mode using PODOGUI and click the "ROS MODE"

e\. use [rviz](rviz) to give an initial position and a goal command

### Using Real Robot Platform

[Youtube](https://www.youtube.com/watch?v=ZtU606QLSq8)

## More Information

-   [ HuboLab Homepage](http://hubolab.kaist.ac.kr )

```{=html}
<!-- -->
```
-   [ Rainbow-Robotics Homepage](http://rainbow-robotics.com )

------------------------------------------------------------------------
