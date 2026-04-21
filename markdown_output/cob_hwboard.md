## Hardware Requirements

To use this package the care-o-bot has to be equiped with a hardware
monitor board.

## ROS API

The [cob_hwboard](cob_hwboard) package can be used to monitor certain
voltages, currents and temperatures inside the robot.


```clearsilver
 name = cob_hwboard
 desc = The `cob_hwboard` node directly recieves measured values from the hardware and publishes them on the [[diagnostics]] topic.

sub{
}

pub{
 0.name = /diagnostics
 0.type = diagnostics_msgs/DiagnosticArray
 0.desc = Diagnostic information about hwboard including voltage, current and temperature values.
}

srv{
}

param{
 0.name = devicestring
 0.type = string
 0.default = Required
 0.desc = Device address of hwbaord, e.g. /dev/ttyHwBoard
 1.name = head_sensor
 1.type = integer
 1.default = Required
 1.desc = ID of temperature sensor located in the head (hexadecimal value).
 2.name = eye_sensor
 2.type = integer
 2.default = Required
 2.desc = ID of temperature sensor located on the eye (hexadecimal value).
 3.name = torso_module_sensor
 3.type = integer
 3.default = Required
 3.desc = ID of temperature sensor located on the torso module (hexadecimal value).
 4.name = torso_sensor
 4.type = integer
 4.default = Required
 4.desc = ID of temperature sensor located in the torso (hexadecimal value).
 5.name = pc_sensor
 5.type = integer
 5.default = Required
 5.desc = ID of temperature sensor located on the pc (hexadecimal value).
 6.name = engine_sensor
 6.type = integer
 6.default = Required
 6.desc = ID of temperature sensor located on the engine (hexadecimal value).
}

req_tf{
}

prov{
}
```



## Usage/Examples

For starting only the hwboard use 

```
roslaunch cob_bringup hwboard.launch
```

 For including
the hwboard in your overall launch file use 

```
<include file="$(find cob_bringup)/components/hwboard.launch" />
```

 All
hardware configuration is done by using a yaml-file stored in the
[cob_hardware_config](cob_hardware_config) package. The file which
contains all necessary parameters is located in
"cob_hardware_config/cob3-3/config/hwboard.yaml" and should be similar
to this 

```
devicestring: /dev/ttyHwBoard
head_sensor: 0x103AEE7A
eye_sensor: 0x1089D07A
torso_module_sensor: 0x102BA47D
torso_sensor: 0x10E4967D
pc_sensor: 0x1082E17B
engine_sensor: 0x10FADC7A
```


