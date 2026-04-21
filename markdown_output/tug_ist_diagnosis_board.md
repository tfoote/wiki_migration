## Overview

Diagnosis board is micro-controller based hardware embedding a TCP/IP
stack. It has low and high channels to connect low voltage and high
voltage hardware sensor devices. It is responsible for the current
measurements, the power monitoring and the power configuration of the
individual channels. The board is connected with the outside over
Ethernet and embeds a server with a proprietary protocol.

## Nodes



```clearsilver
node.0 {
name= diagnosis_board_controller
desc= This is the controller of the board. It acts like a client and communicate with board on TCP. It connects with board via ip and port.
pub{
0.name= /board_measurments
0.type= tug_ist_diagnosis_msgs/DBoardMeasurments
0.desc= This topic publishes channel measurements on ROS topic. It gives id, status (on/off), current and voltage measurements of each individual channel. 
}
param{
    0.name = ~ip
    0.type = string
    0.default = `"127.0.0.1"`
    0.desc = This is ip address of the server board. One can configuer on any usable and valid ip address provided inside robotic system.
    1.name = ~port
    1.type = int
    1.default = 5000
    1.desc = This is the port opened by the server board. One can set port id too.
}
}
node.1 {
name= virtual_diagnosis_board
desc= This node provides functionality of virtual board just for testing purpose. In reality one needs real hardware diagnosis board for real time diagnosis. This node communicates with controller on TCP so it has no publisher and subscriber. It uses ip=127.0.0.1 and port=5000.
}
node.2 {
name= node_action_server
desc= This is a node which is action server providing facility to start and stop the node(s).
}
```


