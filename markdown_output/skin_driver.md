## Skin Driver

The skin_driver provides a high level ROS interface to easily use the
Sensor skin in ROS on your robot: It publishes a topic containing
current measurement data (used e.g. by [skin_dashboard](skin_dashboard)
or a user program) and provides a service (used by
[skin_config](skin_config)) which can be used to reconfigure the skin\'s
parameters.

On the low-level side the skin_driver uses the [sub20](sub20) driver for
the [Xdimax SUB-20 Device](http://www.xdimax.com/sub20/sub20.html) to
communicate with the skin\'s controller (called ECU) over I2C and USB as
depicted in the image below:

![](attachment:skin_driver.png)

### USB udev rules

The user running the skin_driver node needs write access to the
character device of the XDIMAX Box. In Ubuntu this can be easily
achieved by creating a custom udev rule.

The following udev rule allows write access for every user to every USB
device with the VendorID \"04d8\" and ProductID \"ffc3\" (all our XDIMAX
Boxes have these identifiers). The ids can be determined by using
\"lsusb -v\".

Open/create the file with ```
vi /etc/udev/rules.d/65-usb-xdimax.rules
``` and insert (adjust
ids if necessary) ```
# set permission to 666 for xdimax box
BUS=="usb", SYSFS{idVendor}=="04d8", SYSFS{idProduct}=="ffc3", ACTION=="add", MODE="0666"
```

Once the device is (re)plugged into an USB port the udev rule should set
the permission of the corresponding character device to 666.

## Nodes

```clearsilver
node.0{
name=skin_data_publisher
desc= The `skin_data_publisher` node interfaces with the Bosch skin ECU over I2C. The driver requires an [[http://www.xdimax.com/sub20/sub20.html|Xdimax SUB-20 Device]] to communicate with the I2C interface of the ECU. 

param {
}
pub {
  0.name= ~<name>/skin_data
  0.type= skin_driver/skin_meas
  0.desc= Raw skin measurement with configuration data
}
srv {
  0.name= ~<name>/skin_serv
  0.type= skin_driver/skin_serv
  0.desc= Reconfiguration service
}
```
