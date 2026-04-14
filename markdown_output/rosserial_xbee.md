rosserial_xbee provides a simple way to wirelessly connect custom
sensors and actuators to ROS. It creates a point to multi-point network
using XBees. Each hardware node uses an XBee and a microcontroller
running rosserial to communicate to a network coordinator XBee connected
to a ROS computer.

![](attachment:rosserial_network.jpg)

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
factory fresh, use Digi\'s X-CTU software to program it.

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
``` To run xbee_network.py, supply as arguments to
the scrip the xbee\'s serial port and the ID \# of all of the hardware
node xbees. These IDs were programed into the xbee using setup_xbee.py
or Digi\'s X-CTU software.
