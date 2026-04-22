## Goal

[Bag](Bags) files including camera images tend to be very large. To
reduce the overall size, this packages converts the camera images in the
bag file to videos and removes them from the bag file. The resulting bag
file and videos can be converted back to one [bag](Bags) file
afterwards.

## Approach

sensor_msgs/CameraInfo A [bag](Bags) file including
[sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html),
color and depth images, both of type
[sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html),
[wire_msgs/msg/WorldEvidence](https://docs.ros.org/en/rolling/p/wire_msgs/msg/WorldEvidence.html)
and
[tf/msg/tfMessage](https://docs.ros.org/en/rolling/p/tf/msg/tfMessage.html)
will be split into a number of video streams and a bag file. One video
stream for each of the topics from some image type and a bag file for
the remaining topics. In addition the package is able to merge the
resulting bag file and videos back into one large bag file again.

Adapting the package to work for your own bag file with different topics
can be done by simply adding or removing topics from the code.

## Launching the package

Various examples can be found in the [tutorials](wire/Tutorials) of the
[wire](wire) stack.

## Planning

The idea is to extend this package such that it works for a bag file
containing an arbitrary number of topics next to the image topics. There
is, however, no timeline associated with this idea.
