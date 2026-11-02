This is the only package among the ones in
[qb_device](https://index.ros.org/p/qb_device) which can be used as a
stand-alone ROS node, called *Communication Handler*. It wraps the
*qbrobotics®* API, manages the shared resources and provides a
multi-node from/to multi-device communication interface.

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



### qb_device_communication_handler

The Communication Handler provides seven services to interact with
*qbrobotics* devices connected to the system. It is assumed that each
device has a unique ID and that no other qbrobotics devices have the
same ID.

#### Services

- `/communication_handler/activate_motors`
  ([qb_device_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/qb_device_srvs/srv/Trigger.html)):
  Activates the motors of the device which ID is specified in the
  service request. The response `success` variable is set to `true`
  if motors are active.
- `/communication_handler/deactivate_motors`
  ([qb_device_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/qb_device_srvs/srv/Trigger.html)):
  Deactivates the motors of the device which ID is specified in the
  service request. The response `success` variable is set to `true`
  if motors are inactive.
- `/communication_handler/get_info`
  ([qb_device_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/qb_device_srvs/srv/Trigger.html)):
  Retrieves the printable configuration setup of the device which ID is
  specified in the service request. On error, the response `message`
  variable is empty.
- `/communication_handler/get_measurements`
  ([qb_device_srvs/srv/GetMeasurements](https://docs.ros.org/en/rolling/p/qb_device_srvs/srv/GetMeasurements.html)):
  Retrieves the motor positions and currents of the device which ID is
  specified in the service request. The response `success` variable is
  set to `true` if data retrieved (i.e. the response `currents` and
  `positions` variables) is meaningful.
- `/communication_handler/go_to_home`
  ([qb_device_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/qb_device_srvs/srv/Trigger.html)):
  Currently this service is only for qb SoftHand2 Research. It sends the
  device to its initial position.**COMING SOON FOR ALL qbrobotics
  DEVICES**
- `/communication_handler/initialize_device`
  ([qb_device_srvs/srv/InitializeDevice](https://docs.ros.org/en/rolling/p/qb_device_srvs/srv/InitializeDevice.html)):
  Initialize the communication with the device.
- `/communication_handler/set_commands`
  ([qb_device_srvs/srv/SetCommands](https://docs.ros.org/en/rolling/p/qb_device_srvs/srv/SetCommands.html)):
  Send the reference commands (i.e. the request `commands` variable)
  to the motors of the device which ID is specified in the service
  request.
- `/communication_handler/set_control_mode`
  ([qb_device_srvs/srv/SetControlMode](https://docs.ros.org/en/rolling/p/qb_device_srvs/srv/SetControlMode.html)):
  Currently this service is only for qb SoftClaw Research. Set the
  desired control mode. The accepted request field should be
  *deflection* or *position* **COMING SOON FOR ALL qbrobotics DEVICES**
