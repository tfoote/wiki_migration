## Overview

The \`nj_escape_crossing\` package implements a navigating jockey for
the Large Maps Framework ([LaMa](Large Maps Framework)) which role is to
drive the robot away from the crossing center, where the robot is
awaited to be when the jockey is started.

This jockey takes an edge descriptor (with associated exit angle
descriptor) to know in which direction to go. The exit angle descriptor
associated with edge n1-n2, from vertex n1 to vertex n2, indicates which
at which angle the robot should orient itself to go to vertex n2 when
starting at vertex n1. This jockey takes a crossing descriptor to know
how far it should travel. But this distance can also be given as
parameter. If the parameter is non-existent or its value is 0, the robot
will travel a distance equal to the crossing radius. It supports the
TRAVERSE action and is DONE when the distance is traveled. As for now,
the jockey is pretty stupid and does not stop before the distance is
traveled (it does not FAIL).

Implemented actions:

-   TRAVERSE: will start driving the robot: first turning into the given
    direction then going forward. The action does not fail. The action
    is done when a certain distance is travelled.
-   STOP: will stop
-   INTERRUPT: the robot stops
-   CONTINUE: nothing will happen (default implementation)

## Usage

### Interaction with the map (created by other jockeys)

  -- --------------------------- -- -------------------- -- ------------------------ --
     \[Getter\]\[/\]\[Setter\]      message type            interface default name   
     Getter                         lama_msgs/Crossing      \"crossing\"             
     Getter                         float64                 \"exit_angle\"           
  -- --------------------------- -- -------------------- -- ------------------------ --

### ROS API

```clearsilver
sub {
   0.name= ~<name>/odometry
   0.type= nav_msgs/Odometry
   0.desc= robot position

   1.name= ~<name>/direction
   1.type= std_msgs/Float32
   1.desc= The direction must be in the same reference frame as ~odometry.  This topic is used only if the requested edge does not exist or if it has no exit angle descriptor.
}
pub {
   0.name= ~<name>/cmd_vel
   0.type= geometry_msgs/Twist
   0.desc= robot set velocity
}
param {
  0.name= ~<name>/kp_v
  0.type= Float
  0.default= 0.05
  0.desc= proportional gain for the linear velocity (s^-1)

  1.name= ~<name>/kp_w
  1.type= Float
  1.default= 0.2
  1.desc= proportional gain for the angular velocity (s^-1)

  2.name= ~<name>/min_linear_velocity
  2.type= Float
  2.default= 0.020
  2.desc= minimum set linear velocity (m.s^-1)

  3.name= ~<name>/min_angular_velocity
  3.type= Float
  3.default= 0.1
  3.desc= minimum set angular velocity (rad.s^-1).

  4.name= ~<name>/escape_distance
  4.type= Float
  4.default= 0.0
  4.desc= distance to travel from crossing center (m). If set to 0, the radius value in the crossing descriptor will be used.

  5.name= ~<name>/crossing_interface_name
  5.type= String
  5.default= "crossing"
  5.desc= name of the map interface for Crossing

  6.name= ~<name>/exit_angle_interface_name
  6.type= String
  6.default= "exit_angle"
  6.desc= name of the map interface for exit angle

  7.name= ~<name>/exit_angle_topic_name
  7.type= String
  7.default= "exit_angle"
  7.desc= name of the optional topic for exit angle (or direction), will only be used if this information is not associated with the edge to traverse
}
```
