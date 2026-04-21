```wiki
'''Citation Note'''

If you are using this package in your research work, please cite our article, more info[[https://wiki.ros.org/gmcl#Acknowledgements_.26_Citation|here]].
```

## Installation

Before installing gmcl package, please install ROS navigation stack in
your ROS workspace. You can do that with the following command:
```
$ sudo apt-get install ros-$ROS_DISTRO-navigation
``` Then download gmcl package and place it inside
the /src folder of your catkin workspace and compile it, which can be
done through following commands: ```
$ cd catkin_ws
$ git clone -b master https://github.com/adler-1994/gmcl src/gmcl
$ catkin_make
```

Following video shows gmcl in comparison to amcl while running on the
famous turtlebot 3 inside Gazebo simulation in solving the 3
localization problems (Pose Tracking, Global Localization,
Kidnapped-robot): [Youtube](https://www.youtube.com/watch?v=J9ZcCon6k-g)

## Algorithms

Algorithms could be divided into new and migrated from amcl:

### Migrated From amcl

Many of the algorithms and their parameters are well-described in the
book Probabilistic Robotics, by Thrun, Burgard, and Fox. The user is
advised to check there for more detail. In particular, we use the
following algorithms from that book:
**`sample_motion_model_odometry`**, **`beam_range_finder_model`**,
**`likelihood_field_range_finder_model`**, **`Augmented_MCL`**, and
**`KLD_Sampling_MCL`**.

### New Algorithms

Besides algorithms implemented in amcl, gmcl takes advantage of
**`Optimal particle filter`** as described
[here](https://ieeexplore.ieee.org/document/4543250) and **`
Intelligent particle filter`** as described
[here](https://ieeexplore.ieee.org/document/7031437) and
**`Self-adaptive particle filter`** as described
[here](https://ieeexplore.ieee.org/document/5262621) to improve the
performance of amcl while working in real time.

Modifications done on new algorithms to integrate them with amcl, Pseudo
code of amcl & gmcl algorithms, performance and complexity analysis of
amcl & gmcl are well-described in article
[here](https://www.researchgate.net/publication/359482651_Development_of_a_New_Technique_in_ROS_for_Mobile_Robots_Localization_in_Known-Based_2D_Environments).

## Package Requirements

In order to localize a mobile robot inside a map using gmcl package,
following must be represented:

### Complete TF Tree

The robot state publisher node -- more info
[here](http://wiki.ros.org/robot_state_publisher)-- must be running with
`robot_description` param of the robot's urdf and publishes the tf of
robots links (base link and lasers links). In addition, a motion
controller should publish the estimated robot motion as a transform
between the odometry frame (`odom_frame_id`) and the base frame
(`base_frame_id`).

### Occupancy Grid Map

A map server node --more info [here](http://wiki.ros.org/map_server)--
must publish a valid map using correct YAML format.

### Laser Scans

Robot must be equipped with at least one laser scanner. All lasers must
be fixed in place with respect to the robot base because `gmcl` looks
up the transform between the laser's frame (`laser_frame_id`) and the
base frame (`base_frame_id`), and latches it forever. So `gmcl`
"cannot" handle a laser that moves with respect to the base. All lasers
should publish their scans as (<<MsgLink( sensor_msgs/LaserScan
Message)>>) massege.

## Examples

Example of launch file that runs gmcl node and its parameters on
Differential drive mobile robot ```
../gmcl/examples/gmcl_diff.launch
``` To run gmcl
node with initial estimated pose e.g. at (x, y, yaw) := (-1, 2, 0.6)
```
$ rosrun gmcl gmcl_diff.launch initial_pose_x:=-1 initial_pose_y:=2 initial_pose_a:=0.6
```

Example of launch file that runs gmcl node and its parameters on
Holonomic wheeled mobile robot ```
../gmcl/examples/gmcl_omni.launch
``` To run gmcl node
with initial estimated pose e.g. at (x, y, yaw) := (-1, 2, 0.6)
```
$ rosrun gmcl gmcl_omni.launch initial_pose_x:=-1 initial_pose_y:=2 initial_pose_a:=0.6
```

## gmcl Node

Just like [amcl](amcl), `gmcl` takes in a laser-based map, laser
scans, and transform messages, and outputs pose estimates. On startup,
`gmcl` initializes its particle filter according to the parameters
provided. Note that, because of the defaults, if no parameters are set,
the initial filter state will be a moderately sized particle cloud
centered about (0,0,0). The drawing below shows localization using
`gmcl`. During operation `gmcl` estimates the transformation of the
base frame (`base_frame_id`) in respect to the map frame
(`global_frame_id`) but it only publishes the transform between map
frame and the odometry frame (`odom_frame_id`). Essentially, this
transform accounts for the drift that occurs using Dead Reckoning.
![\|width="750px"](attachment:gmcl_localization.png)

### Subscribed Topics

```clearsilver
  sub{
no_header=True
    0.name= scan
    0.type= sensor_msgs/LaserScan
    0.desc= Laser scans.
}
``` ```clearsilver
 sub{
no_header=True

    1.name= tf
    1.type= tf/tfMessage
    1.desc= Transforms.
}
```
```clearsilver
 sub{
no_header=True
    2.name= initialpose
    2.type= geometry_msgs/PoseWithCovarianceStamped
    2.desc= Mean and covariance with which to (re-)initialize the particle filter.
}
``` ```
$ sudo apt-get install ros-$ROS_DISTRO-navigation
```0

### Published Topics

```
$ sudo apt-get install ros-$ROS_DISTRO-navigation
```1 ```
$ sudo apt-get install ros-$ROS_DISTRO-navigation
```2
```
$ sudo apt-get install ros-$ROS_DISTRO-navigation
```3 ```
$ sudo apt-get install ros-$ROS_DISTRO-navigation
```4

### Services

```
$ sudo apt-get install ros-$ROS_DISTRO-navigation
```5 ```
$ sudo apt-get install ros-$ROS_DISTRO-navigation
```6
```
$ sudo apt-get install ros-$ROS_DISTRO-navigation
```7

### Services Called

```
$ sudo apt-get install ros-$ROS_DISTRO-navigation
```8

### Parameters

Besides Parameters that amcl uses to configure its node --Please check
[them](https://wiki.ros.org/amcl#Parameters)-- , gmcl adds eleven
Parameters to overall filter parameters to configure the `gmcl` node
and they are:

```
$ sudo apt-get install ros-$ROS_DISTRO-navigation
```9 ```
$ cd catkin_ws
$ git clone -b master https://github.com/adler-1994/gmcl src/gmcl
$ catkin_make
```0
```
$ cd catkin_ws
$ git clone -b master https://github.com/adler-1994/gmcl src/gmcl
$ catkin_make
```1 ```
$ cd catkin_ws
$ git clone -b master https://github.com/adler-1994/gmcl src/gmcl
$ catkin_make
```2 Previous parameters
define the Flow of gmcl algorithm and can be seen in following
drawing..... ![\|width="750px"](attachment:flow_chart.png) Full size
available
[here](https://wiki.ros.org/gmcl?action=AttachFile&do=get&target=flow_chart.png).

The following table shows name of different techniques based on filters
implemented, it could be seen that gmcl works with default parameters
same as amcl..... ![\|width="750px"](attachment:table.png)

```
$ cd catkin_ws
$ git clone -b master https://github.com/adler-1994/gmcl src/gmcl
$ catkin_make
```3

##### 

```
$ cd catkin_ws
$ git clone -b master https://github.com/adler-1994/gmcl src/gmcl
$ catkin_make
```4

```
$ cd catkin_ws
$ git clone -b master https://github.com/adler-1994/gmcl src/gmcl
$ catkin_make
```5 ```
$ cd catkin_ws
$ git clone -b master https://github.com/adler-1994/gmcl src/gmcl
$ catkin_make
```6
```
$ cd catkin_ws
$ git clone -b master https://github.com/adler-1994/gmcl src/gmcl
$ catkin_make
```7 ```
$ cd catkin_ws
$ git clone -b master https://github.com/adler-1994/gmcl src/gmcl
$ catkin_make
```8

##### 

```
$ cd catkin_ws
$ git clone -b master https://github.com/adler-1994/gmcl src/gmcl
$ catkin_make
```9 ```
../gmcl/examples/gmcl_diff.launch
```0
```
../gmcl/examples/gmcl_diff.launch
```1

## Feedback

To report a bug, or suggest an enhancement, please create a Github issue
[here](https://github.com/adler-1994/gmcl/issues/new).

If you already have enhanced the code and want to add your changes to
the main code, please send a Github pull request through your forked
copy of gmcl repository for merging. If you are not familiar with pull
requests please visit
[page](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

If you have a question, please post it on
[ROS answers](http://answers.ros.org/questions/scope:all/sort:activity-desc/tags:gmcl/page:1/),
make sure your question is tagged by **gmcl** so I get notified.

## Acknowledgements & Citation

This package was written during my master's thesis at Tishreen
University, Syria. My thesis advisor is
Dr.[Iyad Hatem](http://iyadhatem.altervista.org/).
![](attachment:iyad-mhd.png)

This work has been published as an article
[here](https://www.researchgate.net/publication/359482651_Development_of_a_New_Technique_in_ROS_for_Mobile_Robots_Localization_in_Known-Based_2D_Environments).
To properly cite it, please use the following:

```
../gmcl/examples/gmcl_diff.launch
```2
