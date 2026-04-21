## About

The `carl_action_executor` package contains nodes to manage and
execute a sequence of actions ont he CARL robot. The actions are stored
and executed in a queue, and will report common failures to facilitate
plan repair. Examples of actions include base navigation, object
recognition, and pick-and-place.

## Nodes



```clearsilver
node.0 {
  name = carl_action_executor
  desc = 'carl_action_executor' stores and executes the action queue.
  sub {
    0.name = object_recognition_listener/recognized_objects
    0.type = rail_manipulation_msgs/SegmentedObjectList
    0.desc = Recognized objects topic.
  }
  srv {
    0.name = carl_action_executor/add_action
    0.type = carl_action_executor/AddAction
    0.desc = Add an action to the end of the action queue.
    1.name = carl_action_executor/clear_action_list
    1.type = std_srvs/Empty
    1.desc = Clear all actions in the action list.
    2.name = carl_action_executor/get_action_list
    2.type = carl_action_executor/GetActionList
    2.desc = Return the current action list.
    3.name = carl_action_executor/insert_action
    3.type = carl_action_executor/InsertAction
    3.desc = Insert an action into the action list at a specified index.
    4.name = carl_action_executor/remove_action
    4.type = carl_action_executor/RemoveAction
    4.desc = Remove an action from the action list at a specified index.
  }
  srv_called {
    0.name = rail_segmentation/segment
    0.type = std_srvs/Empty
    0.desc = Tabletop object segmentation service.
    1.name = asus_controller/look_at_frame
    1.type = carl_dynamixel/LookAtFrame
    1.desc = Camera look at tf frame service.
  }
  goal {
    0.name = carl_action_executor/execute/goal
    0.type = carl_action_executor/ExecuteGoal
    0.desc = Execute either the first action on the queue or the entire queue.
  }
  feedback {
    0.name = carl_action_executor/execute/feedback
    0.type = carl_action_executor/ExecuteFeedback
    0.desc = The current executing action and the number of actions remaining in the queue.
  }
  result {
    0.name = carl_action_executor/execute/result
    0.type = carl_action_executor/ExecuteResult
    0.desc = Action execution result, including success, an error code on failure, and the failed action on failure.
  }
  act_called {
    0.name = move_base
    0.type = move_base_msgs/MoveBaseAction
    0.desc = Base navigation to a pose.
    1.name = move_carl
    1.type = carl_navigation/MoveCarlAction
    1.desc = Base navigation to a pre-defined named location.
    2.name = carl_moveit_wrapper/common_actions/arm_action
    2.type = carl_moveit/ArmAction
    2.desc = Pre-defined arm movement (e.g. home, retract).
    3.name = carl_moveit_wrapper/common_actions/pickup
    3.type = carl_moveit/PickupAction
    3.desc = Object pickup.
    4.name = carl_moveit_wrapper/common_actions/store
    4.type = carl_moveit/StoreAction
    4.desc = Object storing.
  }
}
```



## Actions Supported

Actions are specified using the `carl_action_executor/GeneralAction`
message type. The message defines a set of supported action types, a set
of common error codes, and a variety of input data whose use is
determined by the action type. Action types and explanations of their
input are as follows:

*Navigate* - plan and move the robot base to a specified location.

-   nav_pose - a pose goal for navigation; this is the default for
    specifying a navigate action.
-   nav_location - a location as specified by the
    [ rail_lab_location_server](carl_navigation ), used only if nav_pose
    is unspecified.

*Ready Arm* - plan and move the arm to the ready position.

-   No further input is used.

*Retract Arm* - plan and move the arm to the retracted position.

-   No further input is used.

*Pickup* - pick up a recognized object, or perform a pick up action at a
specified pose.

-   object_name - name of the object to be picked up, this is the
    default for specifying a pickup action.
-   manipulaiton_pose - end-effector pose at which to perform a pickup
    action, used only if object_name is unspecified.

*Store* - store an object in a specified location.

-   manipulation_pose - end-effector pose at which to release the
    object.

*Segment* - perform tabletop segmentation.

-   surface_frame - (optional) name of the frame to look at before
    segmentation.

*Recognize* - perform tabletop segmentation and object recognition.

-   surface_frame - (optional) name of the frame to look at before
    segmentation and recognition.

## Installation

To install the `carl_action_executor` package, you can install from
source with the following commands: . 

```shell
cd /(your catkin workspace)/src
git clone https://github.com/WPI-RAIL/carl_action_executor.git
cd ..
catkin_make
catkin_make install
```



## Startup

The `carl_action_executor` can be started by simply running the node:

. 

```
rosrun carl_action_executor carl_action_executor
```


