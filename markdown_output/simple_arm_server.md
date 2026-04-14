\<\<MsgSrvDoc(simple_arm_server)\>\>

## Node API

The \`simple_arm_server\` package contains a single node,
\`simple_arm_server.py\` which offers an action-based interface. This
server can generate joint trajectories for 4 and 5 DOF arms using the
[arm_kinematics](arm_kinematics) package for IK. It transparently
handles the issues of low-dof manipulators being unable to reach all
6-dof poses.

The output of the simple_arm_server uses the same action-based interface
as arm_navigation. The simple_arm_server does not do collision
avoidance, if you are looking for collision avoidance planning please
see [move_arm](move_arm)

### ROS Parameters

```clearsilver
param {
  no_header= True
  0.name = ~arm_dof
  0.type = int
  0.desc = Number of servos in the arm chain between root and tip (not including gripper). 
  0.default = 5
  1.name = ~root_name
  1.type = str
  1.desc = Name of frame that arm is rooted at. 
  1.default = base_link
  2.name = ~tip_name
  2.type = str
  2.desc = Name of frame that gripper tip is at.  
  2.default = gripper_link
  3.name = ~timeout
  3.type = float
  3.desc = Maximum amount of time to wait for IK solution.
  3.default = 5.0
}
```

### Action API

The \`simple_arm_server.py\` node provides an implementation of a
\`SimpleActionServer\` (see [ actionlib documentation](actionlib )),
that takes in goals containing \`simple_arm_server/MoveArmGoal\`
messages. You can communicate with the \`simple_arm_server\` node over
ROS directly, but the recommended way to send goals to
\`simple_arm_server\` if you care about tracking their status is by
using the \`SimpleActionClient\`. Please see
[ actionlib documentation](actionlib ) for more information.

#### Action Subscribed Topics

```clearsilver
sub {
  no_header=True
  0.name = move_arm/goal
  0.type = simple_arm_server/MoveArmGoal
  0.desc = A goal for the `simple_arm_server` to pursue in the world.
  1.name = move_arm/cancel
  1.type= actionlib_msgs/GoalID
  1.desc= A request to cancel a specific goal.
}
```

#### Action Published Topics

```clearsilver
pub {
  no_header= True
  0.name= move_arm/feedback
  0.type= simple_arm_server/MoveArmFeedback
  0.desc= Feedback contains the estimated time to completion 
  1.name= move_arm/status
  1.type= actionlib_msgs/GoalStatusArray
  1.desc= Provides status information on the goals that are sent to the `move_arm` action. 
  2.name= move_arm/result
  2.type= simple_arm_server/MoveArmActionResult
  2.desc= Provides boolean status of success or failure.
}
```

### Other Subscriptions

```clearsilver
sub {
  no_header= True
  0.name = joint_states
  0.type = sensor_msgs/JointStates
  0.desc = Used to seed the IK solver.  
}
```

### Required Services

```clearsilver
srv_called {
  no_header= True
  0.name = arm_kinematics/get_ik
  0.type = kinematics_msgs/GetPositionIK
  0.desc = Used to get IK solution.
  1.name = arm_kinematics/get_ik_solver_info
  1.type = kinematics_msgs/GetKinematicSolverInfo
  1.desc = Used to get info on the IK solver.  
}
```

### Outputs

#### Action Outputs

```clearsilver
pub {
  no_header = True
  1.name = follow_joint_trajectory/goal
  1.type = control_msgs/FollowJointTrajectoryGoal
  1.desc = Output to arm controller.
}
```

```clearsilver
pub {
  1.name = gripper_controller/command
  1.type = std_msgs/Float64
  1.desc = Output command to gripper.
}
```

### Configuring for Your Robot

The simple_arm_server package has a launch file
(launch/arm_server.launch) which can bring up the arm_kinematics package
and the simple_arm_server with the correct parameters. To use this
launch file, and supply it the correct parameters, you would add
something like: ```
<launch>
  <include file="$(find simple_arm_server)/launch/arm_server.launch">
    <arg name="arm_dof" value="4" />
    <arg name="root_name" value="arm_base_link" />
     <arg name="tip_name" value="gripper_link" />
  </include>
</launch>
``` To your robot bringup launch
file, supplying the correct root, tip and dof values for your robot.

### Command Line Usage

The \'\'simple_arm_server_test.py\'\' script allows you to move the arm,
using the server, through the command line:

```
$ simple_arm_server_test.py
usage: simple_arm_server_test.py x y z wrist_pitch [wrist_roll=0.0 wrist_yaw=0.0 frame_id='base_link' duration=5.0]
```

Small 5-DOF arms often have small workspaces. To get a starting point,
you can see where the arm is in relation to the base using:

```
rosrun tf tf_echo base_link gripper_link
```
