## Overview

This package provides several utilities for environment perception and
modelling from RGB-D sensor data, e.g. Kinect device.

## System architecture

The package consists of three major components:

-   **[BB Estimator](bb_estimator)** - ROS service performing rough
    bounding box estimation of an object inside a specified 2D region of
    interest using the Kinect depth data.
-   **Depth map segmentation** - ROS service providing Kinect depth map
    segmentation (or other, image based depth map) using several
    approaches, such as maximum normal/depth difference, plane
    prediction etc.
-   **Plane Fitting** - ROS service providing plane fitting in point
    cloud data based on 3D Hough Transform. Node is able to iterate
    through several frames while adding data into current point cloud
    and refining detected planes.

### Depth map segmentation

The depth map segmentation node\'s main purpose is to divide Kinect
depth image into several regions of interest. It is supposed to be the
preprocessing task for 3D environment creation but also for the other
possible detectors (object detection etc.). For depth map segmentation
itself, several algorithms are possible to use:

#### Depth based segmentation

The depth based segmentation method is the fastest segmentation method
due to the nature of segmentation -- simple depth difference of
neighboring pixels. Even if this is not proper plane detector, the
usability as a preprocessing unit it recommended due to very high
efficiency. The scene is divided to multiple depth differing segments,
which pose a very good input for plane detectors.

#### Normal based segmentation

Normal based segmentation method uses similar principle as depth based
method with the difference that this algorithm uses normal difference
for gradient image creation.

#### Depth and normal fused segmentation

Having the outputs from depth based and normal based segmentation
methods, the later fusion can be applied to produce more accurate and
stable final results.

#### Plane prediction segmentation

Plane prediction method emerges from the original need for plane
detector pre-processing algorithm. It applies the same method as
segmentation above -- gradient image followed by watershed segmentation
method, however the process of gradient map computation is different.
The gradient map computation has two outputs -- edge strengths gradient
image and number of changes gradient image .

#### Tiled RANSAC segmentation

Last of implemented methods approaches to the plane segmentation from a
different way. Planes are searched using RANSAC search. Tiled RANSAC has
proven to be fast enough to be used in real-time systems because of
small random sample search. On the other hand, the possibility of
filling regions outside the tile borders ensures that found planes are
marked on the whole depth image.

### Plane Fitting

Plane fitting component constructs iteratively the knowledge of
surrounding scene by creating plane segment information. Plane detection
itself is constructed by analysing Hough Space created by iteratively
adding Hough transform information from several frames.

Altough the Hough transform main disadvantage is high memory
requirements, our method has overcame these drawbacks by implementation
of hierarchic adaptive structure, which keeps memory requirements as low
as possible while speeding up the computation.

The output of this node is a list of detected planes sent in a message.
Each plane is defined in two ways - plane equation and bounding
rectangle (in 3D) for visualisation purposes.

## ROS API

### Nodes

  -- -------------------- -- -------------------------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     **Node Name**           **Published Topics**                                                    **Description**                                                                                                                                                                                                                                   
     but_segmenter           /but_env_model/seg_region_image;/but_env_model/seg_deviation_image      Node implementing depth image segmenter. Publishes region image (image with region index information) and sometimes deviation image (image with computed std. deviations of detected planes). Please see below when these topics are published.   
     but_plane_detector      /but_env_model/plane_array                                              Node implements described plane detector. It publishes a plane array message, which is represented by the list of found planes.                                                                                                                   
  -- -------------------- -- -------------------------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

### Services

  -- ----------------------------- -- ----------- -- -------------------------- -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     **Service Name**                 **Input**      **Output**                    **Description**                                                                                                                                                                                                               
     /but_env_model/clear_planes      \-             Message about the result      Called service clears the accumulator of planes and Hough Space, which is constructed iteratively from all arriving point clouds. After calling this service the node is reset and continues detecting planes from scratch.   
  -- ----------------------------- -- ----------- -- -------------------------- -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

### Published topics

  -- ------------------------------------ -- ----------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     **Topic Name**                          **Message**                      **Description**                                                                                                                                                                                        
     /but_env_model/seg_region_image         sensor_msgs::Image               A 16bit unsigned short image of segmented indices. Indices start with index 1, if index is less than 1, it signifies a border or not segmented region. It is published by every segmentation method.   
     /but_env_model/seg_deviation_image      sensor_msgs::Image               A region image with computed depth std. deviations from plane approximated through every region. It is NOT published by Depth segmentation method (Normals are not computed due to speed reasons).     
     /but_env_model/plane_array              srs_env_model::InsertPlanes      Plane array of srs_env_model_msgs::PlaneDes with each plane information. Each plane has INSERT/MODIFY/DELETE flag, which specifies action.                                                             
  -- ------------------------------------ -- ----------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

## Installation

All components are in srs git in srs_env_model_percp package and can be
compiled with ROS standard tool rosmake ```
rosmake srs_env_model_percp
```

command

## Configuration

Optional parameters for each node. Attention, since this module is
flagged as under construction, several parameters are not possible to
set up yet.

### Depth map segmentation

List of but_segmenter\'s optional parameters:

-   **-type \[TYPE\]**
-   Parameter type specifies type of segmenting method **\*depth** -
    Segmenter uses only depth information **\*normal** - Segmenter uses
    only normal information (delegates also std deviation image)
    **\*combined** - Segmenter uses combined depth and normal
    information (delegates also std deviation image) **\*predictor** -
    Segmenter uses predictor plane algorithm **\*tile** - Segmenter uses
    tiling plane segmentation (delegates also std deviation image)

```{=html}
<!-- -->
```
-   Default is combined method.

**\*-maxdepth \[NUM\]**

-   Number how deep point should be considered for computation (in
    milimeters)\"
-   Default is 3000

### Plane Fitting

List of but_plane+detector\'s optional parameters:

**\*-input \[VAL\]** **\*pcl** - Plane detector will suppose pcl point
cloud as an input **\*kinect** - Plane detector will suppose Kinect
depth map as an input

-   Necessary parameter, please specify the input

**\*-target \[FRAME_ID\]**

-   Target frame id of sent planes.
-   Attention, the tf path from point cloud frame id into target id must
    exist!

## Dependencies

-   opencv2
-   eigen
-   roscpp
-   image_transport
-   camera_calibration_parsers
-   cv_bridge
-   std_msgs
-   pcl
-   visualization_msgs
-   pcl_ros
-   srs_env_model
-   srs_interaction_primitives

## Usage

A few examples of starting described nodes:

-   normal start of segmenter node ```
rosrun srs_env_model_percp but_segmenter
```

```{=html}
<!-- -->
```
-   start of segmenter node with method specified (depth only
    segmentation) ```
rosrun srs_env_model_percp but_segmenter -type depth
```

```{=html}
<!-- -->
```
-   start of segmenter node with maximum depth specified (in milimeters)
    ```
rosrun srs_env_model_percp but_segmenter -maxdepth 4500
```

```{=html}
<!-- -->
```
-   normal start of plane detector node (you must specify the input)
    ```
rosrun srs_env_model_percp but_plane_detector -input pcl
```

```{=html}
<!-- -->
```
-   start of plane detector node with target frame id specified
    ```
rosrun srs_env_model_percp but_plane_detector -input pcl -target /world
```
