## C++ Programming API

Various headers provide common interfaces for the ART autonomous
vehicle. They are described in the
[API documentation](http://www.ros.org/doc/api/art_common/html/files.html).

## Nodes



```clearsilver
node.0 {
 name = vehicle_static_tf
 desc = Broadcast static transforms for various devices in the `/vehicle` frame of reference. Some ROS components require that to be done about once every 10 seconds.
 prov_tf {
  0.from = /vehicle
  0.to = /front_sick
  0.desc = front Sick 2D LIDAR
  1.from = /vehicle
  1.to = /rear_sick
  1.desc = rear Sick 2D LIDAR
  2.from = /vehicle
  2.to = /velodyne
  2.desc = Velodyne 3D LIDAR
  3.from = /vehicle
  3.to = /front_right_camera
  3.desc = front right camera mounted under the Velodyne.
 }
}
```



#### Usage



```
rosrun art_common vehicle_static_tf
```


