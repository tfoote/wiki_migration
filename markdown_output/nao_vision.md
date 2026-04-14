## About

The \`nao_vision\` package allows easy control and access of the NAO\'s
vision via ROS. These packages have been tested with
[NAOqi version 1.10.52](http://users.aldebaran-robotics.com/docs/site_en/index_doc.html).

## Nodes

```clearsilver
node.0 {
  name = nao_vision
  desc = `nao_vision` can remotely stream images from an Aldebaran NAO's built in camera. By default, a 320x240 RGB image is streamed from the top camera and published on the `nao_camera` topic. Optional parameters can be set to change the resolution or change to the bottom camera.
  pub {
    0.name = nao_vision
    0.type = sensor_msgs/Image
    0.desc = Current image from the NAO's on-board camera.
  }
  param {
    0.name = /naoqi/host
    0.type = `string`
    0.desc = Hostname used to communicate with the NAO.
    1.name = /naoqi/port
    1.type = `integer`
    1.desc = Port used to communicate with the NAO.
    2.name = /naoqi/path
    2.type = `string`
    2.desc = Optional path to the NAOqi /lib folder that can be used if your local `PYTHONPATH` does not include it.
    2.default = `null`
    3.name = ~resolution
    3.type = `integer`
    3.desc = Integer representation of the resolution as defined by the [[http://users.aldebaran-robotics.com/docs/site_en/bluedoc/ALVideoDevice.html|Nao video API]]. {0=`kQQVGA`, 1=`kQVGA`, 2=`kVGA`}
    3.default = 1=`kQVGA`
    4.name = ~camera
    4.type = `integer`
    4.desc = Integer representation of the camera to stream from as defined by the [[http://users.aldebaran-robotics.com/docs/site_en/bluedoc/ALVideoDevice.html|Nao video API]]. {0=top-camera, 1=bottom-camera}
    4.default = 0=top-camera
  }
}
```

## Installation

To install the \`nao_rail\` stack, simply run the following commands in
your shell:

```shell
cd /path/to/your/ros/stacks
git clone git://github.com/WPI-RAIL/nao_rail.git
roscd nao_rail
rosdep install nao_rail
rosmake nao_rail
```

### Startup

The \`nao_vision\` package contains a \`nao_vision.launch\` file which
should be edited with the hostname and port of your NAO. Additionally,
if your local \`PYTHONPATH\` does not include the path to your NAOqi
/lib folder, an optional parameter can be set in the launch file.
Parameters are also included to configure the resolution and the camera
(bottom or top) that will be streamed. These are set to the default
values in the given launch file. This file launches an instance of the
\`nao_vision\` node. To launch this node, the following commands can be
used:

```
roslaunch nao_vision nao_vision.launch
```

With the above node running, you can test video streaming with the
[image_view](image_view) package using the following command:

```
rosrun image_view image_view image:=/nao_camera
```

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/nao_rail/issues).
Feel free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)

------------------------------------------------------------------------

  -- ------------------------------------------------- -- ---------- -- -------------------------- --
     \<tablewidth=\"100%\"\> ![](attachment:wpi.png)      \<:99%\>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
