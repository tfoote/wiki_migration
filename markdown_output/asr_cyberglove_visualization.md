![\|width="333",height="200"](attachment:Logo-white-medium.jpg)

## Description

The asr_cyberglove_visualization package is used to test and visualize
the functionalities of the [asr_cyberglove_lib](asr_cyberglove_lib) and
[asr_flock_of_birds](asr_flock_of_birds) packages. It uses an URDF model
of a human hand to provide a visualization of the movement data from the
gloves and the magnet tracking system (Flock of Birds) in RViz.

![\|width="690",height="389"](attachment:asr_cyberglove_visualization.jpg)

## Usage

### Needed packages

This package depends on the following packages:

-   [asr_msgs](asr_msgs) (mandatory)
-   [asr_cyberglove_lib](asr_cyberglove_lib) (optional)
-   [asr_flock_of_birds](asr_flock_of_birds) (optional)

### Needed hardware

To use im combination with [asr_cyberglove_lib](asr_cyberglove_lib) and
[asr_flock_of_birds](AsrFlockOfBirds) the following hardware components
are needed:

-   Cybergloves
-   [Ascension Technology Corp](http://www.ascension-tech.com/products/product-history/)
    magnet tracking system "Flock of Birds"

### Start system

#### Starting the servers

The main function of the package is to visualize the data received from
the hardware sensors of the Cybergloves and/or "Flock of Birds".
Therefore, the nodes of the corresponding packages asr_cyberglove_lib
and/or asr_flock_of_birds should be started first. To start the servers
directly from the PC to which the hardware is connected, use:



```
roslaunch asr_cyberglove_lib glove_lib.launch

roslaunch asr_flock_of_birds flock_of_birds.launch
```

 Alternatively, the servers can also be started
from remote if the hardware is connected to another Lab-PC:



```
rosrun asr_cyberglove_lib glove_lib_remote.sh

rosrun asr_flock_of_birds flock_of_birds_remote.sh
```



#### Starting the visualization

After the asr_cyberglove_lib and/or the asr_flock_of_birds server(s)
is/are started, the visualization in RViz can be launched with the help
of .launch-files:

-   **demo_fob.launch:** This file is used to test the right tracker of
    asr_flock_of_birds. It loads the model of the right hand, which is
    then transformed accordingly to the movements of the tracker
    received from the asr_flock_of_birds server (the asr_cyberglove_lib
    server does not need to be started)
-   **demo_glove.launch:** This file is used to test the sensors of the
    right Cyberglove. It loads the model of the right human, whose
    joints are then transformed accordingly to sensor data received from
    the asr_cyberglove_lib server (the asr_flock_of_birds server does
    not need to be started)
-   **demo_glove_fob.launch:** This file is used to test the sensors of
    the right Cyberglove in cooperation with the right tracker of
    asr_flock_of_birds. It loads the model of the right hand, which is
    then transformed accordingly to data received from the
    asr_cyberglove_lib and asr_flock_of_birds servers.
-   **demo_slider.launch:** This file is used to display the model of
    the right hand in RViz along with a slider to move the joints. The
    asr_cyberglove_lib and asr_flock_of_birds servers are not needed for
    this.
-   **demo_slider_left.launch:** Analogous to the demo_slider.launch
    file, except that the model of the left hand is displayed in RViz.

#### Configuring RViz

RViz has to be configured to show/add the !RobotModel. The RViz
configuration files located in */asr_cyberglove_visualization/rviz* can
be used when launching to provide an ideal view of the model and its
movements in RViz. They are included in the launch files.

## ROS Nodes

### Subscribed Topics

The sensor data of the Cybergloves is received as
**`'asr_msgs::!AsrGlove `**'messages published by the
asr_cyberglove_lib server. The topics to listen to are:

-   **`'/rightGloveData_radian`**'
-   **`'/leftGloveData_radian`**'

The pose data of the Flock of Birds trackers is received as
**`'asr_msgs::!AsrObject`**' messages published by the
asr_flock_of_birds server. The topic to listen to is:

-   **`'/fob_objects`**'

### Published Topics

The current Cyberglove state data is published to the model as
**`'sensor_msgs::!JointState`**' messages. They are published to the
following topic:

-   **`'/joint_states`**'

The Flock of Birds data is published using a
**`'tf::!TransformBroadcaster`**'.
