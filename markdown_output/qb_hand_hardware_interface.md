This package is barely usable alone since it provides only the hardware
interface for the *qbrobotics® qbhand* device.

## API

### qb_hand_hardware_interface

This library inherits from the base device-independent
[qb_device_hardware_interface](qb_device_hardware_interface) (therefore
provides the same ROS API) and extends its features specifically for the
desired *qbhand*. In brief, it provides the specific transmission
interface for the hand, which is the only thing that is really device
dependent, and exploits the same hardware interfaces properly
initialized (cf.
[qb_device_hardware_interface](qb_device_hardware_interface)) and the
same Communication Handler to talk to the physical device (cf.
[qb_device_driver](qb_device_driver)).
