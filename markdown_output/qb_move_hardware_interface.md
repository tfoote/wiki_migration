This package is barely usable alone since it provides only the hardware
interface for the *qbrobotics® qbmove* device.

## API

### qb_move_hardware_interface

This library inherits from the base device-independent
[qb_device_hardware_interface](https://index.ros.org/p/qb_device_hardware_interface)
(therefore provides the same ROS API) and extends its features
specifically for the *qbmove*. In brief, it provides the specific
transmission interface for the *qbmove*, which is the only thing that is
really device dependent, and exploits the same hardware interfaces
properly initialized (cf.
[qb_device_hardware_interface](https://index.ros.org/p/qb_device_hardware_interface)),
and the same Communication Handler to talk to the physical device (cf.
[qb_device_driver](https://index.ros.org/p/qb_device_driver)).
Furthermore, it provides the following additional parameters.

#### Parameters

- `~command_with_position_and_preset` (`boolean`): Chose whether to
  control the *qbmove* using shaft position and stiffness preset
  references (when `true`), or directly using actuator position
  references (when `false`).
- `~encoder_resolutions` (`int`, default: `3000`): The device encoder
  resolutions, in range \[`0`, `8`\].
- `~preset_ticks_limit` (`int`): The *qbmove* stiffness preset upper
  limit, expressed in motor *ticks*.



```wiki
Be aware that it can be dangerous to change `encoder_resolutions` and `preset_ticks_limit` arbitrarily. These values '''must match''' their relative configurations set in the device.
```
