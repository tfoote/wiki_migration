![](attachment:gpsd_viewer.png)

## Usage

The package provides a means of visualizing GPS and map data using the
Open Street Maps GTK Widget.

## Details

Map Viewer for GPS position data provided by
[gps_common/msg/GPSFix](https://docs.ros.org/en/rolling/p/gps_common/msg/GPSFix.html)
messages provided by [gpsd_client](gpsd_client). Due to GPS library and
API synchronization issues this package requires Ubunut 10.04 or newer.

gpsd Version 2.92

Updating to the newest version of gpsd_client is also recommended.

Planned future updates include switching to
[UTM](http://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system)
co-ordinate system and a standardized GPS message format.

## Example

You can run the [gpsd_viewer](gpsd_viewer) on a pre-recorded bag file
that comes with the package. First, make sure you have the
[ccny_ground_station](ccny_ground_station) stack downloaded and
installed by following the instructions
[here](ccny_ground_station#Installing).

Next, make sure you have the necessary tools installed:



```shell
rosmake rviz rosbag
```



Finally, run the demo:



```shell
roslaunch gpsd_viewer demo.launch
```



You should then see a map display and a moving marker for the position
data that was recorded.

[Youtube](https://www.youtube.com/watch?v=t0-ABAmCjkQ)

## Nodes



```clearsilver
node.0 {
  name = gpsd_viewer
  desc = This node provides a map and displays a marker indicating the position obtained from a <<MsgLink(gps_common/GPSFix)>> message.
  sub {
    0.name = /fix
    0.type = gps_common/GPSFix
    0.desc = This topic is advertised by [[gpsd_client]].
  }
}
```



## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.

Please use our [Trac](http://robotics.ccny.cuny.edu/trac/) to
[report bugs](http://robotics.ccny.cuny.edu/trac/newticket?component=ccny_vision/ar_pose&type=defect)
or
[request features](http://robotics.ccny.cuny.edu/trac/newticket?component=ccny_vision/ar_pose&type=enhancement).
