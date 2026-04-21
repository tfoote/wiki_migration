\<\<IncludeCSTemplate(TutorialCSHeaderTemplate)\>\>

## Supported Hardware

This node is intended to work with Pluto and PlutoX drone.

## Getting Started

Use following instructions on how to use this package:

### Prerequisites

Follow this [tutorial](http://wiki.ros.org/joy) on ROS wiki and install
necessary package to use the joystick control feature of
pluto-ros-package.

### Installation

```
# Navigate to catkin workspace
roscd <WORKSPACE_NAME>

# clone repository
git clone https://github.com/DronaAviation/pluto-ros-package

# Build the Package 
catkin_make
```

## Nodes

-   **plutonode**\
    The \`plutonode\` provides a communication with Pluto/PlutoX drone

```
rosrun plutodrone plutonode
```

-   **data_via_rosservice.py**\
    This can be used to get the data from drone

```
rosrun plutoserver data_via_rosservice.py
```

-   **plutojoystick**\
    To control drone using Joystick

```
rosrun plutoserver plutojoystick
```

-   **drone_comb.launch**\
    Use this launch file of node to control drone using keyboard

```
roslaunch plutoserver drone_comb.launch
```

-   **Note**: To use Camera wifi to control drone instead of ESP wifi,
    edit following lines in
    [Communication.cpp](https://github.com/DronaAviation/pluto-ros-package/blob/master/plutodrone/src/Communication.cpp)

```
addr.sin_port = htons(CAMERA_PORT);
addr.sin_addr.s_addr = inet_addr(CAMERA_IP_ADDRESS);
```

### Topics

-   **PlutoMsg**\
    *msg/PlutoMsg*\
    RC data to control the drone

### Parameters

1\. *rcRoll*\
type = int64\
default = 1500\
rc data for roll axis ranges from 1000 to 2000

1\. *rcPitch*\
type = int64\
default = 1500\
rc data for pitch axis ranges from 1000 to 2000

1\. *rcYaw*\
type = int64\
default = 1500\
rc data for yaw axis ranges from 1000 to 2000

1\. *rcThrottle*\
type = int64\
default = 1500\
rc data for throttle axis ranges from 1000 to 2000

1\. *rcAUX1*\
type = int64\
default = 1000\
rc data for AUX1 channel ranges from 1000 to 2000

1\. *rcAUX2*\
type = int64\
default = 1000\
rc data for AUX2 channel ranges from 1000 to 2000

1\. *rcAUX3*\
type = int64\
default = 1000\
rc data for AUX3 channel ranges from 1000 to 2000

1\. *rcAUX4*\
type = int64\
default = 1000\
rc data for AUX4 channel ranges from 1000 to 2000

1\. *plutoIndex*\
type = int64\
default = 0\
pluto index number for multiple drones

### Services

-   **PlutoPilot**\
    *srv/PlutoPilot*\
    This service can be used to get data from drone

### Requests

1\. *roll*\
type = int32\
roll value from drone

1\. *pitch*\
type = int32\
pitch value from drone

1\. *yaw*\
type = int32\
yaw value from drone

1\. *accx*\
type = float32\
Acc sensor x axis value

1\. *accy*\
type = float32\
Acc sensor y axis value

1\. *accz*\
type = float32\
Acc sensor z axis value

1\. *gyrox*\
type = float32\
Gyro sensor x axis value

1\. *gyroy*\
type = float32\
Gyro sensor y axis value

1\. *gyroz*\
type = float32\
Gyro sensor z axis value

1\. *magx*\
type = float32\
Mag sensor x axis value

1\. *magY*\
type = float32\
Mag sensor y axis value

1\. *magZ*\
type = float32\
Mag sensor z axis value

1\. *alt*\
type = float32\
Alt value from drone

1\. *battery*\
type = float32\
vbat from drone

1\. *rssi*\
type = int32\
RSSI value of drone wifi

## Application

### Joystick

The package uses following axes and buttons index to control drone:\

  -- ------ -- -------------- --
     Axes      Control Type   
     2         ROLL           
     3         PITCH          
     0         YAW            
     1         THROTTLE       
     4         TRIM ROLL      
     5         TRIM PITCH     
  -- ------ -- -------------- --

  -- --------- -- ---------------------------- --
     Buttons      Control Type                 
     4            ARM or DISARM                
     3            TAKE OFF                     
     1            LAND                         
     5            SAVE TRIM ROLL, TRIM PITCH   
  -- --------- -- ---------------------------- --

-   **Note** : To change this mapping use
    [plutojoystick.h](https://github.com/DronaAviation/pluto-ros-package/blob/master/plutoserver/include/plutoserver/plutojoystick.h)

### Keyboard

The package uses following keys to control drone:\

  -- ------------- -- ------------------- --
     key              Control Type        
     spacebar         ARM or DISARM       
     w                increase THROTTLE   
     s                decrease THROTTLE   
     q                TAKE OFF            
     e                LAND                
     a                left YAW            
     d                right YAW           
     Up arrow         forward PITCH       
     Down arrow       backward PITCH      
     Left arrow       left ROLL           
     Right arrow      right ROLL          
     Ctrl-C           Quit                
  -- ------------- -- ------------------- --

### ROSTopic PlutoMsg

PlutoMsg can be used to control drone\

-   **ARM**\

```
rostopic pub /drone_command plutodrone/PlutoMsg "{rcRoll: 1500, rcPitch: 1500, rcYaw: 1500, rcThrottle: 1000, rcAUX1: 1500, rcAUX2: 1500, rcAUX3: 1500, rcAUX4: 1500}"
```

-   For more details on how to PlutoMsg to control drone use
    [link](https://github.com/DronaAviation/pluto-ros-package/blob/master/README.md)

### Multiple Drones

-   Following is the procedure to control multiple drones within the
    same network:\

1\. Setting the drone in client mode: Connect to drone wifi and use
following command to open telnet connection:\

```
telnet 192.168.4.1 // drone wifi ip
```

2\. Set the drone in both Station(STA) and Access Point Mode(AP) :\

```
+++AT MODE 3
```

3\. Set the ssid and password:\

```
+++AT STA ssid password
```

4\. Add IPs: Start hotspot and drone should connect to the hotspot. Note
the IP address assigned to it. Edit following lines in
[PlutoSwarm.cpp](https://github.com/DronaAviation/pluto-ros-package/blob/master/plutodrone/src/PlutoSwarm.cpp).
Repeat this for all new drones which are added to the network.\

```
rosrun plutodrone plutonode
```0

5\. Send data: Use PlutoMsg to send RC data to drone and add plutoIndex
in every PlutoMsg command. This index is the same as the index of the IP
within \'all_ips\' vector.\

-   **Note**: This feature is possible with ESP wifi and will not work
    over camera wifi of Pluto/PlutoX.\

## Contact

For any queries related to this package comment on
[github repo](https://github.com/DronaAviation/pluto-ros-package) or
mail on developers@dronaaviation.com

## Acknowledgments

This package is improved version of
<https://github.com/simmubhangu/pluto_drone.git>

Thanks to [e-yantra](http://www.e-yantra.org/) team for developing
original version of this package.

------------------------------------------------------------------------
