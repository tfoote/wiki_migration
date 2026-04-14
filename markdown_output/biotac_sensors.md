## Installation

### Cheetah USB dev rules

In order to be able to read the Biotac data via the Cheetah SPI-USB
board you first have to copy the udev rules

1\. Download the Cheetah SPI board drivers tp-usb-drivers-v2.10.zip from
<http://www.totalphase.com/products/cheetah_spi/>

2\. Unzip the folder ```
unzip tp-usb-drivers-v2.10.zip
``` 3. Copy the udev rules
```
sudo cp tp-usb-drivers-v2.10/linux/99-totalphase.rules /etc/udev/rules.d/
```

Please look at the [biotac_driver](biotac_driver) metapackage page for
more detailed installation instructions.

## Reading the Biotacs in ROS

```
roscore
   rosrun biotac_sensors biotac_pub
```

Please look at the [biotac_driver](biotac_driver) metapackage page for
more detailed instructions on how to read data from the Biotac sensors
in ROS.
