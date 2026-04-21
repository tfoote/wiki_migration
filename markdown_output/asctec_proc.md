## Details

This package is meant to be used together with
[asctec_autopilot](asctec_autopilot) on an
[ AscTec](http://www.asctec.de/?locale=en_US ) quadrotor vehicle such as
the !AscTec Pelican or !AscTec Hummingbird. The
[asctec_proc](asctec_proc) package provides a two-way translation
between the asctec messages published by
[asctec_autopilot](asctec_autopilot) and the hardware-independent MAV
messages used by the rest of the system.

The justification for this package is the following: the messages
published by and sent to \[asctec_autopilot\]\] are defined by the
[ AscTec Autopilot SDK](http://robotics.ccny.cuny.edu/wiki/AscTec/Docs ).
They are not in SI units, and are specific to the vehicle hardware.
Translating them into conventional ROS messages (such as
\<\<MsgLink(sensor_msgs/IMU)\>\>, \<\<MsgLink(geometry_msgs/Pose)\>\>
etc) enables the development of generic micro-air vehicle tools that can
be shared among various hardware platforms.

Apart from translating messages, the package can (optionally) monitor a
**state** topic and send engage/disengage the vehicle\'s motors whenever
appropriate by sending the \"motors on\"/\"motors off\" command to the
[asctec_autopilot](asctec_autopilot).

## Notes

This package does not support all the messages that !AscTec provides. If
you need to add further functionality, you can contact us about it, or
send us the appropriate patch.

## Usage

There are two versions of the driver: a standard ROS node, and a ROS
nodelet. For performance reasons, we recommend using the nodelet
together with the [asctec_autopilot](asctec_autopilot) nodelet when
running them on the onboard computer.

## Namespaces

Our convention is to use **/asctec/** as the namespace for the messages
provided by and sent to [asctec_autopilot](asctec_autopilot), and
**/mav** for the hardware-independent MAV messages.

![](attachment:asctec_proc.png)

## Coordinate frames

At the moment, the package publishes information in the **ENU**
(East-North-Up) frame. While this frame is typically not used for aerial
vehicles, it makes for easier integration with the rest of the ROS tools
.

## Nodes

```clearsilver
 name = asctec_proc_node
 desc = The `asctec_proc_node` is a bridge between the asctec_autopilot software and hardware-independent MAV tools.
sub {
   0{
    name = /asctec/LL_STATUS
    type = asctec_msgs/LL_STATUS
    desc = !AscTec LL_STATUS message (see [[http://robotics.ccny.cuny.edu/wiki/AscTec/Docs | documentation]])
    }
   1{
    name = /asctec/IMU_CALCDATA
    type = asctec_msgs/IMU_CALCDATA
    desc = !AscTec IMU_CALCDATA message (see [[http://robotics.ccny.cuny.edu/wiki/AscTec/Docs | documentation]])
    }
   2{
    name = /mav/cmd_thrust
    type = std_msgs/Float64
    desc = A thrust command, in the range of 0.0 (no thrust) to 1.0 (max thrust).
    }
   3{
    name = /mav/cmd_roll
    type = std_msgs/Float64
    desc = A roll command, in the range of -1.0 (maximum roll) to 1.0 (maximum roll). Note the ENU convention.
    }
   4{
    name = /mav/cmd_pitch
    type = std_msgs/Float64
    desc = A pitch command, in the range of -1.0 (maximum pitch) to 1.0 (maximum pitch). Note the ENU convention.
    }
   5{
    name = /mav/cmd_yaw
    type = std_msgs/Float64
    desc = A yaw command, in the range of -1.0 (maximum yaw) to 1.0 (maximum yaw). Note the ENU convention.
    }
   6{
    name = /mav/state
    type = mav_msgs/State
    desc = A state message ('''OFF''', '''IDLE''', '''FLYING'''). This topic is only subscribed to if the `enable_state_changes` flag is set to `true`. When a transition between '''OFF''' and '''IDLE''' occurs, the motors are engaged. When a transition between '''IDLE''' and '''OFF''' occurs, the motors are disengaged.
    }
  }
pub {
   0{
    name = /mav/imu
    type = sensor_msgs/Imu
    desc = Onboard IMU reading
   }
   1{
    name = /mav/pressure_height
    type = mav_msgs/Height
    desc = The height reported by the onboard pressure sensor (unfiltered)
   }
   2{
    name = /mav/pressure_height_filtered
    type = mav_msgs/Height
    desc = The height reported by the onboard pressure sensor (filtered)
   }
   3{
    name = /asctec/CTRL_INPUT
    type = asctec_msgs/CTRL_INPUT
    desc = !AscTec CTRL_INPUT message (see [[http://robotics.ccny.cuny.edu/wiki/AscTec/Docs | documentation]])
   }
  }

param{
    0.name = ~enable_state_changes
    0.type = bool
    0.default = `false`
    0.desc = whether or not to monitor the `mav/state` topic and engage/disengage motors.

    1.name = ~enable_ctrl_thrust
    1.type = bool
    1.default = `false`
    1.desc = enable thrust control over the serial interface

    2.name = ~enable_ctrl_roll
    2.type = bool
    2.default = `false`
    2.desc = enable roll control over the serial interface

    3.name = ~enable_ctrl_pitch
    3.type = bool
    3.default = `false`
    3.desc = enable pitch control over the serial interface

    4.name = ~enable_ctrl_yaw
    4.type = bool
    4.default = `false`
    4.desc = enable yaw control over the serial interface

    5.name = ~max_ctrl_thrust
    5.type = int
    5.default = `2200`
    5.desc = the maximum thrust ctrl that the autopilot will publish. '''Note''': this is in !AscTec units, and is meant to be used as a last line of safety. 

    6.name = ~max_ctrl_roll
    6.type = int
    6.default = `300`
    6.desc = the minimum/maximum roll ctrl that the autopilot will publish. '''Note''': this is in !AscTec units, and is meant to be used as a last line of safety. 

    7.name = ~max_ctrl_pitch
    7.type = int
    7.default = `300`
    7.desc = the minimum/maximum pitch ctrl that the autopilot will publish. '''Note''': this is in !AscTec units, and is meant to be used as a last line of safety. 

    8.name = ~max_ctrl_yaw
    8.type = int
    8.default = `600`
    8.desc = the minimum/maximum yaw ctrl that the autopilot will publish. '''Note''': this is in !AscTec units, and is meant to be used as a last line of safety. 
  }
```

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.

Please use our [Trac](http://robotics.ccny.cuny.edu/trac/) to
[report bugs](http://robotics.ccny.cuny.edu/trac/newticket?component=asctec_drivers/asctec_autopilot&type=defect)
or
[request features](http://robotics.ccny.cuny.edu/trac/newticket?component=asctec_drivers/asctec_autopilot&type=enhancement).
