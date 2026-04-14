## Hardware Requirements

You\'ll need a TurtleBot!
[Don\'t have one yet?](http://clearpathrobotics.com/turtlebot)

## Instructions

### Installation

1\. Make sure you have the OpenNI Kinect Driver Installed:
```
sudo apt-get install ros-diamondback-openni-kinect
```

2\. You\'ll also need to checkout the following Clearpath Packages:
```
svn co http://clearpath-ros-pkg.googlecode.com/svn/trunk/clearpath_kinect ~/clearpath-ros-pkg/clearpath_kinect
svn co http://clearpath-ros-pkg.googlecode.com/svn/trunk/clearpath_turtlebot ~/clearpath-ros-pkg/clearpath_turtlebot
```

3\. Add the following line to your \'.bashrc\' if it does not already
exist: ```
export ROS_PACKAGE_PATH=${HOME}/clearpath-ros-pkg:${ROS_PACKAGE_PATH}
```

4\. Compile all Clearpath Stacks: ```
rosmake clearpath_kinect
rosmake clearpath_turtlebot
```

### Demo

Make sure the robot starts with a good amount of floor area in it\'s
view so that it can properly calibrate the floor plane.

Use the launch file ```
roslaunch turtlebot_rndmwalk rndm_walk.launch
```

The robot will randomly switch between moving left, straight and right.
In addition the robot will stop when detecting an obstacle and turn for
a random period of time before continuing safe motion. The below video
shows what you should expect.

<http://www.youtube.com/watch?v=P4tag8NouLA>

## Nodes

```clearsilver
node {
  no_header=True
  0.name=ClearpathTurtleRndmWalk 
  0.desc= `ClearpathTurtleRndmWalk` is a ROS node that reads a frame from the Kinect PointCloud and generates a safe random motion output.
}
``` ```clearsilver
sub {
  0.name= rndmwalk_in(~in)
  0.type= sensor_msgs/PointCloud2
  0.desc= Get the Kinect Point cloud as a pcl::PointCloud<pcl::PointXYZRGB>.
}
pub {
  0.name= rndmwalk_out_vel(~out_vel)
  0.type= geometry_msgs/Twist
  0.desc= Publish the commanded velocity.
}
param{
    0.name = ~in
    0.type = string
    0.default = `"rndmwalk_in"`
    0.desc = Name of the topic your XYZRGB Point Cloud is on.
    1.name = ~out_vel
    1.type = string
    1.default = `"rndmwalk_out_vel"`
    1.desc = Name of the topic your cmd_vel should go out on.
    2.name = ~lin_speed
    2.type = double
    2.default = `0.3`
    2.desc = The linear speed for the robot in m/s.
    3.name = ~ang_speed
    3.type = double
    3.default = `0.75`
    3.desc = The angular speed for the robot in rad/s.
    4.name = ~still_ang_speed
    4.type = double
    4.default = `2.0`
    4.desc = The angular speed for the robot in rad/s, when turning in place.
    5.name = ~cam_height
    5.type = double
    5.default = `0.3`
    5.desc = Approximate camera height above the floor plane.
    6.name = ~stop_distance
    6.type = double
    6.default = `0.8`
    6.desc = How close the robot is allowed to come to obstacles.
    7.name = ~stop_point_count
    7.type = int
    7.default = `50`
    7.desc = The number of points that must be inside the stop_distance to warrant an obstacle.
}
```
