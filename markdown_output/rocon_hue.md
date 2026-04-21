

```wiki

||<style="text-align: center;" tablewidth="100%">This is part of the [[http://www.robotconcert.org|Robotics in Concert]] project.||
```



## Overview

[Philips Hue](http://meethue.com/) is a personal wireless light bulb
that allows to manage lighting condition via smartphone or with REST
API. This package exposes ROS api to communicate with Hue bridge server
to get/set hue status.

## Installation



```
> sudo apt-get install ros-<distro>-rocon-hue
```



## Execution

1\. Check Hue IP address

-   via [meethue page](https://www.meethue.com/api/nupnp)
-   by asking your network manager.

2\. Start bridge server



```
> roslaunch rocon_hue hue_bridge_server.launch --screen hue_ip:=<bridge ip>
```



3\. You should be able to see..



```
[INFO] [WallTime: 1397022783.781245] bridge connect
```



## Predefined Colors

Check
[rocon_device_msgs/HueState](http://docs.ros.org/indigo/api/rocon_device_msgs/html/msg/HueState.html)

## APIs



```clearsilver
pub{
 no_header=True
 1{
 name = list_hue
 type = rocon_device_msgs/HueArray
 desc = Provide a list of available hue and status
 }
}
sub{
 no_header=True
 1{
 name = set_hue
 type = rocon_device_msgs/Hue
 desc = Sets status of a single hue bulb
 }
```


