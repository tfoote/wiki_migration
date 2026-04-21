## About

The `carl_demos` package contains various nodes and launch
configurations for [CARL robot](carl_bot) demos, such as a web demo for
running CARL on the [RobotsFor.Me](https://www.robotsfor.me/) project.

## Nodes

```clearsilver
node.0 {
  name = carl_speed_speak
  desc = 'carl_speed_speak' provides auditory feedback for CARL's locomotion, so that he can sound more like what he thinks a vehicle sounds like.
  sub {
    0.name = cmd_vel
    0.type = geometry_msgs/Twist
    0.desc = Velocity commands for CARL's base.
  }
}
```

## Installation

To install the `carl_demos` package, you can install from source with
the following commands: . ```shell
cd /(your catkin workspace)/src
git clone https://github.com/WPI-RAIL/carl_demos.git
cd ..
catkin_make
catkin_make install
```

## Startup

The `carl_demos` package contains the launch file
`basic_web_demo.launch` which will launch a set of nodes on CARL to
allow control of navigation and manipulation through a web interface.
This includes tf publishing, video streaming, interactive markers,
navigation, and an extra level of safety to allow researchers to cut off
control of CARL from the web interface. . ```
roslaunch carl_demos basic_web_demo.launch
```
