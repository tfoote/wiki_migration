```clearsilver
name = ros_cvb_camera_driver_node
desc = Publishes an image using the CVB camera driver by Stemmer Imaging.
sub {
  0.name = /jai_camera/image_raw
  0.type = sensor_msgs/ImageConstPtr
  0.desc = Camera topic
}
pub {
  0.name = /jai_camera/image_raw
  0.type = sensor_msgs/ImageConstPtr
  0.desc = Camera topic
  1.name = /jai_camera/camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = Camera info
}

param {
  0.name = camera_name
  0.type = string
  0.desc = Camera name
  0.default = jai_camera
  1.name = camera_info_url
  1.type = string
  1.desc = Url for camera info
}
```
