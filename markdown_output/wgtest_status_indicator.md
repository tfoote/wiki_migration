## Overview

The `wgtest_status_indicator` package contains a driver for a
[Delcom USB indicator light](http://www.delcom-products.com/productdetails.asp?productnum=904003)
to monitor the status of [Test Manager](life_test).

{X} This tool does not work in Ubuntu 10.10 (Maverick) because
`libhid0` and/or `libhid-dev` are not available.

## Running Light Driver

To run the light driver:



```
roscd wgtest_status_indicator
sudo bash
export ROS_MASTER_URI=http://wgburn1:11311
bin/wgtest_indicator
```



**Note:** You don't have to set the `ROS_MASTER_URI` if you're
running on the same machine as Test Manager.

The driver is persistent, and will still operate if Test Manager goes
down. Notice how the driver needs to be run as root.

## Turning on the Light Manually

The utility `delcom_usb_light` can enable or disable the USB light
manually.



```
$ bin/delcom_usb_light -h
Usage: bin/delcom_usb_light [ --orange | --red | --green | --off | --get ]
```



It also must be run as root.
