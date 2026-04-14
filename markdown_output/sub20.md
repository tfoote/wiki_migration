## Sub20 Library

This package builds a library which can be used from other ROS packages
to communicate over the
[Sub20 Multi Interface USB Adapter](http://www.xdimax.com/sub20/sub20.html).

For example see [bma180](bma180), [smi540](smi540), or [bmp085](bmp085).
In these packages the Sub20 device is used to communicate with an SPI or
I2C slave device.

## Sub20 Permissions

By default, the file permissions for the Sub20 device does not permit
writing. This often leads to an error of \"No Sub device found.\" or
similar. The device will be located in /dev/bus/usb/xxx/xxx, where a
chmod operation can be used.

A udev rule can also be created to permanently change the permissions.
Copy the text in the box below to the file
/etc/udev/rules.d/65-usb-xdimax.rules ```
# set permission to 666 for Sub20 device
SUBSYSTEM=="usb", ATTR{idVendor}=="04d8", ATTR{idProduct}=="ffc3", ACTION=="add", MODE="0666"
```

NB: The vendor and product IDs are case sensitive.
