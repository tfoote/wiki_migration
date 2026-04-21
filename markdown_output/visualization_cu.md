This node provides a graphical interface for interaction with the
prairiedog robotic platform. It gives users the ability to visualize the
operating environment, set robot and goal positions, switch between
autonomous and manual control, and manually control the robot via the
keyboard.

------------------------------------------------------------------------

## GUI

![\|height="345px",width="338px"](attachment:prairiedog_gui.png)

### Display

The following is a list of what data is displayed in the GUI:

-   **Map Cost**: light to dark represents safe to obstacle (obstacle
    prob 0 to 1), respectively.
-   **Goal**: Green disk with compass needle indicating orientation.
-   **Path**: Green lines.
-   **Laser Scan Data**: red dots.
-   **Laser Scan Range Exceeded**: blue dots at max range
-   **Robot**: Disk with compass needle indicating orientation. Color
    denotes system state as follows: . **Blue**: normal autonomous mode
    . **Red**: bumper hit, backing up . **Orange**: no path to goal
    exists . **Purple**: manual stop . **Light-Blue**: manual control .
    **Black**: uninitialized state

### Buttons

The GUI buttons control the system as follows:

-   **Autonomous**: The robot moves in autonomous mode, attempting to
    follow the path. The mouse can be used to re-position and scale the
    map (left and right buttons, respectively).
-   **Set Goal**: Use left mouse button to set the goal position and
    orientation (click on position and drag in the direction of
    orientation).
-   **Set Pose**: Use left mouse button to set the robot's position and
    orientation (click on position and drag in the direction of
    orientation).
-   **reload Map**: Explicitly requests the latest map from the map
    server (may be necessary if automatic map updates have been
    dropped). Afterward the robot is switched to Autonomous mode.
-   ** Move Robot**: Allows the user to control the robot with the arrow
    keys: . **Up arrow**: increase forward speed (decrease reverse
    speed) . **Down arrow**: increase reverse speed (decrease forward
    speed). . **left arrow**: increase counter-clockwise rotation
    (decrease clockwise rotation) . **right arrow**: increase clockwise
    rotation (decrease counter-clockwise rotation) . **space-bar**: stop
    all movement.
-   **Res+**: increase display resolution
-   **Res-**: decrease display resolution

Note: the display resolution is only used for visualization purposes and
does not affect the mapper or planner. It is useful when
`visualization_cu` is being bogged down by the drawing requirements
(this is only an issue in complex environments, when
`visualization_cu` is sharing cpu time with the rest of prairiedog).

### Keyboard Shortcuts

Functionality can also be accessed using the keyboard as follows:

-   **arrow keys**: translate the map (Autonomous mode), or drive the
    robot (Move Robot mode)
-   **space-bar**: stop all movement (always), resume path following
    after a stop (Autonomous mode)
-   **-/_**: zoom-in
-   **+/=**: zoom-out
-   **m/M**: switch to Autonomous mode
-   **g/G**: switch to Set Goal mode
-   **p/P**: switch to Set Pose mode
-   **r/R**: reload map (then switch to Autonomous mode)
-   **c/C**: switch to Move Robot mode
-   **\[/{**: increase display resolution
-   **\[/{**: decrease display resolution
-   **0/)**: stop all movement (always), resume path following after a
    stop (Autonomous mode). Same as space-bar

Note: the display resolution is only used for visualization purposes and
does not affect the mapper or planner. It is useful when
`visualization_cu` is being bogged down by the drawing requirements
(this is only an issue in complex environments, when
`visualization_cu` is sharing cpu time with the rest of
`prairiedog`).

------------------------------------------------------------------------

## Using an external computer for visualization

When using a separate computer for visualization, the following
environment variables must be set appropriately:

On Robot Computer:

. ```
export ROS_IP=ip.of.robot.computer
```

On Visualization Computer:

. ```
export ROS_IP=ip.of.visualisation.computer
export ROS_MASTER_URI='http://ip.of.robot.computer:11311/'
```

------------------------------------------------------------------------

## API Documentation

```clearsilver
name = visualization_cu
desc << EOF
`visualization_cu` is a graphical interface written in OpenGL/GLUT that displays information about the CU `prairiedog` platform. It is a light-weight command center, giving users the ability to set robot and goal pose, visualize autonomous behavior by displaying obstacles/robot/goal/paths, and manually control and/or stop the robot.
EOF
param {
  0.name = prairiedog/using_tf
  0.type = bool
  0.desc = When true, the tf ROS package is used to facilitate coordinate transformations.
  0.default = true
  1.name = mapper_cu/global_map_x_offset
  1.type = double
  1.desc = The map coordinate system (`/map_cu`) is this far off of the world coordinate system (`/world_cu`) in the x direction. Units are in meters.
  1.default = 0 (m)
  2.name = mapper_cu/global_map_y_offset
  2.type = double
  2.desc = The map coordinate system (`/map_cu`) is this far off of the world coordinate system (`/world_cu`) in the y direction. Units are in meters.
  2.default = 0 (m)
  3.name = mapper_cu/global_map_theta_offset
  3.type = double
  3.desc = The map coordinate system (`/map_cu`) is this far off of the world coordinate system (`/world_cu`) in the radial direction. Units are in radians.
  3.default = 0 (rad)
  4.name = base_planner_cu/robot_radius
  4.type = double
  4.desc = The radius of the robot in meters.
  4.default = 0.2 (m)
 }
pub {
  0.name = /cu/reset_goal_cu
  0.type = geometry_msgs/PoseStamped
  0.desc = A new robot goal in map coordinates (`/map_cu`).
  1.name = /cu/user_pose_cu
  1.type = geometry_msgs/PoseStamped
  1.desc = A user defined pose, used to manually define the robots starting position with a GUI in map coordinates (`/map_cu`).
  2.name = /cu/user_control_cu
  2.type = geometry_msgs/Pose2D
  2.desc = this is a simple control message for the robot base, x is forward speed and theta is turn in robot coordinates (`/robot_cu`).
  3.name = /cu/user_state_cu
  3.type = std_msgs/Int32
  3.desc << EOF
A flag indicating what the user is doing via the `visualization_cu` node
   . 0 = passive, doing nothing
   . 1 = manual stop
   . 2 = manual control
EOF
 }
sub {
  0.name = /cu/pose_cu
  0.type = geometry_msgs/PoseStamped
  0.desc = The robot's best estimate of where it is, given all pose data, in map coordinates (`/map_cu`).
  1.name = /cu/global_path_cu
  1.type = nav_msgs/Path
  1.desc = This is a global path between robot and goal in map coordinates (`/map_cu`).
  2.name = /cu/goal_cu
  2.type = geometry_msgs/PoseStamped
  2.desc = pose of the goal in map coordinates (`/map_cu`)
  3.name = /cu/laser_scan_cu
  3.type = hokuyo_listener_cu/PointCloudWithOrigin
  3.desc = A list of laser scan hits, along with the pose of the laser scanner when it captured them. Coordinates are in the map coordinate system (`/map_cu` in tf)
  4.name = /cu/map_changes_cu
  4.type = sensor_msgs/PointCloud
  4.desc = Each point in the cloud is a triple (x,y,z). x and y are used to denote which map grid is changed (in map coordinates scaled to resolution) and z is the new cost value of that grid. Note: map updates must be positive and non-zero.
  5.name = /cu/system_state_cu
  5.type = std_msgs/Int32
  5.desc << EOF
 A flag indicating what state `irobot_create_cu` is in:
   . 0 = initial state (havn't recieved enough info to start moving),
   . 1 = planning and moving normally
   . 2 = bumper hit, backing up
   . 3 = no path to goal exists
   . 4 = manual stop
   . 5 = manual control
EOF
  6.name = /cu/system_update_cu
  6.type = std_msgs/Int32
  6.desc << EOF
A flag containing information from the `base_planner_cu` node:
   . 1 = no path to goal exists.
EOF
 }
srv_called {
  0.name = /cu/get_map_cu
  0.type = nav_msgs/GetMap
  0.desc = Provides a map in map coordinates scaled by resolution.
 }
req_tf {
  0.from = /map_cu
  0.to   = /world_cu
  0.desc = transformation between map and world coordinates.
 }
}
```
