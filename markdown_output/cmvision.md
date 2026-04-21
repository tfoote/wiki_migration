## Usage

### Selecting Blob Colors

![](attachment:lewis_cmvision.png)

```
rosrun cmvision colorgui image:=<image topic>
``` The above command will bring up an interface
that provides a means for graphically selecting desired colors for
blobs. \`colorgui\` displays values for \`RGB\` and \`YUV\` which can be
used in a colors file.

### Colors File Format

Blob parameters are specified to \`cmvision\` using two components:

-   Blob colors in \`RGB\` color space, specified as follows: (r, g, b)
    merge expected_num name
-   Blob threshold parameters in \`YUV\` color space, specified as
    follows: (min_y:max_y, min_u:max_u, min_v:max_v)

Example \`colors.txt\` for detecting a *Research Robot Red* RWI B21r
```
[colors]
(159,  62, 71) 0.000000 7 ResearchRobotRed

[thresholds]
(56:99, 108:117, 173:193)
```

Multiple blob colors can be specified in the same file by adding lines
under \`colors\` and \`thresholds\`.

### Detecting Blobs

```
rosparam set /cmvision/color_file /path/to/colors.txt
rosrun cmvision cmvision image:=<image topic>
```

![](https://raw.githubusercontent.com/teshanshanuka/cmvision/noetic-devel/static/demo.gif)

## Nodes

```clearsilver
node.0 {
  name = colorgui
  desc = Simple node for selecting blob colors.
  sub {
    0.name = image
    0.type = sensor_msgs/Image
    0.desc = The image topic. Should be remapped to the name of the real image topic.
  }
}
node.1 {
  name = cmvision
  desc = Node for detecting blobs.
  sub {
    0.name = image
    0.type = sensor_msgs/Image
    0.desc = The image topic. Should be remapped to the name of the real image appropriately.
  }
  pub {
    0.name = blobs
    0.type = cmvision/Blobs
    0.desc = A list of detected blobs.
  }
  param {
    0.name = /cmvision/color_file
    0.type = string
    0.desc = Specifies a path to the colors file.
    0.default = ""

    1.name = /cmvision/mean_shift_on
    1.type = bool
    1.desc = If `true`, smooth the image using the mean shift algorithm before doing blob detection.
    1.default = false
    
    2.name = /cmvision/debug_on
    2.type = bool
    2.desc = Enables or disables debug output.
    2.default = false
    
    3.name = /cmvision/spatial_radius_pix
    3.type = int
    3.desc = If using mean shift, sets mean shift's spacial radius parameter.
    3.default = 0

    4.name = /cmvision/color_radius_pix
    4.type = int
    4.desc = If using mean shift, sets mean shift's color radius parameter.
    5.default = 0
  }
}
```
