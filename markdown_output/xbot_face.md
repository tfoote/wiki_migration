## Overview

Xbot_face is a face recognition ROS package for XBot-U robots. The
package has various functions such as face registration, face
management, face logout, and face recognition.

## Nodes



```clearsilver
name = face_recog
desc = The `face_recog` node provides face recognition function and outputs recognition results.
 sub {
0.name = /xbot/camera/image
0.type = sensor_msgs/Image
0.desc = Get the camera image data from this topic.
}

 pub {
   0.name = /xbot/face_result
   0.type = xbot_face/FaceResult
   0.desc = Get the face recognition result from this topic.
 }
```

 

```clearsilver
name = camera_image_publisher
desc = The `camera_image_publisher` node provides a `/xbot/camera/image` topic for publishing the image data obtained by the camera sensor.

 pub {
   0.name = /xbot/camera/image
   0.type = sensor_msgs/Image
   0.desc = Get the camera image data from this topic.
 }
```


