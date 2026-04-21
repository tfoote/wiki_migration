## Overview

`robot_markers` is a library for creating
[RViz markers](http://wiki.ros.org/rviz/DisplayTypes/Marker) for a
robot, given a [URDF](http://wiki.ros.org/urdf).

![\|height="400px",width="709px"](attachment:demo.png)

## Quick start

The library's generated documentation explains how to use
`robot_markers`.

[robot_markers::Builder](http://docs.ros.org/indigo/api/robot_markers/html/classrobot__markers_1_1Builder.html)
is the main interface for building a
[MarkerArray](http://docs.ros.org/indigo/api/visualization_msgs/html/msg/MarkerArray.html)
from a URDF.

First, create a `Builder` for a given URDF:



```cplusplus
#include "robot_markers/builder.h"
#include "ros/ros.h"
#include "urdf/model.h"

urdf::Model model;
model.initParam("robot_description");

robot_markers::Builder builder(model);
builder.Init();
```



There are a variety of configuration options you can set before
generating the markers (pose, color, etc.). You should always specify a
namespace and a frame ID.



```cplusplus
builder.SetNamespace("robot");
builder.SetFrameId("base_link");
builder.SetColor(0.33, 0.17, 0.45, 1); // A color of 0, 0, 0, 0 means to use the mesh colors.
geometry_msgs::Pose pose;
pose.position.y = 1;
pose.orientation.w = 0.92387953;
pose.orientation.z = -0.38268343;
builder.SetPose(pose);
```



A notable feature of `Builder` is the ability to set the joint angles
of the robot. To do so, pass in a map that gives the joint angles for a
set of joint names. `Builder` does not check joint angle limits.



```cplusplus
#include <map>
#include <string>

std::map<std::string, double> joint_positions;
joint_positions["torso_lift_joint"] = 0.1;
joint_positions["head_tilt_joint"] = 0.5;
builder.SetJointPositions(joint_positions);
```



Once you have configured the visualization, call `Builder::Build`,
passing in a marker array to append the robot markers to.



```cplusplus
ros::Publisher marker_arr_pub =
  nh.advertise<visualization_msgs::MarkerArray>("robot", 10);
visualization_msgs::MarkerArray robot1;
builder.Build(&robot1);
marker_arr_pub.publish(robot1);
```



Here is a full example, available as a demo file.



```cplusplus
#include <map>
#include <string>

#include "geometry_msgs/Pose.h"
#include "robot_markers/builder.h"
#include "ros/ros.h"
#include "urdf/model.h"
#include "visualization_msgs/MarkerArray.h"

int main(int argc, char** argv) {
  ros::init(argc, argv, "robot_markers_demo");
  ros::NodeHandle nh;
  ros::Publisher marker_arr_pub =
      nh.advertise<visualization_msgs::MarkerArray>("robot", 10);
  ros::Duration(0.5).sleep();

  urdf::Model model;
  model.initParam("robot_description");

  robot_markers::Builder builder(model);
  builder.Init();

  // Robot 1: Default configuration, purple.
  visualization_msgs::MarkerArray robot1;
  builder.SetNamespace("robot");
  builder.SetFrameId("base_link");
  builder.SetColor(0.33, 0.17, 0.45, 1);
  builder.Build(&robot1);
  marker_arr_pub.publish(robot1);

  // Robot 2: Different pose, joints changed.
  visualization_msgs::MarkerArray robot2;
  builder.SetNamespace("robot2");
  builder.SetColor(0, 0, 0, 0);

  std::map<std::string, double> joint_positions;
  joint_positions["torso_lift_joint"] = 0.1;
  joint_positions["head_tilt_joint"] = 0.5;
  builder.SetJointPositions(joint_positions);

  geometry_msgs::Pose pose;
  pose.position.y = 1;
  pose.orientation.w = 0.92387953;
  pose.orientation.z = -0.38268343;
  builder.SetPose(pose);
  builder.Build(&robot2);
  marker_arr_pub.publish(robot2);

  ros::Duration(0.5).sleep();

  return 0;
}
```


