## Overview

\`sync_params\` provides a means to synchronize parameter servers
between multiple ROS masters. The parameter server is polled, and new
parameters are published as a topic. The topic is then synchronized
across masters using
[multimaster_fkie](http://wiki.ros.org/multimaster_fkie). The topic is
received and written to the parameter server on the other ROS master.

By default, all parameters will be synchronized. The \`blacklist\`
excludes parameters based on their name. The \`whitelist\` parameters
are exempt from the \`blacklist\`. These can both be regular
expressions. For example: ```
blacklist = ["/*"]
whitelist = [/my_parameter]
``` Would only
synchronize \`my_parameter\`.

The parameter \`use_wall_time\` is designed for spawning robots in
Gazebo. Gazebo pauses the ROS clock when loading a robot, and waits for
the \`robot_description\` parameter. But that parameter might not get
synchronized if \`sync_params\` uses the ROS clock.

## Usage

Examples can be found in the
[launch folder](https://github.com/NicksSimulationsROS/sync_params/blob/ros-kinetic/launch/example1.launch).

## Nodes

```clearsilver
node.0{
  name = sync_params
  desc = Synchronise parameter servers across multiple ROS masters.
  sub {
    0.name = /params
    0.type = sync_params/ParameterMsg
    0.desc = The topic containing parameters to be synced
  }
  pub {
    0.name = /params
    0.type = sync_params/ParameterMsg
    0.desc = The topic containing parameters to be synced
  }
  param {
    0.name = ~debug
    0.type = boolean
    0.desc = Whether to print out lots of information
    0.default = false
    1.name = ~rate
    1.type = double
    1.desc = The rate to poll the parameter server
    1.default = 1.0
    2.name = ~death_timer
    2.type = double
    2.desc = How many ROS seconds until publishing stops.
    2.default = -1.0
    3.name = ~use_wall_time
    3.type = boolean
    3.desc = Whether to use computer clock instead of ROS clock. Does not affect `death_timer`
    3.default = false
    4.name = ~blacklist
    4.type = array
    4.desc = List of parameter names to exclude from synchronising
    4.default = []
    5.name = ~whitelist
    5.type = array
    5.desc = List of parameter names to exclude from the `blacklist`
    5.default = []
  }
}
```
