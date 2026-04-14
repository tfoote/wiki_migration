![](attachment:pal_logo.png)

## Overview

Segmenting regions of interest in images is a wide field in Computer
Vision and Image Processing. Some methods include a kind of
pre-segmentation inside but there are some which can be boosted using
masks on the image or masked images. In this package we provide ROS
nodes to help with this image processing step.
![](attachment:disparity_k.jpg)
![](attachment:histogram_segmentation_orange_ball_k.png)

## ROS API

```clearsilver
name=disparity_segmentation
node {
  no_header=True
  0.name=disparity_segmentation 
  0.desc=Provides distance-based segmentation based on a disparity image computed using stereo cameras.
}
sub {
  0.name = disparity_image
  0.type = stereo_msgs/DisparityImage
  0.desc = Disparity image provided by [[http://www.ros.org/wiki/stereo_image_proc|stereo_img_proc]].
  1.name = image
  1.type = sensor_msgs/Image
  1.desc = '''Rectified''' image. The disparity image is computed with respect to that so the masking is being done on the rectified image.
  2.name = camera_info
  2.type = sensor_msgs/CameraInfo
  2.desc = Original camera info of the camera.
}
pub {
  0.name = image_masked
  0.type = sensor_msgs/Image
  0.desc = Masked '''rectified''' image.
  1.name = camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = Contains the camera info that corresponds to the '''rectified''' image. The disparity image is computed with respect to that so the masking is being done on the rectified image.
  2.name = mask
  2.type = sensor_msgs/Image
  2.desc = Mask.
}
```

```clearsilver
name=histogram_segmentation
node {
  no_header=True
  0.name=histogram_segmentation 
  0.desc='''Given a single image''' of the target object it provides histogram backprojection-based segmentation on a color image.
}
sub {
  0.name = image
  0.type = sensor_msgs/Image
  0.desc = Input color image.
}
pub {
  0.name = image_masked
  0.type = sensor_msgs/Image
  0.desc = Masked image.
  1.name = mask
  1.type = sensor_msgs/Image
  1.desc = Mask.
}
```

```clearsilver
name=template_segmentation
node {
  no_header=True
  0.name=template_segmentation 
  0.desc='''Given a single image''' of the target object it provides template matching-based segmentation on a color image.
}
sub {
  0.name = image
  0.type = sensor_msgs/Image
  0.desc = Input color image.
}
pub {
  0.name = image_masked
  0.type = sensor_msgs/Image
  0.desc = Masked image.
  1.name = mask
  1.type = sensor_msgs/Image
  1.desc = Mask.
}
```
