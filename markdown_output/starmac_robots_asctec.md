## Nodes

```clearsilver
 name = asctec_adapter
 desc = Bridge between starmac_flyer vehicle-agnostic code and the asctec_autopilot driver package. Enables support for Ascending Technologies' [[http://www.asctec.de/asctec-pelican/|Pelican]] MAV.
 sub {
   0{
    name = teleop_flyer/motor_enable
    type = std_msgs/Bool
    desc = Should only be True whenever joystick trigger (deadman switch) is pressed
    }
   1{
    name = controller_mux/output
    type = flyer_controller/control_mode_output
    desc = The output of the currently active control mode
    }
   2{
    name = odom
    type = nav_msgs/Odometry
    desc = State vector
    }
   3{
    name = asctec_proc/imu
    type = sensor_msgs/Imu
    desc = IMU readings from asctec_autopilot
    }
   4{
    name = ~land_now
    type = std_msgs/Bool
    desc = Set to true to initiate rapid landing
    }
   5{
    name = autopilot/LL_STATUS
    type = asctec_msgs/LLStatus
    desc = Low-level status message (battery voltage, etc) from asctec_autopilot
    }
  }
pub {
0{
    name = <based on output_topic param>
    type = asctec_msgs/CtrlInput
    desc = Control input messages for astec_autopilot
    }
1{
    name = <based on estop_topic param>
    type = std_msgs/Bool
    desc = Emergency stop (motor kill) message to astec_autopilot
    }
2{
    name = /diagnostics
    type = diagnostic_msgs/DiagnosticStatus
    desc = Diagnostics
    }
}
 param{
    0{
    name = ~output_topic
    type = string
    default = `"autopilot/CTRL_INPUT"`
    desc = Topic on which to publish output
    }
    1{
    name = ~estop_topic
    type = string
    default = `"autopilot/ESTOP"`
    desc = Topic on which to publish emergency stop command
    }
    2{
    name = ~deadman_timeout
    type = double
    default = 0.5
    desc = Timeout in seconds
    }
    3{
    name = ~alt_KP
    type = double
    default = 200.0
    desc = Altitude controller proportional gain in thrust counts per meter
    }
    4{
    name = ~alt_KI
    type = double
    default = 15.0
    desc = Altitude controller integral gain in thrust counts per meter-second
    }
    5{
    name = ~alt_KD
    type = double
    default = 300.0
    desc = Altitude controller derivative gain in thrust counts per m/s
    }
    6{
    name = ~alt_KDD
    type = double
    default = 0.0
    desc = Altitude controller acceleration gain in thrust counts per m/s/s
    }
    7{
    name = ~alt_Ilimit
    type = double
    default = 5.0
    desc = Altitude controller integral term limit in thrust counts
    }

    8{
    name = ~yaw_KP
    type = double
    default = 1.0
    desc = Yaw controller proportional gain in deg/s per deg
    }
    9{
    name = ~yaw_KI
    type = double
    default = 1.0
    desc = Yaw controller integral gain in deg/s per deg-second
    }
    10{
    name = ~yaw_KD
    type = double
    default = 0.0
    desc = Yaw controller derivative gain in deg/s per deg/s
    }
    12{
    name = ~yaw_Ilimit
    type = double
    default = 5.0
    desc = Yaw controller integral term limit in deg/s
    }

    13{
    name = ~yaw_rate_limit
    type = double
    default = 4.0
    desc = Yaw controller output rate limit in deg/s
    }
    14{
    name = ~roll_slew_rate_limit
    type = double
    default = 10.0
    desc = Maximum change in output roll angle command in deg/s/s
    }
    15{
    name = ~pitch_slew_rate_limit
    type = double
    default = 10.0
    desc = Maximum change in output pitch angle command in deg/s/s
    }
    16{
    name = ~yaw_slew_rate_limit
    type = double
    default = 5.0
    desc = Maximum change in yaw angle command in deg/s/s
    }

    17{
    name = ~nominal_thrust
    type = int
    default = 1950
    desc = Thrust value at vertical equilibrium in counts (0..4095)
    }
    18{
    name = ~thrust_mult
    type = double
    default = 1.0
    desc = Factor by which output thrust will be multiplied (for testing/troubleshooting)  (0..1.0)
    }
    19{
    name = ~max_thrust
    type = int
    default = 2100
    desc = Maximum thrust value that will be output in counts (0..4095)
    }
    20{
    name = ~accel_bias
    type = double
    default = 9.81
    desc = Value in m/s/s to subtract from z acceleration before using in altitude controller acceleration term
    }
    21{
    name = ~land_now_thrust_decrease_rate
    type = int
    default = 200
    desc = How fast to decrease commanded thrust in counts per second when 'land now' is commanded
    }
    22{
    name = ~land_now_min_thrust_ratio
    type = double
    default = 0.5
    desc = When 'land now' is commanded reduce thrust to this level (as fraction of `~nominal_thrust`) then keep it constant
    }
    23{
    name = ~pitch_trim
    type = double
    default = 0.0
    desc = Will be added to commanded pitch (deg)
    }
    24{
    name = ~roll_trim
    type = double
    default = 0.0
    desc = Will be added to commanded roll (deg)
    }
    25{
    name = ~yaw_offset
    type = double
    default = 0.0
    desc = Angle in degrees by which to rotate (CW as viewed from above) the forward direction of the vehicle, in terms of how pitch and roll commands are interpreted. The default of zero makes 'forward' the standard direction for the Pelican, i.e. towards the rotor arm with orange tape. The normal use case for this would be when you have a forward-facing sensor (e.g. Kinect), and are flying manually and want to fly from the Kinect's point of view.
    }

}
```
