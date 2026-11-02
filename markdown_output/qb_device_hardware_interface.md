This package is barely usable alone since it provides only the common
features to be exploited and expanded in the derived packages (cf.
[qb_hand](https://index.ros.org/p/qb_hand) and
[qb_move](https://index.ros.org/p/qb_move)).

### qb_device_hardware_interface

This device-independent library provides all the common structures to
interface both the [qb_hand](https://index.ros.org/p/qb_hand) and the
[qb_move](https://index.ros.org/p/qb_move) ROS packages with their
related physical devices. It exploits the Communication Handler (cf.
[qb_device_driver](https://index.ros.org/p/qb_device_driver)) to manage
the serial communication and inherits its core from the
[hardware_interface](https://index.ros.org/p/hardware_interface) for the
sake of compatibility with other robots which use ROS. This package
paves the way for control applications (cf.
[qb_device_control](https://index.ros.org/p/qb_device_control)).

#### Published Topics

- `/<namespace>/state` (`qb_device_msgs::StateStamped`): Advertise the
  whole device state, i.e. currents and positions for both actuators and
  joints, plus additional device infos.

#### Services Called

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
- `/communication_handler/set_commands`
  ([qb_device_srvs/srv/SetCommands](https://docs.ros.org/en/rolling/p/qb_device_srvs/srv/SetCommands.html)):
  Send the reference commands (i.e. the request `commands` variable)
  to the motors of the device which ID is specified in the service
  request.

#### Parameters

- `~actuators` (`string[]`): The actuator names in the
  `robot_description`.
- `~device_id` (`int`, default: `1`): The device ID, in range \[`1`,
  `128`\].
- `~joints` (`string[]`): The joint names in the `robot_description`.
- `~namespace` (`string`, default: `qbdevice_<device_id>`): The device
  namespace used to avoid name clashes among same-type devices.
- `~robot_description` (`string`): The
  [urdf](https://index.ros.org/p/urdf) xml robot description.
- `~transmission` (`string`, default: `transmission`): The name of the
  current transmission derived from
  `transmission_interface::Transmission`: *qbhand* and *qbmove* use
  their own specific transmission.
