## Hardware requirements

-   Sick LMS 200

```{=html}
<!-- -->
```
-   Point Grey Chamelon USB2.0 camera

## Software requirements

-   Point Grey flyCapture SDK

## Usage

1.The node "scan" must be run first: 

```shell
rosurn sick_laser scan
```



2.If you want to get the 3D point cloud,the following command must be
run:

rosrun sick_laser point_cloud \[port_number\] \[direction\]
\[frequency\] \[how many degrees to move\] \[the first degree\] \[if
data save as pcd file\].

\[port_number\] : port number;

\[direction\] : '0' or '1';

\[frequency\] : The frequency which motor rotate at;

\[the first degree\] : To ensure the coordinate system is prefect,so you
should give a first degree.

\[if data save as pcd file\] : 'y' -> yes or 'n'-> no.

For example:



```shell
rosrun sick_laser point_cloud 2 1 3600 360 0 y
```



And this node will output the point cloud as "laserdata.pcd".

3.If you want to get the 3D point cloud and the image.Please run the
following command:

rosrun sick_laser cloud_and_image \[port_number\] \[direction\]
\[frequency\] \[how many degrees to move\] \[the first degree\] \[if
data save as pcd file\]

\[port_number\] : port number;

\[direction\] : '0' or '1';

\[frequency\] : The frequency which motor rotate at;

\[the first degree\] : To ensure the coordinate system is prefect,so you
should give a first degree.

\[if data save as pcd file\] : 'y' -> yes or 'n'-> no.

For example:



```shell
rosrun sick_laser cloud_and_image 2 1 3600 360 0 y
```

 And this command will output a point cloud as
laserdata.pcd and eight pictures from image1.bmp to image8.bmp.

## Nodes



```clearsilver
node.0 {
name = scan
desc = The scan node is used to generate the data stream of the sick.

pub {
0.name = /scan
0.type = sensor_msgs/LaserScan
0.desc = Publish the data stream of the laser scan.
}
}
```

 

```clearsilver
node.0 {
name = point_cloud
desc = The point_cloud node is used to get the 3D point cloud with the the data stream of the laser scan. 

sub {
0.name = /scan
0.type = sensor_msgs/LaserScan 
0.desc = Subscribe the laser scan.
}

pub {
0.name = cloud
0.type = sensor_msgs/PointCloud 
0.desc = Publish the point cloud.
}
}
```




```clearsilver
node.0 {
name = cloud_and_image
desc = The cloud_and_image node is used to get the RGBD data of the scene with the sick and the camera. 

sub {
0.name = /scan
0.type = sensor_msgs/LaserScan 
0.desc = Subscribe the laser scan.
}

pub {
0.name = cloud
0.type = sensor_msgs/PointCloud 
0.desc = Publish the point cloud.
}
}
```



## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.
