## Prerequirements

### Software

The pen_gripper is designed to work together with the portrait_robot
stack and its packages. The easiest way to get access to the
pen_grippers functionality is to install the portrait_robot stack if you
haven't done it so far as shown here [portrait_bot](portrait_bot).

### Hardware

-   a pr2 robot at his highest spine level with hanging arms to reduce
    the collision possibility
-   a surface in front of the robot with a minimal height of 60 cm
-   a pen thick enough for the pr2 gripper and with a minimal length of
    10 cm
-   the pen standing on the surface in gripping range and in range of
    the narrow stereo cameras

## Procedure

NOTE: There is no collision detection during the gripper movement.
Please have an eye at the arms while they move.

If the pen_gripper got a request the following happens:

1\. The arms are taken into a start position to the sides of the pr2 out
of the narrow stereo's field of view. The head is lowered and the
projector for the narrow stereo cameras is started.

2\. While the projector is turned on the pr2 tries to find a pen on the
surface. The robot generates a point cloud from the narrow stereo
cameras. In that cloud it tries to find a surface and the highest point
above the surface is supposed to be the head of the pen.

3\. If no errors occured, the pr2 will try to grip the pen and take it
into an end position at the right side of the robot.

## Usage

You can use the pen_gripper with the complete portrait_robot stack as
shown in the tutorial [portrait_bot/Tutorials](portrait_bot/Tutorials)
to let the pr2 draw a portrait or you can use it with an
[portrait_roboter_msgs/srv/alubsc_node_instr](https://docs.ros.org/en/rolling/p/portrait_roboter_msgs/srv/alubsc_node_instr.html)
message

start the service node and the [ee_cart_imped](ee_cart_imped) controller


```
roslaunch pen_gripper pen_gripper.launch
```

 send a service call (with abort = 0 and an
empty list) to let the pr2 grip a pen 

```
rosservice call /alubsc/node_instr/pen_gripper "0" "[]"
```


