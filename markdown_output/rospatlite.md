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



```clearsilver
name = patlite_node
desc = This is a node that controls a patlite device.
sub {
  0.name = ~set/red
  0.type = std_msgs/Int8
  0.desc << EOM
Set the state of the red light.
|| Int8 || State of the light ||
|| 0 || Off ||
|| 1 || On ||
|| 2 || Blink pattern 1 ||
|| 3 || Blink pattern 2 ||
EOM
  1.name = ~set/yellow
  1.type = std_msgs/Int8
  1.desc = Set the state of the yellow light.
  2.name = ~set/green
  2.type = std_msgs/Int8
  2.desc = Set the state of the green light.
  3.name = ~set/blue
  3.type = std_msgs/Int8
  3.desc = Set the state of the blue light.
  4.name = ~set/white
  4.type = std_msgs/Int8
  4.desc = Set the state of the white light.
  5.name = ~set/buzzer
  5.type = std_msgs/Int8
  5.desc << EOM
Set the state of the buzzer.
|| Int8 || State of the buzzer ||
|| 0 || Off ||
|| 1 || Pattern 1 ||
|| 2 || Pattern 2 ||
|| 3 || Pattern 3 ||
|| 4 || Pattern 4 ||
EOM
}
param {
  0.name = ~host
  0.default = "10.68.0.10"
  0.type = string
  0.desc = hostname or IP address of the patlite device.
  1.name = ~port
  1.default = 10000
  1.type = int
  1.desc = TCP port number of the patlite device.
  2.name = ~timeout
  2.default = 0.5
  2.type = float
  2.desc = timeout[sec] for socket connection.
}
```


