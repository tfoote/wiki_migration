## Overview

Assisted grasping has been developed to allow safe and robust grasping
of unknown or unrecognized objects by SDH gripper equipped with tactile
sensors. It has separated API definition (actionlib interface), code and
[GUI in form of RVIZ plugin](srs_assisted_grasping_ui).

When calling grasp action there is possibility to specify target
configuration (angles) for all joints of the gripper, grasp duration and
maximum forces for all tactile pads. Then, for each joint, velocities
with acceleration and deceleration ramps are calculated in a way, that
all joints will reach target configuration at the same time. If the
measured force on a pad will exceed requested maximal force, movement of
a corresponding joint will be stopped. With different target
configurations and appropriate forces, a wide range of objects can be
grasped.

Assisted grasping package also offers node for preprocessing of tactile
data by median and Gaussian filter with configurable parameters and node
for simulation of velocity mode of SDH.

## Grasping node

### Topics, parameters



```clearsilver

sub {
  0.name= tact_in
  0.type= schunk_sdh/TactileSensor
  0.desc=  Data for tactile feedback.

  1.name= state_in
  1.type= pr2_controllers_msgs/JointTrajectoryControllerState
  1.desc=  Data for position feedback.

}

pub {
  0.name= velocity_out
  0.type= brics_actuator/JointVelocities
  0.desc= Velocity commands.
}

param {
  0.name=~max_force
  0.default=`"1000.0"`
  0.type= double
  0.desc=Maximal allowed force. Higher values will be limited to this value.

  1.name=~max_velocity
  1.default=`"1.5"`
  1.type= double
  1.desc=Maximal velocity (rad/s).

  2.name=~a_ramp
  2.default=`"10.0"`
  2.type= double
  2.desc=Length of acceleration ramp in percents of whole trajectory.

  3.name=~d_ramp
  3.default=`"20.0"`
  3.type= double
  3.desc=Length of deceleration ramp in percents of whole trajectory.

  4.name=~rate
  4.default=`"20.0"`
  4.type= double
  4.desc= Rate of internal controller. Also commands are published at this rate.
```



Node also requires list of joints with some additional information. This
can be done easily in YAML file:



```
joints:
 -
  joint: sdh_knuckle_joint
  has_tactile_pad: false
  static: true
 -  
  joint: sdh_thumb_2_joint
  has_tactile_pad: true  
  static: false
 -  
  joint: sdh_thumb_3_joint
  has_tactile_pad: true
  static: false
 -  
  joint: sdh_finger_12_joint
  has_tactile_pad: true
  static: false
 -  
  joint: sdh_finger_13_joint
  has_tactile_pad: true
  static: false
 -  
  joint: sdh_finger_22_joint
  has_tactile_pad: true
  static: false
 -  
  joint: sdh_finger_23_joint
  has_tactile_pad: true
  static: false
```



### Actionlib API

##### Action Subscribed Topics



```clearsilver
sub {
  no_header= True
  0.name= /reactive_grasping_action/goal
  0.type= srs_assisted_grasping_msgs/ReactiveGraspingActionGoal
  0.desc= Target configuration of joints, maximal allowed force for each tactile pad and time to reach target configuration.

  1.name= /reactive_grasping_action/cancel
  1.type= actionlib_msgs/GoalID
  1.desc= A request to cancel given goal.
}
```



##### Action Published Topics



```clearsilver
pub {
  no_header= True
  0.name= /reactive_grasping_action/feedback
  0.type= srs_assisted_grasping_msgs/ReactiveGraspingActionFeedback
  0.desc= Feedback is empty.

  1.name= /reactive_grasping_action/status
  1.type= actionlib_msgs/GoalStatusArray
  1.desc= Status.

  2.name= /reactive_grasping_action/result
  2.type= srs_assisted_grasping_msgs/ReactiveGraspingActionResult
  2.desc= Current joint values, forces and real time to stop for all joints.
}
```



## Tactile filter

TBD

## Simulated velocity mode

TBD
