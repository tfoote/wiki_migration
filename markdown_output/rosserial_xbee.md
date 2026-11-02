rosserial_xbee provides a simple way to wirelessly connect custom
sensors and actuators to ROS. It creates a point to multi-point network
using XBees. Each hardware node uses an XBee and a microcontroller
running rosserial to communicate to a network coordinator XBee connected
to a ROS computer.

![attachment:rosserial_network.jpg](doc/rosserial_network.jpg)

Example network diagram. Each hardware node could be a separate
temperature sensor, rfid reader, ultrasounic ranger, clap detector,
etc\...

Using rosserial_xbee, you can set up a network of sensors around your
home to report back to ROS or just use it to wirelessly control a
homebrew robot.

There are two main tools provided : setup_xbee.py and xbee_network.

## setup_xbee.py

setup_xbee.py is configuration script for Xbees. It takes factory fresh
xbee and programs it to work with your rosserial network. If XBee is not
factory fresh, use Digi's X-CTU software to program it.



```
./setup_xbee.py [options] port my_adr

    port :    serial port of port of the xbee (/dev/ttyUSB0)
    my_adr:   MY address is the 16 bit address of this xbee in the
              network. This must be a unique address in the network.
              This address is always 0 for the coordinator.

Options:
  -h, --help            show this help message and exit
  -P PAN_ID, --pan_id=PAN_ID
                        Pan ID of the xbee network.  This ID must be the same
                        for all XBees in your network.
  -c CHANNEL, --channel=CHANNEL
                        Frequency channel for the xbee network. The channel
                        value must be the same for all XBees in your network.
  -C, --coordinator     Configures the XBee as Coordinator for the network.
                        Only make the XBee connected to the computer a
                        coordiantor
```



## xbee_network.py

This node connects to the master xbee, takes the rosserial communication
from all of the rosserial devices and forwards it to the rest of ROS. It
subscribes / publishes any topic requested by its hardware nodes



```
./xbee_network.py <xbee_serial_port> ID1 [ ID2 ID3 ....]
```

 To run xbee_network.py, supply as arguments to
the scrip the xbee's serial port and the ID \# of all of the hardware
node xbees. These IDs were programed into the xbee using setup_xbee.py
or Digi's X-CTU software.

## Tutorials

- [An Example rosserial_xbee Network](#an-example-rosserial_xbee-network):
  A guide to building a simple rosserial_xbee network
- [ROS RC Car](#ros-rc-car):
  controlling an a small robot base with rosserial_xbee
- [RC_BOT using Xbee](#rc_bot-using-xbee)

## An Example rosserial_xbee Network

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Arduino IDE Setup](https://index.ros.org/p/rosserial_arduino).
- **Description:** A guide to building a simple rosserial_xbee network
- **Tutorial Level:** BEGINNER

The rosserial_xbee package is meant to simplify setting up a network of
ROS hardware nodes throughout a building. This tutorial will show how to
have two Arduino publishers on a rosserial_xbee network. It will walk
you through purchasing hardware, programming your XBees, programming
your Arduinos, and launching the network.

### Hardware

A rosserial_xbee network needs a computer running ROS, an XBee connected
to the computer, and rosserial hardware nodes with XBees. All Xbees used
in a rosserial_xbee network must be XBee series 1. Series 1 and 2 have
different binary APIs which make them incompatible. Arduinos were chosen
as the hardware platform because as of the writing of this tutorial,
they have the only complete implementation of rosserial. However, you
can use any board with a serial port and rosserial implementation.

For this tutorial, you can purchase :

- 3 x [XBee Series 1](http://www.sparkfun.com/products/8742)
- 1 x [XBee Explorer](http://www.sparkfun.com/products/8687)
- 1 x [USB Cable - A-to-miniB](http://www.sparkfun.com/products/10424)
- 2 x [XBee shield](http://www.sparkfun.com/products/9976)
- 2 x [Header](http://www.sparkfun.com/products/116)
- 2 x [Arduino Uno](http://www.sparkfun.com/products/9950)

Plus, you may want to purchase a
[battery pack](http://www.sparkfun.com/products/9835) or
[power supply](http://www.sparkfun.com/products/298) for your Arduino.
These will allow you to set up your hardware nodes away from a computer.

Before you begin, you will need to solder header on to your XBee shield
so that you can plug it into your Arduino.

### Software

#### Configuring the XBees

The first step in setting up our network is setting up the XBees.
Normally to set up the XBees you would use Digi's Windows only X-CTU
software. To simplify deployment of rosserial_xbee networks we have
included setup_xbee.py to program your xbee from Linux.

Plug your first Xbee into your Xbee Explorer and attach the Xbee
explorer via USB. It should show up as /dev/ttyUSB\*.

The first XBee that we will set up will be the coordinator for the
network. It will be the XBee connected to the computer. Run



```
rosrun rosserial_xbee setup_xbee.py -C /dev/ttyUSB0 0
```

 This will set up the XBee and set its ID to 0.
All rosserial_xbee network coordinators should have an ID of 0. It also
sets up some default configurations. The XBee now communicates using API
mode 2 (a binary protocol with escape characters) at 57600 baud. It is
also on the default network ID (1331) and frequency channel (D).

Its a good idea to physically mark the XBee with sharpie as C0
(coordinator with id). You are going to have several XBees and you need
to keep track of how they are programmed.

Next, we are going to program the other two XBees. These XBees will be
configured as end devices in our network. They will always send their
data to the XBee with ID 0. Additionally, their communication interface
is transparent. They communicate in API mode 0 at 56700 baud. They will
be connected to our Arduinos.

XBee for node 1



```
rosrun rosserial_xbee setup_xbee.py /dev/ttyUSB0 1
```

 XBee for node 2



```
rosrun rosserial_xbee setup_xbee.py /dev/ttyUSB0 2
```



#### Programing Your Arduino

Open up your Arduino IDE, copy the following code into your IDE, and
then program your Node 1 Arduino with the code.



```cplusplus

#include <ros.h>
#include <std_msgs/String.h>

ros::NodeHandle nh;

std_msgs::String str_msg;
ros::Publisher chatter("chatter", &str_msg);

unsigned char hello[] = "Hello from Node 1!";

void setup()
{
  nh.initNode();
  nh.advertise(chatter);
}

void loop()
{
  str_msg.data = hello;
  chatter.publish( &str_msg );
  nh.spinOnce();
  delay(1000);
}
```

 Now program your Node 2 Arduino with the same
code, but change the greeting from to



```cplusplus
unsigned char hello[] = "Hello from Node 2!";
```



### Testing

Now its time to wireup our hardware nodes and connect the coordinator
XBee to the computer using the XBee explorer.

Run roscore 

```
roscore
```

 In a new terminal launch the
rosserial_xbee node and tell it the XBee Explorer's serial port and the
id numbers of your node XBees. 

```
rosrun rosserial_xbee xbee_network.py /dev/ttyUSB0 1 2
```

 Now in a new
terminal launch rostopic echo and listen to the chatter of your
rosserial_xbee nodes!



```
rostopic echo chatter
```



### Whats next

This tutorial went over the most basic hardware node. It is now time to
add sensors and actuators to your nodes so that you can augment your ROS
system. Now you can collect information anywhere it is produced instead
of being tied to a robot or a computer. You can use temperature sensors,
barometers, door sensors, switches, Ultrasound rangers, IR Rangers, PIR
motion detectors, light sensors, etc. Demos of many of these sensors are
available in [rosserial_arduino_demos](rosserial_arduino_demos) You also
attach motors, servos, or linear actuators to your hardware nodes to
augment your robots.

## ROS RC Car

- **Note:** This tutorial assumes that you are comfortable with
  rosserial_arduino.
- **Description:** controlling an a small robot base with rosserial_xbee
- **Tutorial Level:** BEGINNER

There a lot of times when as a roboticist, we just want to make a little
robot drive around. If you are not using a robotics framework like ROS,
you need to write the teleoperation code for keyboards and joysticks
yourself, you need to set up the wireless communication, and you need to
define the protocol that you are using to communicate with the robot. By
using ROS with even your smallest robot creation, you can leverage the
ROS infrastructure. In this tutorial we are going to cover controlling
the most bare bones robot base possible. It will be based off of
rosserial_arduino, rosserial_xbee, and the turtlebot teleop programs.

In the end, you will can have a little robot like the one below, that
you can control via ROS.

![attachment:rosseriaL_rc.JPG](doc/rosseriaL_rc.JPG)

### Hardware

You need motors, wheels, an arduino, Xbees, a motor controller, and a
chassis.

- [Xbee Shield](http://www.sparkfun.com/products/9976)
- [Xbee Explorer](http://www.sparkfun.com/products/8687)
- [Motor Driver Shield](http://www.sparkfun.com/products/9815)
- 2 x [Xbees](http://www.sparkfun.com/products/8665)
- 2
  x[Arduino Stackable Header Kit](http://www.sparkfun.com/products/10007)
- Motors- There are a lot of different, good choices for motors. I am a
  big fan of
  [http://www.solarbotics.com/products/gmpw_deal/ Solarbotics GM9 with wheels combo](http://www.solarbotics.com/products/gmpw_deal/ Solarbotics GM9 with wheels combo).
- A chassis of your own design. If you would like, you can use the CAD
  model of the above robot. ADD LINK
- Battery. Again. This choice is up to you. A good choice is a
  rechargable 9V battery.
  [Li-ion 9V from Sparkfun](http://www.sparkfun.com/products/10053) and
  [charger](http://www.sparkfun.com/products/10265). If you start doing
  a lot of small robotics, RC plane lipo batteries are the best.

### Arduino Code

### Launch Files

### Running the programs

## RC_BOT using Xbee

note = Just trying description = A RC bot is prepared on Arduino
platform using Xbee for wireless communication

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: here also trying.
