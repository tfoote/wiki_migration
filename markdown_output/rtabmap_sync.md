[Included page rtabmap_ros/menu not found](Included page rtabmap_ros/menu not found)

## Nodelets



```clearsilver
node {
  name = rtabmap_sync/rgbd_sync
  desc = Synchronize RGB, depth and camera_info messages into a single message. You can then use `subscribe_rgbd` to make `rtabmap` or odometry nodes subscribing to this message instead. This is useful when, for example, rtabmap is subscribed also to a laser scan or odometry topic published at different rate than the image topics. We can then make sure that images are correctly synchronized together. If you have camera publishing on the network, this can be also a good format to synchronize images before sending them on the network, to avoid synchronization issues when the network is lagging.
  sub {
    0.name = rgb/image
    0.type = sensor_msgs/Image
    0.desc = RGB image stream.
    1.name = depth/image
    1.type = sensor_msgs/Image
    1.desc = Registered depth image stream.
    2.name = rgb/camera_info
    2.type = sensor_msgs/CameraInfo
    2.desc = RGB camera metadata.
  }
  pub {
    0.name = rgbd_image
    0.type = rtabmap_msgs/RGBDImage
    0.desc = The RGB-D image topic
    1.name = rgbd_image/compressed
    1.type = rtabmap_msgs/RGBDImage
    1.desc = The compressed RGB-D image topic (rgb=jpeg, depth=png)
  }
  param {
    0.name = ~queue_size
    0.type = int
    0.desc = Size of message queue for each synchronized topic.
    0.default = 10
    1.name = ~approx_sync
    1.type = bool
    1.desc = Use approximate synchronization for the input topics. If false, the RGB and depth images and the camera info must have the same timestamp.
    1.default = `0`
    2.name = ~approx_sync_max_interval
    2.type = double
    2.desc = Max interval (sec) between topics to be synchronized (when `approx_sync` is false). 0 means infinite.
    2.default = `"True"`
    3.name = ~compressed_rate
    3.type = double
    3.desc = Throttling rate at which `rgbd_image/compressed` topic will be published. 0 means no throttling.
    3.default = 0
    4.name = ~depth_scale
    4.type = double
    4.desc = Can be used to re-scale the depth values of the depth image.
    4.default = `1.0`
    5.name = ~decimation
    5.type = int
    5.desc = Decimate resolution of the image while adjusting camera info values.
    5.default = `1`
  }
}
```





```clearsilver
node {
  name = rtabmap_sync/rgb_sync
  desc = Synchronize RGB and camera_info messages into a single message. You can then use `subscribe_rgbd` to make `rtabmap` or odometry nodes subscribing to this message instead. This is useful when, for example, rtabmap is subscribed also to a laser scan or odometry topic published at different rate than the image topics. We can then make sure that images are correctly synchronized together. If you have camera publishing on the network, this can be also a good format to synchronize images before sending them on the network, to avoid synchronization issues when the network is lagging.
  sub {
    0.name = rgb/image
    0.type = sensor_msgs/Image
    0.desc = RGB image stream.
    1.name = rgb/camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = RGB camera metadata.
  }
  pub {
    0.name = rgbd_image
    0.type = rtabmap_msgs/RGBDImage
    0.desc = The RGB-D image topic
    1.name = rgbd_image/compressed
    1.type = rtabmap_msgs/RGBDImage
    1.desc = The compressed RGB-D image topic (rgb=jpeg, depth=png)
  }
  param {
    0.name = ~queue_size
    0.type = int
    0.desc = Size of message queue for each synchronized topic.
    0.default = 10
    1.name = ~approx_sync
    1.type = bool
    1.desc = Use approximate synchronization for the input topics. If false, the RGB and depth images and the camera info must have the same timestamp.
    1.default = `"False"`
    2.name = ~compressed_rate
    2.type = double
    2.desc = Throttling rate at which `rgbd_image/compressed` topic will be published. 0 means no throttling.
    2.default = 0
  }
}
```





```clearsilver
node {
  name = rtabmap_sync/stereo_sync
  desc = Synchronize left image, right image and camera_info messages into a single message. You can then use `subscribe_rgbd` to make `rtabmap` or odometry nodes subscribing to this message instead. This is useful when, for example, rtabmap is subscribed also to a laser scan or odometry topic published at different rate than the image topics. We can then make sure that images are correctly synchronized together. If you have camera publishing on the network, this can be also a good format to synchronize images before sending them on the network, to avoid synchronization issues when the network is lagging.
  sub {
    0.name = left/image_rect
    0.type = sensor_msgs/Image
    0.desc = Left image stream.
    1.name = right/image_rect
    1.type = sensor_msgs/Image
    1.desc = Right image stream.
    2.name = left/camera_info
    2.type = sensor_msgs/CameraInfo
    2.desc = Left camera metadata.
    3.name = right/camera_info
    3.type = sensor_msgs/CameraInfo
    3.desc = Right camera metadata.
  }
  pub {
    0.name = rgbd_image
    0.type = rtabmap_msgs/RGBDImage
    0.desc = The RGB-D image topic. The RGB field is the left image and the depth field is the right image, with corresponding camera info.
    1.name = rgbd_image/compressed
    1.type = rtabmap_msgs/RGBDImage
    1.desc = The compressed RGB-D image topic (images compressed in jpeg). The RGB field is the left image and the depth field is the right image, with corresponding camera info.
  }
  param {
    0.name = ~queue_size
    0.type = int
    0.desc = Size of message queue for each synchronized topic.
    0.default = 10
    1.name = ~approx_sync
    1.type = bool
    1.desc = Use approximate synchronization for the input topics. If false, the left image, right image and the camera info must have the same timestamp (which should be always the case for stereo images).
    1.default = `"False"`
    2.name = ~compressed_rate
    2.type = double
    2.desc = Throttling rate at which `rgbd_image/compressed` topic will be published. 0 means no throttling.
    2.default = 0
  }
}
```





```clearsilver
node {
  name = rtabmap_sync/rgbdx_sync
  desc = Synchronize up to 8 [[http://docs.ros.org/en/api/rtabmap_msgs/html/msg/RGBDImage.html|rtabmap_msgs/RGBDImage]] into a single message [[http://docs.ros.org/en/api/rtabmap_msgs/html/msg/RGBDImages.html|rtabmap_msgs/RGBDImages]]. You can then use `subscribe_rgbd` with `rgbd_cameras=0` to make `rtabmap` or odometry nodes subscribing to this message instead. Input topics should be all RGB-D or all stereo, we cannot mix RGB-D + stereo cameras, and they should have all the same resolution.
  sub {
    0.name = rgbd_image0
    0.type = rtabmap_msgs/RGBDImage
    0.desc = RGBD/Stereo image stream.
    1.name = rgbd_image1
    1.type = rtabmap_msgs/RGBDImage
    1.desc = RGBD/Stereo image stream.
    2.name = rgbd_image2
    2.type = rtabmap_msgs/RGBDImage
    2.desc = RGBD/Stereo image stream.
    3.name = rgbd_image3
    3.type = rtabmap_msgs/RGBDImage
    3.desc = RGBD/Stereo image stream.
    4.name = rgbd_image4
    4.type = rtabmap_msgs/RGBDImage
    4.desc = RGBD/Stereo image stream.
    5.name = rgbd_image5
    5.type = rtabmap_msgs/RGBDImage
    5.desc = RGBD/Stereo image stream.
    6.name = rgbd_image6
    6.type = rtabmap_msgs/RGBDImage
    6.desc = RGBD/Stereo image stream.
    7.name = rgbd_image7
    7.type = rtabmap_msgs/RGBDImage
    7.desc = RGBD/Stereo image stream.
  }
  pub {
    0.name = rgbd_images
    0.type = rtabmap_msgs/RGBDImages
    0.desc = The RGB-D images topic
  }
  param {
    0.name = ~queue_size
    0.type = int
    0.desc = Size of message queue for each synchronized topic.
    0.default = 10
    1.name = ~approx_sync
    1.type = bool
    1.desc = Use approximate synchronization for the input topics. If false, the RGB and depth images and the camera info must have the same timestamp.
    1.default = `"True"`
    2.name = ~approx_sync_max_interval
    2.type = double
    2.desc = Maximum interval for approximate synchronization
    2.default = 0.0
    3.name = ~rgbd_cameras
    3.type = int
    3.desc = Number of cameras to synchronize (>=2 and <=8).
    3.default = 2
  }
}
```


