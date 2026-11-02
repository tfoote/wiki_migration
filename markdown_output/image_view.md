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
wireless!) using the capabilities of
[image_transport](https://index.ros.org/p/image_transport), specify the
transport type as a command-line argument. For example, if
[theora_image_transport](https://index.ros.org/p/theora_image_transport)
is built on the publisher's side, you can use `theora` transport:


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

 

```clearsilver
name = image_view/disparity
desc = Nodelet version of disparity_view. Brings up a display window for a <<MsgLink(stereo_msgs/DisparityImage)>> topic, color-mapped for visualization.
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





```
{{{#!wiki version hydro_and_newer
== Tools ==

{{{
#!clearsilver CS/NodeAPI
name = image_saver
desc = This tool allows you to save images as jpg/png file from streaming (ROS <<MsgLink(sensor_msgs/Image)>> topic) to a file. From command line, you can run by `rosrun image_view image_saver image:=[your topic]`, or see [[http://answers.ros.org/question/9377/how-to-take-save-a-snapshot-from-my-kinect-to-disk/?answer=235294#post-id-235294|this answer]] to control the timing of capture.
sub {
  0.name = image
  0.type = sensor_msgs/Image
  0.desc = The image topic. Should be remapped to the name of the real image topic.
}
srv {
  0.name= save
  0.type= std_srvs/Empty
  0.desc= Save images, you need to set save_all_images to false
}
param {
  0.name = ~filename_format
  0.type = string
  0.desc = File name for saved images, you can use '%04i' for sequence number, and '%s' for default file format, you can use 'jpg' ,'png', 'pgm' as filename suffixes.
  0.default = `left%04d.%s`
  1.name = ~encoding
  1.type = string
  1.desc = Encoding type of input image topic.
  1.default = 'bgr8'
  2.name = ~save_all_image
  2.type = bool
  2.desc = If you set false, images are only saved when 'save' service is called
  2.default = true
}
```

 

```clearsilver
name = extract_images
desc = This tool also allows you to save images as jpg/png file from streaming (ROS <<MsgLink(sensor_msgs/Image)>> topic) to a file. `image_saver` node provide very similar functionalities, such as providing service call to trigger the node to save images, save images other than Jpeg format, etc.
sub {
  0.name = image
  0.type = sensor_msgs/Image
  0.desc = The image topic. Should be remapped to the name of the real image topic.
}
param {
  0.name = ~filename_format
  0.type = string
  0.desc = File name for saved images, you must add use '%04i' for sequence number.
  0.default = `frame%04d.jpg`
  1.name = ~sec_per_frame
  1.type = double
  1.desc = set sec per frame value.
  1.default = '0.1'
}
```




```clearsilver
name = video_recorder
desc = This tool allows you to record a video stream (ROS <<MsgLink(sensor_msgs/Image)>> topic) to a file. It relies on [[http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html#videowriter|OpenCV's VideoWriter class]]. With the default options, it encodes the video as MPG, encapsulated in a AVI container at 15 fps, and produces a file called `output.avi` in the current directory.
sub {
  0.name = image
  0.type = sensor_msgs/Image
  0.desc = The image topic. Should be remapped to the name of the real image topic.
}
param {
  0.name = ~filename
  0.type = string
  0.desc = Path and name of the output video.
  0.default = `output.avi`
  1.name = ~fps
  1.type = int
  1.desc = Framerate of the video.
  1.default = 15
  2.name = ~codec
  2.type = string
  2.desc = The [[http://www.fourcc.org/codecs.php|FOURCC]] identifier of the codec.
  2.default = `MJPG`
  3.name = ~encoding
  3.type = string
  3.desc = The image color space of the video.
  3.default = `bgr8`
}
```

 }}}}}}

## Troubleshooting

### Errors when using package

#### Error: Received error message in header\... Dropping connection

**Example:** 

```
[ERROR] 1260927377.348922000: Received error message in header for connection to [TCPROS connection to [10.0.0.136:39531 on socket 17]]: [Client [/image_view_1260927377013984000] wants topic /image/compressed to have datatype/md5sum [sensor_msgs/Image/060021388200f6f0f447d0fcd9c64743], but our version has [sensor_msgs/CompressedImage/8f7a12909da2c9d3332d540a0977563f]. Dropping connection.]
```



Above that error you might see a warning: 

```
[ WARN] 1260927377.319546000: [image_transport] It looks like you are trying to subscribe directly to a transport-specific image topic '/image/compressed', in which case you will likely get a connection error. Try subscribing to the base topic '/image' instead with parameter ~image_transport set to 'compressed' (on the command line, _image_transport:=compressed). See http://ros.org/wiki/image_transport for details.
```



**Solution:**

- Are you subscribing to an image topic? If the data type of the topic
  you remapping `image` to is not
  [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html),
  ROS will detect the mismatch and drop the connection. For example:
  

```
$ rostopic type image/compressed
sensor_msgs/CompressedImage
# Does not match sensor_msgs/Image
```


- Are you subscribing to a transport-specific subtopic? For example,
  `image_view image:=camera/image/theora`? This is a corollary of the
  previous case; the data type of a transport-specific topic like
  `camera/image/theora` is not
  [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
  but rather some packet message type. If you want to view the base
  topic `camera/image` using theora streaming video, give the
  transport name as a separate argument: 

```
$ rosrun image_view image_view image:=camera/image theora
```

 That
  tells `image_view` to load the theora plugin to
  [image_transport](https://index.ros.org/p/image_transport) and
  subscribe to the appropriate subtopic.
