## Overview

A ROS wrapper for the Maxon Motor
[EPOS Command Library](http://www.maxonmotorusa.com/medias/sys_master/root/8815100788766/EPOS-Command-Library-En.pdf)
to allow use of EPOS motor controllers with ros_control.

## Nodes

```clearsilver
node.0 {
  name = epos_hardware_node
  desc = Node that launches a controller manager with Maxon Motors as the robot hardware. Transmissions are also loaded from the URDF. The motors to load are specified as arguments.
  param {
    0.name = robot_description
    0.type = string
    0.desc = The robot description that is searched for transmissions to load
  }
}
```

#### Usage

```
$ rosrun epos_hardware epos_hardware_node motor_name1 motor_name2 motor_name3
``` Each name that is specified as an argument will
be loaded as a motor. See below for configuration

## Configuration

Both the epos_hardware_node node and the epos_manager library are
configured using ROS parameters. If a parameter is related to a register
value then the register is listed in the parameter description. (NOTE:
the values may not be the same if the units are different) See the
[EPOS Command Library](http://www.maxonmotorusa.com/medias/sys_master/root/8815100788766/EPOS-Command-Library-En.pdf)
documentation for more information.

\'\'\'NOTE:\'\'\' while amps and seconds are used for most parameters,
all position and velocity parameters and control inputs are in the
device units (this is normally rotations and rpm by default).

### Device Parameters

```clearsilver
param {
  no_header=True
  0.name = ~/motor_name/serial_number
  0.type = string
  0.desc = The serial number of the motor (in hex). This is used to locate the motor.
  1.name = ~/motor_name/actuator_name
  1.type = string
  1.desc = The name of the actuator this motor corresponds to in the URDF
  2.name = ~/motor_name/operation_mode
  2.type = string
  2.desc = The mode the motor runs in. One of 'profile_position', 'profile_velocity'
  3.name = ~/motor_name/clear_faults
  3.type = bool
  3.default = false
  3.desc = If the driver should attempt to clear errors on the device before enabling it
}
```

### Motor Parameters

```clearsilver
param {
  no_header=True
  0.name = ~/motor_name/motor/type
  0.type = int
  0.desc = The type of the motor (0x6402-00)
}
```

#### DC Motor Parameters

```clearsilver
param {
  no_header=True
  0.name = ~/motor_name/motor/dc_motor/nominal_current
  0.type = double
  0.desc = The max continuous motor current in amps (0x6410-01)
  1.name = ~/motor_name/motor/dc_motor/max_output_current
  1.type = double
  1.desc = The max peak current in amps (0x6410-02)
  2.name = ~/motor_name/motor/dc_motor/thermal_time_constant
  2.type = double
  2.desc = The thermal time constant in seconds (0x6410-05)
}
```

#### EC Motor Parameters

```clearsilver
param {
  no_header=True
  0.name = ~/motor_name/motor/ec_motor/nominal_current
  0.type = double
  0.desc = The max continuous motor current in amps (0x6410-01)
  1.name = ~/motor_name/motor/ec_motor/max_output_current
  1.type = double
  1.desc = The max peak current in amps (0x6410-02)
  2.name = ~/motor_name/motor/ec_motor/thermal_time_constant
  2.type = double
  2.desc = The thermal time constant in seconds (0x6410-05)
  3.name = ~/motor_name/motor/ec_motor/number_of_pole_pairs
  3.type = int
  3.desc = The number of pole pairs (0x6410-03)
}
```

### Sensor Parameters

```clearsilver
param {
  no_header=True
  0.name = ~/motor_name/sensor/type
  0.type = int
  0.desc = The type of the sensor (0x2210-02)
}
```

#### Incremental Encoder Parameters

```clearsilver
param {
  no_header=True
  0.name = ~/motor_name/motor/incremental_encoder/resolution
  0.type = int
  0.desc = The resolution of the encoder (0x2210-01)
  1.name = ~/motor_name/motor/incremental_encoder/inverted_polarity
  1.type = bool
  1.desc = If the encoder is inverted from the motor (0x2210-04)
}
```

#### Hall Sensor Parameters

```clearsilver
param {
  no_header=True
  0.name = ~/motor_name/motor/hall_sensor/inverted_polarity
  0.type = bool
  0.desc = If the hall sensor is inverted from the motor
}
```

#### SSI Absolute Encoder Parameters

```clearsilver
param {
  no_header=True
  0.name = ~/motor_name/motor/ssi_absolute_encoder/inverted_polarity
  0.type = bool
  0.desc = If the encoder is inverted from the motor (0x2210-04)
  1.name = ~/motor_name/motor/ssi_absolute_encoder/data_rate
  1.type = int
  1.desc = (0x2211-01)
  2.name = ~/motor_name/motor/ssi_absolute_encoder/number_of_multiturn_bits
  2.type = int
  2.desc = (0x2211-02)
  3.name = ~/motor_name/motor/ssi_absolute_encoder/number_of_singleturn_bits
  3.type = int
  3.desc = (0x2211-02)
}
```

### Safety Parameters

```
$ rosrun epos_hardware epos_hardware_node motor_name1 motor_name2 motor_name3
```0

### Position Regulator Parameters

```
$ rosrun epos_hardware epos_hardware_node motor_name1 motor_name2 motor_name3
```1

### Velocity Regulator Parameters

```
$ rosrun epos_hardware epos_hardware_node motor_name1 motor_name2 motor_name3
```2

### Current Regulator Parameters

```
$ rosrun epos_hardware epos_hardware_node motor_name1 motor_name2 motor_name3
```3

### Position Profile Parameters

```
$ rosrun epos_hardware epos_hardware_node motor_name1 motor_name2 motor_name3
```4

### Velocity Profile Parameters

```
$ rosrun epos_hardware epos_hardware_node motor_name1 motor_name2 motor_name3
```5

## Tools

### list_devices

```
$ rosrun epos_hardware epos_hardware_node motor_name1 motor_name2 motor_name3
```6 Enumerate all EPOS devices on USB and
optionally RS232 ports

### get_state

```
$ rosrun epos_hardware epos_hardware_node motor_name1 motor_name2 motor_name3
```7 Get the position, velocity, and current from
the motor with the given serial number
