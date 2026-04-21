## About

The `nao_speech` package allows easy control of the NAO's speech
module via ROS. These packages have been tested with
[NAOqi version 1.10.52](http://users.aldebaran-robotics.com/docs/site_en/index_doc.html).

## Nodes

```clearsilver
node.0 {
  name = nao_speech
  desc = `nao_speech` can remotely control the NAO's speech module. Text-to-speech messages can be sent, volume can be controlled, and the language can be set using this node. 
  sub {
    0.name = nao_say
    0.type = std_msgs/String
    0.desc = The message to be sent to the NAO's speech module that is to be spoken.
  }
  sub {
    1.name = nao_set_volume
    1.type = std_msgs/Float32
    1.desc = The volume level of the NAO's speech module in the range [0,1].
  }
  sub {
    2.name = nao_set_lang
    2.type = std_msgs/String
    2.desc = The language that the NAO's speech module should use. This language must be installed on the NAO.
  }
  param {
    0.name = /naoqi/host
    0.type = `string`
    0.desc = Hostname used to communicate with the Nao.
    1.name = /naoqi/port
    1.type = `integer`
    1.desc = Port used to communicate with the Nao.
    2.name = /naoqi/path
    2.type = `string`
    2.desc = Optional path to the NAOqi /lib folder that can be used if your local `PYTHONPATH` does not include it.
    2.default = `null`
    3.name = ~volume
    3.type = `float`
    3.desc = The volume level of the NAO's speech module in the range [0,1].
    3.default = 0.5
    4.name = ~language
    4.type = `string`
    4.desc = The language that the NAO's speech module should use. This language must be installed on the NAO.
    4.default = "English"
  }
}
```

## Installation

To install the `nao_rail` stack, simply run the following commands in
your shell:

```shell
cd /path/to/your/ros/stacks
git clone git://github.com/WPI-RAIL/nao_rail.git
roscd nao_rail
rosdep install nao_rail
rosmake nao_rail
```

### Startup

The `nao_speech` package contains a `nao_speech.launch` file which
should be edited with the hostname and port of your NAO. Additionally,
if your local `PYTHONPATH` does not include the path to your NAOqi
/lib folder, an optional parameter can be set in the launch file.
Parameters are also included to configure the volume and language of the
NAO's speech module. These are set to the default values in the given
launch file. This file launches an instance of the `nao_speech` node.
To launch this node, the following commands can be used:

```
roslaunch nao_speech nao_speech.launch
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
     <tablewidth="100%"> ![](attachment:wpi.png)      <:99%>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
