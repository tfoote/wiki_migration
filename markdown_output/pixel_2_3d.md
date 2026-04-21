![\|height="250px"](attachment:pixel_2_3d_clickable.jpg)
![\|height="250px"](attachment:pixel_2_3d.jpg)

## Usage

The current algorithm takes advantage of the RGB-D ordering of the point
cloud to find the relevant point quickly and reliably. This ordering is
found natively on the point clouds produced by the
[openni_kinect](openni_kinect) stack. The
[hrl_clickable_display](hrl_clickable_display) package provides an easy
interface for using this code.

These launch files, properly modified, will publish a pose to the
/pixel3d topic with every mouse click on the image.


```
roslaunch pixel_2_3d pixel_2_3d_run.launch # modify the remaps in this file
roslaunch hrl_clickable_display kinect_clickable_UI.launch
```



## Nodes



```clearsilver
node.0 {
 name = pixel_2_3d
 desc = Converts pixel on image to a pose in 3D by projecting the point cloud onto the image and finding the closest projected point in the image space to the given pixel.  The orientation is found by computing the surface normal and making the z-axis point along the normal in the direction of the camera.
 srv {
  0.name= /pixel_2_3d
  0.type= pixel_2_3d/Pixel23d
  0.desc= Input: pixel in `/image` frame.  Output: pose in `/base_footprint` frame.  Also contains an error flag indicating the result of the call.  A non-zero value suggests failure.
}
 sub {
  0.name= /l_mouse_click
  0.type= geomertry_msgs/PointStamped
  0.desc= Along with `/pixel3d` performs the same functionality as `/pixel_2_3d`.  References the x and y values of the point for the u and v pixel values.  Designed for use with [[hrl_clickable_display]].
  1.name= /image
  1.type= sensor_msgs/Image
  1.desc= Image to reference for pixel values.
  2.name= /point_cloud
  2.type= sensor_msgs/PointCloud2
  2.desc= Point cloud for 3D data.
}
 pub {
  0.name= /pixel3d
  0.type= geometry_msgs/PoseStamped
  0.desc= Output 3D pose published with both the service call and subscription call.
}
param {
  0.name= ~normal_radius
  0.type= double
  0.desc= The search radius used to find the normal.  Higher values are more time consuming and less sensitive.  Lower values are sensitive to noise but return quickly.
  0.default= 0.03
 }
}
```


