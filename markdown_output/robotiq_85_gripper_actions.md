## About

The `robotiq_85_gripper_actions` package contains ROS actionlib
implementations of common gripper actions including executing a
control_msgs gripper command, closing or opening the gripper until
contact is made, and verifying whether the gripper is holding something.

## Nodes



```clearsilver
node.0 {
  name = gripper_actions
  desc = Action server implementations of common gripper actions.
  pub {
    0.name = /gripper/cmd
    0.type = robotiq_85_msgs/GripperCmd
    0.desc = Send commands to the gripper. The topic name can be changed by setting the `gripper_command_topic` parameter.
  }
  sub {
    0.name = /gripper/stat
    0.type = robotiq_85_msgs/GripperStat
    0.desc = Gripper status information. The topic name can be changed by setting the `gripper_status_topic` parameter.
  }
  goal {
    0.name = gripper_command/goal
    0.type = control_msgs/GripperCommandGoal
    0.desc = Execute a control_msgs gripper command.
    1.name = gripper_manipulation/goal
    1.type = rail_manipulation_msgs/GripperGoal
    1.desc = Fully close or open the gripper until sufficient contact is made.
    2.name = verify_grasp/goal
    2.type = rail_manipulation_msgs/VerifyGraspGoal
    2.desc = Request verification of whether or not the gripper is holding something.
  }
  feedback {
    0.name = gripper_command/feedback
    0.type = control_msgs/GripperCommandFeedback
    0.desc = Feedback for a control_msgs gripper command.
    1.name = gripper_manipulation/feedback
    1.type = rail_manipulation_msgs/GripperFeedback
    1.desc = Feedback while the gripper is fully opening or closing.
    2.name = verify_grasp/feedback
    2.type = rail_manipulation_msgs/VerifyGraspFeedback
    2.desc = Unused.
  }
  result {
    0.name = gripper_command/result
    0.type = control_msgs/GripperCommandResult
    0.desc = Result of a control_msgs gripper command.
    1.name = gripper_manipulation/result
    1.type = rail_manipulation_msgs/GripperResult
    1.desc = Result of fully closing or opening the gripper.
    2.name = verify_grasp/result
    2.type = rail_manipulation_msgs/VerifyGraspResult
    2.desc = Confirmation of whether or not the gripper is holding something.
  }
  param {
    0.name = gripper_command_topic
    0.type = string
    0.desc = Set the topic for publishing commands to the gripper.
    0.default = "/gripper/cmd"
    1.name = gripper_status_topic
    1.type = string
    1.desc = Set the topic for reading the current gripper status.
    1.default = "/gripper/stat"
  }
}
```



## Installation

To install the `robotiq_85_gripper_actions` package, follow the steps
below:

1\. `robotiq_85_gripper_actions` assumes you are using Stanley
Innovation's `robotiq_85_gripper` package to run the arm. If you do
not already have the package installed, you can get it from the Stanley
Innovation github repository: 

```shell
cd /(your catkin workspace)/src
git clone https://github.com/StanleyInnovation/robotiq_85_gripper.git
```



2\. Install `robotiq_85_gripper_actions` from source with the
following commands: 

```shell
cd /(your catkin workspace)/src
git clone https://github.com/GT-RAIL/remote_manipulation_markers.git
cd ..
catkin_make
catkin_make install
```



## Startup

This package contains a single ros node. Run it with the following,
adding any parameters as necessary:

. 

```
rosrun robotiq_85_gripper_actions gripper_actions
```


