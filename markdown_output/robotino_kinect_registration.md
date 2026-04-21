## Overview

Robotino now supports the Kinect sensor and this package explores the
possibilities of Robotino and the Kinect sensor.

The Kinect sensor on Robotino currently publishes the depth images as
Pointclouds of PointXYZ type. The RGB information will be incorporated
in the Pointclouds soon.

One of the applications of the Kinect could be building a 3D
representation of a surrounding. The kinect_registration node builds a
simple 3D model using the Pointclouds from the Kinect by applying known
transformations to the Pointclouds received. This is done in the
following steps: 1. Get a Pointcloud 2. Rotate Robotino by a pre-defined
value (40.0 degrees in our case, this value can be modified in the
launch file) 3. Get another Pointcloud 4. Transform the Pointcloud from
step 3 by rotating it by 40 degrees \* iteration number along the Z
axis. 5. Publish the cloud 6. Repeat again from step 2 until Robotino
has completed 360 degrees of rotation.

**Note:** The above method doesn't use any registration algorithms such
as ICP etc. It only performs basic registration because the
transformation is known in advance.

A result of the kinect_registration_node can be seen below:

![](attachment:OfficeCloudResized.png)

## ROS Nodes

```clearsilver
node.0 {
 name = kinect_registration_node
 sub {
  0.name= kinect
  0.type= sensor_msgs/PointCloud2
  0.desc= Pointcloud from the Kinect sensor
 } 
 pub {
  0.name= registered_cloud (name configurable in the launch file)
  0.type= sensor_msgs/PointCloud2
  0.desc= The registered pointcloud
}
param {
  0.name= ~angle_rotation
  0.default= 40.0
  0.type= double
  0.desc= The size of the step angle while Robotino rotates a complete 360 degrees
  1.name= ~output_topic
  1.default= registered_cloud
  1.type= string
  1.desc= The name of the topic to publish the registered cloud
 }
}
```

#### Usage

To launch the kinect_registration_node, run the following command.
```
roslaunch robotino_kinect kinect_registration.launch
``` Once the node has been successfully launched,
it will subscribe to the /kinect topic, obtain the pointclouds, register
them and publish the output. This is done repeatedly until Robotino has
rotated a whole 360 degrees.

If you would like to save the pointclouds published by the
kinect_registration_node, run the following command. **Note:** If you
have modified the launch file then your publish topic might be
different. ```
rosrun pcl_ros pointcloud_to_pcd /input:=/kinect_registration_node/registered_cloud
```
