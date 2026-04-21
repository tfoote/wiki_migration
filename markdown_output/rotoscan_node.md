![](attachment:leuze-rod4plus.jpg)

## Usage

This package adapts the Leuze rotoScan series of laser range finders.
Therefore it behaves like any other ROS laser range finder driver and
publishes a \<\<MsgLink(sensor_msgs/LaserScan)\>\> on the \"**scan**\"
topic whenever a new scan comes in.

Configuration of the laser range finder is not supported and requires a
vendor-provided tool.

*Formerly named rod4_node.*

## Supported Hardware

The driver currently supports following connection types and has been
confirmed to work with following models:

-   Ethernet:
-   [ROD-4](http://www.leuze.de/products/los/mess/rod4/rod4_de.html)
-   Serial port:
-   [RS4](http://www.leuze.de/products/las/slsc/rs4/p_01_de.html)
    (RS232)

\... but might be extended to support more interfaces or models.

## Node configuration

frame_id(string, default: \"laser\"):: Transform frame id to be used in
the message header.

range_max(float, default: 40.):: *range_max* to be used in message body.
Differs among models.

### Ethernet specific

The underlying network protocol implementation has been stable for more
than a year now. All testing has been done with a \"ROD4 plus\" unit.

host(string, default: \"192.168.1.1\") :: Hostname/IP address of the
laser range finder.

port(string, default: \"9008\") :: Port of of the laser range finder.

### Serial port specific

device(string, default: \"/dev/ttyUSB0\") :: Serial port device where
the rotoScan is connected to.

baudrate(int, default: 57600) :: Serial baudrate configured in rotoScan.

## Source repository

<https://svn-agbkb.informatik.uni-bremen.de/dfki-sks-ros-pkg/trunk/dfki_sks_laser_drivers/rotoscan_node>
