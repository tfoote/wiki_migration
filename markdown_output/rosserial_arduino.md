This package contains Arduino-specific extensions required to run
[rosserial_client](rosserial_client) on an Arduino. It is meant to
demonstrate how easy it is to integrate custom hardware and cheap
sensors into your ROS project using an Arduino. The Tutorials of this
package will walk you through setting up your Arduino environment,
creating a few example sketches and explain where to purchase the
additional hardware.

## Special defines

Some features can be enabled depending of `#define` statements added
before including `ros.h` in the sketch.

  -- ----------------------------------------------------------------- -- -------------------------------------------- -- ------------------------- --
     **Platform**                                                         **Feature**                                     **`#define`**             
     Arduino based on 32u4 (Leonardo, Micro)                              USB Serial (not pin 0 & 1)                      `USE_USBCON`              
     All Arduino variants                                                 Use Ethernet shield for rosserial over TCP      `ROSSERIAL_ARDUINO_TCP`   
     Teensy 3.x                                                           Hardware Serial (not USB)                       `USE_TEENSY_HW_SERIAL`    
     [STM32F1](https://github.com/rogerclarkmelbourne/Arduino_STM32)      Hardware Serial (not USB)                       `USE_STM32_HW_SERIAL`     
     [STM32Duino](https://github.com/stm32duino/Arduino_Core_STM32)       Use native Ethernet for rosserial over TCP      `STM32ETHERNET`           
  -- ----------------------------------------------------------------- -- -------------------------------------------- -- ------------------------- --

```wiki
'''STM32ETHERNET PR not yet merged'''

https://github.com/ros-drivers/rosserial/pull/395
```

### Example

For example, to use the `ROSSERIAL_ARDUINO_TCP` define, see the
[TcpHelloWorld](https://github.com/ros-drivers/rosserial/blob/dd76994c67c5e4997ef64837c07afb4eb0d4df27/rosserial_arduino/src/ros_lib/examples/TcpHelloWorld/TcpHelloWorld.ino#L15)
example.
