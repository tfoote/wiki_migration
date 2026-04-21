PMAD stands for power management and distribution, Arduino in
combination with solid state relays is being used to switch DC loads on
and off. However, the same could be used to perform I/O (input/output
operations) of digital/analog interface using arduino.

# Step 1

The first thing is to load the provided sketch into your Arduino board.
The sketch is
[`arduino/sketch.txt`](https://sourceforge.net/p/ajh-ros-pkg/code/HEAD/tree/trunk/pmad/arduino/sketch.txt).
You should copy this sketch into the Arduino GUI and it should compile
without problems (hopefully).

# Step 2

Once you load the sketch above into your Arduino, you should be able to
plug the Arduino into a USB port on your computer and start the PMAD
service. This service controls all of the communications to the Arduino.
You can start the service by using:

`rosrun pmad pmad_service.py`

Note that if the Arduino does not connect as `/dev/ttyUSB0`, you will
have to preset a ROS parameter `tty` that defines the port the Arduino
is connected on. You might have to set `tty` to `/dev/ttyUSB1` for
example. The parameter is just a simple string containing the device
path.

# Step 3

Once you set up the service, you can toggle the digital pins with
service calls like:

`rosservice call pmad_switch_control 4 0`

This for example will set digital pin 4 to LOW (represented by 0). You
can also change digital pin 13. This is convenient to test with \-- you
can try turning on and off the LED attached to digital pin 13 that is
provided on most Arduino boards (Not all boards provide this LED. Check
for this for your board of choice.)

# Step 4

Additionally, you may want to periodically receive a status packet from
the Arduino. This status packet contains the state of the 4 digital pins
4, 5, 6, and 7, but also provides the analog values on analog inputs 0,
1, 2, and 3, as well as a command executed counter.

If you want to get this status packet to be a "topic", there is an
application

`rosrun pmad pmad_status_publisher.py`

This application will publish the status data once per second. The
status message is defined in msg/Status.msg.

# More Information

There is also more information in the comments at the top of the
provided Arduino sketch.
