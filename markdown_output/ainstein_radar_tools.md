## Overview

## Nodes



```clearsilver
node.0 {
name = radar_camera_validation_node
desc = Subscribes to input camera image and radar data topics, draws bounding boxes on the image corresponding to radar data for validation, and publishes the annotated image.
sub {
  0.name = radar_topic
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Radar detections (targets) to be used for in annotating the input image.
  1.name = camera_topic
  1.type = sensor_msgs/Image
  1.desc = Name of the camera topic corresponding to the input image to annotate with radar data. It is assumed that both sensor_msgs/Image and sensor_msgs/CameraInfo messages are published within this topic's namespace.
}
pub {
  0.name = ~image_out
  0.type = sensor_msgs/Image
  0.desc = Annotated output image.
}
param {
  0.name = ~use_snr_alpha
  0.type = boolean
  0.desc = Specifies whether to set target transparency based on SNR.
  0.default = false
}
req_tf {
  0.from = <RADAR FRAME>
  0.to   = <CAMERA FRAME>
  0.desc = TF transform describing the transform between the radar sensor and camera frames.
}
}
```


