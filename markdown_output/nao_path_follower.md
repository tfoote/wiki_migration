## Node API

```clearsilver
node.0 {
  name = nao_path_follower
  desc = Make Nao follow a given trajectory.
  pub {
    0.name = cmd_pose
    0.type = geometry_msgs/Pose2D
    0.desc = Command to the pose controller (only if the `use_vel_ctrl` parameter is set to `False`)
    1.name = cmd_vel
    1.type = geometry_msgs/Twist
    1.desc = Command to the velocity controller (only if the `use_vel_ctrl` parameter is set to `True`)
    2.name = nao_path_follower/target_pose
    2.type = geometry_msgs/PoseStamped
    2.desc = ...
    3.name = walk_path/goal
    3.type = naoqi_msgs/FollowPathActionGoal
    3.desc = ...
    4.name = walk_target/goal
    4.type = move_base_msgs/MoveBaseActionGoal
    4.desc = ...
  }
  sub {
    0.name = foot_contact
    0.type = std_msgs/Bool
    0.desc = `True` = robot currently has foot contact with the ground.
  }
  param {
    0.name = base_frame_id
    0.type = string
    0.desc = Base frame of the robot.
    0.default = base_footprint

    1.name = controller_frequency
    1.type = float
    1.desc = Desired frequency for controller loop in Hz.
    1.default = 10.0

    2.name = target_distance_threshold
    2.type = float
    2.desc = Maximum linear deviation to reach target point.
    2.default = 0.05

    3.name = target_angle_threshold
    3.type = float
    3.desc = Maximum angular deviation to reach target orientation.
    3.default = rad(5 degrees)

    4.name = waypoint_distance_threshold
    4.type = float
    4.desc = Maximum linear deviation to switch to next waypoint on path
    4.default = 0.05

    5.name = waypoint_angle_threshold
    5.type = float
    5.desc = Maximum angular deviation to switch to next waypoint on path
    5.default = rad(45 degrees)

    6.name = max_vel_x
    6.type = float
    6.desc = Maximum fraction of forward velocity for velocity controller, between 0.0 and 1.0.
    6.default = 0.7

    7.name = max_vel_y
    7.type = float
    7.desc = Maximum fraction of sideways velocity for velocity controller, between 0.0 and 1.0.
    7.default = 0.7

    8.name = max_vel_yaw
    8.type = float
    8.desc = Maximum fraction of rotational velocity for velocity controller, between 0.0 and 1.0.
    8.default = 0.7

    9.name = step_freq
    9.type = float
    9.desc = Step frequency (should be set to the same value as in nao_walker).
    9.default = 0.5

    10.name = use_vel_ctrl
    10.type = boolean
    10.desc = `True` = use simple velocity controller, `False` = use Aldebaran's walkTo controller.
    10.default = False

    11.name = use_foot_contact_protection
    11.type = boolean
    11.desc = `True` = abort walk when robot is lifted off the ground
    11.default = True

    12.name = path_next_target_distance
    12.type = float
    12.desc = Cumulative Distance to next Velocity Target from current robot pose along path
    12.default = 0.1

    13.name = path_max_start_distance
    13.type = float
    13.desc = Max distance to start of path from robot pose to accept path (safety)
    13.default = 0.1

    14.name = threshold_damp_xy
    14.type = float
    14.desc = Slow down when distance to goal is smaller than this value [in meters].
    14.default = 0.2

    15.name = threshold_damp_yaw
    15.type = float
    15.desc = Slow down rotation when angular deviation from goal pose is smaller than this value [in radians].
    15.default = rad(60 degrees)

  }
```
