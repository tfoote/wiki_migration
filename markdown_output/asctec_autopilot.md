![](attachment:cityflyer.jpg)

## Usage

This package provides the driver interface for communicating with an
[Ascending Technologies AutoPilot](http://www.asctec.de/asctec-hummingbird-autopilot/).
The code is being developed to support both the Hummingbird and the
Pelican Quadrotor aircraft.

## Details

This package accepts and provides data in the same structure as
specified in the [AscTec](http://www.asctec.de/) documentation. The
[asctec_proc](asctec_proc) package provides conversion of the data, such
as IMU information, into standard ROS messages.

### Limitations

Due to hardware limitations of the autopilot the only supported baud
rate on the telemetry link is 57600, because of this the topic polling
intervals and offsets are designed to optimize the available bandwidth.

Due to processing limitations of the autopilot, the maximum update
frequency is 10 HZ using the Zigbee radio or 20 Hz if connected directly
via the serial port. This is due to the latencies involved when
requesting data and sending control messages. If data is only requested
or controls are only sent, the update frequency can be higher.

### Additional Information

Additional technical information about the Ascending Technologies
Pelican and Hummingbird Quadrotor aircraft can be found
[here](http://robotics.ccny.cuny.edu/wiki/AscTec)

## Example

The driver can be started by running:



```shell
roslaunch asctec_autopilot autopilot.launch
```



## Nodes



```clearsilver
 name = asctec_autopilot
 desc = The `asctec_autopilot` node takes in <<MsgLink(asctec_msgs/CtrlInput)>> messages and sends these commands over the serial port to the aircraft.
 sub {
   0{
    name = ~CTRL_INPUT
    type = asctec_msgs/CtrlInput
    desc = Provides an interface to control the yaw, pitch, roll and thrust
    }
   1{
    name = ~ESTOP
    type = std_msgs/Bool
    desc = When a true value is received on this topic, the "motor emergency" command is sent to the !AutoPilot. The !AutoPilot must be restarted to re-enable motors.
    }
  }
 pub {
   0{
    name = ~CONTROLLER_OUTPUT
    type = asctec_msgs/ControllerOutput
    desc = This is the output of the yaw, pitch, roll, thrust controller
   }
   1{
    name = ~GPS_DATA
    type = asctec_msgs/GPSData
    desc = Basic GPS Data
   }
   2{
    name = ~GPS_DATA_ADVANCED
    type = asctec_msgs/GPSDataAdvanced
    desc = Advanced GPS Data
   }
   3{
    name = ~IMU_CALCDATA
    type = asctec_msgs/IMUCalcData
    desc = Fused IMU Data
   }
   4{
    name = ~IMU_RAWDATA
    type = asctec_msgs/IMURawData
    desc = Unfused IMU Data
   }
   5{
    name = ~LL_STATUS
    type = asctec_msgs/LLStatus
    desc = Low Level Status including battery voltage
   }
   6{
    name = ~RC_DATA
    type = asctec_msgs/RCData
    desc = Inputs from the radio control
   }
  }
 param{
    0.name = ~port
    0.type = string
    0.default = `"/dev/ttyUSB0"`
    0.desc = The default name of the serial port

    1.name = ~speed
    1.type = int
    1.default = `57600`
    1.desc = The documentation indicates that 57600 is the only supported speed, however this param is provided in the event that the baud rate can be changed.
 
    2.name = ~freq
    2.type = int
    2.default = `50`
    2.desc = This is the base command/polling frequency

    3.name = ~enable_CONTROLLER_OUTPUT
    3.type = bool
    3.default = `true`
    3.desc = Enables polling

    4.name = ~interval_CONTROLLER_OUTPUT
    4.type = int
    4.default = `1`
    4.desc = Topic frequency = Base frequency / interval

    5.name = ~offset_CONTROLLER_OUTPUT
    5.type = int
    5.default = `0`
    5.desc = If the interval is 2 and the offset is 0 poll on even counts, if offset is 1 poll on odd counts, etc.

    6.name = ~enable_GPS_DATA
    6.type = bool
    6.default = `true`
    6.desc = Enables polling

    7.name = ~interval_GPS_DATA
    7.type = int
    7.default = `1`
    7.desc = Topic frequency = Base frequency / interval

    8.name = ~offset_GPS_DATA
    8.type = int
    8.default = `0`
    8.desc = If the interval is 2 and the offset is 0 poll on even counts, if offset is 1 poll on odd counts, etc.

    9.name = ~enable_GPS_DATA_ADVANCED
    9.type = bool
    9.default = `true`
    9.desc = Enables polling

    10.name = ~interval_GPS_DATA_ADVANCED
    10.type = int
    10.default = `1`
    10.desc = Topic frequency = Base frequency / interval

    11.name = ~offset_GPS_DATA_ADVANCED
    11.type = int
    11.default = `0`
    11.desc = If the interval is 2 and the offset is 0 poll on even counts, if offset is 1 poll on odd counts, etc.

    12.name = ~enable_IMU_CALCDATA
    12.type = bool
    12.default = `true`
    12.desc = Enables polling

    13.name = ~interval_IMU_CALCDATA
    13.type = int
    13.default = `1`
    13.desc = Topic frequency = Base frequency / interval

    14.name = ~offset_IMU_CALCDATA
    14.type = int
    14.default = `0`
    14.desc = If the interval is 2 and the offset is 0 poll on even counts, if offset is 1 poll on odd counts, etc.

    15.name = ~enable_IMU_RAWDATA
    15.type = bool
    15.default = `true`
    15.desc = Enables polling

    16.name = ~interval_IMU_RAWDATA
    16.type = int
    16.default = `1`
    16.desc = Topic frequency = Base frequency / interval

    17.name = ~offset_IMU_RAWDATA
    17.type = int
    17.default = `0`
    17.desc = If the interval is 2 and the offset is 0 poll on even counts, if offset is 1 poll on odd counts, etc.

    18.name = ~enable_LL_STATUS
    18.type = bool
    18.default = `true`
    18.desc = Enables polling

    19.name = ~interval_LL_STATUS
    19.type = int
    19.default = `1`
    19.desc = Topic frequency = Base frequency / interval

    20.name = ~offset_LL_STATUS
    20.type = int
    20.default = `0`
    20.desc = If the interval is 2 and the offset is 0 poll on even counts, if offset is 1 poll on odd counts, etc.

    21.name = ~enable_RC_DATA
    21.type = bool
    21.default = `true`
    21.desc = Enables polling

    22.name = ~interval_RC_DATA
    22.type = int
    22.default = `1`
    22.desc = Topic frequency = Base frequency / interval

    23.name = ~offset_RC_DATA
    23.type = int
    23.default = `0`
    23.desc = If the interval is 2 and the offset is 0 poll on even counts, if offset is 1 poll on odd counts, etc.

    24.name = ~enable_CONTROL
    24.type = bool
    24.default = `true`
    24.desc = Enables polling

    25.name = ~interval_CONTROL
    25.type = int
    25.default = `1`
    25.desc = Topic frequency = Base frequency / interval

    26.name = ~offset_CONTROL
    26.type = int
    26.default = `0`
    26.desc = If the interval is 2 and the offset is 0 poll on even counts, if offset is 1 poll on odd counts, etc.
 }
```



## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.

Please use our [Trac](http://robotics.ccny.cuny.edu/trac/) to
[report bugs](http://robotics.ccny.cuny.edu/trac/newticket?component=asctec_drivers/asctec_autopilot&type=defect)
or
[request features](http://robotics.ccny.cuny.edu/trac/newticket?component=asctec_drivers/asctec_autopilot&type=enhancement).
