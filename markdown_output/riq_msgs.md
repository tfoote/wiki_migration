# Introduction

Contains ROS message definitions for communicating between RobotIQ Hand
EtherCAT driver and the ROS.

# Messages

-   RIQHandCommand : Used for sending commands to RobotIQ EtherCAT
    driver
-   RIQHandState : State of RobotIQ Hand from EtherCAT driver
-   RIQActuatorState : Part of RIQHandState. RobotIQ hand has 4
    actuators.

# Future

(Nov 9 2011) : There is discussion about creating a standard interface
to the Robotiq Adaptive Gripper using a ROS Action interface of using
ROS topics. Part of the motivation is to have stand ROS interface to
Adaptive Grippers that are using different communication back-ends
(EtherCAT, Modbus, DeviceNet, etc\...)
