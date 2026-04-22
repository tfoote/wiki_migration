## Nodes



```clearsilver
node.0 {
  name = grid
  desc = This node takes in a camera image and computes the homography between a detect grid and the idealized grid that it is projecting.
  sub {
    0.name = image
    0.type = sensor_msgs/Image
    0.desc = A camera image containing the projected grid to be detected.
  }
  pub {
    0.name = grid
    0.type = sensor_msgs/Image
    0.desc = The grid which is being projected
  
    1.name = homography
    1.type = projector_calibration/Homography
    1.desc = The homography, mapping points in the camera image to projector pixels.
  }
  param {
  
    0.name = ~grid_size
    0.type = string
    0.desc = Defaults to 5x7
  }
}
```



## Using the Calibration

Given a homography, `H` (provided by
[projector_calibration/grid](projector_calibration#grid)), and camera
calibration `K` (from a
[sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)),
a 3D point, `p` in the world can be projected onto as follows: 1.
Transform `p` into the same frame as the camera used to find `H`
(call the new point `p`,,img,,). 1. Project `p`,,img,, onto the
image plane (call the new point `p`,,proj,,). 1. Transform `p`,,2d,,
to projector pixels using `H`

In python this looks something like 

```python
import image_geometry, tf, cv2

# get camera_info_msg and H from somewhere
# create a tf listener

model = image_geometry.PinholeCameraModel(camera_info_msg)
p_img = tf_listener.transformPoint(model.tf_frame, p)
p_2d = model.project3dToPixel((p_img.x, p_img.y, p_img.z))
p_proj = cv2.perspectiveTransform(H, [p_2d])
```


