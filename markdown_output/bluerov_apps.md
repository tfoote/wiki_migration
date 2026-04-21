## Overview

This package includes various applications for ROVs like the
[BlueROV](Robots/BlueROV).

## Nodes



```wiki
#!clearsilver CS/NodeAPI
node.0 {
 name = 3d_buoy_finder
 desc = Uses RANSAC with a spherical model to identify buoys from a stereo camera.
 sub {
  0.name= points
  0.type= sensor_msgs/PointCloud2
  0.desc= The point cloud from a stereo camera.
 }
 pub {
  0.name= buoys
  0.type= bluerov_apps/Buoys
  0.desc= A list of found buoys.
 }
 param {
  0.name= ~radius_min
  0.type= float
  0.desc= The minimum radius of found spheres in meters.
  0.default= 0.05
  1.name= ~radius_max
  1.type= float
  1.desc= The maximum radius of found spheres in meters.
  1.default= 0.15
 }
}
```





```wiki
#!clearsilver CS/NodeAPI
node.0 {
 name = buoy_ekf
 desc = 
 pub {
  0.name= mavlink/to
  0.type= mavros_msgs/Mavlink
  0.desc= Mavlink stream to autopilot.
 }
 sub {
  0.name= mavlink/from
  0.type= mavros_msgs/Mavlink
  0.desc= Mavlink stream from autopilot.
 }
 param {
  14.name= ~gcs_url
  14.type= string
  14.desc= Connection URL. <<Version(0.7.0)>>
  14.default= udp://@
 }
}
```





```clearsilver
node.0 {
 name = teleop_joy
 desc = 
 sub {
  0.name= joy
  0.type= sensor_msgs/Joy
  0.desc= Joystick feedback.
 }
 pub {
  0.name= mavros/rc/override
  0.type= mavros_msgs/OverrideRCIn
  0.desc= An RC override messages for the FCU.
 }
 srv_called {
  0.name= mavros/cmd/command
  0.type= mavros_msgs/CommandLong
  0.desc= Used for arming, disarming, landing, and taking off.
 }
}
```



## Tutorials

<<TutorialChain(bluerov_apps/Tutorials/teleop_joy)>>
