## Documentation

This package provides various nodes to teleoperate the BipedRobin robot
by joystick. The use of a PS3 joystick is recommended but also other
joysticks can be used after some minor adoptions.

## Nodes

```clearsilver
node.0 {
name = joystick_teleop
desc = Generates desired velocities for given joystick inputs. If one wants to use different dead man keys or other axis to control the robot this node needs to be adopted
sub {
  0.name = joy
  0.type = sensor_msgs/Joy
  0.desc = Data from the joystick
}
pub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Desired velocity for !BipedRobin (x,y, theta)
}
}
node.1 {
name = biped_teleop
desc = Generates desired steps for given desired velocity. The area of allowed steps is hard coded in this node.
sub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Desired velocity for !BipedRobin (x,y, theta)
  1.name = stepsLeftInBuffer
  1.type = std_msgs/UInt8
  1.desc = Number of steps left in the step buffer of !BipedRobin. A new step will only be sent if the buffer is empty.
}
pub {
  0.name = desiredCenterPoint
  0.type = geometry_msgs/PoseStamped
  0.desc = Visualization of the desired center point of !BipedRobin (point between the two feet).
}
srv_called {
  0.name = footstep3DInc_srv
  0.type = biped_robin_msgs/StepTarget3DService
  0.desc = Service is called to pass an incremental step to the step buffer of !BipedRobin.
}
}
node.2 {
name = carrot_teleop
desc = Generates desired velocities so that the robot follows a carrot (actually a frame in the tf tree).
pub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Desired velocity for !BipedRobin (x,y, theta)
}
param {
  0.name = ~carrot_frame_id
  0.type = string
  0.desc = Frame attached to the carrot (z-direction pointing up)
  0.default = /carrot
  1.name = ~base_frame_id
  1.type = string
  1.desc = Base frame of the robot (x-axes pointing forward, z-axes pointing upwards)
  1.default = /base_footprint
  2.name = ~carrot_distance_x
  2.type = double
  2.desc = Distance the robot keeps to the carrot.
  2.default = -0.6
}
req_tf{
  0.from = carrot
  0.to   = base_footprint
  0.desc = carrot frame is set with '~carrot_frame_id' parameter, base_footprint frame is set with '~base_frame_id'.
}
}
```

## Launch Files

There are several launch files to start up the teleoperation:

-   **joystick.launch **- starts the joystick_teleop and biped_teleop
    nodes.
-   **joystick_real.launch** - like joystick.launch but also starts the
    drivers for BipedRobin
-   **joystick_simulated.launch **- like joystick.launch but also starts
    a simulation of BipedRobin.
