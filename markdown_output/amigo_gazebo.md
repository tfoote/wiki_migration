# Package Summary

This package contains the different controllers and launch files for the
Amigo simulation. To communicate with the gazebo simulator in real-time,
the [pr2_controller_manager](pr2_controller_manager) infrastructure is
used. A schematic overview is given in figure below:

![alt text\|width=680](http://cstwiki.wtb.tue.nl/images/Amigo_gazebo_structure.png)

The file *controller_plugins.xml* connects the libamigo_controllers
library, which includes the different controller classes, to the
[pr2_controller_manager](pr2_controller_manager). With use of the
spawner node in the [pr2_controller_manager](pr2_controller_manager)
package, instances of these controllers can be spawned that have the
possibility to communicate with the gazebo simulation.

## Controllers

Functionally the controllers manage Amigo\'s movement in simulation,
that is to make sure its movements are as fast and precise as possible
given the physical and practical limits. The controller library contains
different controller classes that are used to spawn controllers which
are configured with use of the parameter files from the package
[amigo_controller_configuration_gazebo](amigo_controller_configuration_gazebo).
The different controller classes are as follows:

```clearsilver
 name = BaseOdometry
 desc = Publishes the odometry data of Amigo.
 pub {
   0{
    name = /tf
    type = tf/tfMessage
    desc = Transformation of frame /odom to  /base_link
    }
   1{
    name = /odom
    type = nav_msgs/Odometry
    desc = Estimatation of the position and velocity of Amigo in free space
    }
  }
``` ```clearsilver
 name = BaseController
 desc = Controller that makes it possible to move the base of Amigo with use of velocity messages. It listens to twist messages and computes the efforts that needs to be put on the wheels.
 sub {
   0{
    name = /cmd_vel
    type = geometry_msgs/Twist
    desc = Input twist message for Amigo
    }
  }
```
```clearsilver
name = PositionController
desc = Generic controller which parses <<MsgLink(sensor_msgs/JointState)>> messages and calculates the torques / forces on the corresponding joints. The controller also returns the current position of the joints as <<MsgLink(sensor_msgs/JointState)>> messages. This generic controller is used as arm, gripper, spindle and head controller. 
pub {
   0{
    name = /(controller_name)/measurements
    type = sensor_msgs/JointState
    desc = Current joint states
    }
  }
 sub {
   0{
    name = /(controller_name)/references
    type = sensor_msgs/JointState
    desc = Reference joint states
    }
  }
```

Additional documentation of the c++ files can be found as doxygen at
\<INSERT LINK HERE\>

## Launch files

### start.launch

This file loads the [amigo_description](amigo_description), spawns it in
gazebo and launches the gazebo-gui. Furthermore, it starts
the [pr2_controller_manager](pr2_controller_manager) followed by the
amigo simulation controllers (controllers.launch).

### controllers.launch

This file loads the parameter files from the
[amigo_controller_configuration_gazebo](amigo_controller_configuration_gazebo)
package and spawns the following controller nodes that communicate with
the simulator via the [pr2_controller_manager](pr2_controller_manager) :

**\*Basecontroller** base_controller **\*Baseodometry** base_odometry
**\*Positioncontroller** arm_left_controller **\*Positioncontroller**
arm_right_controller **\*Positioncontroller** gripper_left_controller
**\*Positioncontroller** gripper_right_controller
**\*Positioncontroller** head_controller **\*Positioncontroller**
spindle_controller
