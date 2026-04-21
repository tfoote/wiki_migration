## ROS API

This package provides an interface to a micro controller board with
which an array of ultrasonic sensors are connected and distance to the
surrounding environment can be calculated based on the input gathered
from the ultrasonic sensors.

```clearsilver
 name = us_driver
 desc = The `us_driver` node publishes <<MsgLink(ipa_odroidx_ultrasonic_interface/ExRangeArray)>> messages based on how the ultrasonic sensors are configured and their gathered input. Each sensor can be configured as a pinging sensor or a listening sensor. Pinging sensors are activated to send out an echo which are then received by the themselves and the other sensors configured as listening sensors. Configuration of a sensor as a pinging sensor or as a listening sensor is done by means of the parameter `configurations` as described below.

pub{
 0.name = us_reading
 0.type = ipa_odroidx_ultrasonic_interface/ExRangeArray
 0.desc = Publishes the ranges as calculated by the `us_driver` node.
}

param{
 0.name = configurations
 0.default = None
 0.type = list
 0.desc = `configurations` is an array in which each element defines a configuration which is loaded sequentially and in a loop until a new configuration is provided. Each element of the array is a dictionary where the `key` is the sensor address of a pinging sensor defined as a string and the `value` is an array of integers which specify the addresses of the listening sensors which are to be read corresponding to the pinging sensor address provided as the key. 

 1.name = debug
 1.type = boolean
 1.default = None
 1.desc = Enable it to show debug messages.
}
```

## I/O Pin Mapping on controller board

The following table summarizes the input and output connections to and
from the sensors connected to the controller board. The table is with
respect to the micro controller.

  -- -------------------- -- ---------------- -- --------------- --
     **Sensor Address**      **Output Pin**      **Input Pin**   
     0                       PA0                 PB0             
     1                       PA1                 PB1             
     2                       PA2                 PB2             
     3                       PA3                 PB3             
     4                       PA4                 PB4             
     5                       PA5                 PB6             
     6                       PA6                 PC7             
     7                       PD0                 PA7             
     8                       PD1                 PC6             
     9                       PD2                 PC5             
     10                      PD3                 PC4             
     11                      PD4                 PC3             
     12                      PD5                 PC2             
     13                      PD6                 PD7             
  -- -------------------- -- ---------------- -- --------------- --

## Usage/Examples

The `us_driver` node can be executed by: ```
roslaunch ipa_odroidx_ultrasonic_interface us_driver.launch
```

In the following example configuration yaml file, in the first cycle,
sensor '1' and '2' are set as both pinging and listening sensors,
sensors '3' and '4' listen to sensor '1' whereas '5' listens to
sensor '2'. In the second cycle, sensors '10' and '13' are set as
pinging sensors, sensors '1' and '12' listen to sensor '10' and
sensor '7' and '8' listen to sensor '13':

```highlight
configurations:
[
 {
  '1':[1,3,4],
  '2':[2,5]
 },
 {
  '10':[1,12],
  '13':[7,8]
 }
]
```
