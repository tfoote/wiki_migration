The package [ipa_kuka_rsi](ipa_kuka_rsi) implements a ROS driver for the
Kuka RSI XML protocol to control joint and cartesian movements.

## Example launch file

An example to start the driver is given by: ```
roslaunch ipa_kuka_rsi test_driver.launch
```

## Configuration on KR16

To enable the arm to communicate with ROS driver the machting KUKA Robot
Language script has to be started. All necessary files are stored in
\"common/KUKA\". Copy the configuraiton files:

-   RSI_UniversalEthernetConfig.xml
-   RSI_UniversalEthernet.rsi
-   RSI_UniversalEthernet.rsi.diagram
-   RSI_UniversalEthernet.rsi.xml to
    \"C:\\KRC\\Roboter\\Config\\User\\Common\\SensorInterface\" on your
    KR16 arm. Use \"RSI_UniversalEthernet.src\" to start the script on
    the arm which uses the other configuration files and enables RSI
    communication.

## How to use the driver?

Please refer to the test scripts in \"ros/test\". The test scripts are
simple examples of the joint or cartesian control with the action
server.

## ROS API

The [ipa_kuka_rsi](ipa_kuka_rsi) package provides both, a joint based
and a cartesian movement.

```clearsilver

goal{
}

result{
}

feedback{
}

sub{
 0.name = joint_command
 0.type = trajectory_msgs/JointTrajectoryPoint
 0.desc = Receives single joint command.

 1.name = joint_path_command
 1.type = trajectory_msgs/JointTrajectory
 1.desc = Receives a trajectory.
}

pub{
 0.name = diagnostics
 0.type = diagnostic_msgs/DiagnosticArray
 0.desc = Publishes diagnostics messages of the arm.

 1.name = joint_states
 1.type = sensor_msgs/JointState
 1.desc = Publishes the joint states of the arm in rad.
}

srv{
  0.name = init
  0.type = cob_srvs/Trigger
  0.desc = Initializes RSI connection.

  1.name = recover
  1.type = cob_srvs/Trigger
  1.desc = Recovers RSI connection (not implemented).

  2.name = stop
  2.type = cob_srvs/Trigger
  2.desc = Stops movement.

  2.name = motion_mode
  2.type = cob_srvs/SetOperationMode
  2.desc = Switches between cartesian and joint based movement.
}

param{
 0.name = ~initialized
 0.type = bool
 0.default = false
 0.desc = If set to true, the driver initializes automatically (testing purpose).

 1.name = ~frequency
 1.type = int
 1.default = 30
 1.desc = Frequency to publish joint states and diagnostics, as well as for controller.

 2.name = ~joint_names
 2.type = list of strings
 2.desc = A list of names for each joint.

 3.name = ~joint_limits
 3.type = list of of list of float
 3.desc =  Max. and min. limits for each joint in rad, e.g. [ [-1,1], [-2,2] ]

 4.name = ~tolerance
 4.type = list of float
 4.desc =  Tolerance in rad when goal counts as reached

 5.name = ~max_velocity
 5.type = float
 5.default = 0.1
 5.desc = Max. velocity for joint movement

 6.name = ~RSI_joint_name
 6.type = string
 6.default = ASPos
 6.desc = Name of the RSI property for setting joint angles.

 7.name = ~RSI_cart_name
 7.type = string
 7.default = RSol
 7.desc = Name of the RSI property for setting cart. pose.

 8.name = ~tip_link
 8.type = string
 8.desc = Link name of tip of the arm

 9.name = ~base_link_
 9.type = string
 9.desc = Link name of the base of the arm

 10.name = ~config
 10.type = string
 10.default = 1
 10.desc = Filename of the ERC configuration file which is shared between driver and Kuka arm.

 11.name = ~mode_motion
 11.type = string
 11.default = joint
 11.desc = Sets the desired motion mode at startup. Possible values are: joint, cartesian
}

req_tf{
  0.from = ~base_link
  0.to   = "frame_id of goal"
  0.desc = description of transform
}

prov_tf{
}
```

## Action API

The \`ipa_kuka_rsi\` node provides an implementation of two
\`SimpleActionServer\` (see [ actionlib documentation](actionlib )), for
movement of joint based trajectories or cartesian trajectories.

##### Action Subscribed Topics

```clearsilver
sub {
  no_header= True

  0.name= follow_joint_trajectory/goal
  0.type= control_msgs/FollowJointTrajectoryActionGoal
  0.desc= Follow a trajectory (joint).

  1.name= move_cartesian/goal
  1.type= moveit_msgs/MoveGroupActionGoal
  1.desc= Move to a pose (cart.) by filling in the goal constraint of position and orientation with a correct `link_name` (same as `tip_link`).
}
```

##### Action Published Topics

```clearsilver
pub {
  no_header= True

  0.name= follow_joint_trajectory/feedback
  0.type= control_msgs/FollowJointTrajectoryActionFeedback
  0.desc= Feedback contains the current joint position and error to the desired joint position in rad.

  1.name= follow_joint_trajectory/result
  1.type= control_msgs/FollowJointTrajectoryActionResult
  1.desc= Result of the movement.

  2.name= move_cartesian/result
  2.type= moveit_msgs/MoveGroupActionResult
  2.desc= Result of the movement.
}
```

## Dynamic Reconfigure

Some parameters such as frequency, motion mode and more can be
configured by dynamic reconfigure.

## How to use the RSI communication layer for your own software

```cplusplus
#include <ipa_kuka_rsi/rsi_server.h>

RSI::RSI_Server rsi("filename to ERC configuration");

if(rsi.received_something())
  ROS_INFO("connection established!");

double value;
//the method checks the variable type and existence!
bool found = rsi.get("SomeNameFromERC", value);
if(!found)
  ROS_INFO("could not read the variable");

//the method checks the variable type and existence!
bool ok = rsi.set("SomeNameFromERC", 42.37);
if(!ok)
  ROS_INFO("could not set the variable");
```
