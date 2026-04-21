## About

This script can delay the launch of a roslaunch file.

## Installation

### apt

To install the `timed_roslaunch` package via apt, type the command as
follows. 

```shell
sudo apt install ros-${ROS_DISTRO}-timed-roslaunch
```



### source

To install the `timed_roslaunch` package, you can install from source
with the following commands:



```shell
cd /(your catkin workspace)/src
git clone https://github.com/MoriKen254/timed_roslaunch.git
cd ..
catkin_make
```



## Usage

This script can delay the launch of a roslaunch file. Make sure that the
file is executable (chmod +x timed_roslaunch.sh)

### Run it from command line



```shell
rosrun timed_roslaunch timed_roslaunch.sh [number of seconds to delay] [rospkg] [roslaunch file] [arguments (optional)]
```



Or



```shell
roslaunch timed_roslaunch timed_roslaunch.launch time:=[number of second to delay] pkg:=[rospkg] file:=[roslaunch file] value:=[arguments (optional)]
```



Example:



```shell
rosrun timed_roslaunch timed_roslaunch.sh 2 turtlebot_navigation amcl_demo.launch initial_pose_x:=17.0 initial_pose_y:=17.0"
```



### Run it from another roslaunch file



```python
<launch>
  <include file="$(find timed_roslaunch)/launch/timed_roslaunch.launch">
    <arg name="time" value="2" />
    <arg name="pkg" value="turtlebot_navigation" />
    <arg name="file" value="amcl_demo.launch" />
    <arg name="value" value="initial_pose_x:=17.0 initial_pose_y:=17.0" />
    <arg name="node_name" value="timed_roslaunch" /> <!-- This is optional argument -->
    <arg name="output" value="screen" /> <!-- This is an optional argument -->
  </include>
</launch>
```



Or



```python
<launch>
  <node pkg="timed_roslaunch" type="timed_roslaunch.sh"
    args="2 turtlebot_navigation amcl_demo.launch initial_pose_x:=17.0 initial_pose_y:=17.0"
    name="timed_roslaunch" output="screen" />
</launch>
```


