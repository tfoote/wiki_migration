## Nodes



```clearsilver
node.0 {
  name = pose_manager
  desc = The pose manager maintains a library of poses so that clients can move the robot to a given pose by sending the name of the pose as an action goal.
  goal {
    0.name = body_pose
    0.type = naoqi_msgs/BodyPose
    0.desc = Goal containing the name of the pose as a string.
  }
  act_called {
    0.name = joint_trajectory
    0.type = naoqi_msgs/JointTrajectory
    0.desc = Sends the trajectory corresponding to the desired pose to the pose controller
  }
  param {
    0.name = ~xap
    0.desc = File path for the file containing the pose library.
    0.type = string
    1.name = ~poses
    1.desc = Array containing additional poses.
    1.type = list
  }
}
node.1 {
  name = pose_controller
  desc = Provides action servers for controlling the robot's joints by sending joint angles, joint trajectories, or stiffness values.
  goal {
    0.name = joint_angles_action/goal
    0.type = naoqi_msgs/JointAnglesWithSpeedGoal
    0.desc = Send joint angles goal
    1.name = joint_trajectory/goal
    1.type = naoqi_msgs/JointTrajectoryGoal
    1.desc = Send joint trajectory goal
    2.name = joint_stiffness_trajectory/goal
    2.type = naoqi_msgs/JointTrajectoryGoal
    2.desc = Send stiffness trajectory goal
    3.name = body_pose_naoqi/goal
    3.type = naoqi_msgs/BodyPoseWithSpeedGoal
    3.desc = Send body pose goal. This action server is only available if a ALRobotPosture proxy is available.
  }
  param {
    0.name = ~poll_rate
    0.type = float  
    0.default = 0.2
    0.desc = Get poll rate for actionlib (ie. how often to check whether currently running task has been preempted)
    1.name = ~init_stiffness
    1.desc = initial stiffness (defaults to 0 so it doesn't strain the robot when no teleoperation is running), set to 1.0 if you want to control the robot immediately
    1.default = 0.0
  }
  sub {
    0.name = joint_angles
    0.type = naoqi_msgs/JointAnglesWithSpeed
    0.desc = Interpolate the joint angles to the given pose
    1.name = joint_stiffness
    1.type = sensor_msgs/JointState
    1.desc = Set the stiffness for individual joints
  }
  srv {
    0.name = body_stiffness/disable
    0.desc = Turn off all motors. Be careful as the robot might fall.
    0.type = std_srvs/Empty
    1.name = body_stiffness/enable
    1.desc = Turn on all motors.
    1.type = std_srvs/Empty
    2.name = rest
    2.desc = Put the robot in a safe pose and turn off the motors.
    2.type = std_srvs/Empty
    3.name = wakeup
    3.desc = Turn on the motors and go to an initial position.
    3.type = std_srvs/Empty
  }
}
```


