## Overview

ROS package for point cloud filtering. This package allows you to
perform the following filters on a point cloud:

-   X, Y and Z limiting filter. This filter delete the points outside of
    some defined axis limits \[x_min, x_max\], \[y_min, y_max\] and
    \[z_min, z_max\].
-   Voxel Grid. This filter reduce the number of points using a
    voxelized grid approach.

This package uses the algorithms of [PCL](http://pointclouds.org/) to
perform the filtering tasks.

You can find a PCL axis limiting filter tutorial
[here](http://pointclouds.org/documentation/tutorials/passthrough.php)
and a voxel grid downsampling
[here](http://pointclouds.org/documentation/tutorials/voxel_grid.php).

## Usage

1\. Download the package from source
[here](https://github.com/srv/point_cloud_filtering). 2. Include the
package into you ROS workspace:

Go to your ROS home directory 

```
$ roscd
```



Put this package into your workspace 

```
$ rosws set download_path/point_cloud_filtering
```



Update 

```
$ source setup.sh
```



3\. Setup the filter parameters in the file filter_params.yaml 4. Run
the package using the launch file included: 

```
$ roslaunch point_cloud_filtering point_cloud_filtering.launch
```


