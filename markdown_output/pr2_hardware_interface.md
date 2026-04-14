## Hardware components

The PR2 hardware interface provides a C++ abstraction layer for the PR2
hardware that is controlled over the [etherCAT link](ethercat_hardware)
that runs through the robot. Most users should not have to deal directly
with this interface. If you are only interested in controlling the robot
joints, you should directly interact with
[pr2_mechanism_model](pr2_mechanism_model). Only very advanced users
that need direct access to the hardware should be using the PR2 hardware
interface.

-   \'\'\'[Hardware Interface](http://www.ros.org/doc/api/pr2_hardware_interface/html/classpr2__hardware__interface_1_1HardwareInterface.html):\'\'\'
    The \`HardwareInterface\` class provides access to the PR2 hardware
    components that are controlled via EtherCAT. These components
    include:

```{=html}
<!-- -->
```
-   \'\'\'[Actuators](http://www.ros.org/doc/api/pr2_hardware_interface/html/classpr2__hardware__interface_1_1Actuator.html):\'\'\'
    the PR2 robot contains 32 actuators, and each actuator consists of a
    motor and an encoder.

```{=html}
<!-- -->
```
-   \'\'\'[Pressure sensors](http://www.ros.org/doc/api/pr2_hardware_interface/html/classpr2__hardware__interface_1_1PressureSensor.html):\'\'\'
    the fingertips of the PR2 have pressure sensors that provide an
    array of force measurements.

```{=html}
<!-- -->
```
-   \'\'\'[Accelerometers](http://www.ros.org/doc/api/pr2_hardware_interface/html/classpr2__hardware__interface_1_1Accelerometer.html):\'\'\'
    the PR2 grippers contain 3 axis accelerometers. Instruction on
    communicating with these sensors in real-time can be found
    [here](ethercat_hardware/Tutorials/GripperAccelerometer).

```{=html}
<!-- -->
```
-   \'\'\'[Digital out](http://www.ros.org/doc/api/pr2_hardware_interface/html/classpr2__hardware__interface_1_1DigitalOut.html):\'\'\'
    The PR2\'s motor controller boards have one or more digital I/O
    pins. The digital I/Os can be used to control a variety of hardware
    such as a calibration LED or a camera trigger.

```{=html}
<!-- -->
```
-   \'\'\'[Projector](http://www.ros.org/doc/api/pr2_hardware_interface/html/classpr2__hardware__interface_1_1Projector.html):\'\'\'
    the PR2 head has a texture projector mounted on its head. The
    texture helps the stereo cameras to see objects that naturally have
    no texture.

```{=html}
<!-- -->
```
-   \'\'\'[AnalogIn](http://www.ros.org/doc/api/pr2_hardware_interface/html/classpr2__hardware__interface_1_1AnalogIn.html):\'\'\'
    Some EtherCAT devices such as Beckhoff EL3064 represent inputs as
    array of analog values.
