## Get started

To learn how to use this package, take a look to the
[TurtleBot panorama tutorial](turtlebot_panorama/Tutorials/Demo)

## ROS API

```clearsilver
name = pano_app
desc = Creates panorama pictures from stitched snapshots
sub{
  0.name = pano_app/take_pano
  0.type = std_msgs/Empty
  0.desc = start the panorama creation with predefined parameters

  1.name = pano_app/stop_pano
  1.type = std_msgs/Empty
  1.desc = stop the panorama creation

  2.name = pano_app/odom
  2.type = nav_msgs/Odometry
  2.desc = retrieves the robot's odometry to calculate when to take snapshots and when to stop

  3.name = pano_server/stitch
  3.type = sensor_msgs/Image
  3.desc = retrieves the stitched image from the pano_ros action server (via ImageTransport)
}
pub {
  0.name = pano_app/log
  0.type = std_msgs/String
  0.desc = extra logging via rostopic

  1.name = pano_app/panorama
  1.type = sensor_msgs/Image
  1.desc = publishes the stitched image (via ImageTransport)

  2.name = pano_app/cmd_vel
  2.type = geometry_msgs/Twist
  2.desc = velocity commands for rotating the robot

  3.name = pano_server/snap
  3.type = std_msgs/Empty
  3.desc = triggers the pano_ros action server to take a snapshot

  4.name = pano_server/stop
  4.type = std_msgs/Empty
  4.desc = triggers the pano_ros action server to stop taking snapshots and start the stitching process
}
srv {
  0.name = pano_app/take_pano
  0.type = turtlebot_panorama/TakePano
  0.desc = start/stop the panorama creation with user defined parameters
}

param {
  0.name = ~default_mode
  0.type = String
  0.desc = default mode for panorama creation: 1 - continuous, 0 - snap&turn
  0.default = 1

  1.name = ~default_pano_angle
  1.type = double
  1.desc = total rotating angle for the panorama creation in radians
  1.default = 2 * Pi (360 degree)

  2.name = ~default_snap_interval
  2.type = String
  2.desc = interval in degrees or seconds (depending on chosen mode) for taking snapshots
  2.default = 2.0

  3.name = ~default_rotation_velocity
  3.type = double
  3.desc = rotating velocity in radians/sec
  3.default = 0.3

  4.name = ~camera_name
  4.type = String
  4.desc = topic name prefix for the camera image topic
  4.default = /camera/rgb

  5.name = ~bag_location
  5.type = String
  5.desc = location and filename for storing the bag file
  5.default = /tmp/turtlebot_panorama.bag
}
```
