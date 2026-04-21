## ROS API

![](http://datamatrix.kaywa.com/img.php?s=12&d=IPA)



```clearsilver
name = cob_datamatrix
desc = fakes object detection
param {
  0.name = triggermode
  0.type = bool
  0.desc = work as service if true, otherwise polling
  1.name = timeout
  1.type = int
  1.desc = break recognition if nothing was seen after n seconds in triggermode
}

sub {
  0.name = image_rgb
  0.type = std_msgs/Image
  0.desc = color image
  1.name = pointcloud_depth
  1.type = std_msgs/Pointcloud2
  1.desc = pointcloud with depth data
  2.name = camera_info
  2.type = std_msgs/CameraInfo
  2.desc = instrinstric information about camera
}
```



## Usage/Examples

Plug in Kinect or Kinect-style camera and start

`roslaunch cob_datamatrix  kinect.launch`

To trigger recognition start service with:

`rosrun cob_datamatrix test_trigger.py`

## Gererate a datamatrix code

<http://datamatrix.kaywa.com/>

permalink, e.g. for milk
<http://datamatrix.kaywa.com/img.php?s=39&d=milk>

Print it out with a size of around 20cm x 20cm.

<http://www.libdmtx.org/>
