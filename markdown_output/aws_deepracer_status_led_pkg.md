## Overview

The
[DeepRacer Status LED ROS package](https://github.com/aws-deepracer/aws-deepracer-status-led-pkg)
creates the status_led_node which is part of the core AWS DeepRacer
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
name = status_led_node
srv {
  1{
   name = led_solid
   type = srv/SetStatusLedSolidSrv
   desc = A service that is called to stop the current effect on the LED light passed as parameter and set a solid light effect with the color passed as parameter.
  }
  2{
   name = led_blink
   type = srv/SetStatusLedBlinkSrv
   desc = A service that is called to stop the current effect on the LED light passed as parameter and start a blink light effect with the colors passed as parameter.
  }
}
```


