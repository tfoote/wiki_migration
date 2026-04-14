## Overview

This package contains the hardware interface to control the robot. The
[rtai_ros_bridge](rtai_ros_bridge) package from
[rtai_ros_integration](rtai_ros_integration) stack is used to exchange
data with the robot.

## Nodes

```clearsilver
node.0 {
name = biped_serializer
desc = Serialization of data that is sent to the !BipedRobin controller.
sub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Desired velocity for !WheeledRobin (x, theta)
}
pub {
  0.name = data_to_rtai
  0.type = std_msgs/UInt8MultiArray
  0.desc = Serialized data that is sent to the !BipedRobin controller via rtai_ros_bridge.
}
srv {
  0.name = footstep3DInc_srv
  0.type = biped_robin_msgs/StepTarget3DService
  0.desc = Add one step to the step buffer of !BipedRobin (used in walking mode).
  1.name = movePostureCartesian_srv
  1.type = biped_robin_msgs/MovePostureCartesianService
  1.desc = Set the desired cartesian posture for !BipedRobin (used in cartesian posture mode).
  2.name = movePostureJoint_srv
  2.type = biped_robin_msgs/MovePostureJointService
  2.desc = Set the desired joint posture for !BipedRobin (used in joint posture mode).
  3.name = moveGripper_srv
  3.type = biped_robin_msgs/MoveGripperService
  3.desc = Sets the desired speed/force of the gripper of !BipedRobin.
  4.name = acknowledge_srv
  4.type = std_srvs/Empty
  4.desc = Send an error acknowledgement to the !BipedRobin (e.g. after using the emergency stop button or the stop_srv).
  5.name = reference_srv
  5.type = std_srvs/Empty
  5.desc = Used to reference the !BipedRobin (just works in service mode).
  6.name = stop_srv
  6.type = std_srvs/Empty
  6.desc = Send an stop request to the !BipedRobin (before the robot can be moved again the error needs to be acknowledged by acknowledge_srv).
  7.name = resetState_srv
  7.type = std_srvs/Empty
  7.desc = Resets the internal state (joint state) of the robot. Can only be called in idle mode)
  8.name = setMode_srv
  8.type = biped_robin_msgs/SetModeService
  8.desc = Sets the desired mode of the robot (e.g. 0.. idle mode, 1.. home position mode, 2.. walk position mode, 3.. walk mode, 8.. joint posture mode, 9.. cartesian posture mode).
  9.name = setParam_srv
  9.type = biped_robin_msgs/SetParamService
  9.desc = Sets an parameter of !BipedRobin to the desired value.
}
param {
  0.name = par_isRealEnvironment
  0.type = bool
  0.desc = Defines if the !BipedRobin controller is in a simulated mode or controlls the physical robot.
  0.default = false
}
}
node.1 {
name = biped_deserializer
desc =  De-serialization of data that was sent by the !BipedRobin controller to ROS topics.
sub {
  0.name = data_from_rtai
  0.type = std_msgs/UInt8MultiArray
  0.desc = Data the !BipedRobin Controller sent via rtai_ros_bridge.
}
pub {
  1.name = joint_states
  1.type = sensor_msgs/JointState
  1.desc = Joint states of !BipedRobin.
  2.name = bipedRobinGlobalBehaviour
  2.type = biped_robin_msgs/BipedRobinGlobalBehaviour
  2.desc = Current state and behaviour of !BipedRobin
  3.name = stepsLeftInBuffer
  3.type = std_msgs/UInt8
  3.desc = Number of steps left in the step buffer of !BipedRobin. If the buffer is empty the robot stops walking.
}
prov_tf {
  0.from = odom
  0.to = base_link
  0.desc = Transfrom from odom to base_link.
  1.from = base_link
  1.to = center_of_mass
  1.desc = Transfrom from base_link to center_of_mass.
  2.from = base_link
  2.to = gaze
  2.desc = Transfrom from base_link to gaze.
  3.from = base_link
  3.to = l_sole
  3.desc = Transfrom from base_link to l_sole.
  4.from = base_link
  4.to = r_sole
  4.desc = Transfrom from base_link to rl_sole.
  5.from = base_link
  5.to = base_footprint
  5.desc = Transfrom from base_link to base_footprint.
}
}
node.2 {
name = kinect_transform_publisher.py
desc =  Publishes the tranformation from 
sub {
  0.name = cur_tilt_angle
  0.type = std_msgs/Float64
  0.desc = Current angle of the Kinect (e.g. provided by kinect_aux)
}
pub {
  0.name = tilt_angle
  0.type = std_msgs/Float64
  0.desc = Desired angle of the Kinect (e.g. used by kinect_aux)
}
prov_tf {
  0.from = camera_link
  0.to = gaze
  0.desc = Transfrom from camera_link to the gaze frame (Kinect can be rotated, so this transfrom is not static).
}
}
```
