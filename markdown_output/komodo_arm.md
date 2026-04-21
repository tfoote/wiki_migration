```wiki
'''Note:''' This stack is designed for robots purchased before June 2014. 
For new robots, see the [[robotican|robotican]] stack.
```

![alt text\|width=350](attachment:komodo_arm_small.png)

# Package Description

This package handle the communication and control of the komodo arm. The
package uses the dynamixel_motor stack (see
<http://www.ros.org/wiki/dynamixel_motor> for details on sending commads
to the motors and using the arm joint controllers) to setup the
communication with the arm motors and to implement the arm joint
controllers. The package also publishes sensor_msgs/JointState messages
according to the readings from the joint controllers. This conversion is
done by the states_converter.py node.

# Package Configuratoin

Package configuration files are:

○ **\\launch\\komodo_arm.launch** - The first part of this launch file
initiate the communication with the robot arm (see "port_name" parameter
for port configuration). The second part initiate the arm joint
controllers and assign each joint its name. The last part run the
state_converter.py node. This file can be launched from the main launch
file (komodo_launch.launch).

○ **\\config\\arm.yaml** - This file contains configuration details for
each joint controller. User can set joint speed, limit, max torque and
more. It is important to know that this settings are sent to the motors
upon launching the launch file and will not remain after the arm will be
power down. This is important because if the initial values of
parameters such as joint speed are high and if the user will reboot the
arm power and will not re-launch the launch file, all commands will be
performed with the initial parameters. (see
<http://www.ros.org/wiki/dynamixel_motor> for details on configuring the
controllers).
