This package contains two main ROS nodes and two supporting scripts..

## articulate_cart_server.py

This is the main node for performing articulation of a cart using both
arms on the PR2.

### Subscribed topics

`cart_pushing/ready_pose_achieved` (<<MsgLink(roslib/Header)>>)
Once the base achieves a ready pose, in which the robot's arms are in
the position corresponding to the cart being at its initial position,
with grippers open, a message will be sent on this topic (at a fixed
rate).

`command_twist` (<<MsgLink(geometry_msgs/TwistStamped)>>) The
desired twist for the reference point on the cart, relative to the
`base_footprint` frame

### Published topics

`/r_cart/command_pose`, `/l_cart/command_pose`
(<<MsgLink(geometry_msgs/PoseStamped)>>) Desired poses for the left
and right gripper tool frames are sent on these topics
`/r_cart/command_posture`, `/l_cart/command_posture`
(<<MsgLink(std_msg/Float64MultiArray)>>) Since there is a degree of
freedom remaining in the arm after specifying the gripper pose, we send
a desired posture on this topic `invalid_pose`
(<<MsgLink(std_msgs/Empty)>>) This is a debugging topic, on which a
message is sent on this topic whenever a pose is requested that is
outside the workspace bounds for the cart

### Expected services

`manipulation_transforms_server/LoadInitialTransforms`
(<<SrvLink(manipulation_transforms/LoadInitialTransforms)>>) Used to
tell the manipulation transforms server that the current pose is the one
at which the cart is at its initial position
`manipulation_transforms_server/MapObjectPoseToEffectors`
(<<SrvLink(manipulation_transforms/MapObjectPoseToEffectors)>>) Used
to get the effector poses corresponding to a desired cart pose

### TF frames used

`base_footprint` Used as the base position and the reference for the
cart `l_gripper_tool_frame`, `r_gripper_tool_frame` Used as the
locations of the grippers

### Command line parameters

`-g` If specified, the initial pose of the robot (once the
`ready_pose_achieved` message is received) is used as the reference
position. If not, the reference position is read from the parameter
server.

### ROS parameters

`cart_pushing/{x,y,t}_{min,max}` Workspace bounds for the cart pose
`cart_pushing/init_pose/position` The initial position of the cart
relative to the base; specified as `\[x, y, z\]`
`cart_pushing/init_pose/orientation` The initial orientation of the
cart relative to the base; specified as `\[x, y, z, w\]`

## fake_articulate_cart_server.py

This is for use in simulators in which gripper frames are not available.
It provides the interface of `articulate_cart_server.py`.
Additionally, it publishes transforms between `base_footprint` and
`l_gripper_tool_frame`/`r_gripper_tool_frame` corresponding to the
commands it receives on `command_twist`.

## close_grippers.py

Once a message is received on `move_base/goal`, keeps the grippers
closed by sending commands to
`{l,r}_gripper_controller/gripper_action`.

## switch_controllers.py

Once a message is received on `cart_pushing/ready_pose_achieved`,
disables the `{l,r}_arm_controller` controllers and enables
`{l,r}_cart`. Switches the controllers back before exiting.
