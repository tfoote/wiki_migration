## Overview

The
[DeepRacer I2C ROS package](https://github.com/aws-deepracer/aws-deepracer-i2c-pkg)
creates the battery_node which is part of the core AWS DeepRacer
application and will be launched from the
[deepracer_launcher](https://github.com/aws-deepracer/aws-deepracer-launcher).
More details about the application and the components can be found
[here](https://github.com/aws-deepracer/aws-deepracer-launcher).

### License

The source code is released under
[Apache 2.0](https://aws.amazon.com/apache-2-0/).

### Supported ROS Distributions

-   Foxy

## Node Details

```clearsilver
name = battery_node

srv {
  1{
   name = battery_level
   type = srv/BatteryLevelSrv
   desc = A service that is called to get the current vehicle battery level information in the range of [0 to 11].
  }
  
}
```
