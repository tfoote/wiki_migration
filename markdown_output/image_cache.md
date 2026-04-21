![](attachment:republish.jpg) 

```clearsilver
name = image_cache
desc = The image cache node holds a central position in our architecture and serves multiple purposes detailed above.
sub {
  0.name = left/image_raw
  0.type = sensor_msgs/Image
  0.desc = Raw image stream from the left camera
  1.name = left/camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = Left camera metadata
  2.name = right/image_raw
  2.type = sensor_msgs/Image
  2.desc = Raw image stream from the right camera
  3.name = right/camera_info
  3.type = sensor_msgs/CameraInfo
  3.desc = Right camera metadata  
  4.name = node_added
  4.type = slam_backend/NodeAdded
  4.desc = Timestamp and Node ID of vertex newly added to the graph
}
pub {
  0.name = throttled_image_raw
  0.type = sensor_msgs/Image
  0.desc = Republished left image sampled at sub frame rate
}
srv {
  0.name = image_service
  0.type = image_cache/GetImage
  0.desc = Request any number of ''to'' images specified as matching a given ''from'' image using this service.  The caller node should specify IDs in republished space, and is also required to specify whether the return images should be rectified or not.  The service returns the stereo image pairs for the ''from'' image and for all ''to'' images.  
  1.name = info_service
  1.type = image_cache/GetInfo
  1.desc = Request stored camera information via this service.    
  2.name = neighbour_service
  2.type = image_cache/GetNeighbours
  2.desc = Request the neighbours in the SLAM graph corresponding to a particular republished image ID.  This information is then used to insert loop closure edges at interpolated points in the graph.
}
param {
  0.name = ~stereo_topic
  0.type = string
  0.desc = The topic prefix under which stereo images are published.
  0.default = stereo
  1.name = ~republished_topic
  1.type = string
  1.desc = The topic prefix under which the republished image should be published.
  1.default = throttled
  2.name = ~cache_path
  2.type = string
  2.desc = The directory location at which the image cache should be stored.
  2.default = ./
  3.name = ~div
  3.type = int
  3.desc = The rate at which to subsample images.  By default, republish and save every fourth image.
  3.default = 4
}
```


