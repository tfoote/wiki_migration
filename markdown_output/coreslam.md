## Hardware Requirements

To use CoreSLAM, you need a mobile robot that provides odometry data and
is equipped with a horizontally-mounted, fixed, laser range-finder. The
slam_coreslam node will attempt to transform each incoming scan into the
odom (odometry) tf frame. See the "Required tf transforms" for more on
required transforms.

## Example

To make a map from a robot with a laser publishing scans on the
base_scan topic:

```
rosrun coreslam slam_coreslam scan:=base_scan
```

## Nodes

```clearsilver
 name = slam_coreslam
 desc = The `slam_coreslam` node takes in <<MsgLink(sensor_msgs/LaserScan)>> messages and builds a map (<<MsgLink(nav_msgs/OccupancyGrid)>>). The map can be retrieved via a ROS [[Topics|topic]] or [[Services|service]].
 sub {
   0{
    name = tf
    type = tf/tfMessage
    desc = Transforms necessary to relate frames for laser, base, and odometry (see below)
    }
   1{
    name = scan
    type = sensor_msgs/LaserScan
    desc = Laser scans to create the map from
    }
  }
 pub {
   0{
    name = map_metadata
    type = nav_msgs/MapMetaData
    desc = Get the map data from this topic, which is latched, and updated periodically.
   }
   1{
    name = map
    type = nav_msgs/OccupancyGrid
    desc = Get the map data from this topic, which is latched, and updated periodically
   }
  }
 srv {
   0{
    name = dynamic_map
    type = nav_msgs/GetMap
    desc = Call this service to get the map data
    }
  }

 param{
    0.name = ~throttle_scans
    0.type = int
    0.default = 1
    0.desc = Process 1 out of every this many scans (set it to a higher number to skip more scans)
    1.name = ~base_frame
    1.type = string
    1.default = `"base_link"`
    1.desc = The frame attached to the mobile base.
    2.name = ~map_frame
    2.type = string
    2.default = `"map"`
    2.desc = The frame attached to the map.
    3.name = ~odom_frame
    3.type = string
    3.default = `"odom"`
    3.desc = The frame attached to the odometry system.
    4.name = ~map_update_interval
    4.type = float
    4.default = 5.0
    4.desc = How long (in seconds) between updates to the map. Lowering this number updates the occupancy grid more often, at the expense of greater computational load.
    5.name = ~delta
    5.type = float
    5.default = 0.05
    5.desc = Resolution of the map.
    6.name = ~sigma_xy
    6.type = float
    6.default = 0.1
    6.desc = Standard deviation in x and y directions for Monte Carlo sampling (in meters).
    7.name = ~sigma_theta
    7.type = float
    7.default = 0.35
    7.desc = Standard deviation for rotation in Monte Carlo sampling (in radians).
    8.name = ~hole_width
    8.type = float
    8.default = 0.6
    8.desc = Width of a hole (in meters). See CoreSLAM paper for details.
  }

 req_tf{
  0{
    from = <the frame attached to incoming scans>
    to = base_link
    desc = usually a fixed value, broadcast periodically by a [[robot_state_publisher]], or a `tf` [[tf#static_transform_publisher|static_transform_publisher]].
  }
  1{
    from = base_link
    to = odom
    desc = usually provided by the odometry system (e.g., the driver for the mobile base)
  }
 }
 prov_tf{
  0{
    from = map
    to = odom
    desc = the current estimate of the robot's pose within the map frame
  }
 }
```
