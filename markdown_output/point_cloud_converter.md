  -- --------------------------------------- --
     <#FF0000>*DEPRECATED* (Diamondback)   
  -- --------------------------------------- --

Please convert to using PointCloud2, alternatively you can checkout it
by yourself at:
<https://github.com/pal-robotics-forks/point_cloud_converter>

### Usage

The point_cloud_converter package contains a single node (with the same
name) that can be used to convert data between the old
sensor_msgs/PointCloud and the new sensor_msgs/PointCloud2 data formats,
and viceversa. To achieve this, the node accepts inputs on two ROS
topics:

-   **points_in** for PointCloud,
-   and **points2_in** for PointCloud2.

The outputs will be generated as follows:

-   if the input data is coming in on **points_in** as PointCloud
    messages, the output will go on **points2_out** as PointCloud2
    messages;
-   if the input data is coming in on **points2_in** as PointCloud2
    messages, the output will go on **points_out** as PointCloud
    messages.

Examples: 

```
$  rosrun point_cloud_converter point_cloud_converter points2_in:=/my_input_pointcloud2_topic points_out:=/my_output_pointcloud_topic
[ INFO] [1272222413.891331026]: PointCloudConverter initialized to transform from PointCloud (/points_in) to PointCloud2 (/points2_out).
[ INFO] [1272222413.891524710]: PointCloudConverter initialized to transform from PointCloud2 (/points2_in) to PointCloud (/points_out).
```





```
$  rosrun point_cloud_converter point_cloud_converter /points2_in:=my_input_pointcloud2_topic /points_out:=my_output_pointcloud_topic
[ INFO] [1272222329.786616389]: PointCloudConverter initialized to transform from PointCloud (/points_in) to PointCloud2 (/points2_out).
[ INFO] [1272222329.786817983]: PointCloudConverter initialized to transform from PointCloud2 (/my_input_pointcloud2_topic) to PointCloud (/my_output_pointcloud_topic).
```


