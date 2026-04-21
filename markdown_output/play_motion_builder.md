## play_motion_builder

The Play Motion Builder project is an open-source tool that allows the
design and creation of predefined motions for a robot, as well as an
RQT-based GUI, and a Javascript library to interface with said node.

The code can be accesed at the project's
[ GitHub page](https://github.com/pal-robotics/play_motion_builder )

The motions created with this project are intended to be used with the
`play_motion` (see [ play_motion documentation](play_motion ))
package, and as such the motions are stored in YAML format following
that project's structure. This project (as the `play_motion` project)
makes use of the `move_it` (See
[ MoveIt page](https://moveit.ros.org/ ) for more details) project,
particularly, of the SRDF definition of the robot.

### Usage

In order to use this project the node must be ran on the robot or on a
simulation. The project requires that the `robot_description_param`,
the `semantic_description`, and `extra_joints_param_name` parameters
are properly set.

The node can be run using the command: 

```
rosrun play_motion_builder play_motion_builder_node
```



Once the node is running starting the `build` action needs to be
invoked in order to start creating or editing a motion. This action must
remain active during the editing process.

With the action running the services `edit_motion` and
`change_joints` can be used to operate with the motion being created,
and the `run` action can be used to run it for testing purposes.

Finally, the `store_motion` service can be used to generate the motion
code in YAML format, wither as a string or saved into a given file.

### Action API

The `play_motion_builder_node` node provides an implementation of the
`SimpleActionServer` (see [ actionlib documentation](actionlib )) to
start and stop the creation of a motion. Another implementation of the
`SimpleActionServer` is used to trigger an execution for the motion.
To execute this motions `play_motion` (see
[ play_motion documentation](play_motion )) is used.

#### Action Subscribed Topics



```clearsilver
sub {
  no_header= True
  0.name= ~build/goal
  0.type= play_motion_builder_msgs/BuildMotionActionGoal
  0.desc=A goal to start the motion creation pipeline. A motion name can be given a as a parameter to load an existing motion, or left empty to start a new one.
  1.name= ~build/cancel
  1.type= actionlib_msgs/GoalID
  1.desc= A request to cancel a specific goal for the `build` action.
  2.name= ~run/goal
  2.type= play_motion_builder_msgs/RunMotionActionGoal
  2.desc=A goal to start the execution of the motion. Either the complete motion (with an optional slowing parameter), or a specific Keyframe can be targeted.
  3.name= ~run/cancel
  3.type= actionlib_msgs/GoalID
  3.desc= A request to cancel a specific goal for the `run` action.
  4.name= play_motion/feedback
  4.type= play_motion_msgs/PlayMotionActionFeedback
  4.desc= Feedback is empty for the `play_motion` action.
  5.name= play_motion/status
  5.type= actionlib_msgs/GoalStatusArray
  5.desc= Provides status information on the goals that are sent to the `play_motion` action.
  6.name= play_motion/result
  6.type= play_motion_msgs/PlayMotionActionResult
  6.desc= Result is empty for the `play_motion` action.
}
```



#### Action Published Topics



```clearsilver
pub {
  no_header= True
  0.name= ~build/feedback
  0.type= play_motion_builder_msgs/BuildMotionActionFeedback
  0.desc= Feedback is empty for the `build` action.
  1.name= ~build/status
  1.type= actionlib_msgs/GoalStatusArray
  1.desc= Provides status information on the goals that are sent to the `build` action.
  2.name= ~build/result
  2.type= play_motion_builder_msgs/BuildMotionActionResult
  2.desc= Result returns `ok=True` if no issues happened during the creation, otherwise a `message` is returned with more information.
  3.name= ~run/feedback
  3.type= play_motion_builder_msgs/BuildMotionActionFeedback
  3.desc= Feedback is empty for the `run` action.
  4.name= ~run/status
  4.type= actionlib_msgs/GoalStatusArray
  4.desc= Provides status information on the goals that are sent to the `run` action.
  5.name= ~run/result
  5.type= play_motion_builder_msgs/BuildMotionActionResult
  5.desc= Result is empty for the `run` action.
  2.name= play_motion/goal
  2.type= play_motion_msgs/PlayMotionActionGoal
  2.desc=Play Motion goals are sent to execute the motion being created.
  3.name= play_motion/cancel
  3.type= actionlib_msgs/GoalID
  3.desc= A request to cancel a specific goal for the `play_motion` action.
}
```





```clearsilver
sub {
  0.name= joint_states
  0.type= sensor_msgs/JointState
  0.desc= Used by the `play_motion_builder` node to track the current joint configuration of the robot.
}
srv{
  0.name= ~change_joints
  0.type= play_motion_builder_msgs/ChangeJoints
  0.desc= Allows an external user to change the joints that will be controlled by this motion. Via this service the user can add or remove joints that do not belong to any group, or change the used group.
  1.name= ~edit_motion
  1.type= play_motion_builder_msgs/EditMotion
  1.desc= Allows an external user to modify the parameters of the motion being created.
  2.name= ~list_joint_groups
  2.type= play_motion_builder_msgs/ListJointGroups
  2.desc= Allows an external user to ask for the list of available groups and joints not belonging to any group.
  3.name= ~store_motion
  3.type= play_motion_builder_msgs/StoreMotion
  3.desc= Allows an external user to store the motion in `play_motion` compatible format, either to a file or to be returned as a `string`.
}
param {
  0.name=~robot_description_param 
  0.default=`"/robot_description"`
  0.type= string
  0.desc= The name of the parameter containing the URDF description of the robot. 
  1.name=~semantic_description 
  1.default=`"/robot_description_semantic"`
  1.type= string
  1.desc= The name of the parameter containing the semantic description (SRDF, see [[http://docs.ros.org/kinetic/api/moveit_tutorials/html/doc/urdf_srdf/urdf_srdf_tutorial.html?highlight=semantic#srdf | SRDF on move_it documentation]]) of the robot. 
  2.name=~extra_joints_param_name 
  2.default=`"/play_motion/approach_planner/exclude_from_planning_joints"`
  2.type= string[]
  2.desc= A list of joints that do not belong to any group in the SRDF. 
}
```



## rqt_play_motion_builder

The `rqt_play_motion_builder` package provides an RQT-based (See
[ RQT documentation](rqt )) frontend that simplifies the use of the
`play_motion_builder` node.

The GUI can be started by running: 

```
rosrun rqt_play_motion_builder rqt_play_motion_builder
```

 on a system
in which the `play_motion_builder_node` is running.

## play_motion_builder_js

A Javascript library has been implemented, based on roslibjs (See
[ roslibjs documentation](roslibjs )) to integrate the
`play_motion_builder` package in an HTML-based environment. This
library contains a simplified wrapper around the functionalities and
usage of the `play_motion_builder_node`.

In addition, a ready-to-deploy HTML frontend for the
`play_motion_builder` has been developed, which can be used as is, or
as an implementation example.
