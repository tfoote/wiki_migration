![Yujin Robot\|width=30%,align="right"](attachment:yujin.jpg)

## About Yujin LiDAR

YRL series LiDAR is designed to detect objects, measure distances from
surroundings and collect data as point clouds. Yujin LiDAR is an
optimized solution for indoor mapping, navigation, localization and
other applications in a variety of industries including robotics, safety
and security.

## Supported Hardware

  -- --------------------- -- --------- ---------------------------------------------------------------------- --
     <30%>                  <70%>                                                                          
     • YRL2-05 (2D, 5m)       <        6>![Yujin Robot YRL\|width=50%](attachment:LiDAR_3D_Silver.192.png)   
     • YRL2-10 (2D, 10m)                                                                                       
     • YRL2-20 (2D, 20m)                                                                                       
     • YRL3-05 (3D, 5m)                                                                                        
     • YRL3-10 (3D, 10m)                                                                                       
     • YRL3-20 (3D, 20m)                                                                                       
  -- --------------------- -- --------- ---------------------------------------------------------------------- --

## Supported Platforms

ROS support is currently available for:

-   ROS Melodic on Ubuntu 18.04

Please note, that basic drivers for Ubuntu 18.04 (wrapped by this ROS
package) as well as Windows 10 are available as well including viewer
tools.

## ROS API

```clearsilver
node{
 0{
  name = yrl_pub
  desc = Publishes the LiDAR point cloud
  pub{
   0{
    name = yrl_cloud
    type = sensor_msgs/PointCloud2
    desc = LiDAR point cloud
   }
  }
 }
}
```

## Example Usage

### 3D SLAM

![SLAM example 1\|width=100%](attachment:slam_F1.gif)

![SLAM example 2\|width=100%](attachment:slam_F1_2.gif)

### Obstacle Detection

![OD example 1\|width=100%](attachment:od_1.gif)

![OD example 2\|width=100%](attachment:od_2.gif)

![OD example 3\|width=100%](attachment:od_3.gif)

## Further Information

For more details on the YRL series check out the official website:
<http://lidar.yujinrobot.com/>

Available additional information includes among others:

-   User manual
-   Communication protocol specification
-   2D/3D CAD drawings
-   Product catalog

## Report a bug

Use Github to
[report bugs](https://github.com/yujinrobot/yujin_lidar/issues) or
[request features](https://github.com/yujinrobot/yujin_lidar/issues).
