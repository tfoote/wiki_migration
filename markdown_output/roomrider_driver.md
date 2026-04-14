## The AIS Bonn Roomrider Driver

### General Information

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------------- --
     Roomrider is one of the teaching and research robot platforms at AIS Bonn. It is currently equipped with a S300 Professional laser scanner from SICK(R), a notebook for some computational power, and last but not least a Roomba530 from iRobot(R).\      ![Designed by M. Schreiber](attachment:Roomrider.png)   
     \                                                                                                                                                                                                                                                                                                                  
     This package contains a driver to control the Roomba and get all sensory information via the Roomba\'s serial interface.                                                                                                                                                                                           

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------------- --

### Getting started

Make sure that all dependencies are satisfied:

```
rosmake roomrider_driver
```

Run the node:

```
rosrun roomrider_driver roomrider_driver
```

Test your iRobot Roomba500 sensors and actuators:

```
roslaunch roomrider_driver roomrider_test.launch
```

### Messages

```clearsilver
pub {
0.name = /power
0.type = roomrider_driver/Power
0.desc = Information about current and temperature.
}
pub {
1.name = /lightsensor
1.type = roomrider_driver/Lightsensor
1.desc = Cliff and light sensors.
}
pub {
2.name = /bumper
2.type = roomrider_driver/Bumper
2.desc = Bumper sensors.
}
pub {
3.name = /wheeldrop
3.type = roomrider_driver/Wheeldrop
3.desc = Wheeldrop sensors.
}
pub {
4.name = /infrared
4.type = roomrider_driver/Infrared
4.desc = Infrared sensor for virtual wall and base.
}
pub {
5.name = /odom
5.type = nav_msgs/Odometry
5.desc = Position and velocity of roomrider in free space.
}
sub {
0.name = /cmd_vel
0.type = geometry_msgs/Twist
0.desc = Motion commands to roomrider.
}
sub {
1.name = /led
1.type = roomrider_driver/Led
1.desc = Control roomrider leds.
}
param {
0.name = ~safe_mode
0.type = int
0.desc = Roomba safe mode, otherwise full mode.
0.default = 1
1.name = ~debug_mode
1.type = int
1.desc = If set to 1, will print debug messages.
1.default = 0
2.name = ~serial_port
2.type = string
2.desc = Port connected to roomrider.
2.default = "/dev/roomba"
}
```
