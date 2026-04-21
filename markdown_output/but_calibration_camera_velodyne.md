# but_calibration_camera_velodyne

-   sources on GitHub: <https://github.com/robofit/but_velodyne>

ROS package for calibration camera with Velodyne LiDAR sensor. ROS nodes
enable coarse to fine estimation of the calibration parameters (mutual
position and the orientation) of the mentioned sensors using novel 3D
marker.

![Output cloud.\|height=200px](attachment:schema.png)

The package follows the methods proposed by:

\[1\] M. Velas, M. Spanel, Z. Materna, A. Herout. Calibration of RGB
Camera with Velodyne LiDAR. In *WSCG 2014 Communication papers
proceedings*.

Here you can see the example of usage of the computed calibration
parameters for the point cloud coloring by the fusion of camera image
with the LiDAR point cloud:

![Output cloud.\|height=150px](attachment:camera_image.png)
![Output cloud.\|height=150px](attachment:gray_cloud.png)
![Output cloud.\|height=150px](attachment:colored_cloud.png)

## Requirements

-   ROS Hydro
-   PCl 1.7 and
-   OpenCV 2.x library

## Usage

Package contains two ROS nodes for the camera-LiDAR calibration and
supplementary one for the publishing coloured pointcloud using
precomputed calibration.

For successful calibration the presence of the 3D marker (described in
\[1\]) in the scene is neccessary:

![Output cloud.\|height=150px](attachment:geom-shapes-circles-img.png)
![Output cloud.\|height=150px](attachment:detection-borders-ok.png)

Following commands will launch the calibration:



```
roslaunch but_calibration_camera_velodyne calibration_coarse.launch
```



-   command will run the coarse calibration using 3D marker (described
    in the \[1\])
-   if the 3D marker detection fails, the attempt will be repeated after
    5s
-   upon the success the node ends and prints the 6 Degrees of Freedom
    of the Velodyne related to the camera



```
roslaunch but_calibration_camera_velodyne calibration_fine.launch
```



-   will run the calibration with the refinement. This process will take
    a longer time (approx. 1 minute)



```
roslaunch but_calibration_camera_velodyne coloring.launch
```



-   launches the publisher of colored pointclouds created by the camera
    \-- Velodyne fusion
-   the calibration parameters (6DoF) computed by the `calibration` node
    must be set in configuration file `conf/coloring.yaml` (see below)

## Configuration

Configuration of the nodes can be done using \*.yaml files stored in the
`conf/` direcotry. These parameters in following files can be set:

**`conf/calibration.yaml`** file contans parameters:

-   **`camera_frame_topic`** : name of the topic, where camera RGB image
    is published
-   **`camera_info_topic`** : topic of `CameraInfo` type
-   **`velodyne_topic`** : topic, where the Velodyne pointcloud is
    published
-   **`marker`** : physical size of the 3D marker
-   **`circles_distance`** : distance between the circles centres (see
    \[1\])
-   **`circles_radius`** : radius of the circles in marker (also see
    \[1\])

in **`conf/coloring.yaml`** file you can specify:

-   **`6DoF`** : vector of the calibration parameters computed by the
    calibration process
-   **`velodyne_color_topic`** : name of the topic, where the colored
    pointcloud will be published
