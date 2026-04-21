## Documentation

Driver for Dynamixel servos and 3mxl motor board. This package provides
a library and interactive test node, no ROS interface.

For the main API, see the documentation of the
[C3mxl](http://docs.ros.org/hydro/api/threemxl/html/classC3mxl.html)
class.

## Initialization

### Direct communication

You can either communicate using the standard Linux serial port API
(`/dev/ttyXXXX`) or directly using the FTDI driver (if you have an
FTDI USB to serial converter). The latter is generally faster and more
reliable.

#### LxSerial

```cplusplus
#include <threemxl/C3mxl.h>

// ...

C3mxl *motor = new C3mxl();
LxSerial *serial_port = new LxSerial();
CDxlConfig *config = new CDxlConfig();

serial_port->port_open("/dev/ttyUSB0", LxSerial::RS485_FTDI);
serial_port->set_speed(LxSerial::S921600);
motor->setSerialPort(serial_port);

motor->setConfig(config->setID(109));
motor->init(false);
```

#### LxFTDI

You can find the USB ID using `lsusb`.

```cplusplus
#include <threemxl/C3mxl.h>
#include <threemxl/LxFTDI.h>

// ...

C3mxl *motor = new C3mxl();
LxSerial *serial_port = new LxFTDI();
CDxlConfig *config = new CDxlConfig();

serial_port->port_open("i:0x0403:0x6001", LxSerial::RS485_FTDI);
serial_port->set_speed_int(921600);
motor->setSerialPort(serial_port);

motor->setConfig(config->setID(109));
motor->init(false);
```

### shared_serial

To use multiple 3mxl boards on a single bus, use the
[shared_serial](shared_serial) node and
[C3mxlROS](http://docs.ros.org/hydro/api/threemxl/html/classC3mxlROS.html)
class. A launch file would look like this:

```
<launch>
        <node name="threemxl_com" pkg="shared_serial" type="server" output="screen">
                <param name="port_name" value="/dev/ttyUSB1"/>
                <param name="port_type" value="RS485_FTDI"/>
                <param name="baud_rate" value="921600"/>
        </node>
	<node name="dxl_ros_example" pkg="threemxl" type="example" args="threemxl_com" output="screen"/>
</launch>
```

The motor can then be initialized using

```cplusplus
#include <threemxl/C3mxlROS.h>

// ...

C3mxlROS *motor = new C3mxlROS("/threemxl_com");
CDxlConfig *config = new CDxlConfig();

motor->setConfig(config->setID(109));
motor->init(false);
```

## Reading state

For efficiency reasons, reading state information is split in two sets
of functions, `get\...()` and `present\...()`. `get\...()`
functions retrieve the state from the motor, while `present\...()`
functions return the information to the caller. An example:

```cplusplus
ros::Rate loop_rate(10);
motor->setPos(0);
do
{
  loop_rate.sleep();
  motor->getPos();
} while (ros::ok() && fabs(motor->presentPos()) > 0.01);
```

It is possible to retrieve more than one piece of state information at
the same time, e.g. using `getState()`.

## Frequently Asked Questions

-   For testing the motor, you can use the `console` node in the
    threemxl package. It takes an optional argument for the port name
    (default `/dev/ttyUSB0`).
-   By default, the 3mxl board in the hand setup runs at 921600bps with
    ids 108 (testing motor) and 109 (gripper).
-   To avoid having to set permissions on `/dev/ttyUSB0` every time
    you plug in the board, you can add yourself to the `dialout` group
    using `sudo usermod -a -G dialout username ` You will need to log
    out and in for the changes to take effect.
