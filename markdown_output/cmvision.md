## Usage

### Selecting Blob Colors

![attachment:lewis_cmvision.png](doc/lewis_cmvision.png)



```
rosrun cmvision colorgui image:=<image topic>
```

 The above command will bring up an interface
that provides a means for graphically selecting desired colors for
blobs. `colorgui` displays values for `RGB` and `YUV` which can be
used in a colors file.

### Colors File Format

Blob parameters are specified to `cmvision` using two components:

- Blob colors in `RGB` color space, specified as follows: (r, g, b)
  merge expected_num name
- Blob threshold parameters in `YUV` color space, specified as
  follows: (min_y:max_y, min_u:max_u, min_v:max_v)

Example `colors.txt` for detecting a *Research Robot Red* RWI B21r


```
[colors]
(159,  62, 71) 0.000000 7 ResearchRobotRed

[thresholds]
(56:99, 108:117, 173:193)
```



Multiple blob colors can be specified in the same file by adding lines
under `colors` and `thresholds`.

### Detecting Blobs



```
rosparam set /cmvision/color_file /path/to/colors.txt
rosrun cmvision cmvision image:=<image topic>
```



![](https://raw.githubusercontent.com/teshanshanuka/cmvision/noetic-devel/static/demo.gif)

## Nodes

### colorgui

Simple node for selecting blob colors.

#### Subscribed Topics

- `image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  The image topic. Should be remapped to the name of the real image
  topic.

### cmvision

Node for detecting blobs.

#### Subscribed Topics

- `image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  The image topic. Should be remapped to the name of the real image
  appropriately.

#### Published Topics

- `blobs`
  ([cmvision/msg/Blobs](https://docs.ros.org/en/rolling/p/cmvision/msg/Blobs.html)):
  A list of detected blobs.

#### Parameters

- `/cmvision/color_file` (`string`, default: `""`): Specifies a path to
  the colors file.
- `/cmvision/mean_shift_on` (`bool`, default: `false`): If `true`,
  smooth the image using the mean shift algorithm before doing blob
  detection.
- `/cmvision/debug_on` (`bool`, default: `false`): Enables or disables
  debug output.
- `/cmvision/spatial_radius_pix` (`int`, default: `0`): If using mean
  shift, sets mean shift's spacial radius parameter.
- `/cmvision/color_radius_pix` (`int`): If using mean shift, sets mean
  shift's color radius parameter.
- (default: `0`)
