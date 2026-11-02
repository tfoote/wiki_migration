## How to use the Robot Pose EKF

### Configuration

A default launch file for the EKF node can be found in the
robot_pose_ekf package directory. The launch file contains a number of
configurable parameters:

- freq: the update and publishing frequency of the filter. Note that a
  higher frequency will give you more robot poses over time, but it will
  not increase the accuracy of each estimated robot pose.
- sensor_timeout: when a sensor stops sending information to the filter,
  how long should the filter wait before moving on without that sensor.
- odom_used, imu_used, vo_used: enable or disable inputs.

The configuration can be modified in the launch file, which looks
something like this:

. 

```
<launch>
  <node pkg="robot_pose_ekf" type="robot_pose_ekf" name="robot_pose_ekf">
    <param name="output_frame" value="odom"/>
    <param name="base_footprint_frame" value="base_link"/>
    <param name="freq" value="30.0"/>
    <param name="sensor_timeout" value="1.0"/>
    <param name="odom_used" value="true"/>
    <param name="imu_used" value="true"/>
    <param name="vo_used" value="true"/>
    <param name="debug" value="false"/>
    <param name="self_diagnose" value="false"/>
  </node>
 </launch>
```



### Running

- **Build** the package 

```
$ rosdep install robot_pose_ekf
 $ roscd robot_pose_ekf
 $ rosmake
```



<!-- -->

- **Run** the robot pose ekf 

```
$ roslaunch robot_pose_ekf.launch
```



## Nodes



```clearsilver
node.0{
 name = robot_pose_ekf
 desc = `robot_pose_ekf` implements an extended Kalman filter for determining the robot pose.
 sub {
  0.name= odom
  0.type= nav_msgs/Odometry
  0.desc= '''2D pose''' (used by wheel odometry): The 2D pose contains the position and orientation of the robot in the ground plane and the covariance on this pose. The message to send this 2D pose actually represents a 3D pose, but the z, roll and pitch are simply ignored. 
  1.name= imu_data 
  1.type= sensor_msgs/Imu
  1.desc= '''3D orientation''' (used by the IMU): The 3D orientation provides information about the Roll, Pitch and Yaw angles of the robot base frame relative to a world reference frame. The Roll and Pitch angles are interpreted as absolute angles (because an IMU sensor has a gravity reference), and the Yaw angle is interpreted as a relative angle. A covariance matrix specifies the uncertainty on the orientation measurement. The robot pose ekf will not start when it only receives messages on this topic; it also expects messages on either the 'vo' or the 'odom' topic.
  2.name= vo
  2.type= nav_msgs/Odometry
  2.desc= '''3D pose''' (used by Visual Odometry): The 3D pose represents the full position and orientation of the robot and the covariance on this pose. When a sensor only measures part of a 3D pose (e.g. the wheel odometry only measures a 2D pose), simply specify a large covariance on the parts of the 3D pose that were not actually measured.
 }
}
```



The `robot_pose_ekf` node does not require all three sensor sources to
be available all the time. Each source gives a pose estimate and a
covariance. The sources operate at different rates and with different
latencies. A source can appear and disappear over time, and the node
will automatically detect and use the available sensors.To add your own
sensor inputs, check out
[the Adding a GPS sensor tutorial](#adding-a-gps-sensor-to-the-robot-pose-ekf-filter)



```clearsilver
pub {
  0.name= robot_pose_ekf/odom_combined
  0.type= geometry_msgs/PoseWithCovarianceStamped
  0.desc= The output of the filter (the estimated 3D robot pose).
}
```





```clearsilver
prov_tf {
  0.from = odom_combined  
  0.to= base_footprint
  0.desc= 
}
```



## How Robot Pose EKF works

### Pose interpretation

All the sensor sources that send information to the filter node can have
their own *world* reference frame, and each of these *world* reference
frames can drift arbitrary over time. Therefore, the **absolute poses**
sent by the different sensors cannot be compared to each other. The node
uses the **relative pose differences** of each sensor to update the
extended Kalman filter.

### Covariance interpretation

As a robot moves around, the uncertainty on its pose in a world
reference continues to grow larger and larger. Over time, the covariance
would grow without bounds. Therefore it is not useful to publish the
covariance on the pose itself, instead the sensor sources publish how
the covariance changes over time, i.e. the covariance on the velocity.
*Note that using observations of the world (e.g. measuring the distance
to a known wall) will reduce the uncertainty on the robot pose; this
however is localization, not odometry.*

### Timing

Imagine the robot pose filter was last updated at time t_0. The node
will not update the robot pose filter until at least one measurement of
*each* sensor arrived with a timestamp later than t_0. When e.g. a
message was received on the `odom` topic with timestamp t_1 > t_0,
and on the `imu_data` topic with timestamp t_2 > t_1 > t_0, the
filter will now update to the latest time at which information about all
sensors is available, in this case to time t_1. The odom pose at t_1 is
directly given, and the imu pose at t_1 is obtained by linear
interpolation of the imu pose between t_0 and t_2. The robot pose filter
is updated with the relative poses of the odom and imu, between t_0 and
t_1.

![attachment:robot_pose_ekf.png](doc/robot_pose_ekf.png)

The above figure shows experimental results when the PR2 robot started
from a given initial position (green dot), driven around, and returned
to the initial position. A perfect odometry x-y plot should show an
exact loop closure. The blue line shows the input from the wheel
odometry, with the blue dot the estimated end position. The red line
shows the output of the `robot_pose_ekf`, which combined information
of wheel odometry and imu, with the red dot the estimated end position.

## Package Status

### Stability

The code base of this package has been well tested and has been stable
for a long time. The ROS API however has been changing as message types
have evolved over time. In future versions, the ROS API is likely to
change again, to a simplified single-topic interface (see Roadmap
below).

### Roadmap

- The filter is currently designed for the three sensor signals (wheel
  odometry, imu and vo) that we use on the PR2 robot. We plan to make
  this package more generic: future versions will be able to listen to
  'n' sensor sources, all publishing a
  ([nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html))
  message. Each source will set the covariance of the 3D pose in the
  Odometry message to specify which part of the 3D pose it actually
  measured.
- We would like to add velocity to the state of the extended Kalman
  filter.

## Tutorials

## Adding a GPS sensor to the Robot Pose EKF Filter

### Available topics

The Robot Pose EKF node listens for ROS messages on the following topic
names:

- */odom* for the nav_msgs::Odometry message as a 2D pose
- */imu_data* for the sensor_msgs::Imu message as a 3D orientation
- */vo* for the nav_msgs::Odometry message as a 3D pose

To use the Robot Pose EKF node with your own sensor, you need to publish
sensor measurements on one of these three topics. The sensor needs to
publish the position and orientation of the **base_footprint** frame of
the robot, in a world-fixed frame. Any world-fixed frame is fine, and
each sensor can use a different world-fixed frame. Note that each topic
can only take the input of **one single** sensor. In future versions, we
plan the ability to attach *n* sensor signals to the robot pose ekf (see
the Roadmap section). Currently, the most generic input message is the
Odometry, sent on the /vo topic. It contains a 3D pose and 3D twist,
each with a covariance. So this would be the best topic to use when
adding your own sensor.

### Building a GPS sensor message

A GPS sensor measures the robot 3d position, but not its orientation.
The Odometry message sent by the GPS sensor could look something like
this:

. 

```
msg.header.stamp = gps_time                   // time of gps measurement
 msg.header.frame_id = base_footprint          // the tracked robot frame
 msg.pose.pose.position.x = gps_x              // x measurement GPS.
 msg.pose.pose.position.y = gps_y              // y measurement GPS.
 msg.pose.pose.position.z = gps_z              // z measurement GPS.
 msg.pose.pose.orientation.x = 1               // identity quaternion
 msg.pose.pose.orientation.y = 0               // identity quaternion
 msg.pose.pose.orientation.z = 0               // identity quaternion
 msg.pose.pose.orientation.w = 0               // identity quaternion
 msg.pose.covariance = {cox_x, 0, 0, 0, 0, 0,  // covariance on gps_x
                        0, cov_y, 0, 0, 0, 0,  // covariance on gps_y
                        0, 0, cov_z, 0, 0, 0,  // covariance on gps_z
                        0, 0, 0, 99999, 0, 0,  // large covariance on rot x
                        0, 0, 0, 0, 99999, 0,  // large covariance on rot y
                        0, 0, 0, 0, 0, 99999}  // large covariance on rot z
```



#### Using a GPS driver that publishes NavSatFix

The `utm_odometry_node` in the
[gps_common](https://index.ros.org/p/gps_common) package may be used to
convert GPS measurements from
[sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)
to
[sensor_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Odometry.html).

. 

```
<node name="gps_conv" pkg="gps_common" type="utm_odometry_node">
  <remap from="odom" to="vo"/>
  <remap from="fix" to="/gps/fix" />
  <param name="rot_covariance" value="99999" />
  <param name="frame_id" value="base_footprint" />
</node>
```



### Remapping the topic name

The GPS sensor sends its measurements on the topic name *gps_meas*, but
the Robot Pose EKF node expects messages of type Odometry on the topic
name *odom*. To connect the GPS sensor with the filter node, we need to
remap the topic name the node listens on. Therefore, add the following
line to the launch file of the node, within the <node> \... </node>
scope:

. 

```
<remap from="vo" to="gps_meas" />
```



The output of the filter (the estimated 3D robot pose) is broadcast on
the /robot_pose_ekf/odom_combined topic. The node also broadcasts the
transform from 'odom_combined' to 'base_link' to the transform (tf)
topic */tf_message*.

------------------------------------------------------------------------

## Tutorials

- [Adding a GPS sensor to the Robot Pose EKF Filter](#adding-a-gps-sensor-to-the-robot-pose-ekf-filter):
  This tutorial describes how to add GPS sensor input to the Robot Pose
  EKF Filter.

## Troubleshooting

### Understanding log messages

#### Errors when using package

- *Timestamps of odometry and imu are x seconds apart* This error occurs
  when the timestamps of the sensor messages that are received differ
  more than 1 second. This is probably an indication of timing issues in
  your system, e.g. the clocks of two hosts connected to the same ros
  core are not synchronized.

<!-- -->

- *Covariance specified for measurement on topic xxx is zero* Each
  measurement that is processed by the robot pose ekf needs to have a
  covariance associated with it. The diagonal elements of the covariance
  matrix cannot be zero. This error is shown when one of the diagonal
  elements is zero. Messages with an invalid covariance will not be used
  to update the filter.

<!-- -->

- *Filter time older than xxx message buffer* This error occurs when two
  sensor inputs have timestamps that are not synchronized. All sensor
  inputs are stored in a message buffer; this buffer keeps data for 10
  seconds. When the timestamps of two sensor inputs are more than 10
  seconds apart, data will get lost from the message buffer, and you'll
  get this error.

#### Warnings when using package

- *Robot pose ekf diagnostics discovered a potential problem* This
  warning occurs when the internal diagnostics find that something is
  wrong. At this time, the diagnostics system only checks for the
  consistency between the odom and imu sensors. When these two sources
  provide *very different* information about the robot pose, this is a
  good indication that something might be wrong with some of the sensor
  measurements/timestamps.

#### Info when using package

- *xxx sensor activated* This message indicates that a sensor source was
  detected and activated. After receiving this message the filter can
  use measurements from this sensor.

<!-- -->

- *Waiting to activate xxx, because xxx measurements are still x sec in
  the future* When a sensor signal first arrives, its timestamp is
  potentially newer than the latest filter update time. This message
  indicates that sensor will remain inactive, until the filter catches
  up.

<!-- -->

- *xxx sensor not active any more* When a sensor source is not sending
  any measurement for a user-specified timeout (default 1 sec), that
  sensor source is deactivated.

<!-- -->

- *Fiter initialized* This message indicates that either the odom sensor
  or the vo sensor has been detected and activated, and the filter has
  been initialized. After this message is shown, the filter will get
  updated at the user-specified frequency.

### The robot pose ekf does not work

The robot pose ekf provides a service call to give information on its
internal state. Simply run: 

```
$ rosrun robot_pose_ekf wtf.py
```

 The output will
give you good clues about possible problems.

#### Is the robot pose ekf still running?

To check if the robot pose ekf is running, you should find out on what
the name of the node is. The node name depends on the name you specified
in the launch file: 

```
...
  <node pkg="robot_pose_ekf" type="robot_pose_ekf" name="my_name">
  ...
```

 Look for the
*name="\..."* field. In this example, the node name is 'my_name'. To
verify if the node is running, type: 

```
$ rosnode ping my_name
```



#### Is the robot pose ekf sending output?

First you should find out on what topic name the robot pose ekf is
supposed to publish data. The topic name depends on the name you
specified in the launch file: 

```
...
  <node pkg="robot_pose_ekf" type="robot_pose_ekf" name="my_name">
  ...
```

 Look for the
*name="\..."* field. In this example, the output topic name is set to
'my_name/odom_combined'. To verify if any output is published, type:


```
$ rostopic hz my_name/odom_combined
```

 You should see an average publish rate being
displayed. If not, the output is not published.

#### Is the robot pose ekf receiving input?

The robot pose ekf listens on three topics: '/odom', '/imu_data' and
'/vo'. To check if any input is received on these topics, type:


```
$ rostopic hz /odom
 $ rostopic hz /imu_data
 $ rostopic hz /vo
```

 You should see an average publish rate being
displayed. If not, the input is not published.
