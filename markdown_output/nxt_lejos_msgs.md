## Messages

The messages below are used to:

-   publish sensor data from NXT sensors on ROS topics
-   control the robot
-   control individual motors
-   make the robot play tones

See the [nxt_lejos_lcp_proxy](nxt_lejos_lcp_proxy) package for more
details.

Messages from the [nxt_msgs](nxt_msgs) package are also used by
[nxt_lejos_lcp_proxy](nxt_lejos_lcp_proxy).

\<\<MsgSrvDoc(nxt_lejos_msgs False)\>\>

## Message Details

### Battery

The Battery message returns the current NXT battery level in volts.

### Compass

The Compass message returns the heading reported by a !HiTechnic Compass
sensor, in degrees.

### Decibels

The Decibels message returns the sound level in decibels reported by a
sound sensor.

### DNSMessage

The Differential Navigation System Command message allows commands to be
sent to NXT leJOS robot.

The commands currently supported are:

-   forward
-   backward
-   rotateLeft
-   rotateRight
-   travel \<distance\>
-   rotate \<angle\>
-   setRotateSpeed \<speed\>
-   setTravelSpeed \<speed\>

### JointPosition

The !JointPosition message is used to move a specified motor by a
specified number of degrees.

### JointVelocity

The !JointVelocity message is used to make a specific motor move at a
specified speed in degrees per second.

### Tone

The Tone message is used to play a specified tone on the NXT for a
specified duration, in milliseconds.
