## Usage

### Viewing a single image topic



```
rosrun image_view image_view image:=<image topic> [image transport type]
```



For example, to view raw images on the topic `/camera/image`, use:


```
rosrun image_view image_view image:=/camera/image
```



You may save the current image by right-clicking on the display window.
By default, images will be saved as `frame0000.jpg`,
`frame0001.jpg`, \....

If you want to view a compressed image stream (usually a good idea over
wireless!) using the capabilities of [image_transport](image_transport),
specify the transport type as a command-line argument. For example, if
[theora_image_transport](theora_image_transport) is built on the
publisher's side, you can use `theora` transport:


```
rosrun image_view image_view image:=/camera/image theora
```



Note that this is merely shorthand equivalent to setting the
`image_transport` parameter: 

```
rosrun image_view image_view image:=/camera/image _image_transport:=theora
```



### Viewing stereo images



```
rosrun image_view stereo_view stereo:=<stereo namespace> image:=<image topic identifier>
```



For example, to view stereo image pairs on topics
`/my_stereo_cam/left/image_rect_color` and
`/my_stereo_cam/right/image_rect_color`, use: 

```
rosrun image_view stereo_view stereo:=/my_stereo_cam image:=image_rect_color
```



`stereo_view` also shows the disparity image computed from the stereo
pair, color-mapped for clarity.

You may save the current image pair by right-clicking on any display
window. By default, images will be saved as `left0000.jpg`,
`right0000.jpg`, `disp0000.jpg`, `left0001.jpg`,
`right0001.jpg`, `disp0001.jpg`\.... As with `image_view`, you can
specify an image transport to use for the left and right image as an
optional argument.

## Nodes



```clearsilver
name = image_view
desc = Simple image viewer for ROS <<MsgLink(sensor_msgs/Image)>> topics.
sub {
  0.name = image
  0.type = sensor_msgs/Image
  0.desc = The image topic. Should be remapped to the name of the real image topic.
}
param {
  0.name = ~autosize
  0.type = bool
  0.desc = Whether the window should autosize itself to the image or be resizeable by the user.
  0.default = false
  1.name = ~filename_format
  1.type = string
  1.desc = printf-style format for saved image names. Use to control name, location and format of saved images.
  1.default = `"frame%04i.jpg"`
  2.name = ~image_transport
  2.type = string
  2.desc = Transport used for the image stream. `image_view` allows you to specify this as a simple command-line argument for convenience.
  2.default = `"raw"`
  3.name = ~window_name
  3.type = string
  3.desc = The name of the display window.
  3.default = name of the image topic
}
```

 

```clearsilver
name = disparity_view
desc = Simple viewer for <<MsgLink(stereo_msgs/DisparityImage)>> topics. Color-maps the disparity image for visualization.
sub {
  0.name = image
  0.type = stereo_msgs/DisparityImage
  0.desc = The disparity image topic. Should be remapped to the name of the real topic.
}
param {
  0.name = ~autosize
  0.type = bool
  0.desc = Whether the window should autosize itself to the image or be resizeable by the user.
  0.default = false
  1.name = ~window_name
  1.type = string
  1.desc = The name of the display window.
  1.default = name of the image topic
}
```




```clearsilver
name = stereo_view
desc = Viewer for stereo images. Shows the synchronized left/right image pair and the disparity image (color-mapped) computed from them.
sub {
  0.name = <stereo>/left/<image>
  0.type = sensor_msgs/Image
  0.desc = The left image topic. Formal parameters `stereo` and `image` should be remapped appropriately.
  1.name = <stereo>/right/<image>
  1.type = sensor_msgs/Image
  1.desc = The right image topic. Formal parameters `stereo` and `image` should be remapped appropriately.
  2.name = <stereo>/disparity
  2.type = stereo_msgs/DisparityImage
  2.desc = The disparity image computed from the left/right stereo pair.
}
param {
  0.name = ~autosize
  0.type = bool
  0.desc = Whether the windows should autosize to the image or be resizeable by the user.
  0.default = true
  1.name = ~filename_format
  1.type = string
  1.desc = printf-style format for saved image names. Use to control name, location and format of saved images. The string argument is `"left"` or `"right"`.
  1.default = `"%s%04i.jpg"`
  2.name = ~image_transport
  2.type = string
  2.desc = Transport used for the image streams.
  2.default = `"raw"`
  3.name = ~approximate_sync
  3.type = bool
  3.desc = Whether to use approximate synchronization. Set to true if the left and right cameras do not produce exactly synced timestamps.
  3.default = false
  4.name = ~queue_size
  4.type = int
  4.desc = Size of message queue for each synchronized topic. You may need to raise this if disparity processing takes too long, or if there are significant network delays.
  4.default = 5
}
```



## Nodelets



```clearsilver
name = image_view/image
desc = Nodelet version of image_view. Brings up a display window for a <<MsgLink(sensor_msgs/Image)>> topic.
sub {
  0.name = image
  0.type = sensor_msgs/Image
  0.desc = The image topic. Should be remapped to the name of the real image topic.
}
param {
  0.name = ~autosize
  0.type = bool
  0.desc = Whether the window should autosize itself to the image or be resizeable by the user.
  0.default = false
  1.name = ~filename_format
  1.type = string
  1.desc = printf-style format for saved image names. Use to control name, location and format of saved images.
  1.default = `"frame%04i.jpg"`
  2.name = ~image_transport
  2.type = string
  2.desc = Transport used for the image stream. `image_view` allows you to specify this as a simple command-line argument for convenience.
  2.default = `"raw"`
  3.name = ~window_name
  3.type = string
  3.desc = The name of the display window.
  3.default = name of the image topic
}
```

 

```
rosrun image_view image_view image:=/camera/image
```

0



```
rosrun image_view image_view image:=/camera/image
```

1 

```
rosrun image_view image_view image:=/camera/image
```

2


```
rosrun image_view image_view image:=/camera/image
```

3 }}}}}}
