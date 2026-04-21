## Overview

Assisted arm navigation package offers similar functionality as the
[Warehouse Viewer](arm_navigation/Tutorials/tools/Warehouse Viewer) - an
interactive (collision free) arm motion planning. It has been designed
for [Care-O-Bot](care-o-bot) within the SRS project, but can be easily
modified for any robot running the [arm_navigation](arm_navigation)
stack. It enables a user to start the arm planning through RVIZ plugin
with a simple interface. The goal position of the end effector can be
set by a 6 DOF Interactive Marker or by using [SpaceNavigator](spacenav)
device. For collision free trajectory planning a collision map produced
by [Environment Model](srs_env_model) is used.

**Current version has been tested only with ROS Electric.**

Assisted arm navigation is divided into following packages:

-   *srs_assisted_arm_navigation*: Main functionality.
-   *srs_assisted_arm_navigation_msgs*: Definition of services and
    action interface.
-   [srs_assisted_arm_navigation_ui](srs_assisted_arm_navigation_ui):
    RVIZ plugin.

For example of how this functionality can be integrated into more
complex system, please take a look on
[srs_arm_navigation_tests](srs_arm_navigation_tests), where is the
integration into SRS structure in form of SMACH generic states
implemented.

### Screenshots

This is how it looks in RVIZ when user starts arm planning. There is 6
DOF interactive marker, marker representing arm (green) and marker for
the object to be grasped.

![Assisted arm navigation started.\|width=600px](attachment:arm-nav-example-started.png)

Collision with environment or with the object is clearly indicated as
well as the situation when desired goal position is out of reach.

![Gripper in a collision.\|width=600px](attachment:arm-nav-example-collision.png)

![Position is not reachable.\|width=600px](attachment:arm-nav-example-not-reachable.png)

When the trajectory is planned, user can play its animation several
times and decide if it's reasonable and safe.

![Animation of planned trajectory.\|width=600px](attachment:arm-nav-example.png)

User interface consists of few controls and contains description of the
task for user (if using action interface to give tasks to user).

![User interface of Assisted arm navigation.\|width=200px](attachment:arm-nav-example-gui.png)

More detailed user interface documentation can be found on
[its own page](srs_assisted_arm_navigation_ui).

## ROS API

Assisted arm navigation node communicates with user interface using set
of services. There are also some services for adding collision objects
etc. The most important is action interface which can be used to ask
user to perform some task.

### Actionlib interface

##### Action Subscribed Topics



```clearsilver
sub {
  no_header= True
  0.name= /but_arm_manip/manual_arm_manip_action/goal
  0.type= srs_assisted_arm_navigation_msgs/ManualArmManipActionGoal
  0.desc=A task for user.
  1.name= /but_arm_manip/manual_arm_manip_action/cancel
  1.type= actionlib_msgs/GoalID
  1.desc= A request to cancel given task.
}
```



##### Action Published Topics



```clearsilver
pub {
  no_header= True
  0.name= /but_arm_manip/manual_arm_manip_action/feedback
  0.type= srs_assisted_arm_navigation_msgs/ManualArmManipActionFeedback
  0.desc= Feedback contains the current state of the task.
  1.name= move_base/status
  1.type= actionlib_msgs/GoalStatusArray
  1.desc= Provides status information on the goals that are sent to the `assisted_arm_navigation` action.
  2.name= /but_arm_manip/manual_arm_manip_action/result
  2.type= srs_assisted_arm_navigation_msgs/ManualArmManipActionResult
  2.desc= Result contains information about task from user (succeeded, failed etc.).
}
```



### Topics, services, parameters



```clearsilver
pub {
  0.name= /but_arm_manip/state
  0.type=srs_assisted_arm_navigation_msgs/AssistedArmNavigationState
  0.desc= A state of arm navigation. 
}
sub {
  0.name= /spacenav/joy
  0.type= sensor_msgs/Joy
  0.desc=  tbd

  1.name= /spacenav/offset
  1.type= geometry_msgs/Vector3
  1.desc=  tbd

  2.name= /spacenav/rot_offset
  2.type= geometry_msgs/Vector3
  2.desc= tbd

}

srv{

  0.name= /but_arm_manip/arm_nav_new
  0.type= srs_assisted_arm_navigation_msgs/ArmNavNew
  0.desc= Called from user interface, when there is a request for new trajectory planning.

  1.name= /but_arm_manip/arm_nav_plan
  1.type= srs_assisted_arm_navigation_msgs/ArmNavPlan
  1.desc= Plan from current position to the goal position.

  2.name= /but_arm_manip/arm_nav_play
  2.type= srs_assisted_arm_navigation_msgs/ArmNavPlay
  2.desc= Visualize trajectory.

  3.name= /but_arm_manip/arm_nav_execute
  3.type= srs_assisted_arm_navigation_msgs/ArmNavExecute
  3.desc= Execute trajectory.

  4.name= /but_arm_manip/arm_nav_reset
  4.type= srs_assisted_arm_navigation_msgs/ArmNavReset
  4.desc= Cancel current planning.

  5.name= /but_arm_manip/arm_nav_success
  5.type= srs_assisted_arm_navigation_msgs/ArmNavSuccess
  5.desc= Task was successful (user pressed "Success" button).

  6.name= /but_arm_manip/arm_nav_failed
  6.type= srs_assisted_arm_navigation_msgs/ArmNavFailed
  6.desc= User was not able to finish given task.

  7.name= /but_arm_manip/arm_nav_refresh
  7.type= srs_assisted_arm_navigation_msgs/ArmNavRefresh
  7.desc= Refresh planning scene.

  8.name= /but_arm_manip/arm_nav_coll_obj
  8.type= srs_assisted_arm_navigation_msgs/ArmNavCollObj
  8.desc= Add bounding box of object to the planning scene.

  9.name= /but_arm_manip/arm_rem_coll_obj
  9.type= srs_assisted_arm_navigation_msgs/ArmNavRemoveCollObjects
  9.desc= Remove all collision objects.

  10.name= /but_arm_manip/arm_nav_set_attached
  10.type= srs_assisted_arm_navigation_msgs/ArmNavSetAttached
  10.desc= Set collision object to be attached.

  12.name= /but_arm_manip/arm_nav_move_palm_link
  12.type= srs_assisted_arm_navigation_msgs/ArmNavMovePalmLink
  12.desc= Move virtual end effector to some absolute position.

  13.name= /but_arm_manip/arm_nav_move_palm_link_rel
  13.type= srs_assisted_arm_navigation_msgs/ArmNavMovePalmLinkRel
  13.desc= Move virtual end effector relatively.

  14.name= /but_arm_manip/arm_nav_switch_aco
  14.type= srs_assisted_arm_navigation_msgs/ArmNavSwitchACO
  14.desc= Enable/disable artificial collision object attached to gripper.

  15.name= /but_arm_manip/arm_nav_repeat
  15.type= srs_assisted_arm_navigation_msgs/ArmNavRepeat
  15.desc= User pressed "Repeat" button (if it was allowed by action).

  16.name= /but_arm_manip/arm_nav_step
  16.type= srs_assisted_arm_navigation_msgs/ArmNavStep
  16.desc= Undo / redo.

  17.name= /but_arm_manip/arm_nav_stop
  17.type= srs_assisted_arm_navigation_msgs/ArmNavStop
  17.desc= Stop execution of trajectory.

}



param {
  0.name=~arm_planning/arm_planning/inflate_bb 
  0.default=`"1.0"`
  0.type= double
  0.desc= Bounding box of each object inserted into planning scene will be inflated by this factor.
  1.name=~arm_planning/world_frame 
  1.default=`"map"`
  1.type= string
  1.desc= Planning will be performed in this coordinate system.

  2.name=~arm_planning/end_eff_link
  2.default=`"sdh_palm_link"`
  2.type= string
  2.desc= End effector link.

  3.name=~arm_planning/joint_controls
  3.default=`"false"`
  3.type= bool
  3.desc= Enable/disable interactive markers for all joints.

  4.name=~arm_planning/make_collision_objects_selectable
  4.default=`"false"`
  4.type= bool
  4.desc= If the object inserted into the planning scene should be selectable or not.

  5.name=~arm_planning/aco/link
  5.default=`"arm_7_link"`
  5.type= string
  5.desc= Artificial collision object (when enabled) will be attached to this link.

  6.name=~arm_planning/aco/default_state
  6.default=`"false"`
  6.type= bool
  6.desc= Default state of the artificial collision object.

  7.name=~spacenav/enable_spacenav
  7.default=`"true"`
  7.type= bool
  7.desc= Enables usage of Space Navigator control.

  8.name=~spacenav/use_rviz_cam
  8.default=`"true"`
  8.type= bool
  8.desc= Enables usage of RVIZ camera position to make control of end effector in ''user perspective''. Camera position must be published as TF transformation. There is plugin for publishing this in [[srs_env_model_ui|srs_env_model_ui]] package.

  9.name=~spacenav/rviz_cam_link
  9.default=`"rviz_cam"`
  9.type= string
  9.desc= TF frame for RVIZ camera.

  10.name=~spacenav/max_val
  10.default=`"350.0"`
  10.type= double
  10.desc= Maximal value for data from Space Navigator. Higher values will be limited.

  11.name=~spacenav/min_val_th
  11.default=`"0.05"`
  11.type= double
  11.desc= Threshold for normalized values (current / max_val). Must be in <0.0, 0.5> range.

  12.name=~spacenav/step
  12.default=`"0.1"`
  12.type= double
  12.desc= Step for changes of end effector interactive marker position.

  13.name=~arm_links
  13.default=`"cob3-3 arm links"`
  13.type= list of strings
  13.desc= List of arm links.

  14.name=~set_planning_scene_diff_name
  14.default=`"environment_server/set_planning_scene_diff"`
  14.type= string
  14.desc= Service for communication with [[planning_environment|Environment Server]]. 

  15.name=~left_ik_name
  15.default=`"cob3_arm_kinematics/get_constraint_aware_ik"`
  15.type= string
  15.desc= Constraint aware IK service.

  16.name=~planner_1_service_name
  16.default=`"ompl_planning/plan_kinematic_path"`
  16.type= string
  16.desc= Planner service name.

  17.name=~trajectory_filter_1_service_name
  17.default=`"trajectory_filter_server/filter_trajectory_with_constraints"`
  17.type= string
  17.desc= Trajectory filter service name.

  18.name=~vis_topic_name
  18.default=`"planning_scene_visualizer_markers"`
  18.type= string
  18.desc= Topic for publishing visualization markers.

  18.name=~vis_topic_name
  18.default=`"planning_scene_visualizer_markers"`
  18.type= string
  18.desc= Topic for publishing visualization markers.

  19.name=~left_ik_link
  19.default=`"arm_7_link"`
  19.type= string
  19.desc= End effector link for which we perform IK.

  20.name=~left_arm_group
  20.default=`"arm"`
  20.type= string
  20.desc= Arm group.

  21.name=~execute_left_trajectory
  21.default=`"arm_controller/follow_joint_trajectory"`
  21.type= string
  21.desc= Arm controller action.


}
```



## Installation

-   install COB stacks from Ubuntu repository or from git (see
    [installation instructions](Robots/Care-O-bot/electric))
-   checkout srs and srs_public git repositories
-   compile srs_assisted_arm_navigation package 

```
rosmake srs_assisted_arm_navigation
```



## Usage

First, please take a look on how to install and use
[user interface](srs_assisted_arm_navigation_ui) for assisted arm
manipulation.

For starting COB simulation, actionlib server use this:


```
roslaunch srs_assisted_arm_navigation but_arm_nav_sim.launch
```

 and then next command to start user interface
(RVIZ): 

```
roslaunch srs_assisted_arm_navigation_ui rviz.launch
```



There is an example of a [rospy](rospy) script which can be used to
"trigger" manipulation task. Run it and operator should be asked for
action by messagebox from RVIZ plugin.



```python
#!/usr/bin/env python
import roslib; roslib.load_manifest('your_package')
import rospy
import actionlib

from srs_assisted_arm_navigation_msgs.msg import *

def main():
    
  rospy.init_node('arm_manip_action_test')
  rospy.loginfo("Node for testing actionlib server")
 
  client = actionlib.SimpleActionClient('/but_arm_manip/manual_arm_manip_action',ManualArmManipAction)
  
  rospy.loginfo("Waiting for server...")
  client.wait_for_server()
  goal = ManualArmManipGoal()
  
  goal.allow_repeat = False
  goal.action = "Move arm to arbitrary position"
  goal.object_name = ""
  
  client.send_goal(goal)

  client.wait_for_result()
  rospy.loginfo("I have result!! :-)")
  
  result = client.get_result()
  
  if result.success:
    rospy.loginfo("Success!")
    
  if result.failed:
    rospy.loginfo("Failed :-(")
  
  rospy.loginfo("Time elapsed: %ss",result.time_elapsed.to_sec())
  
if __name__ == '__main__':
  main()
```



For instructions on how to test SRS scenarios, please see
[srs_arm_navigation_tests](srs_arm_navigation_tests).

## How to adapt it for your robot

-   Generate planning configuration
    [using wizard](arm_navigation/Tutorials/tools/Planning Description Configuration Wizard).
-   TBD\...
