## Overview

The point cluster grasp planner plans grasps on a segmented point cloud
(typically from the narrow stereo or Kinect) by finding the point
cloud's principal axes and searching for grasps along those axes from
the top and side (NOT grasps of the bounding box used for
visualization\--grasps of the underlying points along the axes of the
displayed box). It also finds overhead grasps of high points with the
gripper oriented toward the center, which is useful for objects such as
bowls. Details on this module can be found in the following paper:
[\*\*Contact-Reactive Grasping of Objects with Partial Shape Information\*\*](http://www.willowgarage.com/sites/default/files/contactreactive.pdf).

The planner can be used for other types of robot hands as well, if a
box-model is created for the hand in a fixed, pre-grasp pose (both
collision boxes and object-should-be-in-here boxes). See the config
directory for models of the 3-fingered Schunk hand and the RobotIQ hand.

Launch the grasp planning server (offers both service and action for
grasp planning, and a separate service for changing various params) with
scripts/point_cluster_grasp_planner_server.py and look in the package
pr2_pick_and_place_demos, test/test_pr2_gripper_grasp_planner_cluster.py
for an example of how to run the grasp planner with the results from the
tabletop object detector. Email hsiao at willowgarage.com if you have
questions.

## ROS API

### API Stability

-   ROS API is UNREVIEWED and UNSTABLE

### Services Offered



```clearsilver
srv{
 no_header= True
 0.name = /plan_point_cluster_grasp
 0.type = object_manipulation_msgs/GraspPlanning
 0.desc = This service takes in grasp planning requests (with the object specified as an object_manipulation_msgs/GraspableObject, which in this case should contain a point cloud) and returns a list of planned grasps.
}
```



### ROS Parameters

There are lots of params besides this one. They're all described in
point_cluster_grasp_planner.py. 

```clearsilver
param {
  no_header= True
  0.name= min_good_grasp_points
  0.default= 15
  0.type= int
  0.desc= The number of points in the cloud that should be in the gripper model's inside-the-gripper-space-box for the grasp to be considered viable (should change depending on the density of the input cloud)
}
```



### ROS Topics

(In Fuerte and beyond, enable this marker for debugging by setting
self.draw_gripper to be 1 in point_cluster_grasp_planner.py. The planner
is much much faster if it doesn't have to draw the grasps.)


```clearsilver
pub {
  no_header= True
  0.name= point_cluster_grasp_planner_markers
  0.type= visualization_msgs/Marker
  0.desc= Shows the boxy gripper model (used for evaluating collisions with the object and whether there are points within the grasp) at each potential grasp pose as it's being checked.
}
```


