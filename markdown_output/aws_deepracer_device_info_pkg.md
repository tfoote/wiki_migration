## Overview

The
[DeepRacer Device Info ROS package](https://github.com/aws-deepracer/aws-deepracer-device-info-pkg)
creates the device_info_node which is part of the core AWS DeepRacer
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
name = device_info_node

srv {
  1{
   name = get_device_info
   type = srv/GetDeviceInfoSrv
   desc = A service that is called to get the DeepRacer hardware and software packages version information.
  }
  
}
```


