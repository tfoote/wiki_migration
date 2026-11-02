`rospatlite` is a ROS driver for patlite Signal Tower NHx series.

## rospatlite Usage

`roslaunch rospatlite patlite.launch IP:=<patlite ip>`

- `patlite ip`: network address or hostname of your patlite device

## Examples



```
$ roslaunch rospatlite patlite.launch IP:=10.68.0.10
```



In another shell 

```
$ rostopic pub /patlite/set/buzzer std_msgs/Int8 1 # <- buzzer ON
$ rostopic pub /patlite/set/buzzer std_msgs/Int8 0 # <- buzzer OFF
$ rostopic pub /patlite/set/red std_msgs/Int8 1 # <- red light ON
$ rostopic pub /patlite/set/yellow std_msgs/Int8 2 # <- yellow light blink
```



## ROS API

### patlite_node

This is a node that controls a patlite device.

#### Subscribed Topics

- `~set/red`
  ([std_msgs/msg/Int8](https://docs.ros.org/en/rolling/p/std_msgs/msg/Int8.html)):
  Set the state of the red light. \|\| Int8 \|\| State of the light \|\|
  \|\| 0 \|\| Off \|\| \|\| 1 \|\| On \|\| \|\| 2 \|\| Blink pattern 1
  \|\| \|\| 3 \|\| Blink pattern 2 \|\|
- `~set/yellow`
  ([std_msgs/msg/Int8](https://docs.ros.org/en/rolling/p/std_msgs/msg/Int8.html)):
  Set the state of the yellow light.
- `~set/green`
  ([std_msgs/msg/Int8](https://docs.ros.org/en/rolling/p/std_msgs/msg/Int8.html)):
  Set the state of the green light.
- `~set/blue`
  ([std_msgs/msg/Int8](https://docs.ros.org/en/rolling/p/std_msgs/msg/Int8.html)):
  Set the state of the blue light.
- `~set/white`
  ([std_msgs/msg/Int8](https://docs.ros.org/en/rolling/p/std_msgs/msg/Int8.html)):
  Set the state of the white light.
- `~set/buzzer`
  ([std_msgs/msg/Int8](https://docs.ros.org/en/rolling/p/std_msgs/msg/Int8.html)):
  Set the state of the buzzer. \|\| Int8 \|\| State of the buzzer \|\|
  \|\| 0 \|\| Off \|\| \|\| 1 \|\| Pattern 1 \|\| \|\| 2 \|\| Pattern 2
  \|\| \|\| 3 \|\| Pattern 3 \|\| \|\| 4 \|\| Pattern 4 \|\|

#### Parameters

- `~host` (`string`, default: `"10.68.0.10"`): hostname or IP address of
  the patlite device.
- `~port` (`int`, default: `10000`): TCP port number of the patlite
  device.
- `~timeout` (`float`, default: `0.5`): timeout\[sec\] for socket
  connection.
