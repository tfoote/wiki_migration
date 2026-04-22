This package provides a ROS node for estimating the cart position.

## Advertised topics

`cart_footprint`
([geometry_msgs/msg/PolygonStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PolygonStamped.html))
A polygon representing the estimated current bounding box for the cart

## Transforms provided

A transform from `cart` to `base_footprint` representing the
estimated cart pose.

## Transforms required

Transforms between `base_footprint` and the gripper frames specified
by the ros parameters.

## Services required

`manipulation_transforms_server/MapEffectorPosesToObject` Used to
transform gripper poses into cart pose

## ROS parameters

`cart_pushing/{width,length}` cart dimensions `{l,r}_gripper_frame`
The frames representing the gripper poses
`cart_pushing/footprint_{x,y}_offset` The offset of the cart
reference point from the corner
