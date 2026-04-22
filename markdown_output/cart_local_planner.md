Cart local planner provides a single ros plugin, `cart_local_planner`,
that implements the `base_local_planner` interface expected by
`move_base`. It simply tries to follow the given base path exactly. It
also provides an additional interface for controlling the cart.

## Advertised topics

`articulate_cart_server`/command_twist
([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html))
Commanded twist for the cart reference point

## Subscribed topics

`/move_base_node/SBPLCartPlanner/sbcl_robot_cart_plan`
([cart_pushing_msgs/msg/RobotCartPath](https://docs.ros.org/en/rolling/p/cart_pushing_msgs/msg/RobotCartPath.html))
The planner is expected to publish the full plan (with both base and
cart poses) on this topic. When the plugin receives a global plan from
move_base, it is compared with the recent plans on this topic to find
the corresponding one, and the arm positions are looked up from there.

## TF frames needed

`base_footprint` The base pose `cart` The pose of the cart reference
point

## Main ROS parameters

`cart_pushing/max_vel_{base,cart}_{x,y,theta}` Max velocities for
the base and cart `HolonomicCartPlanner/k_{trans,rot}_{base_cart}`
Gains for the cart and base velocities `cart_pushing/{length,width}`
Cart dimensions `cart_pushing/footprint_{x,y}_offset` The offset of
the reference point of the cart from the corner
