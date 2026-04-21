## OpenNI_Viewer

**OpenNI Viewer** is a lightweight PointCloud2 viewer.



```
$ rosrun openni_pcl openni_viewer ~input:=/camera/depth/points2
```



![](attachment:pcl_openni_viewer_ds.jpg)

The viewer is based on [PCL](http://pointclouds.org) and
[PCLVisualization](http://www.ros.org/wiki/pcl_visualization), two
packages available in the
[perception_pcl](http://www.ros.org/wiki/perception_pcl) and
[perception_pcl_addons](http://www.ros.org/wiki/perception_pcl_addons)
stacks. To download them, you can use the following rosinstall file:


```
- svn:
    uri: https://code.ros.org/svn/ros-pkg/stacks/perception_pcl/tags/unstable
    local-name: ros_pkg/stacks/perception_pcl
- svn:
    uri: https://code.ros.org/svn/ros-pkg/stacks/perception_pcl_addons/tags/unstable
    local-name: ros_pkg/stacks/perception_pcl_addons
```



Then just rosmake openni_pcl: 

```
rosmake openni_pcl
```


