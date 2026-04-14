## Supported Hardware

This driver should work with the RS232 version of the
[Windsonic](http://www.gill.co.uk/data/datasheets/WindSonicWebDatasheet.pdf).
The RS422/485 versions are not supported by this package.

![](attachment:windsonic.jpg)

## ROS API

```clearsilver
node.0 {
name=windsonic_node
desc=`windsonic_node` is a driver for the RS232 version of the Windsonic ultrasonic wind sensor.
pub{
0.name= wind
0.type= lse_sensor_msgs/Anemometer
0.desc= Wind speed and direction data from the anemometer.
}
param {
0.name= ~port
0.default= /dev/ttyUSB0
0.type= string
0.desc= The port where the Windsonic can be found.
1.name= ~baudrate
1.default= 38400
1.type= int
1.desc= The baudrate of the Windsonic.
2.name= ~frame_id
2.default= /base_anemometer
2.type= string
2.desc= The frame id of the anemometer sensor.
}
}
```

## Communication Protocol Documentation

-   The Windsonic protocol is described in this
    [document](http://www.gill.co.uk/data/manuals/WindSonic%20GPA%20manual%201405-PS-0019%20issue%2018.pdf).
