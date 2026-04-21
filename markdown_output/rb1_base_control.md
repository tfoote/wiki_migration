## Overview

This package contains the launch and configuration files to spawn the
joint controllers with the ROS [controller_manager](controller_manager).
It allows to launch the RB1-Base joint controllers. Besides, it will
execute a [twist_mux](twist_mux) instace in order to determine which cmd
topic will be used.

## Usage

In order to launch the rb1 controller along with the twist_mux node,
execute the following command:



```
roslaunch rb1_base_control rb1_base_control.launch
```



### Arguments

There are some arguments to keep in mind inside the launch file:

\- **sim:** (default: False) Whether we are running the simulation

\- **cmd_vel:** (default: robotnik_base_control/cmd_vel) Name of the cmd
input topic. This arg will overwrite the param with the same name
located in the config directory

\- **id_robot:** (default: robot) Name identifier of the robot. Used for
namespaces

\- **prefix:** (default: robot_) Name identifier with an underscore

\- **has_elevator:** (default: False) Whether the robot has an elevator.
This arg will overwrite the param with the same name located in the
config directory

\- **wheel_diameter:** (default: 0.1524) Indicates the diameter of the
wheel. This arg will overwrite the param with the same name located in
the config directory

## Nodes



```clearsilver
node.0 {
  name = Spawner
  desc = This spawner node from [[controller_manager]] package will spawn the robot's controller.
  sub {
    0.name = robotnik_base_control/cmd_vel
    0.type = geometry_msgs/Twist
    0.desc = Input cmd velocity
    1.name = imu/data
    1.type = sensor_msgs/Imu
    1.desc = Input imu topic used for odometry
}
  pub {
    0.name = robotnik_base_control/odom
    0.type = nav_msgs/Odometry
    0.desc = This is where the robot's odometry is being published
}

param {
  0.name = type
  0.type = string
  0.desc = Name of the controller that will be loaded in [[ros_control]]
  0.default = rb1_base_controller/RB1BaseController
}

}
node.1 {
  name = Twist Mux
  desc = This node is from [[twist_mux]] package.
}
```


