## Overview

This package contains the `stereo_image_proc` node, which sits between
the stereo camera drivers and vision processing nodes.

`stereo_image_proc` performs the duties of [image_proc](image_proc)
for both cameras, undistorting and colorizing the raw images. Note that
for properly calibrated stereo cameras, undistortion is actually
combined with rectification, transforming the images so that their
scanlines line up for fast stereo processing.

`stereo_image_proc` will also compute disparity images from incoming
stereo pairs using
[OpenCV's block matching](https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html#stereobm)
algorithm. These are best inspected using
[stereo_view](image_view#stereo_view).

The node will also produce point clouds, which you can view in
[rviz](rviz), and process with [pcl](pcl).

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- ------------------------------------------------------------------------------------------------ --
                                                                                                                                                                                                                           <tablestyle="width: 99%">**Stereo processing example**                                       
     ![Raw images\|width=650 height=240](attachment:raw.png)                                                                                                                                                                                                                                                                
     **left/image_raw**, **right/image_raw**: The raw images from each camera.                                                                                                                                                                                                                                              
     ![Stereo images\|width=650 height=240](attachment:epipolar.png)                                                                                                                                                       ![Disparity image\|width=320 height=240](attachment:disparity.jpg)                               
     **left/image_rect_color**, **right/image_rect_color**: The rectified images from each camera. The red lines show that the same point in the real world lies on the same horizontal line in each rectified image.      **disparity**: The resulting disparity map, as shown by [stereo_view](image_view#stereo_view).   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- ------------------------------------------------------------------------------------------------ --

## Tutorials

- Also see [dynamic_reconfigure](dynamic_reconfigure) to set camera and
  stereo parameters on line.

## Quick Start

Make sure your stereo camera driver(s) are running. You can check
`rostopic list | grep image_raw` to see the available raw image topics
from compatible drivers.

To get rectified and/or colorized image streams, you need to launch an
instance of `stereo_image_proc`. If you are running on a robot or a
cart, it's probably best to run `stereo_image_proc` there. For
example, if your stereo camera driver(s) are publishing:


```
/stereo/left/image_raw
/stereo/left/camera_info
/stereo/right/image_raw
/stereo/right/camera_info
```



you could do: 

```
$ ROS_NAMESPACE=stereo rosrun stereo_image_proc stereo_image_proc
```



Notice that we push `stereo_image_proc` down into the `stereo`
namespace, in which it subscribes to the camera topics in `left` and
`right`. This is functionally equivalent to running two
[image_proc](image_proc) instances in the `stereo/left` and
`stereo/right` namespaces, with the addition of stereo outputs:
disparity images (`stereo/disparity`) and point clouds
(`stereo/points2`).

In a separate terminal (on your home machine, if you are running on a
robot or cart): 

```
$ rosrun image_view image_view image:=/stereo/left/image_rect_color
```



This will display a rectified color image from the left stereo camera.
Alternatively, [stereo_view](image_view#Viewing_stereo_images) will show
you both the left and right images as well as a color-mapped disparity
image: 

```
$ rosrun image_view stereo_view stereo:=/stereo image:=image_rect_color
```



To view point clouds, you can use [rviz](rviz).

## Nodes

### stereo_image_proc

![](attachment:stereo_image_proc.png)

Performs rectification and de-mosaicing of raw stereo camera image
pairs. May also perform stereo processing to generate disparity images
and point clouds. In topic names below, `left` and `right` are
explicitly resolved by the node, so remapping those names effectively
remaps all topics `left/\*` and `right/\*`.

All processing is on demand. Color processing is performed only if there
is a subscriber to a color topic. Rectification is performed only if
there is a subscriber to a rectified topic. Disparities and point clouds
are generated only if there is a subscriber to a relevant topic. While
there are no subscribers to output topics, `stereo_image_proc`
unsubscribes from the `image_raw` and `camera_info` topics.

Point clouds are generated in the optical frame of the left imager (X
Right, Y Down, Z out). ![](attachment:stereo_frames.png)

[image_transport](image_transport) is used for all image publications
and subscriptions. 

```clearsilver
sub {
  group.0 {
    name = Left camera
    0.name = left/image_raw
    0.type = sensor_msgs/Image
    0.desc = Raw image stream from the left camera.
    1.name = left/camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = Left camera metadata.
  }
  group.1 {
    name = Right camera
    0.name = right/image_raw
    0.type = sensor_msgs/Image
    0.desc = Raw image stream from the right camera.
    1.name = right/camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = Right camera metadata.
  }
}
pub {
  group.0 {
    name = Left camera processed images
    0.name = left/image_mono
    0.type = sensor_msgs/Image
    0.desc = Left monochrome unrectified image.
    1.name = left/image_rect
    1.type = sensor_msgs/Image
    1.desc = Left monochrome rectified image.
    2.name = left/image_color
    2.type = sensor_msgs/Image
    2.desc = Left color unrectified image.
    3.name = left/image_rect_color
    3.type = sensor_msgs/Image
    3.desc = Left color rectified image.
  }
  group.1 {
    name = Right camera processed images
    0.name = right/image_mono
    0.type = sensor_msgs/Image
    0.desc = Right monochrome unrectified image.
    1.name = right/image_rect
    1.type = sensor_msgs/Image
    1.desc = Right monochrome rectified image.
    2.name = right/image_color
    2.type = sensor_msgs/Image
    2.desc = Right color unrectified image.
    3.name = right/image_rect_color
    3.type = sensor_msgs/Image
    3.desc = Right color rectified image.
  }
  group.2 {
    name = 3D processing
    0.name = disparity
    0.type = stereo_msgs/DisparityImage
    0.desc = Floating point disparity image with metadata.
    1.name = points2
    1.type = sensor_msgs/PointCloud2
    1.desc = Stereo point cloud with RGB color.
    2.name = points
    2.type = sensor_msgs/PointCloud
    2.desc = Stereo point cloud with RGB color. This message type is obsoleted by <<MsgLink(sensor_msgs/PointCloud2)>>; if possible, use the `points2` topic instead.
  }
}
```

 

```clearsilver
param {
  group.0 {
    name = Disparity pre-filtering
    0.name = ~prefilter_size
    0.type = int
    0.desc = Normalization window size, pixels.
    0.default = 9
    1.name = ~prefilter_cap
    1.type = int
    1.desc = Bound on normalized pixel values.
    1.default = 31
  }
  group.1 {
    name = Disparity correlation
    0.name = ~correlation_window_size
    0.type = int
    0.desc = Edge size (pixels) of the correlation window for matching. Values must be odd, in the range 5 to 255 (but with an extra performance hit for values larger than 21). Larger values have smoother disparity results, but smear out small features and depth discontinuities.
    0.default = 15
    1.name = ~min_disparity
    1.type = int
    1.desc = Minimum disparity, or the offset to the disparity search window. By setting to a positive value, the cameras become more "cross-eyed" and will find objects closer to the cameras. If the cameras are "verged" (inclined toward each other), it may be appropriate to set `min_disparity` to a negative value. When `min_disparity` is greater than 0, objects at large distances will not be found.
    1.default = 0
    2.name = ~disparity_range
    2.type = int
    2.desc = The size of the disparity search window (pixels). Together with `min_disparity`, this defines the "horopter," the 3D volume that is visible to the stereo algorithm.
    2.default = 64
  }
  group.2 {
    name = Disparity post-filtering
    0.name = ~uniqueness_ratio
    0.type = double
    0.desc = Filters disparity readings based on a comparison to the next-best correlation along the epipolar line. Matches where `uniqueness_ratio > (best_match - next_match) / next_match` are filtered out.
    0.default = 15.0
    1.name = ~texture_threshold
    1.type = int
    1.desc = Filters disparity readings based on the amount of texture in the correlation window.
    1.default = 10
    2.name = ~speckle_size
    2.type = int
    2.desc = Filters disparity regions that are less than this number of pixels.  For example, a value of 100 means that all regions with fewer than 100 pixels will be rejected.
    2.default = 100
    3.name = ~speckle_range
    3.type = int
    3.desc = Groups disparity regions based on their connectedness. Disparities are grouped together in the same region if they are within this distance in pixels.
    3.default = 4
  }
  group.4 {
    name = Synchronization
    0.name = ~approximate_sync
    0.type = bool
    0.desc = Whether to use approximate synchronization. Set to true if the left and right cameras do not produce exactly synced timestamps.
    0.default = false
    1.name = ~queue_size
    1.type = int
    1.desc = Size of message queue for each synchronized topic. You may need to raise this if images take significantly longer to travel over the network than camera info and/or the delay from disparity processing is too long.
    1.default = 5
  }
}
```



## Nodelets

This package contains [nodelets](nodelet) for creating disparity images
and point clouds from stereo. This allows `stereo_image_proc`
functions to be easily combined with other nodelets, for example camera
drivers or higher-level vision processing. In fact, the
`stereo_image_proc` node simply loads a combination of nodelets.



```clearsilver
node {
  name = stereo_image_proc/disparity
  desc = Performs block matching on a pair of rectified stereo images, producing a disparity image.
  sub {
    0.name = left/image_rect
    0.type = sensor_msgs/Image
    0.desc = Left monochrome rectified image stream.
    1.name = left/camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = Left camera metadata.
    2.name = right/image_rect
    2.type = sensor_msgs/Image
    2.desc = Right monochrome rectified image stream.
    3.name = right/camera_info
    3.type = sensor_msgs/CameraInfo
    3.desc = Right camera metadata.
  }
  pub {
    0.name = disparity
    0.type = stereo_msgs/DisparityImage
    0.desc = Floating point disparity image with metadata.
  }
  param {
    0.name = ~approximate_sync
    0.type = bool
    0.desc = Whether to use approximate synchronization. Set to true if the left and right cameras do not produce exactly synced timestamps.
    0.default = false
    1.name = ~queue_size
    1.type = int
    1.desc = Size of message queue for each synchronized topic. You may need to raise this if images take significantly longer to travel over the network than camera info and/or the delay from disparity processing is too long.
    1.default = 5
  }
}
```





```clearsilver
param {
  group.0 {
    name = Disparity pre-filtering
    0.name = ~prefilter_size
    0.type = int
    0.desc = Normalization window size, pixels.
    0.default = 9
    1.name = ~prefilter_cap
    1.type = int
    1.desc = Bound on normalized pixel values.
    1.default = 31
  }
  group.1 {
    name = Disparity correlation
    0.name = ~correlation_window_size
    0.type = int
    0.desc = Edge size (pixels) of the correlation window for matching. Values must be odd, in the range 5 to 255 (but with an extra performance hit for values larger than 21). Larger values have smoother disparity results, but smear out small features and depth discontinuities.
    0.default = 15
    1.name = ~min_disparity
    1.type = int
    1.desc = Minimum disparity, or the offset to the disparity search window. By setting to a positive value, the cameras become more "cross-eyed" and will find objects closer to the cameras. If the cameras are "verged" (inclined toward each other), it may be appropriate to set `min_disparity` to a negative value. When `min_disparity` is greater than 0, objects at large distances will not be found.
    1.default = 0
    2.name = ~disparity_range
    2.type = int
    2.desc = The size of the disparity search window (pixels). Together with `min_disparity`, this defines the "horopter," the 3D volume that is visible to the stereo algorithm.
    2.default = 64
  }
  group.2 {
    name = Disparity post-filtering
    0.name = ~uniqueness_ratio
    0.type = double
    0.desc = Filters disparity readings based on a comparison to the next-best correlation along the epipolar line. Matches where `uniqueness_ratio > (best_match - next_match) / next_match` are filtered out.
    0.default = 15.0
    1.name = ~texture_threshold
    1.type = int
    1.desc = Filters disparity readings based on the amount of texture in the correlation window.
    1.default = 10
    2.name = ~speckle_size
    2.type = int
    2.desc = Filters disparity regions that are less than this number of pixels.  For example, a value of 100 means that all regions with fewer than 100 pixels will be rejected.
    2.default = 100
    3.name = ~speckle_range
    3.type = int
    3.desc = Groups disparity regions based on their connectedness. Disparities are grouped together in the same region if they are within this distance in pixels.
    3.default = 4
  }
  group.4 {
    name = Synchronization
    0.name = ~approximate_sync
    0.type = bool
    0.desc = Whether to use approximate synchronization. Set to true if the left and right cameras do not produce exactly synced timestamps.
    0.default = false
    1.name = ~queue_size
    1.type = int
    1.desc = Size of message queue for each synchronized topic. You may need to raise this if images take significantly longer to travel over the network than camera info and/or the delay from disparity processing is too long.
    1.default = 5
  }
}
```





```clearsilver
node.0 {
  name = stereo_image_proc/point_cloud2
  desc = Combines a rectified color image and disparity image to produce a point cloud.
  sub {
    0.name = left/image_rect_color
    0.type = sensor_msgs/Image
    0.desc = Left color rectified image stream.
    1.name = left/camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = Left camera metadata.
    2.name = right/camera_info
    2.type = sensor_msgs/CameraInfo
    2.desc = Right camera metadata.
    3.name = disparity
    3.type = stereo_msgs/DisparityImage
    3.desc = Floating point disparity image with metadata.
  }
  pub {
    0.name = points2
    0.type = sensor_msgs/PointCloud2
    0.desc = Stereo point cloud with RGB color.
  }
  param {
    0.name = ~approximate_sync
    0.type = bool
    0.desc = Whether to use approximate synchronization. Set to true if the left and right cameras do not produce exactly synced timestamps.
    0.default = false
    1.name = ~queue_size
    1.type = int
    1.desc = Size of message queue for each synchronized topic. You may need to raise this if images take significantly longer to travel over the network than camera info and/or the delay from disparity processing is too long.
    1.default = 5
  }
}
node.1 {
  name = stereo_image_proc/point_cloud
  desc = Combines a rectified color image and disparity image to produce a <<MsgLink(sensor_msgs/PointCloud)>>. Provided for backwards compatibility; this message type is obsoleted by <<MsgLink(sensor_msgs/PointCloud2)>>.
  sub {
    0.name = left/image_rect_color
    0.type = sensor_msgs/Image
    0.desc = Left color rectified image stream.
    1.name = left/camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = Left camera metadata.
    2.name = right/camera_info
    2.type = sensor_msgs/CameraInfo
    2.desc = Right camera metadata.
    3.name = disparity
    3.type = stereo_msgs/DisparityImage
    3.desc = Floating point disparity image with metadata.
  }
  pub {
    0.name = points
    0.type = sensor_msgs/PointCloud
    0.desc = Stereo point cloud with RGB color.
  }
  param {
    0.name = ~approximate_sync
    0.type = bool
    0.desc = Whether to use approximate synchronization. Set to true if the left and right cameras do not produce exactly synced timestamps.
    0.default = false
    1.name = ~queue_size
    1.type = int
    1.desc = Size of message queue for each synchronized topic. You may need to raise this if images take significantly longer to travel over the network than camera info and/or the delay from disparity processing is too long.
    1.default = 5
  }
}
```



## Launch files



```clearsilver
name = stereo_image_proc.launch
desc << EOM
Loads the full constellation of `image_proc`/`stereo_image_proc` nodelets for one stereo camera pair into a user-provided nodelet manager. The in-process equivalent of running the `stereo_image_proc` node. Launch (or include in a higher-level launch file) in the camera namespace, just as you would run `stereo_image_proc`.
EOM
}
```



#### Arguments



```
$ ROS_NAMESPACE=stereo rosrun stereo_image_proc stereo_image_proc
```

0

#### Subscribed and Published Topics

Identical to the `stereo_image_proc` node.
