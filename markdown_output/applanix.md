## Deprecated

This package is fairly specific to the POS-LV device used in the ART
autonomous vehicle. For a long time, it was the only Applanix driver
available in ROS.

Now, there is a more-complete implementation called
[applanix_driver](applanix_driver), developed by Clearpath Robotics with
help from Applanix engineers. We recommend using that driver instead of
this one for new applications.

## Applanix Odometry driver

### Usage

```
rosrun applanix odometry [options]

Options:
    -f <filename>  PCAP packet dump file name (default: use real device)
    -h, -?         print help text
    -q <integer>   set ROS topic queue depth (default: 1)
    -t <filename>  run unit test with fake data from <filename>
```

### Examples

Read the Applanix POS-LV, publishing \`gps\` and \`odom\` messages.
```
$ rosrun applanix odometry
```

Read previously captured Applanix packets from \`dump.pcap\` file.
```
$ rosrun applanix odometry -f dump.pcap
```

```clearsilver
node.0 {
 name = odometry
 pub {
  0.name = odom
  0.type = nav_msgs/Odometry
  0.desc = Three-dimensional odometry from Applanix POS-LV.
  1.name = imu
  1.type = sensor_msgs/Imu
  1.desc = Inertial measurements from Applanix POS-LV.
  2.name = gps
  2.type = art_msgs/GpsInfo
  2.desc = Latitude and longitude data from Applanix POS-LV.
 }
}
prov_tf {
  0.from = /odom
  0.to   = /earth
  0.desc = 2D frame in UTM grid at same elevation as vehicle.
  1.from = /earth
  1.to   = /vehicle
  1.desc = 3D pose of vehicle in UTM grid relative to mean sea level.
}
sub {
  0.name = shifter/state
  0.type = art_msgs/Shifter
  0.desc = Transmission gear currently selected.
}
```
