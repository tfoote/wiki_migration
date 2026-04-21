## Documentation

This package provides various nodes to run the BipedRobin coffee butler
demo, in which the Robot uses a Microsoft Kinect to detect and throw
away cups.

## Nodes



```clearsilver
node.0 {
name = coffee_butler
desc = Controls the execution of the different Services between the biped_robin_coffee_butler and biped_robin_object_manipulator nodes
pub {
  0.name = chatter_pub
  0.type = std_msgs::String
  0.desc = Publishes strings for speech_database voice output.
}
srv {
 0.name = pickup_cylinder
 0.type = biped_robin_msgs/PickupObjectService
 0.desc = Calls service from biped_robin_object_manipulator to pickup the cup which is positioned the cylinder_center frame published by the pcl_cylinder node.
 1.name = place_cylinder
 1.type = biped_robin_msgs/PickupObjectService
 1.desc = Calls service from biped_robin_object_manipulator to place the cup in the bin_frame.
}
srv_called {
 0.name = start_detecting_client
 0.type = std_srvs/Empty
 0.desc = Starts the object detection in the pcl_cylinder node.
 1.name = stop_detecting_client
 1.type = std_srvs/Empty
 1.desc = Stops the object detection in the pcl_cylinder node.
}
}
node.1 {
name = pcl_cylinder
desc = Node to detect cylinders in Kinect point_cloud, creates tf::transform with the cylinder center as origin.
sub {
  0.name = cloud_throttled
  0.type = sensor_msgs/PointCloud2
  0.desc = Subscribes to the Kinect point cloud.
}
pub {
  0.name = filter_cloud
  0.type = sensor_msgs/PointCloud2
  0.desc = Publishes the filtered segment of the Kinect point cloud (only the table).
  1.name = plane_cloud
  1.type = sensor_msgs/PointCloud2
  1.desc = Publishes the detected table plane of the Kinect point cloud.
  2.name = cylinder_cloud
  2.type = sensor_msgs/PointCloud2
  2.desc = Publishes the detected cylinder of the Kinect point cloud.
}
srv {
  0.name = start_detecting_srv
  0.type = std_srvs/Empty
  0.desc = Starts the detection of the cylinder detection.
  1.name = stop_detecting_srv
  1.type = std_srvs/Empty
  1.desc = Stops the detection of the cylinder detection.
}
}
```


