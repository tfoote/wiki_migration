## Overview

The numatac_can_driver package provides a ROS interface to NumaTac
tactile sensors over a CAN interface. See
[product manual ](https://www.syntouchllc.com/Products/NumaTac/_media/NumaTac_Product_Manual.pdf)
for details.

## Bring-up

To bring up the NumaTac tactile sensors, plug in the USB connector.
Configure the CAN interface by running the following command in a
command line prompt:

`sudo ip link set can0 type can bitrate 1000000`

and finally bring-up the CAN interface using:

`sudo ifconfig can0 up`

To run the driver use:

`roslaunch numatac_can_driver numatac_can_driver.launch`

## ROS API



```clearsilver
node.0 {
name=numatac_can_node
desc=Publishes an array of containing each fingers sensor readings of fluid and dynamic pressure in Pa.
pub{
 0.name= hand_pressure
 0.type= numatac_can_driver/HandPressure
 0.desc= An array of containing each fingers sensor readings of fluid and dynamic pressure in Pa.
}
}
  param {
    0.name = ~canbus_dev
    0.type = `string`
    0.default = can0
    0.desc = The CANBUS interface.
    1.name = ~number_of_sensors
    1.type = `int`
    1.default = 3
    1.desc = The amount of NumaTac sensors on the hand/end-effector.
    2.name = ~tare
    2.type = `bool`
    2.default = false
    2.desc = The option the tare the readings based on the first reading.
  }
```


