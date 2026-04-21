## Nodes

### amtec_node

The Amtec node interfaces with the Schunk (formerly Amtec) pan tilt
unit. It provides services to control the motion of the unit, publishes
status messages and publishes transforms.

#### Parameters

##### Motion Parameters



```clearsilver
param {
  no_header=True

  0.name= ~<name>/pan_min_pos
  0.default= -3.5
  0.type= double
  0.desc= Minimum allowed pan position (in radians)

  1.name= ~<name>/pan_max_pos
  1.default= 3.5
  1.type= double
  1.desc= Maximum allowed pan position (in radians)

  2.name= ~<name>/pan_max_vel
  2.default= 2.0
  2.type= double
  2.desc= Maximum allowed pan velocity (in radians/sec)

  3.name= ~<name>/pan_max_acc
  3.default= 5.0
  3.type= double
  3.desc= Maximum allowed pan acceleration (in radians/sec/sec)

  4.name= ~<name>/pan_max_curr
  4.default= 10.0
  4.type= double
  4.desc= Maximum allowed pan current

  5.name= ~<name>/pan_c0
  5.default= 12
  5.type= integer
  5.desc= c0 gain for pan axis

  6.name= ~<name>/pan_damp
  6.default= 4
  6.type= integer
  6.desc= Damping gain for pan axis

  7.name= ~<name>/pan_a0
  7.default= 2
  7.type= integer
  7.desc= a0 gain for pan axis
}
```





```clearsilver
param {
  no_header=True

  0.name= ~<name>/tilt_min_pos
  0.default= -3.5
  0.type= double
  0.desc= Minimum allowed tilt position (in radians)

  1.name= ~<name>/tilt_max_pos
  1.default= 3.5
  1.type= double
  1.desc= Maximum allowed tilt position (in radians)

  2.name= ~<name>/tilt_max_vel
  2.default= 2.0
  2.type= double
  2.desc= Maximum allowed tilt velocity (in radians/sec)

  3.name= ~<name>/tilt_max_acc
  3.default= 5.0
  3.type= double
  3.desc= Maximum allowed tilt acceleration (in radians/sec/sec)

  4.name= ~<name>/tilt_max_curr
  4.default= 10.0
  4.type= double
  4.desc= Maximum allowed tilt current

  5.name= ~<name>/tilt_c0
  5.default= 18
  5.type= integer
  5.desc= c0 gain for tilt axis

  6.name= ~<name>/tilt_damp
  6.default= 3
  6.type= integer
  6.desc= Damping gain for tilt axis

  7.name= ~<name>/tilt_a0
  7.default= 1
  7.type= integer
  7.desc= a0 gain for tilt axis

  8.name= ~<name>tilt_use_break
  8.default= 1
  8.type= integer
  8.desc= Use hardware break to hold tilt axis position
}
```



##### Unit ID Parameters



```clearsilver
param {
  no_header=True

  0.name= ~<name>/pan_id
  0.default= 14
  0.type= integer
  0.desc= Id of pan axis

  1.name= ~<name>/tilt_id
  1.default= 13
  1.type= integer
  1.desc= Id of tilt axis
}
```



##### Frame Parameters



```clearsilver
param {
  no_header=True

  0.name= ~<name>/parent_frame
  0.default=`"head_link"`
  0.type= string
  0.desc= The frame id of the unit's parent frame

  1.name= ~<name>/amtec_frame
  1.default=`"amtec_link"`
  1.type= string
  1.desc= The frame id for the unit itself
}
```



##### Connection Parameters



```clearsilver
param {
  no_header=True

  0.name= ~<name>/port
  0.default=`"/dev/ttyUSB2"`
  0.type= string
  0.desc= The device connected to the unit

  1.name= ~<name>/parity
  1.default=`"N"`
  1.type= string
  1.desc= Parity of serial connection. Possible values are `"N"`, `"E"` and `"O"`

  2.name= ~<name>/baud_rate
  2.default=38400
  2.type= integer
  2.desc= Baud rate of serial connection

  3.name= ~<name>/stop_bits
  3.default=1
  3.type= integer
  3.desc= stop bits

  4.name= ~<name>/hardware_flow_control
  4.default=`0`
  4.type= integer
  4.desc= enable hardware flow control

  5.name= ~<name>/software_flow_control
  5.default=`0`
  5.type= integer
  5.desc= enable software flow control
}
```





```clearsilver
pub {
  0.name= ~<name>/pan_state
  0.type= amtec/AmtecState
  0.desc= The pan state
  1.name= ~<name>/tilt_state
  1.type= amtec/AmtecState
  1.desc= The tilt state
}
```





```clearsilver
srv {
  0.name= ~<name>/get_status
  0.type= amtec/GetStatus
  0.desc= Get the current position and velocity of unit
  1.name= ~<name>/halt
  1.type= amtec/Halt
  1.desc= Halt unit
  2.name= ~<name>/home
  2.type= amtec/Home
  2.desc= Home unit
  3.name= ~<name>/set_position
  3.type= amtec/SetPosition
  3.desc= Set desired position
  4.name= ~<name>/set_velocity
  4.type= amtec/SetVelocity
  4.desc= Home unit
  5.name= ~<name>/target_acceleration
  5.type= amtec/TargetAcceleration
  5.desc= Set desired acceleration to use when executing motion commands
  6.name= ~<name>/target_velocity
  6.type= amtec/TargetVelocity
  6.desc= Set desired velocity to use when executing position commands
  7.name= ~<name>/sweep_pan
  7.type= amtec/SweepPan
  7.desc= Begin a sinusoidal sweeping pattern of the pan axis  
  8.name= ~<name>/sweep_tilt
  8.type= amtec/SweepTilt
  8.desc= Begin a sinusoidal sweeping pattern of the tilt axis
}
```



### sweep_amtec

Sweeps pan axis of amtec using trapezoidal motion profiles instead of
the sinusoidal motion profiles provided by amtec_node directly. Uses the
services provided by amtec_node.



```clearsilver
param {
  0.name= ~<name>/pan_start
  0.default= -0.6
  0.type= double
  0.desc= Starting position of sweep pattern (in radians).

  1.name= ~<name>/pan_stop
  1.default= 0.6
  1.type= double
  1.desc= Ending position of sweep pattern (in radians)

  2.name= ~<name>/pan_velocity
  2.default= 2.5
  2.type= double
  2.desc= Maximum velocity to use in motion profile (in radians/sec)

  3.name= ~<name>/pan_acceleration
  3.default= 4.0
  3.type= double
  3.desc= Acceleration to use in motion profile (in radians/sec/sec)
}
```



### test_amtec

A node that will attempt to establish a connection to an amtec unit,
reset it, home it and then exit. the device and baud_rate should be
specified on the command line. Uses libamtec directly, it doesn't go
through amtec_node.
