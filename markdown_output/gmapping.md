## External Documentation

This is mostly a third party package; the underlying GMapping library is
[externally documented](http://openslam.org/gmapping.html). Look there
for details on many of the parameters listed below.

## Hardware Requirements

To use `slam_gmapping`, you need a mobile robot that provides odometry
data and is equipped with a horizontally-mounted, fixed, laser
range-finder. The `slam_gmapping` node will attempt to transform each
incoming scan into the `odom` (odometry) [tf](tf) frame. See the
"[Required tf transforms](#Required_tf_Transforms)" for more on
required transforms.

## Example

To make a map from a robot with a laser publishing scans on the
`base_scan` topic:

```
rosrun gmapping slam_gmapping scan:=base_scan
```

## Nodes

```clearsilver
 name = slam_gmapping
 desc = The `slam_gmapping` node takes in <<MsgLink(sensor_msgs/LaserScan)>> messages and builds a map (<<MsgLink(nav_msgs/OccupancyGrid)>>). The map can be retrieved via a ROS [[Topics|topic]] or [[Services|service]].
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
   2{
    name = ~entropy
    type = std_msgs/Float64
    desc = Estimate of the entropy of the distribution over the robot's pose (a higher value indicates greater uncertainty).  New in 1.1.0.
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
    0.name = ~inverted_laser
    0.type = string
    0.default = `"false"`
    0.desc = '''(REMOVED in 1.1.1; transform data is used instead)''' Is the laser right side up (scans are ordered CCW), or upside down (scans are ordered CW)?
    1.name = ~throttle_scans
    1.type = int
    1.default = 1
    1.desc = Process 1 out of every this many scans (set it to a higher number to skip more scans)
    2.name = ~base_frame
    2.type = string
    2.default = `"base_link"`
    2.desc = The frame attached to the mobile base.
    3.name = ~map_frame
    3.type = string
    3.default = `"map"`
    3.desc = The frame attached to the map.
    4.name = ~odom_frame
    4.type = string
    4.default = `"odom"`
    4.desc = The frame attached to the odometry system.
    5.name = ~map_update_interval
    5.type = float
    5.default = 5.0
    5.desc = How long (in seconds) between updates to the map. Lowering this number updates the occupancy grid more often, at the expense of greater computational load.
    6.name = ~maxUrange
    6.type = float
    6.default = 80.0
    6.desc = The maximum usable range of the laser. A beam is cropped to this value.
    7.name = ~sigma
    7.type = float
    7.default = 0.05
    7.desc = The sigma used by the greedy endpoint matching
    8.name = ~kernelSize
    8.type = int
    8.default = 1
    8.desc = The kernel in which to look for a correspondence
    9.name = ~lstep
    9.type = float
    9.default = 0.05
    9.desc = The optimization step in translation
    10.name = ~astep
    10.type = float
    10.default = 0.05
    10.desc = The optimization step in rotation
    11.name = ~iterations
    11.type = int
    11.default = 5
    11.desc = The number of iterations of the scanmatcher
    12.name = ~lsigma
    12.type = float
    12.default = 0.075
    12.desc = The sigma of a beam used for likelihood computation
    13.name = ~ogain
    13.type = float
    13.default = 3.0
    13.desc = Gain to be used while evaluating the likelihood, for smoothing the resampling effects
    14.name = ~lskip
    14.type = int
    14.default = 0
    14.desc = Number of beams to skip in each scan. Take only every (n+1)th laser ray for computing a match (0 = take all rays)
    15.name = ~minimumScore
    15.type = float
    15.default = 0.0
    15.desc = Minimum score for considering the outcome of the scan matching good. Can avoid jumping pose estimates in large open spaces when using laser scanners with limited range (e.g. 5m). Scores go up to 600+, try 50 for example when experiencing jumping estimate issues.
    16.name = ~srr
    16.type = float
    16.default = 0.1
    16.desc = Odometry error in translation as a function of translation (rho/rho)
    17.name = ~srt
    17.type = float
    17.default = 0.2
    17.desc = Odometry error in translation as a function of rotation (rho/theta)
    18.name = ~str
    18.type = float
    18.default = 0.1
    18.desc = Odometry error in rotation as a function of translation (theta/rho)
    19.name = ~stt
    19.type = float
    19.default = 0.2
    19.desc = Odometry error in rotation as a function of rotation (theta/theta)
    20.name = ~linearUpdate
    20.type = float
    20.default = 1.0
    20.desc = Process a scan each time the robot translates this far
    21.name = ~angularUpdate
    21.type = float
    21.default = 0.5
    21.desc = Process a scan each time the robot rotates this far
    22.name = ~temporalUpdate
    22.type = float
    22.default = -1.0
    22.desc = Process a scan if the last scan processed is older than the update time in seconds. A value less than zero will turn time based updates off.
    23.name = ~resampleThreshold
    23.type = float
    23.default = 0.5
    23.desc = The Neff based resampling threshold
    24.name = ~particles
    24.type = int
    24.default = 30
    24.desc = Number of particles in the filter
    25.name = ~xmin
    25.type = float
    25.default = -100.0
    25.desc = Initial map size (in metres)
    26.name = ~ymin
    26.type = float
    26.default = -100.0
    26.desc = Initial map size (in metres)
    27.name = ~xmax
    27.type = float
    27.default = 100.0
    27.desc = Initial map size (in metres)
    28.name = ~ymax
    28.type = float
    28.default = 100.0
    28.desc = Initial map size (in metres)
    29.name = ~delta
    29.type = float
    29.default = 0.05
    29.desc = Resolution of the map (in metres per occupancy grid block)
    30.name = ~llsamplerange
    30.type = float
    30.default = 0.01
    30.desc = Translational sampling range for the likelihood
    31.name = ~llsamplestep
    31.type = float
    31.default = 0.01
    31.desc = Translational sampling step for the likelihood
    32.name = ~lasamplerange
    32.type = float
    32.default = 0.005
    32.desc = Angular sampling range for the likelihood
    33.name = ~lasamplestep
    33.type = float
    33.default = 0.005
    33.desc = Angular sampling step for the likelihood
    34.name = ~transform_publish_period
    34.type = float
    34.default = 0.05
    34.desc = How long (in seconds) between transform publications. To disable broadcasting transforms, set to `0`.
    35.name = ~occ_thresh
    35.type = float
    35.default = 0.25
    35.desc = Threshold on gmapping's occupancy values.  Cells with greater occupancy are considered occupied (i.e., set to 100 in the resulting <<MsgLink(sensor_msgs/LaserScan)>>).  New in 1.1.0.
    36.name = ~maxRange
    36.type = float
    36.desc = The maximum range of the sensor. If regions with no obstacles within the range of the sensor should appear as free space in the map, set maxUrange < maximum range of the real sensor <= maxRange.
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
