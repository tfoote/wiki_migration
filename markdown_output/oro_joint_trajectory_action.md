## Overview

This component act as JointTrajectoryAction server from within OROCOS
controller. After receiving JointTrajectoryAction goal, it checks its
validity then feeds trajectory generator with received points.

## OROCOS API

### Properties



```clearsilver
param {
  no_header= True
  0.name=number_of_joints
  0.type=int
  0.desc=Number of joints used by trajectory generation.
  1.name=jointX_name
  1.type=String
  1.desc=Those properties is used for mapping internal joint number X to joint name used in ROS.
}
```



### Action interface

#### Input ports



```clearsilver
sub {
  no_header= True
  0.name=goal
  0.type=pr2_controllers_msgs/JointTrajectoryActionGoal
  0.desc=The goal describes the trajectory for the robot to follow.
  1.name=cancel
  1.type=actionlib_msgs/GoalID
  1.desc=A request to cancel a specific goal.
}
```



#### Output ports



```clearsilver
pub {
  no_header= True
  0.name=feedback
  0.type=pr2_controllers_msgs/JointTrajectoryActionFeedback
  0.desc=Feedback describing the progress the mechanism is making on following the trajectory.
  1.name=status
  1.type=actionlib_msgs/GoalStatusArray
  1.desc=Provides status information on the goals that are sent to the action.
  2.name=result
  2.type=pr2_controllers_msgs/JointTrajectoryActionResult
  2.desc=empty
}
```



### Trajectory interface

#### Input ports



```clearsilver
sub {
  no_header= True
  0.name=buffer_ready
  0.type=bool
  0.desc=This indicates that the trajectory generator is ready to receive a new point.
}
```



#### Output ports



```clearsilver
pub {
  no_header= True
  0.name=trajectory_point
  0.type=trajectory_mags/JointTrajectoryPoint
  0.desc=New point of trajectory for trajectory generator.
}
```


