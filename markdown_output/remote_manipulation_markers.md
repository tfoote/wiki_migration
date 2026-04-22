## About

The `remote_manipulation_markers` package contains interactive marker
servers for a set of remote manipulation interaction approaches. The
approaches include Free Positioning, Constrained Positioning, and
Point-and-Click. These interactive marker servers are intended for use
with rviz or with Robot Web Tools interfaces.

## Remote Manipulation Interaction Approaches

This package includes three approaches: Free Positioning (FP),
Constrained Positioning (CP), and Point-and-Click (P&C). The three
approaches are shown below, with interaction points for setting initial
poses shown in yellow, and interaction points for adjusting poses shown
in blue.

![\|width="700px"](attachment:interaction.png)

Free positioning uses a ring-and-arrow marker which can be clicked and
dragged to individually adjust translation along and rotation about each
Cartesian axis. Constrained positioning uses a sphere marker to first
set a grasp point, followed by setting an approach angle by clicking on
the surface of the sphere. The approach angle is constrained to pass
through the grasp point. Point-and-click makes use of autonomous grasp
calculation, and involves the user selecting a previously calculated
grasp for execution from a list of potential grasps. Further details on
these can be found in
[ A Comparison of Remote Robot Teleoperation Interfaces for General Object Manipulation](http://dl.acm.org/citation.cfm?id=3020249 ),
published in HRI 2017. The approaches are designed for both 2D and 3D
visualization modes. For full details and a comparison of the efficiency
and effectiveness of each approach in both 2D and 3D visualization
modes, see our IJRR 2019 article
[ Leveraging depth data in remote robot teleoperation interfaces for general object manipulation](https://journals.sagepub.com/doi/full/10.1177/0278364919888565 ).
Videos of the approaches in action can be found
[ here](https://youtu.be/4NTyDVmpXRY ) and
[ here](https://youtu.be/1atKPcV_YqU ).

## Messages and Services

## Nodes



```clearsilver
node.0 {
  name = free_positioning
  desc = 'free_positioning' contains the interactive marker server for the Free Positioning interaction approach, i.e. a 6-DOF marker that can be moved in free space with no constraints.
  pub {
    0.name = gripper_marker_pose
    0.type = geometry_msgs/PoseStamped
    0.desc = Publishes the current pose of the gripper marker contained in the free positioning marker.
  }
  srv {
    0.name = reset_marker_pose
    0.type = std_srvs/Empty
    0.desc = Set the marker pose to the current position of the end-effector.
  }
  goal {
    0.name = execute_grasp/goal
    0.type = remote_manipulation_markers/SpecifiedGraspGoal
    0.desc = Execute a grasp action at the pose specified by the marker free positioning marker.
  }
  feedback {
    0.name = execute_grasp/feedback
    0.type = remote_manipulation_markers/SpecifiedGraspFeedback
    0.desc = String indicating the current state of grasp execution.
  }
  result {
    0.name = execute_grasp/result
    0.type = remote_manipulation_markers/SpecifiedGraspResult
    0.desc = Grasp execution success.
  }
  act_called {
    0.name = grasp
    0.type = rail_manipulation_msgs/PickupAction
    0.desc = Action client for grasp execution. The topic can be changed by setting the `grasp_topic` parameter.
  }
  param {
    0.name = base_link
    0.type = string
    0.desc = Name of the base link in the tf tree used for creating the free positioning marker.
    0.default = "base_link"
    1.name = eef_link
    1.type = string
    1.desc = Name of the end-effector link in the tf tree used for creating the free positioning marker.
    1.default = "eef_link"
    2.name = grasp_topic
    2.type = string
    2.desc = Sets the topic name for connecting to the grasp action server.
    2.default = "grasp"
  }
}
node.1 {
  name = constrained_positioning
  desc = 'constrained_positioning' contains the interactive marker server for the Constrained Positioning interaction approach, i.e. a set of markers for specifying a grasp point and an approach angle.
  pub {
    0.name = gripper_marker_pose
    0.type = geometry_msgs/PoseStamped
    0.desc = Publishes the current pose of the gripper marker contained in the free positioning marker.
  }
  srv {
    0.name = clear_gripper_marker
    0.type = std_srvs/Empty
    0.desc = Remove the gripper marker.
    1.name = clear_full_marker
    1.type = std_srvs/Empty
    1.desc = Remove the gripper and the sphere markers.
    2.name = create_sphere
    2.type = remote_manipulation_markers/CreateSphere
    2.desc = Create a sphere marker at the given point.
  }
  goal {
    0.name = execute_grasp/goal
    0.type = remote_manipulation_markers/SpecifiedGraspGoal
    0.desc = Execute a grasp action at the pose specified by the marker free positioning marker.
  }
  feedback {
    0.name = execute_grasp/feedback
    0.type = remote_manipulation_markers/SpecifiedGraspFeedback
    0.desc = String indicating the current state of grasp execution.
  }
  result {
    0.name = execute_grasp/result
    0.type = remote_manipulation_markers/SpecifiedGraspResult
    0.desc = Grasp execution success.
  }
  act_called {
    0.name = grasp
    0.type = rail_manipulation_msgs/PickupAction
    0.desc = Action client for grasp execution. The topic can be changed by setting the `grasp_topic` parameter.
  }
  param {
    0.name = grasp_topic
    0.type = string
    0.desc = Sets the topic name for connecting to the grasp action server.
    0.default = "grasp"
  }
}
node.2 {
  name = point_and_click
  desc = 'point_and_click' contains the interactive marker server for the Point-and-Click interaction approach, i.e. functionality for displaying and cycling through a set of calculated end-effector poses.
  sub {
    0.name = /grasp_sampler/sampled_grasps
    0.type = geometry_msgs/PoseArray
    0.desc = Set of calculated poses to be displayed. The topic can be changed by setting the `calculatedPosesTopic` parameter.
  }
  srv {
    0.name = cycle_grasps
    0.type = remote_manipulation_markers/CycleGrasps
    0.desc = Cycle the currently displayed end-effector pose forward or backward in the calculated poses list.
  }
  goal {
    0.name = execute_grasp/goal
    0.type = remote_manipulation_markers/SpecifiedGraspGoal
    0.desc = Execute a grasp action at the pose specified by the marker free positioning marker.
  }
  feedback {
    0.name = execute_grasp/feedback
    0.type = remote_manipulation_markers/SpecifiedGraspFeedback
    0.desc = String indicating the current state of grasp execution.
  }
  result {
    0.name = execute_grasp/result
    0.type = remote_manipulation_markers/SpecifiedGraspResult
    0.desc = Grasp execution success.
  }
  act_called {
    0.name = grasp
    0.type = rail_manipulation_msgs/PickupAction
    0.desc = Action client for grasp execution. The topic can be changed by setting the `grasp_topic` parameter.
  }
  param {
    0.name = grasp_topic
    0.type = string
    0.desc = Sets the topic name for connecting to the grasp action server.
    0.default = "grasp"
    1.name = calculated_poses_topic
    1.type = string
    1.desc = Sets the topic name for subscribing to the calculated poses list.
    1.default = "grasp_sampler/sampled_grasps"
  }
}
node.3 {
  name = gripper_marker_vis
  desc = A marker server that displays a non-interactable gripper marker at the gripper location specified by one of the other interaction approaches.  This can be used with the Free Positioning and Constrained Positioning approaches, and will link the gripper pose to that of the free positioning or constrained positioning markers.
  sub {
    0.name = /free_positioning/gripper_marker_pose
    0.type = geometry_msgs/PoseStamped
    0.desc = Gets the current pose of the free or constrained positioning marker pose. The namespace for this topic can be set with the `marker_node_name` parameter.
  }
  param {
    0.name = marker_node_name
    0.type = string
    0.desc = Sets the namespace of the topic for connecting to another interaction marker.
    0.default = "free_positioning"
  }
}
```



## Installation

To install the `remote_manipulation_markers` package, you can install
from source with the following commands: . 

```shell
cd /(your catkin workspace)/src
git clone https://github.com/GT-RAIL/remote_manipulation_markers.git
cd ..
catkin_make
catkin_make install
```



## Startup

Each of the methods can be launched with its own launch file, as
follows:

. 

```
roslaunch remote_manipulation_markers free_positioning.launch
```



. 

```
roslaunch remote_manipulation_markers constrained_positioning.launch
```



. 

```
roslaunch remote_manipulation_markers point_and_click.launch
```



Note that `free_positioning.launch` and
`constrained_positioning.launch` include a boolean parameter
`run_separate_vis`. Setting `run_seperate_vis` to true will launch a
`gripper_marker_vis` node that corresponds to the free or constrained
positioning node.

## Citation

If you use this package in your work, please cite our
[ IJRR article](https://journals.sagepub.com/doi/full/10.1177/0278364919888565 ):

David Kent, Carl Saldanha, and Sonia Chernova. Leveraging Depth Data in
Remote Robot Teleoperation Interfaces for General Object Manipulation.
*The International Journal of Robotics Research*, 2019.
