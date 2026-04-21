## About

The `rovio_ctrl` package contains nodes to control the movement of the
Rovio. This includes control the movement of the base itself, as well as
controlling the head (camera) position. Furthermore, joystick
teleoperation is provided via the `rovio_teleop` node.

## Nodes

```clearsilver
node.0 {
  name = rovio_move
  desc = `rovio_move` controls the motors of the Rovio.
  sub {
    0.name = man_drv
    0.type = rovio_shared/man_drv
    0.desc = Control the movement of the Rovio using movement and speed commands as defined by the [[http://www.wowwee.com/static/support/rovio/manuals/Rovio_API_Specifications_v1.2.pdf|Rovio API]].
  }
  sub {
    1.name = cmd_vel
    1.type = geometry_msgs/Twist
    1.desc = Control the movement of the Rovio using a `geometry_msgs/Twist` message. A positive angular-z value corresponds to a clockwise rotation. Movement along linear-y corresponds to moving left/right and movement along linear-x corresponds to moving forwards/backwards.
  }
  param {
    0.name = /rovio_shared/host
    0.type = `string`
    0.desc = Hostname used to communicate with the Rovio.
    1.name = /rovio_shared/user
    1.type = `string`
    1.desc = Username used to authenticate with the Rovio.
    2.name = /rovio_shared/pass
    2.type = `string`
    2.desc = Password used to authenticate with the Rovio.
  }
}
node.1 {
  name = rovio_head
  desc = `rovio_head` publishes the position of the head as well as allows for head position control.
  pub {
    0.name = head_sensor
    0.type = std_msgs/String
    0.desc = Current head position of the Rovio {''"HEAD_UP"'', ''"HEAD_MIDDLE"'', ''"HEAD_DOWN"''}.
  }
  srv {
    0.name = head_ctrl
    0.type = rovio_shared/head_ctrl
    0.desc = Change the position of the Rovio's head.
  }
  param {
    0.name = /rovio_shared/host
    0.type = `string`
    0.desc = Hostname used to communicate with the Rovio.
    1.name = /rovio_shared/user
    1.type = `string`
    1.desc = Username used to authenticate with the Rovio.
    2.name = /rovio_shared/pass
    2.type = `string`
    2.desc = Password used to authenticate with the Rovio.
  }
}
node.2 {
  name = rovio_teleop
  desc = ||<tablewidth="100%" tablestyle="text-align:left">`rovio_teleop` can control the motors, head, and audio device of a Rovio using a joystick. This node listens to a `joy` topic and sends messages to the `cmd_vel` topic in the `rovio_move` node, `head_ctrl` service in the `rovio_head` node, and `wav_play` service in the `rovio_audio` node. Buttons `0`, `1`, and `2` of a joystick control the head, buttons `4`, `5`, `6`, and `7` of a joystick play audio files on the Rovio, and the left and right joysticks control the movement of the Rovio. An example gamepad is shown to the right with its buttons labeled. || {{attachment:rovio_teleop_joy.gif}} ||
  sub {
    0.name = joy
    0.type = sensor_msgs/Joy
    0.desc = Listens for joystick commands.
  }
  pub {
    0.name = cmd_vel
    0.type = geometry_msgs/Twist
    0.desc = Control the movement of the Rovio using the left and right joysticks.
  }
  srv_called {
    0.name = head_ctrl
    0.type = rovio_ctrl/head_ctrl
    0.desc = Change the position of the Rovio's head using buttons `0`, `1`, or `2` of a joystick.
  }
  srv_called {
    1.name = wav_play
    1.type = rovio_shared/wav_play
    1.desc = Play one of four predefined `.wav` files using buttons `4`, `5`, `6`, or `7` of a joystick.
  }
  param {
    0.name = /rovio_shared/rovio_wav
    0.type = `string`
    0.desc = Absolute path to the `wav` folder within the [[rovio_av]] package. This is used when playing audio files using buttons `4`, `5`, `6`, or `7` of a joystick.
  }
}
```

## Installation

To install the `rovio` stack, you can choose to either install from
source, or from the Ubuntu package:

### Source

To install from source, execute the following: ```shell
cd /path/to/your/ros/stacks
git clone https://github.com/WPI-RAIL/rovio.git
roscd rovio
rosdep install rovio
rosmake rovio
```

### Ubuntu Package

To install the Ubuntu package, execute the following:
```
sudo apt-get install ros-fuerte-rovio
```

### Startup

The `rovio_ctrl` package contains a `rovio_ctrl.launch` file which
should be edited with the hostname, username and password to login to
your Rovio. This file launches an instance of the `rovio_move` and
`rovio_head` nodes. To launch these nodes, the following command can
be used:

```
roslaunch rovio_ctrl rovio_ctrl.launch
```

The `rovio_ctrl` package also contains a `rovio_teleop.launch` file
which should be edited with the hostname, username and password to login
to your Rovio as well as absolute path to the `wav` folder within the
[rovio_av](rovio_av) package. This file launches an instance of the
`rovio_move`, `rovio_head`, `rovio_audio` and `rovio_teleop`
nodes. To launch these nodes, the following command can be used:

```
roslaunch rovio_ctrl rovio_teleop.launch
```

You should now be able to teleoperate your Rovio with a joystick.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/rovio/issues). Feel
free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)

------------------------------------------------------------------------

  -- ------------------------------------------------- -- ---------- -- -------------------------- --
     <tablewidth="100%"> ![](attachment:wpi.png)      <:99%>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
