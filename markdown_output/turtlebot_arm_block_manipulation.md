## Documentation

This
[Tutorial](turtlebot_block_manipulation/Tutorials/TurtleBotBlockManipulationDemo)
will walk you through running this demo on your own !TurtleBot. <!>
*The tutorial is for the fuerte (pre-moveit) version of this package, so
be careful and flexible when following it!. Trust this page (already
updated) in case of contradiction.*

## Video

[Youtube](https://www.youtube.com/watch?v=UgIx91QrK0c)

## Requirements

This package requires almost all the others on
[turtlebot_arm](turtlebot_arm) stack. In particular, `arm.launch` from
the [turtlebot_arm_bringup](turtlebot_arm_bringup) package and
`planning_context.launch` and `move_group.launch` from
[turtlebot_arm_moveit_config](turtlebot_arm_moveit_config) have to be
running. See the `block_manipulation_moveit.launch` launch file for more
details.

Additionally, it requires an external kinect to be running and
calibrated to the robot. Refer to
[turtlebot_arm_kinect_calibration](turtlebot_arm_kinect_calibration)
package to learn how to calibrate your camera.

## Files

`demo/block_manipulation_moveit.launch` Brings up everything necessary
to operate the arm with MoveIt!.

`demo/block_manipulation_demo.launch` Brings up everything necessary to
run the block manipulation demo.

`launch/block_manipulation.launch` Brings up the 3 action servers
necessary to run the block manipulation demo.

## Nodes



```clearsilver
name = interactive_manipulation_action_server
desc = Provides an action-based interactive marker server for prompting the user to move blocks around. Requires a goal specifying where the the blocks are, and publishes a result containing a start pose and end pose.
sub {
  0.name = /turtlebot_blocks
  0.type = geometry_msgs/PoseArray
  0.desc = Topic to listen for blocks publications on. These topics are used in addition to the information contained in the goal.
}
pub {
  0.name = /pick_and_place
  0.type = geometry_msgs/PoseArray
  0.desc = Topic to publish the resulting pick-and-place grasp on. These topics are used in addition to the information contained in the result.
}
param {
  0.name = ~bump_size
  0.type = double
  0.desc = The amount (in meters) to bump the result by in the z dimension.
  0.default = 0.005
}
```





```clearsilver
name = block_detection_action_server
desc = Detects blocks of a certain size on a flat surface, given from an action goal.
sub {
  0.name = /camera/depth_registered/points
  0.type = sensor_msgs/PointCloud2
  0.desc = Point clouds from which to detect blocks.
}
pub {
  0.name = /turtlebot_blocks
  0.type = geometry_msgs/PoseArray
  0.desc = A pose array containing the poses of all blocks detected.

  1.name = block_output
  1.type = sensor_msgs/PointCloud2
  1.desc = A message sent for debugging, showing the filtered point cloud.
}
req_tf {
  0.from = pointcloud frame
  0.to   = arm_link (from goal)
  0.desc = Before the block detector performs any operation on the point cloud, it transforms it to the arm_link frame provided by the goal.
}
```





```clearsilver
name = pick_and_place_action_server
desc = Interfaces with MoveIt! for the !TurtleBot arm to move an object from the start pose to the end pose.
```



## Actions

### BlockDetection.action



```
#goal definition
string frame
float32 table_height
float32 block_size
---
#result definition
geometry_msgs/PoseArray blocks
---
#feedback
```



### InteractiveBlockManipulation.action



```
#goal definition
string frame
float32 block_size
---
#result definition
geometry_msgs/Pose pickup_pose
geometry_msgs/Pose place_pose
---
#feedback
```



### PickAndPlace.action



```
#goal definition
string frame
float32 z_up
float32 gripper_open
float32 gripper_closed
geometry_msgs/Pose pickup_pose
geometry_msgs/Pose place_pose
string topic
---
#result definition
---
#feedback
```


