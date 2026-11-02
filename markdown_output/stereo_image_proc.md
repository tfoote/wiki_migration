## Overview

This package contains the `stereo_image_proc` node, which sits between
the stereo camera drivers and vision processing nodes.

`stereo_image_proc` performs the duties of
[image_proc](https://index.ros.org/p/image_proc) for both cameras,
undistorting and colorizing the raw images. Note that for properly
calibrated stereo cameras, undistortion is actually combined with
rectification, transforming the images so that their scanlines line up
for fast stereo processing.

`stereo_image_proc` will also compute disparity images from incoming
stereo pairs using
[OpenCV's block matching](https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html#stereobm)
algorithm. These are best inspected using
[stereo_view](https://index.ros.org/p/image_view).

The node will also produce point clouds, which you can view in
[rviz](https://index.ros.org/p/rviz), and process with [pcl](pcl).

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- ------------------------------------------------------------------------------------------------------------ --
                                                                                                                                                                                                                           <tablestyle="width: 99%">**Stereo processing example**                                                   
     ![Raw images](doc/raw.png)                                                                                                                                                                                                                                                                                                         
     **left/image_raw**, **right/image_raw**: The raw images from each camera.                                                                                                                                                                                                                                                          
     ![Stereo images](doc/epipolar.png)                                                                                                                                                                                    ![Disparity image](doc/disparity.jpg)                                                                        
     **left/image_rect_color**, **right/image_rect_color**: The rectified images from each camera. The red lines show that the same point in the real world lies on the same horizontal line in each rectified image.      **disparity**: The resulting disparity map, as shown by [stereo_view](https://index.ros.org/p/image_view).   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- ------------------------------------------------------------------------------------------------------------ --

## Tutorials

- [Choosing Good Stereo Parameters](#choosing-good-stereo-parameters):
  This tutorial walks you through a real-world example of tuning a
  running stereo_image_proc instance
  to get the best stereo results, using
  [stereo_view](https://index.ros.org/p/image_view) and
  [rviz](https://index.ros.org/p/rviz) for visual feedback.
- [Using OpenCV with Image Processing](#using-opencv-with-image-processing):
  A setup and initialization guide to using an OpenCV node with
  [image_pipeline](https://index.ros.org/p/image_pipeline).
- Also see
  [dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure) to
  set camera and stereo parameters on line.

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
[image_proc](https://index.ros.org/p/image_proc) instances in the
`stereo/left` and `stereo/right` namespaces, with the addition of
stereo outputs: disparity images (`stereo/disparity`) and point clouds
(`stereo/points2`).

In a separate terminal (on your home machine, if you are running on a
robot or cart): 

```
$ rosrun image_view image_view image:=/stereo/left/image_rect_color
```



This will display a rectified color image from the left stereo camera.
Alternatively, [stereo_view](https://index.ros.org/p/image_view) will
show you both the left and right images as well as a color-mapped
disparity image: 

```
$ rosrun image_view stereo_view stereo:=/stereo image:=image_rect_color
```



To view point clouds, you can use [rviz](https://index.ros.org/p/rviz).

## Nodes

### stereo_image_proc

![stereo_image_proc.png](doc/stereo_image_proc.png)

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
Right, Y Down, Z out). ![stereo_frames.png](doc/stereo_frames.png)

[image_transport](https://index.ros.org/p/image_transport) is used for
all image publications and subscriptions.

#### Subscribed Topics

##### Left camera

- `left/image_raw`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Raw image stream from the left camera.
- `left/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Left camera metadata.

##### Right camera

- `right/image_raw`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Raw image stream from the right camera.
- `right/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Right camera metadata.

#### Published Topics

##### Left camera processed images

- `left/image_mono`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Left monochrome unrectified image.
- `left/image_rect`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Left monochrome rectified image.
- `left/image_color`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Left color unrectified image.
- `left/image_rect_color`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Left color rectified image.

##### Right camera processed images

- `right/image_mono`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Right monochrome unrectified image.
- `right/image_rect`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Right monochrome rectified image.
- `right/image_color`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Right color unrectified image.
- `right/image_rect_color`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Right color rectified image.

##### 3D processing

- `disparity`
  ([stereo_msgs/msg/DisparityImage](https://docs.ros.org/en/rolling/p/stereo_msgs/msg/DisparityImage.html)):
  Floating point disparity image with metadata.
- `points2`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  Stereo point cloud with RGB color.
- `points`
  ([sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)):
  Stereo point cloud with RGB color. This message type is obsoleted by
  [sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html);
  if possible, use the `points2` topic instead.

#### Parameters

##### Disparity pre-filtering

- `~prefilter_size` (`int`, default: `9`): Normalization window size,
  pixels.
- `~prefilter_cap` (`int`, default: `31`): Bound on normalized pixel
  values.

##### Disparity correlation

- `~correlation_window_size` (`int`, default: `15`): Edge size (pixels)
  of the correlation window for matching. Values must be odd, in the
  range 5 to 255 (but with an extra performance hit for values larger
  than 21). Larger values have smoother disparity results, but smear out
  small features and depth discontinuities.
- `~min_disparity` (`int`, default: `0`): Minimum disparity, or the
  offset to the disparity search window. By setting to a positive value,
  the cameras become more "cross-eyed" and will find objects closer to
  the cameras. If the cameras are "verged" (inclined toward each
  other), it may be appropriate to set `min_disparity` to a negative
  value. When `min_disparity` is greater than 0, objects at large
  distances will not be found.
- `~disparity_range` (`int`, default: `64`): The size of the disparity
  search window (pixels). Together with `min_disparity`, this defines
  the "horopter," the 3D volume that is visible to the stereo
  algorithm.

##### Disparity post-filtering

- `~uniqueness_ratio` (`double`, default: `15.0`): Filters disparity
  readings based on a comparison to the next-best correlation along the
  epipolar line. Matches where `uniqueness_ratio > (best_match -
  next_match) / next_match` are filtered out.
- `~texture_threshold` (`int`, default: `10`): Filters disparity
  readings based on the amount of texture in the correlation window.
- `~speckle_size` (`int`, default: `100`): Filters disparity regions
  that are less than this number of pixels. For example, a value of 100
  means that all regions with fewer than 100 pixels will be rejected.
- `~speckle_range` (`int`, default: `4`): Groups disparity regions based
  on their connectedness. Disparities are grouped together in the same
  region if they are within this distance in pixels.

##### Synchronization

- `~approximate_sync` (`bool`, default: `false`): Whether to use
  approximate synchronization. Set to true if the left and right cameras
  do not produce exactly synced timestamps.
- `~queue_size` (`int`, default: `5`): Size of message queue for each
  synchronized topic. You may need to raise this if images take
  significantly longer to travel over the network than camera info
  and/or the delay from disparity processing is too long.

## Nodelets

This package contains [nodelets](https://index.ros.org/p/nodelet) for
creating disparity images and point clouds from stereo. This allows
`stereo_image_proc` functions to be easily combined with other
nodelets, for example camera drivers or higher-level vision processing.
In fact, the `stereo_image_proc` node simply loads a combination of
nodelets.

### stereo_image_proc/disparity

Performs block matching on a pair of rectified stereo images, producing
a disparity image.

#### Subscribed Topics

- `left/image_rect`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Left monochrome rectified image stream.
- `left/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Left camera metadata.
- `right/image_rect`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Right monochrome rectified image stream.
- `right/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Right camera metadata.

#### Published Topics

- `disparity`
  ([stereo_msgs/msg/DisparityImage](https://docs.ros.org/en/rolling/p/stereo_msgs/msg/DisparityImage.html)):
  Floating point disparity image with metadata.

#### Parameters

- `~approximate_sync` (`bool`, default: `false`): Whether to use
  approximate synchronization. Set to true if the left and right cameras
  do not produce exactly synced timestamps.
- `~queue_size` (`int`, default: `5`): Size of message queue for each
  synchronized topic. You may need to raise this if images take
  significantly longer to travel over the network than camera info
  and/or the delay from disparity processing is too long.

#### Parameters

##### Disparity pre-filtering

- `~prefilter_size` (`int`, default: `9`): Normalization window size,
  pixels.
- `~prefilter_cap` (`int`, default: `31`): Bound on normalized pixel
  values.

##### Disparity correlation

- `~correlation_window_size` (`int`, default: `15`): Edge size (pixels)
  of the correlation window for matching. Values must be odd, in the
  range 5 to 255 (but with an extra performance hit for values larger
  than 21). Larger values have smoother disparity results, but smear out
  small features and depth discontinuities.
- `~min_disparity` (`int`, default: `0`): Minimum disparity, or the
  offset to the disparity search window. By setting to a positive value,
  the cameras become more "cross-eyed" and will find objects closer to
  the cameras. If the cameras are "verged" (inclined toward each
  other), it may be appropriate to set `min_disparity` to a negative
  value. When `min_disparity` is greater than 0, objects at large
  distances will not be found.
- `~disparity_range` (`int`, default: `64`): The size of the disparity
  search window (pixels). Together with `min_disparity`, this defines
  the "horopter," the 3D volume that is visible to the stereo
  algorithm.

##### Disparity post-filtering

- `~uniqueness_ratio` (`double`, default: `15.0`): Filters disparity
  readings based on a comparison to the next-best correlation along the
  epipolar line. Matches where `uniqueness_ratio > (best_match -
  next_match) / next_match` are filtered out.
- `~texture_threshold` (`int`, default: `10`): Filters disparity
  readings based on the amount of texture in the correlation window.
- `~speckle_size` (`int`, default: `100`): Filters disparity regions
  that are less than this number of pixels. For example, a value of 100
  means that all regions with fewer than 100 pixels will be rejected.
- `~speckle_range` (`int`, default: `4`): Groups disparity regions based
  on their connectedness. Disparities are grouped together in the same
  region if they are within this distance in pixels.

##### Synchronization

- `~approximate_sync` (`bool`, default: `false`): Whether to use
  approximate synchronization. Set to true if the left and right cameras
  do not produce exactly synced timestamps.
- `~queue_size` (`int`, default: `5`): Size of message queue for each
  synchronized topic. You may need to raise this if images take
  significantly longer to travel over the network than camera info
  and/or the delay from disparity processing is too long.

### stereo_image_proc/point_cloud2

Combines a rectified color image and disparity image to produce a point
cloud.

#### Subscribed Topics

- `left/image_rect_color`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Left color rectified image stream.
- `left/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Left camera metadata.
- `right/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Right camera metadata.
- `disparity`
  ([stereo_msgs/msg/DisparityImage](https://docs.ros.org/en/rolling/p/stereo_msgs/msg/DisparityImage.html)):
  Floating point disparity image with metadata.

#### Published Topics

- `points2`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  Stereo point cloud with RGB color.

#### Parameters

- `~approximate_sync` (`bool`, default: `false`): Whether to use
  approximate synchronization. Set to true if the left and right cameras
  do not produce exactly synced timestamps.
- `~queue_size` (`int`, default: `5`): Size of message queue for each
  synchronized topic. You may need to raise this if images take
  significantly longer to travel over the network than camera info
  and/or the delay from disparity processing is too long.

### stereo_image_proc/point_cloud

Combines a rectified color image and disparity image to produce a
[sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html).
Provided for backwards compatibility; this message type is obsoleted by
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html).

#### Subscribed Topics

- `left/image_rect_color`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Left color rectified image stream.
- `left/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Left camera metadata.
- `right/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Right camera metadata.
- `disparity`
  ([stereo_msgs/msg/DisparityImage](https://docs.ros.org/en/rolling/p/stereo_msgs/msg/DisparityImage.html)):
  Floating point disparity image with metadata.

#### Published Topics

- `points`
  ([sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)):
  Stereo point cloud with RGB color.

#### Parameters

- `~approximate_sync` (`bool`, default: `false`): Whether to use
  approximate synchronization. Set to true if the left and right cameras
  do not produce exactly synced timestamps.
- `~queue_size` (`int`, default: `5`): Size of message queue for each
  synchronized topic. You may need to raise this if images take
  significantly longer to travel over the network than camera info
  and/or the delay from disparity processing is too long.

## Launch files

### stereo_image_proc.launch

Loads the full constellation of `image_proc`/`stereo_image_proc`
nodelets for one stereo camera pair into a user-provided nodelet
manager. The in-process equivalent of running the `stereo_image_proc`
node. Launch (or include in a higher-level launch file) in the camera
namespace, just as you would run `stereo_image_proc`.

#### Arguments

- `manager` (`string`): The name of the target nodelet manager. It will
  need to be globally qualified (e.g. `/my_manager`), unless the
  manager is already in the stereo namespace.
- `respawn` (`bool`, default: `false`): If true, enables bond topics and
  respawns any nodelet loaders that die. If the manager also respawns,
  the system is robust to any node dying. However, the proliferation of
  bond topics can overwhelm introspection tools like
  [rqt_graph](https://index.ros.org/p/rqt_graph).

##### Remapping

- `left` (`string`, default: `left`): Remap the 'left' camera
  namespace.
- `right` (`string`, default: `right`): Remap the 'right' camera
  namespace.

#### Subscribed and Published Topics

Identical to the `stereo_image_proc` node.

## Choosing Good Stereo Parameters

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Recording and playing back data](http://www.ros.org/wiki/rosbag/Tutorials/Recording%20and%20playing%20back%20data).
- **Description:** This tutorial walks you through a real-world example
  of tuning a running
  stereo_image_proc instance to get
  the best stereo results, using
  [stereo_view](https://index.ros.org/p/image_view) and
  [rviz](https://index.ros.org/p/rviz) for visual feedback.
- **Tutorial Level:** BEGINNER

### Preliminaries

Make sure you've built these packages:



```
$ rosmake stereo_image_proc image_view dynamic_reconfigure
```

 We will use the stereo camera data recorded in
<http://download.ros.org/data/stereo_image_proc/rotating_detergent_1_6.bag>
(270 MB) in this tutorial.

We need to know what namespace to start `stereo_image_proc` in, so
let's see what topics we've got in the bag:



```
$ rosbag info rotating_detergent_1_6.bag
...
topics:      /narrow_stereo_textured/left/camera_info    437 msgs @ 14.7 Hz : sensor_msgs/CameraInfo
             /narrow_stereo_textured/left/image_raw      437 msgs @ 14.7 Hz : sensor_msgs/Image
             /narrow_stereo_textured/right/camera_info   437 msgs @ 14.7 Hz : sensor_msgs/CameraInfo
             /narrow_stereo_textured/right/image_raw     437 msgs @ 14.7 Hz : sensor_msgs/Image
```

 Or better yet, use
[rqt_bag](https://index.ros.org/p/rqt_bag):



```
$ rqt_bag rotating_detergent_1_6.bag
```


![attachment:rqtbag_stereo.png](doc/rqtbag_stereo.png)

Our stereo namespace is `narrow_stereo_textured`. This particular bag
contains images of a detergent bottle rotating on a pan-tilt table. The
data is from the narrow stereo camera on a PR2 robot, with the textured
light projector running to add texture to the scene. Without this
artificial texture, stereo correlation would fail on blank regions like
the walls and tabletop.

### Start the stereo processing node

When we launch `stereo_image_proc` in the `narrow_stereo_textured`
namespace, it will automatically connect to our camera topics:



```
$ ROS_NAMESPACE=narrow_stereo_textured rosrun stereo_image_proc stereo_image_proc
```

 We will use
[dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure) to
change the stereo processing parameters on the fly. Launch the
reconfigure GUI:



```
$ rosrun rqt_reconfigure rqt_reconfigure
reconfigure_gui started
```

 In the drop-down menu, choose
`/narrow_stereo_textured/stereo_image_proc_XXX`. You should see:

![attachment:reconfigure_stereo.png](doc/reconfigure_stereo.png)

Make sure that your settings match the defaults shown above.

#### What do those parameters mean?

The parameters control various aspects of the block matching algorithm
used by `stereo_image_proc` to find correspondences between the left
and right images. The algorithm has three phases:

1\. Pre-filtering to normalize image brightness and enhance texture. 1.
Correspondence search along horizontal epipolar lines using an SAD
window. 1. Post-filtering to eliminate bad correspondence matches.

Brief descriptions of each parameter can be found in the
`stereo_image_proc`
[parameter listing](#stereo_image_proc).
In this tutorial we'll take a hands-on approach to learning what the
parameters do.

For an in-depth discussion of the block matching algorithm, see pages
438-444 of
[Learning OpenCV](http://www.amazon.com/Learning-OpenCV-Computer-Vision-Library/dp/0596516134).

### Start the visualization nodes

These nodes won't actually show anything until we play back the bag,
but we'll start them now anyway.

The best way to troubleshoot stereo issues is by looking at the
disparity image. The [stereo_view](https://index.ros.org/p/image_view)
utility will display a color-mapped version of the disparity image
alongside the left and right camera images:



```
$ rosrun image_view stereo_view stereo:=narrow_stereo_textured image:=image_rect
```

 Separate the three windows if necessary.

#### OPTIONAL: Start rviz

This tutorial will only assume that you're looking at the disparity
image, but viewing the stereo point cloud in
[rviz](https://index.ros.org/p/rviz) is also useful. If you've built
rviz, do:



```
$ rosrun rviz rviz
```

 In the Display panel click Add and choose Point
Cloud. Click on "Fill in topic here\..." then the button that appears
on the right of the text box. Choose the
`narrow_stereo_textured/points` topic. Since the bag doesn't contain
[tf](https://index.ros.org/p/tf) information, so you will need to set
the fixed and target frames to that of the camera,
`/narrow_stereo_optical_frame`.

### Start bag playback

Now we're ready to stream data into our system:



```
$ rosbag play rotating_detergent_1_6.bag -r 0.1
```

 This plays the bag at one-tenth speed so we
have time to tinker. All of the nodes we're running are stateless with
respect to time, so if the bag stops you can simply play it again. You
should now see data appear in your `stereo_view` (and `rviz`).

### My disparity image is blank!

Depending on your scene and stereo settings, you may encounter an empty
disparity image.

![width="33%"](doc/blank_disparity_left.png)
![width="33%"](doc/blank_disparity_right.png)
![width="33%"](doc/blank_disparity.png)

This means that one or more of the post-filtering thresholds is set too
high. The most likely culprit is `texture_threshold`, which filters
out areas that don't have enough texture for reliable matching. If you
move `texture_threshold` up and down, you should see the disparities
disappear and reappear. `texture_threshold=10` is the default and
tends to work well.

### What's this junk on the tabletop?

You should notice lots of little disparity blobs at apparently random
depths where the table and detergent should be.

![width="50%"](doc/table_junk_left.png)
![width="50%"](doc/table_junk_right.png)
![attachment:table_junk_disp.png](doc/table_junk_disp.png)

Block-based matchers often produce these "speckles" near the
boundaries of objects, where the matching window catches the foreground
on one side and the background on the other. In this scene it appears
that the matcher is also finding small spurious matches in the projected
texture on the table.

To get rid of these artifacts we post-process the disparity image with a
speckle filter controlled by the `speckle_size` and `speckle_range`
parameters. `speckle_size` is the number of pixels below which a
disparity blob is dismissed as "speckle." `speckle_range` controls
how close in value disparities must be to be considered part of the same
blob. In this case the objects in the scene are relatively large, so we
can crank `speckle_size` up to 1000 pixels:

![width="50%"](doc/despeckled_left.png)
![width="50%"](doc/despeckled_right.png)
![attachment:despeckled_disp.png](doc/despeckled_disp.png)

### But where are the table and object?

At this point we have a nice depth gradient for the wall behind the
pan-tilt table. But there is a gaping hole in our disparity image where
the table and detergent should be. What is going on?

The problem is that the table is too close to the camera for the stereo
block matcher (with the current settings) to "see" it. This is an
artifact of the way block matching works. For each pixel in the left
image, the matcher slides a window across some range of pixels in the
corresponding row of the right image, looking for the most similar
region. The search range is determined by two parameters:

- `disparity_range` is how many pixels to slide the window over. The
  larger it is, the larger the range of visible depths, but more
  computation is required.
- `min_disparity` controls the offset from the x-position of the left
  pixel at which to begin searching.

The block matcher can return disparities in the range `\[min_disparity,
min_disparity + disparity_range)`. Since depth is inversely
proportional to disparity, these two parameters determine the
*horopter*, or 3D volume covered by the search range. Objects outside
the horopter are invisible to the algorithm.

In this case the disparity search range is `\[0, 64)`. The table
contains disparities greater than 64, so it falls in front of the
horopter. Increasing `disparity_range` to 128 expands the horopter to
include the table:

![width="50%"](doc/detergent_left.png)
![width="50%"](doc/detergent_right.png)
![attachment:detergent_disp.png](doc/detergent_disp.png)

Notice the blank area to the left of the detergent bottle. That area is
visible to the left camera but occluded by the bottle in the right
camera. You may notice that the empty left margin of the disparity image
has doubled in size; that is also related to `disparity_range`.

If you are running rviz, you can see the reconstructed 3D point cloud:

![attachment:detergent_rviz.png](doc/detergent_rviz.png)

`min_disparity` is normally set to zero, meaning the block matcher can
"see" out to infinity. If you have a pair of stereo cameras that are
*verged*, or inclined towards each other, it's possible to have
negative disparities and you might set `min_disparity` to a negative
value. If you want to detect objects very close to the camera (disparity
> 128), you could set `min_disparity` to a positive value, shifting
the horopter towards the camera and sacrificing far-field for near-field
perception.

For example, try dropping `disparity_range` to 96 and incrementally
increase `min_disparity`. Around `min_disparity = 50` you should see
the table and detergent fade into view and the wall behind them fade
out:

![width="50%"](doc/horopter_left.png)
![width="50%"](doc/horopter_right.png)
![attachment:horopter_disp.png](doc/horopter_disp.png)

### Other parameters

It's less likely that you'll need to tweak parameters that haven't
already been mentioned above. For the sake of completeness:

`correlation_window_size` controls the size of the sliding SAD (sum of
absolute differences) window used to find matching points between the
left and right images. Larger window sizes will smooth over small gaps
in the disparity image but will also smear object boundaries. The
default (15x15) is normally adequate; for comparison, this disparity
image used `correlation_window_size = 9` and has more gaps:

![attachment:correlation_gaps.png](doc/correlation_gaps.png)

`uniqueness_ratio` controls another post-filtering step. If the best
matching disparity is not sufficiently better than every other disparity
in the search range, the pixel is filtered out. You can try tweaking
this if `texture_threshold` and the speckle filtering are still
letting through spurious matches.

`prefilter_size` and `prefilter_cap` control the pre-filtering
phase, which normalizes image brightness and enhances texture in
preparation for block matching. Normally you should not need to adjust
these.

### Conclusion

Congrats! Now you are prepared to use `stereo_image_proc` with your
own stereo camera.

### Further improve the result

With post-filtering offered by OpenCV3, the disparity image can be more
smooth and have less
fragment.[link](http://docs.opencv.org/3.1.0/d3/d14/tutorial_ximgproc_disparity_filtering.html)

Download the source code of
[image_pipeline](https://github.com/ros-perception/image_pipeline),
modify file and recompile it along with
[cv-bridge](http://wiki.ros.org/cv_bridge). Also, you should have
install OpenCV3 library.

## Using OpenCV with Image Processing

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [ROS Tutorials](ROS/Tutorials).
- **Description:** A setup and initialization guide to using an OpenCV
  node with [image_pipeline](https://index.ros.org/p/image_pipeline).
- **Keywords:** OpenCV, stereo vision, image pipeline
- **Tutorial Level:** BEGINNER

### Introduction

While [image_publisher](https://index.ros.org/p/image_publisher) is a
great tool and the [camera_drivers](camera_drivers) package contains a
great resources for using industrial cameras, like the
[Prosilica GigE](https://index.ros.org/p/prosilica_camera) and
[Firewire cameras](https://index.ros.org/p/camera1394), it lacks an easy
guide on how to use OpenCV. Enter: this guide.

### image_pipeline

The structure of the image processing pipeline remains unchanged, the
only difference is the use of the
[cv_camera](https://index.ros.org/p/cv_camera) node in lieu of another
camera driver. There will be two
[cv_camera](https://index.ros.org/p/cv_camera) nodes that each publish
[image_raw](https://index.ros.org/p/sensor_msgs) and
[camera_info](https://index.ros.org/p/sensor_msgs) topics. The
[image_pipeline](https://index.ros.org/p/image_pipeline) node,
stereo_image_proc will subscribe to
these topics and publish the usual data, including a disparity map and
pointcloud.

### Getting Started

Assuming that ROS is installed following the standard install procedure
for your operating system and a catkin workspace has been set up
according to the ROS tutorials, the next step is to install and setup
[OpenCV](https://index.ros.org/p/opencv3) and
[cv_bridge](https://index.ros.org/p/cv_bridge).

#### Project Folder

First make a project folder by entering the following commands into your
terminal:



```
>$ cd ~/catkin_ws/src
>$ mkdir cv_pipeline
>$ cd cv_pipeline
>$ mkdir src
>$ cd ~/catkin_ws
>$ catkin_make
```



This creates the source folder and related build folders.

#### Dependencies

The dependencies necessary for using OpenCV with image_pipeline are as
follows: 1. [opencv3](https://index.ros.org/p/opencv3) 2.
[cv_bridge](https://index.ros.org/p/cv_bridge) 3.
[image_transport](https://index.ros.org/p/image_transport) 4.
stereo_image_proc 5.
[image_view](https://index.ros.org/p/image_view) 6.
[nodelet](https://index.ros.org/p/nodelet) 7.
[cv_camera](https://index.ros.org/p/cv_camera) 8.
[camera_calibration](https://index.ros.org/p/camera_calibration)

These should be installed with `rosdep`: 

```
>$ rosdep install package_name
```


where `package_name` is the name of the package. For more help using
rosdep, check the wiki page or type `rosdep \--help` into the command
line interface.

#### Test System

A test system is created using `rosrun` to make sure that everything
is working and was installed correctly/no missing dependencies. Before
testing, make sure `roscore` is running at address 11311 through:


```
>$ roscore
```

 Then it is recommended that you open a new
terminal window and start `rqt_graph` through:


```
>$ rqt_graph
```

 This will enable you to look at the emerging
network map as you set it up. Before proceeding, check which topics are
being published with 

```
>$ rostopic list
```

 If nothing else is
running, you should only see 

```
/rosout
/rosout_agg
```

 Now you can begin
creating your image_pipeline nodes.

##### cv_camera

First, after both cameras are connected and ROS has been verified to be
running, test the `cv_camera` node through: 

```
>$ rosparam set cv_camera/device_id=0
>$ rosrun cv_camera cv_camera_node
```


This will initialize the first camera publisher with an OpenCV device id
of 0. To test to see if the topic is publishing, type


```
>$ rostopic list
```

 You should see 

```
/cv_camera/image_raw
/cv_camera/camera_info
```



##### image_view

To subscribe to the topics published by the `cv_camera_node` and
visualize the results, use the
[image_view](https://index.ros.org/p/image_view) node in the
`image_pipeline` stack.



```
>$ rosrun image_view image_view image:=/cv_camera/image_raw
```



This will allow you to view the image message data in a visual form.

#### Launch File

Of course, it is easier to set up a launch file. To do so, navigate to
the `cv_pipeline` project folder with `roscd`. Then use your editor
(e.g., `nano`, `vim`, or text editor of your choice) to create a
launch file (e.g., `cv_pipeline.launch`). Save this to your project
directory and open it for editing.

##### Camera Calibration

First the camera must be calibrated. To do so please follow either of
these guides:

For [monocular cameras](https://index.ros.org/p/camera_calibration).

For [stereo cameras](https://index.ros.org/p/camera_calibration).

After the camera(s) have been calibrated, the image processing pipeline
can be set up.

##### Monocular Image Processing

For monocular image processing the following is a sample launch file:


```xml
<launch>
  <!-- Argument for device id -->
  <arg
    name="cam1"
    value="0"
  />
  <!-- Publisher node -->
  <node
    pkg="cv_camera"
    type="cv_camera_node"
    name="camera1" 
    args="$(arg cam1)" >
    <remap from:="cv_camera/image_raw" to:="camera1/image_raw" />
  </node>
  <!-- Subscriber node -->
  <node
    pkg="image_proc"
    type="image_proc"
    name="image_proc" />
</launch>
```

 Save the file, and call it with the following
command: 

```
>$ roslaunch cv_pipeline cv_pipeline.launch
```

 This should bring both nodes up, and
the network map can be see through `rqt_graph` and the topic list
through `rostopic list`. Additionally, the visual data from the
`image_proc` node can be seen with: 

```
>$ rosrun image_view image_view image:=camera1/image_rect
```



##### Stereo Image Processing

For stereo image processing the following is a sample launch file:


```xml
<launch>
  <!-- Argument for device id -->
  <arg
    name="cam1"
    value="0"
  />
  <arg
    name="cam2"
    value="1"
  />
  <!-- Publisher node -->
  <node
    pkg="cv_camera"
    type="cv_camera_node"
    name="left" 
    args="$(arg cam1)" >
    <remap from:="left/image_raw" to:="stereo/left/image_raw" />
    <remap from:="left/camera_info" to:="stereo/left/camera_info" />
  </node>
<node
    pkg="cv_camera"
    type="cv_camera_node"
    name="right" 
    args="$(arg cam2)" >
    <remap from:="right/image_raw" to:="stereo/right/image_raw" />
    <remap from:="right/camera_info" to:="stereo/right/image_raw" />
  </node>
  <!-- Subscriber node -->
  <node
    pkg="stereo_image_proc"
    type="stereo_image_proc"
    name="stereo_image_proc" />
</launch>
```

 Save the file, and call it with the following
command: 

```
>$ roslaunch cv_pipeline cv_pipeline.launch
```

 This should bring all three nodes up,
and the network map can be see through `rqt_graph` and the topic list
through `rostopic list`. Additionally, the visual data from the
`stereo_image_proc` node can be seen with: 

```
>$ rosrun image_view stereo_view stereo:=/stereo image:=image_color
```


This should display both images side-by-side with the disparity image.

## Tutorials

- [Choosing Good Stereo Parameters](#choosing-good-stereo-parameters):
  This tutorial walks you through a real-world example of tuning a
  running stereo_image_proc instance
  to get the best stereo results, using
  [stereo_view](https://index.ros.org/p/image_view) and
  [rviz](https://index.ros.org/p/rviz) for visual feedback.
- [Using OpenCV with Image Processing](#using-opencv-with-image-processing):
  A setup and initialization guide to using an OpenCV node with
  [image_pipeline](https://index.ros.org/p/image_pipeline).
