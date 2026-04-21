## Supported Hardware

This driver should works with any gps sensor

## ROS API



```clearsilver
node.0 {
name=corobot_gps
desc=`corobot_gps` is a driver for gps sensors. This driver was designed to get gps data for the Corobot.
pub{
0.name= extended_fix
0.type= corobot_msgs/GPSFix
0.desc= Send the gps data
1.name= fix
1.type= sensor_msgs/NavSatFix
1.desc= Send the gps data
}
param{
0.name= use_gps_time
0.default= true
0.type= bool
0.desc= use the time from the gps
1.name= host
1.default= localhost
1.type= string
1.desc= host name or ip address of the computer connected to the gps
2.name= port
2.default= 2947
2.type= int
2.desc= port where the gps sends data to
}
}
}
```



## Troubleshooting

Here is what you can do to configure your system to use your GPS:

First find out which port the gps used. For that, disconnect et
reconnect your gps and in a terminal type 

```
{
dmesg
```

}

Now open the file /etc/default/gpsd 

```
{
sudo gedit /etc/default/gpsd
```

} and change
the line DEVICES="" by DEVICES="/dev/ttyUSB0" making sure that the
port is the one the command dmesg gave you.

Lastely, create a rules file to get permission to use the gps device


```
{
touch /etc/udev/rules.d/corobot.rules
echo 'KERNEL=="ttyUSB0", GROUP="users", MODE="0666"' >> /etc/udev/rules.d/corobot.rules
```

} Make sure the change the port, ttyUSB0, by the
port dmesg gave you, generally in the form tty\*.

Now you just need to restart the robot.
