The `nj_oa_costmap` package implements a navigating jockey for the
Large Maps Framework ([LaMa](Large Maps Framework)) that drives the
robot while avoiding obstacles. It is based on a local map
([nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)).
The local map has a fixed position relative to the robot but its
orientation is constant in the world reference frame. It is a reactive,
memory-less jockey.

Implemented action:

-   TRAVERSE: go more or less forward depending on obstacle position.
    The action never stops by itself.
-   STOP: stop the robot, sending this action is the only way to stop a
    TRAVERSE action.
-   INTERRUPT: same as STOP
-   CONTINUE: same as TRAVERSE

Moreover, the package provides the class `TwistHandler` that computes
an appropriate
[geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)
from a
[nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)
in order to go as forward as possible while avoiding obstacles.

## Usage

### ROS API



```clearsilver
sub {
   0.name= ~<name>/local_map
   0.type= nav_msgs/OccupancyGrid
   0.desc= local map with fixed position relative to the robot and fixed orientation relative to the world reference frame
}

pub {
  0.name= ~<name>/cmd_vel
  0.type= geometry_msgs/Twist
  0.desc= set velocity
}

param {
  0.name= ~<name>/robot_radius
  0.type= Float
  0.desc= robot radius (m)

  1.name= ~<name>/min_distance
  1.type= Float
  1.default= 2 * robot_radius
  1.desc= if an obstacle is closer than this, turn and don't go forward (m)

  2.name= ~<name>/long_distance
  2.type= Float
  2.default= 5 * robot_radius
  2.desc= if no obstacle within this distance, go straight (m)

  3.name= ~<name>/turnrate_collide
  3.type= Float
  3.default= 0.4
  3.desc= turn rate when obstacle closer than ~min_distance_ (rad/s)

  4.name= ~<name>/max_vel
  4.type= Float
  4.default= 1.0
  4.desc= linear velocity without obstacle (m/s)

  5.name= ~<name>/vel_close_obstacle
  5.type= Float
  5.default= 0.5
  5.desc= linear velocity if obstacle between min_distance and long_distance (m/s)

  6.name= ~<name>/turnrate_factor
  6.type= Float
  6.default= 0.9
  6.desc= if obstacle closer than ~long_distance, turnrate = -turnrate_factor_ * mean(lateral_position_of_obstacle) (rad.m^-1.s^-1).

  7.name= ~<name>/laser_frame
  7.type= String
  7.default= "base_laser_link"
  7.desc= frame_id of the laser scan messages that are used to build the local map.

  8.name= ~<name>/navigating_jockey_server_name
  8.default= node_name + "_server"
  8.type= String
  8.desc= Jockey name
}
```


