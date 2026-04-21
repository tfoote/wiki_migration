## Overview

The modbus stack provides a wrapper from the modbus TCP communication to
standardized ROS messages. The modbus stack is based on pymodbus, is
written in Python and contains 3 packages:

-   The package modbus is the basic python wrapper for a modbus server
    and client for ROS
-   The package modbus_cognex_insight inherits the modbus client base
    class and which uses specific registers. The client can send job_ids
    to the camera and retrieve the results of the jobs as well as
    barcodes and strings.
-   The package modbus_plc_siemens inherits the modbus client base class
    and changes the register size.

## Install

1\. Clone the stack into your catkin workspace 1.
[git clone https://github.com/HumaRobotics/modbus.git](https://github.com/HumaRobotics/modbus) 1.
Invoke a catkin_make in your catkin root

After the catkin_make the Python modbus classes are also available from
the outside and can be easily integrated in other packages.

## Tutorials

-   [Generic modbus client/server package](http://www.generationrobots.com/en/content/87-modbus-package)
-   [Modbus package for a Siemens S7-1200 PLC](http://www.generationrobots.com/en/content/89-plc-siemens-modbus-ros-package)
-   [Modbus package for a Cognex Insight 7200C](http://www.generationrobots.com/en/content/88-modbus-cognex-in-sight)

*Even is the modbus packages have only been tested with a few Siemens
PLCs and Insight cameras, the package may also work for other models, as
long as they support a modbus TCP server. However the hardware model has
to be changed inside the Insight or Step7 project.*

## Examples

Siemens S7-1200 PLC controlled by a Python ROS node:

\<\<Youtube(1YarNPR-FwI&feature=youtu.be)\>\>

## Nodes

```clearsilver
 name = modbus_client.py
 desc = Creates a Python modbus TCP client and runs several tests using the topic and Python interface. The modified client for the Siemens PLC and Insight camera use the same topics, but address different registers.
sub {
   0{
    name = modbus_wrapper/output
    type = std_msgs/Int32MultiArray
    desc = Corresponds to the outputs of your PLC. Set a non zero value to activate an output.
    }
  }
 pub {
   0{
    name = modbus_wrapper/input
    type = std_msgs/Int32MultiArray
    desc = Corresponds to the inputs of the PLC.
   }
```

```clearsilver
 name = modbus_server.py
 desc = Creates a Python modbus TCP server and runs several tests, if combined with the client.
sub {
   0{
    name = modbus_server/read_from_registers
    type = std_msgs/Int32MultiArray
    desc = Corresponds to the readable modbus registers.
    }
  }
 pub {
   0{
    name = modbus_server/write_to_registers
    type = std_msgs/Int32MultiArray
    desc = Corresponds to the writeable modbus registers. 
   }
```
