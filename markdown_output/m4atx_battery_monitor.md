## About

The \`m4atx_battery_monitor\` package will read the information from a
m4atx battery supply and publish it as a ros message.

## Nodes

```clearsilver
node.0 {
  name = m4atx_battery_monitor_node
  desc = `m4atx_battery_monitor_node` will read in the information from the m4atx and publish the information.
  pub {
    0.name = battery_status_m4atx
    0.type = 'm4atx_batter_monitor/PowerReading'
    0.desc = publishes the Power information
  }
  param {
    0.name = ~diag_frequency
    0.type = `double`
    0.default = 1.0
    0.desc = the frequency at which to poll the power supply
    1.name = ~input_nominal
    1.type = `double`
    1.default = 13.8
    1.desc = the nominal voltage when the battery supply is fully charged
    2.name = ~battery_dead_voltage
    2.type = `double`
    2.default = 10.5
    2.desc = the voltage at which the battery is considered dead (at a 0% charge)
  }
}
```

## Permissions

A startup script is provided which will perform the following commands.
```
lsusb
``` Locate the bus and device number of the device
called \"MicroChip Technology, Inc.\". ```
sudo chmod a+rw /dev/bus/usb/<bus_num>/<device_num>
``` Where
the bus_num and device_num were found above using lsusb.

## Installation

To install the \`m4atx_battery_monitor\` package, you can choose to
either install from source, or from the Ubuntu package:

### Source

To install from source, execute the following: ```shell
cd /path/to/your/catkin/workspace/src
git clone https://github.com/WPI-RAIL/m4atx_battery_monitor.git
cd /path/to/your/catkin/workspace
catkin_make 
catkin_make install
```

### Ubuntu Package

To install the Ubuntu package, execute the following:
```
sudo apt-get install ros-indigo-m4atx-battery-monitor
```

### Startup

The \`ros_ethernet_rmp\` package contains a
\`m4atx-battery-monitor.launch\` file. This file launches an instance of
the \`m4atx_battery_monitor_node\`. To launch these nodes the following
command can be used:

```
roslaunch m4atx_battery_monitor_node m4atx_battery_monitor_node.launch
```

Now the node will publish the information as well as use espeak to
inform the user of a state of charge less than or equal to 20%.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/rovio/issues). Feel
free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)
