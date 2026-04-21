This node provides access to laser scan data, publishing it in the map
coordinate frame.

------------------------------------------------------------------------

## API Documentation



```clearsilver
node.0 {
 name = hokuyo_listener_cu
 desc << EOM
`hokuyo_listener_cu` is responsible for interfacing with the Hokuyo laser scanner and then publishing scan data to the rest of the system. Published messages include the scan origin to give them context. 
EOM
param {
  0.name= ~laser_scanner_x
  0.default= 0.15 (m)
  0.type= double
  0.desc= x displacement in meters between the scanner coordinate system and the world coordinate system (`/scanner_cu` and `/world_cu`, respectively).
  1.name= ~laser_scanner_y
  1.default= 0.0 (m)
  1.type= double
  1.desc= y displacement in meters between the scanner coordinate system and the world coordinate system (`/scanner_cu` and `/world_cu`, respectively).
  2.name= ~laser_scanner_theta
  2.default= PI/6 (rad)
  2.type= double
  2.desc= Radial displacement in radians between the scanner coordinate system and the world coordinate system (`/scanner_cu` and `/world_cu`, respectively).
  3.name= prairiedog/using_tf
  3.default= true
  3.type= bool
  3.desc= When true, the tf ROS package is used to facilitate coordinate transformations. 
 }
pub {
  0.name= /cu/laser_scan_cu
  0.type= hokuyo_listener_cu/PointCloudWithOrigin 
  0.desc= This is a list of laser scan hits, along with the pose of the laser scanner when it captured them. Coordinates are in the map coordinate system (/map_cu).
}
sub {
  0.name= scan
  0.type= sensor_msgs/LaserScan
  0.desc= This is a laser scan from the hokuyo laser scanner node it contains coordinates in local angle-distance format.
  1.name= /cu/pose_cu
  1.type= geometry_msgs/PoseStamped
  1.desc= The robot's best estimate of where it is, given all pose data, in map coordinates (`/map_cu`).
}
srv_called {
  0.name= /cu/get_map_cu
  0.type= nav_msgs/GetMap
  0.desc= Waits this service on boot so that `hokuyo_listener_cu` knows `mapper_cu` is up and running before attempting interaction with it
  1.name= /cu/get_pose_cu
  1.type= localization_cu/GetPose
  1.desc= Waits this service on boot so that listener knows localization_cu is up and running before using data provided by it.
 }
prov_tf {
  0.from= /robot_cu
  0.to= /scanner_cu
  0.desc= Transform between robot and laser scanner.
 }
req_tf {
  0.from= /scanner_cu
  0.to= /map_cu
  0.desc= Transform between laser scanner and map.
 }
}
```



------------------------------------------------------------------------

## Setting up launch file

The **hokuyo_listener_cu** node interacts with the **hokuyo** node that
is included in the ROS kitchen-sink install. To set up the ROS
**hokuyo** node, add the following commands to the .launch file that
kicks-off your code: 

```
<group ns="hokuyo">
 <param name="calibrate_time" type="bool" value="false" />
 <param name="hokuyoLaserModel04LX" type="bool" value="true" />
 <param name="min_ang" type="double" value="-2.086214" />
 <param name="max_ang" type="double" value="2.092350" />
</group>
<node name="hokuyo" pkg="hokuyo_node" type="hokuyo_node" respawn="false" output="screen" />

<node name="hokuyo" pkg="hokuyo_node" type="hokuyo_node" respawn="false" output="screen" />
```


