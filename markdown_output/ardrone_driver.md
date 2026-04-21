## Usage

Be sure that the AR.Drone has completed it's boot sequence (indicated
by a green LED on the bottom), and that it is connected to your computer
via WiFi. Also, make sure you have plenty of room to safely fly the
AR.Drone. When using the AR.Drone, keep in mind the range of WiFi, and
the range of bluetooth.

If the AR.Drone does not receive a command for more than 250 ms, it will
enter hovering mode and remain in place. It will then wait for up to two
minutes for a re-connection, at which point an automatic landing will
occur.

`ardrone_driver` will maintain the connection automatically by sending a
specific packet approximately every 200ms.

To bring the driver online:



```
rosrun ardrone_driver ardrone_driver
```



## Controlling the AR.Drone

A `geometry_msgs/Twist` is used to control the velocity of the AR.Drone.
Four parameters of the message are currently used. All values should be
specified between 1 and -1. For the smoothest possible movement, a
`geometry_msgs/Twist` should be published at a rate of no less than
30Hz.



```
Movement is specified in meters per second. Maximum value specified should be no more than 0.8. For maximum stability while flying, a value of .5 or lower is suggested.
```



-   linear.x - (+)forward and (-)backward
-   linear.y - (+)left and (-)right
-   linear.z - (+)up and (-)down



```
Rotation is specified in radians per second.
```



-   angular.z - The rotational velocity. Causes rotation about the
    center.

## Nodes



```clearsilver
node.0 {
  name = ardrone_driver
  desc = Provides a control interface to the AR.Drone
  sub {
    0.name = cmd_vel
    0.type = geometry_msgs/Twist
  }

  pub {
    0.name = /ardrone/imu/data
    0.type = sensor_msgs/Imu
    0.desc = Imu data from the on-board sensors. 
  }

  pub {
    2.name = /ardrone/imu/is_calibrated
    2.type = std_msgs/Bool
    2.desc = Indicates that the on-board IMU has been zeroed. This happens automatically at takeoff, and can be done manually with a service call.
}

  pub {
    1.name = /ardrone/state
    1.type = ardrone_driver/ARDroneState
    1.desc = Information about the current state, including battery level and altitude. Also indicates if the AR.Drone is currently airborne.
  }

  param {
    0.name = drone_ip
    0.type = string
    0.desc = IP of the AR.Drone
    0.default = "192.168.1.1"
  }

  param {
    1.name = drone_port
    1.type = int
    1.desc = Port for AR.Drone commands
    1.default = 5556
  }
  
  param {
    2.name = tilt_max
    2.type = double
    2.desc = Maximum tilt angle for the AR.Drone. Not to exceed .52 radians. It is highly recommended that users keep this set to the default value. 
    2.default = .44
  }

  param {
    3.name = altitude_max
    3.type = double
    3.desc = Altitude limit for the AR.Drone, in meters. 10 = unlimited.
    3.default = 1
  }

  srv {
    0.name = /ardrone/takeoff
    0.type = ardrone/Takeoff
    0.desc = Causes the AR.Drone to takeoff
  }

  srv {
    1.name = /ardrone/land
    1.type = ardrone/Land
    1.desc = Causes the AR.Drone to land
  }

  srv {
    2.name = /ardrone/reset
    2.type = ardrone/Reset
    2.desc = Toggles the emergency reset flag on the AR.Drone. This can be used as both an emergency kill switch, and a reset command for an AR.Drone that is in emergency stop mode
  }

  srv {
    3.name = /ardrone/imu/calibrate
    3.type = std_srvs/Empty
    3.desc = Calibrates the on-board IMU. Use only while landed on flat ground.
```


