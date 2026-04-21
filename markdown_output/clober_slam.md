*ROS Software Maintainer: [Clobot](http://wiki.ros.org/clobot)*

## Clober SLAM Package

![Clober Robot\|width=400](attachment:clober/clober_right.png)

## Clober e-Manual

-   [Clober e-manual on gitbook](https://app.gitbook.com/@clobot-git/s/clober-manual/)
-   [Github for Clobot](http://github.com/CLOBOT-Co-Ltd/)

## ROS API

```clearsilver
node.0 {
name= clober_slam
desc= This package is used [[http://wiki.ros.org/gmapping|gmapping]].
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
  0{
   name= ~base_frame
   default= base_footprint
   type= string
   desc= The frame attached to the mobile base.
  }
  1{
   name = ~odom_frame
   type = string
   default = odom
   desc = The frame attached to the odometry system.
  }
  2{
   name = ~map_update_interval
   type = double
   default = 2.0
   desc = Map update interval (sec).
  }  
  3{
   name = ~maxUrange
   type = double
   default = 4.0
   desc = Max Range of laser sensor to use (meter).
  }
  4{
   name = ~minimumScore
   type = float
   default = 100
   desc = Min Score considering the results of scan matching.
  }
  5{
   name = ~linearUpdate
   type = float
   default = 0.2
   desc = Max Range of laser sensor to use (meter).
  }
  6{
   name = ~angularUpdate
   type = float
   default = 0.2
   desc = Min rotation angle required for processing.
  }
  7{
   name = ~temporalUpdate
   type = float
   default = 0.5
   desc = If the last scan time exceeds this update time, the scan is performed. Negative values will be ignored and not used.
  }
  8{
   name = ~delta
   type = float
   default = 0.05
   desc = Max Range of laser sensor to use (meter).
  }
  9{
   name = ~lskip
   type = int
   default = 0
   desc = Number of beams to skip in each scan.
  }
  10{
   name = ~particles
   type = int
   default = 120
   desc = Number of particles in the filter.
  }
  11{
   name = ~sigma
   type = float
   default = 0.05
   desc = Standard deviation of laser-assisted search.
  }
  12{
   name = ~delta
   type = float
   default = 0.05
   desc = Max Range of laser sensor to use (meter).
  }
  13{
   name = ~kernelSize
   type = int
   default = 1
   desc = Window size of laser-assisted search.
  }
  14{
   name = ~lstep
   type = float
   default = 0.05
   desc = Initial search step (translation).
  }
  15{
   name = ~astep
   type = float
   default = 0.05
   desc = Initial search step (rotation).
  }
  16{
   name = ~iterations
   type = int
   default = 5
   desc = Number of scan-matching iterations.
  }
  17{
   name = ~lsigma
   type = float
   default = 0.075
   desc = The sigma of a beam used for likelihood computation
  }
  18{
   name = ~ogain
   type = float
   default = 3.0
   desc = Gain to be used while evaluating the likelihood.
  }
  19{
   name = ~srr
   type = float
   default = 0.01
   desc = Odometry error (translation→ translation).
  }
  20{
   name = ~srt
   type = float
   default = 0.02
   desc = Odometry error (translation→ translation).
  }
  21{
   name = ~srr
   type = float
   default = 0.01
   desc = Odometry error (rotation → translation).
  }
  22{
   name = ~stt
   type = float
   default = 0.02
   desc = Odometry error (rotation → rotation).
  }
  23{
   name = ~resampleThreshold
   type = float
   default = 0.5
   desc = Resampling threshold value.
  }
  24{
   name = ~xmin
   type = float
   default = -10.0
   desc = Initial map size (min x).
  }
  25{
   name = ~ymin
   type = float
   default = -10.0
   desc = Initial map size (min y).
  }
  26{
   name = ~xmax
   type = float
   default = 10.0
   desc = Initial map size (max x).
  }
  27{
   name = ~ymax
   type = float
   default = 10.0
   desc = Initial map size (max y).
  }
  28{
   name = ~llsamplerange
   type = float
   default = 0.01
   desc = Translational sampling range for the likelihood.
  }
  29{
   name = ~llsamplestep
   type = float
   default = 0.01
   desc = Translational sampling step for the likelihood.
  }
  30{
   name = ~lasamplerange
   type = float
   default = 0.005
   desc = Angular sampling range for the likelihood.
  }
  31{
   name = ~lasamplestep
   type = float
   default = 0.005
   desc = Angular sampling step for the likelihood.
  }
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
