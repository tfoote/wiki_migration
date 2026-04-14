## ROS API

![](http://datamatrix.kaywa.com/img.php?s=12&d=IPA)

```clearsilver
name = cob_marker
desc = cob_marker allows to find 6DOF markers of different types, like datamatrix, Qr, natural landmarks, ... 
param {
  0.name = algorithm
  0.type = string
  0.desc = selects marker algorithm. possible values: zxing, dmtx
  1.name = tryHarder
  1.type = bool
  1.desc = try harder option of zxing
  2.name = dmtx_timeout
  2.type = int
  2.desc = timeout of marker recognition of dmtx (specifies how many markers can be recognized depending on the execution speed)
}

sub {
  0.name = /camera/rgb/image_color
  0.type = std_msgs/Image
  0.desc = color image
  1.name = /camera/depth/points
  1.type = std_msgs/Pointcloud2
  1.desc = pointcloud with depth data
  2.name = /camera/rgb/camera_info
  2.type = std_msgs/CameraInfo
  2.desc = instrinstric information about camera
}

goal{
 0.name=/object_detection/detect_object/goal
 0.type=cob_object_detection/DetectObjectsActionGoal
 0.desc=Goal for executing object detection procedure
}

result{
 0.name=/object_detection/detect_object/result
 0.type=cob_object_detection/DetectObjectsActionResult
 0.desc=List of detect object instances including a confidence and pose estimate
}

feedback{
 0.name=/object_detection/detect_object/feedback
 0.type=cob_object_detection/DetectObjectsActionFeedback
 0.desc=Feedback holds number to indicate the approximate progress
}
```

## Installation

Install zxing with C-Port and the development package of dmtx.

## Usage/Examples

Plug in Kinect or Kinect-style camera and start

`roslaunch cob_marker marker.launch`

cob_marker provides now an action on the topic
\"/cob_marker/object_detection\". Each action triggers marker
recognition to avoid high CPU usage. The usage of the action is the same
as with cob_object_detection.

## Algorithms

[zxing](http://code.google.com/p/zxing/) is the java implementation of
various kind of marker recognition (bar codes, Qr, datamatrix \...)

[dmtx](http://www.libdmtx.org/) only recognizes datamatrix. But it is
faster than zxing in general.

## Generate a marker code

<http://datamatrix.kaywa.com/>

permalink, e.g. for milk
<http://datamatrix.kaywa.com/img.php?s=39&d=milk>

Print it out with a size of around 20cm x 20cm.

<http://www.libdmtx.org/>
