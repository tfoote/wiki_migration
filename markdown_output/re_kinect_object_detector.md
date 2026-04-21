## What does re_kinect_object_detector do?

Once you recorded a model using
[re_object_recorder](re_object_recorder), you can use
[re_kinect_object_detector](re_kinect_object_detector) to detect it
again in a point cloud.

See the tutorial
[roboearth/Tutorials/Using recorded models for object detection](roboearth/Tutorials/Using recorded models for object detection)
for a usage description.

## Interface



```clearsilver
name = re_kinect
desc = Main node for recognizing objects with the Kinect camera.
sub {
  0.name = camera/depth_registered/points
  0.type = sensor_msgs/PointCloud2
  0.desc = Input point cloud to in which to look for known objects (usually straight from [openni_node]).

  1.name = re_kinect/model_path
  1.type = std_msgs/String
  1.desc = Signals re_kinect to load the model stored at the given path.
}
pub {
  0.name = re_kinect/feature_pcl
  0.type = sensor_msgs/PointCloud2
  0.desc = The matched model aspect as point cloud.
  1.name = re_kinect/detection_results
  1.type = re_kinect_object_detector/DetectionResult
  1.desc = Announces detected objects along with the input image and detected object names.
}
prov_tf {
  0.from = /camera_rgb_optical_frame
  0.to = OBJECT_CLASS.OBJECT_NAME
  0.desc = Transformation from the camera frame to the object frame.
}
```


