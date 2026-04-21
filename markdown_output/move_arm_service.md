

```wiki
/!\ Work in progress.
```



## Overview

The move_arm_service package provides service wrappers around the
[ move_arm action](move_arm ) and the
[ interpolated_ik_motion_planner service](interpolated_ik_motion_planner ).
These services allow the user to calculate and move the PR2 arm along
collision-free trajectories by only specifying
<<MsgLink(geometry_msgs/PoseStamped)>>s rather than the full
<<MsgLink(motion_planning_msgs/MotionPlanRequest)>> message required
by the original action and service.

## ROS API

### Services offered



```clearsilver
srv {
    0.name = move_arm_to_pose
    0.type = move_arm_service/MoveArm
    0.desc = A wrapper around the move_arm action that calculates and moves the arm to a pose goal collision free. 
    1.name = run_interpolated_ik
    1.type = move_arm_service/InterpolatedIK
    1.desc = A wrapper around the interpolated_ik_motion_planner that calculates moves the arm between a starting and ending pose using a collision-free interpolated IK trajectory.
    }
```



### Services required

You must have the [move_arm](move_arm) action AND the
[joint_trajectory_action](joint_trajectory_action) running and all
services necessary for those. In addition, the following services are
required:



```clearsilver
 srv{
    0.name = r/l_interpolated_ik_motion_plan
    0.type = motion_planning_msgs/GetMotionPlan
    0.desc = These services calculate collision-free interpolated IK plans for the right and left arms.
    1.name = get_robot_state
    1.type = planning_environment_msgs/GetRobotState
    1.desc = This services allows move_arm to get the complete state of the robot. This message contains information about the joint positions of all the (real) joints on the robot.
```



## Usage

[Youtube](https://www.youtube.com/watch?v=QBLN7bywr_k)

In the video above, the PR2 uses the move_arm service to position its
hand in front of the cabinet handle and then the interpolated IK service
to grasp the handle.

For examples of how to use the services, see the
[tutorials](move_arm_service/Tutorials).
