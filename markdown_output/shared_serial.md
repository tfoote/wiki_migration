## Documentation

Shared_serial is a server that handles concurrent access to a serial
port. This may be useful when multiple devices are connected to the same
multi-drop bus (e.g. RS485) and you want to keep the system modular. It
comes with a C++ client library for easy access, but can be used through
normal messages and services as well.

To launch the node, use a launch file that sets the port and baud rate,
like in



```
<launch>
	<node name="motor_comm" pkg="shared_serial" type="server">
		<param name="port_name" value="/dev/ttyUSB0"/>
		<param name="port_type" value="RS485_FTDI"/>
		<param name="baud_rate" value="921600"/>
	</node>
</launch>
```



Possible port types are RS232, RS485_FTDI, RS485_EXAR, RS485_SMSC and
TCP. For TCP, the port name is "ip:port". The default 3mxl baud rate
is 921600.

## Report a Bug

Use trac to
[report bugs](https://svn.3me.tudelft.nl/trac/dri-ros-pkg/newticket?component=shared_serial&type=defect&&shared_serial)
or
[request features.](https://svn.3me.tudelft.nl/trac/dri-ros-pkg/newticket?component=shared_serial&type=enhancement&shared_serial)
\[
[View active tickets](https://svn.3me.tudelft.nl/trac/dri-ros-pkg/query?component=shared_serial&status=assigned&status=new&status=reopened)
\]
