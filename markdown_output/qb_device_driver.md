This is the only package among the ones in [qb_device](qb_device) which
can be used as a stand-alone ROS node, called *Communication Handler*.
It wraps the *qbrobotics®* API, manages the shared resources and
provides a multi-node from/to multi-device communication interface.

## Communication Handler

The *Communication Handler* node manages the serial communication from
the ROS ecosystem to the physical *qbrobotics* devices connected to it
through any serial ports, and vice versa. The need of such a mediator is
demanded to the possibility to connect several devices together (i.e. in
a chain) and access them through a single serial port. Each ROS node
representing a device has to request services to the owner of the shared
resources, i.e. the Communication Handler.

### Command-line tools

To start an instance of the Communication Handler node, execute the
following command from a terminal (it **does not require** any
configuration parameters): 

```
roslaunch qb_device_driver communication_handler.launch
```




```clearsilver
name = qb_device_communication_handler
desc = The Communication Handler provides seven services to interact with ''qbrobotics'' devices connected to the system. It is assumed that each device has a unique ID and that no other qbrobotics devices have the same ID.
srv {
  0.name = /communication_handler/activate_motors
  0.type = qb_device_srvs/Trigger
  0.desc = Activates the motors of the device which ID is specified in the service request. The response `success` variable is set to `true` if motors are active.
  1.name = /communication_handler/deactivate_motors
  1.type = qb_device_srvs/Trigger
  1.desc = Deactivates the motors of the device which ID is specified in the service request. The response `success` variable is set to `true` if motors are inactive.
  2.name = /communication_handler/get_info
  2.type = qb_device_srvs/Trigger
  2.desc = Retrieves the printable configuration setup of the device which ID is specified in the service request. On error, the response `message` variable is empty.
  3.name = /communication_handler/get_measurements
  3.type = qb_device_srvs/GetMeasurements
  3.desc = Retrieves the motor positions and currents of the device which ID is specified in the service request. The response `success` variable is set to `true` if data retrieved (i.e. the response `currents` and `positions` variables) is meaningful.
  4.name = /communication_handler/go_to_home
  4.type = qb_device_srvs/Trigger
  4.desc = Currently this service is only for qb SoftHand2 Research. It sends the device to its initial position.'''COMING SOON FOR ALL qbrobotics DEVICES'''
  5.name = /communication_handler/initialize_device
  5.type = qb_device_srvs/InitializeDevice
  5.desc = Initialize the communication with the device.

  6.name = /communication_handler/set_commands
  6.type = qb_device_srvs/SetCommands
  6.desc = Send the reference commands (i.e. the request `commands` variable) to the motors of the device which ID is specified in the service request.
  7.name = /communication_handler/set_control_mode
  7.type = qb_device_srvs/SetControlMode
  7.desc = Currently this service is only for qb SoftClaw Research. Set the desired control mode. The accepted request field should be ''deflection'' or ''position'' '''COMING SOON FOR ALL qbrobotics DEVICES'''
}
```


