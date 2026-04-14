## About

The \`carl_interactive_manipulation\` package provides a backend and
frontend for object manipulation based on interactive markers. It
includes markers to directly control the end-effector pose,
visualization of segmented and recognized objects, and commands to
autonomously pickup specific objects.

## Nodes

```clearsilver
node.0 {
  name = carl_interactive_manipulation
  desc = 'carl_interactive_manipulation' publishes interactive markers that can be used to control the end effector pose, visualize manipulable objects, and issue manipulation commands.
  sub {
    0.name = jaco_arm/joint_states
    0.type = sensor_msgs/JointState
    0.desc = Updates for arm and finger joint states.
  }
  sub {
    1.name = rail_segmentation/segmented_objects_visualization
    1.type = rail_segmentation/SegmentedObjectList
    1.desc = Updates for segmented and recognized objects.
  }
  pub {
    0.name = jaco_arm/cartesian_cmd
    0.type = wpi_jaco_msgs/CartesianCommand
    0.desc = Send Cartesian commands to the arm.
  }
  srv_called {
    0.name = jaco_arm/kinematics/fk
    0.type = wpi_jaco_msgs/JacoFK
    0.desc = Forward kinematics for the arm.
  }
  srv_called {
    1.name = jaco_conversions/quaternion_to_euler
    1.type = wpi_jaco_msgs/QuaternionToEuler
    1.desc = Conversion from quaternion to Euler xyz rotation representations.
  }
  srv_called {
    2.name = rail_pick_and_place/pickup_segmented_object
    2.type = rail_pick_and_place_msgs/PickupSegmentedObject
    2.desc = Initiate autonomous pickup on a segmented object.
  }
  srv_called {
    3.name = rail_segmentation/remove_object
    3.type = rail_segmentation/RemoveObject
    3.desc = Remove an object from the list of segmented objects.
  }
  srv_called {
    4.name = jaco_arm/get_cartesian_position
    4.type = wpi_jaco_msgs/GetCartesianPosition
    4.desc = Read Cartesian position from the arm.
  }
  srv_called {
    5.name = jaco_arm/software_estop
    5.type = wpi_jaco_msgs/EStop
    5.desc = Arm software emergency stop.
  }
  srv_called {
    6.name = jaco_arm/erase_trajectories
    6.type = std_srvs/Empty
    6.desc = Stop any currently running arm trajectories.
  }
  act_called {
    0.name = jaco_arm/manipulation/gripper
    0.type = rail_manipulation_msgs/GripperGoal
    0.desc = Call open and close actions for the gripper.
  }
  act_called {
    1.name = jaco_arm/manipulation/lift
    1.type = rail_manipulation_msgs/LiftGoal
    1.desc = Call object lift action for the arm.
  }
  act_called {
    2.name = carl_moveit_wrapper/common_actions/ready_arm
    2.type = wpi_jaco_msgs/HomeArmGoal
    2.desc = Move the arm to the home position, or to a defined position via the home position.
  }
}
```

### Manipulation Objects

This package visualizes segmented and recognized objects, and provides
menus for interacting with both. Segmented but unrecognized objects will
be shown in red, and recognized objects will be shown in blue, labeled
with their names.

![\|height=\"451\",width=\"670\"](attachment:objects.png)

Selecting the pickup option for an unrecognized object will initiate an
attempt to recognize the object, and upon successful recognition, pick
up the object. Selecting the pickup option for a recognized object will
simply initiate an autonomous pickup attempt. Selecting the remove
option for both recognized and unrecognized objects will remove the
object from the segmented/recognized object list.

## Installation

To install the \`carl_bot\` package, you can install from source with
the following commands:

. ```shell
cd /(your catkin workspace)/src
git clone https://github.com/WPI-RAIL/carl_bot.git
cd ..
catkin_make
catkin_make install
```

## Startup

### Interactive Manipulation Backend

The interactive manipulation backend can be started by running the
carl_interactive_manipulation node, as follows:

. ```
rosrun carl_interactive_manipulation carl_interactive_manipulation
```

The interactive manipulation frontend can be started by launching the
following, which will bring up an rviz interface: .
```
roslaunch carl_interactive_manipulation im_frontend.launch
```
